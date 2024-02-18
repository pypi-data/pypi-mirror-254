"""
Type annotations for chime-sdk-messaging service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_messaging/type_defs/)

Usage::

    ```python
    from types_aiobotocore_chime_sdk_messaging.type_defs import AppInstanceUserMembershipSummaryTypeDef

    data: AppInstanceUserMembershipSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AllowNotificationsType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageStatusType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    ErrorCodeType,
    ExpirationCriterionType,
    FallbackActionType,
    MessagingDataTypeType,
    PushNotificationTypeType,
    SearchFieldOperatorType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AppInstanceUserMembershipSummaryTypeDef",
    "AssociateChannelFlowRequestRequestTypeDef",
    "IdentityTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ChannelAssociatedWithFlowSummaryTypeDef",
    "ChannelSummaryTypeDef",
    "PushNotificationPreferencesTypeDef",
    "MessageAttributeValueTypeDef",
    "PushNotificationConfigurationTypeDef",
    "ChannelMessageStatusStructureTypeDef",
    "TargetTypeDef",
    "ElasticChannelConfigurationTypeDef",
    "ExpirationSettingsTypeDef",
    "CreateChannelBanRequestRequestTypeDef",
    "TagTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelFlowRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteMessagingStreamingConfigurationsRequestRequestTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelFlowRequestRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelMembershipRequestRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelModeratorRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DisassociateChannelFlowRequestRequestTypeDef",
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetChannelMessageStatusRequestRequestTypeDef",
    "MessagingSessionEndpointTypeDef",
    "GetMessagingStreamingConfigurationsRequestRequestTypeDef",
    "StreamingConfigurationTypeDef",
    "LambdaConfigurationTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelFlowsRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "TimestampTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListSubChannelsRequestRequestTypeDef",
    "SubChannelSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "SearchFieldTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "BatchChannelMembershipsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelFlowCallbackResponseTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelFlowResponseTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "UpdateChannelFlowResponseTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ListChannelsResponseTypeDef",
    "SearchChannelsResponseTypeDef",
    "ChannelMembershipPreferencesTypeDef",
    "ChannelMessageCallbackTypeDef",
    "GetChannelMessageStatusResponseTypeDef",
    "SendChannelMessageResponseTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "ChannelTypeDef",
    "PutChannelExpirationSettingsRequestRequestTypeDef",
    "PutChannelExpirationSettingsResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetMessagingStreamingConfigurationsResponseTypeDef",
    "PutMessagingStreamingConfigurationsRequestRequestTypeDef",
    "PutMessagingStreamingConfigurationsResponseTypeDef",
    "ProcessorConfigurationTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListSubChannelsResponseTypeDef",
    "SearchChannelsRequestRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "ListChannelBansResponseTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "GetChannelMembershipPreferencesResponseTypeDef",
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    "PutChannelMembershipPreferencesResponseTypeDef",
    "ChannelFlowCallbackRequestRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "GetChannelMessageResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "ProcessorTypeDef",
    "ChannelFlowSummaryTypeDef",
    "ChannelFlowTypeDef",
    "CreateChannelFlowRequestRequestTypeDef",
    "UpdateChannelFlowRequestRequestTypeDef",
    "ListChannelFlowsResponseTypeDef",
    "DescribeChannelFlowResponseTypeDef",
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": NotRequired[ChannelMembershipTypeType],
        "ReadMarkerTimestamp": NotRequired[datetime],
        "SubChannelId": NotRequired[str],
    },
)
AssociateChannelFlowRequestRequestTypeDef = TypedDict(
    "AssociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)
IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
BatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": Sequence[str],
        "ChimeBearer": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "SubChannelId": NotRequired[str],
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
ChannelAssociatedWithFlowSummaryTypeDef = TypedDict(
    "ChannelAssociatedWithFlowSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
    },
)
ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "LastMessageTimestamp": NotRequired[datetime],
    },
)
PushNotificationPreferencesTypeDef = TypedDict(
    "PushNotificationPreferencesTypeDef",
    {
        "AllowNotifications": AllowNotificationsType,
        "FilterRule": NotRequired[str],
    },
)
MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "StringValues": NotRequired[Sequence[str]],
    },
)
PushNotificationConfigurationTypeDef = TypedDict(
    "PushNotificationConfigurationTypeDef",
    {
        "Title": NotRequired[str],
        "Body": NotRequired[str],
        "Type": NotRequired[PushNotificationTypeType],
    },
)
ChannelMessageStatusStructureTypeDef = TypedDict(
    "ChannelMessageStatusStructureTypeDef",
    {
        "Value": NotRequired[ChannelMessageStatusType],
        "Detail": NotRequired[str],
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "MemberArn": NotRequired[str],
    },
)
ElasticChannelConfigurationTypeDef = TypedDict(
    "ElasticChannelConfigurationTypeDef",
    {
        "MaximumSubChannels": int,
        "TargetMembershipsPerSubChannel": int,
        "MinimumMembershipPercentage": int,
    },
)
ExpirationSettingsTypeDef = TypedDict(
    "ExpirationSettingsTypeDef",
    {
        "ExpirationDays": int,
        "ExpirationCriterion": ExpirationCriterionType,
    },
)
CreateChannelBanRequestRequestTypeDef = TypedDict(
    "CreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "CreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
CreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "CreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)
DeleteChannelBanRequestRequestTypeDef = TypedDict(
    "DeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)
DeleteChannelFlowRequestRequestTypeDef = TypedDict(
    "DeleteChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)
DeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "DeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
DeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "DeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
DeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "DeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
DeleteMessagingStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "DeleteMessagingStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
DescribeChannelBanRequestRequestTypeDef = TypedDict(
    "DescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)
DescribeChannelFlowRequestRequestTypeDef = TypedDict(
    "DescribeChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)
DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)
DescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)
DescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
DisassociateChannelFlowRequestRequestTypeDef = TypedDict(
    "DisassociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)
GetChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)
GetChannelMessageRequestRequestTypeDef = TypedDict(
    "GetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
GetChannelMessageStatusRequestRequestTypeDef = TypedDict(
    "GetChannelMessageStatusRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": NotRequired[str],
    },
)
GetMessagingStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "GetMessagingStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
StreamingConfigurationTypeDef = TypedDict(
    "StreamingConfigurationTypeDef",
    {
        "DataType": MessagingDataTypeType,
        "ResourceArn": str,
    },
)
LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "ResourceArn": str,
        "InvocationType": Literal["ASYNC"],
    },
)
ListChannelBansRequestRequestTypeDef = TypedDict(
    "ListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelFlowsRequestRequestTypeDef = TypedDict(
    "ListChannelFlowsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SubChannelId": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "ListChannelModeratorsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef = TypedDict(
    "ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ChimeBearer": str,
        "Privacy": NotRequired[ChannelPrivacyType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSubChannelsRequestRequestTypeDef = TypedDict(
    "ListSubChannelsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SubChannelSummaryTypeDef = TypedDict(
    "SubChannelSummaryTypeDef",
    {
        "SubChannelId": NotRequired[str],
        "MembershipCount": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
RedactChannelMessageRequestRequestTypeDef = TypedDict(
    "RedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
        "SubChannelId": NotRequired[str],
    },
)
SearchFieldTypeDef = TypedDict(
    "SearchFieldTypeDef",
    {
        "Key": Literal["MEMBERS"],
        "Values": Sequence[str],
        "Operator": SearchFieldOperatorType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "UpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": str,
        "ChimeBearer": str,
        "Metadata": NotRequired[str],
        "SubChannelId": NotRequired[str],
        "ContentType": NotRequired[str],
    },
)
UpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "Name": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Metadata": NotRequired[str],
    },
)
BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": NotRequired[IdentityTypeDef],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Members": NotRequired[List[IdentityTypeDef]],
        "ChannelArn": NotRequired[str],
        "SubChannelId": NotRequired[str],
    },
)
ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": NotRequired[IdentityTypeDef],
    },
)
ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired[IdentityTypeDef],
    },
)
ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": NotRequired[IdentityTypeDef],
    },
)
ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": NotRequired[IdentityTypeDef],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Member": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "SubChannelId": NotRequired[str],
    },
)
ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": NotRequired[IdentityTypeDef],
    },
)
ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": NotRequired[IdentityTypeDef],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired[IdentityTypeDef],
    },
)
ChannelFlowCallbackResponseTypeDef = TypedDict(
    "ChannelFlowCallbackResponseTypeDef",
    {
        "ChannelArn": str,
        "CallbackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelFlowResponseTypeDef = TypedDict(
    "CreateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": IdentityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelFlowResponseTypeDef = TypedDict(
    "UpdateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelsAssociatedWithChannelFlowResponseTypeDef = TypedDict(
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    {
        "Channels": List[ChannelAssociatedWithFlowSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired[ChannelSummaryTypeDef],
        "AppInstanceUserMembershipSummary": NotRequired[AppInstanceUserMembershipSummaryTypeDef],
    },
)
ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired[ChannelSummaryTypeDef],
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchChannelsResponseTypeDef = TypedDict(
    "SearchChannelsResponseTypeDef",
    {
        "Channels": List[ChannelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChannelMembershipPreferencesTypeDef = TypedDict(
    "ChannelMembershipPreferencesTypeDef",
    {
        "PushNotifications": NotRequired[PushNotificationPreferencesTypeDef],
    },
)
ChannelMessageCallbackTypeDef = TypedDict(
    "ChannelMessageCallbackTypeDef",
    {
        "MessageId": str,
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "PushNotification": NotRequired[PushNotificationConfigurationTypeDef],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "SubChannelId": NotRequired[str],
        "ContentType": NotRequired[str],
    },
)
GetChannelMessageStatusResponseTypeDef = TypedDict(
    "GetChannelMessageStatusResponseTypeDef",
    {
        "Status": ChannelMessageStatusStructureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": ChannelMessageStatusStructureTypeDef,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": ChannelMessageStatusStructureTypeDef,
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "Sender": NotRequired[IdentityTypeDef],
        "Redacted": NotRequired[bool],
        "Status": NotRequired[ChannelMessageStatusStructureTypeDef],
        "MessageAttributes": NotRequired[Dict[str, MessageAttributeValueTypeDef]],
        "ContentType": NotRequired[str],
        "Target": NotRequired[List[TargetTypeDef]],
    },
)
ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": NotRequired[str],
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Sender": NotRequired[IdentityTypeDef],
        "Redacted": NotRequired[bool],
        "Persistence": NotRequired[ChannelMessagePersistenceTypeType],
        "Status": NotRequired[ChannelMessageStatusStructureTypeDef],
        "MessageAttributes": NotRequired[Dict[str, MessageAttributeValueTypeDef]],
        "SubChannelId": NotRequired[str],
        "ContentType": NotRequired[str],
        "Target": NotRequired[List[TargetTypeDef]],
    },
)
SendChannelMessageRequestRequestTypeDef = TypedDict(
    "SendChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "ChimeBearer": str,
        "Metadata": NotRequired[str],
        "PushNotification": NotRequired[PushNotificationConfigurationTypeDef],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "SubChannelId": NotRequired[str],
        "ContentType": NotRequired[str],
        "Target": NotRequired[Sequence[TargetTypeDef]],
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "CreatedBy": NotRequired[IdentityTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "LastMessageTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "ChannelFlowArn": NotRequired[str],
        "ElasticChannelConfiguration": NotRequired[ElasticChannelConfigurationTypeDef],
        "ExpirationSettings": NotRequired[ExpirationSettingsTypeDef],
    },
)
PutChannelExpirationSettingsRequestRequestTypeDef = TypedDict(
    "PutChannelExpirationSettingsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
        "ExpirationSettings": NotRequired[ExpirationSettingsTypeDef],
    },
)
PutChannelExpirationSettingsResponseTypeDef = TypedDict(
    "PutChannelExpirationSettingsResponseTypeDef",
    {
        "ChannelArn": str,
        "ExpirationSettings": ExpirationSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
        "ChimeBearer": str,
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ChannelId": NotRequired[str],
        "MemberArns": NotRequired[Sequence[str]],
        "ModeratorArns": NotRequired[Sequence[str]],
        "ElasticChannelConfiguration": NotRequired[ElasticChannelConfigurationTypeDef],
        "ExpirationSettings": NotRequired[ExpirationSettingsTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {
        "Endpoint": MessagingSessionEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMessagingStreamingConfigurationsResponseTypeDef = TypedDict(
    "GetMessagingStreamingConfigurationsResponseTypeDef",
    {
        "StreamingConfigurations": List[StreamingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutMessagingStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "PutMessagingStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "StreamingConfigurations": Sequence[StreamingConfigurationTypeDef],
    },
)
PutMessagingStreamingConfigurationsResponseTypeDef = TypedDict(
    "PutMessagingStreamingConfigurationsResponseTypeDef",
    {
        "StreamingConfigurations": List[StreamingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProcessorConfigurationTypeDef = TypedDict(
    "ProcessorConfigurationTypeDef",
    {
        "Lambda": LambdaConfigurationTypeDef,
    },
)
ListChannelMessagesRequestRequestTypeDef = TypedDict(
    "ListChannelMessagesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "SortOrder": NotRequired[SortOrderType],
        "NotBefore": NotRequired[TimestampTypeDef],
        "NotAfter": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SubChannelId": NotRequired[str],
    },
)
ListSubChannelsResponseTypeDef = TypedDict(
    "ListSubChannelsResponseTypeDef",
    {
        "ChannelArn": str,
        "SubChannels": List[SubChannelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchChannelsRequestRequestTypeDef = TypedDict(
    "SearchChannelsRequestRequestTypeDef",
    {
        "Fields": Sequence[SearchFieldTypeDef],
        "ChimeBearer": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
BatchCreateChannelMembershipResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseTypeDef",
    {
        "BatchChannelMemberships": BatchChannelMembershipsTypeDef,
        "Errors": List[BatchCreateChannelMembershipErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelBans": List[ChannelBanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": ChannelBanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List[ChannelMembershipSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": ChannelMembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List[ChannelModeratorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": ChannelModeratorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": ChannelMembershipForAppInstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List[ChannelMembershipForAppInstanceUserSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": ChannelModeratedByAppInstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channels": List[ChannelModeratedByAppInstanceUserSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "GetChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "Preferences": ChannelMembershipPreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
        "Preferences": ChannelMembershipPreferencesTypeDef,
    },
)
PutChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "PutChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": IdentityTypeDef,
        "Preferences": ChannelMembershipPreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChannelFlowCallbackRequestRequestTypeDef = TypedDict(
    "ChannelFlowCallbackRequestRequestTypeDef",
    {
        "CallbackId": str,
        "ChannelArn": str,
        "ChannelMessage": ChannelMessageCallbackTypeDef,
        "DeleteResource": NotRequired[bool],
    },
)
ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelMessages": List[ChannelMessageSummaryTypeDef],
        "SubChannelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": ChannelMessageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": ChannelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProcessorTypeDef = TypedDict(
    "ProcessorTypeDef",
    {
        "Name": str,
        "Configuration": ProcessorConfigurationTypeDef,
        "ExecutionOrder": int,
        "FallbackAction": FallbackActionType,
    },
)
ChannelFlowSummaryTypeDef = TypedDict(
    "ChannelFlowSummaryTypeDef",
    {
        "ChannelFlowArn": NotRequired[str],
        "Name": NotRequired[str],
        "Processors": NotRequired[List[ProcessorTypeDef]],
    },
)
ChannelFlowTypeDef = TypedDict(
    "ChannelFlowTypeDef",
    {
        "ChannelFlowArn": NotRequired[str],
        "Processors": NotRequired[List[ProcessorTypeDef]],
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
CreateChannelFlowRequestRequestTypeDef = TypedDict(
    "CreateChannelFlowRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Processors": Sequence[ProcessorTypeDef],
        "Name": str,
        "ClientRequestToken": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateChannelFlowRequestRequestTypeDef = TypedDict(
    "UpdateChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
        "Processors": Sequence[ProcessorTypeDef],
        "Name": str,
    },
)
ListChannelFlowsResponseTypeDef = TypedDict(
    "ListChannelFlowsResponseTypeDef",
    {
        "ChannelFlows": List[ChannelFlowSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelFlowResponseTypeDef = TypedDict(
    "DescribeChannelFlowResponseTypeDef",
    {
        "ChannelFlow": ChannelFlowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
