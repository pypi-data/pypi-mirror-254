"""
Main interface for bedrock-agent-runtime service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_bedrock_agent_runtime import (
        AgentsforBedrockRuntimeClient,
        Client,
        RetrievePaginator,
    )

    session = get_session()
    async with session.create_client("bedrock-agent-runtime") as client:
        client: AgentsforBedrockRuntimeClient
        ...


    retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

from .client import AgentsforBedrockRuntimeClient
from .paginator import RetrievePaginator

Client = AgentsforBedrockRuntimeClient

__all__ = ("AgentsforBedrockRuntimeClient", "Client", "RetrievePaginator")
