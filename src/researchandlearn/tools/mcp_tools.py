from crewai.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import subprocess
import json

class YouTubeTranscriptInput(BaseModel):
    """Input schema for YouTube Transcript Tool."""
    url: str = Field(..., description="The URL of the YouTube video")
    lang: Optional[str] = Field(None, description="The preferred language for the transcript (optional)")

class YouTubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Fetcher"
    description: str = (
        "Retrieves the full transcript of a YouTube video given its URL. "
        "Useful for analyzing video content, extracting information from educational videos, "
        "or summarizing video content without watching it."
    )
    args_schema: Type[BaseModel] = YouTubeTranscriptInput

    def _run(self, url: str, lang: Optional[str] = None) -> str:
        """Synchronous wrapper for async MCP call."""
        return asyncio.run(self._async_run(url, lang))

    async def _async_run(self, url: str, lang: Optional[str] = None) -> str:
        """Async implementation that calls the MCP server via Docker."""
        try:
            # Set up the Docker command to run the MCP server
            server_params = StdioServerParameters(
                command="docker",
                args=[
                    "run",
                    "-i",
                    "--rm",
                    "mcp/youtube-transcript"
                ]
            )

            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    # Initialize the connection
                    await session.initialize()

                    # Call the get_transcript tool
                    params = {"url": url}
                    if lang:
                        params["lang"] = lang

                    result = await session.call_tool("get_transcript", arguments=params)
                    
                    # Extract text content from result
                    if result and result.content:
                        transcript_text = ""
                        for item in result.content:
                            if hasattr(item, 'text'):
                                transcript_text += item.text + "\n" # type: ignore
                        return transcript_text.strip()
                    
                    return "No transcript found."

        except Exception as e:
            return f"Error fetching transcript: {str(e)}"


class YouTubeTimedTranscriptInput(BaseModel):
    """Input schema for YouTube Timed Transcript Tool."""
    url: str = Field(..., description="The URL of the YouTube video")
    lang: Optional[str] = Field(None, description="The preferred language for the transcript (optional)")

class YouTubeTimedTranscriptTool(BaseTool):
    name: str = "YouTube Timed Transcript Fetcher"
    description: str = (
        "Retrieves the transcript of a YouTube video WITH timestamps. "
        "Useful when you need to know at what time specific content appears in the video."
    )
    args_schema: Type[BaseModel] = YouTubeTimedTranscriptInput

    def _run(self, url: str, lang: Optional[str] = None) -> str:
        """Synchronous wrapper for async MCP call."""
        return asyncio.run(self._async_run(url, lang))

    async def _async_run(self, url: str, lang: Optional[str] = None) -> str:
        """Async implementation that calls the MCP server via Docker."""
        try:
            server_params = StdioServerParameters(
                command="docker",
                args=[
                    "run",
                    "-i",
                    "--rm",
                    "mcp/youtube-transcript"
                ]
            )

            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()

                    params = {"url": url}
                    if lang:
                        params["lang"] = lang

                    result = await session.call_tool("get_timed_transcript", arguments=params)
                    
                    if result and result.content:
                        transcript_text = ""
                        for item in result.content:
                            if hasattr(item, 'text'):
                                transcript_text += item.text + "\n" # type: ignore
                        return transcript_text.strip()
                    
                    return "No transcript found."

        except Exception as e:
            return f"Error fetching timed transcript: {str(e)}"
        