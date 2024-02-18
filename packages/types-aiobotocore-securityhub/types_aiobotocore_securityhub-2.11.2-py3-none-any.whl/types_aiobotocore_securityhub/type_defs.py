"""
Type annotations for securityhub service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_securityhub/type_defs/)

Usage::

    ```python
    from types_aiobotocore_securityhub.type_defs import AcceptAdministratorInvitationRequestRequestTypeDef

    data: AcceptAdministratorInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdminStatusType,
    AssociationStatusType,
    AssociationTypeType,
    AutoEnableStandardsType,
    AwsIamAccessKeyStatusType,
    AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType,
    ComplianceStatusType,
    ConfigurationPolicyAssociationStatusType,
    ControlFindingGeneratorType,
    ControlStatusType,
    FindingHistoryUpdateSourceTypeType,
    IntegrationTypeType,
    MalwareStateType,
    MalwareTypeType,
    MapFilterComparisonType,
    NetworkDirectionType,
    OrganizationConfigurationConfigurationTypeType,
    OrganizationConfigurationStatusType,
    ParameterValueTypeType,
    PartitionType,
    RecordStateType,
    RegionAvailabilityStatusType,
    RuleStatusType,
    SeverityLabelType,
    SeverityRatingType,
    SortOrderType,
    StandardsStatusType,
    StatusReasonCodeType,
    StringFilterComparisonType,
    TargetTypeType,
    ThreatIntelIndicatorCategoryType,
    ThreatIntelIndicatorTypeType,
    UnprocessedErrorCodeType,
    UpdateStatusType,
    VerificationStateType,
    VulnerabilityExploitAvailableType,
    VulnerabilityFixAvailableType,
    WorkflowStateType,
    WorkflowStatusType,
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
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    "AcceptInvitationRequestRequestTypeDef",
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "DnsRequestActionTypeDef",
    "CityTypeDef",
    "CountryTypeDef",
    "GeoLocationTypeDef",
    "IpOrganizationDetailsTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "AdjustmentTypeDef",
    "AdminAccountTypeDef",
    "AssociatedStandardTypeDef",
    "AssociationFiltersTypeDef",
    "AssociationStateDetailsTypeDef",
    "NoteUpdateTypeDef",
    "RelatedFindingTypeDef",
    "SeverityUpdateTypeDef",
    "WorkflowUpdateTypeDef",
    "MapFilterTypeDef",
    "NumberFilterTypeDef",
    "StringFilterTypeDef",
    "AutomationRulesMetadataTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsPaginatorTypeDef",
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsPaginatorTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayEndpointConfigurationPaginatorTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsCorsConfigurationPaginatorTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsPaginatorTypeDef",
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsPaginatorTypeDef",
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigPaginatorTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    "AwsDmsEndpointDetailsTypeDef",
    "AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef",
    "AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef",
    "AwsDmsReplicationTaskDetailsTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsDynamoDbTableProjectionPaginatorTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceMetadataOptionsTypeDef",
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "IcmpTypeCodeTypeDef",
    "PortRangeFromToTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "PropagatingVgwSetDetailsTypeDef",
    "RouteSetDetailsTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "AwsEc2TransitGatewayDetailsPaginatorTypeDef",
    "AwsEc2TransitGatewayDetailsTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "CidrBlockAssociationTypeDef",
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    "VpcInfoCidrBlockSetDetailsTypeDef",
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    "VpcInfoPeeringOptionsDetailsTypeDef",
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsPaginatorTypeDef",
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    "AwsEcrContainerImageDetailsPaginatorTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    "AwsMountPointTypeDef",
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsPaginatorTypeDef",
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    "AwsEfsAccessPointPosixUserDetailsPaginatorTypeDef",
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsPaginatorTypeDef",
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsPaginatorTypeDef",
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsPaginatorTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionPaginatorTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbv2LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "AwsEventSchemasRegistryDetailsTypeDef",
    "AwsEventsEndpointEventBusesDetailsTypeDef",
    "AwsEventsEndpointReplicationConfigDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef",
    "AwsEventsEventbusDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigPaginatorTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaLayerVersionDetailsPaginatorTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsPaginatorTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef",
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsPaginatorTypeDef",
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributePaginatorTypeDef",
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsPaginatorTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsEventSubscriptionDetailsPaginatorTypeDef",
    "AwsRdsEventSubscriptionDetailsTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterLoggingStatusTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsRoute53HostedZoneConfigDetailsTypeDef",
    "AwsRoute53HostedZoneVpcDetailsTypeDef",
    "CloudWatchLogsLogGroupArnConfigDetailsTypeDef",
    "AwsS3AccessPointVpcConfigurationDetailsTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    "AwsS3BucketLoggingConfigurationTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "BooleanFilterTypeDef",
    "IpFilterTypeDef",
    "KeywordFilterTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "GeneratorDetailsPaginatorTypeDef",
    "MalwareTypeDef",
    "NoteTypeDef",
    "PatchSummaryTypeDef",
    "ProcessDetailsTypeDef",
    "SeverityTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "WorkflowTypeDef",
    "GeneratorDetailsTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsSsmComplianceSummaryTypeDef",
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    "AwsWafRulePredicateListDetailsTypeDef",
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "AwsWafv2CustomHttpHeaderTypeDef",
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    "AwsXrayEncryptionConfigDetailsTypeDef",
    "BatchDeleteAutomationRulesRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedAutomationRuleTypeDef",
    "BatchDisableStandardsRequestRequestTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "BatchGetAutomationRulesRequestRequestTypeDef",
    "ConfigurationPolicyAssociationSummaryTypeDef",
    "BatchGetSecurityControlsRequestRequestTypeDef",
    "UnprocessedSecurityControlTypeDef",
    "StandardsControlAssociationIdTypeDef",
    "StandardsControlAssociationDetailTypeDef",
    "ImportFindingsErrorTypeDef",
    "StandardsControlAssociationUpdateTypeDef",
    "BooleanConfigurationOptionsTypeDef",
    "CellTypeDef",
    "ClassificationStatusTypeDef",
    "CodeVulnerabilitiesFilePathTypeDef",
    "SecurityControlParameterPaginatorTypeDef",
    "StatusReasonTypeDef",
    "SecurityControlParameterTypeDef",
    "DoubleConfigurationOptionsTypeDef",
    "EnumConfigurationOptionsTypeDef",
    "EnumListConfigurationOptionsTypeDef",
    "IntegerConfigurationOptionsTypeDef",
    "IntegerListConfigurationOptionsTypeDef",
    "StringConfigurationOptionsTypeDef",
    "StringListConfigurationOptionsTypeDef",
    "TargetTypeDef",
    "ConfigurationPolicySummaryTypeDef",
    "VolumeMountTypeDef",
    "CreateActionTargetRequestRequestTypeDef",
    "CreateFindingAggregatorRequestRequestTypeDef",
    "ResultTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeleteActionTargetRequestRequestTypeDef",
    "DeleteConfigurationPolicyRequestRequestTypeDef",
    "DeleteFindingAggregatorRequestRequestTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeActionTargetsRequestRequestTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "OrganizationConfigurationTypeDef",
    "DescribeProductsRequestRequestTypeDef",
    "ProductTypeDef",
    "DescribeStandardsControlsRequestRequestTypeDef",
    "StandardsControlTypeDef",
    "DescribeStandardsRequestRequestTypeDef",
    "DisableImportFindingsForProductRequestRequestTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMembersRequestRequestTypeDef",
    "EnableImportFindingsForProductRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "EnableSecurityHubRequestRequestTypeDef",
    "FilePathsTypeDef",
    "FindingAggregatorTypeDef",
    "FindingHistoryUpdateSourceTypeDef",
    "FindingHistoryUpdateTypeDef",
    "FindingProviderSeverityTypeDef",
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    "InvitationTypeDef",
    "GetConfigurationPolicyRequestRequestTypeDef",
    "GetEnabledStandardsRequestRequestTypeDef",
    "GetFindingAggregatorRequestRequestTypeDef",
    "TimestampTypeDef",
    "SortCriterionTypeDef",
    "GetInsightResultsRequestRequestTypeDef",
    "GetInsightsRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "GetSecurityControlDefinitionRequestRequestTypeDef",
    "InsightResultValueTypeDef",
    "InviteMembersRequestRequestTypeDef",
    "ListAutomationRulesRequestRequestTypeDef",
    "ListConfigurationPoliciesRequestRequestTypeDef",
    "ListEnabledProductsForImportRequestRequestTypeDef",
    "ListFindingAggregatorsRequestRequestTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListSecurityControlDefinitionsRequestRequestTypeDef",
    "ListStandardsControlAssociationsRequestRequestTypeDef",
    "StandardsControlAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PortRangeTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ParameterValueTypeDef",
    "RecommendationTypeDef",
    "RuleGroupSourceListDetailsPaginatorTypeDef",
    "RuleGroupSourceListDetailsTypeDef",
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsPaginatorTypeDef",
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsPaginatorTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    "RuleGroupVariablesIpSetsDetailsPaginatorTypeDef",
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    "RuleGroupVariablesPortSetsDetailsPaginatorTypeDef",
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    "SoftwarePackageTypeDef",
    "StandardsManagedByTypeDef",
    "StandardsStatusReasonTypeDef",
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateActionTargetRequestRequestTypeDef",
    "UpdateFindingAggregatorRequestRequestTypeDef",
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    "UpdateStandardsControlRequestRequestTypeDef",
    "VulnerabilityVendorTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "CvssPaginatorTypeDef",
    "CvssTypeDef",
    "ListConfigurationPolicyAssociationsRequestRequestTypeDef",
    "AssociationSetDetailsTypeDef",
    "AutomationRulesFindingFieldsUpdateTypeDef",
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    "AwsApiGatewayRestApiDetailsPaginatorTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayStageDetailsPaginatorTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsPaginatorTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsApiGatewayV2StageDetailsPaginatorTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsPaginatorTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    "AwsBackupBackupVaultDetailsPaginatorTypeDef",
    "AwsBackupBackupVaultDetailsTypeDef",
    "AwsBackupRecoveryPointDetailsTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionPaginatorTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCloudFormationStackDetailsPaginatorTypeDef",
    "AwsCloudFormationStackDetailsTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsPaginatorTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudWatchAlarmDetailsPaginatorTypeDef",
    "AwsCloudWatchAlarmDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentPaginatorTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    "AwsDmsReplicationInstanceDetailsPaginatorTypeDef",
    "AwsDmsReplicationInstanceDetailsTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexPaginatorTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexPaginatorTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef",
    "AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef",
    "AwsEc2InstanceDetailsPaginatorTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsPaginatorTypeDef",
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsPaginatorTypeDef",
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceDetailsPaginatorTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionPaginatorTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SubnetDetailsPaginatorTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2VolumeDetailsPaginatorTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsPaginatorTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsEc2VpcEndpointServiceDetailsPaginatorTypeDef",
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsPaginatorTypeDef",
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsPaginatorTypeDef",
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    "AwsEcrRepositoryDetailsTypeDef",
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    "AwsEcsContainerDetailsPaginatorTypeDef",
    "AwsEcsContainerDetailsTypeDef",
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsPaginatorTypeDef",
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    "AwsEcsTaskVolumeDetailsTypeDef",
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    "AwsEksClusterLoggingDetailsPaginatorTypeDef",
    "AwsEksClusterLoggingDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsPaginatorTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    "AwsElbLoadBalancerPoliciesPaginatorTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerAttributesPaginatorTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerListenerDescriptionPaginatorTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbv2LoadBalancerDetailsPaginatorTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamGroupDetailsPaginatorTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamInstanceProfilePaginatorTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamPolicyDetailsPaginatorTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamUserDetailsPaginatorTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsKinesisStreamDetailsTypeDef",
    "AwsLambdaFunctionEnvironmentPaginatorTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef",
    "AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef",
    "AwsNetworkFirewallFirewallDetailsPaginatorTypeDef",
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    "AwsRdsDbClusterDetailsPaginatorTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterSnapshotDetailsPaginatorTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbSnapshotDetailsPaginatorTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbPendingModifiedValuesPaginatorTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRdsDbSecurityGroupDetailsPaginatorTypeDef",
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRedshiftClusterClusterParameterGroupPaginatorTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsRoute53HostedZoneObjectDetailsTypeDef",
    "AwsRoute53QueryLoggingConfigDetailsTypeDef",
    "AwsS3AccessPointDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterPaginatorTypeDef",
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    "AwsSageMakerNotebookInstanceDetailsPaginatorTypeDef",
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "BatchUpdateFindingsRequestRequestTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "AwsSnsTopicDetailsPaginatorTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    "AwsWafRateBasedRuleDetailsPaginatorTypeDef",
    "AwsWafRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsPaginatorTypeDef",
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    "AwsWafRegionalRuleDetailsPaginatorTypeDef",
    "AwsWafRegionalRuleDetailsTypeDef",
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    "AwsWafRuleDetailsPaginatorTypeDef",
    "AwsWafRuleDetailsTypeDef",
    "AwsWafRuleGroupRulesDetailsTypeDef",
    "AwsWafWebAclRulePaginatorTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsPaginatorTypeDef",
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    "AwsWafv2CustomResponseDetailsPaginatorTypeDef",
    "AwsWafv2CustomResponseDetailsTypeDef",
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateAutomationRuleResponseTypeDef",
    "CreateFindingAggregatorResponseTypeDef",
    "CreateInsightResponseTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteInsightResponseTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubResponseTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "GetConfigurationPolicyAssociationResponseTypeDef",
    "GetFindingAggregatorResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "ListAutomationRulesResponseTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartConfigurationPolicyAssociationResponseTypeDef",
    "UpdateFindingAggregatorResponseTypeDef",
    "BatchDeleteAutomationRulesResponseTypeDef",
    "BatchUpdateAutomationRulesResponseTypeDef",
    "BatchEnableStandardsRequestRequestTypeDef",
    "ListConfigurationPolicyAssociationsResponseTypeDef",
    "BatchGetStandardsControlAssociationsRequestRequestTypeDef",
    "UnprocessedStandardsControlAssociationTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateStandardsControlAssociationsRequestRequestTypeDef",
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    "VulnerabilityCodeVulnerabilitiesPaginatorTypeDef",
    "VulnerabilityCodeVulnerabilitiesTypeDef",
    "CompliancePaginatorTypeDef",
    "ComplianceTypeDef",
    "ConfigurationOptionsTypeDef",
    "ConfigurationPolicyAssociationTypeDef",
    "GetConfigurationPolicyAssociationRequestRequestTypeDef",
    "StartConfigurationPolicyAssociationRequestRequestTypeDef",
    "StartConfigurationPolicyDisassociationRequestRequestTypeDef",
    "ListConfigurationPoliciesResponseTypeDef",
    "ContainerDetailsPaginatorTypeDef",
    "ContainerDetailsTypeDef",
    "CreateMembersResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "InviteMembersResponseTypeDef",
    "DateFilterTypeDef",
    "DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef",
    "DescribeProductsRequestDescribeProductsPaginateTypeDef",
    "DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    "DescribeStandardsRequestDescribeStandardsPaginateTypeDef",
    "GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef",
    "GetInsightsRequestGetInsightsPaginateTypeDef",
    "ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef",
    "ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef",
    "ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef",
    "ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef",
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    "ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef",
    "ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "ThreatPaginatorTypeDef",
    "ThreatTypeDef",
    "ListFindingAggregatorsResponseTypeDef",
    "FindingHistoryRecordTypeDef",
    "FindingProviderFieldsPaginatorTypeDef",
    "FindingProviderFieldsTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    "GetFindingHistoryRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "ListMembersResponseTypeDef",
    "InsightResultsTypeDef",
    "ListStandardsControlAssociationsResponseTypeDef",
    "NetworkPathComponentDetailsPaginatorTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkTypeDef",
    "PageTypeDef",
    "ParameterConfigurationTypeDef",
    "RemediationTypeDef",
    "RuleGroupSourceStatefulRulesDetailsPaginatorTypeDef",
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesPaginatorTypeDef",
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    "RuleGroupVariablesPaginatorTypeDef",
    "RuleGroupVariablesTypeDef",
    "StandardTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatelessCustomPublishMetricActionPaginatorTypeDef",
    "StatelessCustomPublishMetricActionTypeDef",
    "AwsApiCallActionPaginatorTypeDef",
    "AwsApiCallActionTypeDef",
    "NetworkConnectionActionTypeDef",
    "PortProbeDetailTypeDef",
    "AwsEc2RouteTableDetailsPaginatorTypeDef",
    "AwsEc2RouteTableDetailsTypeDef",
    "AutomationRulesActionTypeDef",
    "AwsAmazonMqBrokerDetailsPaginatorTypeDef",
    "AwsAmazonMqBrokerDetailsTypeDef",
    "AwsAppSyncGraphQlApiDetailsPaginatorTypeDef",
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsPaginatorTypeDef",
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsPaginatorTypeDef",
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    "AwsBackupBackupPlanRuleDetailsPaginatorTypeDef",
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryPaginatorTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCloudFrontDistributionOriginItemPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginGroupPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCodeBuildProjectDetailsPaginatorTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsDynamoDbTableReplicaPaginatorTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsEc2ClientVpnEndpointDetailsPaginatorTypeDef",
    "AwsEc2ClientVpnEndpointDetailsTypeDef",
    "AwsEc2LaunchTemplateDataDetailsPaginatorTypeDef",
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    "AwsEc2NetworkAclDetailsPaginatorTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2SecurityGroupDetailsPaginatorTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsPaginatorTypeDef",
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    "AwsEc2VpnConnectionDetailsPaginatorTypeDef",
    "AwsEc2VpnConnectionDetailsTypeDef",
    "AwsEcsClusterConfigurationDetailsTypeDef",
    "AwsEcsServiceDetailsPaginatorTypeDef",
    "AwsEcsServiceDetailsTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    "AwsEcsTaskDetailsPaginatorTypeDef",
    "AwsEcsTaskDetailsTypeDef",
    "AwsEfsAccessPointDetailsPaginatorTypeDef",
    "AwsEfsAccessPointDetailsTypeDef",
    "AwsEksClusterDetailsPaginatorTypeDef",
    "AwsEksClusterDetailsTypeDef",
    "AwsElasticsearchDomainDetailsPaginatorTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElbLoadBalancerDetailsPaginatorTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsEventsEndpointRoutingConfigDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamRoleDetailsPaginatorTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsLambdaFunctionDetailsPaginatorTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsPaginatorTypeDef",
    "AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef",
    "AwsOpenSearchServiceDomainDetailsPaginatorTypeDef",
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    "AwsRdsDbSubnetGroupPaginatorTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRedshiftClusterDetailsPaginatorTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsRoute53HostedZoneDetailsPaginatorTypeDef",
    "AwsRoute53HostedZoneDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsPaginatorTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationFilterPaginatorTypeDef",
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    "AwsS3BucketObjectLockConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationPaginatorTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketWebsiteConfigurationPaginatorTypeDef",
    "AwsS3BucketWebsiteConfigurationTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsPaginatorTypeDef",
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    "AwsWafRegionalRuleGroupDetailsPaginatorTypeDef",
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    "AwsWafRegionalWebAclDetailsPaginatorTypeDef",
    "AwsWafRegionalWebAclDetailsTypeDef",
    "AwsWafRuleGroupDetailsPaginatorTypeDef",
    "AwsWafRuleGroupDetailsTypeDef",
    "AwsWafWebAclDetailsPaginatorTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafv2ActionAllowDetailsPaginatorTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsPaginatorTypeDef",
    "AwsWafv2RulesActionCountDetailsPaginatorTypeDef",
    "AwsWafv2ActionAllowDetailsTypeDef",
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    "AwsWafv2RulesActionCountDetailsTypeDef",
    "AwsWafv2ActionBlockDetailsPaginatorTypeDef",
    "AwsWafv2ActionBlockDetailsTypeDef",
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    "VulnerabilityPaginatorTypeDef",
    "VulnerabilityTypeDef",
    "ParameterDefinitionTypeDef",
    "BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef",
    "UnprocessedConfigurationPolicyAssociationTypeDef",
    "AutomationRulesFindingFiltersTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "GetFindingHistoryResponseTypeDef",
    "GetInsightResultsResponseTypeDef",
    "NetworkHeaderPaginatorTypeDef",
    "NetworkHeaderTypeDef",
    "OccurrencesPaginatorTypeDef",
    "OccurrencesTypeDef",
    "SecurityControlCustomParameterTypeDef",
    "SecurityControlTypeDef",
    "UpdateSecurityControlRequestRequestTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionPaginatorTypeDef",
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    "DescribeStandardsResponseTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "StatelessCustomActionDefinitionPaginatorTypeDef",
    "StatelessCustomActionDefinitionTypeDef",
    "PortProbeActionPaginatorTypeDef",
    "PortProbeActionTypeDef",
    "AwsAthenaWorkGroupDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsPaginatorTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsPaginatorTypeDef",
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsPaginatorTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCloudFrontDistributionOriginsPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudFrontDistributionOriginGroupsPaginatorTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsDynamoDbTableDetailsPaginatorTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsEc2LaunchTemplateDetailsPaginatorTypeDef",
    "AwsEc2LaunchTemplateDetailsTypeDef",
    "AwsEcsClusterDetailsPaginatorTypeDef",
    "AwsEcsClusterDetailsTypeDef",
    "AwsEcsTaskDefinitionDetailsPaginatorTypeDef",
    "AwsEcsTaskDefinitionDetailsTypeDef",
    "AwsEventsEndpointDetailsPaginatorTypeDef",
    "AwsEventsEndpointDetailsTypeDef",
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    "AwsMskClusterClusterInfoDetailsPaginatorTypeDef",
    "AwsMskClusterClusterInfoDetailsTypeDef",
    "AwsRdsDbInstanceDetailsPaginatorTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsPaginatorTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationDetailPaginatorTypeDef",
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    "AwsStepFunctionStateMachineDetailsPaginatorTypeDef",
    "AwsStepFunctionStateMachineDetailsTypeDef",
    "AwsWafv2RulesActionDetailsPaginatorTypeDef",
    "AwsWafv2WebAclActionDetailsPaginatorTypeDef",
    "AwsWafv2RulesActionDetailsTypeDef",
    "AwsWafv2WebAclActionDetailsTypeDef",
    "SecurityControlDefinitionTypeDef",
    "BatchGetConfigurationPolicyAssociationsResponseTypeDef",
    "AutomationRulesConfigTypeDef",
    "CreateAutomationRuleRequestRequestTypeDef",
    "UpdateAutomationRulesRequestItemTypeDef",
    "CreateInsightRequestRequestTypeDef",
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "InsightTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "UpdateInsightRequestRequestTypeDef",
    "NetworkPathComponentPaginatorTypeDef",
    "NetworkPathComponentTypeDef",
    "CustomDataIdentifiersDetectionsPaginatorTypeDef",
    "SensitiveDataDetectionsPaginatorTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "SecurityControlsConfigurationTypeDef",
    "BatchGetSecurityControlsResponseTypeDef",
    "RuleGroupSourceStatelessRulesDetailsPaginatorTypeDef",
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsPaginatorTypeDef",
    "RuleGroupSourceCustomActionsDetailsPaginatorTypeDef",
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    "ActionPaginatorTypeDef",
    "ActionTypeDef",
    "AwsBackupBackupPlanDetailsPaginatorTypeDef",
    "AwsBackupBackupPlanDetailsTypeDef",
    "AwsCloudFrontDistributionDetailsPaginatorTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsGuardDutyDetectorDetailsPaginatorTypeDef",
    "AwsGuardDutyDetectorDetailsTypeDef",
    "AwsMskClusterDetailsPaginatorTypeDef",
    "AwsMskClusterDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsPaginatorTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    "AwsS3BucketNotificationConfigurationPaginatorTypeDef",
    "AwsS3BucketNotificationConfigurationTypeDef",
    "AwsWafv2RulesDetailsPaginatorTypeDef",
    "AwsWafv2RulesDetailsTypeDef",
    "GetSecurityControlDefinitionResponseTypeDef",
    "ListSecurityControlDefinitionsResponseTypeDef",
    "BatchGetAutomationRulesResponseTypeDef",
    "BatchUpdateAutomationRulesRequestRequestTypeDef",
    "GetInsightsResponseTypeDef",
    "CustomDataIdentifiersResultPaginatorTypeDef",
    "SensitiveDataResultPaginatorTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "SensitiveDataResultTypeDef",
    "SecurityHubPolicyTypeDef",
    "FirewallPolicyDetailsPaginatorTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsPaginatorTypeDef",
    "FirewallPolicyDetailsTypeDef",
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsPaginatorTypeDef",
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    "AwsWafv2RuleGroupDetailsPaginatorTypeDef",
    "AwsWafv2WebAclDetailsPaginatorTypeDef",
    "AwsWafv2RuleGroupDetailsTypeDef",
    "AwsWafv2WebAclDetailsTypeDef",
    "ClassificationResultPaginatorTypeDef",
    "ClassificationResultTypeDef",
    "PolicyTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsPaginatorTypeDef",
    "RuleGroupSourcePaginatorTypeDef",
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    "RuleGroupSourceTypeDef",
    "AwsS3BucketDetailsPaginatorTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "DataClassificationDetailsPaginatorTypeDef",
    "DataClassificationDetailsTypeDef",
    "CreateConfigurationPolicyRequestRequestTypeDef",
    "CreateConfigurationPolicyResponseTypeDef",
    "GetConfigurationPolicyResponseTypeDef",
    "UpdateConfigurationPolicyRequestRequestTypeDef",
    "UpdateConfigurationPolicyResponseTypeDef",
    "RuleGroupDetailsPaginatorTypeDef",
    "RuleGroupDetailsTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsPaginatorTypeDef",
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    "ResourceDetailsPaginatorTypeDef",
    "ResourceDetailsTypeDef",
    "ResourcePaginatorTypeDef",
    "ResourceTypeDef",
    "AwsSecurityFindingPaginatorTypeDef",
    "AwsSecurityFindingTypeDef",
    "GetFindingsResponsePaginatorTypeDef",
    "BatchImportFindingsRequestRequestTypeDef",
    "GetFindingsResponseTypeDef",
)

AcceptAdministratorInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAdministratorInvitationRequestRequestTypeDef",
    {
        "AdministratorId": str,
        "InvitationId": str,
    },
)
AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "MasterId": str,
        "InvitationId": str,
    },
)
AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "AccountId": str,
        "Email": NotRequired[str],
    },
)
ActionLocalIpDetailsTypeDef = TypedDict(
    "ActionLocalIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
    },
)
ActionLocalPortDetailsTypeDef = TypedDict(
    "ActionLocalPortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)
DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef",
    {
        "Domain": NotRequired[str],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)
CityTypeDef = TypedDict(
    "CityTypeDef",
    {
        "CityName": NotRequired[str],
    },
)
CountryTypeDef = TypedDict(
    "CountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "CountryName": NotRequired[str],
    },
)
GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "Lon": NotRequired[float],
        "Lat": NotRequired[float],
    },
)
IpOrganizationDetailsTypeDef = TypedDict(
    "IpOrganizationDetailsTypeDef",
    {
        "Asn": NotRequired[int],
        "AsnOrg": NotRequired[str],
        "Isp": NotRequired[str],
        "Org": NotRequired[str],
    },
)
ActionRemotePortDetailsTypeDef = TypedDict(
    "ActionRemotePortDetailsTypeDef",
    {
        "Port": NotRequired[int],
        "PortName": NotRequired[str],
    },
)
ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "ActionTargetArn": str,
        "Name": str,
        "Description": str,
    },
)
AdjustmentTypeDef = TypedDict(
    "AdjustmentTypeDef",
    {
        "Metric": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "AccountId": NotRequired[str],
        "Status": NotRequired[AdminStatusType],
    },
)
AssociatedStandardTypeDef = TypedDict(
    "AssociatedStandardTypeDef",
    {
        "StandardsId": NotRequired[str],
    },
)
AssociationFiltersTypeDef = TypedDict(
    "AssociationFiltersTypeDef",
    {
        "ConfigurationPolicyId": NotRequired[str],
        "AssociationType": NotRequired[AssociationTypeType],
        "AssociationStatus": NotRequired[ConfigurationPolicyAssociationStatusType],
    },
)
AssociationStateDetailsTypeDef = TypedDict(
    "AssociationStateDetailsTypeDef",
    {
        "State": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
NoteUpdateTypeDef = TypedDict(
    "NoteUpdateTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
    },
)
RelatedFindingTypeDef = TypedDict(
    "RelatedFindingTypeDef",
    {
        "ProductArn": str,
        "Id": str,
    },
)
SeverityUpdateTypeDef = TypedDict(
    "SeverityUpdateTypeDef",
    {
        "Normalized": NotRequired[int],
        "Product": NotRequired[float],
        "Label": NotRequired[SeverityLabelType],
    },
)
WorkflowUpdateTypeDef = TypedDict(
    "WorkflowUpdateTypeDef",
    {
        "Status": NotRequired[WorkflowStatusType],
    },
)
MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Comparison": NotRequired[MapFilterComparisonType],
    },
)
NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "Gte": NotRequired[float],
        "Lte": NotRequired[float],
        "Eq": NotRequired[float],
        "Gt": NotRequired[float],
        "Lt": NotRequired[float],
    },
)
StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "Value": NotRequired[str],
        "Comparison": NotRequired[StringFilterComparisonType],
    },
)
AutomationRulesMetadataTypeDef = TypedDict(
    "AutomationRulesMetadataTypeDef",
    {
        "RuleArn": NotRequired[str],
        "RuleStatus": NotRequired[RuleStatusType],
        "RuleOrder": NotRequired[int],
        "RuleName": NotRequired[str],
        "Description": NotRequired[str],
        "IsTerminal": NotRequired[bool],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef",
    {
        "KmsKeyId": NotRequired[str],
        "UseAwsOwnedKey": NotRequired[bool],
    },
)
AwsAmazonMqBrokerLdapServerMetadataDetailsPaginatorTypeDef = TypedDict(
    "AwsAmazonMqBrokerLdapServerMetadataDetailsPaginatorTypeDef",
    {
        "Hosts": NotRequired[List[str]],
        "RoleBase": NotRequired[str],
        "RoleName": NotRequired[str],
        "RoleSearchMatching": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "ServiceAccountUsername": NotRequired[str],
        "UserBase": NotRequired[str],
        "UserRoleName": NotRequired[str],
        "UserSearchMatching": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)
AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef",
    {
        "DayOfWeek": NotRequired[str],
        "TimeOfDay": NotRequired[str],
        "TimeZone": NotRequired[str],
    },
)
AwsAmazonMqBrokerUsersDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerUsersDetailsTypeDef",
    {
        "PendingChange": NotRequired[str],
        "Username": NotRequired[str],
    },
)
AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef",
    {
        "Hosts": NotRequired[Sequence[str]],
        "RoleBase": NotRequired[str],
        "RoleName": NotRequired[str],
        "RoleSearchMatching": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "ServiceAccountUsername": NotRequired[str],
        "UserBase": NotRequired[str],
        "UserRoleName": NotRequired[str],
        "UserSearchMatching": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)
AwsAmazonMqBrokerLogsPendingDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsPendingDetailsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
    },
)
AwsApiCallActionDomainDetailsTypeDef = TypedDict(
    "AwsApiCallActionDomainDetailsTypeDef",
    {
        "Domain": NotRequired[str],
    },
)
AwsApiGatewayAccessLogSettingsTypeDef = TypedDict(
    "AwsApiGatewayAccessLogSettingsTypeDef",
    {
        "Format": NotRequired[str],
        "DestinationArn": NotRequired[str],
    },
)
AwsApiGatewayCanarySettingsPaginatorTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsPaginatorTypeDef",
    {
        "PercentTraffic": NotRequired[float],
        "DeploymentId": NotRequired[str],
        "StageVariableOverrides": NotRequired[Dict[str, str]],
        "UseStageCache": NotRequired[bool],
    },
)
AwsApiGatewayCanarySettingsTypeDef = TypedDict(
    "AwsApiGatewayCanarySettingsTypeDef",
    {
        "PercentTraffic": NotRequired[float],
        "DeploymentId": NotRequired[str],
        "StageVariableOverrides": NotRequired[Mapping[str, str]],
        "UseStageCache": NotRequired[bool],
    },
)
AwsApiGatewayEndpointConfigurationPaginatorTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationPaginatorTypeDef",
    {
        "Types": NotRequired[List[str]],
    },
)
AwsApiGatewayEndpointConfigurationTypeDef = TypedDict(
    "AwsApiGatewayEndpointConfigurationTypeDef",
    {
        "Types": NotRequired[Sequence[str]],
    },
)
AwsApiGatewayMethodSettingsTypeDef = TypedDict(
    "AwsApiGatewayMethodSettingsTypeDef",
    {
        "MetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[str],
        "DataTraceEnabled": NotRequired[bool],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
        "CachingEnabled": NotRequired[bool],
        "CacheTtlInSeconds": NotRequired[int],
        "CacheDataEncrypted": NotRequired[bool],
        "RequireAuthorizationForCacheControl": NotRequired[bool],
        "UnauthorizedCacheControlHeaderStrategy": NotRequired[str],
        "HttpMethod": NotRequired[str],
        "ResourcePath": NotRequired[str],
    },
)
AwsCorsConfigurationPaginatorTypeDef = TypedDict(
    "AwsCorsConfigurationPaginatorTypeDef",
    {
        "AllowOrigins": NotRequired[List[str]],
        "AllowCredentials": NotRequired[bool],
        "ExposeHeaders": NotRequired[List[str]],
        "MaxAge": NotRequired[int],
        "AllowMethods": NotRequired[List[str]],
        "AllowHeaders": NotRequired[List[str]],
    },
)
AwsCorsConfigurationTypeDef = TypedDict(
    "AwsCorsConfigurationTypeDef",
    {
        "AllowOrigins": NotRequired[Sequence[str]],
        "AllowCredentials": NotRequired[bool],
        "ExposeHeaders": NotRequired[Sequence[str]],
        "MaxAge": NotRequired[int],
        "AllowMethods": NotRequired[Sequence[str]],
        "AllowHeaders": NotRequired[Sequence[str]],
    },
)
AwsApiGatewayV2RouteSettingsTypeDef = TypedDict(
    "AwsApiGatewayV2RouteSettingsTypeDef",
    {
        "DetailedMetricsEnabled": NotRequired[bool],
        "LoggingLevel": NotRequired[str],
        "DataTraceEnabled": NotRequired[bool],
        "ThrottlingBurstLimit": NotRequired[int],
        "ThrottlingRateLimit": NotRequired[float],
    },
)
AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef",
    {
        "AuthorizerResultTtlInSeconds": NotRequired[int],
        "AuthorizerUri": NotRequired[str],
        "IdentityValidationExpression": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef",
    {
        "AuthTtL": NotRequired[int],
        "ClientId": NotRequired[str],
        "IatTtL": NotRequired[int],
        "Issuer": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef",
    {
        "AppIdClientRegex": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "UserPoolId": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiLogConfigDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiLogConfigDetailsTypeDef",
    {
        "CloudWatchLogsRoleArn": NotRequired[str],
        "ExcludeVerboseContent": NotRequired[bool],
        "FieldLogLevel": NotRequired[str],
    },
)
AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef",
    {
        "EncryptionOption": NotRequired[str],
        "KmsKey": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef",
    {
        "Value": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef",
    {
        "OnDemandAllocationStrategy": NotRequired[str],
        "OnDemandBaseCapacity": NotRequired[int],
        "OnDemandPercentageAboveBaseCapacity": NotRequired[int],
        "SpotAllocationStrategy": NotRequired[str],
        "SpotInstancePools": NotRequired[int],
        "SpotMaxPrice": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[str],
    },
)
AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)
AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpTokens": NotRequired[str],
    },
)
AwsBackupBackupPlanAdvancedBackupSettingsDetailsPaginatorTypeDef = TypedDict(
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsPaginatorTypeDef",
    {
        "BackupOptions": NotRequired[Dict[str, str]],
        "ResourceType": NotRequired[str],
    },
)
AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef",
    {
        "BackupOptions": NotRequired[Mapping[str, str]],
        "ResourceType": NotRequired[str],
    },
)
AwsBackupBackupPlanLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanLifecycleDetailsTypeDef",
    {
        "DeleteAfterDays": NotRequired[int],
        "MoveToColdStorageAfterDays": NotRequired[int],
    },
)
AwsBackupBackupVaultNotificationsDetailsPaginatorTypeDef = TypedDict(
    "AwsBackupBackupVaultNotificationsDetailsPaginatorTypeDef",
    {
        "BackupVaultEvents": NotRequired[List[str]],
        "SnsTopicArn": NotRequired[str],
    },
)
AwsBackupBackupVaultNotificationsDetailsTypeDef = TypedDict(
    "AwsBackupBackupVaultNotificationsDetailsTypeDef",
    {
        "BackupVaultEvents": NotRequired[Sequence[str]],
        "SnsTopicArn": NotRequired[str],
    },
)
AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef",
    {
        "DeleteAt": NotRequired[str],
        "MoveToColdStorageAt": NotRequired[str],
    },
)
AwsBackupRecoveryPointCreatedByDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointCreatedByDetailsTypeDef",
    {
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "BackupPlanVersion": NotRequired[str],
        "BackupRuleId": NotRequired[str],
    },
)
AwsBackupRecoveryPointLifecycleDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointLifecycleDetailsTypeDef",
    {
        "DeleteAfterDays": NotRequired[int],
        "MoveToColdStorageAfterDays": NotRequired[int],
    },
)
AwsCertificateManagerCertificateExtendedKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    {
        "Name": NotRequired[str],
        "OId": NotRequired[str],
    },
)
AwsCertificateManagerCertificateKeyUsageTypeDef = TypedDict(
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    {
        "Name": NotRequired[str],
    },
)
AwsCertificateManagerCertificateOptionsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": NotRequired[str],
    },
)
AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsCloudFormationStackDriftInformationDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackDriftInformationDetailsTypeDef",
    {
        "StackDriftStatus": NotRequired[str],
    },
)
AwsCloudFormationStackOutputsDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackOutputsDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "OutputKey": NotRequired[str],
        "OutputValue": NotRequired[str],
    },
)
AwsCloudFrontDistributionCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": NotRequired[str],
    },
)
AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    {
        "ViewerProtocolPolicy": NotRequired[str],
    },
)
AwsCloudFrontDistributionLoggingTypeDef = TypedDict(
    "AwsCloudFrontDistributionLoggingTypeDef",
    {
        "Bucket": NotRequired[str],
        "Enabled": NotRequired[bool],
        "IncludeCookies": NotRequired[bool],
        "Prefix": NotRequired[str],
    },
)
AwsCloudFrontDistributionViewerCertificateTypeDef = TypedDict(
    "AwsCloudFrontDistributionViewerCertificateTypeDef",
    {
        "AcmCertificateArn": NotRequired[str],
        "Certificate": NotRequired[str],
        "CertificateSource": NotRequired[str],
        "CloudFrontDefaultCertificate": NotRequired[bool],
        "IamCertificateId": NotRequired[str],
        "MinimumProtocolVersion": NotRequired[str],
        "SslSupportMethod": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginSslProtocolsPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginSslProtocolsPaginatorTypeDef",
    {
        "Items": NotRequired[List[str]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginSslProtocolsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginSslProtocolsTypeDef",
    {
        "Items": NotRequired[Sequence[str]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverStatusCodesPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesPaginatorTypeDef",
    {
        "Items": NotRequired[List[int]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    {
        "Items": NotRequired[Sequence[int]],
        "Quantity": NotRequired[int],
    },
)
AwsCloudFrontDistributionOriginS3OriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    {
        "OriginAccessIdentity": NotRequired[str],
    },
)
AwsCloudTrailTrailDetailsTypeDef = TypedDict(
    "AwsCloudTrailTrailDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "HasCustomEventSelectors": NotRequired[bool],
        "HomeRegion": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "IsOrganizationTrail": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "LogFileValidationEnabled": NotRequired[bool],
        "Name": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "TrailArn": NotRequired[str],
    },
)
AwsCloudWatchAlarmDimensionsDetailsTypeDef = TypedDict(
    "AwsCloudWatchAlarmDimensionsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsCodeBuildProjectArtifactsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectArtifactsDetailsTypeDef",
    {
        "ArtifactIdentifier": NotRequired[str],
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceType": NotRequired[str],
        "OverrideArtifactName": NotRequired[bool],
        "Packaging": NotRequired[str],
        "Path": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Location": NotRequired[str],
        "GitCloneDepth": NotRequired[int],
        "InsecureSsl": NotRequired[bool],
    },
)
AwsCodeBuildProjectVpcConfigPaginatorTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigPaginatorTypeDef",
    {
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)
AwsCodeBuildProjectVpcConfigTypeDef = TypedDict(
    "AwsCodeBuildProjectVpcConfigTypeDef",
    {
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)
AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    {
        "Credential": NotRequired[str],
        "CredentialProvider": NotRequired[str],
    },
)
AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef",
    {
        "GroupName": NotRequired[str],
        "Status": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)
AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef",
    {
        "EncryptionDisabled": NotRequired[bool],
        "Location": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsDmsEndpointDetailsTypeDef = TypedDict(
    "AwsDmsEndpointDetailsTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "EndpointArn": NotRequired[str],
        "EndpointIdentifier": NotRequired[str],
        "EndpointType": NotRequired[str],
        "EngineName": NotRequired[str],
        "ExternalId": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "SslMode": NotRequired[str],
        "Username": NotRequired[str],
    },
)
AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef = TypedDict(
    "AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": NotRequired[str],
    },
)
AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef = TypedDict(
    "AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
    },
)
AwsDmsReplicationTaskDetailsTypeDef = TypedDict(
    "AwsDmsReplicationTaskDetailsTypeDef",
    {
        "CdcStartPosition": NotRequired[str],
        "CdcStartTime": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "MigrationType": NotRequired[str],
        "Id": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "ReplicationTaskIdentifier": NotRequired[str],
        "ReplicationTaskSettings": NotRequired[str],
        "SourceEndpointArn": NotRequired[str],
        "TableMappings": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
        "TaskData": NotRequired[str],
    },
)
AwsDynamoDbTableAttributeDefinitionTypeDef = TypedDict(
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeType": NotRequired[str],
    },
)
AwsDynamoDbTableBillingModeSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    {
        "BillingMode": NotRequired[str],
        "LastUpdateToPayPerRequestDateTime": NotRequired[str],
    },
)
AwsDynamoDbTableKeySchemaTypeDef = TypedDict(
    "AwsDynamoDbTableKeySchemaTypeDef",
    {
        "AttributeName": NotRequired[str],
        "KeyType": NotRequired[str],
    },
)
AwsDynamoDbTableProvisionedThroughputTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    {
        "LastDecreaseDateTime": NotRequired[str],
        "LastIncreaseDateTime": NotRequired[str],
        "NumberOfDecreasesToday": NotRequired[int],
        "ReadCapacityUnits": NotRequired[int],
        "WriteCapacityUnits": NotRequired[int],
    },
)
AwsDynamoDbTableRestoreSummaryTypeDef = TypedDict(
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    {
        "SourceBackupArn": NotRequired[str],
        "SourceTableArn": NotRequired[str],
        "RestoreDateTime": NotRequired[str],
        "RestoreInProgress": NotRequired[bool],
    },
)
AwsDynamoDbTableSseDescriptionTypeDef = TypedDict(
    "AwsDynamoDbTableSseDescriptionTypeDef",
    {
        "InaccessibleEncryptionDateTime": NotRequired[str],
        "Status": NotRequired[str],
        "SseType": NotRequired[str],
        "KmsMasterKeyArn": NotRequired[str],
    },
)
AwsDynamoDbTableStreamSpecificationTypeDef = TypedDict(
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    {
        "StreamEnabled": NotRequired[bool],
        "StreamViewType": NotRequired[str],
    },
)
AwsDynamoDbTableProjectionPaginatorTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionPaginatorTypeDef",
    {
        "NonKeyAttributes": NotRequired[List[str]],
        "ProjectionType": NotRequired[str],
    },
)
AwsDynamoDbTableProjectionTypeDef = TypedDict(
    "AwsDynamoDbTableProjectionTypeDef",
    {
        "NonKeyAttributes": NotRequired[Sequence[str]],
        "ProjectionType": NotRequired[str],
    },
)
AwsDynamoDbTableProvisionedThroughputOverrideTypeDef = TypedDict(
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": NotRequired[int],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef",
    {
        "DirectoryId": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef",
    {
        "SamlProviderArn": NotRequired[str],
        "SelfServiceSamlProviderArn": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef",
    {
        "ClientRootCertificateChain": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "BannerText": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "CloudwatchLogGroup": NotRequired[str],
        "CloudwatchLogStream": NotRequired[str],
    },
)
AwsEc2EipDetailsTypeDef = TypedDict(
    "AwsEc2EipDetailsTypeDef",
    {
        "InstanceId": NotRequired[str],
        "PublicIp": NotRequired[str],
        "AllocationId": NotRequired[str],
        "AssociationId": NotRequired[str],
        "Domain": NotRequired[str],
        "PublicIpv4Pool": NotRequired[str],
        "NetworkBorderGroup": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfaceOwnerId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
    },
)
AwsEc2InstanceMetadataOptionsTypeDef = TypedDict(
    "AwsEc2InstanceMetadataOptionsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpProtocolIpv6": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpTokens": NotRequired[str],
        "InstanceMetadataTags": NotRequired[str],
    },
)
AwsEc2InstanceMonitoringDetailsTypeDef = TypedDict(
    "AwsEc2InstanceMonitoringDetailsTypeDef",
    {
        "State": NotRequired[str],
    },
)
AwsEc2InstanceNetworkInterfacesDetailsTypeDef = TypedDict(
    "AwsEc2InstanceNetworkInterfacesDetailsTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef",
    {
        "DeleteOnTermination": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "Iops": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Throughput": NotRequired[int],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef",
    {
        "CapacityReservationId": NotRequired[str],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef",
    {
        "CoreCount": NotRequired[int],
        "ThreadsPerCore": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef",
    {
        "CpuCredits": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef",
    {
        "Configured": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef",
    {
        "LicenseConfigurationArn": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef",
    {
        "AutoRecovery": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "HttpProtocolIpv6": NotRequired[str],
        "HttpTokens": NotRequired[str],
        "HttpPutResponseHopLimit": NotRequired[int],
        "InstanceMetadataTags": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDataPlacementDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPlacementDetailsTypeDef",
    {
        "Affinity": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "GroupName": NotRequired[str],
        "HostId": NotRequired[str],
        "HostResourceGroupArn": NotRequired[str],
        "PartitionNumber": NotRequired[int],
        "SpreadDomain": NotRequired[str],
        "Tenancy": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef",
    {
        "EnableResourceNameDnsAAAARecord": NotRequired[bool],
        "EnableResourceNameDnsARecord": NotRequired[bool],
        "HostnameType": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef",
    {
        "BlockDurationMinutes": NotRequired[int],
        "InstanceInterruptionBehavior": NotRequired[str],
        "MaxPrice": NotRequired[str],
        "SpotInstanceType": NotRequired[str],
        "ValidUntil": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef",
    {
        "Max": NotRequired[float],
        "Min": NotRequired[float],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef",
    {
        "Max": NotRequired[float],
        "Min": NotRequired[float],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef",
    {
        "Max": NotRequired[int],
        "Min": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef",
    {
        "Ipv4Prefix": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef",
    {
        "Ipv6Address": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef",
    {
        "Ipv6Prefix": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef",
    {
        "Primary": NotRequired[bool],
        "PrivateIpAddress": NotRequired[str],
    },
)
AwsEc2NetworkAclAssociationTypeDef = TypedDict(
    "AwsEc2NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": NotRequired[str],
        "NetworkAclId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": NotRequired[int],
        "Type": NotRequired[int],
    },
)
PortRangeFromToTypeDef = TypedDict(
    "PortRangeFromToTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
    },
)
AwsEc2NetworkInterfaceAttachmentTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "DeviceIndex": NotRequired[int],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    {
        "IpV6Address": NotRequired[str],
    },
)
AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef = TypedDict(
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    {
        "PrivateIpAddress": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceSecurityGroupTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
PropagatingVgwSetDetailsTypeDef = TypedDict(
    "PropagatingVgwSetDetailsTypeDef",
    {
        "GatewayId": NotRequired[str],
    },
)
RouteSetDetailsTypeDef = TypedDict(
    "RouteSetDetailsTypeDef",
    {
        "CarrierGatewayId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "DestinationCidrBlock": NotRequired[str],
        "DestinationIpv6CidrBlock": NotRequired[str],
        "DestinationPrefixListId": NotRequired[str],
        "EgressOnlyInternetGatewayId": NotRequired[str],
        "GatewayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceOwnerId": NotRequired[str],
        "LocalGatewayId": NotRequired[str],
        "NatGatewayId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "Origin": NotRequired[str],
        "State": NotRequired[str],
        "TransitGatewayId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
AwsEc2SecurityGroupIpRangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
    },
)
AwsEc2SecurityGroupIpv6RangeTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    {
        "CidrIpv6": NotRequired[str],
    },
)
AwsEc2SecurityGroupPrefixListIdTypeDef = TypedDict(
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    {
        "PrefixListId": NotRequired[str],
    },
)
AwsEc2SecurityGroupUserIdGroupPairTypeDef = TypedDict(
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "PeeringStatus": NotRequired[str],
        "UserId": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
Ipv6CidrBlockAssociationTypeDef = TypedDict(
    "Ipv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "Ipv6CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[str],
    },
)
AwsEc2TransitGatewayDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2TransitGatewayDetailsPaginatorTypeDef",
    {
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[str],
        "AutoAcceptSharedAttachments": NotRequired[str],
        "DefaultRouteTableAssociation": NotRequired[str],
        "TransitGatewayCidrBlocks": NotRequired[List[str]],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "VpnEcmpSupport": NotRequired[str],
        "DnsSupport": NotRequired[str],
        "MulticastSupport": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
    },
)
AwsEc2TransitGatewayDetailsTypeDef = TypedDict(
    "AwsEc2TransitGatewayDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteTablePropagation": NotRequired[str],
        "AutoAcceptSharedAttachments": NotRequired[str],
        "DefaultRouteTableAssociation": NotRequired[str],
        "TransitGatewayCidrBlocks": NotRequired[Sequence[str]],
        "AssociationDefaultRouteTableId": NotRequired[str],
        "PropagationDefaultRouteTableId": NotRequired[str],
        "VpnEcmpSupport": NotRequired[str],
        "DnsSupport": NotRequired[str],
        "MulticastSupport": NotRequired[str],
        "AmazonSideAsn": NotRequired[int],
    },
)
AwsEc2VolumeAttachmentTypeDef = TypedDict(
    "AwsEc2VolumeAttachmentTypeDef",
    {
        "AttachTime": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
CidrBlockAssociationTypeDef = TypedDict(
    "CidrBlockAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "CidrBlock": NotRequired[str],
        "CidrBlockState": NotRequired[str],
    },
)
AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef",
    {
        "ServiceType": NotRequired[str],
    },
)
AwsEc2VpcPeeringConnectionStatusDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionStatusDetailsTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
VpcInfoCidrBlockSetDetailsTypeDef = TypedDict(
    "VpcInfoCidrBlockSetDetailsTypeDef",
    {
        "CidrBlock": NotRequired[str],
    },
)
VpcInfoIpv6CidrBlockSetDetailsTypeDef = TypedDict(
    "VpcInfoIpv6CidrBlockSetDetailsTypeDef",
    {
        "Ipv6CidrBlock": NotRequired[str],
    },
)
VpcInfoPeeringOptionsDetailsTypeDef = TypedDict(
    "VpcInfoPeeringOptionsDetailsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalClassicLinkToRemoteVpc": NotRequired[bool],
        "AllowEgressFromLocalVpcToRemoteClassicLink": NotRequired[bool],
    },
)
AwsEc2VpnConnectionRoutesDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionRoutesDetailsTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "State": NotRequired[str],
    },
)
AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef",
    {
        "AcceptedRouteCount": NotRequired[int],
        "CertificateArn": NotRequired[str],
        "LastStatusChange": NotRequired[str],
        "OutsideIpAddress": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsTunnelOptionsDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsPaginatorTypeDef",
    {
        "DpdTimeoutSeconds": NotRequired[int],
        "IkeVersions": NotRequired[List[str]],
        "OutsideIpAddress": NotRequired[str],
        "Phase1DhGroupNumbers": NotRequired[List[int]],
        "Phase1EncryptionAlgorithms": NotRequired[List[str]],
        "Phase1IntegrityAlgorithms": NotRequired[List[str]],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2DhGroupNumbers": NotRequired[List[int]],
        "Phase2EncryptionAlgorithms": NotRequired[List[str]],
        "Phase2IntegrityAlgorithms": NotRequired[List[str]],
        "Phase2LifetimeSeconds": NotRequired[int],
        "PreSharedKey": NotRequired[str],
        "RekeyFuzzPercentage": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "TunnelInsideCidr": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef",
    {
        "DpdTimeoutSeconds": NotRequired[int],
        "IkeVersions": NotRequired[Sequence[str]],
        "OutsideIpAddress": NotRequired[str],
        "Phase1DhGroupNumbers": NotRequired[Sequence[int]],
        "Phase1EncryptionAlgorithms": NotRequired[Sequence[str]],
        "Phase1IntegrityAlgorithms": NotRequired[Sequence[str]],
        "Phase1LifetimeSeconds": NotRequired[int],
        "Phase2DhGroupNumbers": NotRequired[Sequence[int]],
        "Phase2EncryptionAlgorithms": NotRequired[Sequence[str]],
        "Phase2IntegrityAlgorithms": NotRequired[Sequence[str]],
        "Phase2LifetimeSeconds": NotRequired[int],
        "PreSharedKey": NotRequired[str],
        "RekeyFuzzPercentage": NotRequired[int],
        "RekeyMarginTimeSeconds": NotRequired[int],
        "ReplayWindowSize": NotRequired[int],
        "TunnelInsideCidr": NotRequired[str],
    },
)
AwsEcrContainerImageDetailsPaginatorTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsPaginatorTypeDef",
    {
        "RegistryId": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Architecture": NotRequired[str],
        "ImageDigest": NotRequired[str],
        "ImageTags": NotRequired[List[str]],
        "ImagePublishedAt": NotRequired[str],
    },
)
AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "RegistryId": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Architecture": NotRequired[str],
        "ImageDigest": NotRequired[str],
        "ImageTags": NotRequired[Sequence[str]],
        "ImagePublishedAt": NotRequired[str],
    },
)
AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef",
    {
        "ScanOnPush": NotRequired[bool],
    },
)
AwsEcrRepositoryLifecyclePolicyDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryLifecyclePolicyDetailsTypeDef",
    {
        "LifecyclePolicyText": NotRequired[str],
        "RegistryId": NotRequired[str],
    },
)
AwsEcsClusterClusterSettingsDetailsTypeDef = TypedDict(
    "AwsEcsClusterClusterSettingsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef",
    {
        "CloudWatchEncryptionEnabled": NotRequired[bool],
        "CloudWatchLogGroupName": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3EncryptionEnabled": NotRequired[bool],
        "S3KeyPrefix": NotRequired[str],
    },
)
AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": NotRequired[int],
        "CapacityProvider": NotRequired[str],
        "Weight": NotRequired[int],
    },
)
AwsMountPointTypeDef = TypedDict(
    "AwsMountPointTypeDef",
    {
        "SourceVolume": NotRequired[str],
        "ContainerPath": NotRequired[str],
    },
)
AwsEcsServiceCapacityProviderStrategyDetailsTypeDef = TypedDict(
    "AwsEcsServiceCapacityProviderStrategyDetailsTypeDef",
    {
        "Base": NotRequired[int],
        "CapacityProvider": NotRequired[str],
        "Weight": NotRequired[int],
    },
)
AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef",
    {
        "Enable": NotRequired[bool],
        "Rollback": NotRequired[bool],
    },
)
AwsEcsServiceDeploymentControllerDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentControllerDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsEcsServiceLoadBalancersDetailsTypeDef = TypedDict(
    "AwsEcsServiceLoadBalancersDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ContainerPort": NotRequired[int],
        "LoadBalancerName": NotRequired[str],
        "TargetGroupArn": NotRequired[str],
    },
)
AwsEcsServicePlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsServicePlacementStrategiesDetailsTypeDef = TypedDict(
    "AwsEcsServicePlacementStrategiesDetailsTypeDef",
    {
        "Field": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsServiceServiceRegistriesDetailsTypeDef = TypedDict(
    "AwsEcsServiceServiceRegistriesDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ContainerPort": NotRequired[int],
        "Port": NotRequired[int],
        "RegistryArn": NotRequired[str],
    },
)
AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsPaginatorTypeDef",
    {
        "AssignPublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "Subnets": NotRequired[List[str]],
    },
)
AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef",
    {
        "AssignPublicIp": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Subnets": NotRequired[Sequence[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef",
    {
        "Condition": NotRequired[str],
        "ContainerName": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef",
    {
        "Hostname": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsPaginatorTypeDef",
    {
        "Options": NotRequired[Dict[str, str]],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsPaginatorTypeDef",
    {
        "Command": NotRequired[List[str]],
        "Interval": NotRequired[int],
        "Retries": NotRequired[int],
        "StartPeriod": NotRequired[int],
        "Timeout": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "SourceVolume": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef",
    {
        "ContainerPort": NotRequired[int],
        "HostPort": NotRequired[int],
        "Protocol": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef",
    {
        "CredentialsParameter": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ValueFrom": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef",
    {
        "Namespace": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef",
    {
        "HardLimit": NotRequired[int],
        "Name": NotRequired[str],
        "SoftLimit": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef",
    {
        "ReadOnly": NotRequired[bool],
        "SourceContainer": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef",
    {
        "Options": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Interval": NotRequired[int],
        "Retries": NotRequired[int],
        "StartPeriod": NotRequired[int],
        "Timeout": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsPaginatorTypeDef",
    {
        "Add": NotRequired[List[str]],
        "Drop": NotRequired[List[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef",
    {
        "Add": NotRequired[Sequence[str]],
        "Drop": NotRequired[Sequence[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsPaginatorTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "HostPath": NotRequired[str],
        "Permissions": NotRequired[List[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsPaginatorTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "MountOptions": NotRequired[List[str]],
        "Size": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "HostPath": NotRequired[str],
        "Permissions": NotRequired[Sequence[str]],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef",
    {
        "ContainerPath": NotRequired[str],
        "MountOptions": NotRequired[Sequence[str]],
        "Size": NotRequired[int],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "ValueFrom": NotRequired[str],
    },
)
AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "DeviceType": NotRequired[str],
    },
)
AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef",
    {
        "Expression": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsPaginatorTypeDef",
    {
        "Autoprovision": NotRequired[bool],
        "Driver": NotRequired[str],
        "DriverOpts": NotRequired[Dict[str, str]],
        "Labels": NotRequired[Dict[str, str]],
        "Scope": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesHostDetailsTypeDef",
    {
        "SourcePath": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef",
    {
        "Autoprovision": NotRequired[bool],
        "Driver": NotRequired[str],
        "DriverOpts": NotRequired[Mapping[str, str]],
        "Labels": NotRequired[Mapping[str, str]],
        "Scope": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Iam": NotRequired[str],
    },
)
AwsEcsTaskVolumeHostDetailsTypeDef = TypedDict(
    "AwsEcsTaskVolumeHostDetailsTypeDef",
    {
        "SourcePath": NotRequired[str],
    },
)
AwsEfsAccessPointPosixUserDetailsPaginatorTypeDef = TypedDict(
    "AwsEfsAccessPointPosixUserDetailsPaginatorTypeDef",
    {
        "Gid": NotRequired[str],
        "SecondaryGids": NotRequired[List[str]],
        "Uid": NotRequired[str],
    },
)
AwsEfsAccessPointPosixUserDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointPosixUserDetailsTypeDef",
    {
        "Gid": NotRequired[str],
        "SecondaryGids": NotRequired[Sequence[str]],
        "Uid": NotRequired[str],
    },
)
AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef",
    {
        "OwnerGid": NotRequired[str],
        "OwnerUid": NotRequired[str],
        "Permissions": NotRequired[str],
    },
)
AwsEksClusterResourcesVpcConfigDetailsPaginatorTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsPaginatorTypeDef",
    {
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "EndpointPublicAccess": NotRequired[bool],
    },
)
AwsEksClusterResourcesVpcConfigDetailsTypeDef = TypedDict(
    "AwsEksClusterResourcesVpcConfigDetailsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "EndpointPublicAccess": NotRequired[bool],
    },
)
AwsEksClusterLoggingClusterLoggingDetailsPaginatorTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsPaginatorTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Types": NotRequired[List[str]],
    },
)
AwsEksClusterLoggingClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingClusterLoggingDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Types": NotRequired[Sequence[str]],
    },
)
AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "LinkName": NotRequired[str],
    },
)
AwsElasticBeanstalkEnvironmentOptionSettingTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    {
        "Namespace": NotRequired[str],
        "OptionName": NotRequired[str],
        "ResourceName": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Version": NotRequired[str],
    },
)
AwsElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": NotRequired[bool],
        "TLSSecurityPolicy": NotRequired[str],
    },
)
AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)
AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsElasticsearchDomainServiceSoftwareOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainServiceSoftwareOptionsTypeDef",
    {
        "AutomatedUpdateDate": NotRequired[str],
        "Cancellable": NotRequired[bool],
        "CurrentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "UpdateStatus": NotRequired[str],
    },
)
AwsElasticsearchDomainVPCOptionsPaginatorTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsPaginatorTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "VPCId": NotRequired[str],
    },
)
AwsElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VPCId": NotRequired[str],
    },
)
AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)
AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)
AwsElbAppCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbAppCookieStickinessPolicyTypeDef",
    {
        "CookieName": NotRequired[str],
        "PolicyName": NotRequired[str],
    },
)
AwsElbLbCookieStickinessPolicyTypeDef = TypedDict(
    "AwsElbLbCookieStickinessPolicyTypeDef",
    {
        "CookieExpirationPeriod": NotRequired[int],
        "PolicyName": NotRequired[str],
    },
)
AwsElbLoadBalancerAccessLogTypeDef = TypedDict(
    "AwsElbLoadBalancerAccessLogTypeDef",
    {
        "EmitInterval": NotRequired[int],
        "Enabled": NotRequired[bool],
        "S3BucketName": NotRequired[str],
        "S3BucketPrefix": NotRequired[str],
    },
)
AwsElbLoadBalancerAdditionalAttributeTypeDef = TypedDict(
    "AwsElbLoadBalancerAdditionalAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsElbLoadBalancerConnectionDrainingTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Timeout": NotRequired[int],
    },
)
AwsElbLoadBalancerConnectionSettingsTypeDef = TypedDict(
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    {
        "IdleTimeout": NotRequired[int],
    },
)
AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef = TypedDict(
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsElbLoadBalancerBackendServerDescriptionPaginatorTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionPaginatorTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[List[str]],
    },
)
AwsElbLoadBalancerBackendServerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    {
        "InstancePort": NotRequired[int],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)
AwsElbLoadBalancerHealthCheckTypeDef = TypedDict(
    "AwsElbLoadBalancerHealthCheckTypeDef",
    {
        "HealthyThreshold": NotRequired[int],
        "Interval": NotRequired[int],
        "Target": NotRequired[str],
        "Timeout": NotRequired[int],
        "UnhealthyThreshold": NotRequired[int],
    },
)
AwsElbLoadBalancerInstanceTypeDef = TypedDict(
    "AwsElbLoadBalancerInstanceTypeDef",
    {
        "InstanceId": NotRequired[str],
    },
)
AwsElbLoadBalancerSourceSecurityGroupTypeDef = TypedDict(
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "OwnerAlias": NotRequired[str],
    },
)
AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": NotRequired[int],
        "InstanceProtocol": NotRequired[str],
        "LoadBalancerPort": NotRequired[int],
        "Protocol": NotRequired[str],
        "SslCertificateId": NotRequired[str],
    },
)
AwsElbv2LoadBalancerAttributeTypeDef = TypedDict(
    "AwsElbv2LoadBalancerAttributeTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
AwsEventSchemasRegistryDetailsTypeDef = TypedDict(
    "AwsEventSchemasRegistryDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "RegistryArn": NotRequired[str],
        "RegistryName": NotRequired[str],
    },
)
AwsEventsEndpointEventBusesDetailsTypeDef = TypedDict(
    "AwsEventsEndpointEventBusesDetailsTypeDef",
    {
        "EventBusArn": NotRequired[str],
    },
)
AwsEventsEndpointReplicationConfigDetailsTypeDef = TypedDict(
    "AwsEventsEndpointReplicationConfigDetailsTypeDef",
    {
        "State": NotRequired[str],
    },
)
AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef",
    {
        "HealthCheck": NotRequired[str],
    },
)
AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef",
    {
        "Route": NotRequired[str],
    },
)
AwsEventsEventbusDetailsTypeDef = TypedDict(
    "AwsEventsEventbusDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Policy": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef",
    {
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef",
    {
        "Reason": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorFeaturesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorFeaturesDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsIamAccessKeySessionContextAttributesTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    {
        "MfaAuthenticated": NotRequired[bool],
        "CreationDate": NotRequired[str],
    },
)
AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {
        "Type": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "Arn": NotRequired[str],
        "AccountId": NotRequired[str],
        "UserName": NotRequired[str],
    },
)
AwsIamAttachedManagedPolicyTypeDef = TypedDict(
    "AwsIamAttachedManagedPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)
AwsIamGroupPolicyTypeDef = TypedDict(
    "AwsIamGroupPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)
AwsIamInstanceProfileRoleTypeDef = TypedDict(
    "AwsIamInstanceProfileRoleTypeDef",
    {
        "Arn": NotRequired[str],
        "AssumeRolePolicyDocument": NotRequired[str],
        "CreateDate": NotRequired[str],
        "Path": NotRequired[str],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
    },
)
AwsIamPermissionsBoundaryTypeDef = TypedDict(
    "AwsIamPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryArn": NotRequired[str],
        "PermissionsBoundaryType": NotRequired[str],
    },
)
AwsIamPolicyVersionTypeDef = TypedDict(
    "AwsIamPolicyVersionTypeDef",
    {
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "CreateDate": NotRequired[str],
    },
)
AwsIamRolePolicyTypeDef = TypedDict(
    "AwsIamRolePolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)
AwsIamUserPolicyTypeDef = TypedDict(
    "AwsIamUserPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
    },
)
AwsKinesisStreamStreamEncryptionDetailsTypeDef = TypedDict(
    "AwsKinesisStreamStreamEncryptionDetailsTypeDef",
    {
        "EncryptionType": NotRequired[str],
        "KeyId": NotRequired[str],
    },
)
AwsKmsKeyDetailsTypeDef = TypedDict(
    "AwsKmsKeyDetailsTypeDef",
    {
        "AWSAccountId": NotRequired[str],
        "CreationDate": NotRequired[float],
        "KeyId": NotRequired[str],
        "KeyManager": NotRequired[str],
        "KeyState": NotRequired[str],
        "Origin": NotRequired[str],
        "Description": NotRequired[str],
        "KeyRotationStatus": NotRequired[bool],
    },
)
AwsLambdaFunctionCodeTypeDef = TypedDict(
    "AwsLambdaFunctionCodeTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3ObjectVersion": NotRequired[str],
        "ZipFile": NotRequired[str],
    },
)
AwsLambdaFunctionDeadLetterConfigTypeDef = TypedDict(
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    {
        "TargetArn": NotRequired[str],
    },
)
AwsLambdaFunctionLayerTypeDef = TypedDict(
    "AwsLambdaFunctionLayerTypeDef",
    {
        "Arn": NotRequired[str],
        "CodeSize": NotRequired[int],
    },
)
AwsLambdaFunctionTracingConfigTypeDef = TypedDict(
    "AwsLambdaFunctionTracingConfigTypeDef",
    {
        "Mode": NotRequired[str],
    },
)
AwsLambdaFunctionVpcConfigPaginatorTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigPaginatorTypeDef",
    {
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "VpcId": NotRequired[str],
    },
)
AwsLambdaFunctionVpcConfigTypeDef = TypedDict(
    "AwsLambdaFunctionVpcConfigTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
    },
)
AwsLambdaFunctionEnvironmentErrorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AwsLambdaLayerVersionDetailsPaginatorTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsPaginatorTypeDef",
    {
        "Version": NotRequired[int],
        "CompatibleRuntimes": NotRequired[List[str]],
        "CreatedDate": NotRequired[str],
    },
)
AwsLambdaLayerVersionDetailsTypeDef = TypedDict(
    "AwsLambdaLayerVersionDetailsTypeDef",
    {
        "Version": NotRequired[int],
        "CompatibleRuntimes": NotRequired[Sequence[str]],
        "CreatedDate": NotRequired[str],
    },
)
AwsMskClusterClusterInfoClientAuthenticationTlsDetailsPaginatorTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsPaginatorTypeDef",
    {
        "CertificateAuthorityArnList": NotRequired[List[str]],
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef",
    {
        "CertificateAuthorityArnList": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef",
    {
        "DataVolumeKMSKeyId": NotRequired[str],
    },
)
AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef",
    {
        "InCluster": NotRequired[bool],
        "ClientBroker": NotRequired[str],
    },
)
AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef",
    {
        "SubnetId": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef",
    {
        "MasterUserArn": NotRequired[str],
        "MasterUserName": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef",
    {
        "AvailabilityZoneCount": NotRequired[int],
    },
)
AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef",
    {
        "CustomEndpointCertificateArn": NotRequired[str],
        "CustomEndpointEnabled": NotRequired[bool],
        "EnforceHTTPS": NotRequired[bool],
        "CustomEndpoint": NotRequired[str],
        "TLSSecurityPolicy": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef",
    {
        "AutomatedUpdateDate": NotRequired[str],
        "Cancellable": NotRequired[bool],
        "CurrentVersion": NotRequired[str],
        "Description": NotRequired[str],
        "NewVersion": NotRequired[str],
        "UpdateAvailable": NotRequired[bool],
        "UpdateStatus": NotRequired[str],
        "OptionalDeployment": NotRequired[bool],
    },
)
AwsOpenSearchServiceDomainVpcOptionsDetailsPaginatorTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsPaginatorTypeDef",
    {
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
    },
)
AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef",
    {
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)
AwsOpenSearchServiceDomainLogPublishingOptionTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "Enabled": NotRequired[bool],
    },
)
AwsRdsDbClusterAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbClusterMemberTypeDef = TypedDict(
    "AwsRdsDbClusterMemberTypeDef",
    {
        "IsClusterWriter": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "DbClusterParameterGroupStatus": NotRequired[str],
    },
)
AwsRdsDbClusterOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    {
        "DbClusterOptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbDomainMembershipTypeDef = TypedDict(
    "AwsRdsDbDomainMembershipTypeDef",
    {
        "Domain": NotRequired[str],
        "Status": NotRequired[str],
        "Fqdn": NotRequired[str],
        "IamRoleName": NotRequired[str],
    },
)
AwsRdsDbInstanceVpcSecurityGroupTypeDef = TypedDict(
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbClusterSnapshotDbClusterSnapshotAttributePaginatorTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributePaginatorTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)
AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[Sequence[str]],
    },
)
AwsRdsDbInstanceAssociatedRoleTypeDef = TypedDict(
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FeatureName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbInstanceEndpointTypeDef = TypedDict(
    "AwsRdsDbInstanceEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "HostedZoneId": NotRequired[str],
    },
)
AwsRdsDbOptionGroupMembershipTypeDef = TypedDict(
    "AwsRdsDbOptionGroupMembershipTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbParameterGroupTypeDef = TypedDict(
    "AwsRdsDbParameterGroupTypeDef",
    {
        "DbParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
    },
)
AwsRdsDbProcessorFeatureTypeDef = TypedDict(
    "AwsRdsDbProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsRdsDbStatusInfoTypeDef = TypedDict(
    "AwsRdsDbStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AwsRdsPendingCloudWatchLogsExportsPaginatorTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsPaginatorTypeDef",
    {
        "LogTypesToEnable": NotRequired[List[str]],
        "LogTypesToDisable": NotRequired[List[str]],
    },
)
AwsRdsPendingCloudWatchLogsExportsTypeDef = TypedDict(
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": NotRequired[Sequence[str]],
        "LogTypesToDisable": NotRequired[Sequence[str]],
    },
)
AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef",
    {
        "Ec2SecurityGroupId": NotRequired[str],
        "Ec2SecurityGroupName": NotRequired[str],
        "Ec2SecurityGroupOwnerId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbSecurityGroupIpRangeTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupIpRangeTypeDef",
    {
        "CidrIp": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
AwsRdsEventSubscriptionDetailsPaginatorTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsPaginatorTypeDef",
    {
        "CustSubscriptionId": NotRequired[str],
        "CustomerAwsId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "EventCategoriesList": NotRequired[List[str]],
        "EventSubscriptionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "SourceType": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
    },
)
AwsRdsEventSubscriptionDetailsTypeDef = TypedDict(
    "AwsRdsEventSubscriptionDetailsTypeDef",
    {
        "CustSubscriptionId": NotRequired[str],
        "CustomerAwsId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "EventCategoriesList": NotRequired[Sequence[str]],
        "EventSubscriptionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SourceIdsList": NotRequired[Sequence[str]],
        "SourceType": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
    },
)
AwsRedshiftClusterClusterNodeTypeDef = TypedDict(
    "AwsRedshiftClusterClusterNodeTypeDef",
    {
        "NodeRole": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
    },
)
AwsRedshiftClusterClusterParameterStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterApplyErrorDescription": NotRequired[str],
    },
)
AwsRedshiftClusterClusterSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef = TypedDict(
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "RetentionPeriod": NotRequired[int],
        "SnapshotCopyGrantName": NotRequired[str],
    },
)
AwsRedshiftClusterDeferredMaintenanceWindowTypeDef = TypedDict(
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceEndTime": NotRequired[str],
        "DeferMaintenanceIdentifier": NotRequired[str],
        "DeferMaintenanceStartTime": NotRequired[str],
    },
)
AwsRedshiftClusterElasticIpStatusTypeDef = TypedDict(
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    {
        "ElasticIp": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterEndpointTypeDef = TypedDict(
    "AwsRedshiftClusterEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)
AwsRedshiftClusterHsmStatusTypeDef = TypedDict(
    "AwsRedshiftClusterHsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterIamRoleTypeDef = TypedDict(
    "AwsRedshiftClusterIamRoleTypeDef",
    {
        "ApplyStatus": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
AwsRedshiftClusterLoggingStatusTypeDef = TypedDict(
    "AwsRedshiftClusterLoggingStatusTypeDef",
    {
        "BucketName": NotRequired[str],
        "LastFailureMessage": NotRequired[str],
        "LastFailureTime": NotRequired[str],
        "LastSuccessfulDeliveryTime": NotRequired[str],
        "LoggingEnabled": NotRequired[bool],
        "S3KeyPrefix": NotRequired[str],
    },
)
AwsRedshiftClusterPendingModifiedValuesTypeDef = TypedDict(
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    {
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ClusterIdentifier": NotRequired[str],
        "ClusterType": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "EncryptionType": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "MaintenanceTrackName": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
    },
)
AwsRedshiftClusterResizeInfoTypeDef = TypedDict(
    "AwsRedshiftClusterResizeInfoTypeDef",
    {
        "AllowCancelResize": NotRequired[bool],
        "ResizeType": NotRequired[str],
    },
)
AwsRedshiftClusterRestoreStatusTypeDef = TypedDict(
    "AwsRedshiftClusterRestoreStatusTypeDef",
    {
        "CurrentRestoreRateInMegaBytesPerSecond": NotRequired[float],
        "ElapsedTimeInSeconds": NotRequired[int],
        "EstimatedTimeToCompletionInSeconds": NotRequired[int],
        "ProgressInMegaBytes": NotRequired[int],
        "SnapshotSizeInMegaBytes": NotRequired[int],
        "Status": NotRequired[str],
    },
)
AwsRedshiftClusterVpcSecurityGroupTypeDef = TypedDict(
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "VpcSecurityGroupId": NotRequired[str],
    },
)
AwsRoute53HostedZoneConfigDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneConfigDetailsTypeDef",
    {
        "Comment": NotRequired[str],
    },
)
AwsRoute53HostedZoneVpcDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneVpcDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Region": NotRequired[str],
    },
)
CloudWatchLogsLogGroupArnConfigDetailsTypeDef = TypedDict(
    "CloudWatchLogsLogGroupArnConfigDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "HostedZoneId": NotRequired[str],
        "Id": NotRequired[str],
    },
)
AwsS3AccessPointVpcConfigurationDetailsTypeDef = TypedDict(
    "AwsS3AccessPointVpcConfigurationDetailsTypeDef",
    {
        "VpcId": NotRequired[str],
    },
)
AwsS3AccountPublicAccessBlockDetailsTypeDef = TypedDict(
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    {
        "BlockPublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
        "IgnorePublicAcls": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef = (
    TypedDict(
        "AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef",
        {
            "DaysAfterInitiation": NotRequired[int],
        },
    )
)
AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef",
    {
        "Days": NotRequired[int],
        "StorageClass": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef",
    {
        "Date": NotRequired[str],
        "Days": NotRequired[int],
        "StorageClass": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsS3BucketBucketVersioningConfigurationTypeDef = TypedDict(
    "AwsS3BucketBucketVersioningConfigurationTypeDef",
    {
        "IsMfaDeleteEnabled": NotRequired[bool],
        "Status": NotRequired[str],
    },
)
AwsS3BucketLoggingConfigurationTypeDef = TypedDict(
    "AwsS3BucketLoggingConfigurationTypeDef",
    {
        "DestinationBucketName": NotRequired[str],
        "LogFilePrefix": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef",
    {
        "Name": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType],
        "Value": NotRequired[str],
    },
)
AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef",
    {
        "Days": NotRequired[int],
        "Mode": NotRequired[str],
        "Years": NotRequired[int],
    },
)
AwsS3BucketServerSideEncryptionByDefaultTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": NotRequired[str],
        "KMSMasterKeyID": NotRequired[str],
    },
)
AwsS3BucketWebsiteConfigurationRedirectToTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRedirectToTypeDef",
    {
        "Hostname": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)
AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": NotRequired[str],
        "KeyPrefixEquals": NotRequired[str],
    },
)
AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef",
    {
        "Hostname": NotRequired[str],
        "HttpRedirectCode": NotRequired[str],
        "Protocol": NotRequired[str],
        "ReplaceKeyPrefixWith": NotRequired[str],
        "ReplaceKeyWith": NotRequired[str],
    },
)
AwsS3ObjectDetailsTypeDef = TypedDict(
    "AwsS3ObjectDetailsTypeDef",
    {
        "LastModified": NotRequired[str],
        "ETag": NotRequired[str],
        "VersionId": NotRequired[str],
        "ContentType": NotRequired[str],
        "ServerSideEncryption": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
    },
)
AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": NotRequired[str],
    },
)
AwsSecretsManagerSecretRotationRulesTypeDef = TypedDict(
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    {
        "AutomaticallyAfterDays": NotRequired[int],
    },
)
BooleanFilterTypeDef = TypedDict(
    "BooleanFilterTypeDef",
    {
        "Value": NotRequired[bool],
    },
)
IpFilterTypeDef = TypedDict(
    "IpFilterTypeDef",
    {
        "Cidr": NotRequired[str],
    },
)
KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Value": NotRequired[str],
    },
)
AwsSecurityFindingIdentifierTypeDef = TypedDict(
    "AwsSecurityFindingIdentifierTypeDef",
    {
        "Id": str,
        "ProductArn": str,
    },
)
GeneratorDetailsPaginatorTypeDef = TypedDict(
    "GeneratorDetailsPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Labels": NotRequired[List[str]],
    },
)
MalwareTypeDef = TypedDict(
    "MalwareTypeDef",
    {
        "Name": str,
        "Type": NotRequired[MalwareTypeType],
        "Path": NotRequired[str],
        "State": NotRequired[MalwareStateType],
    },
)
NoteTypeDef = TypedDict(
    "NoteTypeDef",
    {
        "Text": str,
        "UpdatedBy": str,
        "UpdatedAt": str,
    },
)
PatchSummaryTypeDef = TypedDict(
    "PatchSummaryTypeDef",
    {
        "Id": str,
        "InstalledCount": NotRequired[int],
        "MissingCount": NotRequired[int],
        "FailedCount": NotRequired[int],
        "InstalledOtherCount": NotRequired[int],
        "InstalledRejectedCount": NotRequired[int],
        "InstalledPendingReboot": NotRequired[int],
        "OperationStartTime": NotRequired[str],
        "OperationEndTime": NotRequired[str],
        "RebootOption": NotRequired[str],
        "Operation": NotRequired[str],
    },
)
ProcessDetailsTypeDef = TypedDict(
    "ProcessDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Path": NotRequired[str],
        "Pid": NotRequired[int],
        "ParentPid": NotRequired[int],
        "LaunchedAt": NotRequired[str],
        "TerminatedAt": NotRequired[str],
    },
)
SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "Product": NotRequired[float],
        "Label": NotRequired[SeverityLabelType],
        "Normalized": NotRequired[int],
        "Original": NotRequired[str],
    },
)
ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": NotRequired[ThreatIntelIndicatorTypeType],
        "Value": NotRequired[str],
        "Category": NotRequired[ThreatIntelIndicatorCategoryType],
        "LastObservedAt": NotRequired[str],
        "Source": NotRequired[str],
        "SourceUrl": NotRequired[str],
    },
)
WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Status": NotRequired[WorkflowStatusType],
    },
)
GeneratorDetailsTypeDef = TypedDict(
    "GeneratorDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Labels": NotRequired[Sequence[str]],
    },
)
AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef",
    {
        "Endpoint": NotRequired[str],
        "Protocol": NotRequired[str],
    },
)
AwsSqsQueueDetailsTypeDef = TypedDict(
    "AwsSqsQueueDetailsTypeDef",
    {
        "KmsDataKeyReusePeriodSeconds": NotRequired[int],
        "KmsMasterKeyId": NotRequired[str],
        "QueueName": NotRequired[str],
        "DeadLetterTargetArn": NotRequired[str],
    },
)
AwsSsmComplianceSummaryTypeDef = TypedDict(
    "AwsSsmComplianceSummaryTypeDef",
    {
        "Status": NotRequired[str],
        "CompliantCriticalCount": NotRequired[int],
        "CompliantHighCount": NotRequired[int],
        "CompliantMediumCount": NotRequired[int],
        "ExecutionType": NotRequired[str],
        "NonCompliantCriticalCount": NotRequired[int],
        "CompliantInformationalCount": NotRequired[int],
        "NonCompliantInformationalCount": NotRequired[int],
        "CompliantUnspecifiedCount": NotRequired[int],
        "NonCompliantLowCount": NotRequired[int],
        "NonCompliantHighCount": NotRequired[int],
        "CompliantLowCount": NotRequired[int],
        "ComplianceType": NotRequired[str],
        "PatchBaselineId": NotRequired[str],
        "OverallSeverity": NotRequired[str],
        "NonCompliantMediumCount": NotRequired[int],
        "NonCompliantUnspecifiedCount": NotRequired[int],
        "PatchGroup": NotRequired[str],
    },
)
AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef",
    {
        "LogGroupArn": NotRequired[str],
    },
)
AwsWafRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRateBasedRuleMatchPredicateTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleMatchPredicateTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRegionalRulePredicateListDetailsTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafRulePredicateListDetailsTypeDef = TypedDict(
    "AwsWafRulePredicateListDetailsTypeDef",
    {
        "DataId": NotRequired[str],
        "Negated": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
AwsWafRuleGroupRulesActionDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesActionDetailsTypeDef",
    {
        "Type": NotRequired[str],
    },
)
WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)
WafExcludedRuleTypeDef = TypedDict(
    "WafExcludedRuleTypeDef",
    {
        "RuleId": NotRequired[str],
    },
)
WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": NotRequired[str],
    },
)
AwsWafv2CustomHttpHeaderTypeDef = TypedDict(
    "AwsWafv2CustomHttpHeaderTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AwsWafv2VisibilityConfigDetailsTypeDef = TypedDict(
    "AwsWafv2VisibilityConfigDetailsTypeDef",
    {
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "MetricName": NotRequired[str],
        "SampledRequestsEnabled": NotRequired[bool],
    },
)
AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef",
    {
        "ImmunityTime": NotRequired[int],
    },
)
AwsXrayEncryptionConfigDetailsTypeDef = TypedDict(
    "AwsXrayEncryptionConfigDetailsTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[str],
        "Type": NotRequired[str],
    },
)
BatchDeleteAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchDeleteAutomationRulesRequestRequestTypeDef",
    {
        "AutomationRulesArns": Sequence[str],
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
UnprocessedAutomationRuleTypeDef = TypedDict(
    "UnprocessedAutomationRuleTypeDef",
    {
        "RuleArn": NotRequired[str],
        "ErrorCode": NotRequired[int],
        "ErrorMessage": NotRequired[str],
    },
)
BatchDisableStandardsRequestRequestTypeDef = TypedDict(
    "BatchDisableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": Sequence[str],
    },
)
StandardsSubscriptionRequestTypeDef = TypedDict(
    "StandardsSubscriptionRequestTypeDef",
    {
        "StandardsArn": str,
        "StandardsInput": NotRequired[Mapping[str, str]],
    },
)
BatchGetAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchGetAutomationRulesRequestRequestTypeDef",
    {
        "AutomationRulesArns": Sequence[str],
    },
)
ConfigurationPolicyAssociationSummaryTypeDef = TypedDict(
    "ConfigurationPolicyAssociationSummaryTypeDef",
    {
        "ConfigurationPolicyId": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[TargetTypeType],
        "AssociationType": NotRequired[AssociationTypeType],
        "UpdatedAt": NotRequired[datetime],
        "AssociationStatus": NotRequired[ConfigurationPolicyAssociationStatusType],
        "AssociationStatusMessage": NotRequired[str],
    },
)
BatchGetSecurityControlsRequestRequestTypeDef = TypedDict(
    "BatchGetSecurityControlsRequestRequestTypeDef",
    {
        "SecurityControlIds": Sequence[str],
    },
)
UnprocessedSecurityControlTypeDef = TypedDict(
    "UnprocessedSecurityControlTypeDef",
    {
        "SecurityControlId": str,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": NotRequired[str],
    },
)
StandardsControlAssociationIdTypeDef = TypedDict(
    "StandardsControlAssociationIdTypeDef",
    {
        "SecurityControlId": str,
        "StandardsArn": str,
    },
)
StandardsControlAssociationDetailTypeDef = TypedDict(
    "StandardsControlAssociationDetailTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "AssociationStatus": AssociationStatusType,
        "RelatedRequirements": NotRequired[List[str]],
        "UpdatedAt": NotRequired[datetime],
        "UpdatedReason": NotRequired[str],
        "StandardsControlTitle": NotRequired[str],
        "StandardsControlDescription": NotRequired[str],
        "StandardsControlArns": NotRequired[List[str]],
    },
)
ImportFindingsErrorTypeDef = TypedDict(
    "ImportFindingsErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
StandardsControlAssociationUpdateTypeDef = TypedDict(
    "StandardsControlAssociationUpdateTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "AssociationStatus": AssociationStatusType,
        "UpdatedReason": NotRequired[str],
    },
)
BooleanConfigurationOptionsTypeDef = TypedDict(
    "BooleanConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[bool],
    },
)
CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "Column": NotRequired[int],
        "Row": NotRequired[int],
        "ColumnName": NotRequired[str],
        "CellReference": NotRequired[str],
    },
)
ClassificationStatusTypeDef = TypedDict(
    "ClassificationStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
CodeVulnerabilitiesFilePathTypeDef = TypedDict(
    "CodeVulnerabilitiesFilePathTypeDef",
    {
        "EndLine": NotRequired[int],
        "FileName": NotRequired[str],
        "FilePath": NotRequired[str],
        "StartLine": NotRequired[int],
    },
)
SecurityControlParameterPaginatorTypeDef = TypedDict(
    "SecurityControlParameterPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[List[str]],
    },
)
StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "ReasonCode": str,
        "Description": NotRequired[str],
    },
)
SecurityControlParameterTypeDef = TypedDict(
    "SecurityControlParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[Sequence[str]],
    },
)
DoubleConfigurationOptionsTypeDef = TypedDict(
    "DoubleConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[float],
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
EnumConfigurationOptionsTypeDef = TypedDict(
    "EnumConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[List[str]],
    },
)
EnumListConfigurationOptionsTypeDef = TypedDict(
    "EnumListConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[List[str]],
        "MaxItems": NotRequired[int],
        "AllowedValues": NotRequired[List[str]],
    },
)
IntegerConfigurationOptionsTypeDef = TypedDict(
    "IntegerConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[int],
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
IntegerListConfigurationOptionsTypeDef = TypedDict(
    "IntegerListConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[List[int]],
        "Min": NotRequired[int],
        "Max": NotRequired[int],
        "MaxItems": NotRequired[int],
    },
)
StringConfigurationOptionsTypeDef = TypedDict(
    "StringConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Re2Expression": NotRequired[str],
        "ExpressionDescription": NotRequired[str],
    },
)
StringListConfigurationOptionsTypeDef = TypedDict(
    "StringListConfigurationOptionsTypeDef",
    {
        "DefaultValue": NotRequired[List[str]],
        "Re2Expression": NotRequired[str],
        "MaxItems": NotRequired[int],
        "ExpressionDescription": NotRequired[str],
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "RootId": NotRequired[str],
    },
)
ConfigurationPolicySummaryTypeDef = TypedDict(
    "ConfigurationPolicySummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "ServiceEnabled": NotRequired[bool],
    },
)
VolumeMountTypeDef = TypedDict(
    "VolumeMountTypeDef",
    {
        "Name": NotRequired[str],
        "MountPath": NotRequired[str],
    },
)
CreateActionTargetRequestRequestTypeDef = TypedDict(
    "CreateActionTargetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Id": str,
    },
)
CreateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "CreateFindingAggregatorRequestRequestTypeDef",
    {
        "RegionLinkingMode": str,
        "Regions": NotRequired[Sequence[str]],
    },
)
ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "AccountId": NotRequired[str],
        "ProcessingResult": NotRequired[str],
    },
)
DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "Value": NotRequired[int],
        "Unit": NotRequired[Literal["DAYS"]],
    },
)
DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
DeleteActionTargetRequestRequestTypeDef = TypedDict(
    "DeleteActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
    },
)
DeleteConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationPolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteFindingAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)
DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)
DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
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
DescribeActionTargetsRequestRequestTypeDef = TypedDict(
    "DescribeActionTargetsRequestRequestTypeDef",
    {
        "ActionTargetArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubArn": NotRequired[str],
    },
)
OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "ConfigurationType": NotRequired[OrganizationConfigurationConfigurationTypeType],
        "Status": NotRequired[OrganizationConfigurationStatusType],
        "StatusMessage": NotRequired[str],
    },
)
DescribeProductsRequestRequestTypeDef = TypedDict(
    "DescribeProductsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ProductArn": NotRequired[str],
    },
)
ProductTypeDef = TypedDict(
    "ProductTypeDef",
    {
        "ProductArn": str,
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Description": NotRequired[str],
        "Categories": NotRequired[List[str]],
        "IntegrationTypes": NotRequired[List[IntegrationTypeType]],
        "MarketplaceUrl": NotRequired[str],
        "ActivationUrl": NotRequired[str],
        "ProductSubscriptionResourcePolicy": NotRequired[str],
    },
)
DescribeStandardsControlsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsControlsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
StandardsControlTypeDef = TypedDict(
    "StandardsControlTypeDef",
    {
        "StandardsControlArn": NotRequired[str],
        "ControlStatus": NotRequired[ControlStatusType],
        "DisabledReason": NotRequired[str],
        "ControlStatusUpdatedAt": NotRequired[datetime],
        "ControlId": NotRequired[str],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "RemediationUrl": NotRequired[str],
        "SeverityRating": NotRequired[SeverityRatingType],
        "RelatedRequirements": NotRequired[List[str]],
    },
)
DescribeStandardsRequestRequestTypeDef = TypedDict(
    "DescribeStandardsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DisableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "DisableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductSubscriptionArn": str,
    },
)
DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)
DisassociateMembersRequestRequestTypeDef = TypedDict(
    "DisassociateMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
EnableImportFindingsForProductRequestRequestTypeDef = TypedDict(
    "EnableImportFindingsForProductRequestRequestTypeDef",
    {
        "ProductArn": str,
    },
)
EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AdminAccountId": str,
    },
)
EnableSecurityHubRequestRequestTypeDef = TypedDict(
    "EnableSecurityHubRequestRequestTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
        "EnableDefaultStandards": NotRequired[bool],
        "ControlFindingGenerator": NotRequired[ControlFindingGeneratorType],
    },
)
FilePathsTypeDef = TypedDict(
    "FilePathsTypeDef",
    {
        "FilePath": NotRequired[str],
        "FileName": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Hash": NotRequired[str],
    },
)
FindingAggregatorTypeDef = TypedDict(
    "FindingAggregatorTypeDef",
    {
        "FindingAggregatorArn": NotRequired[str],
    },
)
FindingHistoryUpdateSourceTypeDef = TypedDict(
    "FindingHistoryUpdateSourceTypeDef",
    {
        "Type": NotRequired[FindingHistoryUpdateSourceTypeType],
        "Identity": NotRequired[str],
    },
)
FindingHistoryUpdateTypeDef = TypedDict(
    "FindingHistoryUpdateTypeDef",
    {
        "UpdatedField": NotRequired[str],
        "OldValue": NotRequired[str],
        "NewValue": NotRequired[str],
    },
)
FindingProviderSeverityTypeDef = TypedDict(
    "FindingProviderSeverityTypeDef",
    {
        "Label": NotRequired[SeverityLabelType],
        "Original": NotRequired[str],
    },
)
FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)
FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef",
    {
        "Priority": NotRequired[int],
        "ResourceArn": NotRequired[str],
    },
)
InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "AccountId": NotRequired[str],
        "InvitationId": NotRequired[str],
        "InvitedAt": NotRequired[datetime],
        "MemberStatus": NotRequired[str],
    },
)
GetConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "GetConfigurationPolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetEnabledStandardsRequestRequestTypeDef = TypedDict(
    "GetEnabledStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetFindingAggregatorRequestRequestTypeDef = TypedDict(
    "GetFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
    },
)
TimestampTypeDef = Union[datetime, str]
SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "Field": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)
GetInsightResultsRequestRequestTypeDef = TypedDict(
    "GetInsightResultsRequestRequestTypeDef",
    {
        "InsightArn": str,
    },
)
GetInsightsRequestRequestTypeDef = TypedDict(
    "GetInsightsRequestRequestTypeDef",
    {
        "InsightArns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "AccountId": NotRequired[str],
        "Email": NotRequired[str],
        "MasterId": NotRequired[str],
        "AdministratorId": NotRequired[str],
        "MemberStatus": NotRequired[str],
        "InvitedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
GetSecurityControlDefinitionRequestRequestTypeDef = TypedDict(
    "GetSecurityControlDefinitionRequestRequestTypeDef",
    {
        "SecurityControlId": str,
    },
)
InsightResultValueTypeDef = TypedDict(
    "InsightResultValueTypeDef",
    {
        "GroupByAttributeValue": str,
        "Count": int,
    },
)
InviteMembersRequestRequestTypeDef = TypedDict(
    "InviteMembersRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
    },
)
ListAutomationRulesRequestRequestTypeDef = TypedDict(
    "ListAutomationRulesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListConfigurationPoliciesRequestRequestTypeDef = TypedDict(
    "ListConfigurationPoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEnabledProductsForImportRequestRequestTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFindingAggregatorsRequestRequestTypeDef = TypedDict(
    "ListFindingAggregatorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "OnlyAssociated": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSecurityControlDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSecurityControlDefinitionsRequestRequestTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "ListStandardsControlAssociationsRequestRequestTypeDef",
    {
        "SecurityControlId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
StandardsControlAssociationSummaryTypeDef = TypedDict(
    "StandardsControlAssociationSummaryTypeDef",
    {
        "StandardsArn": str,
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "AssociationStatus": AssociationStatusType,
        "RelatedRequirements": NotRequired[List[str]],
        "UpdatedAt": NotRequired[datetime],
        "UpdatedReason": NotRequired[str],
        "StandardsControlTitle": NotRequired[str],
        "StandardsControlDescription": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "Begin": NotRequired[int],
        "End": NotRequired[int],
    },
)
RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Start": NotRequired[int],
        "End": NotRequired[int],
        "StartColumn": NotRequired[int],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "JsonPath": NotRequired[str],
        "RecordIndex": NotRequired[int],
    },
)
ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "Integer": NotRequired[int],
        "IntegerList": NotRequired[List[int]],
        "Double": NotRequired[float],
        "String": NotRequired[str],
        "StringList": NotRequired[List[str]],
        "Boolean": NotRequired[bool],
        "Enum": NotRequired[str],
        "EnumList": NotRequired[List[str]],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Text": NotRequired[str],
        "Url": NotRequired[str],
    },
)
RuleGroupSourceListDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceListDetailsPaginatorTypeDef",
    {
        "GeneratedRulesType": NotRequired[str],
        "TargetTypes": NotRequired[List[str]],
        "Targets": NotRequired[List[str]],
    },
)
RuleGroupSourceListDetailsTypeDef = TypedDict(
    "RuleGroupSourceListDetailsTypeDef",
    {
        "GeneratedRulesType": NotRequired[str],
        "TargetTypes": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence[str]],
    },
)
RuleGroupSourceStatefulRulesHeaderDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesHeaderDetailsTypeDef",
    {
        "Destination": NotRequired[str],
        "DestinationPort": NotRequired[str],
        "Direction": NotRequired[str],
        "Protocol": NotRequired[str],
        "Source": NotRequired[str],
        "SourcePort": NotRequired[str],
    },
)
RuleGroupSourceStatefulRulesOptionsDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsPaginatorTypeDef",
    {
        "Keyword": NotRequired[str],
        "Settings": NotRequired[List[str]],
    },
)
RuleGroupSourceStatefulRulesOptionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesOptionsDetailsTypeDef",
    {
        "Keyword": NotRequired[str],
        "Settings": NotRequired[Sequence[str]],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef",
    {
        "AddressDefinition": NotRequired[str],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef",
    {
        "AddressDefinition": NotRequired[str],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsPaginatorTypeDef",
    {
        "Flags": NotRequired[List[str]],
        "Masks": NotRequired[List[str]],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef",
    {
        "Flags": NotRequired[Sequence[str]],
        "Masks": NotRequired[Sequence[str]],
    },
)
RuleGroupVariablesIpSetsDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsPaginatorTypeDef",
    {
        "Definition": NotRequired[List[str]],
    },
)
RuleGroupVariablesIpSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesIpSetsDetailsTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)
RuleGroupVariablesPortSetsDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsPaginatorTypeDef",
    {
        "Definition": NotRequired[List[str]],
    },
)
RuleGroupVariablesPortSetsDetailsTypeDef = TypedDict(
    "RuleGroupVariablesPortSetsDetailsTypeDef",
    {
        "Definition": NotRequired[Sequence[str]],
    },
)
SoftwarePackageTypeDef = TypedDict(
    "SoftwarePackageTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Epoch": NotRequired[str],
        "Release": NotRequired[str],
        "Architecture": NotRequired[str],
        "PackageManager": NotRequired[str],
        "FilePath": NotRequired[str],
        "FixedInVersion": NotRequired[str],
        "Remediation": NotRequired[str],
        "SourceLayerHash": NotRequired[str],
        "SourceLayerArn": NotRequired[str],
    },
)
StandardsManagedByTypeDef = TypedDict(
    "StandardsManagedByTypeDef",
    {
        "Company": NotRequired[str],
        "Product": NotRequired[str],
    },
)
StandardsStatusReasonTypeDef = TypedDict(
    "StandardsStatusReasonTypeDef",
    {
        "StatusReasonCode": StatusReasonCodeType,
    },
)
StatelessCustomPublishMetricActionDimensionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionDimensionTypeDef",
    {
        "Value": NotRequired[str],
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
UpdateActionTargetRequestRequestTypeDef = TypedDict(
    "UpdateActionTargetRequestRequestTypeDef",
    {
        "ActionTargetArn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateFindingAggregatorRequestRequestTypeDef = TypedDict(
    "UpdateFindingAggregatorRequestRequestTypeDef",
    {
        "FindingAggregatorArn": str,
        "RegionLinkingMode": str,
        "Regions": NotRequired[Sequence[str]],
    },
)
UpdateSecurityHubConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSecurityHubConfigurationRequestRequestTypeDef",
    {
        "AutoEnableControls": NotRequired[bool],
        "ControlFindingGenerator": NotRequired[ControlFindingGeneratorType],
    },
)
UpdateStandardsControlRequestRequestTypeDef = TypedDict(
    "UpdateStandardsControlRequestRequestTypeDef",
    {
        "StandardsControlArn": str,
        "ControlStatus": NotRequired[ControlStatusType],
        "DisabledReason": NotRequired[str],
    },
)
VulnerabilityVendorTypeDef = TypedDict(
    "VulnerabilityVendorTypeDef",
    {
        "Name": str,
        "Url": NotRequired[str],
        "VendorSeverity": NotRequired[str],
        "VendorCreatedAt": NotRequired[str],
        "VendorUpdatedAt": NotRequired[str],
    },
)
CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "AccountDetails": Sequence[AccountDetailsTypeDef],
    },
)
ActionRemoteIpDetailsTypeDef = TypedDict(
    "ActionRemoteIpDetailsTypeDef",
    {
        "IpAddressV4": NotRequired[str],
        "Organization": NotRequired[IpOrganizationDetailsTypeDef],
        "Country": NotRequired[CountryTypeDef],
        "City": NotRequired[CityTypeDef],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
    },
)
CvssPaginatorTypeDef = TypedDict(
    "CvssPaginatorTypeDef",
    {
        "Version": NotRequired[str],
        "BaseScore": NotRequired[float],
        "BaseVector": NotRequired[str],
        "Source": NotRequired[str],
        "Adjustments": NotRequired[List[AdjustmentTypeDef]],
    },
)
CvssTypeDef = TypedDict(
    "CvssTypeDef",
    {
        "Version": NotRequired[str],
        "BaseScore": NotRequired[float],
        "BaseVector": NotRequired[str],
        "Source": NotRequired[str],
        "Adjustments": NotRequired[Sequence[AdjustmentTypeDef]],
    },
)
ListConfigurationPolicyAssociationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationPolicyAssociationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[AssociationFiltersTypeDef],
    },
)
AssociationSetDetailsTypeDef = TypedDict(
    "AssociationSetDetailsTypeDef",
    {
        "AssociationState": NotRequired[AssociationStateDetailsTypeDef],
        "GatewayId": NotRequired[str],
        "Main": NotRequired[bool],
        "RouteTableAssociationId": NotRequired[str],
        "RouteTableId": NotRequired[str],
        "SubnetId": NotRequired[str],
    },
)
AutomationRulesFindingFieldsUpdateTypeDef = TypedDict(
    "AutomationRulesFindingFieldsUpdateTypeDef",
    {
        "Note": NotRequired[NoteUpdateTypeDef],
        "Severity": NotRequired[SeverityUpdateTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Types": NotRequired[List[str]],
        "UserDefinedFields": NotRequired[Dict[str, str]],
        "Workflow": NotRequired[WorkflowUpdateTypeDef],
        "RelatedFindings": NotRequired[List[RelatedFindingTypeDef]],
    },
)
AwsAmazonMqBrokerLogsDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerLogsDetailsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
        "AuditLogGroup": NotRequired[str],
        "GeneralLogGroup": NotRequired[str],
        "Pending": NotRequired[AwsAmazonMqBrokerLogsPendingDetailsTypeDef],
    },
)
AwsApiGatewayRestApiDetailsPaginatorTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsPaginatorTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Version": NotRequired[str],
        "BinaryMediaTypes": NotRequired[List[str]],
        "MinimumCompressionSize": NotRequired[int],
        "ApiKeySource": NotRequired[str],
        "EndpointConfiguration": NotRequired[AwsApiGatewayEndpointConfigurationPaginatorTypeDef],
    },
)
AwsApiGatewayRestApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayRestApiDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Version": NotRequired[str],
        "BinaryMediaTypes": NotRequired[Sequence[str]],
        "MinimumCompressionSize": NotRequired[int],
        "ApiKeySource": NotRequired[str],
        "EndpointConfiguration": NotRequired[AwsApiGatewayEndpointConfigurationTypeDef],
    },
)
AwsApiGatewayStageDetailsPaginatorTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsPaginatorTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "ClientCertificateId": NotRequired[str],
        "StageName": NotRequired[str],
        "Description": NotRequired[str],
        "CacheClusterEnabled": NotRequired[bool],
        "CacheClusterSize": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "MethodSettings": NotRequired[List[AwsApiGatewayMethodSettingsTypeDef]],
        "Variables": NotRequired[Dict[str, str]],
        "DocumentationVersion": NotRequired[str],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "CanarySettings": NotRequired[AwsApiGatewayCanarySettingsPaginatorTypeDef],
        "TracingEnabled": NotRequired[bool],
        "CreatedDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "WebAclArn": NotRequired[str],
    },
)
AwsApiGatewayStageDetailsTypeDef = TypedDict(
    "AwsApiGatewayStageDetailsTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "ClientCertificateId": NotRequired[str],
        "StageName": NotRequired[str],
        "Description": NotRequired[str],
        "CacheClusterEnabled": NotRequired[bool],
        "CacheClusterSize": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "MethodSettings": NotRequired[Sequence[AwsApiGatewayMethodSettingsTypeDef]],
        "Variables": NotRequired[Mapping[str, str]],
        "DocumentationVersion": NotRequired[str],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "CanarySettings": NotRequired[AwsApiGatewayCanarySettingsTypeDef],
        "TracingEnabled": NotRequired[bool],
        "CreatedDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "WebAclArn": NotRequired[str],
    },
)
AwsApiGatewayV2ApiDetailsPaginatorTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsPaginatorTypeDef",
    {
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKeySelectionExpression": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "Version": NotRequired[str],
        "Name": NotRequired[str],
        "ProtocolType": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[AwsCorsConfigurationPaginatorTypeDef],
    },
)
AwsApiGatewayV2ApiDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2ApiDetailsTypeDef",
    {
        "ApiEndpoint": NotRequired[str],
        "ApiId": NotRequired[str],
        "ApiKeySelectionExpression": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "Version": NotRequired[str],
        "Name": NotRequired[str],
        "ProtocolType": NotRequired[str],
        "RouteSelectionExpression": NotRequired[str],
        "CorsConfiguration": NotRequired[AwsCorsConfigurationTypeDef],
    },
)
AwsApiGatewayV2StageDetailsPaginatorTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsPaginatorTypeDef",
    {
        "ClientCertificateId": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "RouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "StageName": NotRequired[str],
        "StageVariables": NotRequired[Dict[str, str]],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "AutoDeploy": NotRequired[bool],
        "LastDeploymentStatusMessage": NotRequired[str],
        "ApiGatewayManaged": NotRequired[bool],
    },
)
AwsApiGatewayV2StageDetailsTypeDef = TypedDict(
    "AwsApiGatewayV2StageDetailsTypeDef",
    {
        "ClientCertificateId": NotRequired[str],
        "CreatedDate": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "DeploymentId": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "RouteSettings": NotRequired[AwsApiGatewayV2RouteSettingsTypeDef],
        "StageName": NotRequired[str],
        "StageVariables": NotRequired[Mapping[str, str]],
        "AccessLogSettings": NotRequired[AwsApiGatewayAccessLogSettingsTypeDef],
        "AutoDeploy": NotRequired[bool],
        "LastDeploymentStatusMessage": NotRequired[str],
        "ApiGatewayManaged": NotRequired[bool],
    },
)
AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef",
    {
        "AuthenticationType": NotRequired[str],
        "LambdaAuthorizerConfig": NotRequired[
            AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef
        ],
        "OpenIdConnectConfig": NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef],
        "UserPoolConfig": NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef],
    },
)
AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef",
    {
        "EncryptionConfiguration": NotRequired[
            AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsPaginatorTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsPaginatorTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "Overrides": NotRequired[
            List[
                AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
            ]
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "Overrides": NotRequired[
            Sequence[
                AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef
            ]
        ],
    },
)
AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef],
        "NoDevice": NotRequired[bool],
        "VirtualName": NotRequired[str],
    },
)
AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef",
    {
        "DestinationBackupVaultArn": NotRequired[str],
        "Lifecycle": NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef],
    },
)
AwsBackupBackupVaultDetailsPaginatorTypeDef = TypedDict(
    "AwsBackupBackupVaultDetailsPaginatorTypeDef",
    {
        "BackupVaultArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "Notifications": NotRequired[AwsBackupBackupVaultNotificationsDetailsPaginatorTypeDef],
        "AccessPolicy": NotRequired[str],
    },
)
AwsBackupBackupVaultDetailsTypeDef = TypedDict(
    "AwsBackupBackupVaultDetailsTypeDef",
    {
        "BackupVaultArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "Notifications": NotRequired[AwsBackupBackupVaultNotificationsDetailsTypeDef],
        "AccessPolicy": NotRequired[str],
    },
)
AwsBackupRecoveryPointDetailsTypeDef = TypedDict(
    "AwsBackupRecoveryPointDetailsTypeDef",
    {
        "BackupSizeInBytes": NotRequired[int],
        "BackupVaultArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "CalculatedLifecycle": NotRequired[AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef],
        "CompletionDate": NotRequired[str],
        "CreatedBy": NotRequired[AwsBackupRecoveryPointCreatedByDetailsTypeDef],
        "CreationDate": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
        "IsEncrypted": NotRequired[bool],
        "LastRestoreTime": NotRequired[str],
        "Lifecycle": NotRequired[AwsBackupRecoveryPointLifecycleDetailsTypeDef],
        "RecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "SourceBackupVaultArn": NotRequired[str],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "StorageClass": NotRequired[str],
    },
)
AwsCertificateManagerCertificateDomainValidationOptionPaginatorTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionPaginatorTypeDef",
    {
        "DomainName": NotRequired[str],
        "ResourceRecord": NotRequired[AwsCertificateManagerCertificateResourceRecordTypeDef],
        "ValidationDomain": NotRequired[str],
        "ValidationEmails": NotRequired[List[str]],
        "ValidationMethod": NotRequired[str],
        "ValidationStatus": NotRequired[str],
    },
)
AwsCertificateManagerCertificateDomainValidationOptionTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    {
        "DomainName": NotRequired[str],
        "ResourceRecord": NotRequired[AwsCertificateManagerCertificateResourceRecordTypeDef],
        "ValidationDomain": NotRequired[str],
        "ValidationEmails": NotRequired[Sequence[str]],
        "ValidationMethod": NotRequired[str],
        "ValidationStatus": NotRequired[str],
    },
)
AwsCloudFormationStackDetailsPaginatorTypeDef = TypedDict(
    "AwsCloudFormationStackDetailsPaginatorTypeDef",
    {
        "Capabilities": NotRequired[List[str]],
        "CreationTime": NotRequired[str],
        "Description": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "DriftInformation": NotRequired[AwsCloudFormationStackDriftInformationDetailsTypeDef],
        "EnableTerminationProtection": NotRequired[bool],
        "LastUpdatedTime": NotRequired[str],
        "NotificationArns": NotRequired[List[str]],
        "Outputs": NotRequired[List[AwsCloudFormationStackOutputsDetailsTypeDef]],
        "RoleArn": NotRequired[str],
        "StackId": NotRequired[str],
        "StackName": NotRequired[str],
        "StackStatus": NotRequired[str],
        "StackStatusReason": NotRequired[str],
        "TimeoutInMinutes": NotRequired[int],
    },
)
AwsCloudFormationStackDetailsTypeDef = TypedDict(
    "AwsCloudFormationStackDetailsTypeDef",
    {
        "Capabilities": NotRequired[Sequence[str]],
        "CreationTime": NotRequired[str],
        "Description": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "DriftInformation": NotRequired[AwsCloudFormationStackDriftInformationDetailsTypeDef],
        "EnableTerminationProtection": NotRequired[bool],
        "LastUpdatedTime": NotRequired[str],
        "NotificationArns": NotRequired[Sequence[str]],
        "Outputs": NotRequired[Sequence[AwsCloudFormationStackOutputsDetailsTypeDef]],
        "RoleArn": NotRequired[str],
        "StackId": NotRequired[str],
        "StackName": NotRequired[str],
        "StackStatus": NotRequired[str],
        "StackStatusReason": NotRequired[str],
        "TimeoutInMinutes": NotRequired[int],
    },
)
AwsCloudFrontDistributionCacheBehaviorsPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsPaginatorTypeDef",
    {
        "Items": NotRequired[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]],
    },
)
AwsCloudFrontDistributionCacheBehaviorsTypeDef = TypedDict(
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    {
        "Items": NotRequired[Sequence[AwsCloudFrontDistributionCacheBehaviorTypeDef]],
    },
)
AwsCloudFrontDistributionOriginCustomOriginConfigPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginCustomOriginConfigPaginatorTypeDef",
    {
        "HttpPort": NotRequired[int],
        "HttpsPort": NotRequired[int],
        "OriginKeepaliveTimeout": NotRequired[int],
        "OriginProtocolPolicy": NotRequired[str],
        "OriginReadTimeout": NotRequired[int],
        "OriginSslProtocols": NotRequired[
            AwsCloudFrontDistributionOriginSslProtocolsPaginatorTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef",
    {
        "HttpPort": NotRequired[int],
        "HttpsPort": NotRequired[int],
        "OriginKeepaliveTimeout": NotRequired[int],
        "OriginProtocolPolicy": NotRequired[str],
        "OriginReadTimeout": NotRequired[int],
        "OriginSslProtocols": NotRequired[AwsCloudFrontDistributionOriginSslProtocolsTypeDef],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverPaginatorTypeDef",
    {
        "StatusCodes": NotRequired[
            AwsCloudFrontDistributionOriginGroupFailoverStatusCodesPaginatorTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginGroupFailoverTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    {
        "StatusCodes": NotRequired[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef],
    },
)
AwsCloudWatchAlarmDetailsPaginatorTypeDef = TypedDict(
    "AwsCloudWatchAlarmDetailsPaginatorTypeDef",
    {
        "ActionsEnabled": NotRequired[bool],
        "AlarmActions": NotRequired[List[str]],
        "AlarmArn": NotRequired[str],
        "AlarmConfigurationUpdatedTimestamp": NotRequired[str],
        "AlarmDescription": NotRequired[str],
        "AlarmName": NotRequired[str],
        "ComparisonOperator": NotRequired[str],
        "DatapointsToAlarm": NotRequired[int],
        "Dimensions": NotRequired[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "EvaluationPeriods": NotRequired[int],
        "ExtendedStatistic": NotRequired[str],
        "InsufficientDataActions": NotRequired[List[str]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "OkActions": NotRequired[List[str]],
        "Period": NotRequired[int],
        "Statistic": NotRequired[str],
        "Threshold": NotRequired[float],
        "ThresholdMetricId": NotRequired[str],
        "TreatMissingData": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
AwsCloudWatchAlarmDetailsTypeDef = TypedDict(
    "AwsCloudWatchAlarmDetailsTypeDef",
    {
        "ActionsEnabled": NotRequired[bool],
        "AlarmActions": NotRequired[Sequence[str]],
        "AlarmArn": NotRequired[str],
        "AlarmConfigurationUpdatedTimestamp": NotRequired[str],
        "AlarmDescription": NotRequired[str],
        "AlarmName": NotRequired[str],
        "ComparisonOperator": NotRequired[str],
        "DatapointsToAlarm": NotRequired[int],
        "Dimensions": NotRequired[Sequence[AwsCloudWatchAlarmDimensionsDetailsTypeDef]],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "EvaluationPeriods": NotRequired[int],
        "ExtendedStatistic": NotRequired[str],
        "InsufficientDataActions": NotRequired[Sequence[str]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "OkActions": NotRequired[Sequence[str]],
        "Period": NotRequired[int],
        "Statistic": NotRequired[str],
        "Threshold": NotRequired[float],
        "ThresholdMetricId": NotRequired[str],
        "TreatMissingData": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentPaginatorTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentPaginatorTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": NotRequired[str],
        "EnvironmentVariables": NotRequired[
            Sequence[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]
        ],
        "PrivilegedMode": NotRequired[bool],
        "ImagePullCredentialsType": NotRequired[str],
        "RegistryCredential": NotRequired[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef],
        "Type": NotRequired[str],
    },
)
AwsCodeBuildProjectLogsConfigDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectLogsConfigDetailsTypeDef",
    {
        "CloudWatchLogs": NotRequired[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef],
        "S3Logs": NotRequired[AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef],
    },
)
AwsDmsReplicationInstanceDetailsPaginatorTypeDef = TypedDict(
    "AwsDmsReplicationInstanceDetailsPaginatorTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ReplicationInstanceClass": NotRequired[str],
        "ReplicationInstanceIdentifier": NotRequired[str],
        "ReplicationSubnetGroup": NotRequired[
            AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef
        ],
        "VpcSecurityGroups": NotRequired[
            List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]
        ],
    },
)
AwsDmsReplicationInstanceDetailsTypeDef = TypedDict(
    "AwsDmsReplicationInstanceDetailsTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ReplicationInstanceClass": NotRequired[str],
        "ReplicationInstanceIdentifier": NotRequired[str],
        "ReplicationSubnetGroup": NotRequired[
            AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef
        ],
        "VpcSecurityGroups": NotRequired[
            Sequence[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]
        ],
    },
)
AwsDynamoDbTableGlobalSecondaryIndexPaginatorTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexPaginatorTypeDef",
    {
        "Backfilling": NotRequired[bool],
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "IndexSizeBytes": NotRequired[int],
        "IndexStatus": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionPaginatorTypeDef],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
    },
)
AwsDynamoDbTableLocalSecondaryIndexPaginatorTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexPaginatorTypeDef",
    {
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionPaginatorTypeDef],
    },
)
AwsDynamoDbTableGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    {
        "Backfilling": NotRequired[bool],
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "IndexSizeBytes": NotRequired[int],
        "IndexStatus": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionTypeDef],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
    },
)
AwsDynamoDbTableLocalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    {
        "IndexArn": NotRequired[str],
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]],
        "Projection": NotRequired[AwsDynamoDbTableProjectionTypeDef],
    },
)
AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
    },
)
AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ActiveDirectory": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef
        ],
        "MutualAuthentication": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef
        ],
        "FederatedAuthentication": NotRequired[
            AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef
        ],
    },
)
AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LambdaFunctionArn": NotRequired[str],
        "Status": NotRequired[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef],
    },
)
AwsEc2InstanceDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2InstanceDetailsPaginatorTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[List[str]],
        "IpV6Addresses": NotRequired[List[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]],
        "VirtualizationType": NotRequired[str],
        "MetadataOptions": NotRequired[AwsEc2InstanceMetadataOptionsTypeDef],
        "Monitoring": NotRequired[AwsEc2InstanceMonitoringDetailsTypeDef],
    },
)
AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": NotRequired[str],
        "ImageId": NotRequired[str],
        "IpV4Addresses": NotRequired[Sequence[str]],
        "IpV6Addresses": NotRequired[Sequence[str]],
        "KeyName": NotRequired[str],
        "IamInstanceProfileArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "NetworkInterfaces": NotRequired[Sequence[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]],
        "VirtualizationType": NotRequired[str],
        "MetadataOptions": NotRequired[AwsEc2InstanceMetadataOptionsTypeDef],
        "Monitoring": NotRequired[AwsEc2InstanceMonitoringDetailsTypeDef],
    },
)
AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef",
    {
        "DeviceName": NotRequired[str],
        "Ebs": NotRequired[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef",
    {
        "CapacityReservationPreference": NotRequired[str],
        "CapacityReservationTarget": NotRequired[
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef",
    {
        "MarketType": NotRequired[str],
        "SpotOptions": NotRequired[
            AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsPaginatorTypeDef",
    {
        "AcceleratorCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
        ],
        "AcceleratorManufacturers": NotRequired[List[str]],
        "AcceleratorNames": NotRequired[List[str]],
        "AcceleratorTotalMemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
        ],
        "AcceleratorTypes": NotRequired[List[str]],
        "BareMetal": NotRequired[str],
        "BaselineEbsBandwidthMbps": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
        ],
        "BurstablePerformance": NotRequired[str],
        "CpuManufacturers": NotRequired[List[str]],
        "ExcludedInstanceTypes": NotRequired[List[str]],
        "InstanceGenerations": NotRequired[List[str]],
        "LocalStorage": NotRequired[str],
        "LocalStorageTypes": NotRequired[List[str]],
        "MemoryGiBPerVCpu": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
        ],
        "MemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef
        ],
        "NetworkInterfaceCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
        ],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "RequireHibernateSupport": NotRequired[bool],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "TotalLocalStorageGB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
        ],
        "VCpuCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef",
    {
        "AcceleratorCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef
        ],
        "AcceleratorManufacturers": NotRequired[Sequence[str]],
        "AcceleratorNames": NotRequired[Sequence[str]],
        "AcceleratorTotalMemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef
        ],
        "AcceleratorTypes": NotRequired[Sequence[str]],
        "BareMetal": NotRequired[str],
        "BaselineEbsBandwidthMbps": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef
        ],
        "BurstablePerformance": NotRequired[str],
        "CpuManufacturers": NotRequired[Sequence[str]],
        "ExcludedInstanceTypes": NotRequired[Sequence[str]],
        "InstanceGenerations": NotRequired[Sequence[str]],
        "LocalStorage": NotRequired[str],
        "LocalStorageTypes": NotRequired[Sequence[str]],
        "MemoryGiBPerVCpu": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef
        ],
        "MemoryMiB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef
        ],
        "NetworkInterfaceCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef
        ],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "RequireHibernateSupport": NotRequired[bool],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "TotalLocalStorageGB": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef
        ],
        "VCpuCount": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsPaginatorTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[List[str]],
        "InterfaceType": NotRequired[str],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]
        ],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]
        ],
        "Ipv6PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]
        ],
        "NetworkCardIndex": NotRequired[int],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]
        ],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef",
    {
        "AssociateCarrierIpAddress": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "DeleteOnTermination": NotRequired[bool],
        "Description": NotRequired[str],
        "DeviceIndex": NotRequired[int],
        "Groups": NotRequired[Sequence[str]],
        "InterfaceType": NotRequired[str],
        "Ipv4PrefixCount": NotRequired[int],
        "Ipv4Prefixes": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]
        ],
        "Ipv6AddressCount": NotRequired[int],
        "Ipv6Addresses": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]
        ],
        "Ipv6PrefixCount": NotRequired[int],
        "Ipv6Prefixes": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]
        ],
        "NetworkCardIndex": NotRequired[int],
        "NetworkInterfaceId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "PrivateIpAddresses": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]
        ],
        "SecondaryPrivateIpAddressCount": NotRequired[int],
        "SubnetId": NotRequired[str],
    },
)
AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "Egress": NotRequired[bool],
        "IcmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
        "Ipv6CidrBlock": NotRequired[str],
        "PortRange": NotRequired[PortRangeFromToTypeDef],
        "Protocol": NotRequired[str],
        "RuleAction": NotRequired[str],
        "RuleNumber": NotRequired[int],
    },
)
AwsEc2NetworkInterfaceDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsPaginatorTypeDef",
    {
        "Attachment": NotRequired[AwsEc2NetworkInterfaceAttachmentTypeDef],
        "NetworkInterfaceId": NotRequired[str],
        "SecurityGroups": NotRequired[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]],
        "SourceDestCheck": NotRequired[bool],
        "IpV6Addresses": NotRequired[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]],
        "PrivateIpAddresses": NotRequired[
            List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]
        ],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)
AwsEc2NetworkInterfaceDetailsTypeDef = TypedDict(
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    {
        "Attachment": NotRequired[AwsEc2NetworkInterfaceAttachmentTypeDef],
        "NetworkInterfaceId": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[AwsEc2NetworkInterfaceSecurityGroupTypeDef]],
        "SourceDestCheck": NotRequired[bool],
        "IpV6Addresses": NotRequired[Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]],
        "PrivateIpAddresses": NotRequired[
            Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]
        ],
        "PublicDnsName": NotRequired[str],
        "PublicIp": NotRequired[str],
    },
)
AwsEc2SecurityGroupIpPermissionPaginatorTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionPaginatorTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]],
        "IpRanges": NotRequired[List[AwsEc2SecurityGroupIpRangeTypeDef]],
        "Ipv6Ranges": NotRequired[List[AwsEc2SecurityGroupIpv6RangeTypeDef]],
        "PrefixListIds": NotRequired[List[AwsEc2SecurityGroupPrefixListIdTypeDef]],
    },
)
AwsEc2SecurityGroupIpPermissionTypeDef = TypedDict(
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    {
        "IpProtocol": NotRequired[str],
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "UserIdGroupPairs": NotRequired[Sequence[AwsEc2SecurityGroupUserIdGroupPairTypeDef]],
        "IpRanges": NotRequired[Sequence[AwsEc2SecurityGroupIpRangeTypeDef]],
        "Ipv6Ranges": NotRequired[Sequence[AwsEc2SecurityGroupIpv6RangeTypeDef]],
        "PrefixListIds": NotRequired[Sequence[AwsEc2SecurityGroupPrefixListIdTypeDef]],
    },
)
AwsEc2SubnetDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2SubnetDetailsPaginatorTypeDef",
    {
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "SubnetArn": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Ipv6CidrBlockAssociationSet": NotRequired[List[Ipv6CidrBlockAssociationTypeDef]],
    },
)
AwsEc2SubnetDetailsTypeDef = TypedDict(
    "AwsEc2SubnetDetailsTypeDef",
    {
        "AssignIpv6AddressOnCreation": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailableIpAddressCount": NotRequired[int],
        "CidrBlock": NotRequired[str],
        "DefaultForAz": NotRequired[bool],
        "MapPublicIpOnLaunch": NotRequired[bool],
        "OwnerId": NotRequired[str],
        "State": NotRequired[str],
        "SubnetArn": NotRequired[str],
        "SubnetId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Ipv6CidrBlockAssociationSet": NotRequired[Sequence[Ipv6CidrBlockAssociationTypeDef]],
    },
)
AwsEc2VolumeDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VolumeDetailsPaginatorTypeDef",
    {
        "CreateTime": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Attachments": NotRequired[List[AwsEc2VolumeAttachmentTypeDef]],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeScanStatus": NotRequired[str],
    },
)
AwsEc2VolumeDetailsTypeDef = TypedDict(
    "AwsEc2VolumeDetailsTypeDef",
    {
        "CreateTime": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Size": NotRequired[int],
        "SnapshotId": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Attachments": NotRequired[Sequence[AwsEc2VolumeAttachmentTypeDef]],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeScanStatus": NotRequired[str],
    },
)
AwsEc2VpcDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpcDetailsPaginatorTypeDef",
    {
        "CidrBlockAssociationSet": NotRequired[List[CidrBlockAssociationTypeDef]],
        "Ipv6CidrBlockAssociationSet": NotRequired[List[Ipv6CidrBlockAssociationTypeDef]],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[str],
    },
)
AwsEc2VpcDetailsTypeDef = TypedDict(
    "AwsEc2VpcDetailsTypeDef",
    {
        "CidrBlockAssociationSet": NotRequired[Sequence[CidrBlockAssociationTypeDef]],
        "Ipv6CidrBlockAssociationSet": NotRequired[Sequence[Ipv6CidrBlockAssociationTypeDef]],
        "DhcpOptionsId": NotRequired[str],
        "State": NotRequired[str],
    },
)
AwsEc2VpcEndpointServiceDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsPaginatorTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[List[str]],
        "BaseEndpointDnsNames": NotRequired[List[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[List[str]],
        "NetworkLoadBalancerArns": NotRequired[List[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]],
    },
)
AwsEc2VpcEndpointServiceDetailsTypeDef = TypedDict(
    "AwsEc2VpcEndpointServiceDetailsTypeDef",
    {
        "AcceptanceRequired": NotRequired[bool],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BaseEndpointDnsNames": NotRequired[Sequence[str]],
        "ManagesVpcEndpoints": NotRequired[bool],
        "GatewayLoadBalancerArns": NotRequired[Sequence[str]],
        "NetworkLoadBalancerArns": NotRequired[Sequence[str]],
        "PrivateDnsName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceState": NotRequired[str],
        "ServiceType": NotRequired[Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]],
    },
)
AwsEc2VpcPeeringConnectionVpcInfoDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsPaginatorTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "CidrBlockSet": NotRequired[List[VpcInfoCidrBlockSetDetailsTypeDef]],
        "Ipv6CidrBlockSet": NotRequired[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PeeringOptions": NotRequired[VpcInfoPeeringOptionsDetailsTypeDef],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef",
    {
        "CidrBlock": NotRequired[str],
        "CidrBlockSet": NotRequired[Sequence[VpcInfoCidrBlockSetDetailsTypeDef]],
        "Ipv6CidrBlockSet": NotRequired[Sequence[VpcInfoIpv6CidrBlockSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PeeringOptions": NotRequired[VpcInfoPeeringOptionsDetailsTypeDef],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsEc2VpnConnectionOptionsDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsPaginatorTypeDef",
    {
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelOptions": NotRequired[
            List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsPaginatorTypeDef]
        ],
    },
)
AwsEc2VpnConnectionOptionsDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionOptionsDetailsTypeDef",
    {
        "StaticRoutesOnly": NotRequired[bool],
        "TunnelOptions": NotRequired[
            Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef]
        ],
    },
)
AwsEcrRepositoryDetailsTypeDef = TypedDict(
    "AwsEcrRepositoryDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "ImageScanningConfiguration": NotRequired[
            AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef
        ],
        "ImageTagMutability": NotRequired[str],
        "LifecyclePolicy": NotRequired[AwsEcrRepositoryLifecyclePolicyDetailsTypeDef],
        "RepositoryName": NotRequired[str],
        "RepositoryPolicyText": NotRequired[str],
    },
)
AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef",
    {
        "KmsKeyId": NotRequired[str],
        "LogConfiguration": NotRequired[
            AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef
        ],
        "Logging": NotRequired[str],
    },
)
AwsEcsContainerDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsContainerDetailsPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "Image": NotRequired[str],
        "MountPoints": NotRequired[List[AwsMountPointTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
AwsEcsContainerDetailsTypeDef = TypedDict(
    "AwsEcsContainerDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Image": NotRequired[str],
        "MountPoints": NotRequired[Sequence[AwsMountPointTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
AwsEcsServiceDeploymentConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceDeploymentConfigurationDetailsTypeDef",
    {
        "DeploymentCircuitBreaker": NotRequired[
            AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef
        ],
        "MaximumPercent": NotRequired[int],
        "MinimumHealthyPercent": NotRequired[int],
    },
)
AwsEcsServiceNetworkConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsPaginatorTypeDef",
    {
        "AwsVpcConfiguration": NotRequired[
            AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsPaginatorTypeDef
        ],
    },
)
AwsEcsServiceNetworkConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsServiceNetworkConfigurationDetailsTypeDef",
    {
        "AwsVpcConfiguration": NotRequired[
            AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsPaginatorTypeDef",
    {
        "Capabilities": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsPaginatorTypeDef
        ],
        "Devices": NotRequired[
            List[
                AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsPaginatorTypeDef
            ]
        ],
        "InitProcessEnabled": NotRequired[bool],
        "MaxSwap": NotRequired[int],
        "SharedMemorySize": NotRequired[int],
        "Swappiness": NotRequired[int],
        "Tmpfs": NotRequired[
            List[
                AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsPaginatorTypeDef
            ]
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef",
    {
        "Capabilities": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef
        ],
        "Devices": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef]
        ],
        "InitProcessEnabled": NotRequired[bool],
        "MaxSwap": NotRequired[int],
        "SharedMemorySize": NotRequired[int],
        "Swappiness": NotRequired[int],
        "Tmpfs": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef]
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsPaginatorTypeDef",
    {
        "LogDriver": NotRequired[str],
        "Options": NotRequired[Dict[str, str]],
        "SecretOptions": NotRequired[
            List[
                AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef
            ]
        ],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef",
    {
        "LogDriver": NotRequired[str],
        "Options": NotRequired[Mapping[str, str]],
        "SecretOptions": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef
            ]
        ],
    },
)
AwsEcsTaskDefinitionProxyConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsPaginatorTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]
        ],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef",
    {
        "ContainerName": NotRequired[str],
        "ProxyConfigurationProperties": NotRequired[
            Sequence[
                AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef
            ]
        ],
        "Type": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef",
    {
        "AuthorizationConfig": NotRequired[
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef
        ],
        "FilesystemId": NotRequired[str],
        "RootDirectory": NotRequired[str],
        "TransitEncryption": NotRequired[str],
        "TransitEncryptionPort": NotRequired[int],
    },
)
AwsEcsTaskVolumeDetailsTypeDef = TypedDict(
    "AwsEcsTaskVolumeDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Host": NotRequired[AwsEcsTaskVolumeHostDetailsTypeDef],
    },
)
AwsEfsAccessPointRootDirectoryDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointRootDirectoryDetailsTypeDef",
    {
        "CreationInfo": NotRequired[AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef],
        "Path": NotRequired[str],
    },
)
AwsEksClusterLoggingDetailsPaginatorTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsPaginatorTypeDef",
    {
        "ClusterLogging": NotRequired[
            List[AwsEksClusterLoggingClusterLoggingDetailsPaginatorTypeDef]
        ],
    },
)
AwsEksClusterLoggingDetailsTypeDef = TypedDict(
    "AwsEksClusterLoggingDetailsTypeDef",
    {
        "ClusterLogging": NotRequired[Sequence[AwsEksClusterLoggingClusterLoggingDetailsTypeDef]],
    },
)
AwsElasticBeanstalkEnvironmentDetailsPaginatorTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsPaginatorTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "Cname": NotRequired[str],
        "DateCreated": NotRequired[str],
        "DateUpdated": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EnvironmentArn": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentLinks": NotRequired[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]],
        "EnvironmentName": NotRequired[str],
        "OptionSettings": NotRequired[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]],
        "PlatformArn": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "Status": NotRequired[str],
        "Tier": NotRequired[AwsElasticBeanstalkEnvironmentTierTypeDef],
        "VersionLabel": NotRequired[str],
    },
)
AwsElasticBeanstalkEnvironmentDetailsTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "Cname": NotRequired[str],
        "DateCreated": NotRequired[str],
        "DateUpdated": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EnvironmentArn": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentLinks": NotRequired[
            Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]
        ],
        "EnvironmentName": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]],
        "PlatformArn": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "Status": NotRequired[str],
        "Tier": NotRequired[AwsElasticBeanstalkEnvironmentTierTypeDef],
        "VersionLabel": NotRequired[str],
    },
)
AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef",
    {
        "DedicatedMasterCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "DedicatedMasterType": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "ZoneAwarenessConfig": NotRequired[
            AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef
        ],
        "ZoneAwarenessEnabled": NotRequired[bool],
    },
)
AwsElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "AwsElasticsearchDomainLogPublishingOptionsTypeDef",
    {
        "IndexSlowLogs": NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef],
        "SearchSlowLogs": NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef],
        "AuditLogs": NotRequired[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef],
    },
)
AwsElbLoadBalancerPoliciesPaginatorTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesPaginatorTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[List[AwsElbAppCookieStickinessPolicyTypeDef]],
        "LbCookieStickinessPolicies": NotRequired[List[AwsElbLbCookieStickinessPolicyTypeDef]],
        "OtherPolicies": NotRequired[List[str]],
    },
)
AwsElbLoadBalancerPoliciesTypeDef = TypedDict(
    "AwsElbLoadBalancerPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": NotRequired[
            Sequence[AwsElbAppCookieStickinessPolicyTypeDef]
        ],
        "LbCookieStickinessPolicies": NotRequired[Sequence[AwsElbLbCookieStickinessPolicyTypeDef]],
        "OtherPolicies": NotRequired[Sequence[str]],
    },
)
AwsElbLoadBalancerAttributesPaginatorTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesPaginatorTypeDef",
    {
        "AccessLog": NotRequired[AwsElbLoadBalancerAccessLogTypeDef],
        "ConnectionDraining": NotRequired[AwsElbLoadBalancerConnectionDrainingTypeDef],
        "ConnectionSettings": NotRequired[AwsElbLoadBalancerConnectionSettingsTypeDef],
        "CrossZoneLoadBalancing": NotRequired[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef],
        "AdditionalAttributes": NotRequired[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]],
    },
)
AwsElbLoadBalancerAttributesTypeDef = TypedDict(
    "AwsElbLoadBalancerAttributesTypeDef",
    {
        "AccessLog": NotRequired[AwsElbLoadBalancerAccessLogTypeDef],
        "ConnectionDraining": NotRequired[AwsElbLoadBalancerConnectionDrainingTypeDef],
        "ConnectionSettings": NotRequired[AwsElbLoadBalancerConnectionSettingsTypeDef],
        "CrossZoneLoadBalancing": NotRequired[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef],
        "AdditionalAttributes": NotRequired[Sequence[AwsElbLoadBalancerAdditionalAttributeTypeDef]],
    },
)
AwsElbLoadBalancerListenerDescriptionPaginatorTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionPaginatorTypeDef",
    {
        "Listener": NotRequired[AwsElbLoadBalancerListenerTypeDef],
        "PolicyNames": NotRequired[List[str]],
    },
)
AwsElbLoadBalancerListenerDescriptionTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    {
        "Listener": NotRequired[AwsElbLoadBalancerListenerTypeDef],
        "PolicyNames": NotRequired[Sequence[str]],
    },
)
AwsElbv2LoadBalancerDetailsPaginatorTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsPaginatorTypeDef",
    {
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[List[AwsElbv2LoadBalancerAttributeTypeDef]],
    },
)
AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[AvailabilityZoneTypeDef]],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DNSName": NotRequired[str],
        "IpAddressType": NotRequired[str],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[str],
        "VpcId": NotRequired[str],
        "LoadBalancerAttributes": NotRequired[Sequence[AwsElbv2LoadBalancerAttributeTypeDef]],
    },
)
AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef",
    {
        "Primary": NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef],
        "Secondary": NotRequired[
            AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef
        ],
    },
)
AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef",
    {
        "AuditLogs": NotRequired[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef],
    },
)
AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef",
    {
        "EbsVolumes": NotRequired[
            AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef
        ],
    },
)
AwsIamAccessKeySessionContextTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextTypeDef",
    {
        "Attributes": NotRequired[AwsIamAccessKeySessionContextAttributesTypeDef],
        "SessionIssuer": NotRequired[AwsIamAccessKeySessionContextSessionIssuerTypeDef],
    },
)
AwsIamGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsIamGroupDetailsPaginatorTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupPolicyList": NotRequired[List[AwsIamGroupPolicyTypeDef]],
        "Path": NotRequired[str],
    },
)
AwsIamGroupDetailsTypeDef = TypedDict(
    "AwsIamGroupDetailsTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupPolicyList": NotRequired[Sequence[AwsIamGroupPolicyTypeDef]],
        "Path": NotRequired[str],
    },
)
AwsIamInstanceProfilePaginatorTypeDef = TypedDict(
    "AwsIamInstanceProfilePaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[str],
        "InstanceProfileId": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Path": NotRequired[str],
        "Roles": NotRequired[List[AwsIamInstanceProfileRoleTypeDef]],
    },
)
AwsIamInstanceProfileTypeDef = TypedDict(
    "AwsIamInstanceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[str],
        "InstanceProfileId": NotRequired[str],
        "InstanceProfileName": NotRequired[str],
        "Path": NotRequired[str],
        "Roles": NotRequired[Sequence[AwsIamInstanceProfileRoleTypeDef]],
    },
)
AwsIamPolicyDetailsPaginatorTypeDef = TypedDict(
    "AwsIamPolicyDetailsPaginatorTypeDef",
    {
        "AttachmentCount": NotRequired[int],
        "CreateDate": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "Description": NotRequired[str],
        "IsAttachable": NotRequired[bool],
        "Path": NotRequired[str],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyVersionList": NotRequired[List[AwsIamPolicyVersionTypeDef]],
        "UpdateDate": NotRequired[str],
    },
)
AwsIamPolicyDetailsTypeDef = TypedDict(
    "AwsIamPolicyDetailsTypeDef",
    {
        "AttachmentCount": NotRequired[int],
        "CreateDate": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "Description": NotRequired[str],
        "IsAttachable": NotRequired[bool],
        "Path": NotRequired[str],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "PolicyId": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyVersionList": NotRequired[Sequence[AwsIamPolicyVersionTypeDef]],
        "UpdateDate": NotRequired[str],
    },
)
AwsIamUserDetailsPaginatorTypeDef = TypedDict(
    "AwsIamUserDetailsPaginatorTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupList": NotRequired[List[str]],
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserPolicyList": NotRequired[List[AwsIamUserPolicyTypeDef]],
    },
)
AwsIamUserDetailsTypeDef = TypedDict(
    "AwsIamUserDetailsTypeDef",
    {
        "AttachedManagedPolicies": NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "GroupList": NotRequired[Sequence[str]],
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "UserPolicyList": NotRequired[Sequence[AwsIamUserPolicyTypeDef]],
    },
)
AwsKinesisStreamDetailsTypeDef = TypedDict(
    "AwsKinesisStreamDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "StreamEncryption": NotRequired[AwsKinesisStreamStreamEncryptionDetailsTypeDef],
        "ShardCount": NotRequired[int],
        "RetentionPeriodHours": NotRequired[int],
    },
)
AwsLambdaFunctionEnvironmentPaginatorTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentPaginatorTypeDef",
    {
        "Variables": NotRequired[Dict[str, str]],
        "Error": NotRequired[AwsLambdaFunctionEnvironmentErrorTypeDef],
    },
)
AwsLambdaFunctionEnvironmentTypeDef = TypedDict(
    "AwsLambdaFunctionEnvironmentTypeDef",
    {
        "Variables": NotRequired[Mapping[str, str]],
        "Error": NotRequired[AwsLambdaFunctionEnvironmentErrorTypeDef],
    },
)
AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef",
    {
        "Iam": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef],
        "Scram": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef],
    },
)
AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef",
    {
        "EncryptionInTransit": NotRequired[
            AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef
        ],
        "EncryptionAtRest": NotRequired[
            AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef
        ],
    },
)
AwsNetworkFirewallFirewallDetailsPaginatorTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsPaginatorTypeDef",
    {
        "DeleteProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallId": NotRequired[str],
        "FirewallName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "SubnetMappings": NotRequired[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AwsNetworkFirewallFirewallDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallDetailsTypeDef",
    {
        "DeleteProtection": NotRequired[bool],
        "Description": NotRequired[str],
        "FirewallArn": NotRequired[str],
        "FirewallId": NotRequired[str],
        "FirewallName": NotRequired[str],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyChangeProtection": NotRequired[bool],
        "SubnetChangeProtection": NotRequired[bool],
        "SubnetMappings": NotRequired[
            Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]
        ],
        "VpcId": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "InternalUserDatabaseEnabled": NotRequired[bool],
        "MasterUserOptions": NotRequired[AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef],
    },
)
AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "WarmEnabled": NotRequired[bool],
        "WarmCount": NotRequired[int],
        "DedicatedMasterEnabled": NotRequired[bool],
        "ZoneAwarenessConfig": NotRequired[
            AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef
        ],
        "DedicatedMasterCount": NotRequired[int],
        "InstanceType": NotRequired[str],
        "WarmType": NotRequired[str],
        "ZoneAwarenessEnabled": NotRequired[bool],
        "DedicatedMasterType": NotRequired[str],
    },
)
AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef",
    {
        "IndexSlowLogs": NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef],
        "SearchSlowLogs": NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef],
        "AuditLogs": NotRequired[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef],
    },
)
AwsRdsDbClusterDetailsPaginatorTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsPaginatorTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[List[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "Status": NotRequired[str],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[List[str]],
        "MultiAz": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[List[str]],
        "VpcSecurityGroups": NotRequired[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "AssociatedRoles": NotRequired[List[AwsRdsDbClusterAssociatedRoleTypeDef]],
        "ClusterCreateTime": NotRequired[str],
        "EnabledCloudWatchLogsExports": NotRequired[List[str]],
        "EngineMode": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamStatus": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[List[AwsRdsDbDomainMembershipTypeDef]],
        "DbClusterParameterGroup": NotRequired[str],
        "DbSubnetGroup": NotRequired[str],
        "DbClusterOptionGroupMemberships": NotRequired[
            List[AwsRdsDbClusterOptionGroupMembershipTypeDef]
        ],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterMembers": NotRequired[List[AwsRdsDbClusterMemberTypeDef]],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
    },
)
AwsRdsDbClusterDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterDetailsTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "Status": NotRequired[str],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[Sequence[str]],
        "MultiAz": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[Sequence[str]],
        "VpcSecurityGroups": NotRequired[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "AssociatedRoles": NotRequired[Sequence[AwsRdsDbClusterAssociatedRoleTypeDef]],
        "ClusterCreateTime": NotRequired[str],
        "EnabledCloudWatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamStatus": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[Sequence[AwsRdsDbDomainMembershipTypeDef]],
        "DbClusterParameterGroup": NotRequired[str],
        "DbSubnetGroup": NotRequired[str],
        "DbClusterOptionGroupMemberships": NotRequired[
            Sequence[AwsRdsDbClusterOptionGroupMembershipTypeDef]
        ],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterMembers": NotRequired[Sequence[AwsRdsDbClusterMemberTypeDef]],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
    },
)
AwsRdsDbClusterSnapshotDetailsPaginatorTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsPaginatorTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterSnapshotIdentifier": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "DbClusterSnapshotAttributes": NotRequired[
            List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributePaginatorTypeDef]
        ],
    },
)
AwsRdsDbClusterSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
        "DbClusterSnapshotIdentifier": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "DbClusterSnapshotAttributes": NotRequired[
            Sequence[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef]
        ],
    },
)
AwsRdsDbSnapshotDetailsPaginatorTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsPaginatorTypeDef",
    {
        "DbSnapshotIdentifier": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDbSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]],
        "DbiResourceId": NotRequired[str],
    },
)
AwsRdsDbSnapshotDetailsTypeDef = TypedDict(
    "AwsRdsDbSnapshotDetailsTypeDef",
    {
        "DbSnapshotIdentifier": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[str],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDbSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IamDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]],
        "DbiResourceId": NotRequired[str],
    },
)
AwsRdsDbPendingModifiedValuesPaginatorTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesPaginatorTypeDef",
    {
        "DbInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CaCertificateIdentifier": NotRequired[str],
        "DbSubnetGroupName": NotRequired[str],
        "PendingCloudWatchLogsExports": NotRequired[
            AwsRdsPendingCloudWatchLogsExportsPaginatorTypeDef
        ],
        "ProcessorFeatures": NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]],
    },
)
AwsRdsDbPendingModifiedValuesTypeDef = TypedDict(
    "AwsRdsDbPendingModifiedValuesTypeDef",
    {
        "DbInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DbInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CaCertificateIdentifier": NotRequired[str],
        "DbSubnetGroupName": NotRequired[str],
        "PendingCloudWatchLogsExports": NotRequired[AwsRdsPendingCloudWatchLogsExportsTypeDef],
        "ProcessorFeatures": NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]],
    },
)
AwsRdsDbSecurityGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupDetailsPaginatorTypeDef",
    {
        "DbSecurityGroupArn": NotRequired[str],
        "DbSecurityGroupDescription": NotRequired[str],
        "DbSecurityGroupName": NotRequired[str],
        "Ec2SecurityGroups": NotRequired[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]],
        "IpRanges": NotRequired[List[AwsRdsDbSecurityGroupIpRangeTypeDef]],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsRdsDbSecurityGroupDetailsTypeDef = TypedDict(
    "AwsRdsDbSecurityGroupDetailsTypeDef",
    {
        "DbSecurityGroupArn": NotRequired[str],
        "DbSecurityGroupDescription": NotRequired[str],
        "DbSecurityGroupName": NotRequired[str],
        "Ec2SecurityGroups": NotRequired[Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]],
        "IpRanges": NotRequired[Sequence[AwsRdsDbSecurityGroupIpRangeTypeDef]],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
AwsRdsDbSubnetGroupSubnetTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef],
        "SubnetStatus": NotRequired[str],
    },
)
AwsRedshiftClusterClusterParameterGroupPaginatorTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupPaginatorTypeDef",
    {
        "ClusterParameterStatusList": NotRequired[
            List[AwsRedshiftClusterClusterParameterStatusTypeDef]
        ],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
    },
)
AwsRedshiftClusterClusterParameterGroupTypeDef = TypedDict(
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    {
        "ClusterParameterStatusList": NotRequired[
            Sequence[AwsRedshiftClusterClusterParameterStatusTypeDef]
        ],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
    },
)
AwsRoute53HostedZoneObjectDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneObjectDetailsTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Config": NotRequired[AwsRoute53HostedZoneConfigDetailsTypeDef],
    },
)
AwsRoute53QueryLoggingConfigDetailsTypeDef = TypedDict(
    "AwsRoute53QueryLoggingConfigDetailsTypeDef",
    {
        "CloudWatchLogsLogGroupArn": NotRequired[CloudWatchLogsLogGroupArnConfigDetailsTypeDef],
    },
)
AwsS3AccessPointDetailsTypeDef = TypedDict(
    "AwsS3AccessPointDetailsTypeDef",
    {
        "AccessPointArn": NotRequired[str],
        "Alias": NotRequired[str],
        "Bucket": NotRequired[str],
        "BucketAccountId": NotRequired[str],
        "Name": NotRequired[str],
        "NetworkOrigin": NotRequired[str],
        "PublicAccessBlockConfiguration": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "VpcConfiguration": NotRequired[AwsS3AccessPointVpcConfigurationDetailsTypeDef],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterPaginatorTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterPaginatorTypeDef",
    {
        "FilterRules": NotRequired[
            List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef",
    {
        "FilterRules": NotRequired[
            Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]
        ],
    },
)
AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef",
    {
        "DefaultRetention": NotRequired[
            AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef
        ],
    },
)
AwsS3BucketServerSideEncryptionRuleTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": NotRequired[
            AwsS3BucketServerSideEncryptionByDefaultTypeDef
        ],
    },
)
AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef",
    {
        "Condition": NotRequired[AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef],
        "Redirect": NotRequired[AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef],
    },
)
AwsSageMakerNotebookInstanceDetailsPaginatorTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceDetailsPaginatorTypeDef",
    {
        "AcceleratorTypes": NotRequired[List[str]],
        "AdditionalCodeRepositories": NotRequired[List[str]],
        "DefaultCodeRepository": NotRequired[str],
        "DirectInternetAccess": NotRequired[str],
        "FailureReason": NotRequired[str],
        "InstanceMetadataServiceConfiguration": NotRequired[
            AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NotebookInstanceArn": NotRequired[str],
        "NotebookInstanceLifecycleConfigName": NotRequired[str],
        "NotebookInstanceName": NotRequired[str],
        "NotebookInstanceStatus": NotRequired[str],
        "PlatformIdentifier": NotRequired[str],
        "RoleArn": NotRequired[str],
        "RootAccess": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "SubnetId": NotRequired[str],
        "Url": NotRequired[str],
        "VolumeSizeInGB": NotRequired[int],
    },
)
AwsSageMakerNotebookInstanceDetailsTypeDef = TypedDict(
    "AwsSageMakerNotebookInstanceDetailsTypeDef",
    {
        "AcceleratorTypes": NotRequired[Sequence[str]],
        "AdditionalCodeRepositories": NotRequired[Sequence[str]],
        "DefaultCodeRepository": NotRequired[str],
        "DirectInternetAccess": NotRequired[str],
        "FailureReason": NotRequired[str],
        "InstanceMetadataServiceConfiguration": NotRequired[
            AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NotebookInstanceArn": NotRequired[str],
        "NotebookInstanceLifecycleConfigName": NotRequired[str],
        "NotebookInstanceName": NotRequired[str],
        "NotebookInstanceStatus": NotRequired[str],
        "PlatformIdentifier": NotRequired[str],
        "RoleArn": NotRequired[str],
        "RootAccess": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "Url": NotRequired[str],
        "VolumeSizeInGB": NotRequired[int],
    },
)
AwsSecretsManagerSecretDetailsTypeDef = TypedDict(
    "AwsSecretsManagerSecretDetailsTypeDef",
    {
        "RotationRules": NotRequired[AwsSecretsManagerSecretRotationRulesTypeDef],
        "RotationOccurredWithinFrequency": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "RotationEnabled": NotRequired[bool],
        "RotationLambdaArn": NotRequired[str],
        "Deleted": NotRequired[bool],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
BatchUpdateFindingsRequestRequestTypeDef = TypedDict(
    "BatchUpdateFindingsRequestRequestTypeDef",
    {
        "FindingIdentifiers": Sequence[AwsSecurityFindingIdentifierTypeDef],
        "Note": NotRequired[NoteUpdateTypeDef],
        "Severity": NotRequired[SeverityUpdateTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Types": NotRequired[Sequence[str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Workflow": NotRequired[WorkflowUpdateTypeDef],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
    },
)
BatchUpdateFindingsUnprocessedFindingTypeDef = TypedDict(
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
AwsSnsTopicDetailsPaginatorTypeDef = TypedDict(
    "AwsSnsTopicDetailsPaginatorTypeDef",
    {
        "KmsMasterKeyId": NotRequired[str],
        "Subscription": NotRequired[List[AwsSnsTopicSubscriptionTypeDef]],
        "TopicName": NotRequired[str],
        "Owner": NotRequired[str],
        "SqsSuccessFeedbackRoleArn": NotRequired[str],
        "SqsFailureFeedbackRoleArn": NotRequired[str],
        "ApplicationSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseFailureFeedbackRoleArn": NotRequired[str],
        "HttpSuccessFeedbackRoleArn": NotRequired[str],
        "HttpFailureFeedbackRoleArn": NotRequired[str],
    },
)
AwsSnsTopicDetailsTypeDef = TypedDict(
    "AwsSnsTopicDetailsTypeDef",
    {
        "KmsMasterKeyId": NotRequired[str],
        "Subscription": NotRequired[Sequence[AwsSnsTopicSubscriptionTypeDef]],
        "TopicName": NotRequired[str],
        "Owner": NotRequired[str],
        "SqsSuccessFeedbackRoleArn": NotRequired[str],
        "SqsFailureFeedbackRoleArn": NotRequired[str],
        "ApplicationSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseSuccessFeedbackRoleArn": NotRequired[str],
        "FirehoseFailureFeedbackRoleArn": NotRequired[str],
        "HttpSuccessFeedbackRoleArn": NotRequired[str],
        "HttpFailureFeedbackRoleArn": NotRequired[str],
    },
)
AwsSsmPatchTypeDef = TypedDict(
    "AwsSsmPatchTypeDef",
    {
        "ComplianceSummary": NotRequired[AwsSsmComplianceSummaryTypeDef],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef",
    {
        "CloudWatchLogsLogGroup": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef
        ],
    },
)
AwsWafRateBasedRuleDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsPaginatorTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[List[AwsWafRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRateBasedRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[Sequence[AwsWafRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRegionalRateBasedRuleDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsPaginatorTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRegionalRateBasedRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRateBasedRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RateKey": NotRequired[str],
        "RateLimit": NotRequired[int],
        "RuleId": NotRequired[str],
        "MatchPredicates": NotRequired[Sequence[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]],
    },
)
AwsWafRegionalRuleDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRegionalRuleDetailsPaginatorTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[List[AwsWafRegionalRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRegionalRuleDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[Sequence[AwsWafRegionalRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRegionalRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupRulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRegionalRuleGroupRulesActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafRegionalWebAclRulesListDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclRulesListDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRegionalWebAclRulesListActionDetailsTypeDef],
        "OverrideAction": NotRequired[AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafRuleDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRuleDetailsPaginatorTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[List[AwsWafRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRuleDetailsTypeDef = TypedDict(
    "AwsWafRuleDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "PredicateList": NotRequired[Sequence[AwsWafRulePredicateListDetailsTypeDef]],
        "RuleId": NotRequired[str],
    },
)
AwsWafRuleGroupRulesDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupRulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafRuleGroupRulesActionDetailsTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclRulePaginatorTypeDef = TypedDict(
    "AwsWafWebAclRulePaginatorTypeDef",
    {
        "Action": NotRequired[WafActionTypeDef],
        "ExcludedRules": NotRequired[List[WafExcludedRuleTypeDef]],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": NotRequired[WafActionTypeDef],
        "ExcludedRules": NotRequired[Sequence[WafExcludedRuleTypeDef]],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Priority": NotRequired[int],
        "RuleId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsWafv2CustomRequestHandlingDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2CustomRequestHandlingDetailsPaginatorTypeDef",
    {
        "InsertHeaders": NotRequired[List[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2CustomRequestHandlingDetailsTypeDef = TypedDict(
    "AwsWafv2CustomRequestHandlingDetailsTypeDef",
    {
        "InsertHeaders": NotRequired[Sequence[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2CustomResponseDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2CustomResponseDetailsPaginatorTypeDef",
    {
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseCode": NotRequired[int],
        "ResponseHeaders": NotRequired[List[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2CustomResponseDetailsTypeDef = TypedDict(
    "AwsWafv2CustomResponseDetailsTypeDef",
    {
        "CustomResponseBodyKey": NotRequired[str],
        "ResponseCode": NotRequired[int],
        "ResponseHeaders": NotRequired[Sequence[AwsWafv2CustomHttpHeaderTypeDef]],
    },
)
AwsWafv2WebAclCaptchaConfigDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclCaptchaConfigDetailsTypeDef",
    {
        "ImmunityTimeProperty": NotRequired[
            AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef
        ],
    },
)
CreateActionTargetResponseTypeDef = TypedDict(
    "CreateActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAutomationRuleResponseTypeDef = TypedDict(
    "CreateAutomationRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFindingAggregatorResponseTypeDef = TypedDict(
    "CreateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInsightResponseTypeDef = TypedDict(
    "CreateInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteActionTargetResponseTypeDef = TypedDict(
    "DeleteActionTargetResponseTypeDef",
    {
        "ActionTargetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInsightResponseTypeDef = TypedDict(
    "DeleteInsightResponseTypeDef",
    {
        "InsightArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeActionTargetsResponseTypeDef = TypedDict(
    "DescribeActionTargetsResponseTypeDef",
    {
        "ActionTargets": List[ActionTargetTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubArn": str,
        "SubscribedAt": str,
        "AutoEnableControls": bool,
        "ControlFindingGenerator": ControlFindingGeneratorType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableImportFindingsForProductResponseTypeDef = TypedDict(
    "EnableImportFindingsForProductResponseTypeDef",
    {
        "ProductSubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfigurationPolicyAssociationResponseTypeDef = TypedDict(
    "GetConfigurationPolicyAssociationResponseTypeDef",
    {
        "ConfigurationPolicyId": str,
        "TargetId": str,
        "TargetType": TargetTypeType,
        "AssociationType": AssociationTypeType,
        "UpdatedAt": datetime,
        "AssociationStatus": ConfigurationPolicyAssociationStatusType,
        "AssociationStatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingAggregatorResponseTypeDef = TypedDict(
    "GetFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "InvitationsCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAutomationRulesResponseTypeDef = TypedDict(
    "ListAutomationRulesResponseTypeDef",
    {
        "AutomationRulesMetadata": List[AutomationRulesMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnabledProductsForImportResponseTypeDef = TypedDict(
    "ListEnabledProductsForImportResponseTypeDef",
    {
        "ProductSubscriptions": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "AdminAccounts": List[AdminAccountTypeDef],
        "NextToken": str,
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
StartConfigurationPolicyAssociationResponseTypeDef = TypedDict(
    "StartConfigurationPolicyAssociationResponseTypeDef",
    {
        "ConfigurationPolicyId": str,
        "TargetId": str,
        "TargetType": TargetTypeType,
        "AssociationType": AssociationTypeType,
        "UpdatedAt": datetime,
        "AssociationStatus": ConfigurationPolicyAssociationStatusType,
        "AssociationStatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFindingAggregatorResponseTypeDef = TypedDict(
    "UpdateFindingAggregatorResponseTypeDef",
    {
        "FindingAggregatorArn": str,
        "FindingAggregationRegion": str,
        "RegionLinkingMode": str,
        "Regions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteAutomationRulesResponseTypeDef = TypedDict(
    "BatchDeleteAutomationRulesResponseTypeDef",
    {
        "ProcessedAutomationRules": List[str],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateAutomationRulesResponseTypeDef = TypedDict(
    "BatchUpdateAutomationRulesResponseTypeDef",
    {
        "ProcessedAutomationRules": List[str],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEnableStandardsRequestRequestTypeDef = TypedDict(
    "BatchEnableStandardsRequestRequestTypeDef",
    {
        "StandardsSubscriptionRequests": Sequence[StandardsSubscriptionRequestTypeDef],
    },
)
ListConfigurationPolicyAssociationsResponseTypeDef = TypedDict(
    "ListConfigurationPolicyAssociationsResponseTypeDef",
    {
        "ConfigurationPolicyAssociationSummaries": List[
            ConfigurationPolicyAssociationSummaryTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "BatchGetStandardsControlAssociationsRequestRequestTypeDef",
    {
        "StandardsControlAssociationIds": Sequence[StandardsControlAssociationIdTypeDef],
    },
)
UnprocessedStandardsControlAssociationTypeDef = TypedDict(
    "UnprocessedStandardsControlAssociationTypeDef",
    {
        "StandardsControlAssociationId": StandardsControlAssociationIdTypeDef,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": NotRequired[str],
    },
)
BatchImportFindingsResponseTypeDef = TypedDict(
    "BatchImportFindingsResponseTypeDef",
    {
        "FailedCount": int,
        "SuccessCount": int,
        "FailedFindings": List[ImportFindingsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateStandardsControlAssociationsRequestRequestTypeDef = TypedDict(
    "BatchUpdateStandardsControlAssociationsRequestRequestTypeDef",
    {
        "StandardsControlAssociationUpdates": Sequence[StandardsControlAssociationUpdateTypeDef],
    },
)
UnprocessedStandardsControlAssociationUpdateTypeDef = TypedDict(
    "UnprocessedStandardsControlAssociationUpdateTypeDef",
    {
        "StandardsControlAssociationUpdate": StandardsControlAssociationUpdateTypeDef,
        "ErrorCode": UnprocessedErrorCodeType,
        "ErrorReason": NotRequired[str],
    },
)
VulnerabilityCodeVulnerabilitiesPaginatorTypeDef = TypedDict(
    "VulnerabilityCodeVulnerabilitiesPaginatorTypeDef",
    {
        "Cwes": NotRequired[List[str]],
        "FilePath": NotRequired[CodeVulnerabilitiesFilePathTypeDef],
        "SourceArn": NotRequired[str],
    },
)
VulnerabilityCodeVulnerabilitiesTypeDef = TypedDict(
    "VulnerabilityCodeVulnerabilitiesTypeDef",
    {
        "Cwes": NotRequired[Sequence[str]],
        "FilePath": NotRequired[CodeVulnerabilitiesFilePathTypeDef],
        "SourceArn": NotRequired[str],
    },
)
CompliancePaginatorTypeDef = TypedDict(
    "CompliancePaginatorTypeDef",
    {
        "Status": NotRequired[ComplianceStatusType],
        "RelatedRequirements": NotRequired[List[str]],
        "StatusReasons": NotRequired[List[StatusReasonTypeDef]],
        "SecurityControlId": NotRequired[str],
        "AssociatedStandards": NotRequired[List[AssociatedStandardTypeDef]],
        "SecurityControlParameters": NotRequired[List[SecurityControlParameterPaginatorTypeDef]],
    },
)
ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "Status": NotRequired[ComplianceStatusType],
        "RelatedRequirements": NotRequired[Sequence[str]],
        "StatusReasons": NotRequired[Sequence[StatusReasonTypeDef]],
        "SecurityControlId": NotRequired[str],
        "AssociatedStandards": NotRequired[Sequence[AssociatedStandardTypeDef]],
        "SecurityControlParameters": NotRequired[Sequence[SecurityControlParameterTypeDef]],
    },
)
ConfigurationOptionsTypeDef = TypedDict(
    "ConfigurationOptionsTypeDef",
    {
        "Integer": NotRequired[IntegerConfigurationOptionsTypeDef],
        "IntegerList": NotRequired[IntegerListConfigurationOptionsTypeDef],
        "Double": NotRequired[DoubleConfigurationOptionsTypeDef],
        "String": NotRequired[StringConfigurationOptionsTypeDef],
        "StringList": NotRequired[StringListConfigurationOptionsTypeDef],
        "Boolean": NotRequired[BooleanConfigurationOptionsTypeDef],
        "Enum": NotRequired[EnumConfigurationOptionsTypeDef],
        "EnumList": NotRequired[EnumListConfigurationOptionsTypeDef],
    },
)
ConfigurationPolicyAssociationTypeDef = TypedDict(
    "ConfigurationPolicyAssociationTypeDef",
    {
        "Target": NotRequired[TargetTypeDef],
    },
)
GetConfigurationPolicyAssociationRequestRequestTypeDef = TypedDict(
    "GetConfigurationPolicyAssociationRequestRequestTypeDef",
    {
        "Target": TargetTypeDef,
    },
)
StartConfigurationPolicyAssociationRequestRequestTypeDef = TypedDict(
    "StartConfigurationPolicyAssociationRequestRequestTypeDef",
    {
        "ConfigurationPolicyIdentifier": str,
        "Target": TargetTypeDef,
    },
)
StartConfigurationPolicyDisassociationRequestRequestTypeDef = TypedDict(
    "StartConfigurationPolicyDisassociationRequestRequestTypeDef",
    {
        "ConfigurationPolicyIdentifier": str,
        "Target": NotRequired[TargetTypeDef],
    },
)
ListConfigurationPoliciesResponseTypeDef = TypedDict(
    "ListConfigurationPoliciesResponseTypeDef",
    {
        "ConfigurationPolicySummaries": List[ConfigurationPolicySummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerDetailsPaginatorTypeDef = TypedDict(
    "ContainerDetailsPaginatorTypeDef",
    {
        "ContainerRuntime": NotRequired[str],
        "Name": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageName": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "VolumeMounts": NotRequired[List[VolumeMountTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
ContainerDetailsTypeDef = TypedDict(
    "ContainerDetailsTypeDef",
    {
        "ContainerRuntime": NotRequired[str],
        "Name": NotRequired[str],
        "ImageId": NotRequired[str],
        "ImageName": NotRequired[str],
        "LaunchedAt": NotRequired[str],
        "VolumeMounts": NotRequired[Sequence[VolumeMountTypeDef]],
        "Privileged": NotRequired[bool],
    },
)
CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InviteMembersResponseTypeDef = TypedDict(
    "InviteMembersResponseTypeDef",
    {
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "Start": NotRequired[str],
        "End": NotRequired[str],
        "DateRange": NotRequired[DateRangeTypeDef],
    },
)
DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef = TypedDict(
    "DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef",
    {
        "ActionTargetArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeProductsRequestDescribeProductsPaginateTypeDef = TypedDict(
    "DescribeProductsRequestDescribeProductsPaginateTypeDef",
    {
        "ProductArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef = TypedDict(
    "DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStandardsRequestDescribeStandardsPaginateTypeDef = TypedDict(
    "DescribeStandardsRequestDescribeStandardsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef = TypedDict(
    "GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef",
    {
        "StandardsSubscriptionArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetInsightsRequestGetInsightsPaginateTypeDef = TypedDict(
    "GetInsightsRequestGetInsightsPaginateTypeDef",
    {
        "InsightArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef = TypedDict(
    "ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef = TypedDict(
    "ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef",
    {
        "Filters": NotRequired[AssociationFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef = TypedDict(
    "ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef = TypedDict(
    "ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInvitationsRequestListInvitationsPaginateTypeDef = TypedDict(
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembersRequestListMembersPaginateTypeDef = TypedDict(
    "ListMembersRequestListMembersPaginateTypeDef",
    {
        "OnlyAssociated": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef = TypedDict(
    "ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef = TypedDict(
    "ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef",
    {
        "SecurityControlId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "MemberAccountLimitReached": bool,
        "AutoEnableStandards": AutoEnableStandardsType,
        "OrganizationConfiguration": OrganizationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "AutoEnable": bool,
        "AutoEnableStandards": NotRequired[AutoEnableStandardsType],
        "OrganizationConfiguration": NotRequired[OrganizationConfigurationTypeDef],
    },
)
DescribeProductsResponseTypeDef = TypedDict(
    "DescribeProductsResponseTypeDef",
    {
        "Products": List[ProductTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStandardsControlsResponseTypeDef = TypedDict(
    "DescribeStandardsControlsResponseTypeDef",
    {
        "Controls": List[StandardsControlTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ThreatPaginatorTypeDef = TypedDict(
    "ThreatPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "Severity": NotRequired[str],
        "ItemCount": NotRequired[int],
        "FilePaths": NotRequired[List[FilePathsTypeDef]],
    },
)
ThreatTypeDef = TypedDict(
    "ThreatTypeDef",
    {
        "Name": NotRequired[str],
        "Severity": NotRequired[str],
        "ItemCount": NotRequired[int],
        "FilePaths": NotRequired[Sequence[FilePathsTypeDef]],
    },
)
ListFindingAggregatorsResponseTypeDef = TypedDict(
    "ListFindingAggregatorsResponseTypeDef",
    {
        "FindingAggregators": List[FindingAggregatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingHistoryRecordTypeDef = TypedDict(
    "FindingHistoryRecordTypeDef",
    {
        "FindingIdentifier": NotRequired[AwsSecurityFindingIdentifierTypeDef],
        "UpdateTime": NotRequired[datetime],
        "FindingCreated": NotRequired[bool],
        "UpdateSource": NotRequired[FindingHistoryUpdateSourceTypeDef],
        "Updates": NotRequired[List[FindingHistoryUpdateTypeDef]],
        "NextToken": NotRequired[str],
    },
)
FindingProviderFieldsPaginatorTypeDef = TypedDict(
    "FindingProviderFieldsPaginatorTypeDef",
    {
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "RelatedFindings": NotRequired[List[RelatedFindingTypeDef]],
        "Severity": NotRequired[FindingProviderSeverityTypeDef],
        "Types": NotRequired[List[str]],
    },
)
FindingProviderFieldsTypeDef = TypedDict(
    "FindingProviderFieldsTypeDef",
    {
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
        "Severity": NotRequired[FindingProviderSeverityTypeDef],
        "Types": NotRequired[Sequence[str]],
    },
)
GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "Administrator": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "Master": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List[InvitationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef = TypedDict(
    "GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingHistoryRequestRequestTypeDef = TypedDict(
    "GetFindingHistoryRequestRequestTypeDef",
    {
        "FindingIdentifier": AwsSecurityFindingIdentifierTypeDef,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "UnprocessedAccounts": List[ResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InsightResultsTypeDef = TypedDict(
    "InsightResultsTypeDef",
    {
        "InsightArn": str,
        "GroupByAttribute": str,
        "ResultValues": List[InsightResultValueTypeDef],
    },
)
ListStandardsControlAssociationsResponseTypeDef = TypedDict(
    "ListStandardsControlAssociationsResponseTypeDef",
    {
        "StandardsControlAssociationSummaries": List[StandardsControlAssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkPathComponentDetailsPaginatorTypeDef = TypedDict(
    "NetworkPathComponentDetailsPaginatorTypeDef",
    {
        "Address": NotRequired[List[str]],
        "PortRanges": NotRequired[List[PortRangeTypeDef]],
    },
)
NetworkPathComponentDetailsTypeDef = TypedDict(
    "NetworkPathComponentDetailsTypeDef",
    {
        "Address": NotRequired[Sequence[str]],
        "PortRanges": NotRequired[Sequence[PortRangeTypeDef]],
    },
)
NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": NotRequired[NetworkDirectionType],
        "Protocol": NotRequired[str],
        "OpenPortRange": NotRequired[PortRangeTypeDef],
        "SourceIpV4": NotRequired[str],
        "SourceIpV6": NotRequired[str],
        "SourcePort": NotRequired[int],
        "SourceDomain": NotRequired[str],
        "SourceMac": NotRequired[str],
        "DestinationIpV4": NotRequired[str],
        "DestinationIpV6": NotRequired[str],
        "DestinationPort": NotRequired[int],
        "DestinationDomain": NotRequired[str],
    },
)
PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageNumber": NotRequired[int],
        "LineRange": NotRequired[RangeTypeDef],
        "OffsetRange": NotRequired[RangeTypeDef],
    },
)
ParameterConfigurationTypeDef = TypedDict(
    "ParameterConfigurationTypeDef",
    {
        "ValueType": ParameterValueTypeType,
        "Value": NotRequired[ParameterValueTypeDef],
    },
)
RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "Recommendation": NotRequired[RecommendationTypeDef],
    },
)
RuleGroupSourceStatefulRulesDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsPaginatorTypeDef",
    {
        "Action": NotRequired[str],
        "Header": NotRequired[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef],
        "RuleOptions": NotRequired[
            List[RuleGroupSourceStatefulRulesOptionsDetailsPaginatorTypeDef]
        ],
    },
)
RuleGroupSourceStatefulRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatefulRulesDetailsTypeDef",
    {
        "Action": NotRequired[str],
        "Header": NotRequired[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef],
        "RuleOptions": NotRequired[Sequence[RuleGroupSourceStatefulRulesOptionsDetailsTypeDef]],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesPaginatorTypeDef",
    {
        "DestinationPorts": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]
        ],
        "Destinations": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]
        ],
        "Protocols": NotRequired[List[int]],
        "SourcePorts": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]
        ],
        "Sources": NotRequired[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]],
        "TcpFlags": NotRequired[
            List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsPaginatorTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRuleMatchAttributesTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleMatchAttributesTypeDef",
    {
        "DestinationPorts": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]
        ],
        "Destinations": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]
        ],
        "Protocols": NotRequired[Sequence[int]],
        "SourcePorts": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]
        ],
        "Sources": NotRequired[Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]],
        "TcpFlags": NotRequired[
            Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef]
        ],
    },
)
RuleGroupVariablesPaginatorTypeDef = TypedDict(
    "RuleGroupVariablesPaginatorTypeDef",
    {
        "IpSets": NotRequired[RuleGroupVariablesIpSetsDetailsPaginatorTypeDef],
        "PortSets": NotRequired[RuleGroupVariablesPortSetsDetailsPaginatorTypeDef],
    },
)
RuleGroupVariablesTypeDef = TypedDict(
    "RuleGroupVariablesTypeDef",
    {
        "IpSets": NotRequired[RuleGroupVariablesIpSetsDetailsTypeDef],
        "PortSets": NotRequired[RuleGroupVariablesPortSetsDetailsTypeDef],
    },
)
StandardTypeDef = TypedDict(
    "StandardTypeDef",
    {
        "StandardsArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EnabledByDefault": NotRequired[bool],
        "StandardsManagedBy": NotRequired[StandardsManagedByTypeDef],
    },
)
StandardsSubscriptionTypeDef = TypedDict(
    "StandardsSubscriptionTypeDef",
    {
        "StandardsSubscriptionArn": str,
        "StandardsArn": str,
        "StandardsInput": Dict[str, str],
        "StandardsStatus": StandardsStatusType,
        "StandardsStatusReason": NotRequired[StandardsStatusReasonTypeDef],
    },
)
StatelessCustomPublishMetricActionPaginatorTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionPaginatorTypeDef",
    {
        "Dimensions": NotRequired[List[StatelessCustomPublishMetricActionDimensionTypeDef]],
    },
)
StatelessCustomPublishMetricActionTypeDef = TypedDict(
    "StatelessCustomPublishMetricActionTypeDef",
    {
        "Dimensions": NotRequired[Sequence[StatelessCustomPublishMetricActionDimensionTypeDef]],
    },
)
AwsApiCallActionPaginatorTypeDef = TypedDict(
    "AwsApiCallActionPaginatorTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "DomainDetails": NotRequired[AwsApiCallActionDomainDetailsTypeDef],
        "AffectedResources": NotRequired[Dict[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)
AwsApiCallActionTypeDef = TypedDict(
    "AwsApiCallActionTypeDef",
    {
        "Api": NotRequired[str],
        "ServiceName": NotRequired[str],
        "CallerType": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "DomainDetails": NotRequired[AwsApiCallActionDomainDetailsTypeDef],
        "AffectedResources": NotRequired[Mapping[str, str]],
        "FirstSeen": NotRequired[str],
        "LastSeen": NotRequired[str],
    },
)
NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": NotRequired[str],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
        "RemotePortDetails": NotRequired[ActionRemotePortDetailsTypeDef],
        "LocalPortDetails": NotRequired[ActionLocalPortDetailsTypeDef],
        "Protocol": NotRequired[str],
        "Blocked": NotRequired[bool],
    },
)
PortProbeDetailTypeDef = TypedDict(
    "PortProbeDetailTypeDef",
    {
        "LocalPortDetails": NotRequired[ActionLocalPortDetailsTypeDef],
        "LocalIpDetails": NotRequired[ActionLocalIpDetailsTypeDef],
        "RemoteIpDetails": NotRequired[ActionRemoteIpDetailsTypeDef],
    },
)
AwsEc2RouteTableDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2RouteTableDetailsPaginatorTypeDef",
    {
        "AssociationSet": NotRequired[List[AssociationSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PropagatingVgwSet": NotRequired[List[PropagatingVgwSetDetailsTypeDef]],
        "RouteTableId": NotRequired[str],
        "RouteSet": NotRequired[List[RouteSetDetailsTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AwsEc2RouteTableDetailsTypeDef = TypedDict(
    "AwsEc2RouteTableDetailsTypeDef",
    {
        "AssociationSet": NotRequired[Sequence[AssociationSetDetailsTypeDef]],
        "OwnerId": NotRequired[str],
        "PropagatingVgwSet": NotRequired[Sequence[PropagatingVgwSetDetailsTypeDef]],
        "RouteTableId": NotRequired[str],
        "RouteSet": NotRequired[Sequence[RouteSetDetailsTypeDef]],
        "VpcId": NotRequired[str],
    },
)
AutomationRulesActionTypeDef = TypedDict(
    "AutomationRulesActionTypeDef",
    {
        "Type": NotRequired[Literal["FINDING_FIELDS_UPDATE"]],
        "FindingFieldsUpdate": NotRequired[AutomationRulesFindingFieldsUpdateTypeDef],
    },
)
AwsAmazonMqBrokerDetailsPaginatorTypeDef = TypedDict(
    "AwsAmazonMqBrokerDetailsPaginatorTypeDef",
    {
        "AuthenticationStrategy": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "BrokerArn": NotRequired[str],
        "BrokerName": NotRequired[str],
        "DeploymentMode": NotRequired[str],
        "EncryptionOptions": NotRequired[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef],
        "EngineType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "BrokerId": NotRequired[str],
        "LdapServerMetadata": NotRequired[
            AwsAmazonMqBrokerLdapServerMetadataDetailsPaginatorTypeDef
        ],
        "Logs": NotRequired[AwsAmazonMqBrokerLogsDetailsTypeDef],
        "MaintenanceWindowStartTime": NotRequired[
            AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef
        ],
        "PubliclyAccessible": NotRequired[bool],
        "SecurityGroups": NotRequired[List[str]],
        "StorageType": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "Users": NotRequired[List[AwsAmazonMqBrokerUsersDetailsTypeDef]],
    },
)
AwsAmazonMqBrokerDetailsTypeDef = TypedDict(
    "AwsAmazonMqBrokerDetailsTypeDef",
    {
        "AuthenticationStrategy": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "BrokerArn": NotRequired[str],
        "BrokerName": NotRequired[str],
        "DeploymentMode": NotRequired[str],
        "EncryptionOptions": NotRequired[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef],
        "EngineType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "BrokerId": NotRequired[str],
        "LdapServerMetadata": NotRequired[AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef],
        "Logs": NotRequired[AwsAmazonMqBrokerLogsDetailsTypeDef],
        "MaintenanceWindowStartTime": NotRequired[
            AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef
        ],
        "PubliclyAccessible": NotRequired[bool],
        "SecurityGroups": NotRequired[Sequence[str]],
        "StorageType": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "Users": NotRequired[Sequence[AwsAmazonMqBrokerUsersDetailsTypeDef]],
    },
)
AwsAppSyncGraphQlApiDetailsPaginatorTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiDetailsPaginatorTypeDef",
    {
        "ApiId": NotRequired[str],
        "Id": NotRequired[str],
        "OpenIdConnectConfig": NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef],
        "Name": NotRequired[str],
        "LambdaAuthorizerConfig": NotRequired[
            AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef
        ],
        "XrayEnabled": NotRequired[bool],
        "Arn": NotRequired[str],
        "UserPoolConfig": NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef],
        "AuthenticationType": NotRequired[str],
        "LogConfig": NotRequired[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef],
        "AdditionalAuthenticationProviders": NotRequired[
            List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]
        ],
        "WafWebAclArn": NotRequired[str],
    },
)
AwsAppSyncGraphQlApiDetailsTypeDef = TypedDict(
    "AwsAppSyncGraphQlApiDetailsTypeDef",
    {
        "ApiId": NotRequired[str],
        "Id": NotRequired[str],
        "OpenIdConnectConfig": NotRequired[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef],
        "Name": NotRequired[str],
        "LambdaAuthorizerConfig": NotRequired[
            AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef
        ],
        "XrayEnabled": NotRequired[bool],
        "Arn": NotRequired[str],
        "UserPoolConfig": NotRequired[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef],
        "AuthenticationType": NotRequired[str],
        "LogConfig": NotRequired[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef],
        "AdditionalAuthenticationProviders": NotRequired[
            Sequence[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]
        ],
        "WafWebAclArn": NotRequired[str],
    },
)
AwsAthenaWorkGroupConfigurationDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupConfigurationDetailsTypeDef",
    {
        "ResultConfiguration": NotRequired[
            AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsPaginatorTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsPaginatorTypeDef",
    {
        "InstancesDistribution": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsPaginatorTypeDef
        ],
    },
)
AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef",
    {
        "InstancesDistribution": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef
        ],
    },
)
AwsAutoScalingLaunchConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsPaginatorTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BlockDeviceMappings": NotRequired[
            List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]
        ],
        "ClassicLinkVpcId": NotRequired[str],
        "ClassicLinkVpcSecurityGroups": NotRequired[List[str]],
        "CreatedTime": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceMonitoring": NotRequired[
            AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "PlacementTenancy": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "SpotPrice": NotRequired[str],
        "UserData": NotRequired[str],
        "MetadataOptions": NotRequired[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef],
    },
)
AwsAutoScalingLaunchConfigurationDetailsTypeDef = TypedDict(
    "AwsAutoScalingLaunchConfigurationDetailsTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BlockDeviceMappings": NotRequired[
            Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]
        ],
        "ClassicLinkVpcId": NotRequired[str],
        "ClassicLinkVpcSecurityGroups": NotRequired[Sequence[str]],
        "CreatedTime": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "IamInstanceProfile": NotRequired[str],
        "ImageId": NotRequired[str],
        "InstanceMonitoring": NotRequired[
            AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "PlacementTenancy": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SpotPrice": NotRequired[str],
        "UserData": NotRequired[str],
        "MetadataOptions": NotRequired[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef],
    },
)
AwsBackupBackupPlanRuleDetailsPaginatorTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleDetailsPaginatorTypeDef",
    {
        "TargetBackupVault": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "ScheduleExpression": NotRequired[str],
        "RuleName": NotRequired[str],
        "RuleId": NotRequired[str],
        "EnableContinuousBackup": NotRequired[bool],
        "CompletionWindowMinutes": NotRequired[int],
        "CopyActions": NotRequired[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]],
        "Lifecycle": NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef],
    },
)
AwsBackupBackupPlanRuleDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanRuleDetailsTypeDef",
    {
        "TargetBackupVault": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "ScheduleExpression": NotRequired[str],
        "RuleName": NotRequired[str],
        "RuleId": NotRequired[str],
        "EnableContinuousBackup": NotRequired[bool],
        "CompletionWindowMinutes": NotRequired[int],
        "CopyActions": NotRequired[Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]],
        "Lifecycle": NotRequired[AwsBackupBackupPlanLifecycleDetailsTypeDef],
    },
)
AwsCertificateManagerCertificateRenewalSummaryPaginatorTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryPaginatorTypeDef",
    {
        "DomainValidationOptions": NotRequired[
            List[AwsCertificateManagerCertificateDomainValidationOptionPaginatorTypeDef]
        ],
        "RenewalStatus": NotRequired[str],
        "RenewalStatusReason": NotRequired[str],
        "UpdatedAt": NotRequired[str],
    },
)
AwsCertificateManagerCertificateRenewalSummaryTypeDef = TypedDict(
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    {
        "DomainValidationOptions": NotRequired[
            Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]
        ],
        "RenewalStatus": NotRequired[str],
        "RenewalStatusReason": NotRequired[str],
        "UpdatedAt": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginItemPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemPaginatorTypeDef",
    {
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "OriginPath": NotRequired[str],
        "S3OriginConfig": NotRequired[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef],
        "CustomOriginConfig": NotRequired[
            AwsCloudFrontDistributionOriginCustomOriginConfigPaginatorTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginItemTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginItemTypeDef",
    {
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "OriginPath": NotRequired[str],
        "S3OriginConfig": NotRequired[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef],
        "CustomOriginConfig": NotRequired[AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef],
    },
)
AwsCloudFrontDistributionOriginGroupPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupPaginatorTypeDef",
    {
        "FailoverCriteria": NotRequired[
            AwsCloudFrontDistributionOriginGroupFailoverPaginatorTypeDef
        ],
    },
)
AwsCloudFrontDistributionOriginGroupTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    {
        "FailoverCriteria": NotRequired[AwsCloudFrontDistributionOriginGroupFailoverTypeDef],
    },
)
AwsCodeBuildProjectDetailsPaginatorTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsPaginatorTypeDef",
    {
        "EncryptionKey": NotRequired[str],
        "Artifacts": NotRequired[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
        "Environment": NotRequired[AwsCodeBuildProjectEnvironmentPaginatorTypeDef],
        "Name": NotRequired[str],
        "Source": NotRequired[AwsCodeBuildProjectSourceTypeDef],
        "ServiceRole": NotRequired[str],
        "LogsConfig": NotRequired[AwsCodeBuildProjectLogsConfigDetailsTypeDef],
        "VpcConfig": NotRequired[AwsCodeBuildProjectVpcConfigPaginatorTypeDef],
        "SecondaryArtifacts": NotRequired[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
    },
)
AwsCodeBuildProjectDetailsTypeDef = TypedDict(
    "AwsCodeBuildProjectDetailsTypeDef",
    {
        "EncryptionKey": NotRequired[str],
        "Artifacts": NotRequired[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
        "Environment": NotRequired[AwsCodeBuildProjectEnvironmentTypeDef],
        "Name": NotRequired[str],
        "Source": NotRequired[AwsCodeBuildProjectSourceTypeDef],
        "ServiceRole": NotRequired[str],
        "LogsConfig": NotRequired[AwsCodeBuildProjectLogsConfigDetailsTypeDef],
        "VpcConfig": NotRequired[AwsCodeBuildProjectVpcConfigTypeDef],
        "SecondaryArtifacts": NotRequired[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]],
    },
)
AwsDynamoDbTableReplicaPaginatorTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaPaginatorTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)
AwsDynamoDbTableReplicaTypeDef = TypedDict(
    "AwsDynamoDbTableReplicaTypeDef",
    {
        "GlobalSecondaryIndexes": NotRequired[
            Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]
        ],
        "KmsMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired[
            AwsDynamoDbTableProvisionedThroughputOverrideTypeDef
        ],
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[str],
        "ReplicaStatusDescription": NotRequired[str],
    },
)
AwsEc2ClientVpnEndpointDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointDetailsPaginatorTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "ClientCidrBlock": NotRequired[str],
        "DnsServer": NotRequired[List[str]],
        "SplitTunnel": NotRequired[bool],
        "TransportProtocol": NotRequired[str],
        "VpnPort": NotRequired[int],
        "ServerCertificateArn": NotRequired[str],
        "AuthenticationOptions": NotRequired[
            List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]
        ],
        "ConnectionLogOptions": NotRequired[
            AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef
        ],
        "SecurityGroupIdSet": NotRequired[List[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortalUrl": NotRequired[str],
        "ClientConnectOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef
        ],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef
        ],
    },
)
AwsEc2ClientVpnEndpointDetailsTypeDef = TypedDict(
    "AwsEc2ClientVpnEndpointDetailsTypeDef",
    {
        "ClientVpnEndpointId": NotRequired[str],
        "Description": NotRequired[str],
        "ClientCidrBlock": NotRequired[str],
        "DnsServer": NotRequired[Sequence[str]],
        "SplitTunnel": NotRequired[bool],
        "TransportProtocol": NotRequired[str],
        "VpnPort": NotRequired[int],
        "ServerCertificateArn": NotRequired[str],
        "AuthenticationOptions": NotRequired[
            Sequence[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]
        ],
        "ConnectionLogOptions": NotRequired[
            AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef
        ],
        "SecurityGroupIdSet": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
        "SelfServicePortalUrl": NotRequired[str],
        "ClientConnectOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef
        ],
        "SessionTimeoutHours": NotRequired[int],
        "ClientLoginBannerOptions": NotRequired[
            AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef
        ],
    },
)
AwsEc2LaunchTemplateDataDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataDetailsPaginatorTypeDef",
    {
        "BlockDeviceMappingSet": NotRequired[
            List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]
        ],
        "CapacityReservationSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
        ],
        "CpuOptions": NotRequired[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef],
        "CreditSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef
        ],
        "DisableApiStop": NotRequired[bool],
        "DisableApiTermination": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "ElasticGpuSpecificationSet": NotRequired[
            List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]
        ],
        "ElasticInferenceAcceleratorSet": NotRequired[
            List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]
        ],
        "EnclaveOptions": NotRequired[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef],
        "HibernationOptions": NotRequired[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef],
        "IamInstanceProfile": NotRequired[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef],
        "ImageId": NotRequired[str],
        "InstanceInitiatedShutdownBehavior": NotRequired[str],
        "InstanceMarketOptions": NotRequired[
            AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef
        ],
        "InstanceRequirements": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsDetailsPaginatorTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LicenseSet": NotRequired[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]],
        "MaintenanceOptions": NotRequired[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef],
        "MetadataOptions": NotRequired[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef],
        "Monitoring": NotRequired[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef],
        "NetworkInterfaceSet": NotRequired[
            List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsPaginatorTypeDef]
        ],
        "Placement": NotRequired[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef],
        "PrivateDnsNameOptions": NotRequired[
            AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef
        ],
        "RamDiskId": NotRequired[str],
        "SecurityGroupIdSet": NotRequired[List[str]],
        "SecurityGroupSet": NotRequired[List[str]],
        "UserData": NotRequired[str],
    },
)
AwsEc2LaunchTemplateDataDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDataDetailsTypeDef",
    {
        "BlockDeviceMappingSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]
        ],
        "CapacityReservationSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef
        ],
        "CpuOptions": NotRequired[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef],
        "CreditSpecification": NotRequired[
            AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef
        ],
        "DisableApiStop": NotRequired[bool],
        "DisableApiTermination": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "ElasticGpuSpecificationSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]
        ],
        "ElasticInferenceAcceleratorSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]
        ],
        "EnclaveOptions": NotRequired[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef],
        "HibernationOptions": NotRequired[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef],
        "IamInstanceProfile": NotRequired[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef],
        "ImageId": NotRequired[str],
        "InstanceInitiatedShutdownBehavior": NotRequired[str],
        "InstanceMarketOptions": NotRequired[
            AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef
        ],
        "InstanceRequirements": NotRequired[
            AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef
        ],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "KeyName": NotRequired[str],
        "LicenseSet": NotRequired[Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]],
        "MaintenanceOptions": NotRequired[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef],
        "MetadataOptions": NotRequired[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef],
        "Monitoring": NotRequired[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef],
        "NetworkInterfaceSet": NotRequired[
            Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef]
        ],
        "Placement": NotRequired[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef],
        "PrivateDnsNameOptions": NotRequired[
            AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef
        ],
        "RamDiskId": NotRequired[str],
        "SecurityGroupIdSet": NotRequired[Sequence[str]],
        "SecurityGroupSet": NotRequired[Sequence[str]],
        "UserData": NotRequired[str],
    },
)
AwsEc2NetworkAclDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsPaginatorTypeDef",
    {
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Associations": NotRequired[List[AwsEc2NetworkAclAssociationTypeDef]],
        "Entries": NotRequired[List[AwsEc2NetworkAclEntryTypeDef]],
    },
)
AwsEc2NetworkAclDetailsTypeDef = TypedDict(
    "AwsEc2NetworkAclDetailsTypeDef",
    {
        "IsDefault": NotRequired[bool],
        "NetworkAclId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "Associations": NotRequired[Sequence[AwsEc2NetworkAclAssociationTypeDef]],
        "Entries": NotRequired[Sequence[AwsEc2NetworkAclEntryTypeDef]],
    },
)
AwsEc2SecurityGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsPaginatorTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "IpPermissions": NotRequired[List[AwsEc2SecurityGroupIpPermissionPaginatorTypeDef]],
        "IpPermissionsEgress": NotRequired[List[AwsEc2SecurityGroupIpPermissionPaginatorTypeDef]],
    },
)
AwsEc2SecurityGroupDetailsTypeDef = TypedDict(
    "AwsEc2SecurityGroupDetailsTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "IpPermissions": NotRequired[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]],
        "IpPermissionsEgress": NotRequired[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]],
    },
)
AwsEc2VpcPeeringConnectionDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionDetailsPaginatorTypeDef",
    {
        "AccepterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsPaginatorTypeDef],
        "ExpirationTime": NotRequired[str],
        "RequesterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsPaginatorTypeDef],
        "Status": NotRequired[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
AwsEc2VpcPeeringConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpcPeeringConnectionDetailsTypeDef",
    {
        "AccepterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef],
        "ExpirationTime": NotRequired[str],
        "RequesterVpcInfo": NotRequired[AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef],
        "Status": NotRequired[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef],
        "VpcPeeringConnectionId": NotRequired[str],
    },
)
AwsEc2VpnConnectionDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsPaginatorTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]],
        "Options": NotRequired[AwsEc2VpnConnectionOptionsDetailsPaginatorTypeDef],
        "Routes": NotRequired[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]],
        "TransitGatewayId": NotRequired[str],
    },
)
AwsEc2VpnConnectionDetailsTypeDef = TypedDict(
    "AwsEc2VpnConnectionDetailsTypeDef",
    {
        "VpnConnectionId": NotRequired[str],
        "State": NotRequired[str],
        "CustomerGatewayId": NotRequired[str],
        "CustomerGatewayConfiguration": NotRequired[str],
        "Type": NotRequired[str],
        "VpnGatewayId": NotRequired[str],
        "Category": NotRequired[str],
        "VgwTelemetry": NotRequired[Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]],
        "Options": NotRequired[AwsEc2VpnConnectionOptionsDetailsTypeDef],
        "Routes": NotRequired[Sequence[AwsEc2VpnConnectionRoutesDetailsTypeDef]],
        "TransitGatewayId": NotRequired[str],
    },
)
AwsEcsClusterConfigurationDetailsTypeDef = TypedDict(
    "AwsEcsClusterConfigurationDetailsTypeDef",
    {
        "ExecuteCommandConfiguration": NotRequired[
            AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef
        ],
    },
)
AwsEcsServiceDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsServiceDetailsPaginatorTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[AwsEcsServiceDeploymentConfigurationDetailsTypeDef],
        "DeploymentController": NotRequired[AwsEcsServiceDeploymentControllerDetailsTypeDef],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[List[AwsEcsServiceLoadBalancersDetailsTypeDef]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[
            AwsEcsServiceNetworkConfigurationDetailsPaginatorTypeDef
        ],
        "PlacementConstraints": NotRequired[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]],
        "PlacementStrategies": NotRequired[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]],
        "TaskDefinition": NotRequired[str],
    },
)
AwsEcsServiceDetailsTypeDef = TypedDict(
    "AwsEcsServiceDetailsTypeDef",
    {
        "CapacityProviderStrategy": NotRequired[
            Sequence[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]
        ],
        "Cluster": NotRequired[str],
        "DeploymentConfiguration": NotRequired[AwsEcsServiceDeploymentConfigurationDetailsTypeDef],
        "DeploymentController": NotRequired[AwsEcsServiceDeploymentControllerDetailsTypeDef],
        "DesiredCount": NotRequired[int],
        "EnableEcsManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "HealthCheckGracePeriodSeconds": NotRequired[int],
        "LaunchType": NotRequired[str],
        "LoadBalancers": NotRequired[Sequence[AwsEcsServiceLoadBalancersDetailsTypeDef]],
        "Name": NotRequired[str],
        "NetworkConfiguration": NotRequired[AwsEcsServiceNetworkConfigurationDetailsTypeDef],
        "PlacementConstraints": NotRequired[
            Sequence[AwsEcsServicePlacementConstraintsDetailsTypeDef]
        ],
        "PlacementStrategies": NotRequired[
            Sequence[AwsEcsServicePlacementStrategiesDetailsTypeDef]
        ],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[str],
        "Role": NotRequired[str],
        "SchedulingStrategy": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceRegistries": NotRequired[Sequence[AwsEcsServiceServiceRegistriesDetailsTypeDef]],
        "TaskDefinition": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsPaginatorTypeDef",
    {
        "Command": NotRequired[List[str]],
        "Cpu": NotRequired[int],
        "DependsOn": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]
        ],
        "DisableNetworking": NotRequired[bool],
        "DnsSearchDomains": NotRequired[List[str]],
        "DnsServers": NotRequired[List[str]],
        "DockerLabels": NotRequired[Dict[str, str]],
        "DockerSecurityOptions": NotRequired[List[str]],
        "EntryPoint": NotRequired[List[str]],
        "Environment": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]
        ],
        "EnvironmentFiles": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]
        ],
        "Essential": NotRequired[bool],
        "ExtraHosts": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]
        ],
        "FirelensConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsPaginatorTypeDef
        ],
        "HealthCheck": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsPaginatorTypeDef
        ],
        "Hostname": NotRequired[str],
        "Image": NotRequired[str],
        "Interactive": NotRequired[bool],
        "Links": NotRequired[List[str]],
        "LinuxParameters": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsPaginatorTypeDef
        ],
        "LogConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsPaginatorTypeDef
        ],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "MountPoints": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]
        ],
        "Name": NotRequired[str],
        "PortMappings": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]
        ],
        "Privileged": NotRequired[bool],
        "PseudoTerminal": NotRequired[bool],
        "ReadonlyRootFilesystem": NotRequired[bool],
        "RepositoryCredentials": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
        ],
        "ResourceRequirements": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]
        ],
        "Secrets": NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]],
        "StartTimeout": NotRequired[int],
        "StopTimeout": NotRequired[int],
        "SystemControls": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]
        ],
        "Ulimits": NotRequired[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]],
        "User": NotRequired[str],
        "VolumesFrom": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]
        ],
        "WorkingDirectory": NotRequired[str],
    },
)
AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef",
    {
        "Command": NotRequired[Sequence[str]],
        "Cpu": NotRequired[int],
        "DependsOn": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]
        ],
        "DisableNetworking": NotRequired[bool],
        "DnsSearchDomains": NotRequired[Sequence[str]],
        "DnsServers": NotRequired[Sequence[str]],
        "DockerLabels": NotRequired[Mapping[str, str]],
        "DockerSecurityOptions": NotRequired[Sequence[str]],
        "EntryPoint": NotRequired[Sequence[str]],
        "Environment": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]
        ],
        "EnvironmentFiles": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]
        ],
        "Essential": NotRequired[bool],
        "ExtraHosts": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]
        ],
        "FirelensConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef
        ],
        "HealthCheck": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef
        ],
        "Hostname": NotRequired[str],
        "Image": NotRequired[str],
        "Interactive": NotRequired[bool],
        "Links": NotRequired[Sequence[str]],
        "LinuxParameters": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef
        ],
        "LogConfiguration": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef
        ],
        "Memory": NotRequired[int],
        "MemoryReservation": NotRequired[int],
        "MountPoints": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]
        ],
        "Name": NotRequired[str],
        "PortMappings": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]
        ],
        "Privileged": NotRequired[bool],
        "PseudoTerminal": NotRequired[bool],
        "ReadonlyRootFilesystem": NotRequired[bool],
        "RepositoryCredentials": NotRequired[
            AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef
        ],
        "ResourceRequirements": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]
        ],
        "Secrets": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]
        ],
        "StartTimeout": NotRequired[int],
        "StopTimeout": NotRequired[int],
        "SystemControls": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]
        ],
        "Ulimits": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]
        ],
        "User": NotRequired[str],
        "VolumesFrom": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]
        ],
        "WorkingDirectory": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsPaginatorTypeDef",
    {
        "DockerVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsPaginatorTypeDef
        ],
        "EfsVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef
        ],
        "Host": NotRequired[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef],
        "Name": NotRequired[str],
    },
)
AwsEcsTaskDefinitionVolumesDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionVolumesDetailsTypeDef",
    {
        "DockerVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef
        ],
        "EfsVolumeConfiguration": NotRequired[
            AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef
        ],
        "Host": NotRequired[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef],
        "Name": NotRequired[str],
    },
)
AwsEcsTaskDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDetailsPaginatorTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "TaskDefinitionArn": NotRequired[str],
        "Version": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "StartedAt": NotRequired[str],
        "StartedBy": NotRequired[str],
        "Group": NotRequired[str],
        "Volumes": NotRequired[List[AwsEcsTaskVolumeDetailsTypeDef]],
        "Containers": NotRequired[List[AwsEcsContainerDetailsPaginatorTypeDef]],
    },
)
AwsEcsTaskDetailsTypeDef = TypedDict(
    "AwsEcsTaskDetailsTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "TaskDefinitionArn": NotRequired[str],
        "Version": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "StartedAt": NotRequired[str],
        "StartedBy": NotRequired[str],
        "Group": NotRequired[str],
        "Volumes": NotRequired[Sequence[AwsEcsTaskVolumeDetailsTypeDef]],
        "Containers": NotRequired[Sequence[AwsEcsContainerDetailsTypeDef]],
    },
)
AwsEfsAccessPointDetailsPaginatorTypeDef = TypedDict(
    "AwsEfsAccessPointDetailsPaginatorTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Arn": NotRequired[str],
        "ClientToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PosixUser": NotRequired[AwsEfsAccessPointPosixUserDetailsPaginatorTypeDef],
        "RootDirectory": NotRequired[AwsEfsAccessPointRootDirectoryDetailsTypeDef],
    },
)
AwsEfsAccessPointDetailsTypeDef = TypedDict(
    "AwsEfsAccessPointDetailsTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "Arn": NotRequired[str],
        "ClientToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PosixUser": NotRequired[AwsEfsAccessPointPosixUserDetailsTypeDef],
        "RootDirectory": NotRequired[AwsEfsAccessPointRootDirectoryDetailsTypeDef],
    },
)
AwsEksClusterDetailsPaginatorTypeDef = TypedDict(
    "AwsEksClusterDetailsPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityData": NotRequired[str],
        "ClusterStatus": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Name": NotRequired[str],
        "ResourcesVpcConfig": NotRequired[AwsEksClusterResourcesVpcConfigDetailsPaginatorTypeDef],
        "RoleArn": NotRequired[str],
        "Version": NotRequired[str],
        "Logging": NotRequired[AwsEksClusterLoggingDetailsPaginatorTypeDef],
    },
)
AwsEksClusterDetailsTypeDef = TypedDict(
    "AwsEksClusterDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateAuthorityData": NotRequired[str],
        "ClusterStatus": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Name": NotRequired[str],
        "ResourcesVpcConfig": NotRequired[AwsEksClusterResourcesVpcConfigDetailsTypeDef],
        "RoleArn": NotRequired[str],
        "Version": NotRequired[str],
        "Logging": NotRequired[AwsEksClusterLoggingDetailsTypeDef],
    },
)
AwsElasticsearchDomainDetailsPaginatorTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsPaginatorTypeDef",
    {
        "AccessPolicies": NotRequired[str],
        "DomainEndpointOptions": NotRequired[AwsElasticsearchDomainDomainEndpointOptionsTypeDef],
        "DomainId": NotRequired[str],
        "DomainName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Dict[str, str]],
        "ElasticsearchVersion": NotRequired[str],
        "ElasticsearchClusterConfig": NotRequired[
            AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
        ],
        "EncryptionAtRestOptions": NotRequired[
            AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef
        ],
        "LogPublishingOptions": NotRequired[AwsElasticsearchDomainLogPublishingOptionsTypeDef],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef],
        "VPCOptions": NotRequired[AwsElasticsearchDomainVPCOptionsPaginatorTypeDef],
    },
)
AwsElasticsearchDomainDetailsTypeDef = TypedDict(
    "AwsElasticsearchDomainDetailsTypeDef",
    {
        "AccessPolicies": NotRequired[str],
        "DomainEndpointOptions": NotRequired[AwsElasticsearchDomainDomainEndpointOptionsTypeDef],
        "DomainId": NotRequired[str],
        "DomainName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Endpoints": NotRequired[Mapping[str, str]],
        "ElasticsearchVersion": NotRequired[str],
        "ElasticsearchClusterConfig": NotRequired[
            AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef
        ],
        "EncryptionAtRestOptions": NotRequired[
            AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef
        ],
        "LogPublishingOptions": NotRequired[AwsElasticsearchDomainLogPublishingOptionsTypeDef],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef],
        "VPCOptions": NotRequired[AwsElasticsearchDomainVPCOptionsTypeDef],
    },
)
AwsElbLoadBalancerDetailsPaginatorTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsPaginatorTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "BackendServerDescriptions": NotRequired[
            List[AwsElbLoadBalancerBackendServerDescriptionPaginatorTypeDef]
        ],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "HealthCheck": NotRequired[AwsElbLoadBalancerHealthCheckTypeDef],
        "Instances": NotRequired[List[AwsElbLoadBalancerInstanceTypeDef]],
        "ListenerDescriptions": NotRequired[
            List[AwsElbLoadBalancerListenerDescriptionPaginatorTypeDef]
        ],
        "LoadBalancerAttributes": NotRequired[AwsElbLoadBalancerAttributesPaginatorTypeDef],
        "LoadBalancerName": NotRequired[str],
        "Policies": NotRequired[AwsElbLoadBalancerPoliciesPaginatorTypeDef],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "SourceSecurityGroup": NotRequired[AwsElbLoadBalancerSourceSecurityGroupTypeDef],
        "Subnets": NotRequired[List[str]],
        "VpcId": NotRequired[str],
    },
)
AwsElbLoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbLoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackendServerDescriptions": NotRequired[
            Sequence[AwsElbLoadBalancerBackendServerDescriptionTypeDef]
        ],
        "CanonicalHostedZoneName": NotRequired[str],
        "CanonicalHostedZoneNameID": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "DnsName": NotRequired[str],
        "HealthCheck": NotRequired[AwsElbLoadBalancerHealthCheckTypeDef],
        "Instances": NotRequired[Sequence[AwsElbLoadBalancerInstanceTypeDef]],
        "ListenerDescriptions": NotRequired[Sequence[AwsElbLoadBalancerListenerDescriptionTypeDef]],
        "LoadBalancerAttributes": NotRequired[AwsElbLoadBalancerAttributesTypeDef],
        "LoadBalancerName": NotRequired[str],
        "Policies": NotRequired[AwsElbLoadBalancerPoliciesTypeDef],
        "Scheme": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "SourceSecurityGroup": NotRequired[AwsElbLoadBalancerSourceSecurityGroupTypeDef],
        "Subnets": NotRequired[Sequence[str]],
        "VpcId": NotRequired[str],
    },
)
AwsEventsEndpointRoutingConfigDetailsTypeDef = TypedDict(
    "AwsEventsEndpointRoutingConfigDetailsTypeDef",
    {
        "FailoverConfig": NotRequired[AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef],
    },
)
AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef",
    {
        "ScanEc2InstanceWithFindings": NotRequired[
            AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef
        ],
        "ServiceRole": NotRequired[str],
    },
)
AwsIamAccessKeyDetailsTypeDef = TypedDict(
    "AwsIamAccessKeyDetailsTypeDef",
    {
        "UserName": NotRequired[str],
        "Status": NotRequired[AwsIamAccessKeyStatusType],
        "CreatedAt": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[str],
        "PrincipalName": NotRequired[str],
        "AccountId": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "SessionContext": NotRequired[AwsIamAccessKeySessionContextTypeDef],
    },
)
AwsIamRoleDetailsPaginatorTypeDef = TypedDict(
    "AwsIamRoleDetailsPaginatorTypeDef",
    {
        "AssumeRolePolicyDocument": NotRequired[str],
        "AttachedManagedPolicies": NotRequired[List[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "InstanceProfileList": NotRequired[List[AwsIamInstanceProfilePaginatorTypeDef]],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
        "RolePolicyList": NotRequired[List[AwsIamRolePolicyTypeDef]],
        "MaxSessionDuration": NotRequired[int],
        "Path": NotRequired[str],
    },
)
AwsIamRoleDetailsTypeDef = TypedDict(
    "AwsIamRoleDetailsTypeDef",
    {
        "AssumeRolePolicyDocument": NotRequired[str],
        "AttachedManagedPolicies": NotRequired[Sequence[AwsIamAttachedManagedPolicyTypeDef]],
        "CreateDate": NotRequired[str],
        "InstanceProfileList": NotRequired[Sequence[AwsIamInstanceProfileTypeDef]],
        "PermissionsBoundary": NotRequired[AwsIamPermissionsBoundaryTypeDef],
        "RoleId": NotRequired[str],
        "RoleName": NotRequired[str],
        "RolePolicyList": NotRequired[Sequence[AwsIamRolePolicyTypeDef]],
        "MaxSessionDuration": NotRequired[int],
        "Path": NotRequired[str],
    },
)
AwsLambdaFunctionDetailsPaginatorTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsPaginatorTypeDef",
    {
        "Code": NotRequired[AwsLambdaFunctionCodeTypeDef],
        "CodeSha256": NotRequired[str],
        "DeadLetterConfig": NotRequired[AwsLambdaFunctionDeadLetterConfigTypeDef],
        "Environment": NotRequired[AwsLambdaFunctionEnvironmentPaginatorTypeDef],
        "FunctionName": NotRequired[str],
        "Handler": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "LastModified": NotRequired[str],
        "Layers": NotRequired[List[AwsLambdaFunctionLayerTypeDef]],
        "MasterArn": NotRequired[str],
        "MemorySize": NotRequired[int],
        "RevisionId": NotRequired[str],
        "Role": NotRequired[str],
        "Runtime": NotRequired[str],
        "Timeout": NotRequired[int],
        "TracingConfig": NotRequired[AwsLambdaFunctionTracingConfigTypeDef],
        "VpcConfig": NotRequired[AwsLambdaFunctionVpcConfigPaginatorTypeDef],
        "Version": NotRequired[str],
        "Architectures": NotRequired[List[str]],
        "PackageType": NotRequired[str],
    },
)
AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "Code": NotRequired[AwsLambdaFunctionCodeTypeDef],
        "CodeSha256": NotRequired[str],
        "DeadLetterConfig": NotRequired[AwsLambdaFunctionDeadLetterConfigTypeDef],
        "Environment": NotRequired[AwsLambdaFunctionEnvironmentTypeDef],
        "FunctionName": NotRequired[str],
        "Handler": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "LastModified": NotRequired[str],
        "Layers": NotRequired[Sequence[AwsLambdaFunctionLayerTypeDef]],
        "MasterArn": NotRequired[str],
        "MemorySize": NotRequired[int],
        "RevisionId": NotRequired[str],
        "Role": NotRequired[str],
        "Runtime": NotRequired[str],
        "Timeout": NotRequired[int],
        "TracingConfig": NotRequired[AwsLambdaFunctionTracingConfigTypeDef],
        "VpcConfig": NotRequired[AwsLambdaFunctionVpcConfigTypeDef],
        "Version": NotRequired[str],
        "Architectures": NotRequired[Sequence[str]],
        "PackageType": NotRequired[str],
    },
)
AwsMskClusterClusterInfoClientAuthenticationDetailsPaginatorTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationDetailsPaginatorTypeDef",
    {
        "Sasl": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef],
        "Unauthenticated": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef
        ],
        "Tls": NotRequired[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsPaginatorTypeDef],
    },
)
AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef",
    {
        "Sasl": NotRequired[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef],
        "Unauthenticated": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef
        ],
        "Tls": NotRequired[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef],
    },
)
AwsOpenSearchServiceDomainDetailsPaginatorTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "AccessPolicies": NotRequired[str],
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "DomainEndpoint": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EncryptionAtRestOptions": NotRequired[
            AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef
        ],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[
            AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef
        ],
        "ClusterConfig": NotRequired[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef],
        "DomainEndpointOptions": NotRequired[
            AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef
        ],
        "VpcOptions": NotRequired[AwsOpenSearchServiceDomainVpcOptionsDetailsPaginatorTypeDef],
        "LogPublishingOptions": NotRequired[
            AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef
        ],
        "DomainEndpoints": NotRequired[Dict[str, str]],
        "AdvancedSecurityOptions": NotRequired[
            AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef
        ],
    },
)
AwsOpenSearchServiceDomainDetailsTypeDef = TypedDict(
    "AwsOpenSearchServiceDomainDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "AccessPolicies": NotRequired[str],
        "DomainName": NotRequired[str],
        "Id": NotRequired[str],
        "DomainEndpoint": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EncryptionAtRestOptions": NotRequired[
            AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef
        ],
        "NodeToNodeEncryptionOptions": NotRequired[
            AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef
        ],
        "ServiceSoftwareOptions": NotRequired[
            AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef
        ],
        "ClusterConfig": NotRequired[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef],
        "DomainEndpointOptions": NotRequired[
            AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef
        ],
        "VpcOptions": NotRequired[AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef],
        "LogPublishingOptions": NotRequired[
            AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef
        ],
        "DomainEndpoints": NotRequired[Mapping[str, str]],
        "AdvancedSecurityOptions": NotRequired[
            AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef
        ],
    },
)
AwsRdsDbSubnetGroupPaginatorTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupPaginatorTypeDef",
    {
        "DbSubnetGroupName": NotRequired[str],
        "DbSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List[AwsRdsDbSubnetGroupSubnetTypeDef]],
        "DbSubnetGroupArn": NotRequired[str],
    },
)
AwsRdsDbSubnetGroupTypeDef = TypedDict(
    "AwsRdsDbSubnetGroupTypeDef",
    {
        "DbSubnetGroupName": NotRequired[str],
        "DbSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[Sequence[AwsRdsDbSubnetGroupSubnetTypeDef]],
        "DbSubnetGroupArn": NotRequired[str],
    },
)
AwsRedshiftClusterDetailsPaginatorTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsPaginatorTypeDef",
    {
        "AllowVersionUpgrade": NotRequired[bool],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "ClusterAvailabilityStatus": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "ClusterNodes": NotRequired[List[AwsRedshiftClusterClusterNodeTypeDef]],
        "ClusterParameterGroups": NotRequired[
            List[AwsRedshiftClusterClusterParameterGroupPaginatorTypeDef]
        ],
        "ClusterPublicKey": NotRequired[str],
        "ClusterRevisionNumber": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]],
        "ClusterSnapshotCopyStatus": NotRequired[
            AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef
        ],
        "ClusterStatus": NotRequired[str],
        "ClusterSubnetGroupName": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "DBName": NotRequired[str],
        "DeferredMaintenanceWindows": NotRequired[
            List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]
        ],
        "ElasticIpStatus": NotRequired[AwsRedshiftClusterElasticIpStatusTypeDef],
        "ElasticResizeNumberOfNodeOptions": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Endpoint": NotRequired[AwsRedshiftClusterEndpointTypeDef],
        "EnhancedVpcRouting": NotRequired[bool],
        "ExpectedNextSnapshotScheduleTime": NotRequired[str],
        "ExpectedNextSnapshotScheduleTimeStatus": NotRequired[str],
        "HsmStatus": NotRequired[AwsRedshiftClusterHsmStatusTypeDef],
        "IamRoles": NotRequired[List[AwsRedshiftClusterIamRoleTypeDef]],
        "KmsKeyId": NotRequired[str],
        "MaintenanceTrackName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "NextMaintenanceWindowStartTime": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PendingActions": NotRequired[List[str]],
        "PendingModifiedValues": NotRequired[AwsRedshiftClusterPendingModifiedValuesTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ResizeInfo": NotRequired[AwsRedshiftClusterResizeInfoTypeDef],
        "RestoreStatus": NotRequired[AwsRedshiftClusterRestoreStatusTypeDef],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "SnapshotScheduleState": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroups": NotRequired[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]],
        "LoggingStatus": NotRequired[AwsRedshiftClusterLoggingStatusTypeDef],
    },
)
AwsRedshiftClusterDetailsTypeDef = TypedDict(
    "AwsRedshiftClusterDetailsTypeDef",
    {
        "AllowVersionUpgrade": NotRequired[bool],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "ClusterAvailabilityStatus": NotRequired[str],
        "ClusterCreateTime": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "ClusterNodes": NotRequired[Sequence[AwsRedshiftClusterClusterNodeTypeDef]],
        "ClusterParameterGroups": NotRequired[
            Sequence[AwsRedshiftClusterClusterParameterGroupTypeDef]
        ],
        "ClusterPublicKey": NotRequired[str],
        "ClusterRevisionNumber": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[
            Sequence[AwsRedshiftClusterClusterSecurityGroupTypeDef]
        ],
        "ClusterSnapshotCopyStatus": NotRequired[
            AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef
        ],
        "ClusterStatus": NotRequired[str],
        "ClusterSubnetGroupName": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "DBName": NotRequired[str],
        "DeferredMaintenanceWindows": NotRequired[
            Sequence[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]
        ],
        "ElasticIpStatus": NotRequired[AwsRedshiftClusterElasticIpStatusTypeDef],
        "ElasticResizeNumberOfNodeOptions": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "Endpoint": NotRequired[AwsRedshiftClusterEndpointTypeDef],
        "EnhancedVpcRouting": NotRequired[bool],
        "ExpectedNextSnapshotScheduleTime": NotRequired[str],
        "ExpectedNextSnapshotScheduleTimeStatus": NotRequired[str],
        "HsmStatus": NotRequired[AwsRedshiftClusterHsmStatusTypeDef],
        "IamRoles": NotRequired[Sequence[AwsRedshiftClusterIamRoleTypeDef]],
        "KmsKeyId": NotRequired[str],
        "MaintenanceTrackName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "NextMaintenanceWindowStartTime": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "PendingActions": NotRequired[Sequence[str]],
        "PendingModifiedValues": NotRequired[AwsRedshiftClusterPendingModifiedValuesTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ResizeInfo": NotRequired[AwsRedshiftClusterResizeInfoTypeDef],
        "RestoreStatus": NotRequired[AwsRedshiftClusterRestoreStatusTypeDef],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "SnapshotScheduleState": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence[AwsRedshiftClusterVpcSecurityGroupTypeDef]],
        "LoggingStatus": NotRequired[AwsRedshiftClusterLoggingStatusTypeDef],
    },
)
AwsRoute53HostedZoneDetailsPaginatorTypeDef = TypedDict(
    "AwsRoute53HostedZoneDetailsPaginatorTypeDef",
    {
        "HostedZone": NotRequired[AwsRoute53HostedZoneObjectDetailsTypeDef],
        "Vpcs": NotRequired[List[AwsRoute53HostedZoneVpcDetailsTypeDef]],
        "NameServers": NotRequired[List[str]],
        "QueryLoggingConfig": NotRequired[AwsRoute53QueryLoggingConfigDetailsTypeDef],
    },
)
AwsRoute53HostedZoneDetailsTypeDef = TypedDict(
    "AwsRoute53HostedZoneDetailsTypeDef",
    {
        "HostedZone": NotRequired[AwsRoute53HostedZoneObjectDetailsTypeDef],
        "Vpcs": NotRequired[Sequence[AwsRoute53HostedZoneVpcDetailsTypeDef]],
        "NameServers": NotRequired[Sequence[str]],
        "QueryLoggingConfig": NotRequired[AwsRoute53QueryLoggingConfigDetailsTypeDef],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsPaginatorTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsPaginatorTypeDef",
    {
        "Operands": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef",
    {
        "Operands": NotRequired[
            Sequence[
                AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Tag": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationFilterPaginatorTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterPaginatorTypeDef",
    {
        "S3KeyFilter": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterPaginatorTypeDef],
    },
)
AwsS3BucketNotificationConfigurationFilterTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationFilterTypeDef",
    {
        "S3KeyFilter": NotRequired[AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef],
    },
)
AwsS3BucketObjectLockConfigurationTypeDef = TypedDict(
    "AwsS3BucketObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": NotRequired[str],
        "Rule": NotRequired[AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef],
    },
)
AwsS3BucketServerSideEncryptionConfigurationPaginatorTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationPaginatorTypeDef",
    {
        "Rules": NotRequired[List[AwsS3BucketServerSideEncryptionRuleTypeDef]],
    },
)
AwsS3BucketServerSideEncryptionConfigurationTypeDef = TypedDict(
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": NotRequired[Sequence[AwsS3BucketServerSideEncryptionRuleTypeDef]],
    },
)
AwsS3BucketWebsiteConfigurationPaginatorTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationPaginatorTypeDef",
    {
        "ErrorDocument": NotRequired[str],
        "IndexDocumentSuffix": NotRequired[str],
        "RedirectAllRequestsTo": NotRequired[AwsS3BucketWebsiteConfigurationRedirectToTypeDef],
        "RoutingRules": NotRequired[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]],
    },
)
AwsS3BucketWebsiteConfigurationTypeDef = TypedDict(
    "AwsS3BucketWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": NotRequired[str],
        "IndexDocumentSuffix": NotRequired[str],
        "RedirectAllRequestsTo": NotRequired[AwsS3BucketWebsiteConfigurationRedirectToTypeDef],
        "RoutingRules": NotRequired[Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]],
    },
)
BatchUpdateFindingsResponseTypeDef = TypedDict(
    "BatchUpdateFindingsResponseTypeDef",
    {
        "ProcessedFindings": List[AwsSecurityFindingIdentifierTypeDef],
        "UnprocessedFindings": List[BatchUpdateFindingsUnprocessedFindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AwsSsmPatchComplianceDetailsTypeDef = TypedDict(
    "AwsSsmPatchComplianceDetailsTypeDef",
    {
        "Patch": NotRequired[AwsSsmPatchTypeDef],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsPaginatorTypeDef",
    {
        "Destinations": NotRequired[
            List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]
        ],
        "IncludeExecutionData": NotRequired[bool],
        "Level": NotRequired[str],
    },
)
AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef",
    {
        "Destinations": NotRequired[
            Sequence[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]
        ],
        "IncludeExecutionData": NotRequired[bool],
        "Level": NotRequired[str],
    },
)
AwsWafRegionalRuleGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupDetailsPaginatorTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafRegionalRuleGroupDetailsTypeDef = TypedDict(
    "AwsWafRegionalRuleGroupDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafRegionalRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafRegionalWebAclDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRegionalWebAclDetailsPaginatorTypeDef",
    {
        "DefaultAction": NotRequired[str],
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RulesList": NotRequired[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafRegionalWebAclDetailsTypeDef = TypedDict(
    "AwsWafRegionalWebAclDetailsTypeDef",
    {
        "DefaultAction": NotRequired[str],
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RulesList": NotRequired[Sequence[AwsWafRegionalWebAclRulesListDetailsTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafRuleGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsWafRuleGroupDetailsPaginatorTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[List[AwsWafRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafRuleGroupDetailsTypeDef = TypedDict(
    "AwsWafRuleGroupDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "Name": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafRuleGroupRulesDetailsTypeDef]],
    },
)
AwsWafWebAclDetailsPaginatorTypeDef = TypedDict(
    "AwsWafWebAclDetailsPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "Rules": NotRequired[List[AwsWafWebAclRulePaginatorTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafWebAclDetailsTypeDef = TypedDict(
    "AwsWafWebAclDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultAction": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafWebAclRuleTypeDef]],
        "WebAclId": NotRequired[str],
    },
)
AwsWafv2ActionAllowDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2ActionAllowDetailsPaginatorTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsPaginatorTypeDef],
    },
)
AwsWafv2RulesActionCaptchaDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2RulesActionCaptchaDetailsPaginatorTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsPaginatorTypeDef],
    },
)
AwsWafv2RulesActionCountDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2RulesActionCountDetailsPaginatorTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsPaginatorTypeDef],
    },
)
AwsWafv2ActionAllowDetailsTypeDef = TypedDict(
    "AwsWafv2ActionAllowDetailsTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsTypeDef],
    },
)
AwsWafv2RulesActionCaptchaDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionCaptchaDetailsTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsTypeDef],
    },
)
AwsWafv2RulesActionCountDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionCountDetailsTypeDef",
    {
        "CustomRequestHandling": NotRequired[AwsWafv2CustomRequestHandlingDetailsTypeDef],
    },
)
AwsWafv2ActionBlockDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2ActionBlockDetailsPaginatorTypeDef",
    {
        "CustomResponse": NotRequired[AwsWafv2CustomResponseDetailsPaginatorTypeDef],
    },
)
AwsWafv2ActionBlockDetailsTypeDef = TypedDict(
    "AwsWafv2ActionBlockDetailsTypeDef",
    {
        "CustomResponse": NotRequired[AwsWafv2CustomResponseDetailsTypeDef],
    },
)
BatchGetStandardsControlAssociationsResponseTypeDef = TypedDict(
    "BatchGetStandardsControlAssociationsResponseTypeDef",
    {
        "StandardsControlAssociationDetails": List[StandardsControlAssociationDetailTypeDef],
        "UnprocessedAssociations": List[UnprocessedStandardsControlAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateStandardsControlAssociationsResponseTypeDef = TypedDict(
    "BatchUpdateStandardsControlAssociationsResponseTypeDef",
    {
        "UnprocessedAssociationUpdates": List[UnprocessedStandardsControlAssociationUpdateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VulnerabilityPaginatorTypeDef = TypedDict(
    "VulnerabilityPaginatorTypeDef",
    {
        "Id": str,
        "VulnerablePackages": NotRequired[List[SoftwarePackageTypeDef]],
        "Cvss": NotRequired[List[CvssPaginatorTypeDef]],
        "RelatedVulnerabilities": NotRequired[List[str]],
        "Vendor": NotRequired[VulnerabilityVendorTypeDef],
        "ReferenceUrls": NotRequired[List[str]],
        "FixAvailable": NotRequired[VulnerabilityFixAvailableType],
        "EpssScore": NotRequired[float],
        "ExploitAvailable": NotRequired[VulnerabilityExploitAvailableType],
        "CodeVulnerabilities": NotRequired[List[VulnerabilityCodeVulnerabilitiesPaginatorTypeDef]],
    },
)
VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "Id": str,
        "VulnerablePackages": NotRequired[Sequence[SoftwarePackageTypeDef]],
        "Cvss": NotRequired[Sequence[CvssTypeDef]],
        "RelatedVulnerabilities": NotRequired[Sequence[str]],
        "Vendor": NotRequired[VulnerabilityVendorTypeDef],
        "ReferenceUrls": NotRequired[Sequence[str]],
        "FixAvailable": NotRequired[VulnerabilityFixAvailableType],
        "EpssScore": NotRequired[float],
        "ExploitAvailable": NotRequired[VulnerabilityExploitAvailableType],
        "CodeVulnerabilities": NotRequired[Sequence[VulnerabilityCodeVulnerabilitiesTypeDef]],
    },
)
ParameterDefinitionTypeDef = TypedDict(
    "ParameterDefinitionTypeDef",
    {
        "Description": str,
        "ConfigurationOptions": ConfigurationOptionsTypeDef,
    },
)
BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef = TypedDict(
    "BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef",
    {
        "ConfigurationPolicyAssociationIdentifiers": Sequence[
            ConfigurationPolicyAssociationTypeDef
        ],
    },
)
UnprocessedConfigurationPolicyAssociationTypeDef = TypedDict(
    "UnprocessedConfigurationPolicyAssociationTypeDef",
    {
        "ConfigurationPolicyAssociationIdentifiers": NotRequired[
            ConfigurationPolicyAssociationTypeDef
        ],
        "ErrorCode": NotRequired[str],
        "ErrorReason": NotRequired[str],
    },
)
AutomationRulesFindingFiltersTypeDef = TypedDict(
    "AutomationRulesFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[List[StringFilterTypeDef]],
        "Id": NotRequired[List[StringFilterTypeDef]],
        "GeneratorId": NotRequired[List[StringFilterTypeDef]],
        "Type": NotRequired[List[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[List[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[List[DateFilterTypeDef]],
        "CreatedAt": NotRequired[List[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "Confidence": NotRequired[List[NumberFilterTypeDef]],
        "Criticality": NotRequired[List[NumberFilterTypeDef]],
        "Title": NotRequired[List[StringFilterTypeDef]],
        "Description": NotRequired[List[StringFilterTypeDef]],
        "SourceUrl": NotRequired[List[StringFilterTypeDef]],
        "ProductName": NotRequired[List[StringFilterTypeDef]],
        "CompanyName": NotRequired[List[StringFilterTypeDef]],
        "SeverityLabel": NotRequired[List[StringFilterTypeDef]],
        "ResourceType": NotRequired[List[StringFilterTypeDef]],
        "ResourceId": NotRequired[List[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[List[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[List[StringFilterTypeDef]],
        "ResourceTags": NotRequired[List[MapFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[List[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[List[StringFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[List[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[List[StringFilterTypeDef]],
        "VerificationState": NotRequired[List[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[List[StringFilterTypeDef]],
        "RecordState": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[List[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[List[StringFilterTypeDef]],
        "NoteText": NotRequired[List[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[List[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[List[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[List[MapFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[List[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[List[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[List[StringFilterTypeDef]],
    },
)
AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountId": NotRequired[Sequence[StringFilterTypeDef]],
        "Id": NotRequired[Sequence[StringFilterTypeDef]],
        "GeneratorId": NotRequired[Sequence[StringFilterTypeDef]],
        "Region": NotRequired[Sequence[StringFilterTypeDef]],
        "Type": NotRequired[Sequence[StringFilterTypeDef]],
        "FirstObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "LastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "CreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "UpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "SeverityProduct": NotRequired[Sequence[NumberFilterTypeDef]],
        "SeverityNormalized": NotRequired[Sequence[NumberFilterTypeDef]],
        "SeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "Confidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "Criticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "Title": NotRequired[Sequence[StringFilterTypeDef]],
        "Description": NotRequired[Sequence[StringFilterTypeDef]],
        "RecommendationText": NotRequired[Sequence[StringFilterTypeDef]],
        "SourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ProductFields": NotRequired[Sequence[MapFilterTypeDef]],
        "ProductName": NotRequired[Sequence[StringFilterTypeDef]],
        "CompanyName": NotRequired[Sequence[StringFilterTypeDef]],
        "UserDefinedFields": NotRequired[Sequence[MapFilterTypeDef]],
        "MalwareName": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwareType": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwarePath": NotRequired[Sequence[StringFilterTypeDef]],
        "MalwareState": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkDirection": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkProtocol": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkSourceIpV4": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkSourceIpV6": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkSourcePort": NotRequired[Sequence[NumberFilterTypeDef]],
        "NetworkSourceDomain": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkSourceMac": NotRequired[Sequence[StringFilterTypeDef]],
        "NetworkDestinationIpV4": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkDestinationIpV6": NotRequired[Sequence[IpFilterTypeDef]],
        "NetworkDestinationPort": NotRequired[Sequence[NumberFilterTypeDef]],
        "NetworkDestinationDomain": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessName": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessPath": NotRequired[Sequence[StringFilterTypeDef]],
        "ProcessPid": NotRequired[Sequence[NumberFilterTypeDef]],
        "ProcessParentPid": NotRequired[Sequence[NumberFilterTypeDef]],
        "ProcessLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ProcessTerminatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ThreatIntelIndicatorType": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorValue": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorCategory": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorLastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ThreatIntelIndicatorSource": NotRequired[Sequence[StringFilterTypeDef]],
        "ThreatIntelIndicatorSourceUrl": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourcePartition": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceRegion": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "ResourceAwsEc2InstanceType": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV4Addresses": NotRequired[Sequence[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceIpV6Addresses": NotRequired[Sequence[IpFilterTypeDef]],
        "ResourceAwsEc2InstanceKeyName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceVpcId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceSubnetId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsEc2InstanceLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceAwsS3BucketOwnerId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsS3BucketOwnerName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyUserName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyPrincipalName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceAwsIamAccessKeyCreatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceAwsIamUserUserName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerImageName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceContainerLaunchedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "ResourceDetailsOther": NotRequired[Sequence[MapFilterTypeDef]],
        "ComplianceStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "VerificationState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowState": NotRequired[Sequence[StringFilterTypeDef]],
        "WorkflowStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "RecordState": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsProductArn": NotRequired[Sequence[StringFilterTypeDef]],
        "RelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteText": NotRequired[Sequence[StringFilterTypeDef]],
        "NoteUpdatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "NoteUpdatedBy": NotRequired[Sequence[StringFilterTypeDef]],
        "Keyword": NotRequired[Sequence[KeywordFilterTypeDef]],
        "FindingProviderFieldsConfidence": NotRequired[Sequence[NumberFilterTypeDef]],
        "FindingProviderFieldsCriticality": NotRequired[Sequence[NumberFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsId": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsRelatedFindingsProductArn": NotRequired[
            Sequence[StringFilterTypeDef]
        ],
        "FindingProviderFieldsSeverityLabel": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsSeverityOriginal": NotRequired[Sequence[StringFilterTypeDef]],
        "FindingProviderFieldsTypes": NotRequired[Sequence[StringFilterTypeDef]],
        "Sample": NotRequired[Sequence[BooleanFilterTypeDef]],
        "ComplianceSecurityControlId": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceAssociatedStandardsId": NotRequired[Sequence[StringFilterTypeDef]],
        "VulnerabilitiesExploitAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "VulnerabilitiesFixAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersName": NotRequired[Sequence[StringFilterTypeDef]],
        "ComplianceSecurityControlParametersValue": NotRequired[Sequence[StringFilterTypeDef]],
        "AwsAccountName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationName": NotRequired[Sequence[StringFilterTypeDef]],
        "ResourceApplicationArn": NotRequired[Sequence[StringFilterTypeDef]],
    },
)
GetFindingHistoryResponseTypeDef = TypedDict(
    "GetFindingHistoryResponseTypeDef",
    {
        "Records": List[FindingHistoryRecordTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightResultsResponseTypeDef = TypedDict(
    "GetInsightResultsResponseTypeDef",
    {
        "InsightResults": InsightResultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkHeaderPaginatorTypeDef = TypedDict(
    "NetworkHeaderPaginatorTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired[NetworkPathComponentDetailsPaginatorTypeDef],
        "Source": NotRequired[NetworkPathComponentDetailsPaginatorTypeDef],
    },
)
NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": NotRequired[str],
        "Destination": NotRequired[NetworkPathComponentDetailsTypeDef],
        "Source": NotRequired[NetworkPathComponentDetailsTypeDef],
    },
)
OccurrencesPaginatorTypeDef = TypedDict(
    "OccurrencesPaginatorTypeDef",
    {
        "LineRanges": NotRequired[List[RangeTypeDef]],
        "OffsetRanges": NotRequired[List[RangeTypeDef]],
        "Pages": NotRequired[List[PageTypeDef]],
        "Records": NotRequired[List[RecordTypeDef]],
        "Cells": NotRequired[List[CellTypeDef]],
    },
)
OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "LineRanges": NotRequired[Sequence[RangeTypeDef]],
        "OffsetRanges": NotRequired[Sequence[RangeTypeDef]],
        "Pages": NotRequired[Sequence[PageTypeDef]],
        "Records": NotRequired[Sequence[RecordTypeDef]],
        "Cells": NotRequired[Sequence[CellTypeDef]],
    },
)
SecurityControlCustomParameterTypeDef = TypedDict(
    "SecurityControlCustomParameterTypeDef",
    {
        "SecurityControlId": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, ParameterConfigurationTypeDef]],
    },
)
SecurityControlTypeDef = TypedDict(
    "SecurityControlTypeDef",
    {
        "SecurityControlId": str,
        "SecurityControlArn": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "SecurityControlStatus": ControlStatusType,
        "UpdateStatus": NotRequired[UpdateStatusType],
        "Parameters": NotRequired[Dict[str, ParameterConfigurationTypeDef]],
        "LastUpdateReason": NotRequired[str],
    },
)
UpdateSecurityControlRequestRequestTypeDef = TypedDict(
    "UpdateSecurityControlRequestRequestTypeDef",
    {
        "SecurityControlId": str,
        "Parameters": Mapping[str, ParameterConfigurationTypeDef],
        "LastUpdateReason": NotRequired[str],
    },
)
RuleGroupSourceStatelessRuleDefinitionPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionPaginatorTypeDef",
    {
        "Actions": NotRequired[List[str]],
        "MatchAttributes": NotRequired[RuleGroupSourceStatelessRuleMatchAttributesPaginatorTypeDef],
    },
)
RuleGroupSourceStatelessRuleDefinitionTypeDef = TypedDict(
    "RuleGroupSourceStatelessRuleDefinitionTypeDef",
    {
        "Actions": NotRequired[Sequence[str]],
        "MatchAttributes": NotRequired[RuleGroupSourceStatelessRuleMatchAttributesTypeDef],
    },
)
DescribeStandardsResponseTypeDef = TypedDict(
    "DescribeStandardsResponseTypeDef",
    {
        "Standards": List[StandardTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisableStandardsResponseTypeDef = TypedDict(
    "BatchDisableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEnableStandardsResponseTypeDef = TypedDict(
    "BatchEnableStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnabledStandardsResponseTypeDef = TypedDict(
    "GetEnabledStandardsResponseTypeDef",
    {
        "StandardsSubscriptions": List[StandardsSubscriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StatelessCustomActionDefinitionPaginatorTypeDef = TypedDict(
    "StatelessCustomActionDefinitionPaginatorTypeDef",
    {
        "PublishMetricAction": NotRequired[StatelessCustomPublishMetricActionPaginatorTypeDef],
    },
)
StatelessCustomActionDefinitionTypeDef = TypedDict(
    "StatelessCustomActionDefinitionTypeDef",
    {
        "PublishMetricAction": NotRequired[StatelessCustomPublishMetricActionTypeDef],
    },
)
PortProbeActionPaginatorTypeDef = TypedDict(
    "PortProbeActionPaginatorTypeDef",
    {
        "PortProbeDetails": NotRequired[List[PortProbeDetailTypeDef]],
        "Blocked": NotRequired[bool],
    },
)
PortProbeActionTypeDef = TypedDict(
    "PortProbeActionTypeDef",
    {
        "PortProbeDetails": NotRequired[Sequence[PortProbeDetailTypeDef]],
        "Blocked": NotRequired[bool],
    },
)
AwsAthenaWorkGroupDetailsTypeDef = TypedDict(
    "AwsAthenaWorkGroupDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[str],
        "Configuration": NotRequired[AwsAthenaWorkGroupConfigurationDetailsTypeDef],
    },
)
AwsAutoScalingAutoScalingGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsPaginatorTypeDef",
    {
        "LaunchConfigurationName": NotRequired[str],
        "LoadBalancerNames": NotRequired[List[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "CreatedTime": NotRequired[str],
        "MixedInstancesPolicy": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsPaginatorTypeDef
        ],
        "AvailabilityZones": NotRequired[
            List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "CapacityRebalance": NotRequired[bool],
    },
)
AwsAutoScalingAutoScalingGroupDetailsTypeDef = TypedDict(
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    {
        "LaunchConfigurationName": NotRequired[str],
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "CreatedTime": NotRequired[str],
        "MixedInstancesPolicy": NotRequired[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef
        ],
        "AvailabilityZones": NotRequired[
            Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]
        ],
        "LaunchTemplate": NotRequired[
            AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef
        ],
        "CapacityRebalance": NotRequired[bool],
    },
)
AwsBackupBackupPlanBackupPlanDetailsPaginatorTypeDef = TypedDict(
    "AwsBackupBackupPlanBackupPlanDetailsPaginatorTypeDef",
    {
        "BackupPlanName": NotRequired[str],
        "AdvancedBackupSettings": NotRequired[
            List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsPaginatorTypeDef]
        ],
        "BackupPlanRule": NotRequired[List[AwsBackupBackupPlanRuleDetailsPaginatorTypeDef]],
    },
)
AwsBackupBackupPlanBackupPlanDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanBackupPlanDetailsTypeDef",
    {
        "BackupPlanName": NotRequired[str],
        "AdvancedBackupSettings": NotRequired[
            Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef]
        ],
        "BackupPlanRule": NotRequired[Sequence[AwsBackupBackupPlanRuleDetailsTypeDef]],
    },
)
AwsCertificateManagerCertificateDetailsPaginatorTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsPaginatorTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            List[AwsCertificateManagerCertificateDomainValidationOptionPaginatorTypeDef]
        ],
        "ExtendedKeyUsages": NotRequired[
            List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[List[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[List[AwsCertificateManagerCertificateKeyUsageTypeDef]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired[AwsCertificateManagerCertificateOptionsTypeDef],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired[
            AwsCertificateManagerCertificateRenewalSummaryPaginatorTypeDef
        ],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[List[str]],
        "Type": NotRequired[str],
    },
)
AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "DomainValidationOptions": NotRequired[
            Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]
        ],
        "ExtendedKeyUsages": NotRequired[
            Sequence[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]
        ],
        "FailureReason": NotRequired[str],
        "ImportedAt": NotRequired[str],
        "InUseBy": NotRequired[Sequence[str]],
        "IssuedAt": NotRequired[str],
        "Issuer": NotRequired[str],
        "KeyAlgorithm": NotRequired[str],
        "KeyUsages": NotRequired[Sequence[AwsCertificateManagerCertificateKeyUsageTypeDef]],
        "NotAfter": NotRequired[str],
        "NotBefore": NotRequired[str],
        "Options": NotRequired[AwsCertificateManagerCertificateOptionsTypeDef],
        "RenewalEligibility": NotRequired[str],
        "RenewalSummary": NotRequired[AwsCertificateManagerCertificateRenewalSummaryTypeDef],
        "Serial": NotRequired[str],
        "SignatureAlgorithm": NotRequired[str],
        "Status": NotRequired[str],
        "Subject": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[Sequence[str]],
        "Type": NotRequired[str],
    },
)
AwsCloudFrontDistributionOriginsPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsPaginatorTypeDef",
    {
        "Items": NotRequired[List[AwsCloudFrontDistributionOriginItemPaginatorTypeDef]],
    },
)
AwsCloudFrontDistributionOriginsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginsTypeDef",
    {
        "Items": NotRequired[Sequence[AwsCloudFrontDistributionOriginItemTypeDef]],
    },
)
AwsCloudFrontDistributionOriginGroupsPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsPaginatorTypeDef",
    {
        "Items": NotRequired[List[AwsCloudFrontDistributionOriginGroupPaginatorTypeDef]],
    },
)
AwsCloudFrontDistributionOriginGroupsTypeDef = TypedDict(
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    {
        "Items": NotRequired[Sequence[AwsCloudFrontDistributionOriginGroupTypeDef]],
    },
)
AwsDynamoDbTableDetailsPaginatorTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsPaginatorTypeDef",
    {
        "AttributeDefinitions": NotRequired[List[AwsDynamoDbTableAttributeDefinitionTypeDef]],
        "BillingModeSummary": NotRequired[AwsDynamoDbTableBillingModeSummaryTypeDef],
        "CreationDateTime": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableGlobalSecondaryIndexPaginatorTypeDef]
        ],
        "GlobalTableVersion": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[List[AwsDynamoDbTableKeySchemaTypeDef]],
        "LatestStreamArn": NotRequired[str],
        "LatestStreamLabel": NotRequired[str],
        "LocalSecondaryIndexes": NotRequired[
            List[AwsDynamoDbTableLocalSecondaryIndexPaginatorTypeDef]
        ],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
        "Replicas": NotRequired[List[AwsDynamoDbTableReplicaPaginatorTypeDef]],
        "RestoreSummary": NotRequired[AwsDynamoDbTableRestoreSummaryTypeDef],
        "SseDescription": NotRequired[AwsDynamoDbTableSseDescriptionTypeDef],
        "StreamSpecification": NotRequired[AwsDynamoDbTableStreamSpecificationTypeDef],
        "TableId": NotRequired[str],
        "TableName": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "TableStatus": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
AwsDynamoDbTableDetailsTypeDef = TypedDict(
    "AwsDynamoDbTableDetailsTypeDef",
    {
        "AttributeDefinitions": NotRequired[Sequence[AwsDynamoDbTableAttributeDefinitionTypeDef]],
        "BillingModeSummary": NotRequired[AwsDynamoDbTableBillingModeSummaryTypeDef],
        "CreationDateTime": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            Sequence[AwsDynamoDbTableGlobalSecondaryIndexTypeDef]
        ],
        "GlobalTableVersion": NotRequired[str],
        "ItemCount": NotRequired[int],
        "KeySchema": NotRequired[Sequence[AwsDynamoDbTableKeySchemaTypeDef]],
        "LatestStreamArn": NotRequired[str],
        "LatestStreamLabel": NotRequired[str],
        "LocalSecondaryIndexes": NotRequired[Sequence[AwsDynamoDbTableLocalSecondaryIndexTypeDef]],
        "ProvisionedThroughput": NotRequired[AwsDynamoDbTableProvisionedThroughputTypeDef],
        "Replicas": NotRequired[Sequence[AwsDynamoDbTableReplicaTypeDef]],
        "RestoreSummary": NotRequired[AwsDynamoDbTableRestoreSummaryTypeDef],
        "SseDescription": NotRequired[AwsDynamoDbTableSseDescriptionTypeDef],
        "StreamSpecification": NotRequired[AwsDynamoDbTableStreamSpecificationTypeDef],
        "TableId": NotRequired[str],
        "TableName": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "TableStatus": NotRequired[str],
        "DeletionProtectionEnabled": NotRequired[bool],
    },
)
AwsEc2LaunchTemplateDetailsPaginatorTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDetailsPaginatorTypeDef",
    {
        "LaunchTemplateName": NotRequired[str],
        "Id": NotRequired[str],
        "LaunchTemplateData": NotRequired[AwsEc2LaunchTemplateDataDetailsPaginatorTypeDef],
        "DefaultVersionNumber": NotRequired[int],
        "LatestVersionNumber": NotRequired[int],
    },
)
AwsEc2LaunchTemplateDetailsTypeDef = TypedDict(
    "AwsEc2LaunchTemplateDetailsTypeDef",
    {
        "LaunchTemplateName": NotRequired[str],
        "Id": NotRequired[str],
        "LaunchTemplateData": NotRequired[AwsEc2LaunchTemplateDataDetailsTypeDef],
        "DefaultVersionNumber": NotRequired[int],
        "LatestVersionNumber": NotRequired[int],
    },
)
AwsEcsClusterDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsClusterDetailsPaginatorTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ActiveServicesCount": NotRequired[int],
        "CapacityProviders": NotRequired[List[str]],
        "ClusterSettings": NotRequired[List[AwsEcsClusterClusterSettingsDetailsTypeDef]],
        "Configuration": NotRequired[AwsEcsClusterConfigurationDetailsTypeDef],
        "DefaultCapacityProviderStrategy": NotRequired[
            List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]
        ],
        "ClusterName": NotRequired[str],
        "RegisteredContainerInstancesCount": NotRequired[int],
        "RunningTasksCount": NotRequired[int],
        "Status": NotRequired[str],
    },
)
AwsEcsClusterDetailsTypeDef = TypedDict(
    "AwsEcsClusterDetailsTypeDef",
    {
        "ClusterArn": NotRequired[str],
        "ActiveServicesCount": NotRequired[int],
        "CapacityProviders": NotRequired[Sequence[str]],
        "ClusterSettings": NotRequired[Sequence[AwsEcsClusterClusterSettingsDetailsTypeDef]],
        "Configuration": NotRequired[AwsEcsClusterConfigurationDetailsTypeDef],
        "DefaultCapacityProviderStrategy": NotRequired[
            Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]
        ],
        "ClusterName": NotRequired[str],
        "RegisteredContainerInstancesCount": NotRequired[int],
        "RunningTasksCount": NotRequired[int],
        "Status": NotRequired[str],
    },
)
AwsEcsTaskDefinitionDetailsPaginatorTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsPaginatorTypeDef",
    {
        "ContainerDefinitions": NotRequired[
            List[AwsEcsTaskDefinitionContainerDefinitionsDetailsPaginatorTypeDef]
        ],
        "Cpu": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "Family": NotRequired[str],
        "InferenceAccelerators": NotRequired[
            List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]
        ],
        "IpcMode": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkMode": NotRequired[str],
        "PidMode": NotRequired[str],
        "PlacementConstraints": NotRequired[
            List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]
        ],
        "ProxyConfiguration": NotRequired[
            AwsEcsTaskDefinitionProxyConfigurationDetailsPaginatorTypeDef
        ],
        "RequiresCompatibilities": NotRequired[List[str]],
        "TaskRoleArn": NotRequired[str],
        "Volumes": NotRequired[List[AwsEcsTaskDefinitionVolumesDetailsPaginatorTypeDef]],
        "Status": NotRequired[str],
    },
)
AwsEcsTaskDefinitionDetailsTypeDef = TypedDict(
    "AwsEcsTaskDefinitionDetailsTypeDef",
    {
        "ContainerDefinitions": NotRequired[
            Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef]
        ],
        "Cpu": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
        "Family": NotRequired[str],
        "InferenceAccelerators": NotRequired[
            Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]
        ],
        "IpcMode": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkMode": NotRequired[str],
        "PidMode": NotRequired[str],
        "PlacementConstraints": NotRequired[
            Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]
        ],
        "ProxyConfiguration": NotRequired[AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef],
        "RequiresCompatibilities": NotRequired[Sequence[str]],
        "TaskRoleArn": NotRequired[str],
        "Volumes": NotRequired[Sequence[AwsEcsTaskDefinitionVolumesDetailsTypeDef]],
        "Status": NotRequired[str],
    },
)
AwsEventsEndpointDetailsPaginatorTypeDef = TypedDict(
    "AwsEventsEndpointDetailsPaginatorTypeDef",
    {
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointId": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EventBuses": NotRequired[List[AwsEventsEndpointEventBusesDetailsTypeDef]],
        "Name": NotRequired[str],
        "ReplicationConfig": NotRequired[AwsEventsEndpointReplicationConfigDetailsTypeDef],
        "RoleArn": NotRequired[str],
        "RoutingConfig": NotRequired[AwsEventsEndpointRoutingConfigDetailsTypeDef],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
AwsEventsEndpointDetailsTypeDef = TypedDict(
    "AwsEventsEndpointDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointId": NotRequired[str],
        "EndpointUrl": NotRequired[str],
        "EventBuses": NotRequired[Sequence[AwsEventsEndpointEventBusesDetailsTypeDef]],
        "Name": NotRequired[str],
        "ReplicationConfig": NotRequired[AwsEventsEndpointReplicationConfigDetailsTypeDef],
        "RoleArn": NotRequired[str],
        "RoutingConfig": NotRequired[AwsEventsEndpointRoutingConfigDetailsTypeDef],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
AwsGuardDutyDetectorDataSourcesDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDataSourcesDetailsTypeDef",
    {
        "CloudTrail": NotRequired[AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef],
        "DnsLogs": NotRequired[AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef],
        "FlowLogs": NotRequired[AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef],
        "Kubernetes": NotRequired[AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef],
        "MalwareProtection": NotRequired[
            AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef
        ],
        "S3Logs": NotRequired[AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef],
    },
)
AwsMskClusterClusterInfoDetailsPaginatorTypeDef = TypedDict(
    "AwsMskClusterClusterInfoDetailsPaginatorTypeDef",
    {
        "EncryptionInfo": NotRequired[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef],
        "CurrentVersion": NotRequired[str],
        "NumberOfBrokerNodes": NotRequired[int],
        "ClusterName": NotRequired[str],
        "ClientAuthentication": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationDetailsPaginatorTypeDef
        ],
        "EnhancedMonitoring": NotRequired[str],
    },
)
AwsMskClusterClusterInfoDetailsTypeDef = TypedDict(
    "AwsMskClusterClusterInfoDetailsTypeDef",
    {
        "EncryptionInfo": NotRequired[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef],
        "CurrentVersion": NotRequired[str],
        "NumberOfBrokerNodes": NotRequired[int],
        "ClusterName": NotRequired[str],
        "ClientAuthentication": NotRequired[
            AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef
        ],
        "EnhancedMonitoring": NotRequired[str],
    },
)
AwsRdsDbInstanceDetailsPaginatorTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsPaginatorTypeDef",
    {
        "AssociatedRoles": NotRequired[List[AwsRdsDbInstanceAssociatedRoleTypeDef]],
        "CACertificateIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DbiResourceId": NotRequired[str],
        "DBName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "Endpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "InstanceCreateTime": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StorageEncrypted": NotRequired[bool],
        "TdeCredentialArn": NotRequired[str],
        "VpcSecurityGroups": NotRequired[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "MultiAz": NotRequired[bool],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "DbInstanceStatus": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DbSecurityGroups": NotRequired[List[str]],
        "DbParameterGroups": NotRequired[List[AwsRdsDbParameterGroupTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DbSubnetGroup": NotRequired[AwsRdsDbSubnetGroupPaginatorTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[AwsRdsDbPendingModifiedValuesPaginatorTypeDef],
        "LatestRestorableTime": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[List[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[List[str]],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[List[AwsRdsDbOptionGroupMembershipTypeDef]],
        "CharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "StatusInfos": NotRequired[List[AwsRdsDbStatusInfoTypeDef]],
        "StorageType": NotRequired[str],
        "DomainMemberships": NotRequired[List[AwsRdsDbDomainMembershipTypeDef]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKmsKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudWatchLogsExports": NotRequired[List[str]],
        "ProcessorFeatures": NotRequired[List[AwsRdsDbProcessorFeatureTypeDef]],
        "ListenerEndpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "MaxAllocatedStorage": NotRequired[int],
    },
)
AwsRdsDbInstanceDetailsTypeDef = TypedDict(
    "AwsRdsDbInstanceDetailsTypeDef",
    {
        "AssociatedRoles": NotRequired[Sequence[AwsRdsDbInstanceAssociatedRoleTypeDef]],
        "CACertificateIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DbiResourceId": NotRequired[str],
        "DBName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "Endpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "InstanceCreateTime": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StorageEncrypted": NotRequired[bool],
        "TdeCredentialArn": NotRequired[str],
        "VpcSecurityGroups": NotRequired[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]],
        "MultiAz": NotRequired[bool],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "DbInstanceStatus": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DbSecurityGroups": NotRequired[Sequence[str]],
        "DbParameterGroups": NotRequired[Sequence[AwsRdsDbParameterGroupTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DbSubnetGroup": NotRequired[AwsRdsDbSubnetGroupTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[AwsRdsDbPendingModifiedValuesTypeDef],
        "LatestRestorableTime": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[Sequence[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[Sequence[str]],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[Sequence[AwsRdsDbOptionGroupMembershipTypeDef]],
        "CharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "StatusInfos": NotRequired[Sequence[AwsRdsDbStatusInfoTypeDef]],
        "StorageType": NotRequired[str],
        "DomainMemberships": NotRequired[Sequence[AwsRdsDbDomainMembershipTypeDef]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKmsKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudWatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence[AwsRdsDbProcessorFeatureTypeDef]],
        "ListenerEndpoint": NotRequired[AwsRdsDbInstanceEndpointTypeDef],
        "MaxAllocatedStorage": NotRequired[int],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsPaginatorTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsPaginatorTypeDef",
    {
        "Predicate": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsPaginatorTypeDef
        ],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef",
    {
        "Predicate": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef
        ],
    },
)
AwsS3BucketNotificationConfigurationDetailPaginatorTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailPaginatorTypeDef",
    {
        "Events": NotRequired[List[str]],
        "Filter": NotRequired[AwsS3BucketNotificationConfigurationFilterPaginatorTypeDef],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsS3BucketNotificationConfigurationDetailTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationDetailTypeDef",
    {
        "Events": NotRequired[Sequence[str]],
        "Filter": NotRequired[AwsS3BucketNotificationConfigurationFilterTypeDef],
        "Destination": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsStepFunctionStateMachineDetailsPaginatorTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsPaginatorTypeDef",
    {
        "Label": NotRequired[str],
        "LoggingConfiguration": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDetailsPaginatorTypeDef
        ],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StateMachineArn": NotRequired[str],
        "Status": NotRequired[str],
        "TracingConfiguration": NotRequired[
            AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsStepFunctionStateMachineDetailsTypeDef = TypedDict(
    "AwsStepFunctionStateMachineDetailsTypeDef",
    {
        "Label": NotRequired[str],
        "LoggingConfiguration": NotRequired[
            AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef
        ],
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "StateMachineArn": NotRequired[str],
        "Status": NotRequired[str],
        "TracingConfiguration": NotRequired[
            AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef
        ],
        "Type": NotRequired[str],
    },
)
AwsWafv2RulesActionDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2RulesActionDetailsPaginatorTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsPaginatorTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsPaginatorTypeDef],
        "Captcha": NotRequired[AwsWafv2RulesActionCaptchaDetailsPaginatorTypeDef],
        "Count": NotRequired[AwsWafv2RulesActionCountDetailsPaginatorTypeDef],
    },
)
AwsWafv2WebAclActionDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2WebAclActionDetailsPaginatorTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsPaginatorTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsPaginatorTypeDef],
    },
)
AwsWafv2RulesActionDetailsTypeDef = TypedDict(
    "AwsWafv2RulesActionDetailsTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsTypeDef],
        "Captcha": NotRequired[AwsWafv2RulesActionCaptchaDetailsTypeDef],
        "Count": NotRequired[AwsWafv2RulesActionCountDetailsTypeDef],
    },
)
AwsWafv2WebAclActionDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclActionDetailsTypeDef",
    {
        "Allow": NotRequired[AwsWafv2ActionAllowDetailsTypeDef],
        "Block": NotRequired[AwsWafv2ActionBlockDetailsTypeDef],
    },
)
SecurityControlDefinitionTypeDef = TypedDict(
    "SecurityControlDefinitionTypeDef",
    {
        "SecurityControlId": str,
        "Title": str,
        "Description": str,
        "RemediationUrl": str,
        "SeverityRating": SeverityRatingType,
        "CurrentRegionAvailability": RegionAvailabilityStatusType,
        "CustomizableProperties": NotRequired[List[Literal["Parameters"]]],
        "ParameterDefinitions": NotRequired[Dict[str, ParameterDefinitionTypeDef]],
    },
)
BatchGetConfigurationPolicyAssociationsResponseTypeDef = TypedDict(
    "BatchGetConfigurationPolicyAssociationsResponseTypeDef",
    {
        "ConfigurationPolicyAssociations": List[ConfigurationPolicyAssociationSummaryTypeDef],
        "UnprocessedConfigurationPolicyAssociations": List[
            UnprocessedConfigurationPolicyAssociationTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutomationRulesConfigTypeDef = TypedDict(
    "AutomationRulesConfigTypeDef",
    {
        "RuleArn": NotRequired[str],
        "RuleStatus": NotRequired[RuleStatusType],
        "RuleOrder": NotRequired[int],
        "RuleName": NotRequired[str],
        "Description": NotRequired[str],
        "IsTerminal": NotRequired[bool],
        "Criteria": NotRequired[AutomationRulesFindingFiltersTypeDef],
        "Actions": NotRequired[List[AutomationRulesActionTypeDef]],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)
CreateAutomationRuleRequestRequestTypeDef = TypedDict(
    "CreateAutomationRuleRequestRequestTypeDef",
    {
        "RuleOrder": int,
        "RuleName": str,
        "Description": str,
        "Criteria": AutomationRulesFindingFiltersTypeDef,
        "Actions": Sequence[AutomationRulesActionTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "RuleStatus": NotRequired[RuleStatusType],
        "IsTerminal": NotRequired[bool],
    },
)
UpdateAutomationRulesRequestItemTypeDef = TypedDict(
    "UpdateAutomationRulesRequestItemTypeDef",
    {
        "RuleArn": str,
        "RuleStatus": NotRequired[RuleStatusType],
        "RuleOrder": NotRequired[int],
        "Description": NotRequired[str],
        "RuleName": NotRequired[str],
        "IsTerminal": NotRequired[bool],
        "Criteria": NotRequired[AutomationRulesFindingFiltersTypeDef],
        "Actions": NotRequired[Sequence[AutomationRulesActionTypeDef]],
    },
)
CreateInsightRequestRequestTypeDef = TypedDict(
    "CreateInsightRequestRequestTypeDef",
    {
        "Name": str,
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "GroupByAttribute": str,
    },
)
GetFindingsRequestGetFindingsPaginateTypeDef = TypedDict(
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    {
        "Filters": NotRequired[AwsSecurityFindingFiltersTypeDef],
        "SortCriteria": NotRequired[Sequence[SortCriterionTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "Filters": NotRequired[AwsSecurityFindingFiltersTypeDef],
        "SortCriteria": NotRequired[Sequence[SortCriterionTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightArn": str,
        "Name": str,
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "GroupByAttribute": str,
    },
)
UpdateFindingsRequestRequestTypeDef = TypedDict(
    "UpdateFindingsRequestRequestTypeDef",
    {
        "Filters": AwsSecurityFindingFiltersTypeDef,
        "Note": NotRequired[NoteUpdateTypeDef],
        "RecordState": NotRequired[RecordStateType],
    },
)
UpdateInsightRequestRequestTypeDef = TypedDict(
    "UpdateInsightRequestRequestTypeDef",
    {
        "InsightArn": str,
        "Name": NotRequired[str],
        "Filters": NotRequired[AwsSecurityFindingFiltersTypeDef],
        "GroupByAttribute": NotRequired[str],
    },
)
NetworkPathComponentPaginatorTypeDef = TypedDict(
    "NetworkPathComponentPaginatorTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentType": NotRequired[str],
        "Egress": NotRequired[NetworkHeaderPaginatorTypeDef],
        "Ingress": NotRequired[NetworkHeaderPaginatorTypeDef],
    },
)
NetworkPathComponentTypeDef = TypedDict(
    "NetworkPathComponentTypeDef",
    {
        "ComponentId": NotRequired[str],
        "ComponentType": NotRequired[str],
        "Egress": NotRequired[NetworkHeaderTypeDef],
        "Ingress": NotRequired[NetworkHeaderTypeDef],
    },
)
CustomDataIdentifiersDetectionsPaginatorTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsPaginatorTypeDef",
    {
        "Count": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesPaginatorTypeDef],
    },
)
SensitiveDataDetectionsPaginatorTypeDef = TypedDict(
    "SensitiveDataDetectionsPaginatorTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesPaginatorTypeDef],
    },
)
CustomDataIdentifiersDetectionsTypeDef = TypedDict(
    "CustomDataIdentifiersDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesTypeDef],
    },
)
SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {
        "Count": NotRequired[int],
        "Type": NotRequired[str],
        "Occurrences": NotRequired[OccurrencesTypeDef],
    },
)
SecurityControlsConfigurationTypeDef = TypedDict(
    "SecurityControlsConfigurationTypeDef",
    {
        "EnabledSecurityControlIdentifiers": NotRequired[Sequence[str]],
        "DisabledSecurityControlIdentifiers": NotRequired[Sequence[str]],
        "SecurityControlCustomParameters": NotRequired[
            Sequence[SecurityControlCustomParameterTypeDef]
        ],
    },
)
BatchGetSecurityControlsResponseTypeDef = TypedDict(
    "BatchGetSecurityControlsResponseTypeDef",
    {
        "SecurityControls": List[SecurityControlTypeDef],
        "UnprocessedIds": List[UnprocessedSecurityControlTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleGroupSourceStatelessRulesDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsPaginatorTypeDef",
    {
        "Priority": NotRequired[int],
        "RuleDefinition": NotRequired[RuleGroupSourceStatelessRuleDefinitionPaginatorTypeDef],
    },
)
RuleGroupSourceStatelessRulesDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesDetailsTypeDef",
    {
        "Priority": NotRequired[int],
        "RuleDefinition": NotRequired[RuleGroupSourceStatelessRuleDefinitionTypeDef],
    },
)
FirewallPolicyStatelessCustomActionsDetailsPaginatorTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsPaginatorTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionPaginatorTypeDef],
        "ActionName": NotRequired[str],
    },
)
RuleGroupSourceCustomActionsDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsPaginatorTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionPaginatorTypeDef],
        "ActionName": NotRequired[str],
    },
)
FirewallPolicyStatelessCustomActionsDetailsTypeDef = TypedDict(
    "FirewallPolicyStatelessCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionTypeDef],
        "ActionName": NotRequired[str],
    },
)
RuleGroupSourceCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceCustomActionsDetailsTypeDef",
    {
        "ActionDefinition": NotRequired[StatelessCustomActionDefinitionTypeDef],
        "ActionName": NotRequired[str],
    },
)
ActionPaginatorTypeDef = TypedDict(
    "ActionPaginatorTypeDef",
    {
        "ActionType": NotRequired[str],
        "NetworkConnectionAction": NotRequired[NetworkConnectionActionTypeDef],
        "AwsApiCallAction": NotRequired[AwsApiCallActionPaginatorTypeDef],
        "DnsRequestAction": NotRequired[DnsRequestActionTypeDef],
        "PortProbeAction": NotRequired[PortProbeActionPaginatorTypeDef],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ActionType": NotRequired[str],
        "NetworkConnectionAction": NotRequired[NetworkConnectionActionTypeDef],
        "AwsApiCallAction": NotRequired[AwsApiCallActionTypeDef],
        "DnsRequestAction": NotRequired[DnsRequestActionTypeDef],
        "PortProbeAction": NotRequired[PortProbeActionTypeDef],
    },
)
AwsBackupBackupPlanDetailsPaginatorTypeDef = TypedDict(
    "AwsBackupBackupPlanDetailsPaginatorTypeDef",
    {
        "BackupPlan": NotRequired[AwsBackupBackupPlanBackupPlanDetailsPaginatorTypeDef],
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
AwsBackupBackupPlanDetailsTypeDef = TypedDict(
    "AwsBackupBackupPlanDetailsTypeDef",
    {
        "BackupPlan": NotRequired[AwsBackupBackupPlanBackupPlanDetailsTypeDef],
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
AwsCloudFrontDistributionDetailsPaginatorTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsPaginatorTypeDef",
    {
        "CacheBehaviors": NotRequired[AwsCloudFrontDistributionCacheBehaviorsPaginatorTypeDef],
        "DefaultCacheBehavior": NotRequired[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef],
        "DefaultRootObject": NotRequired[str],
        "DomainName": NotRequired[str],
        "ETag": NotRequired[str],
        "LastModifiedTime": NotRequired[str],
        "Logging": NotRequired[AwsCloudFrontDistributionLoggingTypeDef],
        "Origins": NotRequired[AwsCloudFrontDistributionOriginsPaginatorTypeDef],
        "OriginGroups": NotRequired[AwsCloudFrontDistributionOriginGroupsPaginatorTypeDef],
        "ViewerCertificate": NotRequired[AwsCloudFrontDistributionViewerCertificateTypeDef],
        "Status": NotRequired[str],
        "WebAclId": NotRequired[str],
    },
)
AwsCloudFrontDistributionDetailsTypeDef = TypedDict(
    "AwsCloudFrontDistributionDetailsTypeDef",
    {
        "CacheBehaviors": NotRequired[AwsCloudFrontDistributionCacheBehaviorsTypeDef],
        "DefaultCacheBehavior": NotRequired[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef],
        "DefaultRootObject": NotRequired[str],
        "DomainName": NotRequired[str],
        "ETag": NotRequired[str],
        "LastModifiedTime": NotRequired[str],
        "Logging": NotRequired[AwsCloudFrontDistributionLoggingTypeDef],
        "Origins": NotRequired[AwsCloudFrontDistributionOriginsTypeDef],
        "OriginGroups": NotRequired[AwsCloudFrontDistributionOriginGroupsTypeDef],
        "ViewerCertificate": NotRequired[AwsCloudFrontDistributionViewerCertificateTypeDef],
        "Status": NotRequired[str],
        "WebAclId": NotRequired[str],
    },
)
AwsGuardDutyDetectorDetailsPaginatorTypeDef = TypedDict(
    "AwsGuardDutyDetectorDetailsPaginatorTypeDef",
    {
        "DataSources": NotRequired[AwsGuardDutyDetectorDataSourcesDetailsTypeDef],
        "Features": NotRequired[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]],
        "FindingPublishingFrequency": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsGuardDutyDetectorDetailsTypeDef = TypedDict(
    "AwsGuardDutyDetectorDetailsTypeDef",
    {
        "DataSources": NotRequired[AwsGuardDutyDetectorDataSourcesDetailsTypeDef],
        "Features": NotRequired[Sequence[AwsGuardDutyDetectorFeaturesDetailsTypeDef]],
        "FindingPublishingFrequency": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "Status": NotRequired[str],
    },
)
AwsMskClusterDetailsPaginatorTypeDef = TypedDict(
    "AwsMskClusterDetailsPaginatorTypeDef",
    {
        "ClusterInfo": NotRequired[AwsMskClusterClusterInfoDetailsPaginatorTypeDef],
    },
)
AwsMskClusterDetailsTypeDef = TypedDict(
    "AwsMskClusterDetailsTypeDef",
    {
        "ClusterInfo": NotRequired[AwsMskClusterClusterInfoDetailsTypeDef],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesDetailsPaginatorTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsPaginatorTypeDef",
    {
        "AbortIncompleteMultipartUpload": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
        ],
        "ExpirationDate": NotRequired[str],
        "ExpirationInDays": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
        "Filter": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsPaginatorTypeDef
        ],
        "ID": NotRequired[str],
        "NoncurrentVersionExpirationInDays": NotRequired[int],
        "NoncurrentVersionTransitions": NotRequired[
            List[
                AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Status": NotRequired[str],
        "Transitions": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]
        ],
    },
)
AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef",
    {
        "AbortIncompleteMultipartUpload": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef
        ],
        "ExpirationDate": NotRequired[str],
        "ExpirationInDays": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
        "Filter": NotRequired[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef],
        "ID": NotRequired[str],
        "NoncurrentVersionExpirationInDays": NotRequired[int],
        "NoncurrentVersionTransitions": NotRequired[
            Sequence[
                AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef
            ]
        ],
        "Prefix": NotRequired[str],
        "Status": NotRequired[str],
        "Transitions": NotRequired[
            Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationPaginatorTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationPaginatorTypeDef",
    {
        "Configurations": NotRequired[
            List[AwsS3BucketNotificationConfigurationDetailPaginatorTypeDef]
        ],
    },
)
AwsS3BucketNotificationConfigurationTypeDef = TypedDict(
    "AwsS3BucketNotificationConfigurationTypeDef",
    {
        "Configurations": NotRequired[Sequence[AwsS3BucketNotificationConfigurationDetailTypeDef]],
    },
)
AwsWafv2RulesDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2RulesDetailsPaginatorTypeDef",
    {
        "Action": NotRequired[AwsWafv2RulesActionDetailsPaginatorTypeDef],
        "Name": NotRequired[str],
        "OverrideAction": NotRequired[str],
        "Priority": NotRequired[int],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2RulesDetailsTypeDef = TypedDict(
    "AwsWafv2RulesDetailsTypeDef",
    {
        "Action": NotRequired[AwsWafv2RulesActionDetailsTypeDef],
        "Name": NotRequired[str],
        "OverrideAction": NotRequired[str],
        "Priority": NotRequired[int],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
GetSecurityControlDefinitionResponseTypeDef = TypedDict(
    "GetSecurityControlDefinitionResponseTypeDef",
    {
        "SecurityControlDefinition": SecurityControlDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSecurityControlDefinitionsResponseTypeDef = TypedDict(
    "ListSecurityControlDefinitionsResponseTypeDef",
    {
        "SecurityControlDefinitions": List[SecurityControlDefinitionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAutomationRulesResponseTypeDef = TypedDict(
    "BatchGetAutomationRulesResponseTypeDef",
    {
        "Rules": List[AutomationRulesConfigTypeDef],
        "UnprocessedAutomationRules": List[UnprocessedAutomationRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateAutomationRulesRequestRequestTypeDef = TypedDict(
    "BatchUpdateAutomationRulesRequestRequestTypeDef",
    {
        "UpdateAutomationRulesRequestItems": Sequence[UpdateAutomationRulesRequestItemTypeDef],
    },
)
GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "Insights": List[InsightTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomDataIdentifiersResultPaginatorTypeDef = TypedDict(
    "CustomDataIdentifiersResultPaginatorTypeDef",
    {
        "Detections": NotRequired[List[CustomDataIdentifiersDetectionsPaginatorTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
SensitiveDataResultPaginatorTypeDef = TypedDict(
    "SensitiveDataResultPaginatorTypeDef",
    {
        "Category": NotRequired[str],
        "Detections": NotRequired[List[SensitiveDataDetectionsPaginatorTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
CustomDataIdentifiersResultTypeDef = TypedDict(
    "CustomDataIdentifiersResultTypeDef",
    {
        "Detections": NotRequired[Sequence[CustomDataIdentifiersDetectionsTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
SensitiveDataResultTypeDef = TypedDict(
    "SensitiveDataResultTypeDef",
    {
        "Category": NotRequired[str],
        "Detections": NotRequired[Sequence[SensitiveDataDetectionsTypeDef]],
        "TotalCount": NotRequired[int],
    },
)
SecurityHubPolicyTypeDef = TypedDict(
    "SecurityHubPolicyTypeDef",
    {
        "ServiceEnabled": NotRequired[bool],
        "EnabledStandardIdentifiers": NotRequired[Sequence[str]],
        "SecurityControlsConfiguration": NotRequired[SecurityControlsConfigurationTypeDef],
    },
)
FirewallPolicyDetailsPaginatorTypeDef = TypedDict(
    "FirewallPolicyDetailsPaginatorTypeDef",
    {
        "StatefulRuleGroupReferences": NotRequired[
            List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]
        ],
        "StatelessCustomActions": NotRequired[
            List[FirewallPolicyStatelessCustomActionsDetailsPaginatorTypeDef]
        ],
        "StatelessDefaultActions": NotRequired[List[str]],
        "StatelessFragmentDefaultActions": NotRequired[List[str]],
        "StatelessRuleGroupReferences": NotRequired[
            List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRulesAndCustomActionsDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsPaginatorTypeDef",
    {
        "CustomActions": NotRequired[List[RuleGroupSourceCustomActionsDetailsPaginatorTypeDef]],
        "StatelessRules": NotRequired[List[RuleGroupSourceStatelessRulesDetailsPaginatorTypeDef]],
    },
)
FirewallPolicyDetailsTypeDef = TypedDict(
    "FirewallPolicyDetailsTypeDef",
    {
        "StatefulRuleGroupReferences": NotRequired[
            Sequence[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]
        ],
        "StatelessCustomActions": NotRequired[
            Sequence[FirewallPolicyStatelessCustomActionsDetailsTypeDef]
        ],
        "StatelessDefaultActions": NotRequired[Sequence[str]],
        "StatelessFragmentDefaultActions": NotRequired[Sequence[str]],
        "StatelessRuleGroupReferences": NotRequired[
            Sequence[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]
        ],
    },
)
RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef = TypedDict(
    "RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef",
    {
        "CustomActions": NotRequired[Sequence[RuleGroupSourceCustomActionsDetailsTypeDef]],
        "StatelessRules": NotRequired[Sequence[RuleGroupSourceStatelessRulesDetailsTypeDef]],
    },
)
AwsS3BucketBucketLifecycleConfigurationDetailsPaginatorTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsPaginatorTypeDef",
    {
        "Rules": NotRequired[
            List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsPaginatorTypeDef]
        ],
    },
)
AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef = TypedDict(
    "AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef",
    {
        "Rules": NotRequired[Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef]],
    },
)
AwsWafv2RuleGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2RuleGroupDetailsPaginatorTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Rules": NotRequired[List[AwsWafv2RulesDetailsPaginatorTypeDef]],
        "Scope": NotRequired[str],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2WebAclDetailsPaginatorTypeDef = TypedDict(
    "AwsWafv2WebAclDetailsPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "ManagedbyFirewallManager": NotRequired[bool],
        "Id": NotRequired[str],
        "Capacity": NotRequired[int],
        "CaptchaConfig": NotRequired[AwsWafv2WebAclCaptchaConfigDetailsTypeDef],
        "DefaultAction": NotRequired[AwsWafv2WebAclActionDetailsPaginatorTypeDef],
        "Description": NotRequired[str],
        "Rules": NotRequired[List[AwsWafv2RulesDetailsPaginatorTypeDef]],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2RuleGroupDetailsTypeDef = TypedDict(
    "AwsWafv2RuleGroupDetailsTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafv2RulesDetailsTypeDef]],
        "Scope": NotRequired[str],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
AwsWafv2WebAclDetailsTypeDef = TypedDict(
    "AwsWafv2WebAclDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "ManagedbyFirewallManager": NotRequired[bool],
        "Id": NotRequired[str],
        "Capacity": NotRequired[int],
        "CaptchaConfig": NotRequired[AwsWafv2WebAclCaptchaConfigDetailsTypeDef],
        "DefaultAction": NotRequired[AwsWafv2WebAclActionDetailsTypeDef],
        "Description": NotRequired[str],
        "Rules": NotRequired[Sequence[AwsWafv2RulesDetailsTypeDef]],
        "VisibilityConfig": NotRequired[AwsWafv2VisibilityConfigDetailsTypeDef],
    },
)
ClassificationResultPaginatorTypeDef = TypedDict(
    "ClassificationResultPaginatorTypeDef",
    {
        "MimeType": NotRequired[str],
        "SizeClassified": NotRequired[int],
        "AdditionalOccurrences": NotRequired[bool],
        "Status": NotRequired[ClassificationStatusTypeDef],
        "SensitiveData": NotRequired[List[SensitiveDataResultPaginatorTypeDef]],
        "CustomDataIdentifiers": NotRequired[CustomDataIdentifiersResultPaginatorTypeDef],
    },
)
ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "MimeType": NotRequired[str],
        "SizeClassified": NotRequired[int],
        "AdditionalOccurrences": NotRequired[bool],
        "Status": NotRequired[ClassificationStatusTypeDef],
        "SensitiveData": NotRequired[Sequence[SensitiveDataResultTypeDef]],
        "CustomDataIdentifiers": NotRequired[CustomDataIdentifiersResultTypeDef],
    },
)
PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "SecurityHub": NotRequired[SecurityHubPolicyTypeDef],
    },
)
AwsNetworkFirewallFirewallPolicyDetailsPaginatorTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsPaginatorTypeDef",
    {
        "FirewallPolicy": NotRequired[FirewallPolicyDetailsPaginatorTypeDef],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
        "Description": NotRequired[str],
    },
)
RuleGroupSourcePaginatorTypeDef = TypedDict(
    "RuleGroupSourcePaginatorTypeDef",
    {
        "RulesSourceList": NotRequired[RuleGroupSourceListDetailsPaginatorTypeDef],
        "RulesString": NotRequired[str],
        "StatefulRules": NotRequired[List[RuleGroupSourceStatefulRulesDetailsPaginatorTypeDef]],
        "StatelessRulesAndCustomActions": NotRequired[
            RuleGroupSourceStatelessRulesAndCustomActionsDetailsPaginatorTypeDef
        ],
    },
)
AwsNetworkFirewallFirewallPolicyDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallFirewallPolicyDetailsTypeDef",
    {
        "FirewallPolicy": NotRequired[FirewallPolicyDetailsTypeDef],
        "FirewallPolicyArn": NotRequired[str],
        "FirewallPolicyId": NotRequired[str],
        "FirewallPolicyName": NotRequired[str],
        "Description": NotRequired[str],
    },
)
RuleGroupSourceTypeDef = TypedDict(
    "RuleGroupSourceTypeDef",
    {
        "RulesSourceList": NotRequired[RuleGroupSourceListDetailsTypeDef],
        "RulesString": NotRequired[str],
        "StatefulRules": NotRequired[Sequence[RuleGroupSourceStatefulRulesDetailsTypeDef]],
        "StatelessRulesAndCustomActions": NotRequired[
            RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef
        ],
    },
)
AwsS3BucketDetailsPaginatorTypeDef = TypedDict(
    "AwsS3BucketDetailsPaginatorTypeDef",
    {
        "OwnerId": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            AwsS3BucketServerSideEncryptionConfigurationPaginatorTypeDef
        ],
        "BucketLifecycleConfiguration": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationDetailsPaginatorTypeDef
        ],
        "PublicAccessBlockConfiguration": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AccessControlList": NotRequired[str],
        "BucketLoggingConfiguration": NotRequired[AwsS3BucketLoggingConfigurationTypeDef],
        "BucketWebsiteConfiguration": NotRequired[AwsS3BucketWebsiteConfigurationPaginatorTypeDef],
        "BucketNotificationConfiguration": NotRequired[
            AwsS3BucketNotificationConfigurationPaginatorTypeDef
        ],
        "BucketVersioningConfiguration": NotRequired[
            AwsS3BucketBucketVersioningConfigurationTypeDef
        ],
        "ObjectLockConfiguration": NotRequired[AwsS3BucketObjectLockConfigurationTypeDef],
        "Name": NotRequired[str],
    },
)
AwsS3BucketDetailsTypeDef = TypedDict(
    "AwsS3BucketDetailsTypeDef",
    {
        "OwnerId": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[
            AwsS3BucketServerSideEncryptionConfigurationTypeDef
        ],
        "BucketLifecycleConfiguration": NotRequired[
            AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef
        ],
        "PublicAccessBlockConfiguration": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AccessControlList": NotRequired[str],
        "BucketLoggingConfiguration": NotRequired[AwsS3BucketLoggingConfigurationTypeDef],
        "BucketWebsiteConfiguration": NotRequired[AwsS3BucketWebsiteConfigurationTypeDef],
        "BucketNotificationConfiguration": NotRequired[AwsS3BucketNotificationConfigurationTypeDef],
        "BucketVersioningConfiguration": NotRequired[
            AwsS3BucketBucketVersioningConfigurationTypeDef
        ],
        "ObjectLockConfiguration": NotRequired[AwsS3BucketObjectLockConfigurationTypeDef],
        "Name": NotRequired[str],
    },
)
DataClassificationDetailsPaginatorTypeDef = TypedDict(
    "DataClassificationDetailsPaginatorTypeDef",
    {
        "DetailedResultsLocation": NotRequired[str],
        "Result": NotRequired[ClassificationResultPaginatorTypeDef],
    },
)
DataClassificationDetailsTypeDef = TypedDict(
    "DataClassificationDetailsTypeDef",
    {
        "DetailedResultsLocation": NotRequired[str],
        "Result": NotRequired[ClassificationResultTypeDef],
    },
)
CreateConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "CreateConfigurationPolicyRequestRequestTypeDef",
    {
        "Name": str,
        "ConfigurationPolicy": PolicyTypeDef,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateConfigurationPolicyResponseTypeDef = TypedDict(
    "CreateConfigurationPolicyResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "UpdatedAt": datetime,
        "CreatedAt": datetime,
        "ConfigurationPolicy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfigurationPolicyResponseTypeDef = TypedDict(
    "GetConfigurationPolicyResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "UpdatedAt": datetime,
        "CreatedAt": datetime,
        "ConfigurationPolicy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfigurationPolicyRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationPolicyRequestRequestTypeDef",
    {
        "Identifier": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "UpdatedReason": NotRequired[str],
        "ConfigurationPolicy": NotRequired[PolicyTypeDef],
    },
)
UpdateConfigurationPolicyResponseTypeDef = TypedDict(
    "UpdateConfigurationPolicyResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "UpdatedAt": datetime,
        "CreatedAt": datetime,
        "ConfigurationPolicy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleGroupDetailsPaginatorTypeDef = TypedDict(
    "RuleGroupDetailsPaginatorTypeDef",
    {
        "RuleVariables": NotRequired[RuleGroupVariablesPaginatorTypeDef],
        "RulesSource": NotRequired[RuleGroupSourcePaginatorTypeDef],
    },
)
RuleGroupDetailsTypeDef = TypedDict(
    "RuleGroupDetailsTypeDef",
    {
        "RuleVariables": NotRequired[RuleGroupVariablesTypeDef],
        "RulesSource": NotRequired[RuleGroupSourceTypeDef],
    },
)
AwsNetworkFirewallRuleGroupDetailsPaginatorTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsPaginatorTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired[RuleGroupDetailsPaginatorTypeDef],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AwsNetworkFirewallRuleGroupDetailsTypeDef = TypedDict(
    "AwsNetworkFirewallRuleGroupDetailsTypeDef",
    {
        "Capacity": NotRequired[int],
        "Description": NotRequired[str],
        "RuleGroup": NotRequired[RuleGroupDetailsTypeDef],
        "RuleGroupArn": NotRequired[str],
        "RuleGroupId": NotRequired[str],
        "RuleGroupName": NotRequired[str],
        "Type": NotRequired[str],
    },
)
ResourceDetailsPaginatorTypeDef = TypedDict(
    "ResourceDetailsPaginatorTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[
            AwsAutoScalingAutoScalingGroupDetailsPaginatorTypeDef
        ],
        "AwsCodeBuildProject": NotRequired[AwsCodeBuildProjectDetailsPaginatorTypeDef],
        "AwsCloudFrontDistribution": NotRequired[AwsCloudFrontDistributionDetailsPaginatorTypeDef],
        "AwsEc2Instance": NotRequired[AwsEc2InstanceDetailsPaginatorTypeDef],
        "AwsEc2NetworkInterface": NotRequired[AwsEc2NetworkInterfaceDetailsPaginatorTypeDef],
        "AwsEc2SecurityGroup": NotRequired[AwsEc2SecurityGroupDetailsPaginatorTypeDef],
        "AwsEc2Volume": NotRequired[AwsEc2VolumeDetailsPaginatorTypeDef],
        "AwsEc2Vpc": NotRequired[AwsEc2VpcDetailsPaginatorTypeDef],
        "AwsEc2Eip": NotRequired[AwsEc2EipDetailsTypeDef],
        "AwsEc2Subnet": NotRequired[AwsEc2SubnetDetailsPaginatorTypeDef],
        "AwsEc2NetworkAcl": NotRequired[AwsEc2NetworkAclDetailsPaginatorTypeDef],
        "AwsElbv2LoadBalancer": NotRequired[AwsElbv2LoadBalancerDetailsPaginatorTypeDef],
        "AwsElasticBeanstalkEnvironment": NotRequired[
            AwsElasticBeanstalkEnvironmentDetailsPaginatorTypeDef
        ],
        "AwsElasticsearchDomain": NotRequired[AwsElasticsearchDomainDetailsPaginatorTypeDef],
        "AwsS3Bucket": NotRequired[AwsS3BucketDetailsPaginatorTypeDef],
        "AwsS3AccountPublicAccessBlock": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AwsS3Object": NotRequired[AwsS3ObjectDetailsTypeDef],
        "AwsSecretsManagerSecret": NotRequired[AwsSecretsManagerSecretDetailsTypeDef],
        "AwsIamAccessKey": NotRequired[AwsIamAccessKeyDetailsTypeDef],
        "AwsIamUser": NotRequired[AwsIamUserDetailsPaginatorTypeDef],
        "AwsIamPolicy": NotRequired[AwsIamPolicyDetailsPaginatorTypeDef],
        "AwsApiGatewayV2Stage": NotRequired[AwsApiGatewayV2StageDetailsPaginatorTypeDef],
        "AwsApiGatewayV2Api": NotRequired[AwsApiGatewayV2ApiDetailsPaginatorTypeDef],
        "AwsDynamoDbTable": NotRequired[AwsDynamoDbTableDetailsPaginatorTypeDef],
        "AwsApiGatewayStage": NotRequired[AwsApiGatewayStageDetailsPaginatorTypeDef],
        "AwsApiGatewayRestApi": NotRequired[AwsApiGatewayRestApiDetailsPaginatorTypeDef],
        "AwsCloudTrailTrail": NotRequired[AwsCloudTrailTrailDetailsTypeDef],
        "AwsSsmPatchCompliance": NotRequired[AwsSsmPatchComplianceDetailsTypeDef],
        "AwsCertificateManagerCertificate": NotRequired[
            AwsCertificateManagerCertificateDetailsPaginatorTypeDef
        ],
        "AwsRedshiftCluster": NotRequired[AwsRedshiftClusterDetailsPaginatorTypeDef],
        "AwsElbLoadBalancer": NotRequired[AwsElbLoadBalancerDetailsPaginatorTypeDef],
        "AwsIamGroup": NotRequired[AwsIamGroupDetailsPaginatorTypeDef],
        "AwsIamRole": NotRequired[AwsIamRoleDetailsPaginatorTypeDef],
        "AwsKmsKey": NotRequired[AwsKmsKeyDetailsTypeDef],
        "AwsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsPaginatorTypeDef],
        "AwsLambdaLayerVersion": NotRequired[AwsLambdaLayerVersionDetailsPaginatorTypeDef],
        "AwsRdsDbInstance": NotRequired[AwsRdsDbInstanceDetailsPaginatorTypeDef],
        "AwsSnsTopic": NotRequired[AwsSnsTopicDetailsPaginatorTypeDef],
        "AwsSqsQueue": NotRequired[AwsSqsQueueDetailsTypeDef],
        "AwsWafWebAcl": NotRequired[AwsWafWebAclDetailsPaginatorTypeDef],
        "AwsRdsDbSnapshot": NotRequired[AwsRdsDbSnapshotDetailsPaginatorTypeDef],
        "AwsRdsDbClusterSnapshot": NotRequired[AwsRdsDbClusterSnapshotDetailsPaginatorTypeDef],
        "AwsRdsDbCluster": NotRequired[AwsRdsDbClusterDetailsPaginatorTypeDef],
        "AwsEcsCluster": NotRequired[AwsEcsClusterDetailsPaginatorTypeDef],
        "AwsEcsContainer": NotRequired[AwsEcsContainerDetailsPaginatorTypeDef],
        "AwsEcsTaskDefinition": NotRequired[AwsEcsTaskDefinitionDetailsPaginatorTypeDef],
        "Container": NotRequired[ContainerDetailsPaginatorTypeDef],
        "Other": NotRequired[Dict[str, str]],
        "AwsRdsEventSubscription": NotRequired[AwsRdsEventSubscriptionDetailsPaginatorTypeDef],
        "AwsEcsService": NotRequired[AwsEcsServiceDetailsPaginatorTypeDef],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            AwsAutoScalingLaunchConfigurationDetailsPaginatorTypeDef
        ],
        "AwsEc2VpnConnection": NotRequired[AwsEc2VpnConnectionDetailsPaginatorTypeDef],
        "AwsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsPaginatorTypeDef],
        "AwsOpenSearchServiceDomain": NotRequired[
            AwsOpenSearchServiceDomainDetailsPaginatorTypeDef
        ],
        "AwsEc2VpcEndpointService": NotRequired[AwsEc2VpcEndpointServiceDetailsPaginatorTypeDef],
        "AwsXrayEncryptionConfig": NotRequired[AwsXrayEncryptionConfigDetailsTypeDef],
        "AwsWafRateBasedRule": NotRequired[AwsWafRateBasedRuleDetailsPaginatorTypeDef],
        "AwsWafRegionalRateBasedRule": NotRequired[
            AwsWafRegionalRateBasedRuleDetailsPaginatorTypeDef
        ],
        "AwsEcrRepository": NotRequired[AwsEcrRepositoryDetailsTypeDef],
        "AwsEksCluster": NotRequired[AwsEksClusterDetailsPaginatorTypeDef],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            AwsNetworkFirewallFirewallPolicyDetailsPaginatorTypeDef
        ],
        "AwsNetworkFirewallFirewall": NotRequired[
            AwsNetworkFirewallFirewallDetailsPaginatorTypeDef
        ],
        "AwsNetworkFirewallRuleGroup": NotRequired[
            AwsNetworkFirewallRuleGroupDetailsPaginatorTypeDef
        ],
        "AwsRdsDbSecurityGroup": NotRequired[AwsRdsDbSecurityGroupDetailsPaginatorTypeDef],
        "AwsKinesisStream": NotRequired[AwsKinesisStreamDetailsTypeDef],
        "AwsEc2TransitGateway": NotRequired[AwsEc2TransitGatewayDetailsPaginatorTypeDef],
        "AwsEfsAccessPoint": NotRequired[AwsEfsAccessPointDetailsPaginatorTypeDef],
        "AwsCloudFormationStack": NotRequired[AwsCloudFormationStackDetailsPaginatorTypeDef],
        "AwsCloudWatchAlarm": NotRequired[AwsCloudWatchAlarmDetailsPaginatorTypeDef],
        "AwsEc2VpcPeeringConnection": NotRequired[
            AwsEc2VpcPeeringConnectionDetailsPaginatorTypeDef
        ],
        "AwsWafRegionalRuleGroup": NotRequired[AwsWafRegionalRuleGroupDetailsPaginatorTypeDef],
        "AwsWafRegionalRule": NotRequired[AwsWafRegionalRuleDetailsPaginatorTypeDef],
        "AwsWafRegionalWebAcl": NotRequired[AwsWafRegionalWebAclDetailsPaginatorTypeDef],
        "AwsWafRule": NotRequired[AwsWafRuleDetailsPaginatorTypeDef],
        "AwsWafRuleGroup": NotRequired[AwsWafRuleGroupDetailsPaginatorTypeDef],
        "AwsEcsTask": NotRequired[AwsEcsTaskDetailsPaginatorTypeDef],
        "AwsBackupBackupVault": NotRequired[AwsBackupBackupVaultDetailsPaginatorTypeDef],
        "AwsBackupBackupPlan": NotRequired[AwsBackupBackupPlanDetailsPaginatorTypeDef],
        "AwsBackupRecoveryPoint": NotRequired[AwsBackupRecoveryPointDetailsTypeDef],
        "AwsEc2LaunchTemplate": NotRequired[AwsEc2LaunchTemplateDetailsPaginatorTypeDef],
        "AwsSageMakerNotebookInstance": NotRequired[
            AwsSageMakerNotebookInstanceDetailsPaginatorTypeDef
        ],
        "AwsWafv2WebAcl": NotRequired[AwsWafv2WebAclDetailsPaginatorTypeDef],
        "AwsWafv2RuleGroup": NotRequired[AwsWafv2RuleGroupDetailsPaginatorTypeDef],
        "AwsEc2RouteTable": NotRequired[AwsEc2RouteTableDetailsPaginatorTypeDef],
        "AwsAmazonMqBroker": NotRequired[AwsAmazonMqBrokerDetailsPaginatorTypeDef],
        "AwsAppSyncGraphQlApi": NotRequired[AwsAppSyncGraphQlApiDetailsPaginatorTypeDef],
        "AwsEventSchemasRegistry": NotRequired[AwsEventSchemasRegistryDetailsTypeDef],
        "AwsGuardDutyDetector": NotRequired[AwsGuardDutyDetectorDetailsPaginatorTypeDef],
        "AwsStepFunctionStateMachine": NotRequired[
            AwsStepFunctionStateMachineDetailsPaginatorTypeDef
        ],
        "AwsAthenaWorkGroup": NotRequired[AwsAthenaWorkGroupDetailsTypeDef],
        "AwsEventsEventbus": NotRequired[AwsEventsEventbusDetailsTypeDef],
        "AwsDmsEndpoint": NotRequired[AwsDmsEndpointDetailsTypeDef],
        "AwsEventsEndpoint": NotRequired[AwsEventsEndpointDetailsPaginatorTypeDef],
        "AwsDmsReplicationTask": NotRequired[AwsDmsReplicationTaskDetailsTypeDef],
        "AwsDmsReplicationInstance": NotRequired[AwsDmsReplicationInstanceDetailsPaginatorTypeDef],
        "AwsRoute53HostedZone": NotRequired[AwsRoute53HostedZoneDetailsPaginatorTypeDef],
        "AwsMskCluster": NotRequired[AwsMskClusterDetailsPaginatorTypeDef],
        "AwsS3AccessPoint": NotRequired[AwsS3AccessPointDetailsTypeDef],
        "AwsEc2ClientVpnEndpoint": NotRequired[AwsEc2ClientVpnEndpointDetailsPaginatorTypeDef],
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": NotRequired[AwsAutoScalingAutoScalingGroupDetailsTypeDef],
        "AwsCodeBuildProject": NotRequired[AwsCodeBuildProjectDetailsTypeDef],
        "AwsCloudFrontDistribution": NotRequired[AwsCloudFrontDistributionDetailsTypeDef],
        "AwsEc2Instance": NotRequired[AwsEc2InstanceDetailsTypeDef],
        "AwsEc2NetworkInterface": NotRequired[AwsEc2NetworkInterfaceDetailsTypeDef],
        "AwsEc2SecurityGroup": NotRequired[AwsEc2SecurityGroupDetailsTypeDef],
        "AwsEc2Volume": NotRequired[AwsEc2VolumeDetailsTypeDef],
        "AwsEc2Vpc": NotRequired[AwsEc2VpcDetailsTypeDef],
        "AwsEc2Eip": NotRequired[AwsEc2EipDetailsTypeDef],
        "AwsEc2Subnet": NotRequired[AwsEc2SubnetDetailsTypeDef],
        "AwsEc2NetworkAcl": NotRequired[AwsEc2NetworkAclDetailsTypeDef],
        "AwsElbv2LoadBalancer": NotRequired[AwsElbv2LoadBalancerDetailsTypeDef],
        "AwsElasticBeanstalkEnvironment": NotRequired[AwsElasticBeanstalkEnvironmentDetailsTypeDef],
        "AwsElasticsearchDomain": NotRequired[AwsElasticsearchDomainDetailsTypeDef],
        "AwsS3Bucket": NotRequired[AwsS3BucketDetailsTypeDef],
        "AwsS3AccountPublicAccessBlock": NotRequired[AwsS3AccountPublicAccessBlockDetailsTypeDef],
        "AwsS3Object": NotRequired[AwsS3ObjectDetailsTypeDef],
        "AwsSecretsManagerSecret": NotRequired[AwsSecretsManagerSecretDetailsTypeDef],
        "AwsIamAccessKey": NotRequired[AwsIamAccessKeyDetailsTypeDef],
        "AwsIamUser": NotRequired[AwsIamUserDetailsTypeDef],
        "AwsIamPolicy": NotRequired[AwsIamPolicyDetailsTypeDef],
        "AwsApiGatewayV2Stage": NotRequired[AwsApiGatewayV2StageDetailsTypeDef],
        "AwsApiGatewayV2Api": NotRequired[AwsApiGatewayV2ApiDetailsTypeDef],
        "AwsDynamoDbTable": NotRequired[AwsDynamoDbTableDetailsTypeDef],
        "AwsApiGatewayStage": NotRequired[AwsApiGatewayStageDetailsTypeDef],
        "AwsApiGatewayRestApi": NotRequired[AwsApiGatewayRestApiDetailsTypeDef],
        "AwsCloudTrailTrail": NotRequired[AwsCloudTrailTrailDetailsTypeDef],
        "AwsSsmPatchCompliance": NotRequired[AwsSsmPatchComplianceDetailsTypeDef],
        "AwsCertificateManagerCertificate": NotRequired[
            AwsCertificateManagerCertificateDetailsTypeDef
        ],
        "AwsRedshiftCluster": NotRequired[AwsRedshiftClusterDetailsTypeDef],
        "AwsElbLoadBalancer": NotRequired[AwsElbLoadBalancerDetailsTypeDef],
        "AwsIamGroup": NotRequired[AwsIamGroupDetailsTypeDef],
        "AwsIamRole": NotRequired[AwsIamRoleDetailsTypeDef],
        "AwsKmsKey": NotRequired[AwsKmsKeyDetailsTypeDef],
        "AwsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsTypeDef],
        "AwsLambdaLayerVersion": NotRequired[AwsLambdaLayerVersionDetailsTypeDef],
        "AwsRdsDbInstance": NotRequired[AwsRdsDbInstanceDetailsTypeDef],
        "AwsSnsTopic": NotRequired[AwsSnsTopicDetailsTypeDef],
        "AwsSqsQueue": NotRequired[AwsSqsQueueDetailsTypeDef],
        "AwsWafWebAcl": NotRequired[AwsWafWebAclDetailsTypeDef],
        "AwsRdsDbSnapshot": NotRequired[AwsRdsDbSnapshotDetailsTypeDef],
        "AwsRdsDbClusterSnapshot": NotRequired[AwsRdsDbClusterSnapshotDetailsTypeDef],
        "AwsRdsDbCluster": NotRequired[AwsRdsDbClusterDetailsTypeDef],
        "AwsEcsCluster": NotRequired[AwsEcsClusterDetailsTypeDef],
        "AwsEcsContainer": NotRequired[AwsEcsContainerDetailsTypeDef],
        "AwsEcsTaskDefinition": NotRequired[AwsEcsTaskDefinitionDetailsTypeDef],
        "Container": NotRequired[ContainerDetailsTypeDef],
        "Other": NotRequired[Mapping[str, str]],
        "AwsRdsEventSubscription": NotRequired[AwsRdsEventSubscriptionDetailsTypeDef],
        "AwsEcsService": NotRequired[AwsEcsServiceDetailsTypeDef],
        "AwsAutoScalingLaunchConfiguration": NotRequired[
            AwsAutoScalingLaunchConfigurationDetailsTypeDef
        ],
        "AwsEc2VpnConnection": NotRequired[AwsEc2VpnConnectionDetailsTypeDef],
        "AwsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsTypeDef],
        "AwsOpenSearchServiceDomain": NotRequired[AwsOpenSearchServiceDomainDetailsTypeDef],
        "AwsEc2VpcEndpointService": NotRequired[AwsEc2VpcEndpointServiceDetailsTypeDef],
        "AwsXrayEncryptionConfig": NotRequired[AwsXrayEncryptionConfigDetailsTypeDef],
        "AwsWafRateBasedRule": NotRequired[AwsWafRateBasedRuleDetailsTypeDef],
        "AwsWafRegionalRateBasedRule": NotRequired[AwsWafRegionalRateBasedRuleDetailsTypeDef],
        "AwsEcrRepository": NotRequired[AwsEcrRepositoryDetailsTypeDef],
        "AwsEksCluster": NotRequired[AwsEksClusterDetailsTypeDef],
        "AwsNetworkFirewallFirewallPolicy": NotRequired[
            AwsNetworkFirewallFirewallPolicyDetailsTypeDef
        ],
        "AwsNetworkFirewallFirewall": NotRequired[AwsNetworkFirewallFirewallDetailsTypeDef],
        "AwsNetworkFirewallRuleGroup": NotRequired[AwsNetworkFirewallRuleGroupDetailsTypeDef],
        "AwsRdsDbSecurityGroup": NotRequired[AwsRdsDbSecurityGroupDetailsTypeDef],
        "AwsKinesisStream": NotRequired[AwsKinesisStreamDetailsTypeDef],
        "AwsEc2TransitGateway": NotRequired[AwsEc2TransitGatewayDetailsTypeDef],
        "AwsEfsAccessPoint": NotRequired[AwsEfsAccessPointDetailsTypeDef],
        "AwsCloudFormationStack": NotRequired[AwsCloudFormationStackDetailsTypeDef],
        "AwsCloudWatchAlarm": NotRequired[AwsCloudWatchAlarmDetailsTypeDef],
        "AwsEc2VpcPeeringConnection": NotRequired[AwsEc2VpcPeeringConnectionDetailsTypeDef],
        "AwsWafRegionalRuleGroup": NotRequired[AwsWafRegionalRuleGroupDetailsTypeDef],
        "AwsWafRegionalRule": NotRequired[AwsWafRegionalRuleDetailsTypeDef],
        "AwsWafRegionalWebAcl": NotRequired[AwsWafRegionalWebAclDetailsTypeDef],
        "AwsWafRule": NotRequired[AwsWafRuleDetailsTypeDef],
        "AwsWafRuleGroup": NotRequired[AwsWafRuleGroupDetailsTypeDef],
        "AwsEcsTask": NotRequired[AwsEcsTaskDetailsTypeDef],
        "AwsBackupBackupVault": NotRequired[AwsBackupBackupVaultDetailsTypeDef],
        "AwsBackupBackupPlan": NotRequired[AwsBackupBackupPlanDetailsTypeDef],
        "AwsBackupRecoveryPoint": NotRequired[AwsBackupRecoveryPointDetailsTypeDef],
        "AwsEc2LaunchTemplate": NotRequired[AwsEc2LaunchTemplateDetailsTypeDef],
        "AwsSageMakerNotebookInstance": NotRequired[AwsSageMakerNotebookInstanceDetailsTypeDef],
        "AwsWafv2WebAcl": NotRequired[AwsWafv2WebAclDetailsTypeDef],
        "AwsWafv2RuleGroup": NotRequired[AwsWafv2RuleGroupDetailsTypeDef],
        "AwsEc2RouteTable": NotRequired[AwsEc2RouteTableDetailsTypeDef],
        "AwsAmazonMqBroker": NotRequired[AwsAmazonMqBrokerDetailsTypeDef],
        "AwsAppSyncGraphQlApi": NotRequired[AwsAppSyncGraphQlApiDetailsTypeDef],
        "AwsEventSchemasRegistry": NotRequired[AwsEventSchemasRegistryDetailsTypeDef],
        "AwsGuardDutyDetector": NotRequired[AwsGuardDutyDetectorDetailsTypeDef],
        "AwsStepFunctionStateMachine": NotRequired[AwsStepFunctionStateMachineDetailsTypeDef],
        "AwsAthenaWorkGroup": NotRequired[AwsAthenaWorkGroupDetailsTypeDef],
        "AwsEventsEventbus": NotRequired[AwsEventsEventbusDetailsTypeDef],
        "AwsDmsEndpoint": NotRequired[AwsDmsEndpointDetailsTypeDef],
        "AwsEventsEndpoint": NotRequired[AwsEventsEndpointDetailsTypeDef],
        "AwsDmsReplicationTask": NotRequired[AwsDmsReplicationTaskDetailsTypeDef],
        "AwsDmsReplicationInstance": NotRequired[AwsDmsReplicationInstanceDetailsTypeDef],
        "AwsRoute53HostedZone": NotRequired[AwsRoute53HostedZoneDetailsTypeDef],
        "AwsMskCluster": NotRequired[AwsMskClusterDetailsTypeDef],
        "AwsS3AccessPoint": NotRequired[AwsS3AccessPointDetailsTypeDef],
        "AwsEc2ClientVpnEndpoint": NotRequired[AwsEc2ClientVpnEndpointDetailsTypeDef],
    },
)
ResourcePaginatorTypeDef = TypedDict(
    "ResourcePaginatorTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "DataClassification": NotRequired[DataClassificationDetailsPaginatorTypeDef],
        "Details": NotRequired[ResourceDetailsPaginatorTypeDef],
        "ApplicationName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Type": str,
        "Id": str,
        "Partition": NotRequired[PartitionType],
        "Region": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "DataClassification": NotRequired[DataClassificationDetailsTypeDef],
        "Details": NotRequired[ResourceDetailsTypeDef],
        "ApplicationName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
AwsSecurityFindingPaginatorTypeDef = TypedDict(
    "AwsSecurityFindingPaginatorTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": List[ResourcePaginatorTypeDef],
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Region": NotRequired[str],
        "Types": NotRequired[List[str]],
        "FirstObservedAt": NotRequired[str],
        "LastObservedAt": NotRequired[str],
        "Severity": NotRequired[SeverityTypeDef],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Remediation": NotRequired[RemediationTypeDef],
        "SourceUrl": NotRequired[str],
        "ProductFields": NotRequired[Dict[str, str]],
        "UserDefinedFields": NotRequired[Dict[str, str]],
        "Malware": NotRequired[List[MalwareTypeDef]],
        "Network": NotRequired[NetworkTypeDef],
        "NetworkPath": NotRequired[List[NetworkPathComponentPaginatorTypeDef]],
        "Process": NotRequired[ProcessDetailsTypeDef],
        "Threats": NotRequired[List[ThreatPaginatorTypeDef]],
        "ThreatIntelIndicators": NotRequired[List[ThreatIntelIndicatorTypeDef]],
        "Compliance": NotRequired[CompliancePaginatorTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "WorkflowState": NotRequired[WorkflowStateType],
        "Workflow": NotRequired[WorkflowTypeDef],
        "RecordState": NotRequired[RecordStateType],
        "RelatedFindings": NotRequired[List[RelatedFindingTypeDef]],
        "Note": NotRequired[NoteTypeDef],
        "Vulnerabilities": NotRequired[List[VulnerabilityPaginatorTypeDef]],
        "PatchSummary": NotRequired[PatchSummaryTypeDef],
        "Action": NotRequired[ActionPaginatorTypeDef],
        "FindingProviderFields": NotRequired[FindingProviderFieldsPaginatorTypeDef],
        "Sample": NotRequired[bool],
        "GeneratorDetails": NotRequired[GeneratorDetailsPaginatorTypeDef],
        "ProcessedAt": NotRequired[str],
        "AwsAccountName": NotRequired[str],
    },
)
AwsSecurityFindingTypeDef = TypedDict(
    "AwsSecurityFindingTypeDef",
    {
        "SchemaVersion": str,
        "Id": str,
        "ProductArn": str,
        "GeneratorId": str,
        "AwsAccountId": str,
        "CreatedAt": str,
        "UpdatedAt": str,
        "Title": str,
        "Description": str,
        "Resources": Sequence[ResourceTypeDef],
        "ProductName": NotRequired[str],
        "CompanyName": NotRequired[str],
        "Region": NotRequired[str],
        "Types": NotRequired[Sequence[str]],
        "FirstObservedAt": NotRequired[str],
        "LastObservedAt": NotRequired[str],
        "Severity": NotRequired[SeverityTypeDef],
        "Confidence": NotRequired[int],
        "Criticality": NotRequired[int],
        "Remediation": NotRequired[RemediationTypeDef],
        "SourceUrl": NotRequired[str],
        "ProductFields": NotRequired[Mapping[str, str]],
        "UserDefinedFields": NotRequired[Mapping[str, str]],
        "Malware": NotRequired[Sequence[MalwareTypeDef]],
        "Network": NotRequired[NetworkTypeDef],
        "NetworkPath": NotRequired[Sequence[NetworkPathComponentTypeDef]],
        "Process": NotRequired[ProcessDetailsTypeDef],
        "Threats": NotRequired[Sequence[ThreatTypeDef]],
        "ThreatIntelIndicators": NotRequired[Sequence[ThreatIntelIndicatorTypeDef]],
        "Compliance": NotRequired[ComplianceTypeDef],
        "VerificationState": NotRequired[VerificationStateType],
        "WorkflowState": NotRequired[WorkflowStateType],
        "Workflow": NotRequired[WorkflowTypeDef],
        "RecordState": NotRequired[RecordStateType],
        "RelatedFindings": NotRequired[Sequence[RelatedFindingTypeDef]],
        "Note": NotRequired[NoteTypeDef],
        "Vulnerabilities": NotRequired[Sequence[VulnerabilityTypeDef]],
        "PatchSummary": NotRequired[PatchSummaryTypeDef],
        "Action": NotRequired[ActionTypeDef],
        "FindingProviderFields": NotRequired[FindingProviderFieldsTypeDef],
        "Sample": NotRequired[bool],
        "GeneratorDetails": NotRequired[GeneratorDetailsTypeDef],
        "ProcessedAt": NotRequired[str],
        "AwsAccountName": NotRequired[str],
    },
)
GetFindingsResponsePaginatorTypeDef = TypedDict(
    "GetFindingsResponsePaginatorTypeDef",
    {
        "Findings": List[AwsSecurityFindingPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchImportFindingsRequestRequestTypeDef = TypedDict(
    "BatchImportFindingsRequestRequestTypeDef",
    {
        "Findings": Sequence[AwsSecurityFindingTypeDef],
    },
)
GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "Findings": List[AwsSecurityFindingTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
