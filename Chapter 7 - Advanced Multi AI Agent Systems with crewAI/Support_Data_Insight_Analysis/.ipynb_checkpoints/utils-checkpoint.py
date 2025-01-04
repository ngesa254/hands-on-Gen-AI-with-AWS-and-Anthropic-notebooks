# import os
# import boto3
# from typing import Optional
# from dotenv import load_dotenv, find_dotenv



# def get_bedrock_client(region: str = "eu-west-1") -> boto3.client:
#     """Get Bedrock runtime client"""
#     return boto3.client(
#         service_name='bedrock-runtime',  # Add service_name parameter
#         region_name=region
#     )

# def get_sonnet_config(
#     context_size: int = 4096,
#     temperature: float = 0.1,
#     top_p: float = 0.9
# ) -> dict:
#     """Get configuration for Claude 3 Sonnet"""
#     return {
#         "model": "anthropic.claude-3-sonnet-20240229-v1:0",  # Updated to Sonnet model
#         "temperature": temperature,
#         "top_p": top_p,
#         "max_tokens": context_size
#     }

# def get_haiku_config(
#     context_size: int = 4096,
#     temperature: float = 0.1,
#     top_p: float = 0.9
# ) -> dict:
#     """Get configuration for Claude 3 Haiku"""
#     return {
#         "model": "anthropic.claude-3-haiku-20240307",
#         "temperature": temperature,
#         "top_p": top_p,
#         "max_tokens": context_size
#     }


# def pretty_print_result(result):
#     parsed_result = []
#     for line in result.split('\n'):
#         if len(line) > 80:
#             words = line.split(' ')
#             new_line = ''
#             for word in words:
#                 if len(new_line) + len(word) + 1 > 80:
#                     parsed_result.append(new_line)
#                     new_line = word
#                 else:
#                     if new_line == '':
#                         new_line = word
#                     else:
#                         new_line += ' ' + word
#             parsed_result.append(new_line)
#         else:
#             parsed_result.append(line)
#     return "\n".join(parsed_result)


import os
import boto3
import logging
from typing import Optional
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

def get_bedrock_client(region: str = None) -> boto3.client:
    """Get Bedrock runtime client"""
    region = region or os.getenv("AWS_REGION", "eu-west-1")
    logging.info(f"Initializing Bedrock client for region: {region}")
    try:
        return boto3.client(
            service_name='bedrock-runtime',
            region_name=region
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Bedrock client: {e}")

def get_sonnet_config(
    context_size: int = 4096,
    temperature: float = 0.1,
    top_p: float = 0.9
) -> dict:
    """Get configuration for Claude 3 Sonnet"""
    if not (0 <= temperature <= 1):
        raise ValueError("Temperature must be between 0 and 1.")
    if not (0 <= top_p <= 1):
        raise ValueError("Top-p must be between 0 and 1.")
    return {
        "model": "anthropic.claude-3-sonnet-20240229-v1:0",
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": context_size
    }

def get_haiku_config(
    context_size: int = 4096,
    temperature: float = 0.1,
    top_p: float = 0.9
) -> dict:
    """Get configuration for Claude 3 Haiku"""
    if not (0 <= temperature <= 1):
        raise ValueError("Temperature must be between 0 and 1.")
    if not (0 <= top_p <= 1):
        raise ValueError("Top-p must be between 0 and 1.")
    return {
        "model": "anthropic.claude-3-haiku-20240307",
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": context_size
    }

def pretty_print_result(result: str, max_line_length: int = 80) -> str:
    """Pretty print the result by breaking long lines."""
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > max_line_length:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > max_line_length:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    new_line += ' ' + word if new_line else word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
