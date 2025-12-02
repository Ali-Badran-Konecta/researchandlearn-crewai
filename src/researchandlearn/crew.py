from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.mcp import MCPServerStdio, MCPServerHTTP
from crewai.mcp.filters import create_static_tool_filter
from typing import List

import agentops
import os
from dotenv import load_dotenv
load_dotenv()

google_search_key = os.getenv("GOOGLE_SEARCH_KEY")

if not google_search_key:
    raise ValueError("Missing GOOGLE_SEARCH_KEY environment variable")

# Initialize AgentOps if API key is available
if os.getenv("AGENTOPS_API_KEY"):
    agentops.init(os.getenv("AGENTOPS_API_KEY"))

notion_api_key = os.getenv("NOTION_API_KEY")
if not notion_api_key:
    raise ValueError("Missing NOTION_API_KEY environment variable")

@CrewBase
class Researchandlearn():
    """Researchandlearn crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'],
            verbose=True,
            mcps=[
                # YouTube MCP - Analyzes YouTube videos and extracts transcripts
                MCPServerStdio(
                    command="docker",
                    args=[
                        "run",
                        "-i",
                        "--rm",
                        "mcp/youtube-transcript"
                    ],
                    tool_filter=create_static_tool_filter(
                        allowed_tool_names=[
                            "get_transcript",      # Gets full video transcript text
                            "get_timed_transcript", # Gets transcript with timestamps
                            "get_video_info"        # Gets video metadata (title, duration, description)
                        ]
                    ),
                    cache_tools_list=True,
                ),
                # Google Search MCP - Searches web and returns URLs with snippets
                MCPServerHTTP(
                    url="https://kon-mcp-google-search-805102662749.us-central1.run.app/mcp",
                    headers={"Authorization": f"{google_search_key}"},
                    streamable=True,
                    cache_tools_list=True,
                ),
                # Crawl4AI MCP - Extracts full content from web pages (text, code, structure)
                MCPServerHTTP(
                    url="http://0.0.0.0:8080/mcp",
                    tool_filter=create_static_tool_filter(
                        allowed_tool_names=["crawl_url"]  # Takes URL, returns full page content
                    ),
                    cache_tools_list=True,
                )
            ],
            allow_delegation=False,
        )
    
    @agent
    def content_curator_agent(self) -> Agent:
        """Knowledge Synthesizer - distills research into structured learning paths"""
        return Agent(
            config=self.agents_config['content_curator_agent'],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def tutorial_writer_agent(self) -> Agent:
        """Markdown Compiler - creates polished, study-ready tutorials"""
        return Agent(
            config=self.agents_config['tutorial_writer_agent'],
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def notion_publisher_agent(self) -> Agent:
        """Publishes the final roadmap via the Docker-hosted Notion MCP server"""
        return Agent(
            config=self.agents_config["notion_publisher_agent"],
            verbose=True,
            allow_delegation=False,
            mcps=[
                MCPServerStdio(
                    command="docker",
                    args=[
                        "run",
                        "--rm",
                        "-i",
                        "-e",
                        f"NOTION_TOKEN={notion_api_key}",
                        "mcp/notion"
                    ],
                    tool_filter=create_static_tool_filter(
                        allowed_tool_names=[
                            "API-create-a-comment",      # Notion | Create comment
                            "API-delete-a-block",        # Notion | Delete a block
                            "API-get-block-children",    # Notion | Retrieve block children
                            "API-get-self",              # Notion | Retrieve your token's bot user
                            "API-get-user",              # Notion | Retrieve a user
                            "API-get-users",             # Notion | List all users
                            "API-patch-block-children",  # Notion | Append block children
                            "API-patch-page",            # Notion | Update page properties
                            "API-post-page",             # Notion | Create a page
                            "API-post-search",           # Notion | Search by title
                            "API-retrieve-a-block",      # Notion | Retrieve a block
                            "API-retrieve-a-page",       # Notion | Retrieve a page
                            "API-retrieve-a-page-property",  # Notion | Retrieve a page property items
                        ]
                    ),
                    cache_tools_list=True,
                ),
                # HTTP/Streamable HTTP transport for remote servers
                MCPServerHTTP(
                    url="https://kon-mcp-google-search-805102662749.us-central1.run.app/mcp",
                    headers={"Authorization": f"{google_search_key}"},
                    streamable=True,
                    cache_tools_list=True,
                ),
            ],
        )
    

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def curation_task(self) -> Task:
        return Task(
            config=self.tasks_config['curation_task'],
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
        )
    
    @task
    def publishing_task(self) -> Task:
        return Task(
            config=self.tasks_config['publishing_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Researchandlearn crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            cache=False
        )
        
        