"""
Type annotations for bedrock-agent-runtime service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient
    from types_aiobotocore_bedrock_agent_runtime.paginator import (
        RetrievePaginator,
    )

    session = get_session()
    with session.create_client("bedrock-agent-runtime") as client:
        client: AgentsforBedrockRuntimeClient

        retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    KnowledgeBaseQueryTypeDef,
    KnowledgeBaseRetrievalConfigurationTypeDef,
    PaginatorConfigTypeDef,
    RetrieveResponseTypeDef,
)

__all__ = ("RetrievePaginator",)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class RetrievePaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/paginators/#retrievepaginator)
    """

    def paginate(
        self,
        *,
        knowledgeBaseId: str,
        retrievalQuery: KnowledgeBaseQueryTypeDef,
        retrievalConfiguration: KnowledgeBaseRetrievalConfigurationTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[RetrieveResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/paginators/#retrievepaginator)
        """
