"""
Type annotations for support-app service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/type_defs/)

Usage::

    ```python
    from types_aiobotocore_support_app.type_defs import CreateSlackChannelConfigurationRequestRequestTypeDef

    data: CreateSlackChannelConfigurationRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

from .literals import AccountTypeType, NotificationSeverityLevelType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    "DeleteSlackWorkspaceConfigurationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ListSlackChannelConfigurationsRequestRequestTypeDef",
    "SlackChannelConfigurationTypeDef",
    "ListSlackWorkspaceConfigurationsRequestRequestTypeDef",
    "SlackWorkspaceConfigurationTypeDef",
    "PutAccountAliasRequestRequestTypeDef",
    "RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef",
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    "GetAccountAliasResultTypeDef",
    "RegisterSlackWorkspaceForOrganizationResultTypeDef",
    "UpdateSlackChannelConfigurationResultTypeDef",
    "ListSlackChannelConfigurationsResultTypeDef",
    "ListSlackWorkspaceConfigurationsResultTypeDef",
)

CreateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "channelId": str,
        "channelRoleArn": str,
        "notifyOnCaseSeverity": NotificationSeverityLevelType,
        "teamId": str,
        "channelName": NotRequired[str],
        "notifyOnAddCorrespondenceToCase": NotRequired[bool],
        "notifyOnCreateOrReopenCase": NotRequired[bool],
        "notifyOnResolveCase": NotRequired[bool],
    },
)
DeleteSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    {
        "channelId": str,
        "teamId": str,
    },
)
DeleteSlackWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSlackWorkspaceConfigurationRequestRequestTypeDef",
    {
        "teamId": str,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
ListSlackChannelConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSlackChannelConfigurationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
SlackChannelConfigurationTypeDef = TypedDict(
    "SlackChannelConfigurationTypeDef",
    {
        "channelId": str,
        "teamId": str,
        "channelName": NotRequired[str],
        "channelRoleArn": NotRequired[str],
        "notifyOnAddCorrespondenceToCase": NotRequired[bool],
        "notifyOnCaseSeverity": NotRequired[NotificationSeverityLevelType],
        "notifyOnCreateOrReopenCase": NotRequired[bool],
        "notifyOnResolveCase": NotRequired[bool],
    },
)
ListSlackWorkspaceConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSlackWorkspaceConfigurationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
SlackWorkspaceConfigurationTypeDef = TypedDict(
    "SlackWorkspaceConfigurationTypeDef",
    {
        "teamId": str,
        "allowOrganizationMemberAccount": NotRequired[bool],
        "teamName": NotRequired[str],
    },
)
PutAccountAliasRequestRequestTypeDef = TypedDict(
    "PutAccountAliasRequestRequestTypeDef",
    {
        "accountAlias": str,
    },
)
RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef = TypedDict(
    "RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef",
    {
        "teamId": str,
    },
)
UpdateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "channelId": str,
        "teamId": str,
        "channelName": NotRequired[str],
        "channelRoleArn": NotRequired[str],
        "notifyOnAddCorrespondenceToCase": NotRequired[bool],
        "notifyOnCaseSeverity": NotRequired[NotificationSeverityLevelType],
        "notifyOnCreateOrReopenCase": NotRequired[bool],
        "notifyOnResolveCase": NotRequired[bool],
    },
)
GetAccountAliasResultTypeDef = TypedDict(
    "GetAccountAliasResultTypeDef",
    {
        "accountAlias": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterSlackWorkspaceForOrganizationResultTypeDef = TypedDict(
    "RegisterSlackWorkspaceForOrganizationResultTypeDef",
    {
        "accountType": AccountTypeType,
        "teamId": str,
        "teamName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSlackChannelConfigurationResultTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationResultTypeDef",
    {
        "channelId": str,
        "channelName": str,
        "channelRoleArn": str,
        "notifyOnAddCorrespondenceToCase": bool,
        "notifyOnCaseSeverity": NotificationSeverityLevelType,
        "notifyOnCreateOrReopenCase": bool,
        "notifyOnResolveCase": bool,
        "teamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSlackChannelConfigurationsResultTypeDef = TypedDict(
    "ListSlackChannelConfigurationsResultTypeDef",
    {
        "nextToken": str,
        "slackChannelConfigurations": List[SlackChannelConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSlackWorkspaceConfigurationsResultTypeDef = TypedDict(
    "ListSlackWorkspaceConfigurationsResultTypeDef",
    {
        "nextToken": str,
        "slackWorkspaceConfigurations": List[SlackWorkspaceConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
