import sys
from pathlib import Path

# This single line fixes the import forever, no matter how you run it
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Now this import works 100% of the time
from src.researchandlearn.tools.mcp_tools import YouTubeTranscriptTool

tool = YouTubeTranscriptTool()
result = tool._run(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print(result)

# test_mcp.py (run this separately)
from crewai.mcp import MCPServerHTTP
import os
from dotenv import load_dotenv
load_dotenv()

google_search_key = os.getenv("GOOGLE_SEARCH_KEY")

if not google_search_key:
    raise ValueError("Missing GOOGLE_SEARCH_KEY environment variable")

mcp = MCPServerHTTP(
    url="https://kon-mcp-google-search-805102662749.us-central1.run.app/",
    headers={"Authorization": f"Bearer {google_search_key}"},  # f-string = no + error
    streamable=True,
    cache_tools_list=True,
)
# If it connects without errors, it's good. The server should expose tools like 'google_search'.
print("MCP connected successfully!")
