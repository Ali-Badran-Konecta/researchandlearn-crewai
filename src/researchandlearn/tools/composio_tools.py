from composio import Composio

import os
from dotenv import load_dotenv
load_dotenv()

# Get values from environment variables
firecrawl_auth_config_id = os.getenv("FIRECRAWL_AUTH_CONFIG_ID") or ""
user_id = os.getenv("FIRECRAWL_USER_ID") or ""
fire_crawl_api_key = os.getenv("FIRECRAWL_API_KEY") or ""
composio = Composio()

def authenticate_toolkit(user_id: str, auth_config_id: str, user_api_key: str):

    connection_request = composio.connected_accounts.initiate(
        user_id=user_id,
        auth_config_id=auth_config_id,
        config={"auth_scheme": "API_KEY", "val": {"generic_api_key": user_api_key}},
        allow_multiple=True

    )

    # API Key authentication is immediate - no redirect needed
    print(f"Successfully connected Firecrawl for user {user_id}")
    print(f"Connection status: {connection_request.status}")
    
    return connection_request.id

if __name__ == "__main__":
    if all([user_id, firecrawl_auth_config_id, fire_crawl_api_key]):
        connection_id = authenticate_toolkit(user_id, firecrawl_auth_config_id, fire_crawl_api_key)
        print(f"Connection ID: {connection_id}")
    else:
        print("Missing required environment variables")
