"""
Type annotations for kendra-ranking service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_kendra_ranking.client import KendraRankingClient

    session = get_session()
    async with session.create_client("kendra-ranking") as client:
        client: KendraRankingClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import (
    CapacityUnitsConfigurationTypeDef,
    CreateRescoreExecutionPlanResponseTypeDef,
    DescribeRescoreExecutionPlanResponseTypeDef,
    DocumentTypeDef,
    EmptyResponseMetadataTypeDef,
    ListRescoreExecutionPlansResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RescoreResultTypeDef,
    TagTypeDef,
)

__all__ = ("KendraRankingClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class KendraRankingClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KendraRankingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#close)
        """

    async def create_rescore_execution_plan(
        self,
        *,
        Name: str,
        Description: str = ...,
        CapacityUnits: CapacityUnitsConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...,
    ) -> CreateRescoreExecutionPlanResponseTypeDef:
        """
        Creates a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.create_rescore_execution_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#create_rescore_execution_plan)
        """

    async def delete_rescore_execution_plan(self, *, Id: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.delete_rescore_execution_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#delete_rescore_execution_plan)
        """

    async def describe_rescore_execution_plan(
        self, *, Id: str
    ) -> DescribeRescoreExecutionPlanResponseTypeDef:
        """
        Gets information about a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.describe_rescore_execution_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#describe_rescore_execution_plan)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#generate_presigned_url)
        """

    async def list_rescore_execution_plans(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRescoreExecutionPlansResponseTypeDef:
        """
        Lists your rescore execution plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.list_rescore_execution_plans)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#list_rescore_execution_plans)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#list_tags_for_resource)
        """

    async def rescore(
        self, *, RescoreExecutionPlanId: str, SearchQuery: str, Documents: Sequence[DocumentTypeDef]
    ) -> RescoreResultTypeDef:
        """
        Rescores or re-ranks search results from a search service such as OpenSearch
        (self
        managed).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.rescore)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#rescore)
        """

    async def tag_resource(self, *, ResourceARN: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds a specified tag to a specified rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a tag from a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#untag_resource)
        """

    async def update_rescore_execution_plan(
        self,
        *,
        Id: str,
        Name: str = ...,
        Description: str = ...,
        CapacityUnits: CapacityUnitsConfigurationTypeDef = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client.update_rescore_execution_plan)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/#update_rescore_execution_plan)
        """

    async def __aenter__(self) -> "KendraRankingClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra_ranking/client/)
        """
