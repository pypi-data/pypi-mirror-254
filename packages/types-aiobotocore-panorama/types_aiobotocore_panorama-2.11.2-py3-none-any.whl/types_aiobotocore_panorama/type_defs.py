"""
Type annotations for panorama service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_panorama/type_defs/)

Usage::

    ```python
    from types_aiobotocore_panorama.type_defs import AlternateSoftwareMetadataTypeDef

    data: AlternateSoftwareMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ApplicationInstanceHealthStatusType,
    ApplicationInstanceStatusType,
    ConnectionTypeType,
    DesiredStateType,
    DeviceAggregatedStatusType,
    DeviceBrandType,
    DeviceConnectionStatusType,
    DeviceReportedStatusType,
    DeviceStatusType,
    DeviceTypeType,
    JobTypeType,
    ListDevicesSortByType,
    NetworkConnectionStatusType,
    NodeCategoryType,
    NodeFromTemplateJobStatusType,
    NodeInstanceStatusType,
    NodeSignalValueType,
    PackageImportJobStatusType,
    PackageImportJobTypeType,
    PackageVersionStatusType,
    PortTypeType,
    SortOrderType,
    StatusFilterType,
    UpdateProgressType,
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
    "AlternateSoftwareMetadataTypeDef",
    "ReportedRuntimeContextStateTypeDef",
    "ManifestOverridesPayloadTypeDef",
    "ManifestPayloadTypeDef",
    "ResponseMetadataTypeDef",
    "JobTypeDef",
    "JobResourceTagsTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "StorageLocationTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeregisterPackageVersionRequestRequestTypeDef",
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    "DescribeApplicationInstanceRequestRequestTypeDef",
    "DescribeDeviceJobRequestRequestTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "LatestDeviceJobTypeDef",
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    "DescribeNodeRequestRequestTypeDef",
    "DescribePackageImportJobRequestRequestTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "OTAJobConfigTypeDef",
    "DeviceJobTypeDef",
    "StaticIpConnectionInfoTypeDef",
    "EthernetStatusTypeDef",
    "ListApplicationInstanceDependenciesRequestRequestTypeDef",
    "PackageObjectTypeDef",
    "ListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    "NodeInstanceTypeDef",
    "ListApplicationInstancesRequestRequestTypeDef",
    "ListDevicesJobsRequestRequestTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    "NodeFromTemplateJobTypeDef",
    "ListNodesRequestRequestTypeDef",
    "NodeTypeDef",
    "ListPackageImportJobsRequestRequestTypeDef",
    "PackageImportJobTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "PackageListItemTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NtpPayloadTypeDef",
    "NtpStatusTypeDef",
    "NodeInputPortTypeDef",
    "NodeOutputPortTypeDef",
    "NodeSignalTypeDef",
    "OutPutS3LocationTypeDef",
    "PackageVersionOutputConfigTypeDef",
    "S3LocationTypeDef",
    "RegisterPackageVersionRequestRequestTypeDef",
    "RemoveApplicationInstanceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceMetadataRequestRequestTypeDef",
    "ApplicationInstanceTypeDef",
    "CreateApplicationInstanceRequestRequestTypeDef",
    "CreateApplicationInstanceResponseTypeDef",
    "CreateNodeFromTemplateJobResponseTypeDef",
    "CreatePackageImportJobResponseTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    "DescribeApplicationInstanceResponseTypeDef",
    "DescribeDeviceJobResponseTypeDef",
    "DescribePackageVersionResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ProvisionDeviceResponseTypeDef",
    "SignalApplicationInstanceNodeInstancesResponseTypeDef",
    "UpdateDeviceMetadataResponseTypeDef",
    "CreateJobForDevicesResponseTypeDef",
    "CreateNodeFromTemplateJobRequestRequestTypeDef",
    "DescribeNodeFromTemplateJobResponseTypeDef",
    "CreatePackageResponseTypeDef",
    "DescribePackageResponseTypeDef",
    "DeviceTypeDef",
    "DeviceJobConfigTypeDef",
    "ListDevicesJobsResponseTypeDef",
    "EthernetPayloadTypeDef",
    "ListApplicationInstanceDependenciesResponseTypeDef",
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    "ListNodeFromTemplateJobsResponseTypeDef",
    "ListNodesResponseTypeDef",
    "ListPackageImportJobsResponseTypeDef",
    "ListPackagesResponseTypeDef",
    "NetworkStatusTypeDef",
    "NodeInterfaceTypeDef",
    "SignalApplicationInstanceNodeInstancesRequestRequestTypeDef",
    "PackageImportJobOutputTypeDef",
    "PackageImportJobOutputConfigTypeDef",
    "PackageVersionInputConfigTypeDef",
    "ListApplicationInstancesResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "CreateJobForDevicesRequestRequestTypeDef",
    "NetworkPayloadTypeDef",
    "DescribeNodeResponseTypeDef",
    "PackageImportJobInputConfigTypeDef",
    "DescribeDeviceResponseTypeDef",
    "ProvisionDeviceRequestRequestTypeDef",
    "CreatePackageImportJobRequestRequestTypeDef",
    "DescribePackageImportJobResponseTypeDef",
)

AlternateSoftwareMetadataTypeDef = TypedDict(
    "AlternateSoftwareMetadataTypeDef",
    {
        "Version": NotRequired[str],
    },
)
ReportedRuntimeContextStateTypeDef = TypedDict(
    "ReportedRuntimeContextStateTypeDef",
    {
        "DesiredState": DesiredStateType,
        "DeviceReportedStatus": DeviceReportedStatusType,
        "DeviceReportedTime": datetime,
        "RuntimeContextName": str,
    },
)
ManifestOverridesPayloadTypeDef = TypedDict(
    "ManifestOverridesPayloadTypeDef",
    {
        "PayloadData": NotRequired[str],
    },
)
ManifestPayloadTypeDef = TypedDict(
    "ManifestPayloadTypeDef",
    {
        "PayloadData": NotRequired[str],
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
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "DeviceId": NotRequired[str],
        "JobId": NotRequired[str],
    },
)
JobResourceTagsTypeDef = TypedDict(
    "JobResourceTagsTypeDef",
    {
        "ResourceType": Literal["PACKAGE"],
        "Tags": Mapping[str, str],
    },
)
CreatePackageRequestRequestTypeDef = TypedDict(
    "CreatePackageRequestRequestTypeDef",
    {
        "PackageName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "BinaryPrefixLocation": str,
        "Bucket": str,
        "GeneratedPrefixLocation": str,
        "ManifestPrefixLocation": str,
        "RepoPrefixLocation": str,
    },
)
DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
DeletePackageRequestRequestTypeDef = TypedDict(
    "DeletePackageRequestRequestTypeDef",
    {
        "PackageId": str,
        "ForceDelete": NotRequired[bool],
    },
)
DeregisterPackageVersionRequestRequestTypeDef = TypedDict(
    "DeregisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "OwnerAccount": NotRequired[str],
        "UpdatedLatestPatchVersion": NotRequired[str],
    },
)
DescribeApplicationInstanceDetailsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)
DescribeApplicationInstanceRequestRequestTypeDef = TypedDict(
    "DescribeApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
    },
)
DescribeDeviceJobRequestRequestTypeDef = TypedDict(
    "DescribeDeviceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
LatestDeviceJobTypeDef = TypedDict(
    "LatestDeviceJobTypeDef",
    {
        "ImageVersion": NotRequired[str],
        "JobType": NotRequired[JobTypeType],
        "Status": NotRequired[UpdateProgressType],
    },
)
DescribeNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeNodeRequestRequestTypeDef = TypedDict(
    "DescribeNodeRequestRequestTypeDef",
    {
        "NodeId": str,
        "OwnerAccount": NotRequired[str],
    },
)
DescribePackageImportJobRequestRequestTypeDef = TypedDict(
    "DescribePackageImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribePackageRequestRequestTypeDef = TypedDict(
    "DescribePackageRequestRequestTypeDef",
    {
        "PackageId": str,
    },
)
DescribePackageVersionRequestRequestTypeDef = TypedDict(
    "DescribePackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "OwnerAccount": NotRequired[str],
        "PatchVersion": NotRequired[str],
    },
)
OTAJobConfigTypeDef = TypedDict(
    "OTAJobConfigTypeDef",
    {
        "ImageVersion": str,
        "AllowMajorVersionUpdate": NotRequired[bool],
    },
)
DeviceJobTypeDef = TypedDict(
    "DeviceJobTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "DeviceId": NotRequired[str],
        "DeviceName": NotRequired[str],
        "JobId": NotRequired[str],
        "JobType": NotRequired[JobTypeType],
    },
)
StaticIpConnectionInfoTypeDef = TypedDict(
    "StaticIpConnectionInfoTypeDef",
    {
        "DefaultGateway": str,
        "Dns": List[str],
        "IpAddress": str,
        "Mask": str,
    },
)
EthernetStatusTypeDef = TypedDict(
    "EthernetStatusTypeDef",
    {
        "ConnectionStatus": NotRequired[NetworkConnectionStatusType],
        "HwAddress": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)
ListApplicationInstanceDependenciesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstanceDependenciesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PackageObjectTypeDef = TypedDict(
    "PackageObjectTypeDef",
    {
        "Name": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
ListApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NodeInstanceTypeDef = TypedDict(
    "NodeInstanceTypeDef",
    {
        "CurrentStatus": NodeInstanceStatusType,
        "NodeInstanceId": str,
        "NodeId": NotRequired[str],
        "NodeName": NotRequired[str],
        "PackageName": NotRequired[str],
        "PackagePatchVersion": NotRequired[str],
        "PackageVersion": NotRequired[str],
    },
)
ListApplicationInstancesRequestRequestTypeDef = TypedDict(
    "ListApplicationInstancesRequestRequestTypeDef",
    {
        "DeviceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StatusFilter": NotRequired[StatusFilterType],
    },
)
ListDevicesJobsRequestRequestTypeDef = TypedDict(
    "ListDevicesJobsRequestRequestTypeDef",
    {
        "DeviceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceAggregatedStatusFilter": NotRequired[DeviceAggregatedStatusType],
        "MaxResults": NotRequired[int],
        "NameFilter": NotRequired[str],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ListDevicesSortByType],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ListNodeFromTemplateJobsRequestRequestTypeDef = TypedDict(
    "ListNodeFromTemplateJobsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NodeFromTemplateJobTypeDef = TypedDict(
    "NodeFromTemplateJobTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "JobId": NotRequired[str],
        "NodeName": NotRequired[str],
        "Status": NotRequired[NodeFromTemplateJobStatusType],
        "StatusMessage": NotRequired[str],
        "TemplateType": NotRequired[Literal["RTSP_CAMERA_STREAM"]],
    },
)
ListNodesRequestRequestTypeDef = TypedDict(
    "ListNodesRequestRequestTypeDef",
    {
        "Category": NotRequired[NodeCategoryType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "PackageName": NotRequired[str],
        "PackageVersion": NotRequired[str],
        "PatchVersion": NotRequired[str],
    },
)
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "Description": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "PackageArn": NotRequired[str],
    },
)
ListPackageImportJobsRequestRequestTypeDef = TypedDict(
    "ListPackageImportJobsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PackageImportJobTypeDef = TypedDict(
    "PackageImportJobTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "JobId": NotRequired[str],
        "JobType": NotRequired[PackageImportJobTypeType],
        "LastUpdatedTime": NotRequired[datetime],
        "Status": NotRequired[PackageImportJobStatusType],
        "StatusMessage": NotRequired[str],
    },
)
ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PackageListItemTypeDef = TypedDict(
    "PackageListItemTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "PackageId": NotRequired[str],
        "PackageName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
NtpPayloadTypeDef = TypedDict(
    "NtpPayloadTypeDef",
    {
        "NtpServers": List[str],
    },
)
NtpStatusTypeDef = TypedDict(
    "NtpStatusTypeDef",
    {
        "ConnectionStatus": NotRequired[NetworkConnectionStatusType],
        "IpAddress": NotRequired[str],
        "NtpServerName": NotRequired[str],
    },
)
NodeInputPortTypeDef = TypedDict(
    "NodeInputPortTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "MaxConnections": NotRequired[int],
        "Name": NotRequired[str],
        "Type": NotRequired[PortTypeType],
    },
)
NodeOutputPortTypeDef = TypedDict(
    "NodeOutputPortTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[PortTypeType],
    },
)
NodeSignalTypeDef = TypedDict(
    "NodeSignalTypeDef",
    {
        "NodeInstanceId": str,
        "Signal": NodeSignalValueType,
    },
)
OutPutS3LocationTypeDef = TypedDict(
    "OutPutS3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
    },
)
PackageVersionOutputConfigTypeDef = TypedDict(
    "PackageVersionOutputConfigTypeDef",
    {
        "PackageName": str,
        "PackageVersion": str,
        "MarkLatest": NotRequired[bool],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "ObjectKey": str,
        "Region": NotRequired[str],
    },
)
RegisterPackageVersionRequestRequestTypeDef = TypedDict(
    "RegisterPackageVersionRequestRequestTypeDef",
    {
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "MarkLatest": NotRequired[bool],
        "OwnerAccount": NotRequired[str],
    },
)
RemoveApplicationInstanceRequestRequestTypeDef = TypedDict(
    "RemoveApplicationInstanceRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
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
UpdateDeviceMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDeviceMetadataRequestRequestTypeDef",
    {
        "DeviceId": str,
        "Description": NotRequired[str],
    },
)
ApplicationInstanceTypeDef = TypedDict(
    "ApplicationInstanceTypeDef",
    {
        "ApplicationInstanceId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "DefaultRuntimeContextDevice": NotRequired[str],
        "DefaultRuntimeContextDeviceName": NotRequired[str],
        "Description": NotRequired[str],
        "HealthStatus": NotRequired[ApplicationInstanceHealthStatusType],
        "Name": NotRequired[str],
        "RuntimeContextStates": NotRequired[List[ReportedRuntimeContextStateTypeDef]],
        "Status": NotRequired[ApplicationInstanceStatusType],
        "StatusDescription": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateApplicationInstanceRequestRequestTypeDef = TypedDict(
    "CreateApplicationInstanceRequestRequestTypeDef",
    {
        "DefaultRuntimeContextDevice": str,
        "ManifestPayload": ManifestPayloadTypeDef,
        "ApplicationInstanceIdToReplace": NotRequired[str],
        "Description": NotRequired[str],
        "ManifestOverridesPayload": NotRequired[ManifestOverridesPayloadTypeDef],
        "Name": NotRequired[str],
        "RuntimeRoleArn": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateApplicationInstanceResponseTypeDef = TypedDict(
    "CreateApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNodeFromTemplateJobResponseTypeDef = TypedDict(
    "CreateNodeFromTemplateJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePackageImportJobResponseTypeDef = TypedDict(
    "CreatePackageImportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApplicationInstanceDetailsResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceDetailsResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "Description": str,
        "ManifestOverridesPayload": ManifestOverridesPayloadTypeDef,
        "ManifestPayload": ManifestPayloadTypeDef,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApplicationInstanceResponseTypeDef = TypedDict(
    "DescribeApplicationInstanceResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ApplicationInstanceIdToReplace": str,
        "Arn": str,
        "CreatedTime": datetime,
        "DefaultRuntimeContextDevice": str,
        "DefaultRuntimeContextDeviceName": str,
        "Description": str,
        "HealthStatus": ApplicationInstanceHealthStatusType,
        "LastUpdatedTime": datetime,
        "Name": str,
        "RuntimeContextStates": List[ReportedRuntimeContextStateTypeDef],
        "RuntimeRoleArn": str,
        "Status": ApplicationInstanceStatusType,
        "StatusDescription": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDeviceJobResponseTypeDef = TypedDict(
    "DescribeDeviceJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "DeviceArn": str,
        "DeviceId": str,
        "DeviceName": str,
        "DeviceType": DeviceTypeType,
        "ImageVersion": str,
        "JobId": str,
        "JobType": JobTypeType,
        "Status": UpdateProgressType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackageVersionResponseTypeDef = TypedDict(
    "DescribePackageVersionResponseTypeDef",
    {
        "IsLatestPatch": bool,
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "RegisteredTime": datetime,
        "Status": PackageVersionStatusType,
        "StatusDescription": str,
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
ProvisionDeviceResponseTypeDef = TypedDict(
    "ProvisionDeviceResponseTypeDef",
    {
        "Arn": str,
        "Certificates": bytes,
        "DeviceId": str,
        "IotThingName": str,
        "Status": DeviceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SignalApplicationInstanceNodeInstancesResponseTypeDef = TypedDict(
    "SignalApplicationInstanceNodeInstancesResponseTypeDef",
    {
        "ApplicationInstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDeviceMetadataResponseTypeDef = TypedDict(
    "UpdateDeviceMetadataResponseTypeDef",
    {
        "DeviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobForDevicesResponseTypeDef = TypedDict(
    "CreateJobForDevicesResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNodeFromTemplateJobRequestRequestTypeDef = TypedDict(
    "CreateNodeFromTemplateJobRequestRequestTypeDef",
    {
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "TemplateParameters": Mapping[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "JobTags": NotRequired[Sequence[JobResourceTagsTypeDef]],
        "NodeDescription": NotRequired[str],
    },
)
DescribeNodeFromTemplateJobResponseTypeDef = TypedDict(
    "DescribeNodeFromTemplateJobResponseTypeDef",
    {
        "CreatedTime": datetime,
        "JobId": str,
        "JobTags": List[JobResourceTagsTypeDef],
        "LastUpdatedTime": datetime,
        "NodeDescription": str,
        "NodeName": str,
        "OutputPackageName": str,
        "OutputPackageVersion": str,
        "Status": NodeFromTemplateJobStatusType,
        "StatusMessage": str,
        "TemplateParameters": Dict[str, str],
        "TemplateType": Literal["RTSP_CAMERA_STREAM"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef",
    {
        "Arn": str,
        "PackageId": str,
        "StorageLocation": StorageLocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackageResponseTypeDef = TypedDict(
    "DescribePackageResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "PackageId": str,
        "PackageName": str,
        "ReadAccessPrincipalArns": List[str],
        "StorageLocation": StorageLocationTypeDef,
        "Tags": Dict[str, str],
        "WriteAccessPrincipalArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Brand": NotRequired[DeviceBrandType],
        "CreatedTime": NotRequired[datetime],
        "CurrentSoftware": NotRequired[str],
        "Description": NotRequired[str],
        "DeviceAggregatedStatus": NotRequired[DeviceAggregatedStatusType],
        "DeviceId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "LatestDeviceJob": NotRequired[LatestDeviceJobTypeDef],
        "LeaseExpirationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "ProvisioningStatus": NotRequired[DeviceStatusType],
        "Tags": NotRequired[Dict[str, str]],
        "Type": NotRequired[DeviceTypeType],
    },
)
DeviceJobConfigTypeDef = TypedDict(
    "DeviceJobConfigTypeDef",
    {
        "OTAJobConfig": NotRequired[OTAJobConfigTypeDef],
    },
)
ListDevicesJobsResponseTypeDef = TypedDict(
    "ListDevicesJobsResponseTypeDef",
    {
        "DeviceJobs": List[DeviceJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EthernetPayloadTypeDef = TypedDict(
    "EthernetPayloadTypeDef",
    {
        "ConnectionType": ConnectionTypeType,
        "StaticIpConnectionInfo": NotRequired[StaticIpConnectionInfoTypeDef],
    },
)
ListApplicationInstanceDependenciesResponseTypeDef = TypedDict(
    "ListApplicationInstanceDependenciesResponseTypeDef",
    {
        "NextToken": str,
        "PackageObjects": List[PackageObjectTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationInstanceNodeInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstanceNodeInstancesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInstances": List[NodeInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNodeFromTemplateJobsResponseTypeDef = TypedDict(
    "ListNodeFromTemplateJobsResponseTypeDef",
    {
        "NextToken": str,
        "NodeFromTemplateJobs": List[NodeFromTemplateJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "Nodes": List[NodeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPackageImportJobsResponseTypeDef = TypedDict(
    "ListPackageImportJobsResponseTypeDef",
    {
        "NextToken": str,
        "PackageImportJobs": List[PackageImportJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPackagesResponseTypeDef = TypedDict(
    "ListPackagesResponseTypeDef",
    {
        "NextToken": str,
        "Packages": List[PackageListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkStatusTypeDef = TypedDict(
    "NetworkStatusTypeDef",
    {
        "Ethernet0Status": NotRequired[EthernetStatusTypeDef],
        "Ethernet1Status": NotRequired[EthernetStatusTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "NtpStatus": NotRequired[NtpStatusTypeDef],
    },
)
NodeInterfaceTypeDef = TypedDict(
    "NodeInterfaceTypeDef",
    {
        "Inputs": List[NodeInputPortTypeDef],
        "Outputs": List[NodeOutputPortTypeDef],
    },
)
SignalApplicationInstanceNodeInstancesRequestRequestTypeDef = TypedDict(
    "SignalApplicationInstanceNodeInstancesRequestRequestTypeDef",
    {
        "ApplicationInstanceId": str,
        "NodeSignals": Sequence[NodeSignalTypeDef],
    },
)
PackageImportJobOutputTypeDef = TypedDict(
    "PackageImportJobOutputTypeDef",
    {
        "OutputS3Location": OutPutS3LocationTypeDef,
        "PackageId": str,
        "PackageVersion": str,
        "PatchVersion": str,
    },
)
PackageImportJobOutputConfigTypeDef = TypedDict(
    "PackageImportJobOutputConfigTypeDef",
    {
        "PackageVersionOutputConfig": NotRequired[PackageVersionOutputConfigTypeDef],
    },
)
PackageVersionInputConfigTypeDef = TypedDict(
    "PackageVersionInputConfigTypeDef",
    {
        "S3Location": S3LocationTypeDef,
    },
)
ListApplicationInstancesResponseTypeDef = TypedDict(
    "ListApplicationInstancesResponseTypeDef",
    {
        "ApplicationInstances": List[ApplicationInstanceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobForDevicesRequestRequestTypeDef = TypedDict(
    "CreateJobForDevicesRequestRequestTypeDef",
    {
        "DeviceIds": Sequence[str],
        "JobType": JobTypeType,
        "DeviceJobConfig": NotRequired[DeviceJobConfigTypeDef],
    },
)
NetworkPayloadTypeDef = TypedDict(
    "NetworkPayloadTypeDef",
    {
        "Ethernet0": NotRequired[EthernetPayloadTypeDef],
        "Ethernet1": NotRequired[EthernetPayloadTypeDef],
        "Ntp": NotRequired[NtpPayloadTypeDef],
    },
)
DescribeNodeResponseTypeDef = TypedDict(
    "DescribeNodeResponseTypeDef",
    {
        "AssetName": str,
        "Category": NodeCategoryType,
        "CreatedTime": datetime,
        "Description": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NodeId": str,
        "NodeInterface": NodeInterfaceTypeDef,
        "OwnerAccount": str,
        "PackageArn": str,
        "PackageId": str,
        "PackageName": str,
        "PackageVersion": str,
        "PatchVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PackageImportJobInputConfigTypeDef = TypedDict(
    "PackageImportJobInputConfigTypeDef",
    {
        "PackageVersionInputConfig": NotRequired[PackageVersionInputConfigTypeDef],
    },
)
DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "AlternateSoftwares": List[AlternateSoftwareMetadataTypeDef],
        "Arn": str,
        "Brand": DeviceBrandType,
        "CreatedTime": datetime,
        "CurrentNetworkingStatus": NetworkStatusTypeDef,
        "CurrentSoftware": str,
        "Description": str,
        "DeviceAggregatedStatus": DeviceAggregatedStatusType,
        "DeviceConnectionStatus": DeviceConnectionStatusType,
        "DeviceId": str,
        "LatestAlternateSoftware": str,
        "LatestDeviceJob": LatestDeviceJobTypeDef,
        "LatestSoftware": str,
        "LeaseExpirationTime": datetime,
        "Name": str,
        "NetworkingConfiguration": NetworkPayloadTypeDef,
        "ProvisioningStatus": DeviceStatusType,
        "SerialNumber": str,
        "Tags": Dict[str, str],
        "Type": DeviceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionDeviceRequestRequestTypeDef = TypedDict(
    "ProvisionDeviceRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "NetworkingConfiguration": NotRequired[NetworkPayloadTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreatePackageImportJobRequestRequestTypeDef = TypedDict(
    "CreatePackageImportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InputConfig": PackageImportJobInputConfigTypeDef,
        "JobType": PackageImportJobTypeType,
        "OutputConfig": PackageImportJobOutputConfigTypeDef,
        "JobTags": NotRequired[Sequence[JobResourceTagsTypeDef]],
    },
)
DescribePackageImportJobResponseTypeDef = TypedDict(
    "DescribePackageImportJobResponseTypeDef",
    {
        "ClientToken": str,
        "CreatedTime": datetime,
        "InputConfig": PackageImportJobInputConfigTypeDef,
        "JobId": str,
        "JobTags": List[JobResourceTagsTypeDef],
        "JobType": PackageImportJobTypeType,
        "LastUpdatedTime": datetime,
        "Output": PackageImportJobOutputTypeDef,
        "OutputConfig": PackageImportJobOutputConfigTypeDef,
        "Status": PackageImportJobStatusType,
        "StatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
