from infraflow.cdk.iam.base import IamAction


class A4BAssociateDeviceWithRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='AssociateDeviceWithRoom')


class A4BAssociateSkillGroupWithRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='AssociateSkillGroupWithRoom')


class A4BCreateProfile(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='CreateProfile')


class A4BCreateRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='CreateRoom')


class A4BCreateSkillGroup(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='CreateSkillGroup')


class A4BCreateUser(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='CreateUser')


class A4BDeleteProfile(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DeleteProfile')


class A4BDeleteRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DeleteRoom')


class A4BDeleteRoomSkillParameter(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DeleteRoomSkillParameter')


class A4BDeleteSkillGroup(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DeleteSkillGroup')


class A4BDeleteUser(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DeleteUser')


class A4BDisassociateDeviceFromRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DisassociateDeviceFromRoom')


class A4BDisassociateSkillGroupFromRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='DisassociateSkillGroupFromRoom')


class A4BGetDevice(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='GetDevice')


class A4BGetProfile(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='GetProfile')


class A4BGetRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='GetRoom')


class A4BGetRoomSkillParameter(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='GetRoomSkillParameter')


class A4BGetSkillGroup(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='GetSkillGroup')


class A4BListSkills(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='ListSkills')


class A4BListTags(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='ListTags')


class A4BPutRoomSkillParameter(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='PutRoomSkillParameter')


class A4BResolveRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='ResolveRoom')


class A4BRevokeInvitation(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='RevokeInvitation')


class A4BSearchDevices(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='SearchDevices')


class A4BSearchProfiles(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='SearchProfiles')


class A4BSearchRooms(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='SearchRooms')


class A4BSearchSkillGroups(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='SearchSkillGroups')


class A4BSearchUsers(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='SearchUsers')


class A4BSendInvitation(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='SendInvitation')


class A4BStartDeviceSync(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='StartDeviceSync')


class A4BTagResource(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='TagResource')


class A4BUntagResource(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='UntagResource')


class A4BUpdateDevice(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='UpdateDevice')


class A4BUpdateProfile(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='UpdateProfile')


class A4BUpdateRoom(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='UpdateRoom')


class A4BUpdateSkillGroup(IamAction):
    def __init__(self):
        super().__init__('a4b', pattern='UpdateSkillGroup')


class AcmAddTagsToCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='AddTagsToCertificate')


class AcmDeleteCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='DeleteCertificate')


class AcmDescribeCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='DescribeCertificate')


class AcmGetCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='GetCertificate')


class AcmImportCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='ImportCertificate')


class AcmListCertificates(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='ListCertificates')


class AcmListTagsForCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='ListTagsForCertificate')


class AcmRemoveTagsFromCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='RemoveTagsFromCertificate')


class AcmRequestCertificate(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='RequestCertificate')


class AcmResendValidationEmail(IamAction):
    def __init__(self):
        super().__init__('acm', pattern='ResendValidationEmail')


class ApiGatewayDELETE(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='DELETE')


class ApiGatewayGET(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='GET')


class ApiGatewayHEAD(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='HEAD')


class ApiGatewayOPTIONS(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='OPTIONS')


class ApiGatewayPATCH(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='PATCH')


class ApiGatewayPOST(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='POST')


class ApiGatewayPUT(IamAction):
    def __init__(self):
        super().__init__('apigateway', pattern='PUT')


class ApplicationAutoscalingDeleteScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DeleteScalingPolicy')


