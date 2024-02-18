"""
Type annotations for devicefarm service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_devicefarm/type_defs/)

Usage::

    ```python
    from types_aiobotocore_devicefarm.type_defs import TrialMinutesTypeDef

    data: TrialMinutesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ArtifactCategoryType,
    ArtifactTypeType,
    BillingMethodType,
    DeviceAttributeType,
    DeviceAvailabilityType,
    DeviceFilterAttributeType,
    DeviceFormFactorType,
    DevicePlatformType,
    DevicePoolTypeType,
    ExecutionResultCodeType,
    ExecutionResultType,
    ExecutionStatusType,
    InstanceStatusType,
    InteractionModeType,
    NetworkProfileTypeType,
    OfferingTransactionTypeType,
    RuleOperatorType,
    SampleTypeType,
    TestGridSessionArtifactCategoryType,
    TestGridSessionArtifactTypeType,
    TestGridSessionStatusType,
    TestTypeType,
    UploadCategoryType,
    UploadStatusType,
    UploadTypeType,
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
    "TrialMinutesTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "RuleTypeDef",
    "ResponseMetadataTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "InstanceProfileTypeDef",
    "CreateNetworkProfileRequestRequestTypeDef",
    "NetworkProfileTypeDef",
    "VpcConfigTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "TestGridVpcConfigTypeDef",
    "CreateTestGridUrlRequestRequestTypeDef",
    "CreateUploadRequestRequestTypeDef",
    "UploadTypeDef",
    "CreateVPCEConfigurationRequestRequestTypeDef",
    "VPCEConfigurationTypeDef",
    "CustomerArtifactPathsPaginatorTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeleteDevicePoolRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteNetworkProfileRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteTestGridProjectRequestRequestTypeDef",
    "DeleteUploadRequestRequestTypeDef",
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    "DeviceFilterPaginatorTypeDef",
    "DeviceFilterTypeDef",
    "DeviceMinutesTypeDef",
    "IncompatibilityMessageTypeDef",
    "ResolutionTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetDeviceInstanceRequestRequestTypeDef",
    "ScheduleRunTestTypeDef",
    "GetDevicePoolRequestRequestTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetNetworkProfileRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetOfferingStatusRequestRequestTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetRemoteAccessSessionRequestRequestTypeDef",
    "GetRunRequestRequestTypeDef",
    "GetSuiteRequestRequestTypeDef",
    "GetTestGridProjectRequestRequestTypeDef",
    "GetTestGridSessionRequestRequestTypeDef",
    "TestGridSessionTypeDef",
    "GetTestRequestRequestTypeDef",
    "GetUploadRequestRequestTypeDef",
    "GetVPCEConfigurationRequestRequestTypeDef",
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListDeviceInstancesRequestRequestTypeDef",
    "ListDevicePoolsRequestRequestTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListNetworkProfilesRequestRequestTypeDef",
    "ListOfferingPromotionsRequestRequestTypeDef",
    "OfferingPromotionTypeDef",
    "ListOfferingTransactionsRequestRequestTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    "ListRunsRequestRequestTypeDef",
    "ListSamplesRequestRequestTypeDef",
    "SampleTypeDef",
    "ListSuitesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListTestGridProjectsRequestRequestTypeDef",
    "ListTestGridSessionActionsRequestRequestTypeDef",
    "TestGridSessionActionTypeDef",
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TimestampTypeDef",
    "ListTestsRequestRequestTypeDef",
    "ListUniqueProblemsRequestRequestTypeDef",
    "ListUploadsRequestRequestTypeDef",
    "ListVPCEConfigurationsRequestRequestTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "ProblemDetailTypeDef",
    "VpcConfigPaginatorTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "RadiosTypeDef",
    "RenewOfferingRequestRequestTypeDef",
    "StopJobRequestRequestTypeDef",
    "StopRemoteAccessSessionRequestRequestTypeDef",
    "StopRunRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceInstanceRequestRequestTypeDef",
    "UpdateInstanceProfileRequestRequestTypeDef",
    "UpdateNetworkProfileRequestRequestTypeDef",
    "UpdateUploadRequestRequestTypeDef",
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    "AccountSettingsTypeDef",
    "CreateDevicePoolRequestRequestTypeDef",
    "DevicePoolTypeDef",
    "UpdateDevicePoolRequestRequestTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "ListArtifactsResultTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "DeviceInstanceTypeDef",
    "GetInstanceProfileResultTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "GetNetworkProfileResultTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "ProjectTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    "CreateTestGridProjectRequestRequestTypeDef",
    "TestGridProjectTypeDef",
    "UpdateTestGridProjectRequestRequestTypeDef",
    "CreateUploadResultTypeDef",
    "GetUploadResultTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "ListUploadsResultTypeDef",
    "UpdateUploadResultTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
    "DeviceSelectionResultPaginatorTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "SuiteTypeDef",
    "TestTypeDef",
    "GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef",
    "ListArtifactsRequestListArtifactsPaginateTypeDef",
    "ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef",
    "ListDevicePoolsRequestListDevicePoolsPaginateTypeDef",
    "ListDevicesRequestListDevicesPaginateTypeDef",
    "ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef",
    "ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef",
    "ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef",
    "ListOfferingsRequestListOfferingsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef",
    "ListRunsRequestListRunsPaginateTypeDef",
    "ListSamplesRequestListSamplesPaginateTypeDef",
    "ListSuitesRequestListSuitesPaginateTypeDef",
    "ListTestsRequestListTestsPaginateTypeDef",
    "ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef",
    "ListUploadsRequestListUploadsPaginateTypeDef",
    "ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef",
    "GetTestGridSessionResultTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListSamplesResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsRequestRequestTypeDef",
    "RecurringChargeTypeDef",
    "ProjectPaginatorTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "CreateDevicePoolResultTypeDef",
    "GetDevicePoolResultTypeDef",
    "ListDevicePoolsResultTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "DeviceTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "CreateProjectResultTypeDef",
    "GetProjectResultTypeDef",
    "ListProjectsResultTypeDef",
    "UpdateProjectResultTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "GetTestGridProjectResultTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "RunPaginatorTypeDef",
    "RunTypeDef",
    "GetSuiteResultTypeDef",
    "ListSuitesResultTypeDef",
    "GetTestResultTypeDef",
    "ListTestsResultTypeDef",
    "OfferingTypeDef",
    "ListProjectsResultPaginatorTypeDef",
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    "ScheduleRunRequestRequestTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "GetDeviceResultTypeDef",
    "JobTypeDef",
    "ListDevicesResultTypeDef",
    "ProblemTypeDef",
    "RemoteAccessSessionPaginatorTypeDef",
    "RemoteAccessSessionTypeDef",
    "ListRunsResultPaginatorTypeDef",
    "GetRunResultTypeDef",
    "ListRunsResultTypeDef",
    "ScheduleRunResultTypeDef",
    "StopRunResultTypeDef",
    "ListOfferingsResultTypeDef",
    "OfferingStatusTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetJobResultTypeDef",
    "ListJobsResultTypeDef",
    "StopJobResultTypeDef",
    "UniqueProblemTypeDef",
    "ListRemoteAccessSessionsResultPaginatorTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "GetOfferingStatusResultTypeDef",
    "OfferingTransactionTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RenewOfferingResultTypeDef",
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef",
    {
        "total": NotRequired[float],
        "remaining": NotRequired[float],
    },
)
ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ArtifactTypeType],
        "extension": NotRequired[str],
        "url": NotRequired[str],
    },
)
CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "frequency": NotRequired[str],
        "architecture": NotRequired[str],
        "clock": NotRequired[float],
    },
)
CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": NotRequired[int],
        "passed": NotRequired[int],
        "failed": NotRequired[int],
        "warned": NotRequired[int],
        "errored": NotRequired[int],
        "stopped": NotRequired[int],
        "skipped": NotRequired[int],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": NotRequired[DeviceAttributeType],
        "operator": NotRequired[RuleOperatorType],
        "value": NotRequired[str],
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
CreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "CreateInstanceProfileRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[Sequence[str]],
        "rebootAfterUse": NotRequired[bool],
    },
)
InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[List[str]],
        "rebootAfterUse": NotRequired[bool],
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
CreateNetworkProfileRequestRequestTypeDef = TypedDict(
    "CreateNetworkProfileRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)
CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {
        "billingMethod": NotRequired[BillingMethodType],
        "vpceConfigurationArns": NotRequired[Sequence[str]],
    },
)
TestGridVpcConfigTypeDef = TypedDict(
    "TestGridVpcConfigTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)
CreateTestGridUrlRequestRequestTypeDef = TypedDict(
    "CreateTestGridUrlRequestRequestTypeDef",
    {
        "projectArn": str,
        "expiresInSeconds": int,
    },
)
CreateUploadRequestRequestTypeDef = TypedDict(
    "CreateUploadRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "type": UploadTypeType,
        "contentType": NotRequired[str],
    },
)
UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "type": NotRequired[UploadTypeType],
        "status": NotRequired[UploadStatusType],
        "url": NotRequired[str],
        "metadata": NotRequired[str],
        "contentType": NotRequired[str],
        "message": NotRequired[str],
        "category": NotRequired[UploadCategoryType],
    },
)
CreateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "CreateVPCEConfigurationRequestRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": NotRequired[str],
    },
)
VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": NotRequired[str],
        "vpceConfigurationName": NotRequired[str],
        "vpceServiceName": NotRequired[str],
        "serviceDnsName": NotRequired[str],
        "vpceConfigurationDescription": NotRequired[str],
    },
)
CustomerArtifactPathsPaginatorTypeDef = TypedDict(
    "CustomerArtifactPathsPaginatorTypeDef",
    {
        "iosPaths": NotRequired[List[str]],
        "androidPaths": NotRequired[List[str]],
        "deviceHostPaths": NotRequired[List[str]],
    },
)
CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {
        "iosPaths": NotRequired[Sequence[str]],
        "androidPaths": NotRequired[Sequence[str]],
        "deviceHostPaths": NotRequired[Sequence[str]],
    },
)
DeleteDevicePoolRequestRequestTypeDef = TypedDict(
    "DeleteDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteNetworkProfileRequestRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteRunRequestRequestTypeDef = TypedDict(
    "DeleteRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteTestGridProjectRequestRequestTypeDef = TypedDict(
    "DeleteTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)
DeleteUploadRequestRequestTypeDef = TypedDict(
    "DeleteUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeviceFilterPaginatorTypeDef = TypedDict(
    "DeviceFilterPaginatorTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": Sequence[str],
    },
)
DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": List[str],
    },
)
DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef",
    {
        "total": NotRequired[float],
        "metered": NotRequired[float],
        "unmetered": NotRequired[float],
    },
)
IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": NotRequired[str],
        "type": NotRequired[DeviceAttributeType],
    },
)
ResolutionTypeDef = TypedDict(
    "ResolutionTypeDef",
    {
        "width": NotRequired[int],
        "height": NotRequired[int],
    },
)
ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": NotRequired[int],
        "accountsCleanup": NotRequired[bool],
        "appPackagesCleanup": NotRequired[bool],
        "videoCapture": NotRequired[bool],
        "skipAppResign": NotRequired[bool],
    },
)
GetDeviceInstanceRequestRequestTypeDef = TypedDict(
    "GetDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
ScheduleRunTestTypeDef = TypedDict(
    "ScheduleRunTestTypeDef",
    {
        "type": TestTypeType,
        "testPackageArn": NotRequired[str],
        "testSpecArn": NotRequired[str],
        "filter": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
GetDevicePoolRequestRequestTypeDef = TypedDict(
    "GetDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetNetworkProfileRequestRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
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
GetOfferingStatusRequestRequestTypeDef = TypedDict(
    "GetOfferingStatusRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "GetRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetRunRequestRequestTypeDef = TypedDict(
    "GetRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetSuiteRequestRequestTypeDef = TypedDict(
    "GetSuiteRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetTestGridProjectRequestRequestTypeDef = TypedDict(
    "GetTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)
GetTestGridSessionRequestRequestTypeDef = TypedDict(
    "GetTestGridSessionRequestRequestTypeDef",
    {
        "projectArn": NotRequired[str],
        "sessionId": NotRequired[str],
        "sessionArn": NotRequired[str],
    },
)
TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": NotRequired[str],
        "status": NotRequired[TestGridSessionStatusType],
        "created": NotRequired[datetime],
        "ended": NotRequired[datetime],
        "billingMinutes": NotRequired[float],
        "seleniumProperties": NotRequired[str],
    },
)
GetTestRequestRequestTypeDef = TypedDict(
    "GetTestRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetUploadRequestRequestTypeDef = TypedDict(
    "GetUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "GetVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
InstallToRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    {
        "remoteAccessSessionArn": str,
        "appArn": str,
    },
)
ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "nextToken": NotRequired[str],
    },
)
ListDeviceInstancesRequestRequestTypeDef = TypedDict(
    "ListDeviceInstancesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDevicePoolsRequestRequestTypeDef = TypedDict(
    "ListDevicePoolsRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "nextToken": NotRequired[str],
    },
)
ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListNetworkProfilesRequestRequestTypeDef = TypedDict(
    "ListNetworkProfilesRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "nextToken": NotRequired[str],
    },
)
ListOfferingPromotionsRequestRequestTypeDef = TypedDict(
    "ListOfferingPromotionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListOfferingTransactionsRequestRequestTypeDef = TypedDict(
    "ListOfferingTransactionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "arn": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListRemoteAccessSessionsRequestRequestTypeDef = TypedDict(
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListRunsRequestRequestTypeDef = TypedDict(
    "ListRunsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListSamplesRequestRequestTypeDef = TypedDict(
    "ListSamplesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[SampleTypeType],
        "url": NotRequired[str],
    },
)
ListSuitesRequestRequestTypeDef = TypedDict(
    "ListSuitesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ListTestGridProjectsRequestRequestTypeDef = TypedDict(
    "ListTestGridProjectsRequestRequestTypeDef",
    {
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTestGridSessionActionsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionActionsRequestRequestTypeDef",
    {
        "sessionArn": str,
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {
        "action": NotRequired[str],
        "started": NotRequired[datetime],
        "duration": NotRequired[int],
        "statusCode": NotRequired[str],
        "requestMethod": NotRequired[str],
    },
)
ListTestGridSessionArtifactsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    {
        "sessionArn": str,
        "type": NotRequired[TestGridSessionArtifactCategoryType],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {
        "filename": NotRequired[str],
        "type": NotRequired[TestGridSessionArtifactTypeType],
        "url": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ListTestsRequestRequestTypeDef = TypedDict(
    "ListTestsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListUniqueProblemsRequestRequestTypeDef = TypedDict(
    "ListUniqueProblemsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListUploadsRequestRequestTypeDef = TypedDict(
    "ListUploadsRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "nextToken": NotRequired[str],
    },
)
ListVPCEConfigurationsRequestRequestTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "latitude": float,
        "longitude": float,
    },
)
MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef",
    {
        "amount": NotRequired[float],
        "currencyCode": NotRequired[Literal["USD"]],
    },
)
ProblemDetailTypeDef = TypedDict(
    "ProblemDetailTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
    },
)
VpcConfigPaginatorTypeDef = TypedDict(
    "VpcConfigPaginatorTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)
PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
        "offeringPromotionId": NotRequired[str],
    },
)
RadiosTypeDef = TypedDict(
    "RadiosTypeDef",
    {
        "wifi": NotRequired[bool],
        "bluetooth": NotRequired[bool],
        "nfc": NotRequired[bool],
        "gps": NotRequired[bool],
    },
)
RenewOfferingRequestRequestTypeDef = TypedDict(
    "RenewOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)
StopJobRequestRequestTypeDef = TypedDict(
    "StopJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)
StopRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "StopRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
StopRunRequestRequestTypeDef = TypedDict(
    "StopRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDeviceInstanceRequestRequestTypeDef = TypedDict(
    "UpdateDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
        "profileArn": NotRequired[str],
        "labels": NotRequired[Sequence[str]],
    },
)
UpdateInstanceProfileRequestRequestTypeDef = TypedDict(
    "UpdateInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[Sequence[str]],
        "rebootAfterUse": NotRequired[bool],
    },
)
UpdateNetworkProfileRequestRequestTypeDef = TypedDict(
    "UpdateNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
UpdateUploadRequestRequestTypeDef = TypedDict(
    "UpdateUploadRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "contentType": NotRequired[str],
        "editContent": NotRequired[bool],
    },
)
UpdateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": NotRequired[str],
        "vpceServiceName": NotRequired[str],
        "serviceDnsName": NotRequired[str],
        "vpceConfigurationDescription": NotRequired[str],
    },
)
AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": NotRequired[str],
        "unmeteredDevices": NotRequired[Dict[DevicePlatformType, int]],
        "unmeteredRemoteAccessDevices": NotRequired[Dict[DevicePlatformType, int]],
        "maxJobTimeoutMinutes": NotRequired[int],
        "trialMinutes": NotRequired[TrialMinutesTypeDef],
        "maxSlots": NotRequired[Dict[str, int]],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "skipAppResign": NotRequired[bool],
    },
)
CreateDevicePoolRequestRequestTypeDef = TypedDict(
    "CreateDevicePoolRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "rules": Sequence[RuleTypeDef],
        "description": NotRequired[str],
        "maxDevices": NotRequired[int],
    },
)
DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[DevicePoolTypeType],
        "rules": NotRequired[List[RuleTypeDef]],
        "maxDevices": NotRequired[int],
    },
)
UpdateDevicePoolRequestRequestTypeDef = TypedDict(
    "UpdateDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "rules": NotRequired[Sequence[RuleTypeDef]],
        "maxDevices": NotRequired[int],
        "clearMaxDevices": NotRequired[bool],
    },
)
CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef",
    {
        "url": str,
        "expires": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {
        "artifacts": List[ArtifactTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef",
    {
        "instanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": NotRequired[str],
        "deviceArn": NotRequired[str],
        "labels": NotRequired[List[str]],
        "status": NotRequired[InstanceStatusType],
        "udid": NotRequired[str],
        "instanceProfile": NotRequired[InstanceProfileTypeDef],
    },
)
GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef",
    {
        "instanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {
        "instanceProfiles": List[InstanceProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef",
    {
        "instanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef",
    {
        "networkProfile": NetworkProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef",
    {
        "networkProfile": NetworkProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {
        "networkProfiles": List[NetworkProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef",
    {
        "networkProfile": NetworkProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "defaultJobTimeoutMinutes": NotRequired[int],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "created": NotRequired[datetime],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
CreateRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    {
        "projectArn": str,
        "deviceArn": str,
        "instanceArn": NotRequired[str],
        "sshPublicKey": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "name": NotRequired[str],
        "clientId": NotRequired[str],
        "configuration": NotRequired[CreateRemoteAccessSessionConfigurationTypeDef],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
    },
)
CreateTestGridProjectRequestRequestTypeDef = TypedDict(
    "CreateTestGridProjectRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "vpcConfig": NotRequired[TestGridVpcConfigTypeDef],
    },
)
TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "vpcConfig": NotRequired[TestGridVpcConfigTypeDef],
        "created": NotRequired[datetime],
    },
)
UpdateTestGridProjectRequestRequestTypeDef = TypedDict(
    "UpdateTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "vpcConfig": NotRequired[TestGridVpcConfigTypeDef],
    },
)
CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef",
    {
        "upload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef",
    {
        "upload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef",
    {
        "appUpload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef",
    {
        "uploads": List[UploadTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef",
    {
        "upload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": VPCEConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": VPCEConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {
        "vpceConfigurations": List[VPCEConfigurationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": VPCEConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeviceSelectionResultPaginatorTypeDef = TypedDict(
    "DeviceSelectionResultPaginatorTypeDef",
    {
        "filters": NotRequired[List[DeviceFilterPaginatorTypeDef]],
        "matchedDevicesCount": NotRequired[int],
        "maxDevices": NotRequired[int],
    },
)
DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {
        "filters": Sequence[DeviceFilterTypeDef],
        "maxDevices": int,
    },
)
DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {
        "filters": NotRequired[List[DeviceFilterTypeDef]],
        "matchedDevicesCount": NotRequired[int],
        "maxDevices": NotRequired[int],
    },
)
ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "arn": NotRequired[str],
        "nextToken": NotRequired[str],
        "filters": NotRequired[Sequence[DeviceFilterTypeDef]],
    },
)
SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
    },
)
TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
    },
)
GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef = TypedDict(
    "GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListArtifactsRequestListArtifactsPaginateTypeDef = TypedDict(
    "ListArtifactsRequestListArtifactsPaginateTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef = TypedDict(
    "ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicePoolsRequestListDevicePoolsPaginateTypeDef = TypedDict(
    "ListDevicePoolsRequestListDevicePoolsPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicesRequestListDevicesPaginateTypeDef = TypedDict(
    "ListDevicesRequestListDevicesPaginateTypeDef",
    {
        "arn": NotRequired[str],
        "filters": NotRequired[Sequence[DeviceFilterPaginatorTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef = TypedDict(
    "ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef = TypedDict(
    "ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef = TypedDict(
    "ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef = TypedDict(
    "ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingsRequestListOfferingsPaginateTypeDef = TypedDict(
    "ListOfferingsRequestListOfferingsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "arn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef = TypedDict(
    "ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRunsRequestListRunsPaginateTypeDef = TypedDict(
    "ListRunsRequestListRunsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSamplesRequestListSamplesPaginateTypeDef = TypedDict(
    "ListSamplesRequestListSamplesPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSuitesRequestListSuitesPaginateTypeDef = TypedDict(
    "ListSuitesRequestListSuitesPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestsRequestListTestsPaginateTypeDef = TypedDict(
    "ListTestsRequestListTestsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef = TypedDict(
    "ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUploadsRequestListUploadsPaginateTypeDef = TypedDict(
    "ListUploadsRequestListUploadsPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef",
    {
        "testGridSession": TestGridSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {
        "testGridSessions": List[TestGridSessionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {
        "offeringPromotions": List[OfferingPromotionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef",
    {
        "samples": List[SampleTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {
        "actions": List[TestGridSessionActionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {
        "artifacts": List[TestGridSessionArtifactTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridSessionsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionsRequestRequestTypeDef",
    {
        "projectArn": str,
        "status": NotRequired[TestGridSessionStatusType],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "endTimeAfter": NotRequired[TimestampTypeDef],
        "endTimeBefore": NotRequired[TimestampTypeDef],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "cost": NotRequired[MonetaryAmountTypeDef],
        "frequency": NotRequired[Literal["MONTHLY"]],
    },
)
ProjectPaginatorTypeDef = TypedDict(
    "ProjectPaginatorTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "created": NotRequired[datetime],
        "vpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": NotRequired[str],
        "networkProfileArn": NotRequired[str],
        "locale": NotRequired[str],
        "location": NotRequired[LocationTypeDef],
        "vpceConfigurationArns": NotRequired[Sequence[str]],
        "customerArtifactPaths": NotRequired[CustomerArtifactPathsTypeDef],
        "radios": NotRequired[RadiosTypeDef],
        "auxiliaryApps": NotRequired[Sequence[str]],
        "billingMethod": NotRequired[BillingMethodType],
    },
)
GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef",
    {
        "accountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef",
    {
        "devicePool": DevicePoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef",
    {
        "devicePool": DevicePoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {
        "devicePools": List[DevicePoolTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef",
    {
        "devicePool": DevicePoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "manufacturer": NotRequired[str],
        "model": NotRequired[str],
        "modelId": NotRequired[str],
        "formFactor": NotRequired[DeviceFormFactorType],
        "platform": NotRequired[DevicePlatformType],
        "os": NotRequired[str],
        "cpu": NotRequired[CPUTypeDef],
        "resolution": NotRequired[ResolutionTypeDef],
        "heapSize": NotRequired[int],
        "memory": NotRequired[int],
        "image": NotRequired[str],
        "carrier": NotRequired[str],
        "radio": NotRequired[str],
        "remoteAccessEnabled": NotRequired[bool],
        "remoteDebugEnabled": NotRequired[bool],
        "fleetType": NotRequired[str],
        "fleetName": NotRequired[str],
        "instances": NotRequired[List[DeviceInstanceTypeDef]],
        "availability": NotRequired[DeviceAvailabilityType],
    },
)
GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef",
    {
        "deviceInstance": DeviceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {
        "deviceInstances": List[DeviceInstanceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef",
    {
        "deviceInstance": DeviceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List[ProjectTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef",
    {
        "testGridProject": TestGridProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef",
    {
        "testGridProject": TestGridProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {
        "testGridProjects": List[TestGridProjectTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef",
    {
        "testGridProject": TestGridProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunPaginatorTypeDef = TypedDict(
    "RunPaginatorTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "platform": NotRequired[DevicePlatformType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "totalJobs": NotRequired[int],
        "completedJobs": NotRequired[int],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "networkProfile": NotRequired[NetworkProfileTypeDef],
        "parsingResultUrl": NotRequired[str],
        "resultCode": NotRequired[ExecutionResultCodeType],
        "seed": NotRequired[int],
        "appUpload": NotRequired[str],
        "eventCount": NotRequired[int],
        "jobTimeoutMinutes": NotRequired[int],
        "devicePoolArn": NotRequired[str],
        "locale": NotRequired[str],
        "radios": NotRequired[RadiosTypeDef],
        "location": NotRequired[LocationTypeDef],
        "customerArtifactPaths": NotRequired[CustomerArtifactPathsPaginatorTypeDef],
        "webUrl": NotRequired[str],
        "skipAppResign": NotRequired[bool],
        "testSpecArn": NotRequired[str],
        "deviceSelectionResult": NotRequired[DeviceSelectionResultPaginatorTypeDef],
        "vpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "platform": NotRequired[DevicePlatformType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "totalJobs": NotRequired[int],
        "completedJobs": NotRequired[int],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "networkProfile": NotRequired[NetworkProfileTypeDef],
        "parsingResultUrl": NotRequired[str],
        "resultCode": NotRequired[ExecutionResultCodeType],
        "seed": NotRequired[int],
        "appUpload": NotRequired[str],
        "eventCount": NotRequired[int],
        "jobTimeoutMinutes": NotRequired[int],
        "devicePoolArn": NotRequired[str],
        "locale": NotRequired[str],
        "radios": NotRequired[RadiosTypeDef],
        "location": NotRequired[LocationTypeDef],
        "customerArtifactPaths": NotRequired[CustomerArtifactPathsTypeDef],
        "webUrl": NotRequired[str],
        "skipAppResign": NotRequired[bool],
        "testSpecArn": NotRequired[str],
        "deviceSelectionResult": NotRequired[DeviceSelectionResultTypeDef],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
GetSuiteResultTypeDef = TypedDict(
    "GetSuiteResultTypeDef",
    {
        "suite": SuiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef",
    {
        "suites": List[SuiteTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTestResultTypeDef = TypedDict(
    "GetTestResultTypeDef",
    {
        "test": TestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef",
    {
        "tests": List[TestTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[Literal["RECURRING"]],
        "platform": NotRequired[DevicePlatformType],
        "recurringCharges": NotRequired[List[RecurringChargeTypeDef]],
    },
)
ListProjectsResultPaginatorTypeDef = TypedDict(
    "ListProjectsResultPaginatorTypeDef",
    {
        "projects": List[ProjectPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicePoolCompatibilityRequestRequestTypeDef = TypedDict(
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    {
        "devicePoolArn": str,
        "appArn": NotRequired[str],
        "testType": NotRequired[TestTypeType],
        "test": NotRequired[ScheduleRunTestTypeDef],
        "configuration": NotRequired[ScheduleRunConfigurationTypeDef],
    },
)
ScheduleRunRequestRequestTypeDef = TypedDict(
    "ScheduleRunRequestRequestTypeDef",
    {
        "projectArn": str,
        "test": ScheduleRunTestTypeDef,
        "appArn": NotRequired[str],
        "devicePoolArn": NotRequired[str],
        "deviceSelectionConfiguration": NotRequired[DeviceSelectionConfigurationTypeDef],
        "name": NotRequired[str],
        "configuration": NotRequired[ScheduleRunConfigurationTypeDef],
        "executionConfiguration": NotRequired[ExecutionConfigurationTypeDef],
    },
)
DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": NotRequired[DeviceTypeDef],
        "compatible": NotRequired[bool],
        "incompatibilityMessages": NotRequired[List[IncompatibilityMessageTypeDef]],
    },
)
GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef",
    {
        "device": DeviceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "device": NotRequired[DeviceTypeDef],
        "instanceArn": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "videoEndpoint": NotRequired[str],
        "videoCapture": NotRequired[bool],
    },
)
ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef",
    {
        "devices": List[DeviceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": NotRequired[ProblemDetailTypeDef],
        "job": NotRequired[ProblemDetailTypeDef],
        "suite": NotRequired[ProblemDetailTypeDef],
        "test": NotRequired[ProblemDetailTypeDef],
        "device": NotRequired[DeviceTypeDef],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
    },
)
RemoteAccessSessionPaginatorTypeDef = TypedDict(
    "RemoteAccessSessionPaginatorTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "device": NotRequired[DeviceTypeDef],
        "instanceArn": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "hostAddress": NotRequired[str],
        "clientId": NotRequired[str],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "endpoint": NotRequired[str],
        "deviceUdid": NotRequired[str],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
        "vpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "device": NotRequired[DeviceTypeDef],
        "instanceArn": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "hostAddress": NotRequired[str],
        "clientId": NotRequired[str],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "endpoint": NotRequired[str],
        "deviceUdid": NotRequired[str],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
ListRunsResultPaginatorTypeDef = TypedDict(
    "ListRunsResultPaginatorTypeDef",
    {
        "runs": List[RunPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRunResultTypeDef = TypedDict(
    "GetRunResultTypeDef",
    {
        "run": RunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef",
    {
        "runs": List[RunTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleRunResultTypeDef = TypedDict(
    "ScheduleRunResultTypeDef",
    {
        "run": RunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRunResultTypeDef = TypedDict(
    "StopRunResultTypeDef",
    {
        "run": RunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {
        "offerings": List[OfferingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": NotRequired[OfferingTransactionTypeType],
        "offering": NotRequired[OfferingTypeDef],
        "quantity": NotRequired[int],
        "effectiveOn": NotRequired[datetime],
    },
)
GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List[DevicePoolCompatibilityResultTypeDef],
        "incompatibleDevices": List[DevicePoolCompatibilityResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobResultTypeDef = TypedDict(
    "GetJobResultTypeDef",
    {
        "job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "jobs": List[JobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopJobResultTypeDef = TypedDict(
    "StopJobResultTypeDef",
    {
        "job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef",
    {
        "message": NotRequired[str],
        "problems": NotRequired[List[ProblemTypeDef]],
    },
)
ListRemoteAccessSessionsResultPaginatorTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultPaginatorTypeDef",
    {
        "remoteAccessSessions": List[RemoteAccessSessionPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": RemoteAccessSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": RemoteAccessSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {
        "remoteAccessSessions": List[RemoteAccessSessionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": RemoteAccessSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, OfferingStatusTypeDef],
        "nextPeriod": Dict[str, OfferingStatusTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": NotRequired[OfferingStatusTypeDef],
        "transactionId": NotRequired[str],
        "offeringPromotionId": NotRequired[str],
        "createdOn": NotRequired[datetime],
        "cost": NotRequired[MonetaryAmountTypeDef],
    },
)
ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[ExecutionResultType, List[UniqueProblemTypeDef]],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {
        "offeringTransactions": List[OfferingTransactionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {
        "offeringTransaction": OfferingTransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef",
    {
        "offeringTransaction": OfferingTransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
