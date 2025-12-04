from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.mcp import MCPServerStdio, MCPServerHTTP
from crewai.mcp.filters import create_static_tool_filter
from typing import List
from composio import Composio
from composio_crewai import CrewAIProvider


# import agentops
import os
from dotenv import load_dotenv
load_dotenv()

google_search_key = os.getenv("GOOGLE_SEARCH_KEY")

if not google_search_key:
    raise ValueError("Missing GOOGLE_SEARCH_KEY environment variable")

# # Initialize AgentOps if API key is available
# if os.getenv("AGENTOPS_API_KEY"):
#     agentops.init(os.getenv("AGENTOPS_API_KEY"))

# notion_api_key = os.getenv("NOTION_API_KEY")
# if not notion_api_key:
#     raise ValueError("Missing NOTION_API_KEY environment variable")

user_id = os.getenv("FIRECRAWL_USER_ID")

composio = Composio(provider=CrewAIProvider())
# Get All the tools
research_agent_tools = composio.tools.get(user_id=user_id, toolkits=["FIRECRAWL"])
notion_publisher_agent_tools = composio.tools.get(user_id=user_id, toolkits=["NOTION"])

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
            tools= research_agent_tools,
            mcps=[
                # Google Search MCP - Searches web and returns URLs with snippets
                MCPServerHTTP(
                    url="https://kon-mcp-google-search-805102662749.us-central1.run.app/mcp",
                    headers={"Authorization": f"{google_search_key}"},
                    streamable=True,
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
            tools=notion_publisher_agent_tools,
            allow_delegation=False,
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
        
        