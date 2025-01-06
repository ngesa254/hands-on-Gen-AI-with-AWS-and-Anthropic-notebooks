import os
import boto3
from typing import Optional

def get_bedrock_client(region: str = "eu-west-1") -> boto3.client:
    """Get Bedrock runtime client"""
    return boto3.client(
        service_name='bedrock-runtime',  # Add service_name parameter
        region_name=region
    )

def get_sonnet_config(
    context_size: int = 4096,
    temperature: float = 0.1,
    top_p: float = 0.9
) -> dict:
    """Get configuration for Claude 3 Sonnet"""
    return {
        "model": "anthropic.claude-3-sonnet-20240229-v1:0",  # Updated to Sonnet model
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
    return {
        "model": "anthropic.claude-3-haiku-20240307",
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": context_size
    }


def pretty_print_result(result):
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:
                        new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)