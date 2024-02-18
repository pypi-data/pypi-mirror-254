"""
Type annotations for synthetics service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_synthetics.client import SyntheticsClient

    session = get_session()
    async with session.create_client("synthetics") as client:
        client: SyntheticsClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import (
    ArtifactConfigInputTypeDef,
    CanaryCodeInputTypeDef,
    CanaryRunConfigInputTypeDef,
    CanaryScheduleInputTypeDef,
    CreateCanaryResponseTypeDef,
    CreateGroupResponseTypeDef,
    DescribeCanariesLastRunResponseTypeDef,
    DescribeCanariesResponseTypeDef,
    DescribeRuntimeVersionsResponseTypeDef,
    GetCanaryResponseTypeDef,
    GetCanaryRunsResponseTypeDef,
    GetGroupResponseTypeDef,
    ListAssociatedGroupsResponseTypeDef,
    ListGroupResourcesResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    VisualReferenceInputTypeDef,
    VpcConfigInputTypeDef,
)

__all__ = ("SyntheticsClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    RequestEntityTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SyntheticsClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SyntheticsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#exceptions)
        """

    async def associate_resource(self, *, GroupIdentifier: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Associates a canary with a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.associate_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#associate_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#close)
        """

    async def create_canary(
        self,
        *,
        Name: str,
        Code: CanaryCodeInputTypeDef,
        ArtifactS3Location: str,
        ExecutionRoleArn: str,
        Schedule: CanaryScheduleInputTypeDef,
        RuntimeVersion: str,
        RunConfig: CanaryRunConfigInputTypeDef = ...,
        SuccessRetentionPeriodInDays: int = ...,
        FailureRetentionPeriodInDays: int = ...,
        VpcConfig: VpcConfigInputTypeDef = ...,
        Tags: Mapping[str, str] = ...,
        ArtifactConfig: ArtifactConfigInputTypeDef = ...,
    ) -> CreateCanaryResponseTypeDef:
        """
        Creates a canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.create_canary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#create_canary)
        """

    async def create_group(
        self, *, Name: str, Tags: Mapping[str, str] = ...
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a group which you can use to associate canaries with each other,
        including cross-Region
        canaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.create_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#create_group)
        """

    async def delete_canary(self, *, Name: str, DeleteLambda: bool = ...) -> Dict[str, Any]:
        """
        Permanently deletes the specified canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.delete_canary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#delete_canary)
        """

    async def delete_group(self, *, GroupIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.delete_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#delete_group)
        """

    async def describe_canaries(
        self, *, NextToken: str = ..., MaxResults: int = ..., Names: Sequence[str] = ...
    ) -> DescribeCanariesResponseTypeDef:
        """
        This operation returns a list of the canaries in your account, along with full
        details about each
        canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.describe_canaries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#describe_canaries)
        """

    async def describe_canaries_last_run(
        self, *, NextToken: str = ..., MaxResults: int = ..., Names: Sequence[str] = ...
    ) -> DescribeCanariesLastRunResponseTypeDef:
        """
        Use this operation to see information from the most recent run of each canary
        that you have
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.describe_canaries_last_run)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#describe_canaries_last_run)
        """

    async def describe_runtime_versions(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeRuntimeVersionsResponseTypeDef:
        """
        Returns a list of Synthetics canary runtime versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.describe_runtime_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#describe_runtime_versions)
        """

    async def disassociate_resource(
        self, *, GroupIdentifier: str, ResourceArn: str
    ) -> Dict[str, Any]:
        """
        Removes a canary from a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.disassociate_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#disassociate_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#generate_presigned_url)
        """

    async def get_canary(self, *, Name: str) -> GetCanaryResponseTypeDef:
        """
        Retrieves complete information about one canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.get_canary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#get_canary)
        """

    async def get_canary_runs(
        self, *, Name: str, NextToken: str = ..., MaxResults: int = ...
    ) -> GetCanaryRunsResponseTypeDef:
        """
        Retrieves a list of runs for a specified canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.get_canary_runs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#get_canary_runs)
        """

    async def get_group(self, *, GroupIdentifier: str) -> GetGroupResponseTypeDef:
        """
        Returns information about one group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.get_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#get_group)
        """

    async def list_associated_groups(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListAssociatedGroupsResponseTypeDef:
        """
        Returns a list of the groups that the specified canary is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.list_associated_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#list_associated_groups)
        """

    async def list_group_resources(
        self, *, GroupIdentifier: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListGroupResourcesResponseTypeDef:
        """
        This operation returns a list of the ARNs of the canaries that are associated
        with the specified
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.list_group_resources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#list_group_resources)
        """

    async def list_groups(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListGroupsResponseTypeDef:
        """
        Returns a list of all groups in the account, displaying their names, unique
        IDs, and
        ARNs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.list_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#list_groups)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a canary or group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#list_tags_for_resource)
        """

    async def start_canary(self, *, Name: str) -> Dict[str, Any]:
        """
        Use this operation to run a canary that has already been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.start_canary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#start_canary)
        """

    async def stop_canary(self, *, Name: str) -> Dict[str, Any]:
        """
        Stops the canary to prevent all future runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.stop_canary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#stop_canary)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified canary or group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#untag_resource)
        """

    async def update_canary(
        self,
        *,
        Name: str,
        Code: CanaryCodeInputTypeDef = ...,
        ExecutionRoleArn: str = ...,
        RuntimeVersion: str = ...,
        Schedule: CanaryScheduleInputTypeDef = ...,
        RunConfig: CanaryRunConfigInputTypeDef = ...,
        SuccessRetentionPeriodInDays: int = ...,
        FailureRetentionPeriodInDays: int = ...,
        VpcConfig: VpcConfigInputTypeDef = ...,
        VisualReference: VisualReferenceInputTypeDef = ...,
        ArtifactS3Location: str = ...,
        ArtifactConfig: ArtifactConfigInputTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates the configuration of a canary that has already been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client.update_canary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/#update_canary)
        """

    async def __aenter__(self) -> "SyntheticsClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_synthetics/client/)
        """
