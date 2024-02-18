"""
Type annotations for dlm service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dlm/type_defs/)

Usage::

    ```python
    from types_aiobotocore_dlm.type_defs import RetentionArchiveTierTypeDef

    data: RetentionArchiveTierTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    DefaultPoliciesTypeValuesType,
    DefaultPolicyTypeValuesType,
    GettablePolicyStateValuesType,
    LocationValuesType,
    PolicyLanguageValuesType,
    PolicyTypeValuesType,
    ResourceLocationValuesType,
    ResourceTypeValuesType,
    RetentionIntervalUnitValuesType,
    SettablePolicyStateValuesType,
    StageValuesType,
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
    "RetentionArchiveTierTypeDef",
    "CrossRegionCopyTargetTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "EncryptionConfigurationTypeDef",
    "CrossRegionCopyDeprecateRuleTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeprecateRuleTypeDef",
    "EventParametersTypeDef",
    "TagTypeDef",
    "FastRestoreRuleTypeDef",
    "GetLifecyclePoliciesRequestRequestTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RetainRuleTypeDef",
    "ShareRuleTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ArchiveRetainRuleTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateRuleTypeDef",
    "CrossRegionCopyActionTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "EventSourceTypeDef",
    "ExclusionsTypeDef",
    "ParametersTypeDef",
    "GetLifecyclePoliciesResponseTypeDef",
    "ArchiveRuleTypeDef",
    "ActionTypeDef",
    "ScheduleTypeDef",
    "PolicyDetailsTypeDef",
    "CreateLifecyclePolicyRequestRequestTypeDef",
    "LifecyclePolicyTypeDef",
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
)

RetentionArchiveTierTypeDef = TypedDict(
    "RetentionArchiveTierTypeDef",
    {
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
CrossRegionCopyTargetTypeDef = TypedDict(
    "CrossRegionCopyTargetTypeDef",
    {
        "TargetRegion": NotRequired[str],
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
ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ExecutionHandler": str,
        "Stages": NotRequired[Sequence[StageValuesType]],
        "ExecutionHandlerService": NotRequired[Literal["AWS_SYSTEMS_MANAGER"]],
        "ExecuteOperationOnScriptFailure": NotRequired[bool],
        "ExecutionTimeout": NotRequired[int],
        "MaximumRetryCount": NotRequired[int],
    },
)
CrossRegionCopyRetainRuleTypeDef = TypedDict(
    "CrossRegionCopyRetainRuleTypeDef",
    {
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "Encrypted": bool,
        "CmkArn": NotRequired[str],
    },
)
CrossRegionCopyDeprecateRuleTypeDef = TypedDict(
    "CrossRegionCopyDeprecateRuleTypeDef",
    {
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
DeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
DeprecateRuleTypeDef = TypedDict(
    "DeprecateRuleTypeDef",
    {
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
EventParametersTypeDef = TypedDict(
    "EventParametersTypeDef",
    {
        "EventType": Literal["shareSnapshot"],
        "SnapshotOwner": Sequence[str],
        "DescriptionRegex": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
FastRestoreRuleTypeDef = TypedDict(
    "FastRestoreRuleTypeDef",
    {
        "AvailabilityZones": Sequence[str],
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
GetLifecyclePoliciesRequestRequestTypeDef = TypedDict(
    "GetLifecyclePoliciesRequestRequestTypeDef",
    {
        "PolicyIds": NotRequired[Sequence[str]],
        "State": NotRequired[GettablePolicyStateValuesType],
        "ResourceTypes": NotRequired[Sequence[ResourceTypeValuesType]],
        "TargetTags": NotRequired[Sequence[str]],
        "TagsToAdd": NotRequired[Sequence[str]],
        "DefaultPolicyType": NotRequired[DefaultPoliciesTypeValuesType],
    },
)
LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "PolicyId": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[GettablePolicyStateValuesType],
        "Tags": NotRequired[Dict[str, str]],
        "PolicyType": NotRequired[PolicyTypeValuesType],
        "DefaultPolicy": NotRequired[bool],
    },
)
GetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
RetainRuleTypeDef = TypedDict(
    "RetainRuleTypeDef",
    {
        "Count": NotRequired[int],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
ShareRuleTypeDef = TypedDict(
    "ShareRuleTypeDef",
    {
        "TargetAccounts": Sequence[str],
        "UnshareInterval": NotRequired[int],
        "UnshareIntervalUnit": NotRequired[RetentionIntervalUnitValuesType],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
ArchiveRetainRuleTypeDef = TypedDict(
    "ArchiveRetainRuleTypeDef",
    {
        "RetentionArchiveTier": RetentionArchiveTierTypeDef,
    },
)
CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef",
    {
        "PolicyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRuleTypeDef = TypedDict(
    "CreateRuleTypeDef",
    {
        "Location": NotRequired[LocationValuesType],
        "Interval": NotRequired[int],
        "IntervalUnit": NotRequired[Literal["HOURS"]],
        "Times": NotRequired[Sequence[str]],
        "CronExpression": NotRequired[str],
        "Scripts": NotRequired[Sequence[ScriptTypeDef]],
    },
)
CrossRegionCopyActionTypeDef = TypedDict(
    "CrossRegionCopyActionTypeDef",
    {
        "Target": str,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
        "RetainRule": NotRequired[CrossRegionCopyRetainRuleTypeDef],
    },
)
CrossRegionCopyRuleTypeDef = TypedDict(
    "CrossRegionCopyRuleTypeDef",
    {
        "Encrypted": bool,
        "TargetRegion": NotRequired[str],
        "Target": NotRequired[str],
        "CmkArn": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "RetainRule": NotRequired[CrossRegionCopyRetainRuleTypeDef],
        "DeprecateRule": NotRequired[CrossRegionCopyDeprecateRuleTypeDef],
    },
)
EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Type": Literal["MANAGED_CWE"],
        "Parameters": NotRequired[EventParametersTypeDef],
    },
)
ExclusionsTypeDef = TypedDict(
    "ExclusionsTypeDef",
    {
        "ExcludeBootVolumes": NotRequired[bool],
        "ExcludeVolumeTypes": NotRequired[Sequence[str]],
        "ExcludeTags": NotRequired[Sequence[TagTypeDef]],
    },
)
ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "ExcludeBootVolume": NotRequired[bool],
        "NoReboot": NotRequired[bool],
        "ExcludeDataVolumeTags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetLifecyclePoliciesResponseTypeDef = TypedDict(
    "GetLifecyclePoliciesResponseTypeDef",
    {
        "Policies": List[LifecyclePolicySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ArchiveRuleTypeDef = TypedDict(
    "ArchiveRuleTypeDef",
    {
        "RetainRule": ArchiveRetainRuleTypeDef,
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Name": str,
        "CrossRegionCopy": Sequence[CrossRegionCopyActionTypeDef],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "TagsToAdd": NotRequired[Sequence[TagTypeDef]],
        "VariableTags": NotRequired[Sequence[TagTypeDef]],
        "CreateRule": NotRequired[CreateRuleTypeDef],
        "RetainRule": NotRequired[RetainRuleTypeDef],
        "FastRestoreRule": NotRequired[FastRestoreRuleTypeDef],
        "CrossRegionCopyRules": NotRequired[Sequence[CrossRegionCopyRuleTypeDef]],
        "ShareRules": NotRequired[Sequence[ShareRuleTypeDef]],
        "DeprecateRule": NotRequired[DeprecateRuleTypeDef],
        "ArchiveRule": NotRequired[ArchiveRuleTypeDef],
    },
)
PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "PolicyType": NotRequired[PolicyTypeValuesType],
        "ResourceTypes": NotRequired[Sequence[ResourceTypeValuesType]],
        "ResourceLocations": NotRequired[Sequence[ResourceLocationValuesType]],
        "TargetTags": NotRequired[Sequence[TagTypeDef]],
        "Schedules": NotRequired[Sequence[ScheduleTypeDef]],
        "Parameters": NotRequired[ParametersTypeDef],
        "EventSource": NotRequired[EventSourceTypeDef],
        "Actions": NotRequired[Sequence[ActionTypeDef]],
        "PolicyLanguage": NotRequired[PolicyLanguageValuesType],
        "ResourceType": NotRequired[ResourceTypeValuesType],
        "CreateInterval": NotRequired[int],
        "RetainInterval": NotRequired[int],
        "CopyTags": NotRequired[bool],
        "CrossRegionCopyTargets": NotRequired[Sequence[CrossRegionCopyTargetTypeDef]],
        "ExtendDeletion": NotRequired[bool],
        "Exclusions": NotRequired[ExclusionsTypeDef],
    },
)
CreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "CreateLifecyclePolicyRequestRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "Description": str,
        "State": SettablePolicyStateValuesType,
        "PolicyDetails": NotRequired[PolicyDetailsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "DefaultPolicy": NotRequired[DefaultPolicyTypeValuesType],
        "CreateInterval": NotRequired[int],
        "RetainInterval": NotRequired[int],
        "CopyTags": NotRequired[bool],
        "ExtendDeletion": NotRequired[bool],
        "CrossRegionCopyTargets": NotRequired[Sequence[CrossRegionCopyTargetTypeDef]],
        "Exclusions": NotRequired[ExclusionsTypeDef],
    },
)
LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "PolicyId": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[GettablePolicyStateValuesType],
        "StatusMessage": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
        "PolicyDetails": NotRequired[PolicyDetailsTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "PolicyArn": NotRequired[str],
        "DefaultPolicy": NotRequired[bool],
    },
)
UpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "ExecutionRoleArn": NotRequired[str],
        "State": NotRequired[SettablePolicyStateValuesType],
        "Description": NotRequired[str],
        "PolicyDetails": NotRequired[PolicyDetailsTypeDef],
        "CreateInterval": NotRequired[int],
        "RetainInterval": NotRequired[int],
        "CopyTags": NotRequired[bool],
        "ExtendDeletion": NotRequired[bool],
        "CrossRegionCopyTargets": NotRequired[Sequence[CrossRegionCopyTargetTypeDef]],
        "Exclusions": NotRequired[ExclusionsTypeDef],
    },
)
GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "Policy": LifecyclePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
