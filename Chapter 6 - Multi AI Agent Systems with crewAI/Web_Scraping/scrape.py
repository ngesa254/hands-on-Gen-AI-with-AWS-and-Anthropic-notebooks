import os
import boto3
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
import json
import nest_asyncio

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Initialize AWS Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='eu-west-1'  # replace with your AWS region if different
)

# Configuration for the SmartScraperGraph
graph_config = {
    "llm": {
        "model": "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
        "client": bedrock  # Pass the bedrock client directly
    },
    "embeddings": {
        "model": "bedrock/amazon.titan-embed-text-v2:0",
        "client": bedrock  # Pass the bedrock client directly
    }
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the products name with their price.",
    source="https://www.amazon.in/iphone/s?k=iphone",
    config=graph_config
)

# Execute the scraper and save the results to a JSON file
result = smart_scraper_graph.run()
with open("results.json", 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)

print("Scraping completed. Results saved to results.json")
