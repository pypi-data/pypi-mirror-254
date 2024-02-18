"""
Type annotations for support-app service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_support_app.client import SupportAppClient

    session = get_session()
    async with session.create_client("support-app") as client:
        client: SupportAppClient
    ```
"""

from typing import Any, Dict, Mapping, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import NotificationSeverityLevelType
from .type_defs import (
    GetAccountAliasResultTypeDef,
    ListSlackChannelConfigurationsResultTypeDef,
    ListSlackWorkspaceConfigurationsResultTypeDef,
    RegisterSlackWorkspaceForOrganizationResultTypeDef,
    UpdateSlackChannelConfigurationResultTypeDef,
)

__all__ = ("SupportAppClient",)


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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SupportAppClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SupportAppClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#close)
        """

    async def create_slack_channel_configuration(
        self,
        *,
        channelId: str,
        channelRoleArn: str,
        notifyOnCaseSeverity: NotificationSeverityLevelType,
        teamId: str,
        channelName: str = ...,
        notifyOnAddCorrespondenceToCase: bool = ...,
        notifyOnCreateOrReopenCase: bool = ...,
        notifyOnResolveCase: bool = ...,
    ) -> Dict[str, Any]:
        """
        Creates a Slack channel configuration for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.create_slack_channel_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#create_slack_channel_configuration)
        """

    async def delete_account_alias(self) -> Dict[str, Any]:
        """
        Deletes an alias for an Amazon Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.delete_account_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#delete_account_alias)
        """

    async def delete_slack_channel_configuration(
        self, *, channelId: str, teamId: str
    ) -> Dict[str, Any]:
        """
        Deletes a Slack channel configuration from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.delete_slack_channel_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#delete_slack_channel_configuration)
        """

    async def delete_slack_workspace_configuration(self, *, teamId: str) -> Dict[str, Any]:
        """
        Deletes a Slack workspace configuration from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.delete_slack_workspace_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#delete_slack_workspace_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#generate_presigned_url)
        """

    async def get_account_alias(self) -> GetAccountAliasResultTypeDef:
        """
        Retrieves the alias from an Amazon Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.get_account_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#get_account_alias)
        """

    async def list_slack_channel_configurations(
        self, *, nextToken: str = ...
    ) -> ListSlackChannelConfigurationsResultTypeDef:
        """
        Lists the Slack channel configurations for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.list_slack_channel_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#list_slack_channel_configurations)
        """

    async def list_slack_workspace_configurations(
        self, *, nextToken: str = ...
    ) -> ListSlackWorkspaceConfigurationsResultTypeDef:
        """
        Lists the Slack workspace configurations for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.list_slack_workspace_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#list_slack_workspace_configurations)
        """

    async def put_account_alias(self, *, accountAlias: str) -> Dict[str, Any]:
        """
        Creates or updates an individual alias for each Amazon Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.put_account_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#put_account_alias)
        """

    async def register_slack_workspace_for_organization(
        self, *, teamId: str
    ) -> RegisterSlackWorkspaceForOrganizationResultTypeDef:
        """
        Registers a Slack workspace for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.register_slack_workspace_for_organization)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#register_slack_workspace_for_organization)
        """

    async def update_slack_channel_configuration(
        self,
        *,
        channelId: str,
        teamId: str,
        channelName: str = ...,
        channelRoleArn: str = ...,
        notifyOnAddCorrespondenceToCase: bool = ...,
        notifyOnCaseSeverity: NotificationSeverityLevelType = ...,
        notifyOnCreateOrReopenCase: bool = ...,
        notifyOnResolveCase: bool = ...,
    ) -> UpdateSlackChannelConfigurationResultTypeDef:
        """
        Updates the configuration for a Slack channel, such as case update
        notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client.update_slack_channel_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/#update_slack_channel_configuration)
        """

    async def __aenter__(self) -> "SupportAppClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html#SupportApp.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/client/)
        """
