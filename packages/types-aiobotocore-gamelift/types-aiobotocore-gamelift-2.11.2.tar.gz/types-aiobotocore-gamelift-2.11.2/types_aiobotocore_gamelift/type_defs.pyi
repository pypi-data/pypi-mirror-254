"""
Type annotations for gamelift service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_gamelift/type_defs/)

Usage::

    ```python
    from types_aiobotocore_gamelift.type_defs import AcceptMatchInputRequestTypeDef

    data: AcceptMatchInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    AcceptanceTypeType,
    BackfillModeType,
    BalancingStrategyType,
    BuildStatusType,
    CertificateTypeType,
    ComparisonOperatorTypeType,
    ComputeStatusType,
    ComputeTypeType,
    EC2InstanceTypeType,
    EventCodeType,
    FilterInstanceStatusType,
    FleetStatusType,
    FleetTypeType,
    FlexMatchModeType,
    GameServerGroupDeleteOptionType,
    GameServerGroupInstanceTypeType,
    GameServerGroupStatusType,
    GameServerInstanceStatusType,
    GameServerProtectionPolicyType,
    GameServerUtilizationStatusType,
    GameSessionPlacementStateType,
    GameSessionStatusType,
    InstanceStatusType,
    IpProtocolType,
    LocationFilterType,
    MatchmakingConfigurationStatusType,
    MetricNameType,
    OperatingSystemType,
    PlayerSessionCreationPolicyType,
    PlayerSessionStatusType,
    PolicyTypeType,
    PriorityTypeType,
    ProtectionPolicyType,
    RoutingStrategyTypeType,
    ScalingAdjustmentTypeType,
    ScalingStatusTypeType,
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
    "AcceptMatchInputRequestTypeDef",
    "RoutingStrategyTypeDef",
    "AnywhereConfigurationTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BlobTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "ClaimFilterOptionTypeDef",
    "GameServerTypeDef",
    "ResponseMetadataTypeDef",
    "ComputeTypeDef",
    "TagTypeDef",
    "S3LocationTypeDef",
    "IpPermissionTypeDef",
    "LocationConfigurationTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "LocationStateTypeDef",
    "InstanceDefinitionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "GamePropertyTypeDef",
    "FilterConfigurationTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PriorityConfigurationTypeDef",
    "LocationModelTypeDef",
    "MatchmakingRuleSetTypeDef",
    "CreatePlayerSessionInputRequestTypeDef",
    "PlayerSessionTypeDef",
    "CreatePlayerSessionsInputRequestTypeDef",
    "CreateVpcPeeringAuthorizationInputRequestTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "CreateVpcPeeringConnectionInputRequestTypeDef",
    "DeleteAliasInputRequestTypeDef",
    "DeleteBuildInputRequestTypeDef",
    "DeleteFleetInputRequestTypeDef",
    "DeleteFleetLocationsInputRequestTypeDef",
    "DeleteGameServerGroupInputRequestTypeDef",
    "DeleteGameSessionQueueInputRequestTypeDef",
    "DeleteLocationInputRequestTypeDef",
    "DeleteMatchmakingConfigurationInputRequestTypeDef",
    "DeleteMatchmakingRuleSetInputRequestTypeDef",
    "DeleteScalingPolicyInputRequestTypeDef",
    "DeleteScriptInputRequestTypeDef",
    "DeleteVpcPeeringAuthorizationInputRequestTypeDef",
    "DeleteVpcPeeringConnectionInputRequestTypeDef",
    "DeregisterComputeInputRequestTypeDef",
    "DeregisterGameServerInputRequestTypeDef",
    "DescribeAliasInputRequestTypeDef",
    "DescribeBuildInputRequestTypeDef",
    "DescribeComputeInputRequestTypeDef",
    "DescribeEC2InstanceLimitsInputRequestTypeDef",
    "EC2InstanceLimitTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeFleetAttributesInputRequestTypeDef",
    "DescribeFleetCapacityInputRequestTypeDef",
    "TimestampTypeDef",
    "EventTypeDef",
    "DescribeFleetLocationAttributesInputRequestTypeDef",
    "DescribeFleetLocationCapacityInputRequestTypeDef",
    "DescribeFleetLocationUtilizationInputRequestTypeDef",
    "FleetUtilizationTypeDef",
    "DescribeFleetPortSettingsInputRequestTypeDef",
    "DescribeFleetUtilizationInputRequestTypeDef",
    "DescribeGameServerGroupInputRequestTypeDef",
    "DescribeGameServerInputRequestTypeDef",
    "DescribeGameServerInstancesInputRequestTypeDef",
    "GameServerInstanceTypeDef",
    "DescribeGameSessionDetailsInputRequestTypeDef",
    "DescribeGameSessionPlacementInputRequestTypeDef",
    "DescribeGameSessionQueuesInputRequestTypeDef",
    "DescribeGameSessionsInputRequestTypeDef",
    "DescribeInstancesInputRequestTypeDef",
    "InstanceTypeDef",
    "DescribeMatchmakingConfigurationsInputRequestTypeDef",
    "DescribeMatchmakingInputRequestTypeDef",
    "DescribeMatchmakingRuleSetsInputRequestTypeDef",
    "DescribePlayerSessionsInputRequestTypeDef",
    "DescribeRuntimeConfigurationInputRequestTypeDef",
    "DescribeScalingPoliciesInputRequestTypeDef",
    "DescribeScriptInputRequestTypeDef",
    "DescribeVpcPeeringConnectionsInputRequestTypeDef",
    "DesiredPlayerSessionTypeDef",
    "EC2InstanceCountsTypeDef",
    "FilterConfigurationPaginatorTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "MatchedPlayerSessionTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyTypeDef",
    "PriorityConfigurationPaginatorTypeDef",
    "GetComputeAccessInputRequestTypeDef",
    "GetComputeAuthTokenInputRequestTypeDef",
    "GetGameSessionLogUrlInputRequestTypeDef",
    "GetInstanceAccessInputRequestTypeDef",
    "InstanceCredentialsTypeDef",
    "ListAliasesInputRequestTypeDef",
    "ListBuildsInputRequestTypeDef",
    "ListComputeInputRequestTypeDef",
    "ListFleetsInputRequestTypeDef",
    "ListGameServerGroupsInputRequestTypeDef",
    "ListGameServersInputRequestTypeDef",
    "ListLocationsInputRequestTypeDef",
    "ListScriptsInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TargetConfigurationTypeDef",
    "RegisterComputeInputRequestTypeDef",
    "RegisterGameServerInputRequestTypeDef",
    "RequestUploadCredentialsInputRequestTypeDef",
    "ResolveAliasInputRequestTypeDef",
    "ResumeGameServerGroupInputRequestTypeDef",
    "ServerProcessTypeDef",
    "SearchGameSessionsInputRequestTypeDef",
    "StartFleetActionsInputRequestTypeDef",
    "StopFleetActionsInputRequestTypeDef",
    "StopGameSessionPlacementInputRequestTypeDef",
    "StopMatchmakingInputRequestTypeDef",
    "SuspendGameServerGroupInputRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBuildInputRequestTypeDef",
    "UpdateFleetCapacityInputRequestTypeDef",
    "UpdateGameServerInputRequestTypeDef",
    "ValidateMatchmakingRuleSetInputRequestTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "AliasTypeDef",
    "UpdateAliasInputRequestTypeDef",
    "PlayerTypeDef",
    "ClaimGameServerInputRequestTypeDef",
    "ClaimGameServerOutputTypeDef",
    "DescribeBuildOutputTypeDef",
    "DescribeGameServerOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetComputeAccessOutputTypeDef",
    "GetComputeAuthTokenOutputTypeDef",
    "GetGameSessionLogUrlOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServersOutputTypeDef",
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerOutputTypeDef",
    "ResolveAliasOutputTypeDef",
    "StartFleetActionsOutputTypeDef",
    "StopFleetActionsOutputTypeDef",
    "UpdateBuildOutputTypeDef",
    "UpdateFleetAttributesOutputTypeDef",
    "UpdateFleetCapacityOutputTypeDef",
    "UpdateFleetPortSettingsOutputTypeDef",
    "UpdateGameServerOutputTypeDef",
    "ValidateMatchmakingRuleSetOutputTypeDef",
    "DescribeComputeOutputTypeDef",
    "ListComputeOutputTypeDef",
    "RegisterComputeOutputTypeDef",
    "CreateAliasInputRequestTypeDef",
    "CreateLocationInputRequestTypeDef",
    "CreateMatchmakingRuleSetInputRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateBuildInputRequestTypeDef",
    "CreateBuildOutputTypeDef",
    "CreateScriptInputRequestTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ScriptTypeDef",
    "UpdateScriptInputRequestTypeDef",
    "DescribeFleetPortSettingsOutputTypeDef",
    "UpdateFleetPortSettingsInputRequestTypeDef",
    "CreateFleetLocationsInputRequestTypeDef",
    "FleetAttributesTypeDef",
    "UpdateFleetAttributesInputRequestTypeDef",
    "CreateFleetLocationsOutputTypeDef",
    "DeleteFleetLocationsOutputTypeDef",
    "LocationAttributesTypeDef",
    "GameServerGroupTypeDef",
    "UpdateGameServerGroupInputRequestTypeDef",
    "CreateGameSessionInputRequestTypeDef",
    "CreateMatchmakingConfigurationInputRequestTypeDef",
    "GameSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "UpdateGameSessionInputRequestTypeDef",
    "UpdateMatchmakingConfigurationInputRequestTypeDef",
    "CreateGameSessionQueueInputRequestTypeDef",
    "GameSessionQueueTypeDef",
    "UpdateGameSessionQueueInputRequestTypeDef",
    "CreateLocationOutputTypeDef",
    "ListLocationsOutputTypeDef",
    "CreateMatchmakingRuleSetOutputTypeDef",
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    "CreatePlayerSessionOutputTypeDef",
    "CreatePlayerSessionsOutputTypeDef",
    "DescribePlayerSessionsOutputTypeDef",
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    "DescribeEC2InstanceLimitsOutputTypeDef",
    "DescribeFleetAttributesInputDescribeFleetAttributesPaginateTypeDef",
    "DescribeFleetCapacityInputDescribeFleetCapacityPaginateTypeDef",
    "DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateTypeDef",
    "DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateTypeDef",
    "DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateTypeDef",
    "DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateTypeDef",
    "DescribeGameSessionsInputDescribeGameSessionsPaginateTypeDef",
    "DescribeInstancesInputDescribeInstancesPaginateTypeDef",
    "DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateTypeDef",
    "DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateTypeDef",
    "DescribePlayerSessionsInputDescribePlayerSessionsPaginateTypeDef",
    "DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateTypeDef",
    "ListAliasesInputListAliasesPaginateTypeDef",
    "ListBuildsInputListBuildsPaginateTypeDef",
    "ListComputeInputListComputePaginateTypeDef",
    "ListFleetsInputListFleetsPaginateTypeDef",
    "ListGameServerGroupsInputListGameServerGroupsPaginateTypeDef",
    "ListGameServersInputListGameServersPaginateTypeDef",
    "ListLocationsInputListLocationsPaginateTypeDef",
    "ListScriptsInputListScriptsPaginateTypeDef",
    "SearchGameSessionsInputSearchGameSessionsPaginateTypeDef",
    "DescribeFleetEventsInputDescribeFleetEventsPaginateTypeDef",
    "DescribeFleetEventsInputRequestTypeDef",
    "DescribeFleetEventsOutputTypeDef",
    "DescribeFleetLocationUtilizationOutputTypeDef",
    "DescribeFleetUtilizationOutputTypeDef",
    "DescribeGameServerInstancesOutputTypeDef",
    "DescribeInstancesOutputTypeDef",
    "FleetCapacityTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionPlacementTypeDef",
    "StartGameSessionPlacementInputRequestTypeDef",
    "GameSessionQueuePaginatorTypeDef",
    "InstanceAccessTypeDef",
    "PutScalingPolicyInputRequestTypeDef",
    "ScalingPolicyTypeDef",
    "RuntimeConfigurationTypeDef",
    "VpcPeeringConnectionTypeDef",
    "CreateAliasOutputTypeDef",
    "DescribeAliasOutputTypeDef",
    "ListAliasesOutputTypeDef",
    "UpdateAliasOutputTypeDef",
    "StartMatchBackfillInputRequestTypeDef",
    "StartMatchmakingInputRequestTypeDef",
    "CreateScriptOutputTypeDef",
    "DescribeScriptOutputTypeDef",
    "ListScriptsOutputTypeDef",
    "UpdateScriptOutputTypeDef",
    "CreateFleetOutputTypeDef",
    "DescribeFleetAttributesOutputTypeDef",
    "DescribeFleetLocationAttributesOutputTypeDef",
    "CreateGameServerGroupOutputTypeDef",
    "DeleteGameServerGroupOutputTypeDef",
    "DescribeGameServerGroupOutputTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ResumeGameServerGroupOutputTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "UpdateGameServerGroupOutputTypeDef",
    "CreateGameSessionOutputTypeDef",
    "DescribeGameSessionsOutputTypeDef",
    "GameSessionDetailTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "UpdateGameSessionOutputTypeDef",
    "CreateMatchmakingConfigurationOutputTypeDef",
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    "UpdateMatchmakingConfigurationOutputTypeDef",
    "CreateGameSessionQueueOutputTypeDef",
    "DescribeGameSessionQueuesOutputTypeDef",
    "UpdateGameSessionQueueOutputTypeDef",
    "DescribeFleetCapacityOutputTypeDef",
    "DescribeFleetLocationCapacityOutputTypeDef",
    "CreateGameServerGroupInputRequestTypeDef",
    "MatchmakingTicketTypeDef",
    "DescribeGameSessionPlacementOutputTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "DescribeGameSessionQueuesOutputPaginatorTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "DescribeScalingPoliciesOutputTypeDef",
    "CreateFleetInputRequestTypeDef",
    "DescribeRuntimeConfigurationOutputTypeDef",
    "UpdateRuntimeConfigurationInputRequestTypeDef",
    "UpdateRuntimeConfigurationOutputTypeDef",
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    "DescribeGameSessionDetailsOutputTypeDef",
    "DescribeMatchmakingOutputTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingOutputTypeDef",
)

AcceptMatchInputRequestTypeDef = TypedDict(
    "AcceptMatchInputRequestTypeDef",
    {
        "TicketId": str,
        "PlayerIds": Sequence[str],
        "AcceptanceType": AcceptanceTypeType,
    },
)
RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {
        "Type": NotRequired[RoutingStrategyTypeType],
        "FleetId": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AnywhereConfigurationTypeDef = TypedDict(
    "AnywhereConfigurationTypeDef",
    {
        "Cost": str,
    },
)
AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": NotRequired[str],
        "N": NotRequired[float],
        "SL": NotRequired[List[str]],
        "SDM": NotRequired[Dict[str, float]],
    },
)
AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "SecretAccessKey": NotRequired[str],
        "SessionToken": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "BuildId": NotRequired[str],
        "BuildArn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Status": NotRequired[BuildStatusType],
        "SizeOnDisk": NotRequired[int],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "CreationTime": NotRequired[datetime],
        "ServerSdkVersion": NotRequired[str],
    },
)
CertificateConfigurationTypeDef = TypedDict(
    "CertificateConfigurationTypeDef",
    {
        "CertificateType": CertificateTypeType,
    },
)
ClaimFilterOptionTypeDef = TypedDict(
    "ClaimFilterOptionTypeDef",
    {
        "InstanceStatuses": NotRequired[Sequence[FilterInstanceStatusType]],
    },
)
GameServerTypeDef = TypedDict(
    "GameServerTypeDef",
    {
        "GameServerGroupName": NotRequired[str],
        "GameServerGroupArn": NotRequired[str],
        "GameServerId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "ConnectionInfo": NotRequired[str],
        "GameServerData": NotRequired[str],
        "ClaimStatus": NotRequired[Literal["CLAIMED"]],
        "UtilizationStatus": NotRequired[GameServerUtilizationStatusType],
        "RegistrationTime": NotRequired[datetime],
        "LastClaimTime": NotRequired[datetime],
        "LastHealthCheckTime": NotRequired[datetime],
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
ComputeTypeDef = TypedDict(
    "ComputeTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "ComputeName": NotRequired[str],
        "ComputeArn": NotRequired[str],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "ComputeStatus": NotRequired[ComputeStatusType],
        "Location": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Type": NotRequired[EC2InstanceTypeType],
        "GameLiftServiceSdkEndpoint": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ObjectVersion": NotRequired[str],
    },
)
IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "IpRange": str,
        "Protocol": IpProtocolType,
    },
)
LocationConfigurationTypeDef = TypedDict(
    "LocationConfigurationTypeDef",
    {
        "Location": str,
    },
)
ResourceCreationLimitPolicyTypeDef = TypedDict(
    "ResourceCreationLimitPolicyTypeDef",
    {
        "NewGameSessionsPerCreator": NotRequired[int],
        "PolicyPeriodInMinutes": NotRequired[int],
    },
)
LocationStateTypeDef = TypedDict(
    "LocationStateTypeDef",
    {
        "Location": NotRequired[str],
        "Status": NotRequired[FleetStatusType],
    },
)
InstanceDefinitionTypeDef = TypedDict(
    "InstanceDefinitionTypeDef",
    {
        "InstanceType": GameServerGroupInstanceTypeType,
        "WeightedCapacity": NotRequired[str],
    },
)
LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
GamePropertyTypeDef = TypedDict(
    "GamePropertyTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef",
    {
        "AllowedLocations": NotRequired[Sequence[str]],
    },
)
GameSessionQueueDestinationTypeDef = TypedDict(
    "GameSessionQueueDestinationTypeDef",
    {
        "DestinationArn": NotRequired[str],
    },
)
PlayerLatencyPolicyTypeDef = TypedDict(
    "PlayerLatencyPolicyTypeDef",
    {
        "MaximumIndividualPlayerLatencyMilliseconds": NotRequired[int],
        "PolicyDurationSeconds": NotRequired[int],
    },
)
PriorityConfigurationTypeDef = TypedDict(
    "PriorityConfigurationTypeDef",
    {
        "PriorityOrder": NotRequired[Sequence[PriorityTypeType]],
        "LocationOrder": NotRequired[Sequence[str]],
    },
)
LocationModelTypeDef = TypedDict(
    "LocationModelTypeDef",
    {
        "LocationName": NotRequired[str],
        "LocationArn": NotRequired[str],
    },
)
MatchmakingRuleSetTypeDef = TypedDict(
    "MatchmakingRuleSetTypeDef",
    {
        "RuleSetBody": str,
        "RuleSetName": NotRequired[str],
        "RuleSetArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)
CreatePlayerSessionInputRequestTypeDef = TypedDict(
    "CreatePlayerSessionInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerId": str,
        "PlayerData": NotRequired[str],
    },
)
PlayerSessionTypeDef = TypedDict(
    "PlayerSessionTypeDef",
    {
        "PlayerSessionId": NotRequired[str],
        "PlayerId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "TerminationTime": NotRequired[datetime],
        "Status": NotRequired[PlayerSessionStatusType],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "PlayerData": NotRequired[str],
    },
)
CreatePlayerSessionsInputRequestTypeDef = TypedDict(
    "CreatePlayerSessionsInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerIds": Sequence[str],
        "PlayerDataMap": NotRequired[Mapping[str, str]],
    },
)
CreateVpcPeeringAuthorizationInputRequestTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationInputRequestTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)
VpcPeeringAuthorizationTypeDef = TypedDict(
    "VpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": NotRequired[str],
        "PeerVpcAwsAccountId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
    },
)
CreateVpcPeeringConnectionInputRequestTypeDef = TypedDict(
    "CreateVpcPeeringConnectionInputRequestTypeDef",
    {
        "FleetId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
    },
)
DeleteAliasInputRequestTypeDef = TypedDict(
    "DeleteAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)
DeleteBuildInputRequestTypeDef = TypedDict(
    "DeleteBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)
DeleteFleetInputRequestTypeDef = TypedDict(
    "DeleteFleetInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
DeleteFleetLocationsInputRequestTypeDef = TypedDict(
    "DeleteFleetLocationsInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": Sequence[str],
    },
)
DeleteGameServerGroupInputRequestTypeDef = TypedDict(
    "DeleteGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "DeleteOption": NotRequired[GameServerGroupDeleteOptionType],
    },
)
DeleteGameSessionQueueInputRequestTypeDef = TypedDict(
    "DeleteGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteLocationInputRequestTypeDef = TypedDict(
    "DeleteLocationInputRequestTypeDef",
    {
        "LocationName": str,
    },
)
DeleteMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "DeleteMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "DeleteMatchmakingRuleSetInputRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteScalingPolicyInputRequestTypeDef = TypedDict(
    "DeleteScalingPolicyInputRequestTypeDef",
    {
        "Name": str,
        "FleetId": str,
    },
)
DeleteScriptInputRequestTypeDef = TypedDict(
    "DeleteScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)
DeleteVpcPeeringAuthorizationInputRequestTypeDef = TypedDict(
    "DeleteVpcPeeringAuthorizationInputRequestTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)
DeleteVpcPeeringConnectionInputRequestTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionInputRequestTypeDef",
    {
        "FleetId": str,
        "VpcPeeringConnectionId": str,
    },
)
DeregisterComputeInputRequestTypeDef = TypedDict(
    "DeregisterComputeInputRequestTypeDef",
    {
        "FleetId": str,
        "ComputeName": str,
    },
)
DeregisterGameServerInputRequestTypeDef = TypedDict(
    "DeregisterGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)
DescribeAliasInputRequestTypeDef = TypedDict(
    "DescribeAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)
DescribeBuildInputRequestTypeDef = TypedDict(
    "DescribeBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)
DescribeComputeInputRequestTypeDef = TypedDict(
    "DescribeComputeInputRequestTypeDef",
    {
        "FleetId": str,
        "ComputeName": str,
    },
)
DescribeEC2InstanceLimitsInputRequestTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsInputRequestTypeDef",
    {
        "EC2InstanceType": NotRequired[EC2InstanceTypeType],
        "Location": NotRequired[str],
    },
)
EC2InstanceLimitTypeDef = TypedDict(
    "EC2InstanceLimitTypeDef",
    {
        "EC2InstanceType": NotRequired[EC2InstanceTypeType],
        "CurrentInstances": NotRequired[int],
        "InstanceLimit": NotRequired[int],
        "Location": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
DescribeFleetAttributesInputRequestTypeDef = TypedDict(
    "DescribeFleetAttributesInputRequestTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFleetCapacityInputRequestTypeDef = TypedDict(
    "DescribeFleetCapacityInputRequestTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "EventCode": NotRequired[EventCodeType],
        "Message": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "PreSignedLogUrl": NotRequired[str],
    },
)
DescribeFleetLocationAttributesInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationAttributesInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFleetLocationCapacityInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationCapacityInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)
DescribeFleetLocationUtilizationInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)
FleetUtilizationTypeDef = TypedDict(
    "FleetUtilizationTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "ActiveServerProcessCount": NotRequired[int],
        "ActiveGameSessionCount": NotRequired[int],
        "CurrentPlayerSessionCount": NotRequired[int],
        "MaximumPlayerSessionCount": NotRequired[int],
        "Location": NotRequired[str],
    },
)
DescribeFleetPortSettingsInputRequestTypeDef = TypedDict(
    "DescribeFleetPortSettingsInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": NotRequired[str],
    },
)
DescribeFleetUtilizationInputRequestTypeDef = TypedDict(
    "DescribeFleetUtilizationInputRequestTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeGameServerGroupInputRequestTypeDef = TypedDict(
    "DescribeGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)
DescribeGameServerInputRequestTypeDef = TypedDict(
    "DescribeGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)
DescribeGameServerInstancesInputRequestTypeDef = TypedDict(
    "DescribeGameServerInstancesInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GameServerInstanceTypeDef = TypedDict(
    "GameServerInstanceTypeDef",
    {
        "GameServerGroupName": NotRequired[str],
        "GameServerGroupArn": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceStatus": NotRequired[GameServerInstanceStatusType],
    },
)
DescribeGameSessionDetailsInputRequestTypeDef = TypedDict(
    "DescribeGameSessionDetailsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "StatusFilter": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeGameSessionPlacementInputRequestTypeDef = TypedDict(
    "DescribeGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
    },
)
DescribeGameSessionQueuesInputRequestTypeDef = TypedDict(
    "DescribeGameSessionQueuesInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeGameSessionsInputRequestTypeDef = TypedDict(
    "DescribeGameSessionsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "StatusFilter": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstancesInputRequestTypeDef = TypedDict(
    "DescribeInstancesInputRequestTypeDef",
    {
        "FleetId": str,
        "InstanceId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "Location": NotRequired[str],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Type": NotRequired[EC2InstanceTypeType],
        "Status": NotRequired[InstanceStatusType],
        "CreationTime": NotRequired[datetime],
        "Location": NotRequired[str],
    },
)
DescribeMatchmakingConfigurationsInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "RuleSetName": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeMatchmakingInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingInputRequestTypeDef",
    {
        "TicketIds": Sequence[str],
    },
)
DescribeMatchmakingRuleSetsInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribePlayerSessionsInputRequestTypeDef = TypedDict(
    "DescribePlayerSessionsInputRequestTypeDef",
    {
        "GameSessionId": NotRequired[str],
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
        "PlayerSessionStatusFilter": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeRuntimeConfigurationInputRequestTypeDef = TypedDict(
    "DescribeRuntimeConfigurationInputRequestTypeDef",
    {
        "FleetId": str,
    },
)
DescribeScalingPoliciesInputRequestTypeDef = TypedDict(
    "DescribeScalingPoliciesInputRequestTypeDef",
    {
        "FleetId": str,
        "StatusFilter": NotRequired[ScalingStatusTypeType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "Location": NotRequired[str],
    },
)
DescribeScriptInputRequestTypeDef = TypedDict(
    "DescribeScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)
DescribeVpcPeeringConnectionsInputRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
    },
)
DesiredPlayerSessionTypeDef = TypedDict(
    "DesiredPlayerSessionTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerData": NotRequired[str],
    },
)
EC2InstanceCountsTypeDef = TypedDict(
    "EC2InstanceCountsTypeDef",
    {
        "DESIRED": NotRequired[int],
        "MINIMUM": NotRequired[int],
        "MAXIMUM": NotRequired[int],
        "PENDING": NotRequired[int],
        "ACTIVE": NotRequired[int],
        "IDLE": NotRequired[int],
        "TERMINATING": NotRequired[int],
    },
)
FilterConfigurationPaginatorTypeDef = TypedDict(
    "FilterConfigurationPaginatorTypeDef",
    {
        "AllowedLocations": NotRequired[List[str]],
    },
)
TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)
MatchedPlayerSessionTypeDef = TypedDict(
    "MatchedPlayerSessionTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
    },
)
PlacedPlayerSessionTypeDef = TypedDict(
    "PlacedPlayerSessionTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
    },
)
PlayerLatencyTypeDef = TypedDict(
    "PlayerLatencyTypeDef",
    {
        "PlayerId": NotRequired[str],
        "RegionIdentifier": NotRequired[str],
        "LatencyInMilliseconds": NotRequired[float],
    },
)
PriorityConfigurationPaginatorTypeDef = TypedDict(
    "PriorityConfigurationPaginatorTypeDef",
    {
        "PriorityOrder": NotRequired[List[PriorityTypeType]],
        "LocationOrder": NotRequired[List[str]],
    },
)
GetComputeAccessInputRequestTypeDef = TypedDict(
    "GetComputeAccessInputRequestTypeDef",
    {
        "FleetId": str,
        "ComputeName": str,
    },
)
GetComputeAuthTokenInputRequestTypeDef = TypedDict(
    "GetComputeAuthTokenInputRequestTypeDef",
    {
        "FleetId": str,
        "ComputeName": str,
    },
)
GetGameSessionLogUrlInputRequestTypeDef = TypedDict(
    "GetGameSessionLogUrlInputRequestTypeDef",
    {
        "GameSessionId": str,
    },
)
GetInstanceAccessInputRequestTypeDef = TypedDict(
    "GetInstanceAccessInputRequestTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
    },
)
InstanceCredentialsTypeDef = TypedDict(
    "InstanceCredentialsTypeDef",
    {
        "UserName": NotRequired[str],
        "Secret": NotRequired[str],
    },
)
ListAliasesInputRequestTypeDef = TypedDict(
    "ListAliasesInputRequestTypeDef",
    {
        "RoutingStrategyType": NotRequired[RoutingStrategyTypeType],
        "Name": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListBuildsInputRequestTypeDef = TypedDict(
    "ListBuildsInputRequestTypeDef",
    {
        "Status": NotRequired[BuildStatusType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListComputeInputRequestTypeDef = TypedDict(
    "ListComputeInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFleetsInputRequestTypeDef = TypedDict(
    "ListFleetsInputRequestTypeDef",
    {
        "BuildId": NotRequired[str],
        "ScriptId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGameServerGroupsInputRequestTypeDef = TypedDict(
    "ListGameServerGroupsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGameServersInputRequestTypeDef = TypedDict(
    "ListGameServersInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "SortOrder": NotRequired[SortOrderType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLocationsInputRequestTypeDef = TypedDict(
    "ListLocationsInputRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[LocationFilterType]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListScriptsInputRequestTypeDef = TypedDict(
    "ListScriptsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)
RegisterComputeInputRequestTypeDef = TypedDict(
    "RegisterComputeInputRequestTypeDef",
    {
        "FleetId": str,
        "ComputeName": str,
        "CertificatePath": NotRequired[str],
        "DnsName": NotRequired[str],
        "IpAddress": NotRequired[str],
        "Location": NotRequired[str],
    },
)
RegisterGameServerInputRequestTypeDef = TypedDict(
    "RegisterGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
        "InstanceId": str,
        "ConnectionInfo": NotRequired[str],
        "GameServerData": NotRequired[str],
    },
)
RequestUploadCredentialsInputRequestTypeDef = TypedDict(
    "RequestUploadCredentialsInputRequestTypeDef",
    {
        "BuildId": str,
    },
)
ResolveAliasInputRequestTypeDef = TypedDict(
    "ResolveAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)
ResumeGameServerGroupInputRequestTypeDef = TypedDict(
    "ResumeGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "ResumeActions": Sequence[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)
ServerProcessTypeDef = TypedDict(
    "ServerProcessTypeDef",
    {
        "LaunchPath": str,
        "ConcurrentExecutions": int,
        "Parameters": NotRequired[str],
    },
)
SearchGameSessionsInputRequestTypeDef = TypedDict(
    "SearchGameSessionsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "SortExpression": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StartFleetActionsInputRequestTypeDef = TypedDict(
    "StartFleetActionsInputRequestTypeDef",
    {
        "FleetId": str,
        "Actions": Sequence[Literal["AUTO_SCALING"]],
        "Location": NotRequired[str],
    },
)
StopFleetActionsInputRequestTypeDef = TypedDict(
    "StopFleetActionsInputRequestTypeDef",
    {
        "FleetId": str,
        "Actions": Sequence[Literal["AUTO_SCALING"]],
        "Location": NotRequired[str],
    },
)
StopGameSessionPlacementInputRequestTypeDef = TypedDict(
    "StopGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
    },
)
StopMatchmakingInputRequestTypeDef = TypedDict(
    "StopMatchmakingInputRequestTypeDef",
    {
        "TicketId": str,
    },
)
SuspendGameServerGroupInputRequestTypeDef = TypedDict(
    "SuspendGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "SuspendActions": Sequence[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateBuildInputRequestTypeDef = TypedDict(
    "UpdateBuildInputRequestTypeDef",
    {
        "BuildId": str,
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
UpdateFleetCapacityInputRequestTypeDef = TypedDict(
    "UpdateFleetCapacityInputRequestTypeDef",
    {
        "FleetId": str,
        "DesiredInstances": NotRequired[int],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "Location": NotRequired[str],
    },
)
UpdateGameServerInputRequestTypeDef = TypedDict(
    "UpdateGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
        "GameServerData": NotRequired[str],
        "UtilizationStatus": NotRequired[GameServerUtilizationStatusType],
        "HealthCheck": NotRequired[Literal["HEALTHY"]],
    },
)
ValidateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetInputRequestTypeDef",
    {
        "RuleSetBody": str,
    },
)
VpcPeeringConnectionStatusTypeDef = TypedDict(
    "VpcPeeringConnectionStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasId": NotRequired[str],
        "Name": NotRequired[str],
        "AliasArn": NotRequired[str],
        "Description": NotRequired[str],
        "RoutingStrategy": NotRequired[RoutingStrategyTypeDef],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
UpdateAliasInputRequestTypeDef = TypedDict(
    "UpdateAliasInputRequestTypeDef",
    {
        "AliasId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RoutingStrategy": NotRequired[RoutingStrategyTypeDef],
    },
)
PlayerTypeDef = TypedDict(
    "PlayerTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerAttributes": NotRequired[Dict[str, AttributeValueTypeDef]],
        "Team": NotRequired[str],
        "LatencyInMs": NotRequired[Dict[str, int]],
    },
)
ClaimGameServerInputRequestTypeDef = TypedDict(
    "ClaimGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": NotRequired[str],
        "GameServerData": NotRequired[str],
        "FilterOption": NotRequired[ClaimFilterOptionTypeDef],
    },
)
ClaimGameServerOutputTypeDef = TypedDict(
    "ClaimGameServerOutputTypeDef",
    {
        "GameServer": GameServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBuildOutputTypeDef = TypedDict(
    "DescribeBuildOutputTypeDef",
    {
        "Build": BuildTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameServerOutputTypeDef = TypedDict(
    "DescribeGameServerOutputTypeDef",
    {
        "GameServer": GameServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComputeAccessOutputTypeDef = TypedDict(
    "GetComputeAccessOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ComputeName": str,
        "ComputeArn": str,
        "Credentials": AwsCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComputeAuthTokenOutputTypeDef = TypedDict(
    "GetComputeAuthTokenOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ComputeName": str,
        "ComputeArn": str,
        "AuthToken": str,
        "ExpirationTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGameSessionLogUrlOutputTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputTypeDef",
    {
        "PreSignedUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "Builds": List[BuildTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFleetsOutputTypeDef = TypedDict(
    "ListFleetsOutputTypeDef",
    {
        "FleetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGameServersOutputTypeDef = TypedDict(
    "ListGameServersOutputTypeDef",
    {
        "GameServers": List[GameServerTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutScalingPolicyOutputTypeDef = TypedDict(
    "PutScalingPolicyOutputTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterGameServerOutputTypeDef = TypedDict(
    "RegisterGameServerOutputTypeDef",
    {
        "GameServer": GameServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResolveAliasOutputTypeDef = TypedDict(
    "ResolveAliasOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFleetActionsOutputTypeDef = TypedDict(
    "StartFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopFleetActionsOutputTypeDef = TypedDict(
    "StopFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBuildOutputTypeDef = TypedDict(
    "UpdateBuildOutputTypeDef",
    {
        "Build": BuildTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFleetAttributesOutputTypeDef = TypedDict(
    "UpdateFleetAttributesOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFleetCapacityOutputTypeDef = TypedDict(
    "UpdateFleetCapacityOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFleetPortSettingsOutputTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGameServerOutputTypeDef = TypedDict(
    "UpdateGameServerOutputTypeDef",
    {
        "GameServer": GameServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputTypeDef",
    {
        "Valid": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeComputeOutputTypeDef = TypedDict(
    "DescribeComputeOutputTypeDef",
    {
        "Compute": ComputeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComputeOutputTypeDef = TypedDict(
    "ListComputeOutputTypeDef",
    {
        "ComputeList": List[ComputeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterComputeOutputTypeDef = TypedDict(
    "RegisterComputeOutputTypeDef",
    {
        "Compute": ComputeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAliasInputRequestTypeDef = TypedDict(
    "CreateAliasInputRequestTypeDef",
    {
        "Name": str,
        "RoutingStrategy": RoutingStrategyTypeDef,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateLocationInputRequestTypeDef = TypedDict(
    "CreateLocationInputRequestTypeDef",
    {
        "LocationName": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "CreateMatchmakingRuleSetInputRequestTypeDef",
    {
        "Name": str,
        "RuleSetBody": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
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
CreateBuildInputRequestTypeDef = TypedDict(
    "CreateBuildInputRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "StorageLocation": NotRequired[S3LocationTypeDef],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ServerSdkVersion": NotRequired[str],
    },
)
CreateBuildOutputTypeDef = TypedDict(
    "CreateBuildOutputTypeDef",
    {
        "Build": BuildTypeDef,
        "UploadCredentials": AwsCredentialsTypeDef,
        "StorageLocation": S3LocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScriptInputRequestTypeDef = TypedDict(
    "CreateScriptInputRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "StorageLocation": NotRequired[S3LocationTypeDef],
        "ZipFile": NotRequired[BlobTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
RequestUploadCredentialsOutputTypeDef = TypedDict(
    "RequestUploadCredentialsOutputTypeDef",
    {
        "UploadCredentials": AwsCredentialsTypeDef,
        "StorageLocation": S3LocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ScriptId": NotRequired[str],
        "ScriptArn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "SizeOnDisk": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "StorageLocation": NotRequired[S3LocationTypeDef],
    },
)
UpdateScriptInputRequestTypeDef = TypedDict(
    "UpdateScriptInputRequestTypeDef",
    {
        "ScriptId": str,
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "StorageLocation": NotRequired[S3LocationTypeDef],
        "ZipFile": NotRequired[BlobTypeDef],
    },
)
DescribeFleetPortSettingsOutputTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InboundPermissions": List[IpPermissionTypeDef],
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFleetPortSettingsInputRequestTypeDef = TypedDict(
    "UpdateFleetPortSettingsInputRequestTypeDef",
    {
        "FleetId": str,
        "InboundPermissionAuthorizations": NotRequired[Sequence[IpPermissionTypeDef]],
        "InboundPermissionRevocations": NotRequired[Sequence[IpPermissionTypeDef]],
    },
)
CreateFleetLocationsInputRequestTypeDef = TypedDict(
    "CreateFleetLocationsInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": Sequence[LocationConfigurationTypeDef],
    },
)
FleetAttributesTypeDef = TypedDict(
    "FleetAttributesTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "FleetType": NotRequired[FleetTypeType],
        "InstanceType": NotRequired[EC2InstanceTypeType],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "TerminationTime": NotRequired[datetime],
        "Status": NotRequired[FleetStatusType],
        "BuildId": NotRequired[str],
        "BuildArn": NotRequired[str],
        "ScriptId": NotRequired[str],
        "ScriptArn": NotRequired[str],
        "ServerLaunchPath": NotRequired[str],
        "ServerLaunchParameters": NotRequired[str],
        "LogPaths": NotRequired[List[str]],
        "NewGameSessionProtectionPolicy": NotRequired[ProtectionPolicyType],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "ResourceCreationLimitPolicy": NotRequired[ResourceCreationLimitPolicyTypeDef],
        "MetricGroups": NotRequired[List[str]],
        "StoppedActions": NotRequired[List[Literal["AUTO_SCALING"]]],
        "InstanceRoleArn": NotRequired[str],
        "CertificateConfiguration": NotRequired[CertificateConfigurationTypeDef],
        "ComputeType": NotRequired[ComputeTypeType],
        "AnywhereConfiguration": NotRequired[AnywhereConfigurationTypeDef],
        "InstanceRoleCredentialsProvider": NotRequired[Literal["SHARED_CREDENTIAL_FILE"]],
    },
)
UpdateFleetAttributesInputRequestTypeDef = TypedDict(
    "UpdateFleetAttributesInputRequestTypeDef",
    {
        "FleetId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "NewGameSessionProtectionPolicy": NotRequired[ProtectionPolicyType],
        "ResourceCreationLimitPolicy": NotRequired[ResourceCreationLimitPolicyTypeDef],
        "MetricGroups": NotRequired[Sequence[str]],
        "AnywhereConfiguration": NotRequired[AnywhereConfigurationTypeDef],
    },
)
CreateFleetLocationsOutputTypeDef = TypedDict(
    "CreateFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List[LocationStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFleetLocationsOutputTypeDef = TypedDict(
    "DeleteFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List[LocationStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LocationAttributesTypeDef = TypedDict(
    "LocationAttributesTypeDef",
    {
        "LocationState": NotRequired[LocationStateTypeDef],
        "StoppedActions": NotRequired[List[Literal["AUTO_SCALING"]]],
        "UpdateStatus": NotRequired[Literal["PENDING_UPDATE"]],
    },
)
GameServerGroupTypeDef = TypedDict(
    "GameServerGroupTypeDef",
    {
        "GameServerGroupName": NotRequired[str],
        "GameServerGroupArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "InstanceDefinitions": NotRequired[List[InstanceDefinitionTypeDef]],
        "BalancingStrategy": NotRequired[BalancingStrategyType],
        "GameServerProtectionPolicy": NotRequired[GameServerProtectionPolicyType],
        "AutoScalingGroupArn": NotRequired[str],
        "Status": NotRequired[GameServerGroupStatusType],
        "StatusReason": NotRequired[str],
        "SuspendedActions": NotRequired[List[Literal["REPLACE_INSTANCE_TYPES"]]],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
UpdateGameServerGroupInputRequestTypeDef = TypedDict(
    "UpdateGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "RoleArn": NotRequired[str],
        "InstanceDefinitions": NotRequired[Sequence[InstanceDefinitionTypeDef]],
        "GameServerProtectionPolicy": NotRequired[GameServerProtectionPolicyType],
        "BalancingStrategy": NotRequired[BalancingStrategyType],
    },
)
CreateGameSessionInputRequestTypeDef = TypedDict(
    "CreateGameSessionInputRequestTypeDef",
    {
        "MaximumPlayerSessionCount": int,
        "FleetId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Name": NotRequired[str],
        "GameProperties": NotRequired[Sequence[GamePropertyTypeDef]],
        "CreatorId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
        "GameSessionData": NotRequired[str],
        "Location": NotRequired[str],
    },
)
CreateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "CreateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "RequestTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "Description": NotRequired[str],
        "GameSessionQueueArns": NotRequired[Sequence[str]],
        "AcceptanceTimeoutSeconds": NotRequired[int],
        "NotificationTarget": NotRequired[str],
        "AdditionalPlayerCount": NotRequired[int],
        "CustomEventData": NotRequired[str],
        "GameProperties": NotRequired[Sequence[GamePropertyTypeDef]],
        "GameSessionData": NotRequired[str],
        "BackfillMode": NotRequired[BackfillModeType],
        "FlexMatchMode": NotRequired[FlexMatchModeType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GameSessionTypeDef = TypedDict(
    "GameSessionTypeDef",
    {
        "GameSessionId": NotRequired[str],
        "Name": NotRequired[str],
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "TerminationTime": NotRequired[datetime],
        "CurrentPlayerSessionCount": NotRequired[int],
        "MaximumPlayerSessionCount": NotRequired[int],
        "Status": NotRequired[GameSessionStatusType],
        "StatusReason": NotRequired[Literal["INTERRUPTED"]],
        "GameProperties": NotRequired[List[GamePropertyTypeDef]],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "PlayerSessionCreationPolicy": NotRequired[PlayerSessionCreationPolicyType],
        "CreatorId": NotRequired[str],
        "GameSessionData": NotRequired[str],
        "MatchmakerData": NotRequired[str],
        "Location": NotRequired[str],
    },
)
MatchmakingConfigurationTypeDef = TypedDict(
    "MatchmakingConfigurationTypeDef",
    {
        "Name": NotRequired[str],
        "ConfigurationArn": NotRequired[str],
        "Description": NotRequired[str],
        "GameSessionQueueArns": NotRequired[List[str]],
        "RequestTimeoutSeconds": NotRequired[int],
        "AcceptanceTimeoutSeconds": NotRequired[int],
        "AcceptanceRequired": NotRequired[bool],
        "RuleSetName": NotRequired[str],
        "RuleSetArn": NotRequired[str],
        "NotificationTarget": NotRequired[str],
        "AdditionalPlayerCount": NotRequired[int],
        "CustomEventData": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "GameProperties": NotRequired[List[GamePropertyTypeDef]],
        "GameSessionData": NotRequired[str],
        "BackfillMode": NotRequired[BackfillModeType],
        "FlexMatchMode": NotRequired[FlexMatchModeType],
    },
)
UpdateGameSessionInputRequestTypeDef = TypedDict(
    "UpdateGameSessionInputRequestTypeDef",
    {
        "GameSessionId": str,
        "MaximumPlayerSessionCount": NotRequired[int],
        "Name": NotRequired[str],
        "PlayerSessionCreationPolicy": NotRequired[PlayerSessionCreationPolicyType],
        "ProtectionPolicy": NotRequired[ProtectionPolicyType],
        "GameProperties": NotRequired[Sequence[GamePropertyTypeDef]],
    },
)
UpdateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "GameSessionQueueArns": NotRequired[Sequence[str]],
        "RequestTimeoutSeconds": NotRequired[int],
        "AcceptanceTimeoutSeconds": NotRequired[int],
        "AcceptanceRequired": NotRequired[bool],
        "RuleSetName": NotRequired[str],
        "NotificationTarget": NotRequired[str],
        "AdditionalPlayerCount": NotRequired[int],
        "CustomEventData": NotRequired[str],
        "GameProperties": NotRequired[Sequence[GamePropertyTypeDef]],
        "GameSessionData": NotRequired[str],
        "BackfillMode": NotRequired[BackfillModeType],
        "FlexMatchMode": NotRequired[FlexMatchModeType],
    },
)
CreateGameSessionQueueInputRequestTypeDef = TypedDict(
    "CreateGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[Sequence[PlayerLatencyPolicyTypeDef]],
        "Destinations": NotRequired[Sequence[GameSessionQueueDestinationTypeDef]],
        "FilterConfiguration": NotRequired[FilterConfigurationTypeDef],
        "PriorityConfiguration": NotRequired[PriorityConfigurationTypeDef],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GameSessionQueueTypeDef = TypedDict(
    "GameSessionQueueTypeDef",
    {
        "Name": NotRequired[str],
        "GameSessionQueueArn": NotRequired[str],
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[List[PlayerLatencyPolicyTypeDef]],
        "Destinations": NotRequired[List[GameSessionQueueDestinationTypeDef]],
        "FilterConfiguration": NotRequired[FilterConfigurationTypeDef],
        "PriorityConfiguration": NotRequired[PriorityConfigurationTypeDef],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
    },
)
UpdateGameSessionQueueInputRequestTypeDef = TypedDict(
    "UpdateGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[Sequence[PlayerLatencyPolicyTypeDef]],
        "Destinations": NotRequired[Sequence[GameSessionQueueDestinationTypeDef]],
        "FilterConfiguration": NotRequired[FilterConfigurationTypeDef],
        "PriorityConfiguration": NotRequired[PriorityConfigurationTypeDef],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
    },
)
CreateLocationOutputTypeDef = TypedDict(
    "CreateLocationOutputTypeDef",
    {
        "Location": LocationModelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLocationsOutputTypeDef = TypedDict(
    "ListLocationsOutputTypeDef",
    {
        "Locations": List[LocationModelTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "CreateMatchmakingRuleSetOutputTypeDef",
    {
        "RuleSet": MatchmakingRuleSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    {
        "RuleSets": List[MatchmakingRuleSetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlayerSessionOutputTypeDef = TypedDict(
    "CreatePlayerSessionOutputTypeDef",
    {
        "PlayerSession": PlayerSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlayerSessionsOutputTypeDef = TypedDict(
    "CreatePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List[PlayerSessionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePlayerSessionsOutputTypeDef = TypedDict(
    "DescribePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List[PlayerSessionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcPeeringAuthorizationOutputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    {
        "VpcPeeringAuthorization": VpcPeeringAuthorizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcPeeringAuthorizationsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    {
        "VpcPeeringAuthorizations": List[VpcPeeringAuthorizationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEC2InstanceLimitsOutputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputTypeDef",
    {
        "EC2InstanceLimits": List[EC2InstanceLimitTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetAttributesInputDescribeFleetAttributesPaginateTypeDef = TypedDict(
    "DescribeFleetAttributesInputDescribeFleetAttributesPaginateTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFleetCapacityInputDescribeFleetCapacityPaginateTypeDef = TypedDict(
    "DescribeFleetCapacityInputDescribeFleetCapacityPaginateTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateTypeDef = TypedDict(
    "DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateTypeDef = TypedDict(
    "DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateTypeDef",
    {
        "GameServerGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateTypeDef = TypedDict(
    "DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateTypeDef",
    {
        "FleetId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "StatusFilter": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateTypeDef = TypedDict(
    "DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGameSessionsInputDescribeGameSessionsPaginateTypeDef = TypedDict(
    "DescribeGameSessionsInputDescribeGameSessionsPaginateTypeDef",
    {
        "FleetId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "StatusFilter": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeInstancesInputDescribeInstancesPaginateTypeDef = TypedDict(
    "DescribeInstancesInputDescribeInstancesPaginateTypeDef",
    {
        "FleetId": str,
        "InstanceId": NotRequired[str],
        "Location": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "RuleSetName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePlayerSessionsInputDescribePlayerSessionsPaginateTypeDef = TypedDict(
    "DescribePlayerSessionsInputDescribePlayerSessionsPaginateTypeDef",
    {
        "GameSessionId": NotRequired[str],
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
        "PlayerSessionStatusFilter": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateTypeDef = TypedDict(
    "DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateTypeDef",
    {
        "FleetId": str,
        "StatusFilter": NotRequired[ScalingStatusTypeType],
        "Location": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAliasesInputListAliasesPaginateTypeDef = TypedDict(
    "ListAliasesInputListAliasesPaginateTypeDef",
    {
        "RoutingStrategyType": NotRequired[RoutingStrategyTypeType],
        "Name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBuildsInputListBuildsPaginateTypeDef = TypedDict(
    "ListBuildsInputListBuildsPaginateTypeDef",
    {
        "Status": NotRequired[BuildStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComputeInputListComputePaginateTypeDef = TypedDict(
    "ListComputeInputListComputePaginateTypeDef",
    {
        "FleetId": str,
        "Location": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFleetsInputListFleetsPaginateTypeDef = TypedDict(
    "ListFleetsInputListFleetsPaginateTypeDef",
    {
        "BuildId": NotRequired[str],
        "ScriptId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGameServerGroupsInputListGameServerGroupsPaginateTypeDef = TypedDict(
    "ListGameServerGroupsInputListGameServerGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGameServersInputListGameServersPaginateTypeDef = TypedDict(
    "ListGameServersInputListGameServersPaginateTypeDef",
    {
        "GameServerGroupName": str,
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLocationsInputListLocationsPaginateTypeDef = TypedDict(
    "ListLocationsInputListLocationsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[LocationFilterType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListScriptsInputListScriptsPaginateTypeDef = TypedDict(
    "ListScriptsInputListScriptsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchGameSessionsInputSearchGameSessionsPaginateTypeDef = TypedDict(
    "SearchGameSessionsInputSearchGameSessionsPaginateTypeDef",
    {
        "FleetId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "SortExpression": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFleetEventsInputDescribeFleetEventsPaginateTypeDef = TypedDict(
    "DescribeFleetEventsInputDescribeFleetEventsPaginateTypeDef",
    {
        "FleetId": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFleetEventsInputRequestTypeDef = TypedDict(
    "DescribeFleetEventsInputRequestTypeDef",
    {
        "FleetId": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFleetEventsOutputTypeDef = TypedDict(
    "DescribeFleetEventsOutputTypeDef",
    {
        "Events": List[EventTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetLocationUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationOutputTypeDef",
    {
        "FleetUtilization": FleetUtilizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputTypeDef",
    {
        "FleetUtilization": List[FleetUtilizationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameServerInstancesOutputTypeDef = TypedDict(
    "DescribeGameServerInstancesOutputTypeDef",
    {
        "GameServerInstances": List[GameServerInstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstancesOutputTypeDef = TypedDict(
    "DescribeInstancesOutputTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FleetCapacityTypeDef = TypedDict(
    "FleetCapacityTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "InstanceType": NotRequired[EC2InstanceTypeType],
        "InstanceCounts": NotRequired[EC2InstanceCountsTypeDef],
        "Location": NotRequired[str],
    },
)
GameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "GameServerGroupAutoScalingPolicyTypeDef",
    {
        "TargetTrackingConfiguration": TargetTrackingConfigurationTypeDef,
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)
GameSessionConnectionInfoTypeDef = TypedDict(
    "GameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": NotRequired[str],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "MatchedPlayerSessions": NotRequired[List[MatchedPlayerSessionTypeDef]],
    },
)
GameSessionPlacementTypeDef = TypedDict(
    "GameSessionPlacementTypeDef",
    {
        "PlacementId": NotRequired[str],
        "GameSessionQueueName": NotRequired[str],
        "Status": NotRequired[GameSessionPlacementStateType],
        "GameProperties": NotRequired[List[GamePropertyTypeDef]],
        "MaximumPlayerSessionCount": NotRequired[int],
        "GameSessionName": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "GameSessionArn": NotRequired[str],
        "GameSessionRegion": NotRequired[str],
        "PlayerLatencies": NotRequired[List[PlayerLatencyTypeDef]],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "PlacedPlayerSessions": NotRequired[List[PlacedPlayerSessionTypeDef]],
        "GameSessionData": NotRequired[str],
        "MatchmakerData": NotRequired[str],
    },
)
StartGameSessionPlacementInputRequestTypeDef = TypedDict(
    "StartGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "MaximumPlayerSessionCount": int,
        "GameProperties": NotRequired[Sequence[GamePropertyTypeDef]],
        "GameSessionName": NotRequired[str],
        "PlayerLatencies": NotRequired[Sequence[PlayerLatencyTypeDef]],
        "DesiredPlayerSessions": NotRequired[Sequence[DesiredPlayerSessionTypeDef]],
        "GameSessionData": NotRequired[str],
    },
)
GameSessionQueuePaginatorTypeDef = TypedDict(
    "GameSessionQueuePaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "GameSessionQueueArn": NotRequired[str],
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[List[PlayerLatencyPolicyTypeDef]],
        "Destinations": NotRequired[List[GameSessionQueueDestinationTypeDef]],
        "FilterConfiguration": NotRequired[FilterConfigurationPaginatorTypeDef],
        "PriorityConfiguration": NotRequired[PriorityConfigurationPaginatorTypeDef],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
    },
)
InstanceAccessTypeDef = TypedDict(
    "InstanceAccessTypeDef",
    {
        "FleetId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Credentials": NotRequired[InstanceCredentialsTypeDef],
    },
)
PutScalingPolicyInputRequestTypeDef = TypedDict(
    "PutScalingPolicyInputRequestTypeDef",
    {
        "Name": str,
        "FleetId": str,
        "MetricName": MetricNameType,
        "ScalingAdjustment": NotRequired[int],
        "ScalingAdjustmentType": NotRequired[ScalingAdjustmentTypeType],
        "Threshold": NotRequired[float],
        "ComparisonOperator": NotRequired[ComparisonOperatorTypeType],
        "EvaluationPeriods": NotRequired[int],
        "PolicyType": NotRequired[PolicyTypeType],
        "TargetConfiguration": NotRequired[TargetConfigurationTypeDef],
    },
)
ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ScalingStatusTypeType],
        "ScalingAdjustment": NotRequired[int],
        "ScalingAdjustmentType": NotRequired[ScalingAdjustmentTypeType],
        "ComparisonOperator": NotRequired[ComparisonOperatorTypeType],
        "Threshold": NotRequired[float],
        "EvaluationPeriods": NotRequired[int],
        "MetricName": NotRequired[MetricNameType],
        "PolicyType": NotRequired[PolicyTypeType],
        "TargetConfiguration": NotRequired[TargetConfigurationTypeDef],
        "UpdateStatus": NotRequired[Literal["PENDING_UPDATE"]],
        "Location": NotRequired[str],
    },
)
RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "ServerProcesses": NotRequired[Sequence[ServerProcessTypeDef]],
        "MaxConcurrentGameSessionActivations": NotRequired[int],
        "GameSessionActivationTimeoutSeconds": NotRequired[int],
    },
)
VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "IpV4CidrBlock": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "Status": NotRequired[VpcPeeringConnectionStatusTypeDef],
        "PeerVpcId": NotRequired[str],
        "GameLiftVpcId": NotRequired[str],
    },
)
CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAliasOutputTypeDef = TypedDict(
    "DescribeAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List[AliasTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMatchBackfillInputRequestTypeDef = TypedDict(
    "StartMatchBackfillInputRequestTypeDef",
    {
        "ConfigurationName": str,
        "Players": Sequence[PlayerTypeDef],
        "TicketId": NotRequired[str],
        "GameSessionArn": NotRequired[str],
    },
)
StartMatchmakingInputRequestTypeDef = TypedDict(
    "StartMatchmakingInputRequestTypeDef",
    {
        "ConfigurationName": str,
        "Players": Sequence[PlayerTypeDef],
        "TicketId": NotRequired[str],
    },
)
CreateScriptOutputTypeDef = TypedDict(
    "CreateScriptOutputTypeDef",
    {
        "Script": ScriptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScriptOutputTypeDef = TypedDict(
    "DescribeScriptOutputTypeDef",
    {
        "Script": ScriptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListScriptsOutputTypeDef = TypedDict(
    "ListScriptsOutputTypeDef",
    {
        "Scripts": List[ScriptTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateScriptOutputTypeDef = TypedDict(
    "UpdateScriptOutputTypeDef",
    {
        "Script": ScriptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFleetOutputTypeDef = TypedDict(
    "CreateFleetOutputTypeDef",
    {
        "FleetAttributes": FleetAttributesTypeDef,
        "LocationStates": List[LocationStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetAttributesOutputTypeDef = TypedDict(
    "DescribeFleetAttributesOutputTypeDef",
    {
        "FleetAttributes": List[FleetAttributesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetLocationAttributesOutputTypeDef = TypedDict(
    "DescribeFleetLocationAttributesOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationAttributes": List[LocationAttributesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGameServerGroupOutputTypeDef = TypedDict(
    "CreateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": GameServerGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGameServerGroupOutputTypeDef = TypedDict(
    "DeleteGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": GameServerGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameServerGroupOutputTypeDef = TypedDict(
    "DescribeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": GameServerGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGameServerGroupsOutputTypeDef = TypedDict(
    "ListGameServerGroupsOutputTypeDef",
    {
        "GameServerGroups": List[GameServerGroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResumeGameServerGroupOutputTypeDef = TypedDict(
    "ResumeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": GameServerGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SuspendGameServerGroupOutputTypeDef = TypedDict(
    "SuspendGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": GameServerGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGameServerGroupOutputTypeDef = TypedDict(
    "UpdateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": GameServerGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGameSessionOutputTypeDef = TypedDict(
    "CreateGameSessionOutputTypeDef",
    {
        "GameSession": GameSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameSessionsOutputTypeDef = TypedDict(
    "DescribeGameSessionsOutputTypeDef",
    {
        "GameSessions": List[GameSessionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GameSessionDetailTypeDef = TypedDict(
    "GameSessionDetailTypeDef",
    {
        "GameSession": NotRequired[GameSessionTypeDef],
        "ProtectionPolicy": NotRequired[ProtectionPolicyType],
    },
)
SearchGameSessionsOutputTypeDef = TypedDict(
    "SearchGameSessionsOutputTypeDef",
    {
        "GameSessions": List[GameSessionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGameSessionOutputTypeDef = TypedDict(
    "UpdateGameSessionOutputTypeDef",
    {
        "GameSession": GameSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": MatchmakingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMatchmakingConfigurationsOutputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    {
        "Configurations": List[MatchmakingConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": MatchmakingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGameSessionQueueOutputTypeDef = TypedDict(
    "CreateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": GameSessionQueueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameSessionQueuesOutputTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputTypeDef",
    {
        "GameSessionQueues": List[GameSessionQueueTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGameSessionQueueOutputTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": GameSessionQueueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetCapacityOutputTypeDef = TypedDict(
    "DescribeFleetCapacityOutputTypeDef",
    {
        "FleetCapacity": List[FleetCapacityTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFleetLocationCapacityOutputTypeDef = TypedDict(
    "DescribeFleetLocationCapacityOutputTypeDef",
    {
        "FleetCapacity": FleetCapacityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGameServerGroupInputRequestTypeDef = TypedDict(
    "CreateGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "RoleArn": str,
        "MinSize": int,
        "MaxSize": int,
        "LaunchTemplate": LaunchTemplateSpecificationTypeDef,
        "InstanceDefinitions": Sequence[InstanceDefinitionTypeDef],
        "AutoScalingPolicy": NotRequired[GameServerGroupAutoScalingPolicyTypeDef],
        "BalancingStrategy": NotRequired[BalancingStrategyType],
        "GameServerProtectionPolicy": NotRequired[GameServerProtectionPolicyType],
        "VpcSubnets": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MatchmakingTicketTypeDef = TypedDict(
    "MatchmakingTicketTypeDef",
    {
        "TicketId": NotRequired[str],
        "ConfigurationName": NotRequired[str],
        "ConfigurationArn": NotRequired[str],
        "Status": NotRequired[MatchmakingConfigurationStatusType],
        "StatusReason": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Players": NotRequired[List[PlayerTypeDef]],
        "GameSessionConnectionInfo": NotRequired[GameSessionConnectionInfoTypeDef],
        "EstimatedWaitTime": NotRequired[int],
    },
)
DescribeGameSessionPlacementOutputTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": GameSessionPlacementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartGameSessionPlacementOutputTypeDef = TypedDict(
    "StartGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": GameSessionPlacementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopGameSessionPlacementOutputTypeDef = TypedDict(
    "StopGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": GameSessionPlacementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameSessionQueuesOutputPaginatorTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputPaginatorTypeDef",
    {
        "GameSessionQueues": List[GameSessionQueuePaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceAccessOutputTypeDef = TypedDict(
    "GetInstanceAccessOutputTypeDef",
    {
        "InstanceAccess": InstanceAccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScalingPoliciesOutputTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputTypeDef",
    {
        "ScalingPolicies": List[ScalingPolicyTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFleetInputRequestTypeDef = TypedDict(
    "CreateFleetInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "BuildId": NotRequired[str],
        "ScriptId": NotRequired[str],
        "ServerLaunchPath": NotRequired[str],
        "ServerLaunchParameters": NotRequired[str],
        "LogPaths": NotRequired[Sequence[str]],
        "EC2InstanceType": NotRequired[EC2InstanceTypeType],
        "EC2InboundPermissions": NotRequired[Sequence[IpPermissionTypeDef]],
        "NewGameSessionProtectionPolicy": NotRequired[ProtectionPolicyType],
        "RuntimeConfiguration": NotRequired[RuntimeConfigurationTypeDef],
        "ResourceCreationLimitPolicy": NotRequired[ResourceCreationLimitPolicyTypeDef],
        "MetricGroups": NotRequired[Sequence[str]],
        "PeerVpcAwsAccountId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "FleetType": NotRequired[FleetTypeType],
        "InstanceRoleArn": NotRequired[str],
        "CertificateConfiguration": NotRequired[CertificateConfigurationTypeDef],
        "Locations": NotRequired[Sequence[LocationConfigurationTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ComputeType": NotRequired[ComputeTypeType],
        "AnywhereConfiguration": NotRequired[AnywhereConfigurationTypeDef],
        "InstanceRoleCredentialsProvider": NotRequired[Literal["SHARED_CREDENTIAL_FILE"]],
    },
)
DescribeRuntimeConfigurationOutputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": RuntimeConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRuntimeConfigurationInputRequestTypeDef = TypedDict(
    "UpdateRuntimeConfigurationInputRequestTypeDef",
    {
        "FleetId": str,
        "RuntimeConfiguration": RuntimeConfigurationTypeDef,
    },
)
UpdateRuntimeConfigurationOutputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": RuntimeConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcPeeringConnectionsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    {
        "VpcPeeringConnections": List[VpcPeeringConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGameSessionDetailsOutputTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputTypeDef",
    {
        "GameSessionDetails": List[GameSessionDetailTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMatchmakingOutputTypeDef = TypedDict(
    "DescribeMatchmakingOutputTypeDef",
    {
        "TicketList": List[MatchmakingTicketTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMatchBackfillOutputTypeDef = TypedDict(
    "StartMatchBackfillOutputTypeDef",
    {
        "MatchmakingTicket": MatchmakingTicketTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMatchmakingOutputTypeDef = TypedDict(
    "StartMatchmakingOutputTypeDef",
    {
        "MatchmakingTicket": MatchmakingTicketTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
