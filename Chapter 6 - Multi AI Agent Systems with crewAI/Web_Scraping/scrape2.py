import boto3
from scrapegraphai.graphs import SmartScraperGraph,SearchGraph

import nest_asyncio

# Apply nest_asyncio to allow nested event loops
#nest_asyncio.apply()


# Define the prompt and configuration
prompt = "What is Chioggia famous for?"



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


# Create the search graph
search_graph = SearchGraph(prompt, graph_config)

# Run the search graph
result = search_graph.run()

print(result)