class ApplicationAutoscalingDeleteScheduledAction(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DeleteScheduledAction')


class ApplicationAutoscalingDeregisterScalableTarget(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DeregisterScalableTarget')


class ApplicationAutoscalingDescribeScalableTargets(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DescribeScalableTargets')


class ApplicationAutoscalingDescribeScalingActivities(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DescribeScalingActivities')


class ApplicationAutoscalingDescribeScalingPolicies(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DescribeScalingPolicies')


class ApplicationAutoscalingDescribeScheduledActions(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='DescribeScheduledActions')


class ApplicationAutoscalingPutScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='PutScalingPolicy')


class ApplicationAutoscalingPutScheduledAction(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='PutScheduledAction')


class ApplicationAutoscalingRegisterScalableTarget(IamAction):
    def __init__(self):
        super().__init__('application-autoscaling', pattern='RegisterScalableTarget')


class AppstreamAssociateFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='AssociateFleet')


class AppstreamCreateDirectoryConfig(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='CreateDirectoryConfig')


class AppstreamCreateFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='CreateFleet')


class AppstreamCreateImageBuilder(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='CreateImageBuilder')


class AppstreamCreateImageBuilderStreamingURL(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='CreateImageBuilderStreamingURL')


class AppstreamCreateStack(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='CreateStack')


class AppstreamCreateStreamingURL(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='CreateStreamingURL')


class AppstreamDeleteDirectoryConfig(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DeleteDirectoryConfig')


class AppstreamDeleteFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DeleteFleet')


class AppstreamDeleteImage(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DeleteImage')


class AppstreamDeleteImageBuilder(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DeleteImageBuilder')


class AppstreamDeleteStack(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DeleteStack')


class AppstreamDescribeDirectoryConfigs(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DescribeDirectoryConfigs')


class AppstreamDescribeFleets(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DescribeFleets')


class AppstreamDescribeImageBuilders(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DescribeImageBuilders')


class AppstreamDescribeImages(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DescribeImages')


class AppstreamDescribeSessions(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DescribeSessions')


class AppstreamDescribeStacks(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DescribeStacks')


class AppstreamDisassociateFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='DisassociateFleet')


class AppstreamExpireSession(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='ExpireSession')


class AppstreamListAssociatedFleets(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='ListAssociatedFleets')


class AppstreamListAssociatedStacks(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='ListAssociatedStacks')


class AppstreamListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='ListTagsForResource')


class AppstreamStartFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='StartFleet')


class AppstreamStartImageBuilder(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='StartImageBuilder')


class AppstreamStopFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='StopFleet')


class AppstreamStopImageBuilder(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='StopImageBuilder')


class AppstreamStream(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='Stream')


class AppstreamTagResource(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='TagResource')


class AppstreamUntagResource(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='UntagResource')


class AppstreamUpdateDirectoryConfig(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='UpdateDirectoryConfig')


class AppstreamUpdateFleet(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='UpdateFleet')


class AppstreamUpdateStack(IamAction):
    def __init__(self):
        super().__init__('appstream', pattern='UpdateStack')


class AppsyncCreateApiKey(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='CreateApiKey')


class AppsyncCreateDataSource(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='CreateDataSource')


class AppsyncCreateGraphqlApi(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='CreateGraphqlApi')


class AppsyncCreateResolver(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='CreateResolver')


class AppsyncCreateType(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='CreateType')


class AppsyncDeleteApiKey(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='DeleteApiKey')


class AppsyncDeleteDataSource(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='DeleteDataSource')


class AppsyncDeleteGraphqlApi(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='DeleteGraphqlApi')


class AppsyncDeleteResolver(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='DeleteResolver')


class AppsyncDeleteType(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='DeleteType')


class AppsyncGetDataSource(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GetDataSource')


class AppsyncGetGraphqlApi(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GetGraphqlApi')


class AppsyncGetIntrospectionSchema(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GetIntrospectionSchema')


class AppsyncGetResolver(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GetResolver')


class AppsyncGetSchemaCreationStatus(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GetSchemaCreationStatus')


class AppsyncGetType(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GetType')


class AppsyncGraphQL(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='GraphQL')


class AppsyncListApiKeys(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='ListApiKeys')


class AppsyncListDataSources(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='ListDataSources')


class AppsyncListGraphqlApis(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='ListGraphqlApis')


class AppsyncListResolvers(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='ListResolvers')


class AppsyncListTypes(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='ListTypes')


class AppsyncStartSchemaCreation(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='StartSchemaCreation')


class AppsyncUpdateApiKey(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='UpdateApiKey')


class AppsyncUpdateDataSource(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='UpdateDataSource')


class AppsyncUpdateGraphqlApi(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='UpdateGraphqlApi')


class AppsyncUpdateResolver(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='UpdateResolver')


class AppsyncUpdateType(IamAction):
    def __init__(self):
        super().__init__('appsync', pattern='UpdateType')


class ArtifactAcceptAgreement(IamAction):
    def __init__(self):
        super().__init__('artifact', pattern='AcceptAgreement')


class ArtifactDownloadAgreement(IamAction):
    def __init__(self):
        super().__init__('artifact', pattern='DownloadAgreement')


class ArtifactGet(IamAction):
    def __init__(self):
        super().__init__('artifact', pattern='Get')


class ArtifactTerminateAgreement(IamAction):
    def __init__(self):
        super().__init__('artifact', pattern='TerminateAgreement')


class AthenaBatchGetNamedQuery(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='BatchGetNamedQuery')


class AthenaBatchGetQueryExecution(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='BatchGetQueryExecution')


class AthenaCancelQueryExecution(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='CancelQueryExecution')


class AthenaCreateNamedQuery(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='CreateNamedQuery')


class AthenaDeleteNamedQuery(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='DeleteNamedQuery')


class AthenaGetCatalogs(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetCatalogs')


class AthenaGetExecutionEngine(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetExecutionEngine')


class AthenaGetExecutionEngines(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetExecutionEngines')


class AthenaGetNamedQuery(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetNamedQuery')


class AthenaGetNamespace(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetNamespace')


class AthenaGetNamespaces(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetNamespaces')


class AthenaGetQueryExecution(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetQueryExecution')


class AthenaGetQueryExecutions(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetQueryExecutions')


class AthenaGetQueryResults(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetQueryResults')


class AthenaGetTable(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetTable')


class AthenaGetTables(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='GetTables')


class AthenaListNamedQueries(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='ListNamedQueries')


class AthenaListQueryExecutions(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='ListQueryExecutions')


class AthenaRunQuery(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='RunQuery')


class AthenaStartQueryExecution(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='StartQueryExecution')


class AthenaStopQueryExecution(IamAction):
    def __init__(self):
        super().__init__('athena', pattern='StopQueryExecution')


class AutoscalingPlansCreateScalingPlan(IamAction):
    def __init__(self):
        super().__init__('autoscaling-plans', pattern='CreateScalingPlan')


class AutoscalingPlansDeleteScalingPlan(IamAction):
    def __init__(self):
        super().__init__('autoscaling-plans', pattern='DeleteScalingPlan')


class AutoscalingPlansDescribeScalingPlanResources(IamAction):
    def __init__(self):
        super().__init__('autoscaling-plans', pattern='DescribeScalingPlanResources')


class AutoscalingPlansDescribeScalingPlans(IamAction):
    def __init__(self):
        super().__init__('autoscaling-plans', pattern='DescribeScalingPlans')


class AutoscalingAttachInstances(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='AttachInstances')


class AutoscalingAttachLoadBalancerTargetGroups(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='AttachLoadBalancerTargetGroups')


class AutoscalingAttachLoadBalancers(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='AttachLoadBalancers')


class AutoscalingCompleteLifecycleAction(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='CompleteLifecycleAction')


class AutoscalingCreateAutoScalingGroup(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='CreateAutoScalingGroup')


class AutoscalingCreateLaunchConfiguration(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='CreateLaunchConfiguration')


class AutoscalingCreateOrUpdateTags(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='CreateOrUpdateTags')


class AutoscalingDeleteAutoScalingGroup(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeleteAutoScalingGroup')


class AutoscalingDeleteLaunchConfiguration(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeleteLaunchConfiguration')


class AutoscalingDeleteLifecycleHook(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeleteLifecycleHook')


class AutoscalingDeleteNotificationConfiguration(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeleteNotificationConfiguration')


class AutoscalingDeletePolicy(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeletePolicy')


class AutoscalingDeleteScheduledAction(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeleteScheduledAction')


class AutoscalingDeleteTags(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DeleteTags')


class AutoscalingDescribeAccountLimits(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeAccountLimits')


class AutoscalingDescribeAdjustmentTypes(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeAdjustmentTypes')


class AutoscalingDescribeAutoScalingGroups(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeAutoScalingGroups')


class AutoscalingDescribeAutoScalingInstances(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeAutoScalingInstances')


class AutoscalingDescribeAutoScalingNotificationTypes(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeAutoScalingNotificationTypes')


class AutoscalingDescribeLaunchConfigurations(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeLaunchConfigurations')


class AutoscalingDescribeLifecycleHookTypes(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeLifecycleHookTypes')


class AutoscalingDescribeLifecycleHooks(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeLifecycleHooks')


class AutoscalingDescribeLoadBalancerTargetGroups(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeLoadBalancerTargetGroups')


class AutoscalingDescribeLoadBalancers(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeLoadBalancers')


class AutoscalingDescribeMetricCollectionTypes(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeMetricCollectionTypes')


class AutoscalingDescribeNotificationConfigurations(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeNotificationConfigurations')


class AutoscalingDescribePolicies(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribePolicies')


class AutoscalingDescribeScalingActivities(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeScalingActivities')


class AutoscalingDescribeScalingProcessTypes(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeScalingProcessTypes')


class AutoscalingDescribeScheduledActions(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeScheduledActions')


class AutoscalingDescribeTags(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeTags')


class AutoscalingDescribeTerminationPolicyTypes(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DescribeTerminationPolicyTypes')


class AutoscalingDetachInstances(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DetachInstances')


class AutoscalingDetachLoadBalancerTargetGroups(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DetachLoadBalancerTargetGroups')


class AutoscalingDetachLoadBalancers(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DetachLoadBalancers')


class AutoscalingDisableMetricsCollection(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='DisableMetricsCollection')


class AutoscalingEnableMetricsCollection(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='EnableMetricsCollection')


class AutoscalingEnterStandby(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='EnterStandby')


class AutoscalingExecutePolicy(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='ExecutePolicy')


class AutoscalingExitStandby(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='ExitStandby')


class AutoscalingPutLifecycleHook(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='PutLifecycleHook')


class AutoscalingPutNotificationConfiguration(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='PutNotificationConfiguration')


class AutoscalingPutScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='PutScalingPolicy')


class AutoscalingPutScheduledUpdateGroupAction(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='PutScheduledUpdateGroupAction')


class AutoscalingRecordLifecycleActionHeartbeat(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='RecordLifecycleActionHeartbeat')


class AutoscalingResumeProcesses(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='ResumeProcesses')


class AutoscalingSetDesiredCapacity(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='SetDesiredCapacity')


class AutoscalingSetInstanceHealth(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='SetInstanceHealth')


class AutoscalingSetInstanceProtection(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='SetInstanceProtection')


class AutoscalingSuspendProcesses(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='SuspendProcesses')


class AutoscalingTerminateInstanceInAutoScalingGroup(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='TerminateInstanceInAutoScalingGroup')


class AutoscalingUpdateAutoScalingGroup(IamAction):
    def __init__(self):
        super().__init__('autoscaling', pattern='UpdateAutoScalingGroup')


class AwsMarketplaceManagementuploadFiles(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace-management', pattern='uploadFiles')


class AwsMarketplaceManagementviewMarketing(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace-management', pattern='viewMarketing')


class AwsMarketplaceManagementviewReports(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace-management', pattern='viewReports')


class AwsMarketplaceManagementviewSupport(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace-management', pattern='viewSupport')


class AwsMarketplaceBatchMeterUsage(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace', pattern='BatchMeterUsage')


class AwsMarketplaceMeterUsage(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace', pattern='MeterUsage')


class AwsMarketplaceResolveCustomer(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace', pattern='ResolveCustomer')


class AwsMarketplaceSubscribe(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace', pattern='Subscribe')


class AwsMarketplaceUnsubscribe(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace', pattern='Unsubscribe')


class AwsMarketplaceViewSubscriptions(IamAction):
    def __init__(self):
        super().__init__('aws-marketplace', pattern='ViewSubscriptions')


class AwsPortalModifyAccount(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ModifyAccount')


class AwsPortalModifyBilling(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ModifyBilling')


class AwsPortalModifyPaymentMethods(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ModifyPaymentMethods')


class AwsPortalViewAccount(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ViewAccount')


class AwsPortalViewBilling(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ViewBilling')


class AwsPortalViewPaymentMethods(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ViewPaymentMethods')


class AwsPortalViewUsage(IamAction):
    def __init__(self):
        super().__init__('aws-portal', pattern='ViewUsage')


class BatchCancelJob(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='CancelJob')


class BatchCreateComputeEnvironment(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='CreateComputeEnvironment')


class BatchCreateJobQueue(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='CreateJobQueue')


class BatchDeleteComputeEnvironment(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DeleteComputeEnvironment')


class BatchDeleteJobQueue(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DeleteJobQueue')


class BatchDeregisterJobDefinition(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DeregisterJobDefinition')


class BatchDescribeComputeEnvironments(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DescribeComputeEnvironments')


class BatchDescribeJobDefinitions(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DescribeJobDefinitions')


class BatchDescribeJobQueues(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DescribeJobQueues')


class BatchDescribeJobs(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='DescribeJobs')


class BatchListJobs(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='ListJobs')


class BatchRegisterJobDefinition(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='RegisterJobDefinition')


class BatchSubmitJob(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='SubmitJob')


class BatchTerminateJob(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='TerminateJob')


class BatchUpdateComputeEnvironment(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='UpdateComputeEnvironment')


class BatchUpdateJobQueue(IamAction):
    def __init__(self):
        super().__init__('batch', pattern='UpdateJobQueue')


class BudgetsModifyBudget(IamAction):
    def __init__(self):
        super().__init__('budgets', pattern='ModifyBudget')


class BudgetsViewBudget(IamAction):
    def __init__(self):
        super().__init__('budgets', pattern='ViewBudget')


class CeGetCostAndUsage(IamAction):
    def __init__(self):
        super().__init__('ce', pattern='GetCostAndUsage')


class CeGetDimensionValues(IamAction):
    def __init__(self):
        super().__init__('ce', pattern='GetDimensionValues')


class CeGetReservationUtilization(IamAction):
    def __init__(self):
        super().__init__('ce', pattern='GetReservationUtilization')


class CeGetTags(IamAction):
    def __init__(self):
        super().__init__('ce', pattern='GetTags')


class ChimeAcceptDelegate(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='AcceptDelegate')


class ChimeActivateUsers(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ActivateUsers')


class ChimeAddDomain(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='AddDomain')


class ChimeAddOrUpdateGroups(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='AddOrUpdateGroups')


class ChimeAuthorizeDirectory(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='AuthorizeDirectory')


class ChimeConnectDirectory(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ConnectDirectory')


class ChimeCreateAccount(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='CreateAccount')


class ChimeCreateCDRBucket(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='CreateCDRBucket')


class ChimeDeleteAccount(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='DeleteAccount')


class ChimeDeleteCDRBucket(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='DeleteCDRBucket')


class ChimeDeleteDelegate(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='DeleteDelegate')


class ChimeDeleteDomain(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='DeleteDomain')


class ChimeDeleteGroups(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='DeleteGroups')


class ChimeDisconnectDirectory(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='DisconnectDirectory')


class ChimeGetAccount(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetAccount')


class ChimeGetAccountResource(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetAccountResource')


class ChimeGetAccountSettings(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetAccountSettings')


class ChimeGetCDRBucket(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetCDRBucket')


class ChimeGetDomain(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetDomain')


class ChimeGetUser(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetUser')


class ChimeGetUserByEmail(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='GetUserByEmail')


class ChimeInviteDelegate(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='InviteDelegate')


class ChimeInviteUsers(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='InviteUsers')


class ChimeListAccounts(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListAccounts')


class ChimeListCDRBucket(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListCDRBucket')


class ChimeListDelegates(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListDelegates')


class ChimeListDirectories(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListDirectories')


class ChimeListDomains(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListDomains')


class ChimeListGroups(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListGroups')


class ChimeListUsers(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ListUsers')


class ChimeLogoutUser(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='LogoutUser')


class ChimeRenameAccount(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='RenameAccount')


class ChimeRenewDelegate(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='RenewDelegate')


class ChimeResetAccountResource(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ResetAccountResource')


class ChimeResetPersonalPin(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ResetPersonalPin')


class ChimeSubmitSupportRequest(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='SubmitSupportRequest')


class ChimeSuspendUsers(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='SuspendUsers')


class ChimeUnauthorizeDirectory(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='UnauthorizeDirectory')


class ChimeUpdateAccountResource(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='UpdateAccountResource')


class ChimeUpdateAccountSettings(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='UpdateAccountSettings')


class ChimeUpdateCDRBucket(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='UpdateCDRBucket')


class ChimeUpdateSupportedLicenses(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='UpdateSupportedLicenses')


class ChimeUpdateUserLicenses(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='UpdateUserLicenses')


class ChimeValidateAccountResource(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ValidateAccountResource')


class ChimeValidateDelegate(IamAction):
    def __init__(self):
        super().__init__('chime', pattern='ValidateDelegate')


class Cloud9CreateEnvironmentEC2(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='CreateEnvironmentEC2')


class Cloud9CreateEnvironmentMembership(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='CreateEnvironmentMembership')


class Cloud9CreateEnvironmentSSH(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='CreateEnvironmentSSH')


class Cloud9DeleteEnvironment(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='DeleteEnvironment')


class Cloud9DeleteEnvironmentMembership(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='DeleteEnvironmentMembership')


class Cloud9DescribeEnvironmentMemberships(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='DescribeEnvironmentMemberships')


class Cloud9DescribeEnvironmentStatus(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='DescribeEnvironmentStatus')


class Cloud9DescribeEnvironments(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='DescribeEnvironments')


class Cloud9GetUserPublicKey(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='GetUserPublicKey')


class Cloud9ListEnvironments(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='ListEnvironments')


class Cloud9UpdateEnvironment(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='UpdateEnvironment')


class Cloud9UpdateEnvironmentMembership(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='UpdateEnvironmentMembership')


class Cloud9ValidateEnvironmentName(IamAction):
    def __init__(self):
        super().__init__('cloud9', pattern='ValidateEnvironmentName')


class ClouddirectoryAddFacetToObject(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='AddFacetToObject')


class ClouddirectoryApplySchema(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ApplySchema')


class ClouddirectoryAttachObject(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='AttachObject')


class ClouddirectoryAttachPolicy(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='AttachPolicy')


class ClouddirectoryAttachToIndex(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='AttachToIndex')


class ClouddirectoryAttachTypedLink(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='AttachTypedLink')


class ClouddirectoryBatchRead(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='BatchRead')


class ClouddirectoryBatchWrite(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='BatchWrite')


class ClouddirectoryCreateDirectory(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='CreateDirectory')


class ClouddirectoryCreateFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='CreateFacet')


class ClouddirectoryCreateIndex(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='CreateIndex')


class ClouddirectoryCreateObject(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='CreateObject')


class ClouddirectoryCreateSchema(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='CreateSchema')


class ClouddirectoryCreateTypedLinkFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='CreateTypedLinkFacet')


class ClouddirectoryDeleteDirectory(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DeleteDirectory')


class ClouddirectoryDeleteFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DeleteFacet')


class ClouddirectoryDeleteObject(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DeleteObject')


class ClouddirectoryDeleteSchema(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DeleteSchema')


class ClouddirectoryDeleteTypedLinkFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DeleteTypedLinkFacet')


class ClouddirectoryDetachFromIndex(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DetachFromIndex')


class ClouddirectoryDetachObject(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DetachObject')


class ClouddirectoryDetachPolicy(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DetachPolicy')


class ClouddirectoryDetachTypedLink(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DetachTypedLink')


class ClouddirectoryDisableDirectory(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='DisableDirectory')


class ClouddirectoryEnableDirectory(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='EnableDirectory')


class ClouddirectoryGetDirectory(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='GetDirectory')


class ClouddirectoryGetFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='GetFacet')


class ClouddirectoryGetObjectInformation(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='GetObjectInformation')


class ClouddirectoryGetSchemaAsJson(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='GetSchemaAsJson')


class ClouddirectoryGetTypedLinkFacetInformation(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='GetTypedLinkFacetInformation')


class ClouddirectoryListAppliedSchemaArns(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListAppliedSchemaArns')


class ClouddirectoryListAttachedIndices(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListAttachedIndices')


class ClouddirectoryListDevelopmentSchemaArns(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListDevelopmentSchemaArns')


class ClouddirectoryListDirectories(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListDirectories')


class ClouddirectoryListFacetAttributes(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListFacetAttributes')


class ClouddirectoryListFacetNames(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListFacetNames')


class ClouddirectoryListIncomingTypedLinks(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListIncomingTypedLinks')


class ClouddirectoryListIndex(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListIndex')


class ClouddirectoryListObjectAttributes(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListObjectAttributes')


class ClouddirectoryListObjectChildren(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListObjectChildren')


class ClouddirectoryListObjectParentPaths(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListObjectParentPaths')


class ClouddirectoryListObjectParents(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListObjectParents')


class ClouddirectoryListObjectPolicies(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListObjectPolicies')


class ClouddirectoryListOutgoingTypedLinks(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListOutgoingTypedLinks')


class ClouddirectoryListPolicyAttachments(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListPolicyAttachments')


class ClouddirectoryListPublishedSchemaArns(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListPublishedSchemaArns')


class ClouddirectoryListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListTagsForResource')


class ClouddirectoryListTypedLinkFacetAttributes(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListTypedLinkFacetAttributes')


class ClouddirectoryListTypedLinkFacetNames(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='ListTypedLinkFacetNames')


class ClouddirectoryLookupPolicy(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='LookupPolicy')


class ClouddirectoryPublishSchema(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='PublishSchema')


class ClouddirectoryPutSchemaFromJson(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='PutSchemaFromJson')


class ClouddirectoryRemoveFacetFromObject(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='RemoveFacetFromObject')


class ClouddirectoryTagResource(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='TagResource')


class ClouddirectoryUntagResource(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='UntagResource')


class ClouddirectoryUpdateFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='UpdateFacet')


class ClouddirectoryUpdateObjectAttributes(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='UpdateObjectAttributes')


class ClouddirectoryUpdateSchema(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='UpdateSchema')


class ClouddirectoryUpdateTypedLinkFacet(IamAction):
    def __init__(self):
        super().__init__('clouddirectory', pattern='UpdateTypedLinkFacet')


class CloudformationCancelUpdateStack(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='CancelUpdateStack')


class CloudformationContinueUpdateRollback(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ContinueUpdateRollback')


class CloudformationCreateChangeSet(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='CreateChangeSet')


class CloudformationCreateStack(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='CreateStack')


class CloudformationCreateUploadBucket(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='CreateUploadBucket')


class CloudformationDeleteChangeSet(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DeleteChangeSet')


class CloudformationDeleteStack(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DeleteStack')


class CloudformationDescribeAccountLimits(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DescribeAccountLimits')


class CloudformationDescribeChangeSet(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DescribeChangeSet')


class CloudformationDescribeStackEvents(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DescribeStackEvents')


class CloudformationDescribeStackResource(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DescribeStackResource')


class CloudformationDescribeStackResources(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DescribeStackResources')


class CloudformationDescribeStacks(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='DescribeStacks')


class CloudformationEstimateTemplateCost(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='EstimateTemplateCost')


class CloudformationExecuteChangeSet(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ExecuteChangeSet')


class CloudformationGetStackPolicy(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='GetStackPolicy')


class CloudformationGetTemplate(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='GetTemplate')


class CloudformationGetTemplateSummary(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='GetTemplateSummary')


class CloudformationListChangeSets(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ListChangeSets')


class CloudformationListExports(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ListExports')


class CloudformationListImports(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ListImports')


class CloudformationListStackResources(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ListStackResources')


class CloudformationListStacks(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ListStacks')


class CloudformationPreviewStackUpdate(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='PreviewStackUpdate')


class CloudformationSetStackPolicy(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='SetStackPolicy')


class CloudformationSignalResource(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='SignalResource')


class CloudformationUpdateStack(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='UpdateStack')


class CloudformationUpdateTerminationProtection(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='UpdateTerminationProtection')


class CloudformationValidateTemplate(IamAction):
    def __init__(self):
        super().__init__('cloudformation', pattern='ValidateTemplate')


class CloudfrontCreateCloudFrontOriginAccessIdentity(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='CreateCloudFrontOriginAccessIdentity')


class CloudfrontCreateDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='CreateDistribution')


class CloudfrontCreateDistributionWithTags(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='CreateDistributionWithTags')


class CloudfrontCreateInvalidation(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='CreateInvalidation')


class CloudfrontCreateStreamingDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='CreateStreamingDistribution')


class CloudfrontCreateStreamingDistributionWithTags(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='CreateStreamingDistributionWithTags')


class CloudfrontDeleteCloudFrontOriginAccessIdentity(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='DeleteCloudFrontOriginAccessIdentity')


class CloudfrontDeleteDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='DeleteDistribution')


class CloudfrontDeleteStreamingDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='DeleteStreamingDistribution')


class CloudfrontGetCloudFrontOriginAccessIdentity(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetCloudFrontOriginAccessIdentity')


class CloudfrontGetCloudFrontOriginAccessIdentityConfig(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetCloudFrontOriginAccessIdentityConfig')


class CloudfrontGetDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetDistribution')


class CloudfrontGetDistributionConfig(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetDistributionConfig')


class CloudfrontGetInvalidation(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetInvalidation')


class CloudfrontGetStreamingDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetStreamingDistribution')


class CloudfrontGetStreamingDistributionConfig(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='GetStreamingDistributionConfig')


class CloudfrontListCloudFrontOriginAccessIdentities(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='ListCloudFrontOriginAccessIdentities')


class CloudfrontListDistributions(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='ListDistributions')


class CloudfrontListDistributionsByWebACLId(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='ListDistributionsByWebACLId')


class CloudfrontListInvalidations(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='ListInvalidations')


class CloudfrontListStreamingDistributions(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='ListStreamingDistributions')


class CloudfrontListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='ListTagsForResource')


class CloudfrontTagResource(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='TagResource')


class CloudfrontUntagResource(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='UntagResource')


class CloudfrontUpdateCloudFrontOriginAccessIdentity(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='UpdateCloudFrontOriginAccessIdentity')


class CloudfrontUpdateDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='UpdateDistribution')


class CloudfrontUpdateStreamingDistribution(IamAction):
    def __init__(self):
        super().__init__('cloudfront', pattern='UpdateStreamingDistribution')


class CloudhsmAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='AddTagsToResource')


class CloudhsmCreateHapg(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='CreateHapg')


class CloudhsmCreateHsm(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='CreateHsm')


class CloudhsmCreateLunaClient(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='CreateLunaClient')


class CloudhsmDeleteHapg(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='DeleteHapg')


class CloudhsmDeleteHsm(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='DeleteHsm')


class CloudhsmDeleteLunaClient(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='DeleteLunaClient')


class CloudhsmDescribeHapg(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='DescribeHapg')


class CloudhsmDescribeHsm(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='DescribeHsm')


class CloudhsmDescribeLunaClient(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='DescribeLunaClient')


class CloudhsmGetConfig(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='GetConfig')


class CloudhsmListAvailableZones(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ListAvailableZones')


class CloudhsmListHapgs(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ListHapgs')


class CloudhsmListHsms(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ListHsms')


class CloudhsmListLunaClients(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ListLunaClients')


class CloudhsmListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ListTagsForResource')


class CloudhsmModifyHapg(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ModifyHapg')


class CloudhsmModifyHsm(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ModifyHsm')


class CloudhsmModifyLunaClient(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='ModifyLunaClient')


class CloudhsmRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('cloudhsm', pattern='RemoveTagsFromResource')


class CloudsearchAddTags(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='AddTags')


class CloudsearchBuildSuggesters(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='BuildSuggesters')


class CloudsearchCreateDomain(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='CreateDomain')


class CloudsearchDefineAnalysisScheme(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DefineAnalysisScheme')


class CloudsearchDefineExpression(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DefineExpression')


class CloudsearchDefineIndexField(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DefineIndexField')


class CloudsearchDefineSuggester(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DefineSuggester')


class CloudsearchDeleteAnalysisScheme(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DeleteAnalysisScheme')


class CloudsearchDeleteDomain(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DeleteDomain')


class CloudsearchDeleteExpression(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DeleteExpression')


class CloudsearchDeleteIndexField(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DeleteIndexField')


class CloudsearchDeleteSuggester(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DeleteSuggester')


class CloudsearchDescribeAnalysisSchemes(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeAnalysisSchemes')


class CloudsearchDescribeAvailabilityOptions(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeAvailabilityOptions')


class CloudsearchDescribeDomains(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeDomains')


class CloudsearchDescribeExpressions(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeExpressions')


class CloudsearchDescribeIndexFields(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeIndexFields')


class CloudsearchDescribeScalingParameters(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeScalingParameters')


class CloudsearchDescribeServiceAccessPolicies(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeServiceAccessPolicies')


class CloudsearchDescribeSuggesters(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='DescribeSuggesters')


class CloudsearchIndexDocuments(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='IndexDocuments')


class CloudsearchListDomainNames(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='ListDomainNames')


class CloudsearchListTags(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='ListTags')


class CloudsearchRemoveTags(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='RemoveTags')


class CloudsearchUpdateAvailabilityOptions(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='UpdateAvailabilityOptions')


class CloudsearchUpdateScalingParameters(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='UpdateScalingParameters')


class CloudsearchUpdateServiceAccessPolicies(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='UpdateServiceAccessPolicies')


class Cloudsearchdocument(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='document')


class Cloudsearchsearch(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='search')


class Cloudsearchsuggest(IamAction):
    def __init__(self):
        super().__init__('cloudsearch', pattern='suggest')


class CloudtrailAddTags(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='AddTags')


class CloudtrailCreateTrail(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='CreateTrail')


class CloudtrailDeleteTrail(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='DeleteTrail')


class CloudtrailDescribeTrails(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='DescribeTrails')


class CloudtrailGetEventSelectors(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='GetEventSelectors')


class CloudtrailGetTrailStatus(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='GetTrailStatus')


class CloudtrailListPublicKeys(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='ListPublicKeys')


class CloudtrailListTags(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='ListTags')


class CloudtrailLookupEvents(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='LookupEvents')


class CloudtrailPutEventSelectors(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='PutEventSelectors')


class CloudtrailRemoveTags(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='RemoveTags')


class CloudtrailStartLogging(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='StartLogging')


class CloudtrailStopLogging(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='StopLogging')


class CloudtrailUpdateTrail(IamAction):
    def __init__(self):
        super().__init__('cloudtrail', pattern='UpdateTrail')


class CloudwatchDeleteAlarms(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='DeleteAlarms')


class CloudwatchDeleteDashboards(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='DeleteDashboards')


class CloudwatchDescribeAlarmHistory(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='DescribeAlarmHistory')


class CloudwatchDescribeAlarms(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='DescribeAlarms')


class CloudwatchDescribeAlarmsForMetric(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='DescribeAlarmsForMetric')


class CloudwatchDisableAlarmActions(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='DisableAlarmActions')


class CloudwatchEnableAlarmActions(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='EnableAlarmActions')


class CloudwatchGetDashboard(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='GetDashboard')


class CloudwatchGetMetricData(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='GetMetricData')


class CloudwatchGetMetricStatistics(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='GetMetricStatistics')


class CloudwatchListDashboards(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='ListDashboards')


class CloudwatchListMetrics(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='ListMetrics')


class CloudwatchPutDashboard(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='PutDashboard')


class CloudwatchPutMetricAlarm(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='PutMetricAlarm')


class CloudwatchPutMetricData(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='PutMetricData')


class CloudwatchSetAlarmState(IamAction):
    def __init__(self):
        super().__init__('cloudwatch', pattern='SetAlarmState')


class CodebuildBatchDeleteBuilds(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='BatchDeleteBuilds')


class CodebuildBatchGetBuilds(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='BatchGetBuilds')


class CodebuildBatchGetProjects(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='BatchGetProjects')


class CodebuildCreateProject(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='CreateProject')


class CodebuildDeleteProject(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='DeleteProject')


class CodebuildListBuilds(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='ListBuilds')


class CodebuildListBuildsForProject(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='ListBuildsForProject')


class CodebuildListConnectedOAuthAccounts(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='ListConnectedOAuthAccounts')


class CodebuildListCuratedEnvironmentImages(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='ListCuratedEnvironmentImages')


class CodebuildListProjects(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='ListProjects')


class CodebuildListRepositories(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='ListRepositories')


class CodebuildPersistOAuthToken(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='PersistOAuthToken')


class CodebuildStartBuild(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='StartBuild')


class CodebuildStopBuild(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='StopBuild')


class CodebuildUpdateProject(IamAction):
    def __init__(self):
        super().__init__('codebuild', pattern='UpdateProject')


class CodecommitBatchGetPullRequests(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='BatchGetPullRequests')


class CodecommitBatchGetRepositories(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='BatchGetRepositories')


class CodecommitCancelUploadArchive(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='CancelUploadArchive')


class CodecommitCreateBranch(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='CreateBranch')


class CodecommitCreatePullRequest(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='CreatePullRequest')


class CodecommitCreateRepository(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='CreateRepository')


class CodecommitDeleteBranch(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='DeleteBranch')


class CodecommitDeleteCommentContent(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='DeleteCommentContent')


class CodecommitDeleteRepository(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='DeleteRepository')


class CodecommitDescribePullRequestEvents(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='DescribePullRequestEvents')


class CodecommitGetBlob(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetBlob')


class CodecommitGetBranch(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetBranch')


class CodecommitGetComment(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetComment')


class CodecommitGetCommentsForComparedCommit(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetCommentsForComparedCommit')


class CodecommitGetCommentsForPullRequest(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetCommentsForPullRequest')


class CodecommitGetCommit(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetCommit')


class CodecommitGetCommitHistory(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetCommitHistory')


class CodecommitGetCommitsFromMergeBase(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetCommitsFromMergeBase')


class CodecommitGetDifferences(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetDifferences')


class CodecommitGetMergeConflicts(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetMergeConflicts')


class CodecommitGetObjectIdentifier(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetObjectIdentifier')


class CodecommitGetPullRequest(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetPullRequest')


class CodecommitGetReferences(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetReferences')


class CodecommitGetRepository(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetRepository')


class CodecommitGetRepositoryTriggers(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetRepositoryTriggers')


class CodecommitGetTree(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetTree')


class CodecommitGetUploadArchiveStatus(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GetUploadArchiveStatus')


class CodecommitGitPull(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GitPull')


class CodecommitGitPush(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='GitPush')


class CodecommitListBranches(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='ListBranches')


class CodecommitListPullRequests(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='ListPullRequests')


class CodecommitListRepositories(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='ListRepositories')


class CodecommitMergePullRequestByFastForward(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='MergePullRequestByFastForward')


class CodecommitPostCommentForComparedCommit(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='PostCommentForComparedCommit')


class CodecommitPostCommentForPullRequest(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='PostCommentForPullRequest')


class CodecommitPostCommentReply(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='PostCommentReply')


class CodecommitPutFile(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='PutFile')


class CodecommitPutRepositoryTriggers(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='PutRepositoryTriggers')


class CodecommitTestRepositoryTriggers(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='TestRepositoryTriggers')


class CodecommitUpdateComment(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdateComment')


class CodecommitUpdateDefaultBranch(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdateDefaultBranch')


class CodecommitUpdatePullRequestDescription(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdatePullRequestDescription')


class CodecommitUpdatePullRequestStatus(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdatePullRequestStatus')


class CodecommitUpdatePullRequestTitle(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdatePullRequestTitle')


class CodecommitUpdateRepositoryDescription(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdateRepositoryDescription')


class CodecommitUpdateRepositoryName(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UpdateRepositoryName')


class CodecommitUploadArchive(IamAction):
    def __init__(self):
        super().__init__('codecommit', pattern='UploadArchive')


class CodedeployAddTagsToOnPremisesInstances(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='AddTagsToOnPremisesInstances')


class CodedeployBatchGetApplicationRevisions(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='BatchGetApplicationRevisions')


class CodedeployBatchGetApplications(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='BatchGetApplications')


class CodedeployBatchGetDeploymentGroups(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='BatchGetDeploymentGroups')


class CodedeployBatchGetDeploymentInstances(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='BatchGetDeploymentInstances')


class CodedeployBatchGetDeployments(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='BatchGetDeployments')


class CodedeployBatchGetOnPremisesInstances(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='BatchGetOnPremisesInstances')


class CodedeployContinueDeployment(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ContinueDeployment')


class CodedeployCreateApplication(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='CreateApplication')


class CodedeployCreateDeployment(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='CreateDeployment')


class CodedeployCreateDeploymentConfig(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='CreateDeploymentConfig')


class CodedeployCreateDeploymentGroup(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='CreateDeploymentGroup')


class CodedeployDeleteApplication(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='DeleteApplication')


class CodedeployDeleteDeploymentConfig(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='DeleteDeploymentConfig')


class CodedeployDeleteDeploymentGroup(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='DeleteDeploymentGroup')


class CodedeployDeregisterOnPremisesInstance(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='DeregisterOnPremisesInstance')


class CodedeployGetApplication(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetApplication')


class CodedeployGetApplicationRevision(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetApplicationRevision')


class CodedeployGetDeployment(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetDeployment')


class CodedeployGetDeploymentConfig(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetDeploymentConfig')


class CodedeployGetDeploymentGroup(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetDeploymentGroup')


class CodedeployGetDeploymentInstance(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetDeploymentInstance')


class CodedeployGetOnPremisesInstance(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='GetOnPremisesInstance')


class CodedeployListApplicationRevisions(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListApplicationRevisions')


class CodedeployListApplications(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListApplications')


class CodedeployListDeploymentConfigs(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListDeploymentConfigs')


class CodedeployListDeploymentGroups(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListDeploymentGroups')


class CodedeployListDeploymentInstances(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListDeploymentInstances')


class CodedeployListDeployments(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListDeployments')


class CodedeployListOnPremisesInstances(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='ListOnPremisesInstances')


class CodedeployRegisterApplicationRevision(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='RegisterApplicationRevision')


class CodedeployRegisterOnPremisesInstance(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='RegisterOnPremisesInstance')


class CodedeployRemoveTagsFromOnPremisesInstances(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='RemoveTagsFromOnPremisesInstances')


class CodedeployStopDeployment(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='StopDeployment')


class CodedeployUpdateApplication(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='UpdateApplication')


class CodedeployUpdateDeploymentGroup(IamAction):
    def __init__(self):
        super().__init__('codedeploy', pattern='UpdateDeploymentGroup')


class CodepipelineAcknowledgeJob(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='AcknowledgeJob')


class CodepipelineAcknowledgeThirdPartyJob(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='AcknowledgeThirdPartyJob')


class CodepipelineCreateCustomActionType(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='CreateCustomActionType')


class CodepipelineCreatePipeline(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='CreatePipeline')


class CodepipelineDeleteCustomActionType(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='DeleteCustomActionType')


class CodepipelineDeletePipeline(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='DeletePipeline')


class CodepipelineDisableStageTransition(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='DisableStageTransition')


class CodepipelineEnableStageTransition(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='EnableStageTransition')


class CodepipelineGetJobDetails(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='GetJobDetails')


class CodepipelineGetPipeline(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='GetPipeline')


class CodepipelineGetPipelineExecution(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='GetPipelineExecution')


class CodepipelineGetPipelineState(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='GetPipelineState')


class CodepipelineGetThirdPartyJobDetails(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='GetThirdPartyJobDetails')


class CodepipelineListActionTypes(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='ListActionTypes')


class CodepipelineListPipelineExecutions(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='ListPipelineExecutions')


class CodepipelineListPipelines(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='ListPipelines')


class CodepipelinePollForJobs(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PollForJobs')


class CodepipelinePollForThirdPartyJobs(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PollForThirdPartyJobs')


class CodepipelinePutActionRevision(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PutActionRevision')


class CodepipelinePutApprovalResult(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PutApprovalResult')


class CodepipelinePutJobFailureResult(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PutJobFailureResult')


class CodepipelinePutJobSuccessResult(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PutJobSuccessResult')


class CodepipelinePutThirdPartyJobFailureResult(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PutThirdPartyJobFailureResult')


class CodepipelinePutThirdPartyJobSuccessResult(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='PutThirdPartyJobSuccessResult')


class CodepipelineRetryStageExecution(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='RetryStageExecution')


class CodepipelineStartPipelineExecution(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='StartPipelineExecution')


class CodepipelineUpdatePipeline(IamAction):
    def __init__(self):
        super().__init__('codepipeline', pattern='UpdatePipeline')


class CodestarAssociateTeamMember(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='AssociateTeamMember')


class CodestarCreateProject(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='CreateProject')


class CodestarCreateUserProfile(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='CreateUserProfile')


class CodestarDeleteExtendedAccess(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='DeleteExtendedAccess')


class CodestarDeleteProject(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='DeleteProject')


class CodestarDeleteUserProfile(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='DeleteUserProfile')


class CodestarDescribeProject(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='DescribeProject')


class CodestarDescribeUserProfile(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='DescribeUserProfile')


class CodestarDisassociateTeamMember(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='DisassociateTeamMember')


class CodestarGetExtendedAccess(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='GetExtendedAccess')


class CodestarListProjects(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='ListProjects')


class CodestarListResources(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='ListResources')


class CodestarListTeamMembers(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='ListTeamMembers')


class CodestarListUserProfiles(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='ListUserProfiles')


class CodestarPutExtendedAccess(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='PutExtendedAccess')


class CodestarUpdateProject(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='UpdateProject')


class CodestarUpdateTeamMember(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='UpdateTeamMember')


class CodestarUpdateUserProfile(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='UpdateUserProfile')


class CodestarVerifyServiceRole(IamAction):
    def __init__(self):
        super().__init__('codestar', pattern='VerifyServiceRole')


class CognitoIdentityCreateIdentityPool(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='CreateIdentityPool')


class CognitoIdentityDeleteIdentities(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='DeleteIdentities')


class CognitoIdentityDeleteIdentityPool(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='DeleteIdentityPool')


class CognitoIdentityDescribeIdentity(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='DescribeIdentity')


class CognitoIdentityDescribeIdentityPool(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='DescribeIdentityPool')


class CognitoIdentityGetCredentialsForIdentity(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='GetCredentialsForIdentity')


class CognitoIdentityGetId(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='GetId')


class CognitoIdentityGetIdentityPoolRoles(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='GetIdentityPoolRoles')


class CognitoIdentityGetOpenIdToken(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='GetOpenIdToken')


class CognitoIdentityGetOpenIdTokenForDeveloperIdentity(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='GetOpenIdTokenForDeveloperIdentity')


class CognitoIdentityListIdentities(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='ListIdentities')


class CognitoIdentityListIdentityPools(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='ListIdentityPools')


class CognitoIdentityLookupDeveloperIdentity(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='LookupDeveloperIdentity')


class CognitoIdentityMergeDeveloperIdentities(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='MergeDeveloperIdentities')


class CognitoIdentitySetIdentityPoolRoles(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='SetIdentityPoolRoles')


class CognitoIdentityUnlinkDeveloperIdentity(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='UnlinkDeveloperIdentity')


class CognitoIdentityUnlinkIdentity(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='UnlinkIdentity')


class CognitoIdentityUpdateIdentityPool(IamAction):
    def __init__(self):
        super().__init__('cognito-identity', pattern='UpdateIdentityPool')


class CognitoIdpAddCustomAttributes(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AddCustomAttributes')


class CognitoIdpAdminAddUserToGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminAddUserToGroup')


class CognitoIdpAdminConfirmSignUp(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminConfirmSignUp')


class CognitoIdpAdminCreateUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminCreateUser')


class CognitoIdpAdminDeleteUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminDeleteUser')


class CognitoIdpAdminDeleteUserAttributes(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminDeleteUserAttributes')


class CognitoIdpAdminDisableUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminDisableUser')


class CognitoIdpAdminEnableUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminEnableUser')


class CognitoIdpAdminForgetDevice(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminForgetDevice')


class CognitoIdpAdminGetDevice(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminGetDevice')


class CognitoIdpAdminGetUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminGetUser')


class CognitoIdpAdminInitiateAuth(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminInitiateAuth')


class CognitoIdpAdminListDevices(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminListDevices')


class CognitoIdpAdminListGroupsForUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminListGroupsForUser')


class CognitoIdpAdminListUserAuthEvents(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminListUserAuthEvents')


class CognitoIdpAdminRemoveUserFromGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminRemoveUserFromGroup')


class CognitoIdpAdminResetUserPassword(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminResetUserPassword')


class CognitoIdpAdminRespondToAuthChallenge(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminRespondToAuthChallenge')


class CognitoIdpAdminSetUserMFAPreference(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminSetUserMFAPreference')


class CognitoIdpAdminSetUserSettings(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminSetUserSettings')


class CognitoIdpAdminUpdateAuthEventFeedback(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminUpdateAuthEventFeedback')


class CognitoIdpAdminUpdateDeviceStatus(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminUpdateDeviceStatus')


class CognitoIdpAdminUpdateUserAttributes(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminUpdateUserAttributes')


class CognitoIdpAdminUserGlobalSignOut(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='AdminUserGlobalSignOut')


class CognitoIdpChangePassword(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ChangePassword')


class CognitoIdpConfirmDevice(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ConfirmDevice')


class CognitoIdpConfirmForgotPassword(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ConfirmForgotPassword')


class CognitoIdpConfirmSignUp(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ConfirmSignUp')


class CognitoIdpCreateGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='CreateGroup')


class CognitoIdpCreateUserImportJob(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='CreateUserImportJob')


class CognitoIdpCreateUserPool(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='CreateUserPool')


class CognitoIdpCreateUserPoolClient(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='CreateUserPoolClient')


class CognitoIdpDeleteGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DeleteGroup')


class CognitoIdpDeleteUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DeleteUser')


class CognitoIdpDeleteUserAttributes(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DeleteUserAttributes')


class CognitoIdpDeleteUserPool(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DeleteUserPool')


class CognitoIdpDeleteUserPoolClient(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DeleteUserPoolClient')


class CognitoIdpDescribeRiskConfiguration(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DescribeRiskConfiguration')


class CognitoIdpDescribeUserImportJob(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DescribeUserImportJob')


class CognitoIdpDescribeUserPool(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DescribeUserPool')


class CognitoIdpDescribeUserPoolClient(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='DescribeUserPoolClient')


class CognitoIdpForgetDevice(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ForgetDevice')


class CognitoIdpForgotPassword(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ForgotPassword')


class CognitoIdpGetCSVHeader(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GetCSVHeader')


class CognitoIdpGetDevice(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GetDevice')


class CognitoIdpGetGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GetGroup')


class CognitoIdpGetUser(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GetUser')


class CognitoIdpGetUserAttributeVerificationCode(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GetUserAttributeVerificationCode')


class CognitoIdpGetUserPoolMfaConfig(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GetUserPoolMfaConfig')


class CognitoIdpGlobalSignOut(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='GlobalSignOut')


class CognitoIdpInitiateAuth(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='InitiateAuth')


class CognitoIdpListDevices(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ListDevices')


class CognitoIdpListGroups(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ListGroups')


class CognitoIdpListUserImportJobs(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ListUserImportJobs')


class CognitoIdpListUserPoolClients(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ListUserPoolClients')


class CognitoIdpListUsersInGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ListUsersInGroup')


class CognitoIdpResendConfirmationCode(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='ResendConfirmationCode')


class CognitoIdpRespondToAuthChallenge(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='RespondToAuthChallenge')


class CognitoIdpSetRiskConfiguration(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='SetRiskConfiguration')


class CognitoIdpSetUserMFAPreference(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='SetUserMFAPreference')


class CognitoIdpSetUserPoolMfaConfig(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='SetUserPoolMfaConfig')


class CognitoIdpSetUserSettings(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='SetUserSettings')


class CognitoIdpSignUp(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='SignUp')


class CognitoIdpStartUserImportJob(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='StartUserImportJob')


class CognitoIdpStopUserImportJob(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='StopUserImportJob')


class CognitoIdpUpdateAuthEventFeedback(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='UpdateAuthEventFeedback')


class CognitoIdpUpdateDeviceStatus(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='UpdateDeviceStatus')


class CognitoIdpUpdateGroup(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='UpdateGroup')


class CognitoIdpUpdateUserAttributes(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='UpdateUserAttributes')


class CognitoIdpUpdateUserPool(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='UpdateUserPool')


class CognitoIdpUpdateUserPoolClient(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='UpdateUserPoolClient')


class CognitoIdpVerifyUserAttribute(IamAction):
    def __init__(self):
        super().__init__('cognito-idp', pattern='VerifyUserAttribute')


class CognitoSyncBulkPublish(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='BulkPublish')


class CognitoSyncDeleteDataset(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='DeleteDataset')


class CognitoSyncDescribeDataset(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='DescribeDataset')


class CognitoSyncDescribeIdentityPoolUsage(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='DescribeIdentityPoolUsage')


class CognitoSyncDescribeIdentityUsage(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='DescribeIdentityUsage')


class CognitoSyncGetBulkPublishDetails(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='GetBulkPublishDetails')


class CognitoSyncGetCognitoEvents(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='GetCognitoEvents')


class CognitoSyncGetIdentityPoolConfiguration(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='GetIdentityPoolConfiguration')


class CognitoSyncListDatasets(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='ListDatasets')


class CognitoSyncListIdentityPoolUsage(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='ListIdentityPoolUsage')


class CognitoSyncListRecords(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='ListRecords')


class CognitoSyncQueryRecords(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='QueryRecords')


class CognitoSyncRegisterDevice(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='RegisterDevice')


class CognitoSyncSetCognitoEvents(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='SetCognitoEvents')


class CognitoSyncSetDatasetConfiguration(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='SetDatasetConfiguration')


class CognitoSyncSetIdentityPoolConfiguration(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='SetIdentityPoolConfiguration')


class CognitoSyncSubscribeToDataset(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='SubscribeToDataset')


class CognitoSyncUnsubscribeFromDataset(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='UnsubscribeFromDataset')


class CognitoSyncUpdateRecords(IamAction):
    def __init__(self):
        super().__init__('cognito-sync', pattern='UpdateRecords')


class ComprehendBatchDetectDominantLanguage(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='BatchDetectDominantLanguage')


class ComprehendBatchDetectEntities(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='BatchDetectEntities')


class ComprehendBatchDetectKeyPhrases(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='BatchDetectKeyPhrases')


class ComprehendBatchDetectSentiment(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='BatchDetectSentiment')


class ComprehendDescribeTopicsDetectionJob(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='DescribeTopicsDetectionJob')


class ComprehendDetectDominantLanguage(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='DetectDominantLanguage')


class ComprehendDetectEntities(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='DetectEntities')


class ComprehendDetectKeyPhrases(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='DetectKeyPhrases')


class ComprehendDetectSentiment(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='DetectSentiment')


class ComprehendListTopicsDetectionJobs(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='ListTopicsDetectionJobs')


class ComprehendStartTopicsDetectionJob(IamAction):
    def __init__(self):
        super().__init__('comprehend', pattern='StartTopicsDetectionJob')


class ConfigDeleteConfigRule(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DeleteConfigRule')


class ConfigDeleteConfigurationRecorder(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DeleteConfigurationRecorder')


class ConfigDeleteDeliveryChannel(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DeleteDeliveryChannel')


class ConfigDeleteEvaluationResults(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DeleteEvaluationResults')


class ConfigDeliverConfigSnapshot(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DeliverConfigSnapshot')


class ConfigDescribeComplianceByConfigRule(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeComplianceByConfigRule')


class ConfigDescribeComplianceByResource(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeComplianceByResource')


class ConfigDescribeConfigRuleEvaluationStatus(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeConfigRuleEvaluationStatus')


class ConfigDescribeConfigRules(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeConfigRules')


class ConfigDescribeConfigurationRecorderStatus(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeConfigurationRecorderStatus')


class ConfigDescribeConfigurationRecorders(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeConfigurationRecorders')


class ConfigDescribeDeliveryChannelStatus(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeDeliveryChannelStatus')


class ConfigDescribeDeliveryChannels(IamAction):
    def __init__(self):
        super().__init__('config', pattern='DescribeDeliveryChannels')


class ConfigGetComplianceDetailsByConfigRule(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetComplianceDetailsByConfigRule')


class ConfigGetComplianceDetailsByResource(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetComplianceDetailsByResource')


class ConfigGetComplianceSummaryByConfigRule(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetComplianceSummaryByConfigRule')


class ConfigGetComplianceSummaryByResourceType(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetComplianceSummaryByResourceType')


class ConfigGetResourceConfigHistory(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetResourceConfigHistory')


class ConfigGetResources(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetResources')


class ConfigGetTagKeys(IamAction):
    def __init__(self):
        super().__init__('config', pattern='GetTagKeys')


class ConfigListDiscoveredResources(IamAction):
    def __init__(self):
        super().__init__('config', pattern='ListDiscoveredResources')


class ConfigPutConfigRule(IamAction):
    def __init__(self):
        super().__init__('config', pattern='PutConfigRule')


class ConfigPutConfigurationRecorder(IamAction):
    def __init__(self):
        super().__init__('config', pattern='PutConfigurationRecorder')


class ConfigPutDeliveryChannel(IamAction):
    def __init__(self):
        super().__init__('config', pattern='PutDeliveryChannel')


class ConfigPutEvaluations(IamAction):
    def __init__(self):
        super().__init__('config', pattern='PutEvaluations')


class ConfigStartConfigRulesEvaluation(IamAction):
    def __init__(self):
        super().__init__('config', pattern='StartConfigRulesEvaluation')


class ConfigStartConfigurationRecorder(IamAction):
    def __init__(self):
        super().__init__('config', pattern='StartConfigurationRecorder')


class ConfigStopConfigurationRecorder(IamAction):
    def __init__(self):
        super().__init__('config', pattern='StopConfigurationRecorder')


class ConnectCreateInstance(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='CreateInstance')


class ConnectDescribeInstance(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='DescribeInstance')


class ConnectDestroyInstance(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='DestroyInstance')


class ConnectGetFederationToken(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='GetFederationToken')


class ConnectGetFederationTokens(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='GetFederationTokens')


class ConnectListInstances(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='ListInstances')


class ConnectModifyInstance(IamAction):
    def __init__(self):
        super().__init__('connect', pattern='ModifyInstance')


class CrowdGetTask(IamAction):
    def __init__(self):
        super().__init__('crowd', pattern='GetTask')


class CrowdPutTask(IamAction):
    def __init__(self):
        super().__init__('crowd', pattern='PutTask')


class CurDeleteReportDefinition(IamAction):
    def __init__(self):
        super().__init__('cur', pattern='DeleteReportDefinition')


class CurDescribeReportDefinitions(IamAction):
    def __init__(self):
        super().__init__('cur', pattern='DescribeReportDefinitions')


class CurPutReportDefinition(IamAction):
    def __init__(self):
        super().__init__('cur', pattern='PutReportDefinition')


class DatapipelineActivatePipeline(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='ActivatePipeline')


class DatapipelineAddTags(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='AddTags')


class DatapipelineCreatePipeline(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='CreatePipeline')


class DatapipelineDeactivatePipeline(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='DeactivatePipeline')


class DatapipelineDeletePipeline(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='DeletePipeline')


class DatapipelineDescribeObjects(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='DescribeObjects')


class DatapipelineDescribePipelines(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='DescribePipelines')


class DatapipelineEvaluateExpression(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='EvaluateExpression')


class DatapipelineGetAccountLimits(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='GetAccountLimits')


class DatapipelineGetPipelineDefinition(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='GetPipelineDefinition')


class DatapipelineListPipelines(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='ListPipelines')


class DatapipelinePollForTask(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='PollForTask')


class DatapipelinePutAccountLimits(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='PutAccountLimits')


class DatapipelinePutPipelineDefinition(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='PutPipelineDefinition')


class DatapipelineQueryObjects(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='QueryObjects')


class DatapipelineRemoveTags(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='RemoveTags')


class DatapipelineReportTaskProgress(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='ReportTaskProgress')


class DatapipelineReportTaskRunnerHeartbeat(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='ReportTaskRunnerHeartbeat')


class DatapipelineSetStatus(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='SetStatus')


class DatapipelineSetTaskStatus(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='SetTaskStatus')


class DatapipelineValidatePipelineDefinition(IamAction):
    def __init__(self):
        super().__init__('datapipeline', pattern='ValidatePipelineDefinition')


class DaxBatchGetItem(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='BatchGetItem')


class DaxBatchWriteItem(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='BatchWriteItem')


class DaxCreateCluster(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='CreateCluster')


class DaxCreateParameterGroup(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='CreateParameterGroup')


class DaxCreateSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='CreateSubnetGroup')


class DaxDecreaseReplicationFactor(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DecreaseReplicationFactor')


class DaxDeleteCluster(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DeleteCluster')


class DaxDeleteItem(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DeleteItem')


class DaxDeleteParameterGroup(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DeleteParameterGroup')


class DaxDeleteSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DeleteSubnetGroup')


class DaxDescribeClusters(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeClusters')


class DaxDescribeDefaultParameters(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeDefaultParameters')


class DaxDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeEvents')


class DaxDescribeParameterGroups(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeParameterGroups')


class DaxDescribeParameters(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeParameters')


class DaxDescribeSubnetGroups(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeSubnetGroups')


class DaxDescribeTable(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='DescribeTable')


class DaxGetItem(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='GetItem')


class DaxIncreaseReplicationFactor(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='IncreaseReplicationFactor')


class DaxListTables(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='ListTables')


class DaxListTags(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='ListTags')


class DaxPutItem(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='PutItem')


class DaxQuery(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='Query')


class DaxRebootNode(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='RebootNode')


class DaxScan(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='Scan')


class DaxTagResource(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='TagResource')


class DaxUntagResource(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='UntagResource')


class DaxUpdateCluster(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='UpdateCluster')


class DaxUpdateItem(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='UpdateItem')


class DaxUpdateParameterGroup(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='UpdateParameterGroup')


class DaxUpdateSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('dax', pattern='UpdateSubnetGroup')


class DevicefarmCreateDevicePool(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='CreateDevicePool')


class DevicefarmCreateNetworkProfile(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='CreateNetworkProfile')


class DevicefarmCreateProject(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='CreateProject')


class DevicefarmCreateRemoteAccessSession(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='CreateRemoteAccessSession')


class DevicefarmCreateUpload(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='CreateUpload')


class DevicefarmDeleteDevicePool(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='DeleteDevicePool')


class DevicefarmDeleteNetworkProfile(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='DeleteNetworkProfile')


class DevicefarmDeleteProject(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='DeleteProject')


class DevicefarmDeleteRemoteAccessSession(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='DeleteRemoteAccessSession')


class DevicefarmDeleteRun(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='DeleteRun')


class DevicefarmDeleteUpload(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='DeleteUpload')


class DevicefarmGetAccountSettings(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetAccountSettings')


class DevicefarmGetDevice(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetDevice')


class DevicefarmGetDevicePool(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetDevicePool')


class DevicefarmGetDevicePoolCompatibility(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetDevicePoolCompatibility')


class DevicefarmGetJob(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetJob')


class DevicefarmGetNetworkProfile(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetNetworkProfile')


class DevicefarmGetOfferingStatus(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetOfferingStatus')


class DevicefarmGetProject(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetProject')


class DevicefarmGetRemoteAccessSession(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetRemoteAccessSession')


class DevicefarmGetRun(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetRun')


class DevicefarmGetSuite(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetSuite')


class DevicefarmGetTest(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetTest')


class DevicefarmGetUpload(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='GetUpload')


class DevicefarmInstallToRemoteAccessSession(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='InstallToRemoteAccessSession')


class DevicefarmListArtifacts(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListArtifacts')


class DevicefarmListDevicePools(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListDevicePools')


class DevicefarmListDevices(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListDevices')


class DevicefarmListJobs(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListJobs')


class DevicefarmListNetworkProfiles(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListNetworkProfiles')


class DevicefarmListOfferingTransactions(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListOfferingTransactions')


class DevicefarmListOfferings(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListOfferings')


class DevicefarmListProjects(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListProjects')


class DevicefarmListRemoteAccessSessions(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListRemoteAccessSessions')


class DevicefarmListRuns(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListRuns')


class DevicefarmListSamples(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListSamples')


class DevicefarmListSuites(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListSuites')


class DevicefarmListTests(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListTests')


class DevicefarmListUniqueProblems(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListUniqueProblems')


class DevicefarmListUploads(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ListUploads')


class DevicefarmPurchaseOffering(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='PurchaseOffering')


class DevicefarmRenewOffering(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='RenewOffering')


class DevicefarmScheduleRun(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='ScheduleRun')


class DevicefarmStopRemoteAccessSession(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='StopRemoteAccessSession')


class DevicefarmStopRun(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='StopRun')


class DevicefarmUpdateDevicePool(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='UpdateDevicePool')


class DevicefarmUpdateNetworkProfile(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='UpdateNetworkProfile')


class DevicefarmUpdateProject(IamAction):
    def __init__(self):
        super().__init__('devicefarm', pattern='UpdateProject')


class DirectconnectAllocateConnectionOnInterconnect(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='AllocateConnectionOnInterconnect')


class DirectconnectAllocatePrivateVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='AllocatePrivateVirtualInterface')


class DirectconnectAllocatePublicVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='AllocatePublicVirtualInterface')


class DirectconnectConfirmConnection(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='ConfirmConnection')


class DirectconnectConfirmPrivateVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='ConfirmPrivateVirtualInterface')


class DirectconnectConfirmPublicVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='ConfirmPublicVirtualInterface')


class DirectconnectCreateConnection(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='CreateConnection')


class DirectconnectCreateInterconnect(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='CreateInterconnect')


class DirectconnectCreatePrivateVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='CreatePrivateVirtualInterface')


class DirectconnectCreatePublicVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='CreatePublicVirtualInterface')


class DirectconnectDeleteConnection(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DeleteConnection')


class DirectconnectDeleteInterconnect(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DeleteInterconnect')


class DirectconnectDeleteVirtualInterface(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DeleteVirtualInterface')


class DirectconnectDescribeConnectionLoa(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeConnectionLoa')


class DirectconnectDescribeConnections(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeConnections')


class DirectconnectDescribeConnectionsOnInterconnect(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeConnectionsOnInterconnect')


class DirectconnectDescribeInterconnectLoa(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeInterconnectLoa')


class DirectconnectDescribeInterconnects(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeInterconnects')


class DirectconnectDescribeLocations(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeLocations')


class DirectconnectDescribeVirtualGateways(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeVirtualGateways')


class DirectconnectDescribeVirtualInterfaces(IamAction):
    def __init__(self):
        super().__init__('directconnect', pattern='DescribeVirtualInterfaces')


class DiscoveryAssociateConfigurationItemsToApplication(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='AssociateConfigurationItemsToApplication')


class DiscoveryCreateApplication(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='CreateApplication')


class DiscoveryCreateTags(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='CreateTags')


class DiscoveryDeleteApplications(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DeleteApplications')


class DiscoveryDeleteTags(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DeleteTags')


class DiscoveryDescribeAgents(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DescribeAgents')


class DiscoveryDescribeConfigurations(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DescribeConfigurations')


class DiscoveryDescribeExportConfigurations(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DescribeExportConfigurations')


class DiscoveryDescribeTags(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DescribeTags')


class DiscoveryDisassociateConfigurationItemsFromApplication(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='DisassociateConfigurationItemsFromApplication')


class DiscoveryExportConfigurations(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='ExportConfigurations')


class DiscoveryGetDiscoverySummary(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='GetDiscoverySummary')


class DiscoveryListConfigurations(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='ListConfigurations')


class DiscoveryListServerNeighbors(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='ListServerNeighbors')


class DiscoveryStartDataCollectionByAgentIds(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='StartDataCollectionByAgentIds')


class DiscoveryStartExportTask(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='StartExportTask')


class DiscoveryStopDataCollectionByAgentIds(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='StopDataCollectionByAgentIds')


class DiscoveryUpdateApplication(IamAction):
    def __init__(self):
        super().__init__('discovery', pattern='UpdateApplication')


class DmsAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='AddTagsToResource')


class DmsCreateEndpoint(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='CreateEndpoint')


class DmsCreateReplicationInstance(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='CreateReplicationInstance')


class DmsCreateReplicationSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='CreateReplicationSubnetGroup')


class DmsCreateReplicationTask(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='CreateReplicationTask')


class DmsDeleteEndpoint(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DeleteEndpoint')


class DmsDeleteEventSubscription(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DeleteEventSubscription')


class DmsDeleteReplicationInstance(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DeleteReplicationInstance')


class DmsDeleteReplicationSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DeleteReplicationSubnetGroup')


class DmsDeleteReplicationTask(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DeleteReplicationTask')


class DmsDescribeAccountAttributes(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeAccountAttributes')


class DmsDescribeCertificates(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeCertificates')


class DmsDescribeConnections(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeConnections')


class DmsDescribeEndpointTypes(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeEndpointTypes')


class DmsDescribeEndpoints(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeEndpoints')


class DmsDescribeEventCategories(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeEventCategories')


class DmsDescribeEventSubscriptions(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeEventSubscriptions')


class DmsDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeEvents')


class DmsDescribeOrderableReplicationInstances(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeOrderableReplicationInstances')


class DmsDescribeRefreshSchemasStatus(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeRefreshSchemasStatus')


class DmsDescribeReplicationInstances(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeReplicationInstances')


class DmsDescribeReplicationSubnetGroups(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeReplicationSubnetGroups')


class DmsDescribeReplicationTasks(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeReplicationTasks')


class DmsDescribeSchemas(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeSchemas')


class DmsDescribeTableStatistics(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='DescribeTableStatistics')


class DmsListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='ListTagsForResource')


class DmsModifyEndpoint(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='ModifyEndpoint')


class DmsModifyEventSubscription(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='ModifyEventSubscription')


class DmsModifyReplicationInstance(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='ModifyReplicationInstance')


class DmsModifyReplicationSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='ModifyReplicationSubnetGroup')


class DmsModifyReplicationTask(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='ModifyReplicationTask')


class DmsRefreshSchemas(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='RefreshSchemas')


class DmsRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='RemoveTagsFromResource')


class DmsStartReplicationTask(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='StartReplicationTask')


class DmsStopReplicationTask(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='StopReplicationTask')


class DmsTestConnection(IamAction):
    def __init__(self):
        super().__init__('dms', pattern='TestConnection')


class DsAddIpRoutes(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='AddIpRoutes')


class DsAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='AddTagsToResource')


class DsAuthorizeApplication(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='AuthorizeApplication')


class DsCancelSchemaExtension(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CancelSchemaExtension')


class DsConnectDirectory(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='ConnectDirectory')


class DsCreateAlias(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateAlias')


class DsCreateComputer(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateComputer')


class DsCreateConditionalForwarder(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateConditionalForwarder')


class DsCreateDirectory(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateDirectory')


class DsCreateMicrosoftAD(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateMicrosoftAD')


class DsCreateSnapshot(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateSnapshot')


class DsCreateTrust(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='CreateTrust')


class DsDeleteConditionalForwarder(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DeleteConditionalForwarder')


class DsDeleteDirectory(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DeleteDirectory')


class DsDeleteSnapshot(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DeleteSnapshot')


class DsDeleteTrust(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DeleteTrust')


class DsDeregisterEventTopic(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DeregisterEventTopic')


class DsDescribeConditionalForwarders(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DescribeConditionalForwarders')


class DsDescribeDirectories(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DescribeDirectories')


class DsDescribeEventTopics(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DescribeEventTopics')


class DsDescribeSnapshots(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DescribeSnapshots')


class DsDescribeTrusts(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DescribeTrusts')


class DsDisableRadius(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DisableRadius')


class DsDisableSso(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='DisableSso')


class DsEnableRadius(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='EnableRadius')


class DsEnableSso(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='EnableSso')


class DsGetDirectoryLimits(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='GetDirectoryLimits')


class DsGetSnapshotLimits(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='GetSnapshotLimits')


class DsListAuthorizedApplications(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='ListAuthorizedApplications')


class DsListIpRoutes(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='ListIpRoutes')


class DsListSchemaExtensions(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='ListSchemaExtensions')


class DsListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='ListTagsForResource')


class DsRegisterEventTopic(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='RegisterEventTopic')


class DsRemoveIpRoutes(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='RemoveIpRoutes')


class DsRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='RemoveTagsFromResource')


class DsRestoreFromSnapshot(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='RestoreFromSnapshot')


class DsStartSchemaExtension(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='StartSchemaExtension')


class DsUnauthorizeApplication(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='UnauthorizeApplication')


class DsUpdateConditionalForwarder(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='UpdateConditionalForwarder')


class DsUpdateRadius(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='UpdateRadius')


class DsVerifyTrust(IamAction):
    def __init__(self):
        super().__init__('ds', pattern='VerifyTrust')


class DynamodbBatchGetItem(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='BatchGetItem')


class DynamodbBatchWriteItem(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='BatchWriteItem')


class DynamodbCreateBackup(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='CreateBackup')


class DynamodbCreateTable(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='CreateTable')


class DynamodbDeleteBackup(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DeleteBackup')


class DynamodbDeleteItem(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DeleteItem')


class DynamodbDeleteTable(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DeleteTable')


class DynamodbDescribeBackup(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeBackup')


class DynamodbDescribeContinuousBackups(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeContinuousBackups')


class DynamodbDescribeLimits(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeLimits')


class DynamodbDescribeReservedCapacity(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeReservedCapacity')


class DynamodbDescribeReservedCapacityOfferings(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeReservedCapacityOfferings')


class DynamodbDescribeStream(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeStream')


class DynamodbDescribeTable(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeTable')


class DynamodbDescribeTimeToLive(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='DescribeTimeToLive')


class DynamodbGetItem(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='GetItem')


class DynamodbGetRecords(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='GetRecords')


class DynamodbGetShardIterator(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='GetShardIterator')


class DynamodbListBackups(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='ListBackups')


class DynamodbListStreams(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='ListStreams')


class DynamodbListTables(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='ListTables')


class DynamodbListTagsOfResource(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='ListTagsOfResource')


class DynamodbPurchaseReservedCapacityOfferings(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='PurchaseReservedCapacityOfferings')


class DynamodbPutItem(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='PutItem')


class DynamodbQuery(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='Query')


class DynamodbRestoreTableFromBackup(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='RestoreTableFromBackup')


class DynamodbRestoreTableToPointInTime(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='RestoreTableToPointInTime')


class DynamodbScan(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='Scan')


class DynamodbTagResource(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='TagResource')


class DynamodbUntagResource(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='UntagResource')


class DynamodbUpdateContinuousBackups(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='UpdateContinuousBackups')


class DynamodbUpdateItem(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='UpdateItem')


class DynamodbUpdateTable(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='UpdateTable')


class DynamodbUpdateTimeToLive(IamAction):
    def __init__(self):
        super().__init__('dynamodb', pattern='UpdateTimeToLive')


class Ec2AcceptReservedInstancesExchangeQuote(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AcceptReservedInstancesExchangeQuote')


class Ec2AcceptVpcEndpointConnections(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AcceptVpcEndpointConnections')


class Ec2AcceptVpcPeeringConnection(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AcceptVpcPeeringConnection')


class Ec2AllocateAddress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AllocateAddress')


class Ec2AllocateHosts(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AllocateHosts')


class Ec2AssignIpv6Addresses(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssignIpv6Addresses')


class Ec2AssignPrivateIpAddresses(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssignPrivateIpAddresses')


class Ec2AssociateAddress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssociateAddress')


class Ec2AssociateDhcpOptions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssociateDhcpOptions')


class Ec2AssociateIamInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssociateIamInstanceProfile')


class Ec2AssociateRouteTable(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssociateRouteTable')


class Ec2AssociateSubnetCidrBlock(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssociateSubnetCidrBlock')


class Ec2AssociateVpcCidrBlock(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AssociateVpcCidrBlock')


class Ec2AttachClassicLinkVpc(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AttachClassicLinkVpc')


class Ec2AttachInternetGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AttachInternetGateway')


class Ec2AttachNetworkInterface(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AttachNetworkInterface')


class Ec2AttachVolume(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AttachVolume')


class Ec2AttachVpnGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AttachVpnGateway')


class Ec2AuthorizeSecurityGroupEgress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AuthorizeSecurityGroupEgress')


class Ec2AuthorizeSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='AuthorizeSecurityGroupIngress')


class Ec2BundleInstance(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='BundleInstance')


class Ec2CancelBundleTask(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelBundleTask')


class Ec2CancelConversionTask(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelConversionTask')


class Ec2CancelExportTask(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelExportTask')


class Ec2CancelImportTask(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelImportTask')


class Ec2CancelReservedInstancesListing(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelReservedInstancesListing')


class Ec2CancelSpotFleetRequests(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelSpotFleetRequests')


class Ec2CancelSpotInstanceRequests(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CancelSpotInstanceRequests')


class Ec2ConfirmProductInstance(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ConfirmProductInstance')


class Ec2CopyFpgaImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CopyFpgaImage')


class Ec2CopyImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CopyImage')


class Ec2CopySnapshot(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CopySnapshot')


class Ec2CreateCustomerGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateCustomerGateway')


class Ec2CreateDefaultSubnet(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateDefaultSubnet')


class Ec2CreateDefaultVpc(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateDefaultVpc')


class Ec2CreateDhcpOptions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateDhcpOptions')


class Ec2CreateEgressOnlyInternetGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateEgressOnlyInternetGateway')


class Ec2CreateFlowLogs(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateFlowLogs')


class Ec2CreateFpgaImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateFpgaImage')


class Ec2CreateImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateImage')


class Ec2CreateInstanceExportTask(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateInstanceExportTask')


class Ec2CreateInternetGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateInternetGateway')


class Ec2CreateKeyPair(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateKeyPair')


class Ec2CreateLaunchTemplate(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateLaunchTemplate')


class Ec2CreateLaunchTemplateVersion(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateLaunchTemplateVersion')


class Ec2CreateNatGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateNatGateway')


class Ec2CreateNetworkAcl(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateNetworkAcl')


class Ec2CreateNetworkAclEntry(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateNetworkAclEntry')


class Ec2CreateNetworkInterface(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateNetworkInterface')


class Ec2CreateNetworkInterfacePermission(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateNetworkInterfacePermission')


class Ec2CreatePlacementGroup(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreatePlacementGroup')


class Ec2CreateReservedInstancesListing(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateReservedInstancesListing')


class Ec2CreateRoute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateRoute')


class Ec2CreateRouteTable(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateRouteTable')


class Ec2CreateSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateSecurityGroup')


class Ec2CreateSnapshot(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateSnapshot')


class Ec2CreateSpotDatafeedSubscription(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateSpotDatafeedSubscription')


class Ec2CreateSubnet(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateSubnet')


class Ec2CreateTags(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateTags')


class Ec2CreateVolume(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVolume')


class Ec2CreateVpc(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpc')


class Ec2CreateVpcEndpoint(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpcEndpoint')


class Ec2CreateVpcEndpointConnectionNotification(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpcEndpointConnectionNotification')


class Ec2CreateVpcEndpointServiceConfiguration(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpcEndpointServiceConfiguration')


class Ec2CreateVpcPeeringConnection(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpcPeeringConnection')


class Ec2CreateVpnConnection(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpnConnection')


class Ec2CreateVpnConnectionRoute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpnConnectionRoute')


class Ec2CreateVpnGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='CreateVpnGateway')


class Ec2DeleteCustomerGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteCustomerGateway')


class Ec2DeleteDhcpOptions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteDhcpOptions')


class Ec2DeleteEgressOnlyInternetGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteEgressOnlyInternetGateway')


class Ec2DeleteFlowLogs(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteFlowLogs')


class Ec2DeleteFpgaImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteFpgaImage')


class Ec2DeleteInternetGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteInternetGateway')


class Ec2DeleteKeyPair(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteKeyPair')


class Ec2DeleteLaunchTemplate(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteLaunchTemplate')


class Ec2DeleteLaunchTemplateVersions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteLaunchTemplateVersions')


class Ec2DeleteNatGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteNatGateway')


class Ec2DeleteNetworkAcl(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteNetworkAcl')


class Ec2DeleteNetworkAclEntry(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteNetworkAclEntry')


class Ec2DeleteNetworkInterface(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteNetworkInterface')


class Ec2DeleteNetworkInterfacePermission(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteNetworkInterfacePermission')


class Ec2DeletePlacementGroup(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeletePlacementGroup')


class Ec2DeleteRoute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteRoute')


class Ec2DeleteRouteTable(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteRouteTable')


class Ec2DeleteSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteSecurityGroup')


class Ec2DeleteSnapshot(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteSnapshot')


class Ec2DeleteSpotDatafeedSubscription(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteSpotDatafeedSubscription')


class Ec2DeleteSubnet(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteSubnet')


class Ec2DeleteTags(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteTags')


class Ec2DeleteVolume(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVolume')


class Ec2DeleteVpc(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpc')


class Ec2DeleteVpcEndpointConnectionNotifications(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpcEndpointConnectionNotifications')


class Ec2DeleteVpcEndpointServiceConfigurations(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpcEndpointServiceConfigurations')


class Ec2DeleteVpcEndpoints(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpcEndpoints')


class Ec2DeleteVpcPeeringConnection(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpcPeeringConnection')


class Ec2DeleteVpnConnection(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpnConnection')


class Ec2DeleteVpnConnectionRoute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpnConnectionRoute')


class Ec2DeleteVpnGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeleteVpnGateway')


class Ec2DeregisterImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DeregisterImage')


class Ec2DescribeAccountAttributes(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeAccountAttributes')


class Ec2DescribeAddresses(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeAddresses')


class Ec2DescribeAvailabilityZones(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeAvailabilityZones')


class Ec2DescribeBundleTasks(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeBundleTasks')


class Ec2DescribeClassicLinkInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeClassicLinkInstances')


class Ec2DescribeConversionTasks(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeConversionTasks')


class Ec2DescribeCustomerGateways(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeCustomerGateways')


class Ec2DescribeDhcpOptions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeDhcpOptions')


class Ec2DescribeEgressOnlyInternetGateways(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeEgressOnlyInternetGateways')


class Ec2DescribeElasticGpus(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeElasticGpus')


class Ec2DescribeExportTasks(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeExportTasks')


class Ec2DescribeFlowLogs(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeFlowLogs')


class Ec2DescribeFpgaImageAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeFpgaImageAttribute')


class Ec2DescribeFpgaImages(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeFpgaImages')


class Ec2DescribeHostReservationOfferings(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeHostReservationOfferings')


class Ec2DescribeHostReservations(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeHostReservations')


class Ec2DescribeHosts(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeHosts')


class Ec2DescribeIamInstanceProfileAssociations(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeIamInstanceProfileAssociations')


class Ec2DescribeIdFormat(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeIdFormat')


class Ec2DescribeIdentityIdFormat(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeIdentityIdFormat')


class Ec2DescribeImageAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeImageAttribute')


class Ec2DescribeImages(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeImages')


class Ec2DescribeImportImageTasks(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeImportImageTasks')


class Ec2DescribeImportSnapshotTasks(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeImportSnapshotTasks')


class Ec2DescribeInstanceAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeInstanceAttribute')


class Ec2DescribeInstanceCreditSpecifications(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeInstanceCreditSpecifications')


class Ec2DescribeInstanceStatus(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeInstanceStatus')


class Ec2DescribeInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeInstances')


class Ec2DescribeInternetGateways(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeInternetGateways')


class Ec2DescribeKeyPairs(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeKeyPairs')


class Ec2DescribeLaunchTemplateVersions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeLaunchTemplateVersions')


class Ec2DescribeLaunchTemplates(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeLaunchTemplates')


class Ec2DescribeMovingAddresses(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeMovingAddresses')


class Ec2DescribeNatGateways(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeNatGateways')


class Ec2DescribeNetworkAcls(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeNetworkAcls')


class Ec2DescribeNetworkInterfaceAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeNetworkInterfaceAttribute')


class Ec2DescribeNetworkInterfacePermissions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeNetworkInterfacePermissions')


class Ec2DescribeNetworkInterfaces(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeNetworkInterfaces')


class Ec2DescribePlacementGroups(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribePlacementGroups')


class Ec2DescribePrefixLists(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribePrefixLists')


class Ec2DescribeRegions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeRegions')


class Ec2DescribeReservedInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeReservedInstances')


class Ec2DescribeReservedInstancesListings(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeReservedInstancesListings')


class Ec2DescribeReservedInstancesModifications(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeReservedInstancesModifications')


class Ec2DescribeReservedInstancesOfferings(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeReservedInstancesOfferings')


class Ec2DescribeRouteTables(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeRouteTables')


class Ec2DescribeScheduledInstanceAvailability(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeScheduledInstanceAvailability')


class Ec2DescribeScheduledInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeScheduledInstances')


class Ec2DescribeSecurityGroupReferences(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSecurityGroupReferences')


class Ec2DescribeSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSecurityGroups')


class Ec2DescribeSnapshotAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSnapshotAttribute')


class Ec2DescribeSnapshots(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSnapshots')


class Ec2DescribeSpotDatafeedSubscription(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSpotDatafeedSubscription')


class Ec2DescribeSpotFleetInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSpotFleetInstances')


class Ec2DescribeSpotFleetRequestHistory(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSpotFleetRequestHistory')


class Ec2DescribeSpotFleetRequests(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSpotFleetRequests')


class Ec2DescribeSpotInstanceRequests(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSpotInstanceRequests')


class Ec2DescribeSpotPriceHistory(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSpotPriceHistory')


class Ec2DescribeStaleSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeStaleSecurityGroups')


class Ec2DescribeSubnets(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeSubnets')


class Ec2DescribeTags(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeTags')


class Ec2DescribeVolumeAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVolumeAttribute')


class Ec2DescribeVolumeStatus(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVolumeStatus')


class Ec2DescribeVolumes(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVolumes')


class Ec2DescribeVolumesModifications(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVolumesModifications')


class Ec2DescribeVpcAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcAttribute')


class Ec2DescribeVpcClassicLink(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcClassicLink')


class Ec2DescribeVpcClassicLinkDnsSupport(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcClassicLinkDnsSupport')


class Ec2DescribeVpcEndpointConnectionNotifications(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcEndpointConnectionNotifications')


class Ec2DescribeVpcEndpointConnections(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcEndpointConnections')


class Ec2DescribeVpcEndpointServiceConfigurations(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcEndpointServiceConfigurations')


class Ec2DescribeVpcEndpointServicePermissions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcEndpointServicePermissions')


class Ec2DescribeVpcEndpointServices(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcEndpointServices')


class Ec2DescribeVpcEndpoints(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcEndpoints')


class Ec2DescribeVpcPeeringConnections(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcPeeringConnections')


class Ec2DescribeVpcs(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpcs')


class Ec2DescribeVpnConnections(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpnConnections')


class Ec2DescribeVpnGateways(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DescribeVpnGateways')


class Ec2DetachClassicLinkVpc(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DetachClassicLinkVpc')


class Ec2DetachInternetGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DetachInternetGateway')


class Ec2DetachNetworkInterface(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DetachNetworkInterface')


class Ec2DetachVolume(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DetachVolume')


class Ec2DetachVpnGateway(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DetachVpnGateway')


class Ec2DisableVgwRoutePropagation(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisableVgwRoutePropagation')


class Ec2DisableVpcClassicLink(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisableVpcClassicLink')


class Ec2DisableVpcClassicLinkDnsSupport(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisableVpcClassicLinkDnsSupport')


class Ec2DisassociateAddress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisassociateAddress')


class Ec2DisassociateIamInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisassociateIamInstanceProfile')


class Ec2DisassociateRouteTable(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisassociateRouteTable')


class Ec2DisassociateSubnetCidrBlock(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisassociateSubnetCidrBlock')


class Ec2DisassociateVpcCidrBlock(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='DisassociateVpcCidrBlock')


class Ec2EnableVgwRoutePropagation(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='EnableVgwRoutePropagation')


class Ec2EnableVolumeIO(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='EnableVolumeIO')


class Ec2EnableVpcClassicLink(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='EnableVpcClassicLink')


class Ec2EnableVpcClassicLinkDnsSupport(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='EnableVpcClassicLinkDnsSupport')


class Ec2GetConsoleOutput(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='GetConsoleOutput')


class Ec2GetConsoleScreenshot(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='GetConsoleScreenshot')


class Ec2GetHostReservationPurchasePreview(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='GetHostReservationPurchasePreview')


class Ec2GetLaunchTemplateData(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='GetLaunchTemplateData')


class Ec2GetPasswordData(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='GetPasswordData')


class Ec2GetReservedInstancesExchangeQuote(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='GetReservedInstancesExchangeQuote')


class Ec2ImportImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ImportImage')


class Ec2ImportInstance(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ImportInstance')


class Ec2ImportKeyPair(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ImportKeyPair')


class Ec2ImportSnapshot(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ImportSnapshot')


class Ec2ImportVolume(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ImportVolume')


class Ec2ModifyFpgaImageAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyFpgaImageAttribute')


class Ec2ModifyHosts(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyHosts')


class Ec2ModifyIdFormat(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyIdFormat')


class Ec2ModifyIdentityIdFormat(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyIdentityIdFormat')


class Ec2ModifyImageAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyImageAttribute')


class Ec2ModifyInstanceAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyInstanceAttribute')


class Ec2ModifyInstanceCreditSpecification(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyInstanceCreditSpecification')


class Ec2ModifyInstancePlacement(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyInstancePlacement')


class Ec2ModifyLaunchTemplate(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyLaunchTemplate')


class Ec2ModifyNetworkInterfaceAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyNetworkInterfaceAttribute')


class Ec2ModifyReservedInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyReservedInstances')


class Ec2ModifySnapshotAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifySnapshotAttribute')


class Ec2ModifySpotFleetRequest(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifySpotFleetRequest')


class Ec2ModifySubnetAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifySubnetAttribute')


class Ec2ModifyVolume(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVolume')


class Ec2ModifyVolumeAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVolumeAttribute')


class Ec2ModifyVpcAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcAttribute')


class Ec2ModifyVpcEndpoint(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcEndpoint')


class Ec2ModifyVpcEndpointConnectionNotification(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcEndpointConnectionNotification')


class Ec2ModifyVpcEndpointServiceConfiguration(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcEndpointServiceConfiguration')


class Ec2ModifyVpcEndpointServicePermissions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcEndpointServicePermissions')


class Ec2ModifyVpcPeeringConnectionOptions(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcPeeringConnectionOptions')


class Ec2ModifyVpcTenancy(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ModifyVpcTenancy')


class Ec2MonitorInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='MonitorInstances')


class Ec2MoveAddressToVpc(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='MoveAddressToVpc')


class Ec2PurchaseHostReservation(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='PurchaseHostReservation')


class Ec2PurchaseReservedInstancesOffering(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='PurchaseReservedInstancesOffering')


class Ec2PurchaseScheduledInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='PurchaseScheduledInstances')


class Ec2RebootInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RebootInstances')


class Ec2RegisterImage(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RegisterImage')


class Ec2RejectVpcEndpointConnections(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RejectVpcEndpointConnections')


class Ec2RejectVpcPeeringConnection(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RejectVpcPeeringConnection')


class Ec2ReleaseAddress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReleaseAddress')


class Ec2ReleaseHosts(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReleaseHosts')


class Ec2ReplaceIamInstanceProfileAssociation(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReplaceIamInstanceProfileAssociation')


class Ec2ReplaceNetworkAclAssociation(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReplaceNetworkAclAssociation')


class Ec2ReplaceNetworkAclEntry(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReplaceNetworkAclEntry')


class Ec2ReplaceRoute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReplaceRoute')


class Ec2ReplaceRouteTableAssociation(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReplaceRouteTableAssociation')


class Ec2ReportInstanceStatus(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ReportInstanceStatus')


class Ec2RequestSpotFleet(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RequestSpotFleet')


class Ec2RequestSpotInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RequestSpotInstances')


class Ec2ResetFpgaImageAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ResetFpgaImageAttribute')


class Ec2ResetImageAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ResetImageAttribute')


class Ec2ResetInstanceAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ResetInstanceAttribute')


class Ec2ResetNetworkInterfaceAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ResetNetworkInterfaceAttribute')


class Ec2ResetSnapshotAttribute(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='ResetSnapshotAttribute')


class Ec2RestoreAddressToClassic(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RestoreAddressToClassic')


class Ec2RevokeSecurityGroupEgress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RevokeSecurityGroupEgress')


class Ec2RevokeSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RevokeSecurityGroupIngress')


class Ec2RunInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RunInstances')


class Ec2RunScheduledInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='RunScheduledInstances')


class Ec2StartInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='StartInstances')


class Ec2StopInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='StopInstances')


class Ec2TerminateInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='TerminateInstances')


class Ec2UnassignIpv6Addresses(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='UnassignIpv6Addresses')


class Ec2UnassignPrivateIpAddresses(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='UnassignPrivateIpAddresses')


class Ec2UnmonitorInstances(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='UnmonitorInstances')


class Ec2UpdateSecurityGroupRuleDescriptionsEgress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='UpdateSecurityGroupRuleDescriptionsEgress')


class Ec2UpdateSecurityGroupRuleDescriptionsIngress(IamAction):
    def __init__(self):
        super().__init__('ec2', pattern='UpdateSecurityGroupRuleDescriptionsIngress')


class Ec2MessagesAcknowledgeMessage(IamAction):
    def __init__(self):
        super().__init__('ec2messages', pattern='AcknowledgeMessage')


class Ec2MessagesDeleteMessage(IamAction):
    def __init__(self):
        super().__init__('ec2messages', pattern='DeleteMessage')


class Ec2MessagesFailMessage(IamAction):
    def __init__(self):
        super().__init__('ec2messages', pattern='FailMessage')


class Ec2MessagesGetEndpoint(IamAction):
    def __init__(self):
        super().__init__('ec2messages', pattern='GetEndpoint')


class Ec2MessagesGetMessages(IamAction):
    def __init__(self):
        super().__init__('ec2messages', pattern='GetMessages')


class Ec2MessagesSendReply(IamAction):
    def __init__(self):
        super().__init__('ec2messages', pattern='SendReply')


class EcrBatchCheckLayerAvailability(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='BatchCheckLayerAvailability')


class EcrBatchDeleteImage(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='BatchDeleteImage')


class EcrBatchGetImage(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='BatchGetImage')


class EcrCompleteLayerUpload(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='CompleteLayerUpload')


class EcrCreateRepository(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='CreateRepository')


class EcrDeleteRepository(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='DeleteRepository')


class EcrDeleteRepositoryPolicy(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='DeleteRepositoryPolicy')


class EcrDescribeImages(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='DescribeImages')


class EcrDescribeRepositories(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='DescribeRepositories')


class EcrGetAuthorizationToken(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='GetAuthorizationToken')


class EcrGetDownloadUrlForLayer(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='GetDownloadUrlForLayer')


class EcrGetRepositoryPolicy(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='GetRepositoryPolicy')


class EcrInitiateLayerUpload(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='InitiateLayerUpload')


class EcrListImages(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='ListImages')


class EcrPutImage(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='PutImage')


class EcrSetRepositoryPolicy(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='SetRepositoryPolicy')


class EcrUploadLayerPart(IamAction):
    def __init__(self):
        super().__init__('ecr', pattern='UploadLayerPart')


class EcsCreateCluster(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='CreateCluster')


class EcsCreateService(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='CreateService')


class EcsDeleteCluster(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DeleteCluster')


class EcsDeleteService(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DeleteService')


class EcsDeregisterContainerInstance(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DeregisterContainerInstance')


class EcsDeregisterTaskDefinition(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DeregisterTaskDefinition')


class EcsDescribeClusters(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DescribeClusters')


class EcsDescribeContainerInstances(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DescribeContainerInstances')


class EcsDescribeServices(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DescribeServices')


class EcsDescribeTaskDefinition(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DescribeTaskDefinition')


class EcsDescribeTasks(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DescribeTasks')


class EcsDiscoverPollEndpoint(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='DiscoverPollEndpoint')


class EcsListClusters(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='ListClusters')


class EcsListContainerInstances(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='ListContainerInstances')


class EcsListServices(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='ListServices')


class EcsListTaskDefinitionFamilies(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='ListTaskDefinitionFamilies')


class EcsListTaskDefinitions(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='ListTaskDefinitions')


class EcsListTasks(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='ListTasks')


class EcsPoll(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='Poll')


class EcsRegisterContainerInstance(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='RegisterContainerInstance')


class EcsRegisterTaskDefinition(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='RegisterTaskDefinition')


class EcsRunTask(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='RunTask')


class EcsStartTask(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='StartTask')


class EcsStartTelemetrySession(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='StartTelemetrySession')


class EcsStopTask(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='StopTask')


class EcsSubmitContainerStateChange(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='SubmitContainerStateChange')


class EcsSubmitTaskStateChange(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='SubmitTaskStateChange')


class EcsUpdateContainerAgent(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='UpdateContainerAgent')


class EcsUpdateContainerInstancesState(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='UpdateContainerInstancesState')


class EcsUpdateService(IamAction):
    def __init__(self):
        super().__init__('ecs', pattern='UpdateService')


class ElasticacheAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='AddTagsToResource')


class ElasticacheAuthorizeCacheSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='AuthorizeCacheSecurityGroupIngress')


class ElasticacheCopySnapshot(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CopySnapshot')


class ElasticacheCreateCacheCluster(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CreateCacheCluster')


class ElasticacheCreateCacheParameterGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CreateCacheParameterGroup')


class ElasticacheCreateCacheSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CreateCacheSecurityGroup')


class ElasticacheCreateCacheSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CreateCacheSubnetGroup')


class ElasticacheCreateReplicationGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CreateReplicationGroup')


class ElasticacheCreateSnapshot(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='CreateSnapshot')


class ElasticacheDeleteCacheCluster(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DeleteCacheCluster')


class ElasticacheDeleteCacheParameterGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DeleteCacheParameterGroup')


class ElasticacheDeleteCacheSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DeleteCacheSecurityGroup')


class ElasticacheDeleteCacheSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DeleteCacheSubnetGroup')


class ElasticacheDeleteReplicationGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DeleteReplicationGroup')


class ElasticacheDeleteSnapshot(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DeleteSnapshot')


class ElasticacheDescribeCacheClusters(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeCacheClusters')


class ElasticacheDescribeCacheEngineVersions(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeCacheEngineVersions')


class ElasticacheDescribeCacheParameterGroups(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeCacheParameterGroups')


class ElasticacheDescribeCacheParameters(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeCacheParameters')


class ElasticacheDescribeCacheSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeCacheSecurityGroups')


class ElasticacheDescribeCacheSubnetGroups(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeCacheSubnetGroups')


class ElasticacheDescribeEngineDefaultParameters(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeEngineDefaultParameters')


class ElasticacheDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeEvents')


class ElasticacheDescribeReplicationGroups(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeReplicationGroups')


class ElasticacheDescribeReservedCacheNodes(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeReservedCacheNodes')


class ElasticacheDescribeReservedCacheNodesOfferings(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeReservedCacheNodesOfferings')


class ElasticacheDescribeSnapshots(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='DescribeSnapshots')


class ElasticacheListAllowedNodeTypeModifications(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ListAllowedNodeTypeModifications')


class ElasticacheListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ListTagsForResource')


class ElasticacheModifyCacheCluster(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ModifyCacheCluster')


class ElasticacheModifyCacheParameterGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ModifyCacheParameterGroup')


class ElasticacheModifyCacheSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ModifyCacheSubnetGroup')


class ElasticacheModifyReplicationGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ModifyReplicationGroup')


class ElasticachePurchaseReservedCacheNodesOffering(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='PurchaseReservedCacheNodesOffering')


class ElasticacheRebootCacheCluster(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='RebootCacheCluster')


class ElasticacheRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='RemoveTagsFromResource')


class ElasticacheResetCacheParameterGroup(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='ResetCacheParameterGroup')


class ElasticacheRevokeCacheSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('elasticache', pattern='RevokeCacheSecurityGroupIngress')


class ElasticbeanstalkAbortEnvironmentUpdate(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='AbortEnvironmentUpdate')


class ElasticbeanstalkApplyEnvironmentManagedAction(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='ApplyEnvironmentManagedAction')


class ElasticbeanstalkCheckDNSAvailability(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CheckDNSAvailability')


class ElasticbeanstalkComposeEnvironments(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='ComposeEnvironments')


class ElasticbeanstalkCreateApplication(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CreateApplication')


class ElasticbeanstalkCreateApplicationVersion(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CreateApplicationVersion')


class ElasticbeanstalkCreateConfigurationTemplate(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CreateConfigurationTemplate')


class ElasticbeanstalkCreateEnvironment(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CreateEnvironment')


class ElasticbeanstalkCreatePlatformVersion(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CreatePlatformVersion')


class ElasticbeanstalkCreateStorageLocation(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='CreateStorageLocation')


class ElasticbeanstalkDeleteApplication(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DeleteApplication')


class ElasticbeanstalkDeleteApplicationVersion(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DeleteApplicationVersion')


class ElasticbeanstalkDeleteConfigurationTemplate(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DeleteConfigurationTemplate')


class ElasticbeanstalkDeleteEnvironmentConfiguration(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DeleteEnvironmentConfiguration')


class ElasticbeanstalkDeletePlatformVersion(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DeletePlatformVersion')


class ElasticbeanstalkDescribeApplicationVersions(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeApplicationVersions')


class ElasticbeanstalkDescribeApplications(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeApplications')


class ElasticbeanstalkDescribeConfigurationOptions(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeConfigurationOptions')


class ElasticbeanstalkDescribeConfigurationSettings(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeConfigurationSettings')


class ElasticbeanstalkDescribeEnvironmentHealth(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeEnvironmentHealth')


class ElasticbeanstalkDescribeEnvironmentManagedActionHistory(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeEnvironmentManagedActionHistory')


class ElasticbeanstalkDescribeEnvironmentManagedActions(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeEnvironmentManagedActions')


class ElasticbeanstalkDescribeEnvironmentResources(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeEnvironmentResources')


class ElasticbeanstalkDescribeEnvironments(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeEnvironments')


class ElasticbeanstalkDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeEvents')


class ElasticbeanstalkDescribeInstancesHealth(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribeInstancesHealth')


class ElasticbeanstalkDescribePlatformVersion(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='DescribePlatformVersion')


class ElasticbeanstalkListAvailableSolutionStacks(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='ListAvailableSolutionStacks')


class ElasticbeanstalkListPlatformVersions(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='ListPlatformVersions')


class ElasticbeanstalkRebuildEnvironment(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='RebuildEnvironment')


class ElasticbeanstalkRequestEnvironmentInfo(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='RequestEnvironmentInfo')


class ElasticbeanstalkRestartAppServer(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='RestartAppServer')


class ElasticbeanstalkRetrieveEnvironmentInfo(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='RetrieveEnvironmentInfo')


class ElasticbeanstalkSwapEnvironmentCNAMEs(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='SwapEnvironmentCNAMEs')


class ElasticbeanstalkTerminateEnvironment(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='TerminateEnvironment')


class ElasticbeanstalkUpdateApplication(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='UpdateApplication')


class ElasticbeanstalkUpdateApplicationResourceLifecycle(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='UpdateApplicationResourceLifecycle')


class ElasticbeanstalkUpdateApplicationVersion(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='UpdateApplicationVersion')


class ElasticbeanstalkUpdateConfigurationTemplate(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='UpdateConfigurationTemplate')


class ElasticbeanstalkUpdateEnvironment(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='UpdateEnvironment')


class ElasticbeanstalkValidateConfigurationSettings(IamAction):
    def __init__(self):
        super().__init__('elasticbeanstalk', pattern='ValidateConfigurationSettings')


class ElasticfilesystemCreateFileSystem(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='CreateFileSystem')


class ElasticfilesystemCreateMountTarget(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='CreateMountTarget')


class ElasticfilesystemCreateTags(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='CreateTags')


class ElasticfilesystemDeleteFileSystem(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DeleteFileSystem')


class ElasticfilesystemDeleteMountTarget(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DeleteMountTarget')


class ElasticfilesystemDeleteTags(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DeleteTags')


class ElasticfilesystemDescribeFileSystems(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DescribeFileSystems')


class ElasticfilesystemDescribeMountTargetSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DescribeMountTargetSecurityGroups')


class ElasticfilesystemDescribeMountTargets(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DescribeMountTargets')


class ElasticfilesystemDescribeTags(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='DescribeTags')


class ElasticfilesystemModifyMountTargetSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('elasticfilesystem', pattern='ModifyMountTargetSecurityGroups')


class ElasticloadbalancingAddTags(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='AddTags')


class ElasticloadbalancingApplySecurityGroupsToLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ApplySecurityGroupsToLoadBalancer')


class ElasticloadbalancingAttachLoadBalancerToSubnets(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='AttachLoadBalancerToSubnets')


class ElasticloadbalancingConfigureHealthCheck(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ConfigureHealthCheck')


class ElasticloadbalancingCreateAppCookieStickinessPolicy(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateAppCookieStickinessPolicy')


class ElasticloadbalancingCreateLBCookieStickinessPolicy(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateLBCookieStickinessPolicy')


class ElasticloadbalancingCreateListener(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateListener')


class ElasticloadbalancingCreateLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateLoadBalancer')


class ElasticloadbalancingCreateLoadBalancerListeners(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateLoadBalancerListeners')


class ElasticloadbalancingCreateLoadBalancerPolicy(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateLoadBalancerPolicy')


class ElasticloadbalancingCreateRule(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateRule')


class ElasticloadbalancingCreateTargetGroup(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='CreateTargetGroup')


class ElasticloadbalancingDeleteListener(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeleteListener')


class ElasticloadbalancingDeleteLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeleteLoadBalancer')


class ElasticloadbalancingDeleteLoadBalancerListeners(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeleteLoadBalancerListeners')


class ElasticloadbalancingDeleteLoadBalancerPolicy(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeleteLoadBalancerPolicy')


class ElasticloadbalancingDeleteRule(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeleteRule')


class ElasticloadbalancingDeleteTargetGroup(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeleteTargetGroup')


class ElasticloadbalancingDeregisterInstancesFromLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeregisterInstancesFromLoadBalancer')


class ElasticloadbalancingDeregisterTargets(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DeregisterTargets')


class ElasticloadbalancingDescribeInstanceHealth(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeInstanceHealth')


class ElasticloadbalancingDescribeListeners(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeListeners')


class ElasticloadbalancingDescribeLoadBalancerAttributes(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeLoadBalancerAttributes')


class ElasticloadbalancingDescribeLoadBalancerPolicies(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeLoadBalancerPolicies')


class ElasticloadbalancingDescribeLoadBalancerPolicyTypes(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeLoadBalancerPolicyTypes')


class ElasticloadbalancingDescribeLoadBalancers(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeLoadBalancers')


class ElasticloadbalancingDescribeRules(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeRules')


class ElasticloadbalancingDescribeSSLPolicies(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeSSLPolicies')


class ElasticloadbalancingDescribeTags(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeTags')


class ElasticloadbalancingDescribeTargetGroupAttributes(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeTargetGroupAttributes')


class ElasticloadbalancingDescribeTargetGroups(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeTargetGroups')


class ElasticloadbalancingDescribeTargetHealth(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DescribeTargetHealth')


class ElasticloadbalancingDetachLoadBalancerFromSubnets(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DetachLoadBalancerFromSubnets')


class ElasticloadbalancingDisableAvailabilityZonesForLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='DisableAvailabilityZonesForLoadBalancer')


class ElasticloadbalancingEnableAvailabilityZonesForLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='EnableAvailabilityZonesForLoadBalancer')


class ElasticloadbalancingModifyListener(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ModifyListener')


class ElasticloadbalancingModifyLoadBalancerAttributes(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ModifyLoadBalancerAttributes')


class ElasticloadbalancingModifyRule(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ModifyRule')


class ElasticloadbalancingModifyTargetGroup(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ModifyTargetGroup')


class ElasticloadbalancingModifyTargetGroupAttributes(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='ModifyTargetGroupAttributes')


class ElasticloadbalancingRegisterInstancesWithLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='RegisterInstancesWithLoadBalancer')


class ElasticloadbalancingRegisterTargets(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='RegisterTargets')


class ElasticloadbalancingRemoveTags(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='RemoveTags')


class ElasticloadbalancingSetIpAddressType(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetIpAddressType')


class ElasticloadbalancingSetLoadBalancerListenerSSLCertificate(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetLoadBalancerListenerSSLCertificate')


class ElasticloadbalancingSetLoadBalancerPoliciesForBackendServer(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetLoadBalancerPoliciesForBackendServer')


class ElasticloadbalancingSetLoadBalancerPoliciesOfListener(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetLoadBalancerPoliciesOfListener')


class ElasticloadbalancingSetRulePriorities(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetRulePriorities')


class ElasticloadbalancingSetSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetSecurityGroups')


class ElasticloadbalancingSetSubnets(IamAction):
    def __init__(self):
        super().__init__('elasticloadbalancing', pattern='SetSubnets')


class ElasticmapreduceAddInstanceGroups(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='AddInstanceGroups')


class ElasticmapreduceAddJobFlowSteps(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='AddJobFlowSteps')


class ElasticmapreduceAddTags(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='AddTags')


class ElasticmapreduceCancelSteps(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='CancelSteps')


class ElasticmapreduceCreateSecurityConfiguration(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='CreateSecurityConfiguration')


class ElasticmapreduceDeleteSecurityConfiguration(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='DeleteSecurityConfiguration')


class ElasticmapreduceDescribeCluster(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='DescribeCluster')


class ElasticmapreduceDescribeJobFlows(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='DescribeJobFlows')


class ElasticmapreduceDescribeSecurityConfiguration(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='DescribeSecurityConfiguration')


class ElasticmapreduceDescribeStep(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='DescribeStep')


class ElasticmapreduceListBootstrapActions(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ListBootstrapActions')


class ElasticmapreduceListClusters(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ListClusters')


class ElasticmapreduceListInstanceGroups(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ListInstanceGroups')


class ElasticmapreduceListInstances(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ListInstances')


class ElasticmapreduceListSecurityConfigurations(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ListSecurityConfigurations')


class ElasticmapreduceListSteps(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ListSteps')


class ElasticmapreduceModifyInstanceGroups(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ModifyInstanceGroups')


class ElasticmapreducePutAutoScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='PutAutoScalingPolicy')


class ElasticmapreduceRemoveAutoScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='RemoveAutoScalingPolicy')


class ElasticmapreduceRemoveTags(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='RemoveTags')


class ElasticmapreduceRunJobFlow(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='RunJobFlow')


class ElasticmapreduceSetTerminationProtection(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='SetTerminationProtection')


class ElasticmapreduceSetVisibleToAllUsers(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='SetVisibleToAllUsers')


class ElasticmapreduceTerminateJobFlows(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='TerminateJobFlows')


class ElasticmapreduceViewEventsFromAllClustersInConsole(IamAction):
    def __init__(self):
        super().__init__('elasticmapreduce', pattern='ViewEventsFromAllClustersInConsole')


class ElastictranscoderCancelJob(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='CancelJob')


class ElastictranscoderCreateJob(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='CreateJob')


class ElastictranscoderCreatePipeline(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='CreatePipeline')


class ElastictranscoderCreatePreset(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='CreatePreset')


class ElastictranscoderDeletePipeline(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='DeletePipeline')


class ElastictranscoderDeletePreset(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='DeletePreset')


class ElastictranscoderListJobsByPipeline(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ListJobsByPipeline')


class ElastictranscoderListJobsByStatus(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ListJobsByStatus')


class ElastictranscoderListPipelines(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ListPipelines')


class ElastictranscoderListPresets(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ListPresets')


class ElastictranscoderReadJob(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ReadJob')


class ElastictranscoderReadPipeline(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ReadPipeline')


class ElastictranscoderReadPreset(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='ReadPreset')


class ElastictranscoderTestRole(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='TestRole')


class ElastictranscoderUpdatePipeline(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='UpdatePipeline')


class ElastictranscoderUpdatePipelineNotifications(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='UpdatePipelineNotifications')


class ElastictranscoderUpdatePipelineStatus(IamAction):
    def __init__(self):
        super().__init__('elastictranscoder', pattern='UpdatePipelineStatus')


class EsAddTags(IamAction):
    def __init__(self):
        super().__init__('es', pattern='AddTags')


class EsCreateElasticsearchDomain(IamAction):
    def __init__(self):
        super().__init__('es', pattern='CreateElasticsearchDomain')


class EsDeleteElasticsearchDomain(IamAction):
    def __init__(self):
        super().__init__('es', pattern='DeleteElasticsearchDomain')


class EsDescribeElasticsearchDomain(IamAction):
    def __init__(self):
        super().__init__('es', pattern='DescribeElasticsearchDomain')


class EsDescribeElasticsearchDomainConfig(IamAction):
    def __init__(self):
        super().__init__('es', pattern='DescribeElasticsearchDomainConfig')


class EsDescribeElasticsearchDomains(IamAction):
    def __init__(self):
        super().__init__('es', pattern='DescribeElasticsearchDomains')


class EsESHttpDelete(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ESHttpDelete')


class EsESHttpGet(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ESHttpGet')


class EsESHttpHead(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ESHttpHead')


class EsESHttpPost(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ESHttpPost')


class EsESHttpPut(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ESHttpPut')


class EsListDomainNames(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ListDomainNames')


class EsListTags(IamAction):
    def __init__(self):
        super().__init__('es', pattern='ListTags')


class EsRemoveTags(IamAction):
    def __init__(self):
        super().__init__('es', pattern='RemoveTags')


class EsUpdateElasticsearchDomainConfig(IamAction):
    def __init__(self):
        super().__init__('es', pattern='UpdateElasticsearchDomainConfig')


class EventsDeleteRule(IamAction):
    def __init__(self):
        super().__init__('events', pattern='DeleteRule')


class EventsDescribeRule(IamAction):
    def __init__(self):
        super().__init__('events', pattern='DescribeRule')


class EventsDisableRule(IamAction):
    def __init__(self):
        super().__init__('events', pattern='DisableRule')


class EventsEnableRule(IamAction):
    def __init__(self):
        super().__init__('events', pattern='EnableRule')


class EventsListRuleNamesByTarget(IamAction):
    def __init__(self):
        super().__init__('events', pattern='ListRuleNamesByTarget')


class EventsListRules(IamAction):
    def __init__(self):
        super().__init__('events', pattern='ListRules')


class EventsListTargetsByRule(IamAction):
    def __init__(self):
        super().__init__('events', pattern='ListTargetsByRule')


class EventsPutEvents(IamAction):
    def __init__(self):
        super().__init__('events', pattern='PutEvents')


class EventsPutRule(IamAction):
    def __init__(self):
        super().__init__('events', pattern='PutRule')


class EventsPutTargets(IamAction):
    def __init__(self):
        super().__init__('events', pattern='PutTargets')


class EventsRemoveTargets(IamAction):
    def __init__(self):
        super().__init__('events', pattern='RemoveTargets')


class EventsTestEventPattern(IamAction):
    def __init__(self):
        super().__init__('events', pattern='TestEventPattern')


class ExecuteApiInvalidateCache(IamAction):
    def __init__(self):
        super().__init__('execute-api', pattern='InvalidateCache')


class ExecuteApiInvoke(IamAction):
    def __init__(self):
        super().__init__('execute-api', pattern='Invoke')


class FirehoseCreateDeliveryStream(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='CreateDeliveryStream')


class FirehoseDeleteDeliveryStream(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='DeleteDeliveryStream')


class FirehoseDescribeDeliveryStream(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='DescribeDeliveryStream')


class FirehoseListDeliveryStreams(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='ListDeliveryStreams')


class FirehosePutRecord(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='PutRecord')


class FirehosePutRecordBatch(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='PutRecordBatch')


class FirehoseUpdateDestination(IamAction):
    def __init__(self):
        super().__init__('firehose', pattern='UpdateDestination')


class FreertosCreateSoftwareConfiguration(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='CreateSoftwareConfiguration')


class FreertosDeleteSoftwareConfiguration(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='DeleteSoftwareConfiguration')


class FreertosDescribeHardwarePlatform(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='DescribeHardwarePlatform')


class FreertosDescribeSoftwareConfiguration(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='DescribeSoftwareConfiguration')


class FreertosGetSoftwareURL(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='GetSoftwareURL')


class FreertosGetSoftwareURLForConfiguration(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='GetSoftwareURLForConfiguration')


class FreertosListFreeRTOSVersions(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='ListFreeRTOSVersions')


class FreertosListHardwarePlatforms(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='ListHardwarePlatforms')


class FreertosListHardwareVendors(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='ListHardwareVendors')


class FreertosListSoftwareConfigurations(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='ListSoftwareConfigurations')


class FreertosUpdateSoftwareConfiguration(IamAction):
    def __init__(self):
        super().__init__('freertos', pattern='UpdateSoftwareConfiguration')


class GameliftCreateAlias(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='CreateAlias')


class GameliftCreateBuild(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='CreateBuild')


class GameliftCreateFleet(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='CreateFleet')


class GameliftCreateGameSession(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='CreateGameSession')


class GameliftCreatePlayerSession(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='CreatePlayerSession')


class GameliftCreatePlayerSessions(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='CreatePlayerSessions')


class GameliftDeleteAlias(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DeleteAlias')


class GameliftDeleteBuild(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DeleteBuild')


class GameliftDeleteFleet(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DeleteFleet')


class GameliftDeleteScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DeleteScalingPolicy')


class GameliftDescribeAlias(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeAlias')


class GameliftDescribeBuild(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeBuild')


class GameliftDescribeEC2InstanceLimits(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeEC2InstanceLimits')


class GameliftDescribeFleetAttributes(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeFleetAttributes')


class GameliftDescribeFleetCapacity(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeFleetCapacity')


class GameliftDescribeFleetEvents(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeFleetEvents')


class GameliftDescribeFleetPortSettings(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeFleetPortSettings')


class GameliftDescribeFleetUtilization(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeFleetUtilization')


class GameliftDescribeGameSessionDetails(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeGameSessionDetails')


class GameliftDescribeGameSessions(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeGameSessions')


class GameliftDescribeInstances(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeInstances')


class GameliftDescribePlayerSessions(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribePlayerSessions')


class GameliftDescribeRuntimeConfiguration(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeRuntimeConfiguration')


class GameliftDescribeScalingPolicies(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='DescribeScalingPolicies')


class GameliftGetGameSessionLogUrl(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='GetGameSessionLogUrl')


class GameliftGetInstanceAccess(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='GetInstanceAccess')


class GameliftListAliases(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='ListAliases')


class GameliftListBuilds(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='ListBuilds')


class GameliftListFleets(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='ListFleets')


class GameliftPutScalingPolicy(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='PutScalingPolicy')


class GameliftRequestUploadCredentials(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='RequestUploadCredentials')


class GameliftResolveAlias(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='ResolveAlias')


class GameliftSearchGameSessions(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='SearchGameSessions')


class GameliftUpdateAlias(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateAlias')


class GameliftUpdateBuild(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateBuild')


class GameliftUpdateFleetAttributes(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateFleetAttributes')


class GameliftUpdateFleetCapacity(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateFleetCapacity')


class GameliftUpdateFleetPortSettings(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateFleetPortSettings')


class GameliftUpdateGameSession(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateGameSession')


class GameliftUpdateRuntimeConfiguration(IamAction):
    def __init__(self):
        super().__init__('gamelift', pattern='UpdateRuntimeConfiguration')


class GlacierAbortMultipartUpload(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='AbortMultipartUpload')


class GlacierAbortVaultLock(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='AbortVaultLock')


class GlacierAddTagsToVault(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='AddTagsToVault')


class GlacierCompleteMultipartUpload(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='CompleteMultipartUpload')


class GlacierCompleteVaultLock(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='CompleteVaultLock')


class GlacierCreateVault(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='CreateVault')


class GlacierDeleteArchive(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='DeleteArchive')


class GlacierDeleteVault(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='DeleteVault')


class GlacierDeleteVaultAccessPolicy(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='DeleteVaultAccessPolicy')


class GlacierDeleteVaultNotifications(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='DeleteVaultNotifications')


class GlacierDescribeJob(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='DescribeJob')


class GlacierDescribeVault(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='DescribeVault')


class GlacierGetDataRetrievalPolicy(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='GetDataRetrievalPolicy')


class GlacierGetJobOutput(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='GetJobOutput')


class GlacierGetVaultAccessPolicy(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='GetVaultAccessPolicy')


class GlacierGetVaultLock(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='GetVaultLock')


class GlacierGetVaultNotifications(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='GetVaultNotifications')


class GlacierInitiateJob(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='InitiateJob')


class GlacierInitiateMultipartUpload(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='InitiateMultipartUpload')


class GlacierInitiateVaultLock(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='InitiateVaultLock')


class GlacierListJobs(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='ListJobs')


class GlacierListMultipartUploads(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='ListMultipartUploads')


class GlacierListParts(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='ListParts')


class GlacierListProvisionedCapacity(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='ListProvisionedCapacity')


class GlacierListTagsForVault(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='ListTagsForVault')


class GlacierListVaults(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='ListVaults')


class GlacierPurchaseProvisionedCapacity(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='PurchaseProvisionedCapacity')


class GlacierRemoveTagsFromVault(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='RemoveTagsFromVault')


class GlacierSetDataRetrievalPolicy(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='SetDataRetrievalPolicy')


class GlacierSetVaultAccessPolicy(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='SetVaultAccessPolicy')


class GlacierSetVaultNotifications(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='SetVaultNotifications')


class GlacierUploadArchive(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='UploadArchive')


class GlacierUploadMultipartPart(IamAction):
    def __init__(self):
        super().__init__('glacier', pattern='UploadMultipartPart')


class GlueBatchCreatePartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='BatchCreatePartition')


class GlueBatchDeleteConnection(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='BatchDeleteConnection')


class GlueBatchDeletePartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='BatchDeletePartition')


class GlueBatchDeleteTable(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='BatchDeleteTable')


class GlueBatchGetPartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='BatchGetPartition')


class GlueCreateClassifier(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateClassifier')


class GlueCreateConnection(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateConnection')


class GlueCreateCrawler(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateCrawler')


class GlueCreateDatabase(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateDatabase')


class GlueCreateDevEndpoint(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateDevEndpoint')


class GlueCreateJob(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateJob')


class GlueCreatePartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreatePartition')


class GlueCreateScript(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateScript')


class GlueCreateTable(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateTable')


class GlueCreateTrigger(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateTrigger')


class GlueCreateUserDefinedFunction(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='CreateUserDefinedFunction')


class GlueDeleteClassifier(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteClassifier')


class GlueDeleteConnection(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteConnection')


class GlueDeleteCrawler(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteCrawler')


class GlueDeleteDatabase(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteDatabase')


class GlueDeleteDevEndpoint(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteDevEndpoint')


class GlueDeleteJob(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteJob')


class GlueDeletePartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeletePartition')


class GlueDeleteTable(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteTable')


class GlueDeleteTrigger(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteTrigger')


class GlueDeleteUserDefinedFunction(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='DeleteUserDefinedFunction')


class GlueGetCatalogImportStatus(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetCatalogImportStatus')


class GlueGetClassifier(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetClassifier')


class GlueGetClassifiers(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetClassifiers')


class GlueGetConnection(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetConnection')


class GlueGetConnections(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetConnections')


class GlueGetCrawler(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetCrawler')


class GlueGetCrawlerMetrics(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetCrawlerMetrics')


class GlueGetCrawlers(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetCrawlers')


class GlueGetDatabase(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetDatabase')


class GlueGetDatabases(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetDatabases')


class GlueGetDataflowGraph(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetDataflowGraph')


class GlueGetDevEndpoint(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetDevEndpoint')


class GlueGetDevEndpoints(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetDevEndpoints')


class GlueGetJob(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetJob')


class GlueGetJobRun(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetJobRun')


class GlueGetJobRuns(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetJobRuns')


class GlueGetJobs(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetJobs')


class GlueGetMapping(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetMapping')


class GlueGetPartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetPartition')


class GlueGetPartitions(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetPartitions')


class GlueGetPlan(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetPlan')


class GlueGetTable(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetTable')


class GlueGetTableVersions(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetTableVersions')


class GlueGetTables(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetTables')


class GlueGetTrigger(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetTrigger')


class GlueGetTriggers(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetTriggers')


class GlueGetUserDefinedFunction(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetUserDefinedFunction')


class GlueGetUserDefinedFunctions(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='GetUserDefinedFunctions')


class GlueImportCatalogToGlue(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='ImportCatalogToGlue')


class GlueResetJobBookmark(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='ResetJobBookmark')


class GlueStartCrawler(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StartCrawler')


class GlueStartCrawlerSchedule(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StartCrawlerSchedule')


class GlueStartJobRun(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StartJobRun')


class GlueStartTrigger(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StartTrigger')


class GlueStopCrawler(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StopCrawler')


class GlueStopCrawlerSchedule(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StopCrawlerSchedule')


class GlueStopTrigger(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='StopTrigger')


class GlueUpdateClassifier(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateClassifier')


class GlueUpdateConnection(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateConnection')


class GlueUpdateCrawler(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateCrawler')


class GlueUpdateDatabase(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateDatabase')


class GlueUpdateDevEndpoint(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateDevEndpoint')


class GlueUpdateJob(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateJob')


class GlueUpdatePartition(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdatePartition')


class GlueUpdateTable(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateTable')


class GlueUpdateTrigger(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateTrigger')


class GlueUpdateUserDefinedFunction(IamAction):
    def __init__(self):
        super().__init__('glue', pattern='UpdateUserDefinedFunction')


class GreengrassAssociateRoleToGroup(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='AssociateRoleToGroup')


class GreengrassAssociateServiceRoleToAccount(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='AssociateServiceRoleToAccount')


class GreengrassCreateCoreDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateCoreDefinition')


class GreengrassCreateCoreDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateCoreDefinitionVersion')


class GreengrassCreateDeployment(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateDeployment')


class GreengrassCreateDeviceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateDeviceDefinition')


class GreengrassCreateDeviceDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateDeviceDefinitionVersion')


class GreengrassCreateFunctionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateFunctionDefinition')


class GreengrassCreateFunctionDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateFunctionDefinitionVersion')


class GreengrassCreateGroup(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateGroup')


class GreengrassCreateGroupCertificateAuthority(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateGroupCertificateAuthority')


class GreengrassCreateGroupVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateGroupVersion')


class GreengrassCreateLoggerDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateLoggerDefinition')


class GreengrassCreateLoggerDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateLoggerDefinitionVersion')


class GreengrassCreateResourceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateResourceDefinition')


class GreengrassCreateResourceDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateResourceDefinitionVersion')


class GreengrassCreateSoftwareUpdateJob(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateSoftwareUpdateJob')


class GreengrassCreateSubscriptionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateSubscriptionDefinition')


class GreengrassCreateSubscriptionDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='CreateSubscriptionDefinitionVersion')


class GreengrassDeleteCoreDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteCoreDefinition')


class GreengrassDeleteDeviceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteDeviceDefinition')


class GreengrassDeleteFunctionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteFunctionDefinition')


class GreengrassDeleteGroup(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteGroup')


class GreengrassDeleteLoggerDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteLoggerDefinition')


class GreengrassDeleteResourceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteResourceDefinition')


class GreengrassDeleteSubscriptionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DeleteSubscriptionDefinition')


class GreengrassDisassociateRoleFromGroup(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DisassociateRoleFromGroup')


class GreengrassDisassociateServiceRoleFromAccount(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='DisassociateServiceRoleFromAccount')


class GreengrassGetAssociatedRole(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetAssociatedRole')


class GreengrassGetConnectivityInfo(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetConnectivityInfo')


class GreengrassGetCoreDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetCoreDefinition')


class GreengrassGetCoreDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetCoreDefinitionVersion')


class GreengrassGetDeploymentStatus(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetDeploymentStatus')


class GreengrassGetDeviceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetDeviceDefinition')


class GreengrassGetDeviceDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetDeviceDefinitionVersion')


class GreengrassGetFunctionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetFunctionDefinition')


class GreengrassGetFunctionDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetFunctionDefinitionVersion')


class GreengrassGetGroup(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetGroup')


class GreengrassGetGroupCertificateAuthority(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetGroupCertificateAuthority')


class GreengrassGetGroupCertificateConfiguration(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetGroupCertificateConfiguration')


class GreengrassGetGroupVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetGroupVersion')


class GreengrassGetLoggerDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetLoggerDefinition')


class GreengrassGetLoggerDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetLoggerDefinitionVersion')


class GreengrassGetResourceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetResourceDefinition')


class GreengrassGetResourceDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetResourceDefinitionVersion')


class GreengrassGetServiceRoleForAccount(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetServiceRoleForAccount')


class GreengrassGetSubscriptionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetSubscriptionDefinition')


class GreengrassGetSubscriptionDefinitionVersion(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='GetSubscriptionDefinitionVersion')


class GreengrassListCoreDefinitionVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListCoreDefinitionVersions')


class GreengrassListCoreDefinitions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListCoreDefinitions')


class GreengrassListDeployments(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListDeployments')


class GreengrassListDeviceDefinitionVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListDeviceDefinitionVersions')


class GreengrassListDeviceDefinitions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListDeviceDefinitions')


class GreengrassListFunctionDefinitionVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListFunctionDefinitionVersions')


class GreengrassListFunctionDefinitions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListFunctionDefinitions')


class GreengrassListGroupCertificateAuthorities(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListGroupCertificateAuthorities')


class GreengrassListGroupVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListGroupVersions')


class GreengrassListGroups(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListGroups')


class GreengrassListLoggerDefinitionVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListLoggerDefinitionVersions')


class GreengrassListLoggerDefinitions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListLoggerDefinitions')


class GreengrassListResourceDefinitionVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListResourceDefinitionVersions')


class GreengrassListResourceDefinitions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListResourceDefinitions')


class GreengrassListSubscriptionDefinitionVersions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListSubscriptionDefinitionVersions')


class GreengrassListSubscriptionDefinitions(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ListSubscriptionDefinitions')


class GreengrassResetDeployments(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='ResetDeployments')


class GreengrassUpdateConnectivityInfo(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateConnectivityInfo')


class GreengrassUpdateCoreDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateCoreDefinition')


class GreengrassUpdateDeviceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateDeviceDefinition')


class GreengrassUpdateFunctionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateFunctionDefinition')


class GreengrassUpdateGroup(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateGroup')


class GreengrassUpdateGroupCertificateConfiguration(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateGroupCertificateConfiguration')


class GreengrassUpdateLoggerDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateLoggerDefinition')


class GreengrassUpdateResourceDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateResourceDefinition')


class GreengrassUpdateSubscriptionDefinition(IamAction):
    def __init__(self):
        super().__init__('greengrass', pattern='UpdateSubscriptionDefinition')


class GuarddutyAcceptInvitation(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='AcceptInvitation')


class GuarddutyArchiveFindings(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ArchiveFindings')


class GuarddutyCreateDetector(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='CreateDetector')


class GuarddutyCreateIPSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='CreateIPSet')


class GuarddutyCreateMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='CreateMembers')


class GuarddutyCreateSampleFindings(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='CreateSampleFindings')


class GuarddutyCreateThreatIntelSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='CreateThreatIntelSet')


class GuarddutyDeclineInvitations(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DeclineInvitations')


class GuarddutyDeleteDetector(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DeleteDetector')


class GuarddutyDeleteIPSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DeleteIPSet')


class GuarddutyDeleteInvitations(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DeleteInvitations')


class GuarddutyDeleteMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DeleteMembers')


class GuarddutyDeleteThreatIntelSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DeleteThreatIntelSet')


class GuarddutyDisassociateFromMasterAccount(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DisassociateFromMasterAccount')


class GuarddutyDisassociateMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='DisassociateMembers')


class GuarddutyGetDetector(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetDetector')


class GuarddutyGetFindings(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetFindings')


class GuarddutyGetFindingsStatistics(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetFindingsStatistics')


class GuarddutyGetIPSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetIPSet')


class GuarddutyGetInvitationsCount(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetInvitationsCount')


class GuarddutyGetMasterAccount(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetMasterAccount')


class GuarddutyGetMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetMembers')


class GuarddutyGetThreatIntelSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='GetThreatIntelSet')


class GuarddutyInviteMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='InviteMembers')


class GuarddutyListDetectors(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ListDetectors')


class GuarddutyListFindings(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ListFindings')


class GuarddutyListIPSets(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ListIPSets')


class GuarddutyListInvitations(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ListInvitations')


class GuarddutyListMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ListMembers')


class GuarddutyListThreatIntelSets(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='ListThreatIntelSets')


class GuarddutyStartMonitoringMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='StartMonitoringMembers')


class GuarddutyStopMonitoringMembers(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='StopMonitoringMembers')


class GuarddutyUnarchiveFindings(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='UnarchiveFindings')


class GuarddutyUpdateDetector(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='UpdateDetector')


class GuarddutyUpdateFindingsFeedback(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='UpdateFindingsFeedback')


class GuarddutyUpdateIPSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='UpdateIPSet')


class GuarddutyUpdateThreatIntelSet(IamAction):
    def __init__(self):
        super().__init__('guardduty', pattern='UpdateThreatIntelSet')


class HealthDescribeAffectedEntities(IamAction):
    def __init__(self):
        super().__init__('health', pattern='DescribeAffectedEntities')


class HealthDescribeEntityAggregates(IamAction):
    def __init__(self):
        super().__init__('health', pattern='DescribeEntityAggregates')


class HealthDescribeEventAggregates(IamAction):
    def __init__(self):
        super().__init__('health', pattern='DescribeEventAggregates')


class HealthDescribeEventDetails(IamAction):
    def __init__(self):
        super().__init__('health', pattern='DescribeEventDetails')


class HealthDescribeEventTypes(IamAction):
    def __init__(self):
        super().__init__('health', pattern='DescribeEventTypes')


class HealthDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('health', pattern='DescribeEvents')


class IamAddClientIDToOpenIDConnectProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='AddClientIDToOpenIDConnectProvider')


class IamAddRoleToInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='AddRoleToInstanceProfile')


class IamAddUserToGroup(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='AddUserToGroup')


class IamAttachGroupPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='AttachGroupPolicy')


class IamAttachRolePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='AttachRolePolicy')


class IamAttachUserPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='AttachUserPolicy')


class IamChangePassword(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ChangePassword')


class IamCreateAccessKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateAccessKey')


class IamCreateAccountAlias(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateAccountAlias')


class IamCreateGroup(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateGroup')


class IamCreateInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateInstanceProfile')


class IamCreateLoginProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateLoginProfile')


class IamCreateOpenIDConnectProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateOpenIDConnectProvider')


class IamCreatePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreatePolicy')


class IamCreatePolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreatePolicyVersion')


class IamCreateRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateRole')


class IamCreateSAMLProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateSAMLProvider')


class IamCreateServiceLinkedRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateServiceLinkedRole')


class IamCreateServiceSpecificCredential(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateServiceSpecificCredential')


class IamCreateUser(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateUser')


class IamCreateVirtualMFADevice(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='CreateVirtualMFADevice')


class IamDeactivateMFADevice(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeactivateMFADevice')


class IamDeleteAccessKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteAccessKey')


class IamDeleteAccountAlias(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteAccountAlias')


class IamDeleteAccountPasswordPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteAccountPasswordPolicy')


class IamDeleteGroup(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteGroup')


class IamDeleteGroupPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteGroupPolicy')


class IamDeleteInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteInstanceProfile')


class IamDeleteLoginProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteLoginProfile')


class IamDeleteOpenIDConnectProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteOpenIDConnectProvider')


class IamDeletePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeletePolicy')


class IamDeletePolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeletePolicyVersion')


class IamDeleteRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteRole')


class IamDeleteRolePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteRolePolicy')


class IamDeleteSAMLProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteSAMLProvider')


class IamDeleteSSHPublicKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteSSHPublicKey')


class IamDeleteServerCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteServerCertificate')


class IamDeleteServiceLinkedRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteServiceLinkedRole')


class IamDeleteServiceSpecificCredential(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteServiceSpecificCredential')


class IamDeleteSigningCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteSigningCertificate')


class IamDeleteUser(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteUser')


class IamDeleteUserPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteUserPolicy')


class IamDeleteVirtualMFADevice(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DeleteVirtualMFADevice')


class IamDetachGroupPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DetachGroupPolicy')


class IamDetachRolePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DetachRolePolicy')


class IamDetachUserPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='DetachUserPolicy')


class IamEnableMFADevice(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='EnableMFADevice')


class IamGenerateCredentialReport(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GenerateCredentialReport')


class IamGenerateServiceLastAccessedDetails(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GenerateServiceLastAccessedDetails')


class IamGetAccessKeyLastUsed(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetAccessKeyLastUsed')


class IamGetAccountAuthorizationDetails(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetAccountAuthorizationDetails')


class IamGetAccountPasswordPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetAccountPasswordPolicy')


class IamGetAccountSummary(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetAccountSummary')


class IamGetContextKeysForCustomPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetContextKeysForCustomPolicy')


class IamGetContextKeysForPrincipalPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetContextKeysForPrincipalPolicy')


class IamGetCredentialReport(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetCredentialReport')


class IamGetGroup(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetGroup')


class IamGetGroupPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetGroupPolicy')


class IamGetInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetInstanceProfile')


class IamGetLoginProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetLoginProfile')


class IamGetOpenIDConnectProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetOpenIDConnectProvider')


class IamGetPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetPolicy')


class IamGetPolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetPolicyVersion')


class IamGetRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetRole')


class IamGetRolePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetRolePolicy')


class IamGetSAMLProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetSAMLProvider')


class IamGetSSHPublicKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetSSHPublicKey')


class IamGetServerCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetServerCertificate')


class IamGetServiceLastAccessedDetails(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetServiceLastAccessedDetails')


class IamGetServiceLastAccessedDetailsWithEntities(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetServiceLastAccessedDetailsWithEntities')


class IamGetServiceLinkedRoleDeletionStatus(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetServiceLinkedRoleDeletionStatus')


class IamGetUser(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetUser')


class IamGetUserPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='GetUserPolicy')


class IamListAccessKeys(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListAccessKeys')


class IamListAccountAliases(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListAccountAliases')


class IamListAttachedGroupPolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListAttachedGroupPolicies')


class IamListAttachedRolePolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListAttachedRolePolicies')


class IamListAttachedUserPolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListAttachedUserPolicies')


class IamListEntitiesForPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListEntitiesForPolicy')


class IamListGroupPolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListGroupPolicies')


class IamListGroups(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListGroups')


class IamListGroupsForUser(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListGroupsForUser')


class IamListInstanceProfiles(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListInstanceProfiles')


class IamListInstanceProfilesForRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListInstanceProfilesForRole')


class IamListMFADevices(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListMFADevices')


class IamListOpenIDConnectProviders(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListOpenIDConnectProviders')


class IamListPolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListPolicies')


class IamListPoliciesGrantingServiceAccess(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListPoliciesGrantingServiceAccess')


class IamListPolicyVersions(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListPolicyVersions')


class IamListRolePolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListRolePolicies')


class IamListRoles(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListRoles')


class IamListSAMLProviders(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListSAMLProviders')


class IamListSSHPublicKeys(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListSSHPublicKeys')


class IamListServerCertificates(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListServerCertificates')


class IamListServiceSpecificCredentials(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListServiceSpecificCredentials')


class IamListSigningCertificates(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListSigningCertificates')


class IamListUserPolicies(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListUserPolicies')


class IamListUsers(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListUsers')


class IamListVirtualMFADevices(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ListVirtualMFADevices')


class IamPassRole(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='PassRole')


class IamPutGroupPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='PutGroupPolicy')


class IamPutRolePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='PutRolePolicy')


class IamPutUserPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='PutUserPolicy')


class IamRemoveClientIDFromOpenIDConnectProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='RemoveClientIDFromOpenIDConnectProvider')


class IamRemoveRoleFromInstanceProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='RemoveRoleFromInstanceProfile')


class IamRemoveUserFromGroup(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='RemoveUserFromGroup')


class IamResetServiceSpecificCredential(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ResetServiceSpecificCredential')


class IamResyncMFADevice(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='ResyncMFADevice')


class IamSetDefaultPolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='SetDefaultPolicyVersion')


class IamSimulateCustomPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='SimulateCustomPolicy')


class IamSimulatePrincipalPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='SimulatePrincipalPolicy')


class IamUpdateAccessKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateAccessKey')


class IamUpdateAccountPasswordPolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateAccountPasswordPolicy')


class IamUpdateAssumeRolePolicy(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateAssumeRolePolicy')


class IamUpdateGroup(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateGroup')


class IamUpdateLoginProfile(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateLoginProfile')


class IamUpdateOpenIDConnectProviderThumbprint(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateOpenIDConnectProviderThumbprint')


class IamUpdateRoleDescription(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateRoleDescription')


class IamUpdateSAMLProvider(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateSAMLProvider')


class IamUpdateSSHPublicKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateSSHPublicKey')


class IamUpdateServerCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateServerCertificate')


class IamUpdateServiceSpecificCredential(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateServiceSpecificCredential')


class IamUpdateSigningCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateSigningCertificate')


class IamUpdateUser(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UpdateUser')


class IamUploadSSHPublicKey(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UploadSSHPublicKey')


class IamUploadServerCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UploadServerCertificate')


class IamUploadSigningCertificate(IamAction):
    def __init__(self):
        super().__init__('iam', pattern='UploadSigningCertificate')


class ImportexportCancelJob(IamAction):
    def __init__(self):
        super().__init__('importexport', pattern='CancelJob')


class ImportexportCreateJob(IamAction):
    def __init__(self):
        super().__init__('importexport', pattern='CreateJob')


class ImportexportGetShippingLabel(IamAction):
    def __init__(self):
        super().__init__('importexport', pattern='GetShippingLabel')


class ImportexportGetStatus(IamAction):
    def __init__(self):
        super().__init__('importexport', pattern='GetStatus')


class ImportexportListJobs(IamAction):
    def __init__(self):
        super().__init__('importexport', pattern='ListJobs')


class ImportexportUpdateJob(IamAction):
    def __init__(self):
        super().__init__('importexport', pattern='UpdateJob')


class InspectorAddAttributesToFindings(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='AddAttributesToFindings')


class InspectorCreateAssessmentTarget(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='CreateAssessmentTarget')


class InspectorCreateAssessmentTemplate(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='CreateAssessmentTemplate')


class InspectorCreateResourceGroup(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='CreateResourceGroup')


class InspectorDeleteAssessmentRun(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DeleteAssessmentRun')


class InspectorDeleteAssessmentTarget(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DeleteAssessmentTarget')


class InspectorDeleteAssessmentTemplate(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DeleteAssessmentTemplate')


class InspectorDescribeAssessmentRuns(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeAssessmentRuns')


class InspectorDescribeAssessmentTargets(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeAssessmentTargets')


class InspectorDescribeAssessmentTemplates(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeAssessmentTemplates')


class InspectorDescribeCrossAccountAccessRole(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeCrossAccountAccessRole')


class InspectorDescribeFindings(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeFindings')


class InspectorDescribeResourceGroups(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeResourceGroups')


class InspectorDescribeRulesPackages(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='DescribeRulesPackages')


class InspectorGetTelemetryMetadata(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='GetTelemetryMetadata')


class InspectorListAssessmentRunAgents(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListAssessmentRunAgents')


class InspectorListAssessmentRuns(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListAssessmentRuns')


class InspectorListAssessmentTargets(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListAssessmentTargets')


class InspectorListAssessmentTemplates(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListAssessmentTemplates')


class InspectorListEventSubscriptions(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListEventSubscriptions')


class InspectorListFindings(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListFindings')


class InspectorListRulesPackages(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListRulesPackages')


class InspectorListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='ListTagsForResource')


class InspectorPreviewAgents(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='PreviewAgents')


class InspectorRegisterCrossAccountAccessRole(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='RegisterCrossAccountAccessRole')


class InspectorRemoveAttributesFromFindings(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='RemoveAttributesFromFindings')


class InspectorSetTagsForResource(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='SetTagsForResource')


class InspectorStartAssessmentRun(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='StartAssessmentRun')


class InspectorStopAssessmentRun(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='StopAssessmentRun')


class InspectorSubscribeToEvent(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='SubscribeToEvent')


class InspectorUnsubscribeFromEvent(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='UnsubscribeFromEvent')


class InspectorUpdateAssessmentTarget(IamAction):
    def __init__(self):
        super().__init__('inspector', pattern='UpdateAssessmentTarget')


class IotAcceptCertificateTransfer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='AcceptCertificateTransfer')


class IotAssociateTargetsWithJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='AssociateTargetsWithJob')


class IotAttachPolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='AttachPolicy')


class IotAttachPrincipalPolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='AttachPrincipalPolicy')


class IotAttachThingPrincipal(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='AttachThingPrincipal')


class IotCancelCertificateTransfer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CancelCertificateTransfer')


class IotCancelJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CancelJob')


class IotClearDefaultAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ClearDefaultAuthorizer')


class IotConnect(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='Connect')


class IotCreateAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateAuthorizer')


class IotCreateCertificateFromCsr(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateCertificateFromCsr')


class IotCreateJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateJob')


class IotCreateKeysAndCertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateKeysAndCertificate')


class IotCreateOTAUpdateJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateOTAUpdateJob')


class IotCreatePolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreatePolicy')


class IotCreatePolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreatePolicyVersion')


class IotCreateRoleAlias(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateRoleAlias')


class IotCreateStream(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateStream')


class IotCreateThing(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateThing')


class IotCreateThingType(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateThingType')


class IotCreateTopicRule(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='CreateTopicRule')


class IotDeleteAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteAuthorizer')


class IotDeleteCACertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteCACertificate')


class IotDeleteCertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteCertificate')


class IotDeleteOTAUpdateJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteOTAUpdateJob')


class IotDeletePolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeletePolicy')


class IotDeletePolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeletePolicyVersion')


class IotDeleteRegistrationCode(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteRegistrationCode')


class IotDeleteRoleAlias(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteRoleAlias')


class IotDeleteStream(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteStream')


class IotDeleteThing(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteThing')


class IotDeleteThingShadow(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteThingShadow')


class IotDeleteThingType(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteThingType')


class IotDeleteTopicRule(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeleteTopicRule')


class IotDeprecateThingType(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DeprecateThingType')


class IotDescribeAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeAuthorizer')


class IotDescribeCACertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeCACertificate')


class IotDescribeCertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeCertificate')


class IotDescribeDefaultAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeDefaultAuthorizer')


class IotDescribeEndpoint(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeEndpoint')


class IotDescribeIndex(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeIndex')


class IotDescribeJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeJob')


class IotDescribeJobExecution(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeJobExecution')


class IotDescribeRoleAlias(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeRoleAlias')


class IotDescribeStream(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeStream')


class IotDescribeThing(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeThing')


class IotDescribeThingType(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DescribeThingType')


class IotDetachPolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DetachPolicy')


class IotDetachPrincipalPolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DetachPrincipalPolicy')


class IotDetachThingPrincipal(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DetachThingPrincipal')


class IotDisableTopicRule(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='DisableTopicRule')


class IotEnableTopicRule(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='EnableTopicRule')


class IotGetEffectivePolicies(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetEffectivePolicies')


class IotGetIndexingConfiguration(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetIndexingConfiguration')


class IotGetJobDocument(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetJobDocument')


class IotGetLoggingOptions(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetLoggingOptions')


class IotGetOTAUpdateJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetOTAUpdateJob')


class IotGetPolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetPolicy')


class IotGetPolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetPolicyVersion')


class IotGetRegistrationCode(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetRegistrationCode')


class IotGetThingShadow(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetThingShadow')


class IotGetTopicRule(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='GetTopicRule')


class IotListAttachedPolicies(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListAttachedPolicies')


class IotListAuthorizers(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListAuthorizers')


class IotListCACertificates(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListCACertificates')


class IotListCertificates(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListCertificates')


class IotListCertificatesByCA(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListCertificatesByCA')


class IotListIndices(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListIndices')


class IotListJobExecutionsForJob(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListJobExecutionsForJob')


class IotListJobExecutionsForThing(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListJobExecutionsForThing')


class IotListJobs(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListJobs')


class IotListOTAUpdateJobs(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListOTAUpdateJobs')


class IotListOutgoingCertificates(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListOutgoingCertificates')


class IotListPolicies(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListPolicies')


class IotListPolicyPrincipals(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListPolicyPrincipals')


class IotListPolicyVersions(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListPolicyVersions')


class IotListPrincipalPolicies(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListPrincipalPolicies')


class IotListPrincipalThings(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListPrincipalThings')


class IotListRoleAliases(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListRoleAliases')


class IotListStreams(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListStreams')


class IotListTargetsForPolicy(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListTargetsForPolicy')


class IotListThingPrincipals(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListThingPrincipals')


class IotListThingTypes(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListThingTypes')


class IotListThings(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListThings')


class IotListTopicRules(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ListTopicRules')


class IotPublish(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='Publish')


class IotReceive(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='Receive')


class IotRegisterCACertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='RegisterCACertificate')


class IotRegisterCertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='RegisterCertificate')


class IotRejectCertificateTransfer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='RejectCertificateTransfer')


class IotReplaceTopicRule(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='ReplaceTopicRule')


class IotSearchIndex(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='SearchIndex')


class IotSetDefaultAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='SetDefaultAuthorizer')


class IotSetDefaultPolicyVersion(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='SetDefaultPolicyVersion')


class IotSetLoggingOptions(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='SetLoggingOptions')


class IotSubscribe(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='Subscribe')


class IotTestAuthorization(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='TestAuthorization')


class IotTestInvokeAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='TestInvokeAuthorizer')


class IotTransferCertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='TransferCertificate')


class IotUpdateAuthorizer(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateAuthorizer')


class IotUpdateCACertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateCACertificate')


class IotUpdateCertificate(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateCertificate')


class IotUpdateIndexingConfiguration(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateIndexingConfiguration')


class IotUpdateRoleAlias(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateRoleAlias')


class IotUpdateStream(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateStream')


class IotUpdateThing(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateThing')


class IotUpdateThingShadow(IamAction):
    def __init__(self):
        super().__init__('iot', pattern='UpdateThingShadow')


class IotanalyticsCreateChannel(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='CreateChannel')


class IotanalyticsCreateDataset(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='CreateDataset')


class IotanalyticsCreateDatasetContent(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='CreateDatasetContent')


class IotanalyticsCreateDatastore(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='CreateDatastore')


class IotanalyticsCreatePipeline(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='CreatePipeline')


class IotanalyticsDeleteChannel(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DeleteChannel')


class IotanalyticsDeleteDataset(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DeleteDataset')


class IotanalyticsDeleteDatasetContent(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DeleteDatasetContent')


class IotanalyticsDeleteDatastore(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DeleteDatastore')


class IotanalyticsDeletePipeline(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DeletePipeline')


class IotanalyticsDescribeChannel(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DescribeChannel')


class IotanalyticsDescribeDataset(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DescribeDataset')


class IotanalyticsDescribeDatastore(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DescribeDatastore')


class IotanalyticsDescribePipeline(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='DescribePipeline')


class IotanalyticsGetDatasetContent(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='GetDatasetContent')


class IotanalyticsListChannels(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='ListChannels')


class IotanalyticsListDatasets(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='ListDatasets')


class IotanalyticsListDatastores(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='ListDatastores')


class IotanalyticsListPipelines(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='ListPipelines')


class IotanalyticsUpdateDataset(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='UpdateDataset')


class IotanalyticsUpdatePipeline(IamAction):
    def __init__(self):
        super().__init__('iotanalytics', pattern='UpdatePipeline')


class KinesisAddTagsToStream(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='AddTagsToStream')


class KinesisCreateStream(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='CreateStream')


class KinesisDecreaseStreamRetentionPeriod(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='DecreaseStreamRetentionPeriod')


class KinesisDeleteStream(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='DeleteStream')


class KinesisDescribeLimits(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='DescribeLimits')


class KinesisDescribeStream(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='DescribeStream')


class KinesisDisableEnhancedMonitoring(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='DisableEnhancedMonitoring')


class KinesisEnableEnhancedMonitoring(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='EnableEnhancedMonitoring')


class KinesisGetRecords(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='GetRecords')


class KinesisGetShardIterator(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='GetShardIterator')


class KinesisIncreaseStreamRetentionPeriod(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='IncreaseStreamRetentionPeriod')


class KinesisListStreams(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='ListStreams')


class KinesisListTagsForStream(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='ListTagsForStream')


class KinesisMergeShards(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='MergeShards')


class KinesisPutRecord(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='PutRecord')


class KinesisPutRecords(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='PutRecords')


class KinesisRemoveTagsFromStream(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='RemoveTagsFromStream')


class KinesisSplitShard(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='SplitShard')


class KinesisUpdateShardCount(IamAction):
    def __init__(self):
        super().__init__('kinesis', pattern='UpdateShardCount')


class KinesisanalyticsAddApplicationInput(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='AddApplicationInput')


class KinesisanalyticsAddApplicationOutput(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='AddApplicationOutput')


class KinesisanalyticsAddApplicationReferenceDataSource(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='AddApplicationReferenceDataSource')


class KinesisanalyticsCreateApplication(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='CreateApplication')


class KinesisanalyticsDeleteApplication(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='DeleteApplication')


class KinesisanalyticsDeleteApplicationOutput(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='DeleteApplicationOutput')


class KinesisanalyticsDeleteApplicationReferenceDataSource(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='DeleteApplicationReferenceDataSource')


class KinesisanalyticsDescribeApplication(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='DescribeApplication')


class KinesisanalyticsDiscoverInputSchema(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='DiscoverInputSchema')


class KinesisanalyticsListApplications(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='ListApplications')


class KinesisanalyticsStartApplication(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='StartApplication')


class KinesisanalyticsStopApplication(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='StopApplication')


class KinesisanalyticsUpdateApplication(IamAction):
    def __init__(self):
        super().__init__('kinesisanalytics', pattern='UpdateApplication')


class KinesisvideoCreateStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='CreateStream')


class KinesisvideoDeleteStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='DeleteStream')


class KinesisvideoDescribeStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='DescribeStream')


class KinesisvideoGetDataEndpoint(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='GetDataEndpoint')


class KinesisvideoGetMedia(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='GetMedia')


class KinesisvideoGetMediaForFragmentList(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='GetMediaForFragmentList')


class KinesisvideoListFragments(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='ListFragments')


class KinesisvideoListStreams(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='ListStreams')


class KinesisvideoListTagsForStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='ListTagsForStream')


class KinesisvideoPutMedia(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='PutMedia')


class KinesisvideoTagStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='TagStream')


class KinesisvideoUntagStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='UntagStream')


class KinesisvideoUpdateDataRetention(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='UpdateDataRetention')


class KinesisvideoUpdateStream(IamAction):
    def __init__(self):
        super().__init__('kinesisvideo', pattern='UpdateStream')


class KmsCancelKeyDeletion(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='CancelKeyDeletion')


class KmsCreateAlias(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='CreateAlias')


class KmsCreateGrant(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='CreateGrant')


class KmsCreateKey(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='CreateKey')


class KmsDecrypt(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='Decrypt')


class KmsDeleteAlias(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='DeleteAlias')


class KmsDeleteImportedKeyMaterial(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='DeleteImportedKeyMaterial')


class KmsDescribeKey(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='DescribeKey')


class KmsDisableKey(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='DisableKey')


class KmsDisableKeyRotation(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='DisableKeyRotation')


class KmsEnableKey(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='EnableKey')


class KmsEnableKeyRotation(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='EnableKeyRotation')


class KmsEncrypt(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='Encrypt')


class KmsGenerateDataKey(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='GenerateDataKey')


class KmsGenerateDataKeyWithoutPlaintext(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='GenerateDataKeyWithoutPlaintext')


class KmsGenerateRandom(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='GenerateRandom')


class KmsGetKeyPolicy(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='GetKeyPolicy')


class KmsGetKeyRotationStatus(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='GetKeyRotationStatus')


class KmsGetParametersForImport(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='GetParametersForImport')


class KmsImportKeyMaterial(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ImportKeyMaterial')


class KmsListAliases(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ListAliases')


class KmsListGrants(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ListGrants')


class KmsListKeyPolicies(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ListKeyPolicies')


class KmsListKeys(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ListKeys')


class KmsListResourceTags(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ListResourceTags')


class KmsListRetirableGrants(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ListRetirableGrants')


class KmsPutKeyPolicy(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='PutKeyPolicy')


class KmsReEncryptFrom(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ReEncryptFrom')


class KmsReEncryptTo(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ReEncryptTo')


class KmsRetireGrant(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='RetireGrant')


class KmsRevokeGrant(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='RevokeGrant')


class KmsScheduleKeyDeletion(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='ScheduleKeyDeletion')


class KmsTagResource(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='TagResource')


class KmsUntagResource(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='UntagResource')


class KmsUpdateAlias(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='UpdateAlias')


class KmsUpdateKeyDescription(IamAction):
    def __init__(self):
        super().__init__('kms', pattern='UpdateKeyDescription')


class LambdaAddPermission(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='AddPermission')


class LambdaCreateAlias(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='CreateAlias')


class LambdaCreateEventSourceMapping(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='CreateEventSourceMapping')


class LambdaCreateFunction(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='CreateFunction')


class LambdaDeleteAlias(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='DeleteAlias')


class LambdaDeleteEventSourceMapping(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='DeleteEventSourceMapping')


class LambdaDeleteFunction(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='DeleteFunction')


class LambdaDeleteFunctionConcurrency(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='DeleteFunctionConcurrency')


class LambdaEnableReplication(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='EnableReplication')


class LambdaGetAccountSettings(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='GetAccountSettings')


class LambdaGetAlias(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='GetAlias')


class LambdaGetEventSourceMapping(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='GetEventSourceMapping')


class LambdaGetFunction(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='GetFunction')


class LambdaGetFunctionConfiguration(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='GetFunctionConfiguration')


class LambdaGetPolicy(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='GetPolicy')


class LambdaInvokeAsync(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='InvokeAsync')


class LambdaInvokeFunction(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='InvokeFunction')


class LambdaListAliases(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='ListAliases')


class LambdaListEventSourceMappings(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='ListEventSourceMappings')


class LambdaListFunctions(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='ListFunctions')


class LambdaListTags(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='ListTags')


class LambdaListVersionsByFunction(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='ListVersionsByFunction')


class LambdaPublishVersion(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='PublishVersion')


class LambdaPutFunctionConcurrency(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='PutFunctionConcurrency')


class LambdaRemovePermission(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='RemovePermission')


class LambdaTagResource(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='TagResource')


class LambdaUntagResource(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='UntagResource')


class LambdaUpdateAlias(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='UpdateAlias')


class LambdaUpdateEventSourceMapping(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='UpdateEventSourceMapping')


class LambdaUpdateFunctionCode(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='UpdateFunctionCode')


class LambdaUpdateFunctionConfiguration(IamAction):
    def __init__(self):
        super().__init__('lambda', pattern='UpdateFunctionConfiguration')


class LexCreateBotVersion(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='CreateBotVersion')


class LexCreateIntentVersion(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='CreateIntentVersion')


class LexCreateSlotTypeVersion(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='CreateSlotTypeVersion')


class LexDeleteBot(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteBot')


class LexDeleteBotAlias(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteBotAlias')


class LexDeleteBotChannelAssociation(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteBotChannelAssociation')


class LexDeleteBotVersion(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteBotVersion')


class LexDeleteIntent(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteIntent')


class LexDeleteIntentVersion(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteIntentVersion')


class LexDeleteSlotType(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteSlotType')


class LexDeleteSlotTypeVersion(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteSlotTypeVersion')


class LexDeleteUtterances(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='DeleteUtterances')


class LexGetBot(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBot')


class LexGetBotAlias(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBotAlias')


class LexGetBotAliases(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBotAliases')


class LexGetBotChannelAssociation(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBotChannelAssociation')


class LexGetBotChannelAssociations(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBotChannelAssociations')


class LexGetBotVersions(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBotVersions')


class LexGetBots(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBots')


class LexGetBuiltinIntent(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBuiltinIntent')


class LexGetBuiltinIntents(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBuiltinIntents')


class LexGetBuiltinSlotTypes(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetBuiltinSlotTypes')


class LexGetIntent(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetIntent')


class LexGetIntentVersions(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetIntentVersions')


class LexGetIntents(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetIntents')


class LexGetSlotType(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetSlotType')


class LexGetSlotTypeVersions(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetSlotTypeVersions')


class LexGetSlotTypes(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetSlotTypes')


class LexGetUtterancesView(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='GetUtterancesView')


class LexPostContent(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='PostContent')


class LexPostText(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='PostText')


class LexPutBot(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='PutBot')


class LexPutBotAlias(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='PutBotAlias')


class LexPutIntent(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='PutIntent')


class LexPutSlotType(IamAction):
    def __init__(self):
        super().__init__('lex', pattern='PutSlotType')


class LightsailAllocateStaticIp(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='AllocateStaticIp')


class LightsailAttachStaticIp(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='AttachStaticIp')


class LightsailCloseInstancePublicPorts(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CloseInstancePublicPorts')


class LightsailCreateDomain(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CreateDomain')


class LightsailCreateDomainEntry(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CreateDomainEntry')


class LightsailCreateInstanceSnapshot(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CreateInstanceSnapshot')


class LightsailCreateInstances(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CreateInstances')


class LightsailCreateInstancesFromSnapshot(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CreateInstancesFromSnapshot')


class LightsailCreateKeyPair(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='CreateKeyPair')


class LightsailDeleteDomain(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DeleteDomain')


class LightsailDeleteDomainEntry(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DeleteDomainEntry')


class LightsailDeleteInstance(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DeleteInstance')


class LightsailDeleteInstanceSnapshot(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DeleteInstanceSnapshot')


class LightsailDeleteKeyPair(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DeleteKeyPair')


class LightsailDetachStaticIp(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DetachStaticIp')


class LightsailDownloadDefaultKeyPair(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='DownloadDefaultKeyPair')


class LightsailGetActiveNames(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetActiveNames')


class LightsailGetBlueprints(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetBlueprints')


class LightsailGetBundles(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetBundles')


class LightsailGetDomain(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetDomain')


class LightsailGetDomains(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetDomains')


class LightsailGetInstance(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstance')


class LightsailGetInstanceAccessDetails(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstanceAccessDetails')


class LightsailGetInstanceMetricData(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstanceMetricData')


class LightsailGetInstancePortStates(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstancePortStates')


class LightsailGetInstanceSnapshot(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstanceSnapshot')


class LightsailGetInstanceSnapshots(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstanceSnapshots')


class LightsailGetInstanceState(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstanceState')


class LightsailGetInstances(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetInstances')


class LightsailGetKeyPair(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetKeyPair')


class LightsailGetKeyPairs(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetKeyPairs')


class LightsailGetOperation(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetOperation')


class LightsailGetOperations(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetOperations')


class LightsailGetOperationsForResource(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetOperationsForResource')


class LightsailGetRegions(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetRegions')


class LightsailGetStaticIp(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetStaticIp')


class LightsailGetStaticIps(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='GetStaticIps')


class LightsailImportKeyPair(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='ImportKeyPair')


class LightsailIsVpcPeered(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='IsVpcPeered')


class LightsailOpenInstancePublicPorts(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='OpenInstancePublicPorts')


class LightsailPeerVpc(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='PeerVpc')


class LightsailRebootInstance(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='RebootInstance')


class LightsailReleaseStaticIp(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='ReleaseStaticIp')


class LightsailStartInstance(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='StartInstance')


class LightsailStopInstance(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='StopInstance')


class LightsailUnpeerVpc(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='UnpeerVpc')


class LightsailUpdateDomainEntry(IamAction):
    def __init__(self):
        super().__init__('lightsail', pattern='UpdateDomainEntry')


class LogsAssociateKmsKey(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='AssociateKmsKey')


class LogsCancelExportTask(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='CancelExportTask')


class LogsCreateExportTask(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='CreateExportTask')


class LogsCreateLogGroup(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='CreateLogGroup')


class LogsCreateLogStream(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='CreateLogStream')


class LogsDeleteDestination(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteDestination')


class LogsDeleteLogGroup(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteLogGroup')


class LogsDeleteLogStream(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteLogStream')


class LogsDeleteMetricFilter(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteMetricFilter')


class LogsDeleteResourcePolicy(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteResourcePolicy')


class LogsDeleteRetentionPolicy(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteRetentionPolicy')


class LogsDeleteSubscriptionFilter(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DeleteSubscriptionFilter')


class LogsDescribeDestinations(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeDestinations')


class LogsDescribeExportTasks(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeExportTasks')


class LogsDescribeLogGroups(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeLogGroups')


class LogsDescribeLogStreams(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeLogStreams')


class LogsDescribeMetricFilters(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeMetricFilters')


class LogsDescribeResourcePolicies(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeResourcePolicies')


class LogsDescribeSubscriptionFilters(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DescribeSubscriptionFilters')


class LogsDisassociateKmsKey(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='DisassociateKmsKey')


class LogsFilterLogEvents(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='FilterLogEvents')


class LogsGetLogEvents(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='GetLogEvents')


class LogsListTagsLogGroup(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='ListTagsLogGroup')


class LogsPutDestination(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutDestination')


class LogsPutDestinationPolicy(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutDestinationPolicy')


class LogsPutLogEvents(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutLogEvents')


class LogsPutMetricFilter(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutMetricFilter')


class LogsPutResourcePolicy(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutResourcePolicy')


class LogsPutRetentionPolicy(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutRetentionPolicy')


class LogsPutSubscriptionFilter(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='PutSubscriptionFilter')


class LogsTagLogGroup(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='TagLogGroup')


class LogsTestMetricFilter(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='TestMetricFilter')


class LogsUntagLogGroup(IamAction):
    def __init__(self):
        super().__init__('logs', pattern='UntagLogGroup')


class MachinelearningAddTags(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='AddTags')


class MachinelearningCreateBatchPrediction(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateBatchPrediction')


class MachinelearningCreateDataSourceFromRDS(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateDataSourceFromRDS')


class MachinelearningCreateDataSourceFromRedshift(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateDataSourceFromRedshift')


class MachinelearningCreateDataSourceFromS3(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateDataSourceFromS3')


class MachinelearningCreateEvaluation(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateEvaluation')


class MachinelearningCreateMLModel(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateMLModel')


class MachinelearningCreateRealtimeEndpoint(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='CreateRealtimeEndpoint')


class MachinelearningDeleteBatchPrediction(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DeleteBatchPrediction')


class MachinelearningDeleteDataSource(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DeleteDataSource')


class MachinelearningDeleteEvaluation(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DeleteEvaluation')


class MachinelearningDeleteMLModel(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DeleteMLModel')


class MachinelearningDeleteRealtimeEndpoint(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DeleteRealtimeEndpoint')


class MachinelearningDeleteTags(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DeleteTags')


class MachinelearningDescribeBatchPredictions(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DescribeBatchPredictions')


class MachinelearningDescribeDataSources(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DescribeDataSources')


class MachinelearningDescribeEvaluations(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DescribeEvaluations')


class MachinelearningDescribeMLModels(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DescribeMLModels')


class MachinelearningDescribeTags(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='DescribeTags')


class MachinelearningGetBatchPrediction(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='GetBatchPrediction')


class MachinelearningGetDataSource(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='GetDataSource')


class MachinelearningGetEvaluation(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='GetEvaluation')


class MachinelearningGetMLModel(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='GetMLModel')


class MachinelearningPredict(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='Predict')


class MachinelearningUpdateBatchPrediction(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='UpdateBatchPrediction')


class MachinelearningUpdateDataSource(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='UpdateDataSource')


class MachinelearningUpdateEvaluation(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='UpdateEvaluation')


class MachinelearningUpdateMLModel(IamAction):
    def __init__(self):
        super().__init__('machinelearning', pattern='UpdateMLModel')


class MechanicalturkApproveAssignment(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='ApproveAssignment')


class MechanicalturkApproveRejectedAssignment(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='ApproveRejectedAssignment')


class MechanicalturkAssignQualification(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='AssignQualification')


class MechanicalturkBlockWorker(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='BlockWorker')


class MechanicalturkChangeHITTypeOfHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='ChangeHITTypeOfHIT')


class MechanicalturkCreateHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='CreateHIT')


class MechanicalturkCreateQualificationType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='CreateQualificationType')


class MechanicalturkDisableHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='DisableHIT')


class MechanicalturkDisposeHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='DisposeHIT')


class MechanicalturkDisposeQualificationType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='DisposeQualificationType')


class MechanicalturkExtendHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='ExtendHIT')


class MechanicalturkForceExpireHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='ForceExpireHIT')


class MechanicalturkGetAccountBalance(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetAccountBalance')


class MechanicalturkGetAssignment(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetAssignment')


class MechanicalturkGetAssignmentsForHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetAssignmentsForHIT')


class MechanicalturkGetBlockedWorkers(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetBlockedWorkers')


class MechanicalturkGetBonusPayments(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetBonusPayments')


class MechanicalturkGetFileUploadURL(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetFileUploadURL')


class MechanicalturkGetHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetHIT')


class MechanicalturkGetHITsForQualificationType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetHITsForQualificationType')


class MechanicalturkGetQualificationRequests(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetQualificationRequests')


class MechanicalturkGetQualificationScore(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetQualificationScore')


class MechanicalturkGetQualificationType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetQualificationType')


class MechanicalturkGetQualificationsForQualificationType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetQualificationsForQualificationType')


class MechanicalturkGetRequesterStatistic(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetRequesterStatistic')


class MechanicalturkGetRequesterWorkerStatistic(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetRequesterWorkerStatistic')


class MechanicalturkGetReviewResultsForHIT(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetReviewResultsForHIT')


class MechanicalturkGetReviewableHITs(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GetReviewableHITs')


class MechanicalturkGrantBonus(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GrantBonus')


class MechanicalturkGrantQualification(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='GrantQualification')


class MechanicalturkNotifyWorkers(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='NotifyWorkers')


class MechanicalturkRegisterHITType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='RegisterHITType')


class MechanicalturkRejectAssignment(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='RejectAssignment')


class MechanicalturkRejectQualificationRequest(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='RejectQualificationRequest')


class MechanicalturkRevokeQualification(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='RevokeQualification')


class MechanicalturkSearchHITs(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='SearchHITs')


class MechanicalturkSearchQualificationTypes(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='SearchQualificationTypes')


class MechanicalturkSendTestEventNotification(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='SendTestEventNotification')


class MechanicalturkSetHITAsReviewing(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='SetHITAsReviewing')


class MechanicalturkSetHITTypeNotification(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='SetHITTypeNotification')


class MechanicalturkUnblockWorker(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='UnblockWorker')


class MechanicalturkUpdateQualificationScore(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='UpdateQualificationScore')


class MechanicalturkUpdateQualificationType(IamAction):
    def __init__(self):
        super().__init__('mechanicalturk', pattern='UpdateQualificationType')


class MediaconvertCancelJob(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='CancelJob')


class MediaconvertCreateJob(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='CreateJob')


class MediaconvertCreateJobTemplate(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='CreateJobTemplate')


class MediaconvertCreatePreset(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='CreatePreset')


class MediaconvertCreateQueue(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='CreateQueue')


class MediaconvertDeleteJobTemplate(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='DeleteJobTemplate')


class MediaconvertDeletePreset(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='DeletePreset')


class MediaconvertDeleteQueue(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='DeleteQueue')


class MediaconvertDescribeEndpoint(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='DescribeEndpoint')


class MediaconvertGetJob(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='GetJob')


class MediaconvertGetJobTemplate(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='GetJobTemplate')


class MediaconvertGetPreset(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='GetPreset')


class MediaconvertGetQueue(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='GetQueue')


class MediaconvertListJobTemplates(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='ListJobTemplates')


class MediaconvertListJobs(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='ListJobs')


class MediaconvertListPresets(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='ListPresets')


class MediaconvertListQueues(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='ListQueues')


class MediaconvertUpdateJobTemplate(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='UpdateJobTemplate')


class MediaconvertUpdatePreset(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='UpdatePreset')


class MediaconvertUpdateQueue(IamAction):
    def __init__(self):
        super().__init__('mediaconvert', pattern='UpdateQueue')


class MedialiveCreateChannel(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='CreateChannel')


class MedialiveCreateInput(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='CreateInput')


class MedialiveCreateInputSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='CreateInputSecurityGroup')


class MedialiveDeleteChannel(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='DeleteChannel')


class MedialiveDeleteInput(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='DeleteInput')


class MedialiveDeleteInputSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='DeleteInputSecurityGroup')


class MedialiveDescribeChannel(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='DescribeChannel')


class MedialiveDescribeInput(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='DescribeInput')


class MedialiveDescribeInputSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='DescribeInputSecurityGroup')


class MedialiveListChannels(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='ListChannels')


class MedialiveListInputSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='ListInputSecurityGroups')


class MedialiveListInputs(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='ListInputs')


class MedialiveStartChannel(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='StartChannel')


class MedialiveStopChannel(IamAction):
    def __init__(self):
        super().__init__('medialive', pattern='StopChannel')


class MediapackageCreateChannel(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='CreateChannel')


class MediapackageCreateOriginEndpoint(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='CreateOriginEndpoint')


class MediapackageDeleteChannel(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='DeleteChannel')


class MediapackageDeleteOriginEndpoint(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='DeleteOriginEndpoint')


class MediapackageDescribeChannel(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='DescribeChannel')


class MediapackageDescribeOriginEndpoint(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='DescribeOriginEndpoint')


class MediapackageListChannels(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='ListChannels')


class MediapackageListOriginEndpoints(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='ListOriginEndpoints')


class MediapackageUpdateChannel(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='UpdateChannel')


class MediapackageUpdateOriginEndpoint(IamAction):
    def __init__(self):
        super().__init__('mediapackage', pattern='UpdateOriginEndpoint')


class MediastoreCreateContainer(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='CreateContainer')


class MediastoreDeleteContainer(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='DeleteContainer')


class MediastoreDeleteContainerPolicy(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='DeleteContainerPolicy')


class MediastoreDeleteObject(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='DeleteObject')


class MediastoreDescribeContainer(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='DescribeContainer')


class MediastoreDescribeObject(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='DescribeObject')


class MediastoreGetContainerPolicy(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='GetContainerPolicy')


class MediastoreGetObject(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='GetObject')


class MediastoreListContainers(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='ListContainers')


class MediastoreListItems(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='ListItems')


class MediastorePutContainerPolicy(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='PutContainerPolicy')


class MediastorePutObject(IamAction):
    def __init__(self):
        super().__init__('mediastore', pattern='PutObject')


class MghAssociateCreatedArtifact(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='AssociateCreatedArtifact')


class MghAssociateDiscoveredResource(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='AssociateDiscoveredResource')


class MghCreateProgressUpdateStream(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='CreateProgressUpdateStream')


class MghDeleteProgressUpdateStream(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='DeleteProgressUpdateStream')


class MghDescribeApplicationState(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='DescribeApplicationState')


class MghDescribeMigrationTask(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='DescribeMigrationTask')


class MghDisassociateCreatedArtifact(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='DisassociateCreatedArtifact')


class MghDisassociateDiscoveredResource(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='DisassociateDiscoveredResource')


class MghImportMigrationTask(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='ImportMigrationTask')


class MghListCreatedArtifacts(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='ListCreatedArtifacts')


class MghListDiscoveredResources(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='ListDiscoveredResources')


class MghListMigrationTasks(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='ListMigrationTasks')


class MghListProgressUpdateStreams(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='ListProgressUpdateStreams')


class MghNotifyApplicationState(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='NotifyApplicationState')


class MghNotifyMigrationTaskState(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='NotifyMigrationTaskState')


class MghPutResourceAttributes(IamAction):
    def __init__(self):
        super().__init__('mgh', pattern='PutResourceAttributes')


class MobileanalyticsGetFinancialReports(IamAction):
    def __init__(self):
        super().__init__('mobileanalytics', pattern='GetFinancialReports')


class MobileanalyticsGetReports(IamAction):
    def __init__(self):
        super().__init__('mobileanalytics', pattern='GetReports')


class MobileanalyticsPutEvents(IamAction):
    def __init__(self):
        super().__init__('mobileanalytics', pattern='PutEvents')


class MobilehubCreateProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='CreateProject')


class MobilehubCreateServiceRole(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='CreateServiceRole')


class MobilehubDeleteProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='DeleteProject')


class MobilehubDeployToStage(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='DeployToStage')


class MobilehubDescribeBundle(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='DescribeBundle')


class MobilehubExportBundle(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ExportBundle')


class MobilehubExportProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ExportProject')


class MobilehubGenerateProjectParameters(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='GenerateProjectParameters')


class MobilehubGetProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='GetProject')


class MobilehubGetProjectSnapshot(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='GetProjectSnapshot')


class MobilehubImportProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ImportProject')


class MobilehubListAvailableConnectors(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ListAvailableConnectors')


class MobilehubListAvailableFeatures(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ListAvailableFeatures')


class MobilehubListAvailableRegions(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ListAvailableRegions')


class MobilehubListBundles(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ListBundles')


class MobilehubListProjects(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='ListProjects')


class MobilehubSynchronizeProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='SynchronizeProject')


class MobilehubUpdateProject(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='UpdateProject')


class MobilehubVerifyServiceRole(IamAction):
    def __init__(self):
        super().__init__('mobilehub', pattern='VerifyServiceRole')


class MobiletargetingCreateCampaign(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='CreateCampaign')


class MobiletargetingCreateImportJob(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='CreateImportJob')


class MobiletargetingCreateSegment(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='CreateSegment')


class MobiletargetingDeleteApnsChannel(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='DeleteApnsChannel')


class MobiletargetingDeleteCampaign(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='DeleteCampaign')


class MobiletargetingDeleteGcmChannel(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='DeleteGcmChannel')


class MobiletargetingDeleteSegment(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='DeleteSegment')


class MobiletargetingGetApnsChannel(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetApnsChannel')


class MobiletargetingGetApplicationSettings(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetApplicationSettings')


class MobiletargetingGetCampaign(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetCampaign')


class MobiletargetingGetCampaignActivities(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetCampaignActivities')


class MobiletargetingGetCampaignVersion(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetCampaignVersion')


class MobiletargetingGetCampaignVersions(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetCampaignVersions')


class MobiletargetingGetCampaigns(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetCampaigns')


class MobiletargetingGetEndpoint(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetEndpoint')


class MobiletargetingGetGcmChannel(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetGcmChannel')


class MobiletargetingGetImportJob(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetImportJob')


class MobiletargetingGetImportJobs(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetImportJobs')


class MobiletargetingGetReports(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetReports')


class MobiletargetingGetSegment(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetSegment')


class MobiletargetingGetSegmentImportJobs(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetSegmentImportJobs')


class MobiletargetingGetSegmentVersion(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetSegmentVersion')


class MobiletargetingGetSegmentVersions(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetSegmentVersions')


class MobiletargetingGetSegments(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='GetSegments')


class MobiletargetingUpdateApnsChannel(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateApnsChannel')


class MobiletargetingUpdateApplicationSettings(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateApplicationSettings')


class MobiletargetingUpdateCampaign(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateCampaign')


class MobiletargetingUpdateEndpoint(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateEndpoint')


class MobiletargetingUpdateEndpointsBatch(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateEndpointsBatch')


class MobiletargetingUpdateGcmChannel(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateGcmChannel')


class MobiletargetingUpdateSegment(IamAction):
    def __init__(self):
        super().__init__('mobiletargeting', pattern='UpdateSegment')


class MqCreateBroker(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='CreateBroker')


class MqCreateConfiguration(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='CreateConfiguration')


class MqCreateUser(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='CreateUser')


class MqDeleteBroker(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='DeleteBroker')


class MqDeleteUser(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='DeleteUser')


class MqDescribeBroker(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='DescribeBroker')


class MqDescribeConfiguration(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='DescribeConfiguration')


class MqDescribeConfigurationRevision(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='DescribeConfigurationRevision')


class MqDescribeUser(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='DescribeUser')


class MqListBrokers(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='ListBrokers')


class MqListConfigurationRevisions(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='ListConfigurationRevisions')


class MqListConfigurations(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='ListConfigurations')


class MqListUsers(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='ListUsers')


class MqRebootBroker(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='RebootBroker')


class MqUpdateBroker(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='UpdateBroker')


class MqUpdateConfiguration(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='UpdateConfiguration')


class MqUpdateUser(IamAction):
    def __init__(self):
        super().__init__('mq', pattern='UpdateUser')


class OpsworksCmAssociateNode(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='AssociateNode')


class OpsworksCmCreateBackup(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='CreateBackup')


class OpsworksCmCreateServer(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='CreateServer')


class OpsworksCmDeleteBackup(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DeleteBackup')


class OpsworksCmDeleteServer(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DeleteServer')


class OpsworksCmDescribeAccountAttributes(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DescribeAccountAttributes')


class OpsworksCmDescribeBackups(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DescribeBackups')


class OpsworksCmDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DescribeEvents')


class OpsworksCmDescribeNodeAssociationStatus(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DescribeNodeAssociationStatus')


class OpsworksCmDescribeServers(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DescribeServers')


class OpsworksCmDisassociateNode(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='DisassociateNode')


class OpsworksCmRestoreServer(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='RestoreServer')


class OpsworksCmStartMaintenance(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='StartMaintenance')


class OpsworksCmUpdateServer(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='UpdateServer')


class OpsworksCmUpdateServerEngineAttributes(IamAction):
    def __init__(self):
        super().__init__('opsworks-cm', pattern='UpdateServerEngineAttributes')


class OpsworksAssignInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='AssignInstance')


class OpsworksAssignVolume(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='AssignVolume')


class OpsworksAssociateElasticIp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='AssociateElasticIp')


class OpsworksAttachElasticLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='AttachElasticLoadBalancer')


class OpsworksCloneStack(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CloneStack')


class OpsworksCreateApp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CreateApp')


class OpsworksCreateDeployment(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CreateDeployment')


class OpsworksCreateInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CreateInstance')


class OpsworksCreateLayer(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CreateLayer')


class OpsworksCreateStack(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CreateStack')


class OpsworksCreateUserProfile(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='CreateUserProfile')


class OpsworksDeleteApp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeleteApp')


class OpsworksDeleteInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeleteInstance')


class OpsworksDeleteLayer(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeleteLayer')


class OpsworksDeleteStack(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeleteStack')


class OpsworksDeleteUserProfile(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeleteUserProfile')


class OpsworksDeregisterEcsCluster(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeregisterEcsCluster')


class OpsworksDeregisterElasticIp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeregisterElasticIp')


class OpsworksDeregisterInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeregisterInstance')


class OpsworksDeregisterRdsDbInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeregisterRdsDbInstance')


class OpsworksDeregisterVolume(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DeregisterVolume')


class OpsworksDescribeAgentVersions(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeAgentVersions')


class OpsworksDescribeApps(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeApps')


class OpsworksDescribeCommands(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeCommands')


class OpsworksDescribeDeployments(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeDeployments')


class OpsworksDescribeEcsClusters(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeEcsClusters')


class OpsworksDescribeElasticIps(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeElasticIps')


class OpsworksDescribeElasticLoadBalancers(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeElasticLoadBalancers')


class OpsworksDescribeInstances(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeInstances')


class OpsworksDescribeLayers(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeLayers')


class OpsworksDescribeLoadBasedAutoScaling(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeLoadBasedAutoScaling')


class OpsworksDescribeMyUserProfile(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeMyUserProfile')


class OpsworksDescribePermissions(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribePermissions')


class OpsworksDescribeRaidArrays(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeRaidArrays')


class OpsworksDescribeRdsDbInstances(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeRdsDbInstances')


class OpsworksDescribeServiceErrors(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeServiceErrors')


class OpsworksDescribeStackProvisioningParameters(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeStackProvisioningParameters')


class OpsworksDescribeStackSummary(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeStackSummary')


class OpsworksDescribeStacks(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeStacks')


class OpsworksDescribeTimeBasedAutoScaling(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeTimeBasedAutoScaling')


class OpsworksDescribeUserProfiles(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeUserProfiles')


class OpsworksDescribeVolumes(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DescribeVolumes')


class OpsworksDetachElasticLoadBalancer(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DetachElasticLoadBalancer')


class OpsworksDisassociateElasticIp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='DisassociateElasticIp')


class OpsworksGetHostnameSuggestion(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='GetHostnameSuggestion')


class OpsworksGrantAccess(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='GrantAccess')


class OpsworksListTags(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='ListTags')


class OpsworksRebootInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='RebootInstance')


class OpsworksRegisterEcsCluster(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='RegisterEcsCluster')


class OpsworksRegisterElasticIp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='RegisterElasticIp')


class OpsworksRegisterInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='RegisterInstance')


class OpsworksRegisterRdsDbInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='RegisterRdsDbInstance')


class OpsworksRegisterVolume(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='RegisterVolume')


class OpsworksSetLoadBasedAutoScaling(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='SetLoadBasedAutoScaling')


class OpsworksSetPermission(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='SetPermission')


class OpsworksSetTimeBasedAutoScaling(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='SetTimeBasedAutoScaling')


class OpsworksStartInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='StartInstance')


class OpsworksStartStack(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='StartStack')


class OpsworksStopInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='StopInstance')


class OpsworksStopStack(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='StopStack')


class OpsworksTagResource(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='TagResource')


class OpsworksUnassignInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UnassignInstance')


class OpsworksUnassignVolume(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UnassignVolume')


class OpsworksUntagResource(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UntagResource')


class OpsworksUpdateApp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateApp')


class OpsworksUpdateElasticIp(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateElasticIp')


class OpsworksUpdateInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateInstance')


class OpsworksUpdateLayer(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateLayer')


class OpsworksUpdateMyUserProfile(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateMyUserProfile')


class OpsworksUpdateRdsDbInstance(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateRdsDbInstance')


class OpsworksUpdateStack(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateStack')


class OpsworksUpdateUserProfile(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateUserProfile')


class OpsworksUpdateVolume(IamAction):
    def __init__(self):
        super().__init__('opsworks', pattern='UpdateVolume')


class OrganizationsAcceptHandshake(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='AcceptHandshake')


class OrganizationsAttachPolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='AttachPolicy')


class OrganizationsCancelHandshake(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='CancelHandshake')


class OrganizationsCreateAccount(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='CreateAccount')


class OrganizationsCreateOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='CreateOrganization')


class OrganizationsCreateOrganizationalUnit(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='CreateOrganizationalUnit')


class OrganizationsCreatePolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='CreatePolicy')


class OrganizationsDeclineHandshake(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DeclineHandshake')


class OrganizationsDeleteOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DeleteOrganization')


class OrganizationsDeleteOrganizationalUnit(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DeleteOrganizationalUnit')


class OrganizationsDeletePolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DeletePolicy')


class OrganizationsDescribeAccount(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DescribeAccount')


class OrganizationsDescribeCreateAccountStatus(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DescribeCreateAccountStatus')


class OrganizationsDescribeHandshake(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DescribeHandshake')


class OrganizationsDescribeOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DescribeOrganization')


class OrganizationsDescribeOrganizationalUnit(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DescribeOrganizationalUnit')


class OrganizationsDescribePolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DescribePolicy')


class OrganizationsDetachPolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DetachPolicy')


class OrganizationsDisablePolicyType(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='DisablePolicyType')


class OrganizationsEnableAllFeatures(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='EnableAllFeatures')


class OrganizationsEnablePolicyType(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='EnablePolicyType')


class OrganizationsInviteAccountToOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='InviteAccountToOrganization')


class OrganizationsLeaveOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='LeaveOrganization')


class OrganizationsListAccounts(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListAccounts')


class OrganizationsListAccountsForParent(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListAccountsForParent')


class OrganizationsListChildren(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListChildren')


class OrganizationsListCreateAccountStatus(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListCreateAccountStatus')


class OrganizationsListHandshakesForAccount(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListHandshakesForAccount')


class OrganizationsListHandshakesForOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListHandshakesForOrganization')


class OrganizationsListOrganizationalUnitsForParent(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListOrganizationalUnitsForParent')


class OrganizationsListParents(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListParents')


class OrganizationsListPolicies(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListPolicies')


class OrganizationsListPoliciesForTarget(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListPoliciesForTarget')


class OrganizationsListRoots(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListRoots')


class OrganizationsListTargetsForPolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='ListTargetsForPolicy')


class OrganizationsMoveAccount(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='MoveAccount')


class OrganizationsRemoveAccountFromOrganization(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='RemoveAccountFromOrganization')


class OrganizationsUpdateOrganizationalUnit(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='UpdateOrganizationalUnit')


class OrganizationsUpdatePolicy(IamAction):
    def __init__(self):
        super().__init__('organizations', pattern='UpdatePolicy')


class PollyDeleteLexicon(IamAction):
    def __init__(self):
        super().__init__('polly', pattern='DeleteLexicon')


class PollyDescribeVoices(IamAction):
    def __init__(self):
        super().__init__('polly', pattern='DescribeVoices')


class PollyGetLexicon(IamAction):
    def __init__(self):
        super().__init__('polly', pattern='GetLexicon')


class PollyListLexicons(IamAction):
    def __init__(self):
        super().__init__('polly', pattern='ListLexicons')


class PollyPutLexicon(IamAction):
    def __init__(self):
        super().__init__('polly', pattern='PutLexicon')


class PollySynthesizeSpeech(IamAction):
    def __init__(self):
        super().__init__('polly', pattern='SynthesizeSpeech')


class PricingDescribeServices(IamAction):
    def __init__(self):
        super().__init__('pricing', pattern='DescribeServices')


class PricingGetAttributeValues(IamAction):
    def __init__(self):
        super().__init__('pricing', pattern='GetAttributeValues')


class PricingGetProducts(IamAction):
    def __init__(self):
        super().__init__('pricing', pattern='GetProducts')


class RdsAddRoleToDBCluster(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='AddRoleToDBCluster')


class RdsAddSourceIdentifierToSubscription(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='AddSourceIdentifierToSubscription')


class RdsAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='AddTagsToResource')


class RdsApplyPendingMaintenanceAction(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ApplyPendingMaintenanceAction')


class RdsAuthorizeDBSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='AuthorizeDBSecurityGroupIngress')


class RdsCopyDBClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CopyDBClusterSnapshot')


class RdsCopyDBParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CopyDBParameterGroup')


class RdsCopyDBSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CopyDBSnapshot')


class RdsCopyOptionGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CopyOptionGroup')


class RdsCreateDBCluster(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBCluster')


class RdsCreateDBClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBClusterParameterGroup')


class RdsCreateDBClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBClusterSnapshot')


class RdsCreateDBInstance(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBInstance')


class RdsCreateDBInstanceReadReplica(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBInstanceReadReplica')


class RdsCreateDBParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBParameterGroup')


class RdsCreateDBSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBSecurityGroup')


class RdsCreateDBSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBSnapshot')


class RdsCreateDBSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateDBSubnetGroup')


class RdsCreateEventSubscription(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateEventSubscription')


class RdsCreateOptionGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='CreateOptionGroup')


class RdsDeleteDBCluster(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBCluster')


class RdsDeleteDBClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBClusterParameterGroup')


class RdsDeleteDBClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBClusterSnapshot')


class RdsDeleteDBInstance(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBInstance')


class RdsDeleteDBParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBParameterGroup')


class RdsDeleteDBSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBSecurityGroup')


class RdsDeleteDBSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBSnapshot')


class RdsDeleteDBSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteDBSubnetGroup')


class RdsDeleteEventSubscription(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteEventSubscription')


class RdsDeleteOptionGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DeleteOptionGroup')


class RdsDescribeAccountAttributes(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeAccountAttributes')


class RdsDescribeCertificates(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeCertificates')


class RdsDescribeDBClusterParameterGroups(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBClusterParameterGroups')


class RdsDescribeDBClusterParameters(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBClusterParameters')


class RdsDescribeDBClusterSnapshotAttributes(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBClusterSnapshotAttributes')


class RdsDescribeDBClusterSnapshots(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBClusterSnapshots')


class RdsDescribeDBClusters(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBClusters')


class RdsDescribeDBEngineVersions(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBEngineVersions')


class RdsDescribeDBInstances(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBInstances')


class RdsDescribeDBLogFiles(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBLogFiles')


class RdsDescribeDBParameterGroups(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBParameterGroups')


class RdsDescribeDBParameters(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBParameters')


class RdsDescribeDBSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBSecurityGroups')


class RdsDescribeDBSnapshotAttributes(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBSnapshotAttributes')


class RdsDescribeDBSnapshots(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBSnapshots')


class RdsDescribeDBSubnetGroups(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeDBSubnetGroups')


class RdsDescribeEngineDefaultClusterParameters(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeEngineDefaultClusterParameters')


class RdsDescribeEngineDefaultParameters(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeEngineDefaultParameters')


class RdsDescribeEventCategories(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeEventCategories')


class RdsDescribeEventSubscriptions(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeEventSubscriptions')


class RdsDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeEvents')


class RdsDescribeOptionGroupOptions(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeOptionGroupOptions')


class RdsDescribeOptionGroups(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeOptionGroups')


class RdsDescribeOrderableDBInstanceOptions(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeOrderableDBInstanceOptions')


class RdsDescribePendingMaintenanceActions(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribePendingMaintenanceActions')


class RdsDescribeReservedDBInstances(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeReservedDBInstances')


class RdsDescribeReservedDBInstancesOfferings(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DescribeReservedDBInstancesOfferings')


class RdsDownloadCompleteDBLogFile(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DownloadCompleteDBLogFile')


class RdsDownloadDBLogFilePortion(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='DownloadDBLogFilePortion')


class RdsFailoverDBCluster(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='FailoverDBCluster')


class RdsListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ListTagsForResource')


class RdsModifyDBCluster(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBCluster')


class RdsModifyDBClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBClusterParameterGroup')


class RdsModifyDBClusterSnapshotAttribute(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBClusterSnapshotAttribute')


class RdsModifyDBInstance(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBInstance')


class RdsModifyDBParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBParameterGroup')


class RdsModifyDBSnapshotAttribute(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBSnapshotAttribute')


class RdsModifyDBSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyDBSubnetGroup')


class RdsModifyEventSubscription(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyEventSubscription')


class RdsModifyOptionGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ModifyOptionGroup')


class RdsPromoteReadReplica(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='PromoteReadReplica')


class RdsPurchaseReservedDBInstancesOffering(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='PurchaseReservedDBInstancesOffering')


class RdsRebootDBInstance(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RebootDBInstance')


class RdsRemoveSourceIdentifierFromSubscription(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RemoveSourceIdentifierFromSubscription')


class RdsRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RemoveTagsFromResource')


class RdsResetDBClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ResetDBClusterParameterGroup')


class RdsResetDBParameterGroup(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='ResetDBParameterGroup')


class RdsRestoreDBClusterFromSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RestoreDBClusterFromSnapshot')


class RdsRestoreDBClusterToPointInTime(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RestoreDBClusterToPointInTime')


class RdsRestoreDBInstanceFromDBSnapshot(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RestoreDBInstanceFromDBSnapshot')


class RdsRestoreDBInstanceToPointInTime(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RestoreDBInstanceToPointInTime')


class RdsRevokeDBSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='RevokeDBSecurityGroupIngress')


class RdsStartDBInstance(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='StartDBInstance')


class RdsStopDBInstance(IamAction):
    def __init__(self):
        super().__init__('rds', pattern='StopDBInstance')


class RedshiftAuthorizeClusterSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='AuthorizeClusterSecurityGroupIngress')


class RedshiftAuthorizeSnapshotAccess(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='AuthorizeSnapshotAccess')


class RedshiftCancelQuerySession(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CancelQuerySession')


class RedshiftCopyClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CopyClusterSnapshot')


class RedshiftCreateCluster(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateCluster')


class RedshiftCreateClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateClusterParameterGroup')


class RedshiftCreateClusterSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateClusterSecurityGroup')


class RedshiftCreateClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateClusterSnapshot')


class RedshiftCreateClusterSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateClusterSubnetGroup')


class RedshiftCreateClusterUser(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateClusterUser')


class RedshiftCreateEventSubscription(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateEventSubscription')


class RedshiftCreateHsmClientCertificate(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateHsmClientCertificate')


class RedshiftCreateHsmConfiguration(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateHsmConfiguration')


class RedshiftCreateSnapshotCopyGrant(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateSnapshotCopyGrant')


class RedshiftCreateTags(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='CreateTags')


class RedshiftDeleteCluster(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteCluster')


class RedshiftDeleteClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteClusterParameterGroup')


class RedshiftDeleteClusterSecurityGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteClusterSecurityGroup')


class RedshiftDeleteClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteClusterSnapshot')


class RedshiftDeleteClusterSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteClusterSubnetGroup')


class RedshiftDeleteEventSubscription(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteEventSubscription')


class RedshiftDeleteHsmClientCertificate(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteHsmClientCertificate')


class RedshiftDeleteHsmConfiguration(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteHsmConfiguration')


class RedshiftDeleteSnapshotCopyGrant(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteSnapshotCopyGrant')


class RedshiftDeleteTags(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DeleteTags')


class RedshiftDescribeClusterParameterGroups(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusterParameterGroups')


class RedshiftDescribeClusterParameters(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusterParameters')


class RedshiftDescribeClusterSecurityGroups(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusterSecurityGroups')


class RedshiftDescribeClusterSnapshots(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusterSnapshots')


class RedshiftDescribeClusterSubnetGroups(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusterSubnetGroups')


class RedshiftDescribeClusterVersions(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusterVersions')


class RedshiftDescribeClusters(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeClusters')


class RedshiftDescribeDefaultClusterParameters(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeDefaultClusterParameters')


class RedshiftDescribeEventCategories(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeEventCategories')


class RedshiftDescribeEventSubscriptions(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeEventSubscriptions')


class RedshiftDescribeEvents(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeEvents')


class RedshiftDescribeHsmClientCertificates(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeHsmClientCertificates')


class RedshiftDescribeHsmConfigurations(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeHsmConfigurations')


class RedshiftDescribeLoggingStatus(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeLoggingStatus')


class RedshiftDescribeOrderableClusterOptions(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeOrderableClusterOptions')


class RedshiftDescribeReservedNodeOfferings(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeReservedNodeOfferings')


class RedshiftDescribeReservedNodes(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeReservedNodes')


class RedshiftDescribeResize(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeResize')


class RedshiftDescribeSnapshotCopyGrants(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeSnapshotCopyGrants')


class RedshiftDescribeTableRestoreStatus(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeTableRestoreStatus')


class RedshiftDescribeTags(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DescribeTags')


class RedshiftDisableLogging(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DisableLogging')


class RedshiftDisableSnapshotCopy(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='DisableSnapshotCopy')


class RedshiftEnableLogging(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='EnableLogging')


class RedshiftEnableSnapshotCopy(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='EnableSnapshotCopy')


class RedshiftGetClusterCredentials(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='GetClusterCredentials')


class RedshiftJoinGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='JoinGroup')


class RedshiftModifyCluster(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ModifyCluster')


class RedshiftModifyClusterIamRoles(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ModifyClusterIamRoles')


class RedshiftModifyClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ModifyClusterParameterGroup')


class RedshiftModifyClusterSubnetGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ModifyClusterSubnetGroup')


class RedshiftModifyEventSubscription(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ModifyEventSubscription')


class RedshiftModifySnapshotCopyRetentionPeriod(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ModifySnapshotCopyRetentionPeriod')


class RedshiftPurchaseReservedNodeOffering(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='PurchaseReservedNodeOffering')


class RedshiftRebootCluster(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='RebootCluster')


class RedshiftResetClusterParameterGroup(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ResetClusterParameterGroup')


class RedshiftRestoreFromClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='RestoreFromClusterSnapshot')


class RedshiftRestoreTableFromClusterSnapshot(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='RestoreTableFromClusterSnapshot')


class RedshiftRevokeClusterSecurityGroupIngress(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='RevokeClusterSecurityGroupIngress')


class RedshiftRevokeSnapshotAccess(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='RevokeSnapshotAccess')


class RedshiftRotateEncryptionKey(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='RotateEncryptionKey')


class RedshiftViewQueriesInConsole(IamAction):
    def __init__(self):
        super().__init__('redshift', pattern='ViewQueriesInConsole')


class RekognitionCompareFaces(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='CompareFaces')


class RekognitionCreateCollection(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='CreateCollection')


class RekognitionCreateStreamProcessor(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='CreateStreamProcessor')


class RekognitionDeleteCollection(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DeleteCollection')


class RekognitionDeleteFaces(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DeleteFaces')


class RekognitionDeleteStreamProcessor(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DeleteStreamProcessor')


class RekognitionDescribeStreamProcessor(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DescribeStreamProcessor')


class RekognitionDetectFaces(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DetectFaces')


class RekognitionDetectLabels(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DetectLabels')


class RekognitionDetectModerationLabels(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DetectModerationLabels')


class RekognitionDetectText(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='DetectText')


class RekognitionGetCelebrityInfo(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetCelebrityInfo')


class RekognitionGetCelebrityRecognition(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetCelebrityRecognition')


class RekognitionGetContentModeration(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetContentModeration')


class RekognitionGetFaceDetection(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetFaceDetection')


class RekognitionGetFaceSearch(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetFaceSearch')


class RekognitionGetLabelDetection(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetLabelDetection')


class RekognitionGetPersonTracking(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='GetPersonTracking')


class RekognitionIndexFaces(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='IndexFaces')


class RekognitionListCollections(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='ListCollections')


class RekognitionListFaces(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='ListFaces')


class RekognitionListStreamProcessors(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='ListStreamProcessors')


class RekognitionRecognizeCelebrities(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='RecognizeCelebrities')


class RekognitionSearchFaces(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='SearchFaces')


class RekognitionSearchFacesByImage(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='SearchFacesByImage')


class RekognitionStartCelebrityRecognition(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartCelebrityRecognition')


class RekognitionStartContentModeration(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartContentModeration')


class RekognitionStartFaceDetection(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartFaceDetection')


class RekognitionStartFaceSearch(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartFaceSearch')


class RekognitionStartLabelDetection(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartLabelDetection')


class RekognitionStartPersonTracking(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartPersonTracking')


class RekognitionStartStreamProcessor(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StartStreamProcessor')


class RekognitionStopStreamProcessor(IamAction):
    def __init__(self):
        super().__init__('rekognition', pattern='StopStreamProcessor')


class ResourceGroupsCreateGroup(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='CreateGroup')


class ResourceGroupsDeleteGroup(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='DeleteGroup')


class ResourceGroupsGetGroup(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='GetGroup')


class ResourceGroupsGetGroupQuery(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='GetGroupQuery')


class ResourceGroupsGetTags(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='GetTags')


class ResourceGroupsListGroupResources(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='ListGroupResources')


class ResourceGroupsListGroups(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='ListGroups')


class ResourceGroupsSearchResources(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='SearchResources')


class ResourceGroupsTag(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='Tag')


class ResourceGroupsUntag(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='Untag')


class ResourceGroupsUpdateGroup(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='UpdateGroup')


class ResourceGroupsUpdateGroupQuery(IamAction):
    def __init__(self):
        super().__init__('resource-groups', pattern='UpdateGroupQuery')


class Route53AssociateVPCWithHostedZone(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='AssociateVPCWithHostedZone')


class Route53ChangeResourceRecordSets(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ChangeResourceRecordSets')


class Route53ChangeTagsForResource(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ChangeTagsForResource')


class Route53CreateHealthCheck(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='CreateHealthCheck')


class Route53CreateHostedZone(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='CreateHostedZone')


class Route53CreateReusableDelegationSet(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='CreateReusableDelegationSet')


class Route53CreateTrafficPolicy(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='CreateTrafficPolicy')


class Route53CreateTrafficPolicyInstance(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='CreateTrafficPolicyInstance')


class Route53CreateTrafficPolicyVersion(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='CreateTrafficPolicyVersion')


class Route53DeleteHealthCheck(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DeleteHealthCheck')


class Route53DeleteHostedZone(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DeleteHostedZone')


class Route53DeleteReusableDelegationSet(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DeleteReusableDelegationSet')


class Route53DeleteTrafficPolicy(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DeleteTrafficPolicy')


class Route53DeleteTrafficPolicyInstance(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DeleteTrafficPolicyInstance')


class Route53DisableDomainAutoRenew(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DisableDomainAutoRenew')


class Route53DisassociateVPCFromHostedZone(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='DisassociateVPCFromHostedZone')


class Route53EnableDomainAutoRenew(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='EnableDomainAutoRenew')


class Route53GetChange(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetChange')


class Route53GetCheckerIpRanges(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetCheckerIpRanges')


class Route53GetGeoLocation(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetGeoLocation')


class Route53GetHealthCheck(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetHealthCheck')


class Route53GetHealthCheckCount(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetHealthCheckCount')


class Route53GetHealthCheckLastFailureReason(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetHealthCheckLastFailureReason')


class Route53GetHealthCheckStatus(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetHealthCheckStatus')


class Route53GetHostedZone(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetHostedZone')


class Route53GetHostedZoneCount(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetHostedZoneCount')


class Route53GetReusableDelegationSet(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetReusableDelegationSet')


class Route53GetTrafficPolicy(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetTrafficPolicy')


class Route53GetTrafficPolicyInstance(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetTrafficPolicyInstance')


class Route53GetTrafficPolicyInstanceCount(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='GetTrafficPolicyInstanceCount')


class Route53ListGeoLocations(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListGeoLocations')


class Route53ListHealthChecks(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListHealthChecks')


class Route53ListHostedZones(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListHostedZones')


class Route53ListHostedZonesByName(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListHostedZonesByName')


class Route53ListResourceRecordSets(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListResourceRecordSets')


class Route53ListReusableDelegationSets(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListReusableDelegationSets')


class Route53ListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTagsForResource')


class Route53ListTagsForResources(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTagsForResources')


class Route53ListTrafficPolicies(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTrafficPolicies')


class Route53ListTrafficPolicyInstances(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTrafficPolicyInstances')


class Route53ListTrafficPolicyInstancesByHostedZone(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTrafficPolicyInstancesByHostedZone')


class Route53ListTrafficPolicyInstancesByPolicy(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTrafficPolicyInstancesByPolicy')


class Route53ListTrafficPolicyVersions(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='ListTrafficPolicyVersions')


class Route53TestDNSAnswer(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='TestDNSAnswer')


class Route53UpdateHealthCheck(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='UpdateHealthCheck')


class Route53UpdateHostedZoneComment(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='UpdateHostedZoneComment')


class Route53UpdateTrafficPolicyComment(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='UpdateTrafficPolicyComment')


class Route53UpdateTrafficPolicyInstance(IamAction):
    def __init__(self):
        super().__init__('route53', pattern='UpdateTrafficPolicyInstance')


class Route53DomainsCheckDomainAvailability(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='CheckDomainAvailability')


class Route53DomainsDeleteTagsForDomain(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='DeleteTagsForDomain')


class Route53DomainsDisableDomainAutoRenew(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='DisableDomainAutoRenew')


class Route53DomainsDisableDomainTransferLock(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='DisableDomainTransferLock')


class Route53DomainsEnableDomainAutoRenew(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='EnableDomainAutoRenew')


class Route53DomainsEnableDomainTransferLock(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='EnableDomainTransferLock')


class Route53DomainsGetContactReachabilityStatus(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='GetContactReachabilityStatus')


class Route53DomainsGetDomainDetail(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='GetDomainDetail')


class Route53DomainsGetDomainSuggestions(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='GetDomainSuggestions')


class Route53DomainsGetOperationDetail(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='GetOperationDetail')


class Route53DomainsListDomains(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='ListDomains')


class Route53DomainsListOperations(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='ListOperations')


class Route53DomainsListTagsForDomain(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='ListTagsForDomain')


class Route53DomainsRegisterDomain(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='RegisterDomain')


class Route53DomainsRenewDomain(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='RenewDomain')


class Route53DomainsResendContactReachabilityEmail(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='ResendContactReachabilityEmail')


class Route53DomainsRetrieveDomainAuthCode(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='RetrieveDomainAuthCode')


class Route53DomainsTransferDomain(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='TransferDomain')


class Route53DomainsUpdateDomainContact(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='UpdateDomainContact')


class Route53DomainsUpdateDomainContactPrivacy(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='UpdateDomainContactPrivacy')


class Route53DomainsUpdateDomainNameservers(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='UpdateDomainNameservers')


class Route53DomainsUpdateTagsForDomain(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='UpdateTagsForDomain')


class Route53DomainsViewBilling(IamAction):
    def __init__(self):
        super().__init__('route53domains', pattern='ViewBilling')


class S3AbortMultipartUpload(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='AbortMultipartUpload')


class S3CreateBucket(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='CreateBucket')


class S3DeleteBucket(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteBucket')


class S3DeleteBucketPolicy(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteBucketPolicy')


class S3DeleteBucketWebsite(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteBucketWebsite')


class S3DeleteObject(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteObject')


class S3DeleteObjectTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteObjectTagging')


class S3DeleteObjectVersion(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteObjectVersion')


class S3DeleteObjectVersionTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='DeleteObjectVersionTagging')


class S3GetAccelerateConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetAccelerateConfiguration')


class S3GetAnalyticsConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetAnalyticsConfiguration')


class S3GetBucketAcl(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketAcl')


class S3GetBucketCORS(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketCORS')


class S3GetBucketLocation(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketLocation')


class S3GetBucketLogging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketLogging')


class S3GetBucketNotification(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketNotification')


class S3GetBucketPolicy(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketPolicy')


class S3GetBucketRequestPayment(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketRequestPayment')


class S3GetBucketTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketTagging')


class S3GetBucketVersioning(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketVersioning')


class S3GetBucketWebsite(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetBucketWebsite')


class S3GetInventoryConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetInventoryConfiguration')


class S3GetIpConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetIpConfiguration')


class S3GetLifecycleConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetLifecycleConfiguration')


class S3GetMetricsConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetMetricsConfiguration')


class S3GetObject(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObject')


class S3GetObjectAcl(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectAcl')


class S3GetObjectTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectTagging')


class S3GetObjectTorrent(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectTorrent')


class S3GetObjectVersion(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectVersion')


class S3GetObjectVersionAcl(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectVersionAcl')


class S3GetObjectVersionForReplication(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectVersionForReplication')


class S3GetObjectVersionTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectVersionTagging')


class S3GetObjectVersionTorrent(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetObjectVersionTorrent')


class S3GetReplicationConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='GetReplicationConfiguration')


class S3HeadBucket(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='HeadBucket')


class S3ListAllMyBuckets(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListAllMyBuckets')


class S3ListBucket(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListBucket')


class S3ListBucketByTags(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListBucketByTags')


class S3ListBucketMultipartUploads(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListBucketMultipartUploads')


class S3ListBucketVersions(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListBucketVersions')


class S3ListMultipartUploadParts(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListMultipartUploadParts')


class S3ListObjects(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ListObjects')


class S3ObjectOwnerOverrideToBucketOwner(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ObjectOwnerOverrideToBucketOwner')


class S3PutAccelerateConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutAccelerateConfiguration')


class S3PutAnalyticsConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutAnalyticsConfiguration')


class S3PutBucketAcl(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketAcl')


class S3PutBucketCORS(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketCORS')


class S3PutBucketLogging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketLogging')


class S3PutBucketNotification(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketNotification')


class S3PutBucketPolicy(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketPolicy')


class S3PutBucketRequestPayment(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketRequestPayment')


class S3PutBucketTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketTagging')


class S3PutBucketVersioning(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketVersioning')


class S3PutBucketWebsite(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutBucketWebsite')


class S3PutInventoryConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutInventoryConfiguration')


class S3PutIpConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutIpConfiguration')


class S3PutLifecycleConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutLifecycleConfiguration')


class S3PutMetricsConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutMetricsConfiguration')


class S3PutObject(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutObject')


class S3PutObjectAcl(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutObjectAcl')


class S3PutObjectTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutObjectTagging')


class S3PutObjectVersionAcl(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutObjectVersionAcl')


class S3PutObjectVersionTagging(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutObjectVersionTagging')


class S3PutReplicationConfiguration(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='PutReplicationConfiguration')


class S3ReplicateDelete(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ReplicateDelete')


class S3ReplicateObject(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ReplicateObject')


class S3ReplicateTags(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='ReplicateTags')


class S3RestoreObject(IamAction):
    def __init__(self):
        super().__init__('s3', pattern='RestoreObject')


class SagemakerAddTags(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='AddTags')


class SagemakerCreateEndpoint(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='CreateEndpoint')


class SagemakerCreateEndpointConfig(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='CreateEndpointConfig')


class SagemakerCreateModel(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='CreateModel')


class SagemakerCreateNotebookInstance(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='CreateNotebookInstance')


class SagemakerCreatePresignedNotebookInstanceUrl(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='CreatePresignedNotebookInstanceUrl')


class SagemakerCreateTrainingJob(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='CreateTrainingJob')


class SagemakerDeleteEndpoint(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DeleteEndpoint')


class SagemakerDeleteEndpointConfig(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DeleteEndpointConfig')


class SagemakerDeleteModel(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DeleteModel')


class SagemakerDeleteNotebookInstance(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DeleteNotebookInstance')


class SagemakerDeleteTags(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DeleteTags')


class SagemakerDescribeEndpoint(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DescribeEndpoint')


class SagemakerDescribeEndpointConfig(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DescribeEndpointConfig')


class SagemakerDescribeModel(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DescribeModel')


class SagemakerDescribeNotebookInstance(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DescribeNotebookInstance')


class SagemakerDescribeTrainingJob(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='DescribeTrainingJob')


class SagemakerInvokeEndpoint(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='InvokeEndpoint')


class SagemakerListEndpointConfigs(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='ListEndpointConfigs')


class SagemakerListEndpoints(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='ListEndpoints')


class SagemakerListModels(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='ListModels')


class SagemakerListNotebookInstances(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='ListNotebookInstances')


class SagemakerListTags(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='ListTags')


class SagemakerListTrainingJobs(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='ListTrainingJobs')


class SagemakerStartNotebookInstance(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='StartNotebookInstance')


class SagemakerStopNotebookInstance(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='StopNotebookInstance')


class SagemakerStopTrainingJob(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='StopTrainingJob')


class SagemakerUpdateEndpoint(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='UpdateEndpoint')


class SagemakerUpdateEndpointWeightsAndCapacities(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='UpdateEndpointWeightsAndCapacities')


class SagemakerUpdateNotebookInstance(IamAction):
    def __init__(self):
        super().__init__('sagemaker', pattern='UpdateNotebookInstance')


class SdbBatchDeleteAttributes(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='BatchDeleteAttributes')


class SdbBatchPutAttributes(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='BatchPutAttributes')


class SdbCreateDomain(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='CreateDomain')


class SdbDeleteAttributes(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='DeleteAttributes')


class SdbDeleteDomain(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='DeleteDomain')


class SdbDomainMetadata(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='DomainMetadata')


class SdbGetAttributes(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='GetAttributes')


class SdbListDomains(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='ListDomains')


class SdbPutAttributes(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='PutAttributes')


class SdbSelect(IamAction):
    def __init__(self):
        super().__init__('sdb', pattern='Select')


class ServerlessrepoCreateApplication(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='CreateApplication')


class ServerlessrepoCreateApplicationVersion(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='CreateApplicationVersion')


class ServerlessrepoCreateCloudFormationChangeSet(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='CreateCloudFormationChangeSet')


class ServerlessrepoDeleteApplication(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='DeleteApplication')


class ServerlessrepoGetApplication(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='GetApplication')


class ServerlessrepoGetApplicationPolicy(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='GetApplicationPolicy')


class ServerlessrepoListApplicationVersions(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='ListApplicationVersions')


class ServerlessrepoListApplications(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='ListApplications')


class ServerlessrepoPutApplicationPolicy(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='PutApplicationPolicy')


class ServerlessrepoSearchApplications(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='SearchApplications')


class ServerlessrepoUpdateApplication(IamAction):
    def __init__(self):
        super().__init__('serverlessrepo', pattern='UpdateApplication')


class ServicecatalogAcceptPortfolioShare(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='AcceptPortfolioShare')


class ServicecatalogAssociatePrincipalWithPortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='AssociatePrincipalWithPortfolio')


class ServicecatalogAssociateProductWithPortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='AssociateProductWithPortfolio')


class ServicecatalogCreateConstraint(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='CreateConstraint')


class ServicecatalogCreatePortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='CreatePortfolio')


class ServicecatalogCreatePortfolioShare(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='CreatePortfolioShare')


class ServicecatalogCreateProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='CreateProduct')


class ServicecatalogCreateProvisioningArtifact(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='CreateProvisioningArtifact')


class ServicecatalogDeleteConstraint(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DeleteConstraint')


class ServicecatalogDeletePortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DeletePortfolio')


class ServicecatalogDeletePortfolioShare(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DeletePortfolioShare')


class ServicecatalogDeleteProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DeleteProduct')


class ServicecatalogDeleteProvisioningArtifact(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DeleteProvisioningArtifact')


class ServicecatalogDescribeConstraint(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeConstraint')


class ServicecatalogDescribePortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribePortfolio')


class ServicecatalogDescribeProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeProduct')


class ServicecatalogDescribeProductAsAdmin(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeProductAsAdmin')


class ServicecatalogDescribeProductView(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeProductView')


class ServicecatalogDescribeProvisioningArtifact(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeProvisioningArtifact')


class ServicecatalogDescribeProvisioningParameters(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeProvisioningParameters')


class ServicecatalogDescribeRecord(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DescribeRecord')


class ServicecatalogDisassociatePrincipalFromPortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DisassociatePrincipalFromPortfolio')


class ServicecatalogDisassociateProductFromPortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='DisassociateProductFromPortfolio')


class ServicecatalogListAcceptedPortfolioShares(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListAcceptedPortfolioShares')


class ServicecatalogListConstraintsForPortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListConstraintsForPortfolio')


class ServicecatalogListLaunchPaths(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListLaunchPaths')


class ServicecatalogListPortfolioAccess(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListPortfolioAccess')


class ServicecatalogListPortfolios(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListPortfolios')


class ServicecatalogListPortfoliosForProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListPortfoliosForProduct')


class ServicecatalogListPrincipalsForPortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListPrincipalsForPortfolio')


class ServicecatalogListProvisioningArtifacts(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListProvisioningArtifacts')


class ServicecatalogListRecordHistory(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ListRecordHistory')


class ServicecatalogProvisionProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ProvisionProduct')


class ServicecatalogRejectPortfolioShare(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='RejectPortfolioShare')


class ServicecatalogScanProvisionedProducts(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='ScanProvisionedProducts')


class ServicecatalogSearchProducts(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='SearchProducts')


class ServicecatalogSearchProductsAsAdmin(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='SearchProductsAsAdmin')


class ServicecatalogTerminateProvisionedProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='TerminateProvisionedProduct')


class ServicecatalogUpdateConstraint(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='UpdateConstraint')


class ServicecatalogUpdatePortfolio(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='UpdatePortfolio')


class ServicecatalogUpdateProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='UpdateProduct')


class ServicecatalogUpdateProvisionedProduct(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='UpdateProvisionedProduct')


class ServicecatalogUpdateProvisioningArtifact(IamAction):
    def __init__(self):
        super().__init__('servicecatalog', pattern='UpdateProvisioningArtifact')


class ServicediscoveryCreatePrivateDnsNamespace(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='CreatePrivateDnsNamespace')


class ServicediscoveryCreatePublicDnsNamespace(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='CreatePublicDnsNamespace')


class ServicediscoveryCreateService(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='CreateService')


class ServicediscoveryDeleteNamespace(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='DeleteNamespace')


class ServicediscoveryDeleteService(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='DeleteService')


class ServicediscoveryDeregisterInstance(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='DeregisterInstance')


class ServicediscoveryGetInstance(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='GetInstance')


class ServicediscoveryGetInstancesHealthStatus(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='GetInstancesHealthStatus')


class ServicediscoveryGetNamespace(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='GetNamespace')


class ServicediscoveryGetOperation(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='GetOperation')


class ServicediscoveryGetService(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='GetService')


class ServicediscoveryListInstances(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='ListInstances')


class ServicediscoveryListNamespaces(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='ListNamespaces')


class ServicediscoveryListOperations(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='ListOperations')


class ServicediscoveryListServices(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='ListServices')


class ServicediscoveryRegisterInstance(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='RegisterInstance')


class ServicediscoveryUpdateInstanceHeartbeatStatus(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='UpdateInstanceHeartbeatStatus')


class ServicediscoveryUpdateService(IamAction):
    def __init__(self):
        super().__init__('servicediscovery', pattern='UpdateService')


class SesCloneReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CloneReceiptRuleSet')


class SesCreateConfigurationSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateConfigurationSet')


class SesCreateConfigurationSetEventDestination(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateConfigurationSetEventDestination')


class SesCreateConfigurationSetTrackingOptions(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateConfigurationSetTrackingOptions')


class SesCreateCustomVerificationEmailTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateCustomVerificationEmailTemplate')


class SesCreateReceiptFilter(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateReceiptFilter')


class SesCreateReceiptRule(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateReceiptRule')


class SesCreateReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateReceiptRuleSet')


class SesCreateTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='CreateTemplate')


class SesDeleteConfigurationSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteConfigurationSet')


class SesDeleteConfigurationSetEventDestination(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteConfigurationSetEventDestination')


class SesDeleteConfigurationSetTrackingOptions(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteConfigurationSetTrackingOptions')


class SesDeleteCustomVerificationEmailTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteCustomVerificationEmailTemplate')


class SesDeleteIdentity(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteIdentity')


class SesDeleteIdentityPolicy(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteIdentityPolicy')


class SesDeleteReceiptFilter(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteReceiptFilter')


class SesDeleteReceiptRule(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteReceiptRule')


class SesDeleteReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteReceiptRuleSet')


class SesDeleteTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteTemplate')


class SesDeleteVerifiedEmailAddress(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DeleteVerifiedEmailAddress')


class SesDescribeActiveReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DescribeActiveReceiptRuleSet')


class SesDescribeConfigurationSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DescribeConfigurationSet')


class SesDescribeReceiptRule(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DescribeReceiptRule')


class SesDescribeReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='DescribeReceiptRuleSet')


class SesGetAccountSendingEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetAccountSendingEnabled')


class SesGetCustomVerificationEmailTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetCustomVerificationEmailTemplate')


class SesGetIdentityDkimAttributes(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetIdentityDkimAttributes')


class SesGetIdentityMailFromDomainAttributes(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetIdentityMailFromDomainAttributes')


class SesGetIdentityNotificationAttributes(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetIdentityNotificationAttributes')


class SesGetIdentityPolicies(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetIdentityPolicies')


class SesGetIdentityVerificationAttributes(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetIdentityVerificationAttributes')


class SesGetSendQuota(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetSendQuota')


class SesGetSendStatistics(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetSendStatistics')


class SesGetTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='GetTemplate')


class SesListConfigurationSets(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListConfigurationSets')


class SesListCustomVerificationEmailTemplates(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListCustomVerificationEmailTemplates')


class SesListIdentities(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListIdentities')


class SesListIdentityPolicies(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListIdentityPolicies')


class SesListReceiptFilters(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListReceiptFilters')


class SesListReceiptRuleSets(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListReceiptRuleSets')


class SesListTemplates(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListTemplates')


class SesListVerifiedEmailAddresses(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ListVerifiedEmailAddresses')


class SesPutIdentityPolicy(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='PutIdentityPolicy')


class SesReorderReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='ReorderReceiptRuleSet')


class SesSendBounce(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SendBounce')


class SesSendBulkTemplatedEmail(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SendBulkTemplatedEmail')


class SesSendCustomVerificationEmail(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SendCustomVerificationEmail')


class SesSendEmail(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SendEmail')


class SesSendRawEmail(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SendRawEmail')


class SesSendTemplatedEmail(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SendTemplatedEmail')


class SesSetActiveReceiptRuleSet(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetActiveReceiptRuleSet')


class SesSetIdentityDkimEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetIdentityDkimEnabled')


class SesSetIdentityFeedbackForwardingEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetIdentityFeedbackForwardingEnabled')


class SesSetIdentityHeadersInNotificationsEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetIdentityHeadersInNotificationsEnabled')


class SesSetIdentityMailFromDomain(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetIdentityMailFromDomain')


class SesSetIdentityNotificationTopic(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetIdentityNotificationTopic')


class SesSetReceiptRulePosition(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='SetReceiptRulePosition')


class SesTestRenderTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='TestRenderTemplate')


class SesUpdateAccountSendingEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateAccountSendingEnabled')


class SesUpdateConfigurationSetEventDestination(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateConfigurationSetEventDestination')


class SesUpdateConfigurationSetReputationMetricsEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateConfigurationSetReputationMetricsEnabled')


class SesUpdateConfigurationSetSendingEnabled(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateConfigurationSetSendingEnabled')


class SesUpdateConfigurationSetTrackingOptions(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateConfigurationSetTrackingOptions')


class SesUpdateCustomVerificationEmailTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateCustomVerificationEmailTemplate')


class SesUpdateReceiptRule(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateReceiptRule')


class SesUpdateTemplate(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='UpdateTemplate')


class SesVerifyDomainDkim(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='VerifyDomainDkim')


class SesVerifyDomainIdentity(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='VerifyDomainIdentity')


class SesVerifyEmailAddress(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='VerifyEmailAddress')


class SesVerifyEmailIdentity(IamAction):
    def __init__(self):
        super().__init__('ses', pattern='VerifyEmailIdentity')


class ShieldCreateProtection(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='CreateProtection')


class ShieldCreateSubscription(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='CreateSubscription')


class ShieldDeleteProtection(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='DeleteProtection')


class ShieldDeleteSubscription(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='DeleteSubscription')


class ShieldDescribeAttack(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='DescribeAttack')


class ShieldDescribeProtection(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='DescribeProtection')


class ShieldDescribeSubscription(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='DescribeSubscription')


class ShieldListAttacks(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='ListAttacks')


class ShieldListProtections(IamAction):
    def __init__(self):
        super().__init__('shield', pattern='ListProtections')


class SignerDescribeSigningJob(IamAction):
    def __init__(self):
        super().__init__('signer', pattern='DescribeSigningJob')


class SignerListSigningJobs(IamAction):
    def __init__(self):
        super().__init__('signer', pattern='ListSigningJobs')


class SignerStartSigningJob(IamAction):
    def __init__(self):
        super().__init__('signer', pattern='StartSigningJob')


class SnowballCancelCluster(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='CancelCluster')


class SnowballCancelJob(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='CancelJob')


class SnowballCreateAddress(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='CreateAddress')


class SnowballCreateCluster(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='CreateCluster')


class SnowballCreateJob(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='CreateJob')


class SnowballDescribeAddress(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='DescribeAddress')


class SnowballDescribeAddresses(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='DescribeAddresses')


class SnowballDescribeCluster(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='DescribeCluster')


class SnowballDescribeJob(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='DescribeJob')


class SnowballGetJobManifest(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='GetJobManifest')


class SnowballGetJobUnlockCode(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='GetJobUnlockCode')


class SnowballGetSnowballUsage(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='GetSnowballUsage')


class SnowballListClusterJobs(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='ListClusterJobs')


class SnowballListClusters(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='ListClusters')


class SnowballListJobs(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='ListJobs')


class SnowballUpdateCluster(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='UpdateCluster')


class SnowballUpdateJob(IamAction):
    def __init__(self):
        super().__init__('snowball', pattern='UpdateJob')


class SnsAddPermission(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='AddPermission')


class SnsCheckIfPhoneNumberIsOptedOut(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='CheckIfPhoneNumberIsOptedOut')


class SnsConfirmSubscription(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ConfirmSubscription')


class SnsCreatePlatformApplication(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='CreatePlatformApplication')


class SnsCreatePlatformEndpoint(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='CreatePlatformEndpoint')


class SnsCreateTopic(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='CreateTopic')


class SnsDeleteEndpoint(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='DeleteEndpoint')


class SnsDeletePlatformApplication(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='DeletePlatformApplication')


class SnsDeleteTopic(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='DeleteTopic')


class SnsGetEndpointAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='GetEndpointAttributes')


class SnsGetPlatformApplicationAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='GetPlatformApplicationAttributes')


class SnsGetSMSAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='GetSMSAttributes')


class SnsGetSubscriptionAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='GetSubscriptionAttributes')


class SnsGetTopicAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='GetTopicAttributes')


class SnsListEndpointsByPlatformApplication(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ListEndpointsByPlatformApplication')


class SnsListPhoneNumbersOptedOut(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ListPhoneNumbersOptedOut')


class SnsListPlatformApplications(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ListPlatformApplications')


class SnsListSubscriptions(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ListSubscriptions')


class SnsListSubscriptionsByTopic(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ListSubscriptionsByTopic')


class SnsListTopics(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='ListTopics')


class SnsOptInPhoneNumber(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='OptInPhoneNumber')


class SnsPublish(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='Publish')


class SnsRemovePermission(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='RemovePermission')


class SnsSetEndpointAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='SetEndpointAttributes')


class SnsSetPlatformApplicationAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='SetPlatformApplicationAttributes')


class SnsSetSMSAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='SetSMSAttributes')


class SnsSetSubscriptionAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='SetSubscriptionAttributes')


class SnsSetTopicAttributes(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='SetTopicAttributes')


class SnsSubscribe(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='Subscribe')


class SnsUnsubscribe(IamAction):
    def __init__(self):
        super().__init__('sns', pattern='Unsubscribe')


class SqsAddPermission(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='AddPermission')


class SqsChangeMessageVisibility(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='ChangeMessageVisibility')


class SqsChangeMessageVisibilityBatch(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='ChangeMessageVisibilityBatch')


class SqsCreateQueue(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='CreateQueue')


class SqsDeleteMessage(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='DeleteMessage')


class SqsDeleteMessageBatch(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='DeleteMessageBatch')


class SqsDeleteQueue(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='DeleteQueue')


class SqsGetQueueAttributes(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='GetQueueAttributes')


class SqsGetQueueUrl(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='GetQueueUrl')


class SqsListDeadLetterSourceQueues(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='ListDeadLetterSourceQueues')


class SqsListQueueTags(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='ListQueueTags')


class SqsListQueues(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='ListQueues')


class SqsPurgeQueue(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='PurgeQueue')


class SqsReceiveMessage(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='ReceiveMessage')


class SqsRemovePermission(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='RemovePermission')


class SqsSendMessage(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='SendMessage')


class SqsSendMessageBatch(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='SendMessageBatch')


class SqsSetQueueAttributes(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='SetQueueAttributes')


class SqsTagQueue(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='TagQueue')


class SqsUntagQueue(IamAction):
    def __init__(self):
        super().__init__('sqs', pattern='UntagQueue')


class SsmAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='AddTagsToResource')


class SsmCancelCommand(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CancelCommand')


class SsmCreateActivation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreateActivation')


class SsmCreateAssociation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreateAssociation')


class SsmCreateAssociationBatch(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreateAssociationBatch')


class SsmCreateDocument(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreateDocument')


class SsmCreateMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreateMaintenanceWindow')


class SsmCreatePatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreatePatchBaseline')


class SsmCreateResourceDataSync(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='CreateResourceDataSync')


class SsmDeleteActivation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteActivation')


class SsmDeleteAssociation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteAssociation')


class SsmDeleteDocument(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteDocument')


class SsmDeleteMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteMaintenanceWindow')


class SsmDeleteParameter(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteParameter')


class SsmDeleteParameters(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteParameters')


class SsmDeletePatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeletePatchBaseline')


class SsmDeleteResourceDataSync(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeleteResourceDataSync')


class SsmDeregisterManagedInstance(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeregisterManagedInstance')


class SsmDeregisterPatchBaselineForPatchGroup(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeregisterPatchBaselineForPatchGroup')


class SsmDeregisterTargetFromMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeregisterTargetFromMaintenanceWindow')


class SsmDeregisterTaskFromMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DeregisterTaskFromMaintenanceWindow')


class SsmDescribeActivations(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeActivations')


class SsmDescribeAssociation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeAssociation')


class SsmDescribeAutomationExecutions(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeAutomationExecutions')


class SsmDescribeAutomationStepExecutions(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeAutomationStepExecutions')


class SsmDescribeAvailablePatches(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeAvailablePatches')


class SsmDescribeDocument(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeDocument')


class SsmDescribeDocumentParameters(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeDocumentParameters')


class SsmDescribeDocumentPermission(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeDocumentPermission')


class SsmDescribeEffectiveInstanceAssociations(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeEffectiveInstanceAssociations')


class SsmDescribeEffectivePatchesForPatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeEffectivePatchesForPatchBaseline')


class SsmDescribeInstanceAssociationsStatus(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeInstanceAssociationsStatus')


class SsmDescribeInstanceInformation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeInstanceInformation')


class SsmDescribeInstancePatchStates(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeInstancePatchStates')


class SsmDescribeInstancePatchStatesForPatchGroup(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeInstancePatchStatesForPatchGroup')


class SsmDescribeInstancePatches(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeInstancePatches')


class SsmDescribeInstanceProperties(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeInstanceProperties')


class SsmDescribeMaintenanceWindowExecutionTaskInvocations(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeMaintenanceWindowExecutionTaskInvocations')


class SsmDescribeMaintenanceWindowExecutionTasks(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeMaintenanceWindowExecutionTasks')


class SsmDescribeMaintenanceWindowExecutions(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeMaintenanceWindowExecutions')


class SsmDescribeMaintenanceWindowTargets(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeMaintenanceWindowTargets')


class SsmDescribeMaintenanceWindowTasks(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeMaintenanceWindowTasks')


class SsmDescribeMaintenanceWindows(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeMaintenanceWindows')


class SsmDescribeParameters(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribeParameters')


class SsmDescribePatchBaselines(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribePatchBaselines')


class SsmDescribePatchGroupState(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribePatchGroupState')


class SsmDescribePatchGroups(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='DescribePatchGroups')


class SsmGetAutomationExecution(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetAutomationExecution')


class SsmGetCommandInvocation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetCommandInvocation')


class SsmGetDefaultPatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetDefaultPatchBaseline')


class SsmGetDeployablePatchSnapshotForInstance(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetDeployablePatchSnapshotForInstance')


class SsmGetDocument(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetDocument')


class SsmGetInventory(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetInventory')


class SsmGetInventorySchema(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetInventorySchema')


class SsmGetMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetMaintenanceWindow')


class SsmGetMaintenanceWindowExecution(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetMaintenanceWindowExecution')


class SsmGetMaintenanceWindowExecutionTask(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetMaintenanceWindowExecutionTask')


class SsmGetMaintenanceWindowExecutionTaskInvocation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetMaintenanceWindowExecutionTaskInvocation')


class SsmGetMaintenanceWindowTask(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetMaintenanceWindowTask')


class SsmGetManifest(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetManifest')


class SsmGetParameter(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetParameter')


class SsmGetParameterHistory(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetParameterHistory')


class SsmGetParameters(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetParameters')


class SsmGetParametersByPath(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetParametersByPath')


class SsmGetPatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetPatchBaseline')


class SsmGetPatchBaselineForPatchGroup(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='GetPatchBaselineForPatchGroup')


class SsmListAssociationVersions(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListAssociationVersions')


class SsmListAssociations(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListAssociations')


class SsmListCommandInvocations(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListCommandInvocations')


class SsmListCommands(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListCommands')


class SsmListDocumentVersions(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListDocumentVersions')


class SsmListDocuments(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListDocuments')


class SsmListInstanceAssociations(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListInstanceAssociations')


class SsmListInventoryEntries(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListInventoryEntries')


class SsmListResourceDataSync(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListResourceDataSync')


class SsmListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ListTagsForResource')


class SsmModifyDocumentPermission(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='ModifyDocumentPermission')


class SsmPutComplianceItems(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='PutComplianceItems')


class SsmPutConfigurePackageResult(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='PutConfigurePackageResult')


class SsmPutInventory(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='PutInventory')


class SsmPutParameter(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='PutParameter')


class SsmRegisterDefaultPatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='RegisterDefaultPatchBaseline')


class SsmRegisterPatchBaselineForPatchGroup(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='RegisterPatchBaselineForPatchGroup')


class SsmRegisterTargetWithMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='RegisterTargetWithMaintenanceWindow')


class SsmRegisterTaskWithMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='RegisterTaskWithMaintenanceWindow')


class SsmRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='RemoveTagsFromResource')


class SsmSendAutomationSignal(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='SendAutomationSignal')


class SsmSendCommand(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='SendCommand')


class SsmStartAssociationsOnce(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='StartAssociationsOnce')


class SsmStartAutomationExecution(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='StartAutomationExecution')


class SsmStopAutomationExecution(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='StopAutomationExecution')


class SsmUpdateAssociation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateAssociation')


class SsmUpdateAssociationStatus(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateAssociationStatus')


class SsmUpdateDocument(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateDocument')


class SsmUpdateDocumentDefaultVersion(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateDocumentDefaultVersion')


class SsmUpdateInstanceAssociationStatus(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateInstanceAssociationStatus')


class SsmUpdateInstanceInformation(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateInstanceInformation')


class SsmUpdateMaintenanceWindow(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateMaintenanceWindow')


class SsmUpdateMaintenanceWindowTarget(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateMaintenanceWindowTarget')


class SsmUpdateMaintenanceWindowTask(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateMaintenanceWindowTask')


class SsmUpdateManagedInstanceRole(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdateManagedInstanceRole')


class SsmUpdatePatchBaseline(IamAction):
    def __init__(self):
        super().__init__('ssm', pattern='UpdatePatchBaseline')


class SsoAssociateDirectory(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='AssociateDirectory')


class SsoAssociateProfile(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='AssociateProfile')


class SsoCreateApplicationInstance(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='CreateApplicationInstance')


class SsoCreateApplicationInstanceCertificate(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='CreateApplicationInstanceCertificate')


class SsoCreatePermissionSet(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='CreatePermissionSet')


class SsoCreateProfile(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='CreateProfile')


class SsoCreateTrust(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='CreateTrust')


class SsoDeleteApplicationInstance(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DeleteApplicationInstance')


class SsoDeleteApplicationInstanceCertificate(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DeleteApplicationInstanceCertificate')


class SsoDeletePermissionSet(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DeletePermissionSet')


class SsoDeletePermissionsPolicy(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DeletePermissionsPolicy')


class SsoDeleteProfile(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DeleteProfile')


class SsoDescribePermissionsPolicies(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DescribePermissionsPolicies')


class SsoDisassociateDirectory(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DisassociateDirectory')


class SsoDisassociateProfile(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='DisassociateProfile')


class SsoGetApplicationInstance(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='GetApplicationInstance')


class SsoGetApplicationTemplate(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='GetApplicationTemplate')


class SsoGetPermissionSet(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='GetPermissionSet')


class SsoGetProfile(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='GetProfile')


class SsoGetSSOStatus(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='GetSSOStatus')


class SsoGetTrust(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='GetTrust')


class SsoImportApplicationInstanceServiceProviderMetadata(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ImportApplicationInstanceServiceProviderMetadata')


class SsoListApplicationInstanceCertificates(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListApplicationInstanceCertificates')


class SsoListApplicationInstances(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListApplicationInstances')


class SsoListApplicationTemplates(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListApplicationTemplates')


class SsoListDirectoryAssociations(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListDirectoryAssociations')


class SsoListPermissionSets(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListPermissionSets')


class SsoListProfileAssociations(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListProfileAssociations')


class SsoListProfiles(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='ListProfiles')


class SsoPutPermissionsPolicy(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='PutPermissionsPolicy')


class SsoStartSSO(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='StartSSO')


class SsoUpdateApplicationInstanceActiveCertificate(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceActiveCertificate')


class SsoUpdateApplicationInstanceDisplayData(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceDisplayData')


class SsoUpdateApplicationInstanceResponseConfiguration(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceResponseConfiguration')


class SsoUpdateApplicationInstanceResponseSchemaConfiguration(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceResponseSchemaConfiguration')


class SsoUpdateApplicationInstanceSecurityConfiguration(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceSecurityConfiguration')


class SsoUpdateApplicationInstanceServiceProviderConfiguration(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceServiceProviderConfiguration')


class SsoUpdateApplicationInstanceStatus(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateApplicationInstanceStatus')


class SsoUpdateDirectoryAssociation(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateDirectoryAssociation')


class SsoUpdateProfile(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateProfile')


class SsoUpdateTrust(IamAction):
    def __init__(self):
        super().__init__('sso', pattern='UpdateTrust')


class StatesCreateActivity(IamAction):
    def __init__(self):
        super().__init__('states', pattern='CreateActivity')


class StatesCreateStateMachine(IamAction):
    def __init__(self):
        super().__init__('states', pattern='CreateStateMachine')


class StatesDeleteActivity(IamAction):
    def __init__(self):
        super().__init__('states', pattern='DeleteActivity')


class StatesDeleteStateMachine(IamAction):
    def __init__(self):
        super().__init__('states', pattern='DeleteStateMachine')


class StatesDescribeActivity(IamAction):
    def __init__(self):
        super().__init__('states', pattern='DescribeActivity')


class StatesDescribeExecution(IamAction):
    def __init__(self):
        super().__init__('states', pattern='DescribeExecution')


class StatesDescribeStateMachine(IamAction):
    def __init__(self):
        super().__init__('states', pattern='DescribeStateMachine')


class StatesDescribeStateMachineForExecution(IamAction):
    def __init__(self):
        super().__init__('states', pattern='DescribeStateMachineForExecution')


class StatesGetActivityTask(IamAction):
    def __init__(self):
        super().__init__('states', pattern='GetActivityTask')


class StatesGetExecutionHistory(IamAction):
    def __init__(self):
        super().__init__('states', pattern='GetExecutionHistory')


class StatesListActivities(IamAction):
    def __init__(self):
        super().__init__('states', pattern='ListActivities')


class StatesListExecutions(IamAction):
    def __init__(self):
        super().__init__('states', pattern='ListExecutions')


class StatesListStateMachines(IamAction):
    def __init__(self):
        super().__init__('states', pattern='ListStateMachines')


class StatesSendTaskFailure(IamAction):
    def __init__(self):
        super().__init__('states', pattern='SendTaskFailure')


class StatesSendTaskHeartbeat(IamAction):
    def __init__(self):
        super().__init__('states', pattern='SendTaskHeartbeat')


class StatesSendTaskSuccess(IamAction):
    def __init__(self):
        super().__init__('states', pattern='SendTaskSuccess')


class StatesStartExecution(IamAction):
    def __init__(self):
        super().__init__('states', pattern='StartExecution')


class StatesStopExecution(IamAction):
    def __init__(self):
        super().__init__('states', pattern='StopExecution')


class StatesUpdateStateMachine(IamAction):
    def __init__(self):
        super().__init__('states', pattern='UpdateStateMachine')


class StoragegatewayActivateGateway(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ActivateGateway')


class StoragegatewayAddCache(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='AddCache')


class StoragegatewayAddTagsToResource(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='AddTagsToResource')


class StoragegatewayAddUploadBuffer(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='AddUploadBuffer')


class StoragegatewayAddWorkingStorage(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='AddWorkingStorage')


class StoragegatewayCancelArchival(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CancelArchival')


class StoragegatewayCancelRetrieval(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CancelRetrieval')


class StoragegatewayCreateCachediSCSIVolume(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateCachediSCSIVolume')


class StoragegatewayCreateNFSFileShare(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateNFSFileShare')


class StoragegatewayCreateSnapshot(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateSnapshot')


class StoragegatewayCreateSnapshotFromVolumeRecoveryPoint(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateSnapshotFromVolumeRecoveryPoint')


class StoragegatewayCreateStorediSCSIVolume(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateStorediSCSIVolume')


class StoragegatewayCreateTapeWithBarcode(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateTapeWithBarcode')


class StoragegatewayCreateTapes(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='CreateTapes')


class StoragegatewayDeleteBandwidthRateLimit(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteBandwidthRateLimit')


class StoragegatewayDeleteChapCredentials(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteChapCredentials')


class StoragegatewayDeleteFileShare(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteFileShare')


class StoragegatewayDeleteGateway(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteGateway')


class StoragegatewayDeleteSnapshotSchedule(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteSnapshotSchedule')


class StoragegatewayDeleteTape(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteTape')


class StoragegatewayDeleteTapeArchive(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteTapeArchive')


class StoragegatewayDeleteVolume(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DeleteVolume')


class StoragegatewayDescribeBandwidthRateLimit(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeBandwidthRateLimit')


class StoragegatewayDescribeCache(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeCache')


class StoragegatewayDescribeCachediSCSIVolumes(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeCachediSCSIVolumes')


class StoragegatewayDescribeChapCredentials(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeChapCredentials')


class StoragegatewayDescribeGatewayInformation(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeGatewayInformation')


class StoragegatewayDescribeMaintenanceStartTime(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeMaintenanceStartTime')


class StoragegatewayDescribeNFSFileShares(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeNFSFileShares')


class StoragegatewayDescribeSnapshotSchedule(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeSnapshotSchedule')


class StoragegatewayDescribeStorediSCSIVolumes(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeStorediSCSIVolumes')


class StoragegatewayDescribeTapeArchives(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeTapeArchives')


class StoragegatewayDescribeTapeRecoveryPoints(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeTapeRecoveryPoints')


class StoragegatewayDescribeTapes(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeTapes')


class StoragegatewayDescribeUploadBuffer(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeUploadBuffer')


class StoragegatewayDescribeVTLDevices(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeVTLDevices')


class StoragegatewayDescribeWorkingStorage(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DescribeWorkingStorage')


class StoragegatewayDisableGateway(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='DisableGateway')


class StoragegatewayListFileShares(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListFileShares')


class StoragegatewayListGateways(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListGateways')


class StoragegatewayListLocalDisks(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListLocalDisks')


class StoragegatewayListTagsForResource(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListTagsForResource')


class StoragegatewayListTapes(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListTapes')


class StoragegatewayListVolumeInitiators(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListVolumeInitiators')


class StoragegatewayListVolumeRecoveryPoints(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListVolumeRecoveryPoints')


class StoragegatewayListVolumes(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ListVolumes')


class StoragegatewayRefreshCache(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='RefreshCache')


class StoragegatewayRemoveTagsFromResource(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='RemoveTagsFromResource')


class StoragegatewayResetCache(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ResetCache')


class StoragegatewayRetrieveTapeArchive(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='RetrieveTapeArchive')


class StoragegatewayRetrieveTapeRecoveryPoint(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='RetrieveTapeRecoveryPoint')


class StoragegatewaySetLocalConsolePassword(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='SetLocalConsolePassword')


class StoragegatewayShutdownGateway(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='ShutdownGateway')


class StoragegatewayStartGateway(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='StartGateway')


class StoragegatewayUpdateBandwidthRateLimit(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateBandwidthRateLimit')


class StoragegatewayUpdateChapCredentials(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateChapCredentials')


class StoragegatewayUpdateGatewayInformation(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateGatewayInformation')


class StoragegatewayUpdateGatewaySoftwareNow(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateGatewaySoftwareNow')


class StoragegatewayUpdateMaintenanceStartTime(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateMaintenanceStartTime')


class StoragegatewayUpdateNFSFileShare(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateNFSFileShare')


class StoragegatewayUpdateSnapshotSchedule(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateSnapshotSchedule')


class StoragegatewayUpdateVTLDeviceType(IamAction):
    def __init__(self):
        super().__init__('storagegateway', pattern='UpdateVTLDeviceType')


class StsAssumeRole(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='AssumeRole')


class StsAssumeRoleWithSAML(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='AssumeRoleWithSAML')


class StsAssumeRoleWithWebIdentity(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='AssumeRoleWithWebIdentity')


class StsDecodeAuthorizationMessage(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='DecodeAuthorizationMessage')


class StsGetCallerIdentity(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='GetCallerIdentity')


class StsGetFederationToken(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='GetFederationToken')


class StsGetSessionToken(IamAction):
    def __init__(self):
        super().__init__('sts', pattern='GetSessionToken')


class SupportAddAttachmentsToSet(IamAction):
    def __init__(self):
        super().__init__('support', pattern='AddAttachmentsToSet')


class SupportAddCommunicationToCase(IamAction):
    def __init__(self):
        super().__init__('support', pattern='AddCommunicationToCase')


class SupportCreateCase(IamAction):
    def __init__(self):
        super().__init__('support', pattern='CreateCase')


class SupportDescribeAttachment(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeAttachment')


class SupportDescribeCases(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeCases')


class SupportDescribeCommunications(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeCommunications')


class SupportDescribeServices(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeServices')


class SupportDescribeSeverityLevels(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeSeverityLevels')


class SupportDescribeTrustedAdvisorCheckRefreshStatuses(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeTrustedAdvisorCheckRefreshStatuses')


class SupportDescribeTrustedAdvisorCheckResult(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeTrustedAdvisorCheckResult')


class SupportDescribeTrustedAdvisorCheckSummaries(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeTrustedAdvisorCheckSummaries')


class SupportDescribeTrustedAdvisorChecks(IamAction):
    def __init__(self):
        super().__init__('support', pattern='DescribeTrustedAdvisorChecks')


class SupportRefreshTrustedAdvisorCheck(IamAction):
    def __init__(self):
        super().__init__('support', pattern='RefreshTrustedAdvisorCheck')


class SupportResolveCase(IamAction):
    def __init__(self):
        super().__init__('support', pattern='ResolveCase')


class SwfCancelTimer(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CancelTimer')


class SwfCancelWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CancelWorkflowExecution')


class SwfCompleteWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CompleteWorkflowExecution')


class SwfContinueAsNewWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ContinueAsNewWorkflowExecution')


class SwfCountClosedWorkflowExecutions(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CountClosedWorkflowExecutions')


class SwfCountOpenWorkflowExecutions(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CountOpenWorkflowExecutions')


class SwfCountPendingActivityTasks(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CountPendingActivityTasks')


class SwfCountPendingDecisionTasks(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='CountPendingDecisionTasks')


class SwfDeprecateActivityType(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DeprecateActivityType')


class SwfDeprecateDomain(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DeprecateDomain')


class SwfDeprecateWorkflowType(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DeprecateWorkflowType')


class SwfDescribeActivityType(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DescribeActivityType')


class SwfDescribeDomain(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DescribeDomain')


class SwfDescribeWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DescribeWorkflowExecution')


class SwfDescribeWorkflowType(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='DescribeWorkflowType')


class SwfFailWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='FailWorkflowExecution')


class SwfGetWorkflowExecutionHistory(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='GetWorkflowExecutionHistory')


class SwfListActivityTypes(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ListActivityTypes')


class SwfListClosedWorkflowExecutions(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ListClosedWorkflowExecutions')


class SwfListDomains(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ListDomains')


class SwfListOpenWorkflowExecutions(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ListOpenWorkflowExecutions')


class SwfListWorkflowTypes(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ListWorkflowTypes')


class SwfPollForActivityTask(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='PollForActivityTask')


class SwfPollForDecisionTask(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='PollForDecisionTask')


class SwfRecordActivityTaskHeartbeat(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RecordActivityTaskHeartbeat')


class SwfRecordMarker(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RecordMarker')


class SwfRegisterActivityType(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RegisterActivityType')


class SwfRegisterDomain(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RegisterDomain')


class SwfRegisterWorkflowType(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RegisterWorkflowType')


class SwfRequestCancelActivityTask(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RequestCancelActivityTask')


class SwfRequestCancelExternalWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RequestCancelExternalWorkflowExecution')


class SwfRequestCancelWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RequestCancelWorkflowExecution')


class SwfRespondActivityTaskCanceled(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RespondActivityTaskCanceled')


class SwfRespondActivityTaskCompleted(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RespondActivityTaskCompleted')


class SwfRespondActivityTaskFailed(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RespondActivityTaskFailed')


class SwfRespondDecisionTaskCompleted(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='RespondDecisionTaskCompleted')


class SwfScheduleActivityTask(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='ScheduleActivityTask')


class SwfSignalExternalWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='SignalExternalWorkflowExecution')


class SwfSignalWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='SignalWorkflowExecution')


class SwfStartChildWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='StartChildWorkflowExecution')


class SwfStartTimer(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='StartTimer')


class SwfStartWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='StartWorkflowExecution')


class SwfTerminateWorkflowExecution(IamAction):
    def __init__(self):
        super().__init__('swf', pattern='TerminateWorkflowExecution')


class TagGetResources(IamAction):
    def __init__(self):
        super().__init__('tag', pattern='GetResources')


class TagGetTagKeys(IamAction):
    def __init__(self):
        super().__init__('tag', pattern='GetTagKeys')


class TagGetTagValues(IamAction):
    def __init__(self):
        super().__init__('tag', pattern='GetTagValues')


class TagTagResources(IamAction):
    def __init__(self):
        super().__init__('tag', pattern='TagResources')


class TagUntagResources(IamAction):
    def __init__(self):
        super().__init__('tag', pattern='UntagResources')


class TranscribeGetTranscriptionJob(IamAction):
    def __init__(self):
        super().__init__('transcribe', pattern='GetTranscriptionJob')


class TranscribeListTranscriptionJobs(IamAction):
    def __init__(self):
        super().__init__('transcribe', pattern='ListTranscriptionJobs')


class TranscribeStartTranscriptionJob(IamAction):
    def __init__(self):
        super().__init__('transcribe', pattern='StartTranscriptionJob')


class TranslateTranslateText(IamAction):
    def __init__(self):
        super().__init__('translate', pattern='TranslateText')


class TrustedadvisorDescribeCheckItems(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='DescribeCheckItems')


class TrustedadvisorDescribeCheckRefreshStatuses(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='DescribeCheckRefreshStatuses')


class TrustedadvisorDescribeCheckSummaries(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='DescribeCheckSummaries')


class TrustedadvisorDescribeNotificationPreferences(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='DescribeNotificationPreferences')


class TrustedadvisorExcludeCheckItems(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='ExcludeCheckItems')


class TrustedadvisorIncludeCheckItems(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='IncludeCheckItems')


class TrustedadvisorRefreshCheck(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='RefreshCheck')


class TrustedadvisorUpdateNotificationPreferences(IamAction):
    def __init__(self):
        super().__init__('trustedadvisor', pattern='UpdateNotificationPreferences')


class WafRegionalAssociateWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='AssociateWebACL')


class WafRegionalCreateByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateByteMatchSet')


class WafRegionalCreateGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateGeoMatchSet')


class WafRegionalCreateIPSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateIPSet')


class WafRegionalCreateRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateRateBasedRule')


class WafRegionalCreateRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateRegexMatchSet')


class WafRegionalCreateRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateRegexPatternSet')


class WafRegionalCreateRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateRule')


class WafRegionalCreateSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateSizeConstraintSet')


class WafRegionalCreateSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateSqlInjectionMatchSet')


class WafRegionalCreateWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateWebACL')


class WafRegionalCreateXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='CreateXssMatchSet')


class WafRegionalDeleteByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteByteMatchSet')


class WafRegionalDeleteGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteGeoMatchSet')


class WafRegionalDeleteIPSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteIPSet')


class WafRegionalDeleteRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteRateBasedRule')


class WafRegionalDeleteRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteRegexMatchSet')


class WafRegionalDeleteRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteRegexPatternSet')


class WafRegionalDeleteRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteRule')


class WafRegionalDeleteSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteSizeConstraintSet')


class WafRegionalDeleteSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteSqlInjectionMatchSet')


class WafRegionalDeleteWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteWebACL')


class WafRegionalDeleteXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DeleteXssMatchSet')


class WafRegionalDisassociateWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='DisassociateWebACL')


class WafRegionalGetByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetByteMatchSet')


class WafRegionalGetChangeToken(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetChangeToken')


class WafRegionalGetChangeTokenStatus(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetChangeTokenStatus')


class WafRegionalGetGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetGeoMatchSet')


class WafRegionalGetIPSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetIPSet')


class WafRegionalGetRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetRateBasedRule')


class WafRegionalGetRateBasedRuleManagedKeys(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetRateBasedRuleManagedKeys')


class WafRegionalGetRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetRegexMatchSet')


class WafRegionalGetRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetRegexPatternSet')


class WafRegionalGetRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetRule')


class WafRegionalGetSampledRequests(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetSampledRequests')


class WafRegionalGetSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetSizeConstraintSet')


class WafRegionalGetSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetSqlInjectionMatchSet')


class WafRegionalGetWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetWebACL')


class WafRegionalGetWebACLForResource(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetWebACLForResource')


class WafRegionalGetXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='GetXssMatchSet')


class WafRegionalListByteMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListByteMatchSets')


class WafRegionalListGeoMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListGeoMatchSets')


class WafRegionalListIPSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListIPSets')


class WafRegionalListRateBasedRules(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListRateBasedRules')


class WafRegionalListRegexMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListRegexMatchSets')


class WafRegionalListRegexPatternSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListRegexPatternSets')


class WafRegionalListResourcesForWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListResourcesForWebACL')


class WafRegionalListRules(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListRules')


class WafRegionalListSizeConstraintSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListSizeConstraintSets')


class WafRegionalListSqlInjectionMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListSqlInjectionMatchSets')


class WafRegionalListWebACLs(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListWebACLs')


class WafRegionalListXssMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='ListXssMatchSets')


class WafRegionalUpdateByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateByteMatchSet')


class WafRegionalUpdateGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateGeoMatchSet')


class WafRegionalUpdateIPSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateIPSet')


class WafRegionalUpdateRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateRateBasedRule')


class WafRegionalUpdateRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateRegexMatchSet')


class WafRegionalUpdateRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateRegexPatternSet')


class WafRegionalUpdateRule(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateRule')


class WafRegionalUpdateSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateSizeConstraintSet')


class WafRegionalUpdateSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateSqlInjectionMatchSet')


class WafRegionalUpdateWebACL(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateWebACL')


class WafRegionalUpdateXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf-regional', pattern='UpdateXssMatchSet')


class WafCreateByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateByteMatchSet')


class WafCreateGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateGeoMatchSet')


class WafCreateIPSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateIPSet')


class WafCreateRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateRateBasedRule')


class WafCreateRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateRegexMatchSet')


class WafCreateRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateRegexPatternSet')


class WafCreateRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateRule')


class WafCreateSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateSizeConstraintSet')


class WafCreateSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateSqlInjectionMatchSet')


class WafCreateWebACL(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateWebACL')


class WafCreateXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='CreateXssMatchSet')


class WafDeleteByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteByteMatchSet')


class WafDeleteGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteGeoMatchSet')


class WafDeleteIPSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteIPSet')


class WafDeleteRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteRateBasedRule')


class WafDeleteRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteRegexMatchSet')


class WafDeleteRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteRegexPatternSet')


class WafDeleteRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteRule')


class WafDeleteSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteSizeConstraintSet')


class WafDeleteSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteSqlInjectionMatchSet')


class WafDeleteWebACL(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteWebACL')


class WafDeleteXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='DeleteXssMatchSet')


class WafGetByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetByteMatchSet')


class WafGetChangeToken(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetChangeToken')


class WafGetChangeTokenStatus(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetChangeTokenStatus')


class WafGetGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetGeoMatchSet')


class WafGetIPSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetIPSet')


class WafGetRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetRateBasedRule')


class WafGetRateBasedRuleManagedKeys(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetRateBasedRuleManagedKeys')


class WafGetRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetRegexMatchSet')


class WafGetRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetRegexPatternSet')


class WafGetRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetRule')


class WafGetSampledRequests(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetSampledRequests')


class WafGetSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetSizeConstraintSet')


class WafGetSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetSqlInjectionMatchSet')


class WafGetWebACL(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetWebACL')


class WafGetXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='GetXssMatchSet')


class WafListByteMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListByteMatchSets')


class WafListGeoMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListGeoMatchSets')


class WafListIPSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListIPSets')


class WafListRateBasedRules(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListRateBasedRules')


class WafListRegexMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListRegexMatchSets')


class WafListRegexPatternSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListRegexPatternSets')


class WafListRules(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListRules')


class WafListSizeConstraintSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListSizeConstraintSets')


class WafListSqlInjectionMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListSqlInjectionMatchSets')


class WafListWebACLs(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListWebACLs')


class WafListXssMatchSets(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='ListXssMatchSets')


class WafUpdateByteMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateByteMatchSet')


class WafUpdateGeoMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateGeoMatchSet')


class WafUpdateIPSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateIPSet')


class WafUpdateRateBasedRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateRateBasedRule')


class WafUpdateRegexMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateRegexMatchSet')


class WafUpdateRegexPatternSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateRegexPatternSet')


class WafUpdateRule(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateRule')


class WafUpdateSizeConstraintSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateSizeConstraintSet')


class WafUpdateSqlInjectionMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateSqlInjectionMatchSet')


class WafUpdateWebACL(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateWebACL')


class WafUpdateXssMatchSet(IamAction):
    def __init__(self):
        super().__init__('waf', pattern='UpdateXssMatchSet')


class WamAuthenticatePackager(IamAction):
    def __init__(self):
        super().__init__('wam', pattern='AuthenticatePackager')


class WorkdocsAbortDocumentVersionUpload(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='AbortDocumentVersionUpload')


class WorkdocsActivateUser(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='ActivateUser')


class WorkdocsAddResourcePermissions(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='AddResourcePermissions')


class WorkdocsAddUserToGroup(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='AddUserToGroup')


class WorkdocsCheckAlias(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='CheckAlias')


class WorkdocsCreateFolder(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='CreateFolder')


class WorkdocsCreateInstance(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='CreateInstance')


class WorkdocsCreateNotificationSubscription(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='CreateNotificationSubscription')


class WorkdocsCreateUser(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='CreateUser')


class WorkdocsDeactivateUser(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeactivateUser')


class WorkdocsDeleteDocument(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeleteDocument')


class WorkdocsDeleteFolder(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeleteFolder')


class WorkdocsDeleteFolderContents(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeleteFolderContents')


class WorkdocsDeleteInstance(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeleteInstance')


class WorkdocsDeleteNotificationSubscription(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeleteNotificationSubscription')


class WorkdocsDeleteUser(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeleteUser')


class WorkdocsDeregisterDirectory(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DeregisterDirectory')


class WorkdocsDescribeAvailableDirectories(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeAvailableDirectories')


class WorkdocsDescribeDocumentVersions(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeDocumentVersions')


class WorkdocsDescribeFolderContents(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeFolderContents')


class WorkdocsDescribeInstances(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeInstances')


class WorkdocsDescribeNotificationSubscriptions(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeNotificationSubscriptions')


class WorkdocsDescribeResourcePermissions(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeResourcePermissions')


class WorkdocsDescribeUsers(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='DescribeUsers')


class WorkdocsGetDocument(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='GetDocument')


class WorkdocsGetDocumentPath(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='GetDocumentPath')


class WorkdocsGetDocumentVersion(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='GetDocumentVersion')


class WorkdocsGetFolder(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='GetFolder')


class WorkdocsGetFolderPath(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='GetFolderPath')


class WorkdocsInitiateDocumentVersionUpload(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='InitiateDocumentVersionUpload')


class WorkdocsRegisterDirectory(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='RegisterDirectory')


class WorkdocsRemoveAllResourcePermissions(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='RemoveAllResourcePermissions')


class WorkdocsRemoveResourcePermission(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='RemoveResourcePermission')


class WorkdocsRemoveUserFromGroup(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='RemoveUserFromGroup')


class WorkdocsUpdateDocument(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='UpdateDocument')


class WorkdocsUpdateDocumentVersion(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='UpdateDocumentVersion')


class WorkdocsUpdateFolder(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='UpdateFolder')


class WorkdocsUpdateInstanceAlias(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='UpdateInstanceAlias')


class WorkdocsUpdateUser(IamAction):
    def __init__(self):
        super().__init__('workdocs', pattern='UpdateUser')


class WorkmailAddMembersToGroup(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='AddMembersToGroup')


class WorkmailCreateGroup(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='CreateGroup')


class WorkmailCreateMailDomain(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='CreateMailDomain')


class WorkmailCreateMailUser(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='CreateMailUser')


class WorkmailCreateOrganization(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='CreateOrganization')


class WorkmailCreateResource(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='CreateResource')


class WorkmailDeleteMailDomain(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DeleteMailDomain')


class WorkmailDeleteMobileDevice(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DeleteMobileDevice')


class WorkmailDeleteOrganization(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DeleteOrganization')


class WorkmailDescribeDirectories(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DescribeDirectories')


class WorkmailDescribeKmsKeys(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DescribeKmsKeys')


class WorkmailDescribeMailDomains(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DescribeMailDomains')


class WorkmailDescribeMailGroups(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DescribeMailGroups')


class WorkmailDescribeMailUsers(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DescribeMailUsers')


class WorkmailDescribeOrganizations(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DescribeOrganizations')


class WorkmailDisableMailGroups(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DisableMailGroups')


class WorkmailDisableMailUsers(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='DisableMailUsers')


class WorkmailEnableMailDomain(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='EnableMailDomain')


class WorkmailEnableMailGroups(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='EnableMailGroups')


class WorkmailEnableMailUsers(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='EnableMailUsers')


class WorkmailGetMailDomainDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='GetMailDomainDetails')


class WorkmailGetMailGroupDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='GetMailGroupDetails')


class WorkmailGetMailUserDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='GetMailUserDetails')


class WorkmailGetMobileDeviceDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='GetMobileDeviceDetails')


class WorkmailGetMobileDevicesForUser(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='GetMobileDevicesForUser')


class WorkmailGetMobilePolicyDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='GetMobilePolicyDetails')


class WorkmailListMembersInMailGroup(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='ListMembersInMailGroup')


class WorkmailRemoveMembersFromGroup(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='RemoveMembersFromGroup')


class WorkmailResetUserPassword(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='ResetUserPassword')


class WorkmailSearchMembers(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='SearchMembers')


class WorkmailSetAdmin(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='SetAdmin')


class WorkmailSetDefaultMailDomain(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='SetDefaultMailDomain')


class WorkmailSetMailGroupDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='SetMailGroupDetails')


class WorkmailSetMailUserDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='SetMailUserDetails')


class WorkmailSetMobilePolicyDetails(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='SetMobilePolicyDetails')


class WorkmailWipeMobileDevice(IamAction):
    def __init__(self):
        super().__init__('workmail', pattern='WipeMobileDevice')


class WorkspacesCreateTags(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='CreateTags')


class WorkspacesCreateWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='CreateWorkspaces')


class WorkspacesDeleteTags(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='DeleteTags')


class WorkspacesDescribeTags(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='DescribeTags')


class WorkspacesDescribeWorkspaceBundles(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='DescribeWorkspaceBundles')


class WorkspacesDescribeWorkspaceDirectories(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='DescribeWorkspaceDirectories')


class WorkspacesDescribeWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='DescribeWorkspaces')


class WorkspacesDescribeWorkspacesConnectionStatus(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='DescribeWorkspacesConnectionStatus')


class WorkspacesModifyWorkspaceProperties(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='ModifyWorkspaceProperties')


class WorkspacesRebootWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='RebootWorkspaces')


class WorkspacesRebuildWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='RebuildWorkspaces')


class WorkspacesStartWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='StartWorkspaces')


class WorkspacesStopWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='StopWorkspaces')


class WorkspacesTerminateWorkspaces(IamAction):
    def __init__(self):
        super().__init__('workspaces', pattern='TerminateWorkspaces')


class XrayBatchGetTraces(IamAction):
    def __init__(self):
        super().__init__('xray', pattern='BatchGetTraces')


class XrayGetServiceGraph(IamAction):
    def __init__(self):
        super().__init__('xray', pattern='GetServiceGraph')


class XrayGetTraceGraph(IamAction):
    def __init__(self):
        super().__init__('xray', pattern='GetTraceGraph')


class XrayGetTraceSummaries(IamAction):
    def __init__(self):
        super().__init__('xray', pattern='GetTraceSummaries')


class XrayPutTelemetryRecords(IamAction):
    def __init__(self):
        super().__init__('xray', pattern='PutTelemetryRecords')


class XrayPutTraceSegments(IamAction):
    def __init__(self):
        super().__init__('xray', pattern='PutTraceSegments')
