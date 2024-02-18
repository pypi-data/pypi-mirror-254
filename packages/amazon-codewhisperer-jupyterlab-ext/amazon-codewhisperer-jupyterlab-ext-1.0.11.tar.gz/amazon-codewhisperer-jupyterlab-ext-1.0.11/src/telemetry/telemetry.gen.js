"use strict";
exports.__esModule = true;
exports.TelemetryBase = exports.definitions = void 0;
exports.definitions = {
    apigateway_copyUrl: { unit: "None", passive: false, requiredMetadata: [] },
    apigateway_invokeLocal: {
        unit: "None",
        passive: false,
        requiredMetadata: ["debug"],
    },
    apigateway_invokeRemote: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apigateway_startLocalServer: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_openServiceUrl: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_copyServiceUrl: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_createService: {
        unit: "None",
        passive: false,
        requiredMetadata: ["appRunnerServiceSource"],
    },
    apprunner_pauseService: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_resumeService: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_deleteService: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_startDeployment: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_viewApplicationLogs: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    apprunner_viewServiceLogs: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    aws_copyArn: {
        unit: "None",
        passive: false,
        requiredMetadata: ["serviceType"],
    },
    aws_deleteResource: {
        unit: "None",
        passive: false,
        requiredMetadata: ["serviceType"],
    },
    aws_setCredentials: { unit: "None", passive: false, requiredMetadata: [] },
    aws_setRegion: { unit: "None", passive: false, requiredMetadata: [] },
    aws_setPartition: {
        unit: "None",
        passive: false,
        requiredMetadata: ["partitionId"],
    },
    aws_openCredentials: { unit: "None", passive: false, requiredMetadata: [] },
    aws_openUrl: { unit: "None", passive: false, requiredMetadata: [] },
    aws_saveCredentials: { unit: "None", passive: false, requiredMetadata: [] },
    aws_modifyCredentials: {
        unit: "None",
        passive: false,
        requiredMetadata: ["credentialModification", "source"],
    },
    aws_loadCredentials: {
        unit: "Count",
        passive: true,
        requiredMetadata: ["credentialSourceId"],
    },
    aws_createCredentials: { unit: "None", passive: false, requiredMetadata: [] },
    aws_injectCredentials: { unit: "None", passive: false, requiredMetadata: [] },
    aws_validateCredentials: {
        unit: "None",
        passive: true,
        requiredMetadata: [],
    },
    aws_refreshCredentials: { unit: "None", passive: true, requiredMetadata: [] },
    aws_loginWithBrowser: { unit: "None", passive: false, requiredMetadata: [] },
    aws_help: { unit: "None", passive: false, requiredMetadata: [] },
    aws_helpQuickstart: { unit: "None", passive: true, requiredMetadata: [] },
    aws_showExtensionSource: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    aws_refreshExplorer: { unit: "None", passive: false, requiredMetadata: [] },
    aws_expandExplorerNode: {
        unit: "None",
        passive: false,
        requiredMetadata: ["serviceType"],
    },
    aws_reportPluginIssue: { unit: "None", passive: false, requiredMetadata: [] },
    beanstalk_deploy: {
        unit: "None",
        passive: false,
        requiredMetadata: ["initialDeploy"],
    },
    beanstalk_publishWizard: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_openApplication: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_openEnvironment: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_deleteApplication: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_deleteEnvironment: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_restartApplication: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_rebuildEnvironment: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    beanstalk_editEnvironment: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_openDistribution: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_openStreamingDistribution: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_openInvalidationRequest: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_deleteDistribution: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_deleteStreamingDistribution: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_createDistribution: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudfront_createStreamingDistribution: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_copyArn: {
        unit: "None",
        passive: false,
        requiredMetadata: ["cloudWatchResourceType"],
    },
    cloudwatchlogs_open: {
        unit: "None",
        passive: false,
        requiredMetadata: ["cloudWatchResourceType", "source"],
    },
    cloudwatchlogs_openGroup: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_openStream: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_delete: {
        unit: "None",
        passive: false,
        requiredMetadata: ["cloudWatchResourceType"],
    },
    cloudwatchlogs_download: {
        unit: "Bytes",
        passive: false,
        requiredMetadata: ["cloudWatchResourceType"],
    },
    cloudwatchlogs_downloadStreamToFile: {
        unit: "Bytes",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_openStreamInEditor: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_viewCurrentMessagesInEditor: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_wrapEvents: {
        unit: "None",
        passive: false,
        requiredMetadata: ["enabled"],
    },
    cloudwatchlogs_tailStream: {
        unit: "None",
        passive: false,
        requiredMetadata: ["enabled"],
    },
    cloudwatchlogs_refresh: {
        unit: "None",
        passive: false,
        requiredMetadata: ["cloudWatchResourceType"],
    },
    cloudwatchlogs_refreshGroup: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_refreshStream: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_filter: {
        unit: "None",
        passive: false,
        requiredMetadata: ["cloudWatchResourceType"],
    },
    cloudwatchlogs_searchStream: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_searchGroup: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchlogs_showEventsAround: {
        unit: "Milliseconds",
        passive: false,
        requiredMetadata: [],
    },
    cloudformation_createProject: {
        unit: "None",
        passive: false,
        requiredMetadata: ["templateName"],
    },
    cloudformation_deploy: {
        unit: "None",
        passive: false,
        requiredMetadata: ["initialDeploy"],
    },
    cloudformation_publishWizard: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudformation_open: { unit: "None", passive: false, requiredMetadata: [] },
    codecommit_cloneRepo: { unit: "None", passive: false, requiredMetadata: [] },
    codecommit_createRepo: { unit: "None", passive: false, requiredMetadata: [] },
    codecommit_setCredentials: {
        unit: "None",
        passive: true,
        requiredMetadata: [],
    },
    dynamodb_createTable: { unit: "None", passive: false, requiredMetadata: [] },
    dynamodb_deleteTable: { unit: "None", passive: false, requiredMetadata: [] },
    dynamodb_edit: {
        unit: "None",
        passive: false,
        requiredMetadata: ["dynamoDbTarget"],
    },
    dynamodb_fetchRecords: {
        unit: "None",
        passive: false,
        requiredMetadata: ["dynamoDbFetchType"],
    },
    dynamodb_openTable: { unit: "None", passive: false, requiredMetadata: [] },
    dynamodb_view: {
        unit: "None",
        passive: false,
        requiredMetadata: ["dynamoDbTarget"],
    },
    ec2_changeState: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ec2InstanceState"],
    },
    ec2_clearPrivateKey: { unit: "Count", passive: false, requiredMetadata: [] },
    ec2_connectToInstance: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ec2ConnectionType"],
    },
    ec2_copyAmiToRegion: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_createAmi: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_createElasticIp: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_createKeyPair: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_createSecurityGroup: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_createSnapshot: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_createVolume: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_deleteAmi: { unit: "Count", passive: false, requiredMetadata: [] },
    ec2_deleteElasticIp: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_deleteKeyPair: { unit: "Count", passive: false, requiredMetadata: [] },
    ec2_deleteSecurityGroup: {
        unit: "Count",
        passive: false,
        requiredMetadata: [],
    },
    ec2_deleteSnapshot: { unit: "Count", passive: false, requiredMetadata: [] },
    ec2_deleteVolume: { unit: "Count", passive: false, requiredMetadata: [] },
    ec2_editAmiPermission: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_editInstanceElasticIp: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_editInstanceShutdownBehavior: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_editInstanceTerminationProtection: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_editInstanceType: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_editInstanceUserData: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_editSecurityGroupPermission: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_editVolumeAttachment: {
        unit: "None",
        passive: false,
        requiredMetadata: ["enabled"],
    },
    ec2_exportPrivateKey: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_importPrivateKey: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_launchInstance: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_openInstances: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_openAMIs: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_openElasticIPs: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_openKeyPairs: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_openSecurityGroups: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ec2_openVolumes: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_viewInstanceSystemLog: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ecs_openCluster: { unit: "None", passive: false, requiredMetadata: [] },
    ec2_viewInstanceUserData: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ecs_enableExecuteCommand: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ecs_disableExecuteCommand: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    ecs_runExecuteCommand: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ecsExecuteCommandType"],
    },
    ecr_copyRepositoryUri: { unit: "None", passive: false, requiredMetadata: [] },
    ecr_copyTagUri: { unit: "None", passive: false, requiredMetadata: [] },
    ecr_createRepository: { unit: "None", passive: false, requiredMetadata: [] },
    ecr_deleteRepository: { unit: "None", passive: false, requiredMetadata: [] },
    ecr_deleteTags: { unit: "Count", passive: false, requiredMetadata: [] },
    ecr_deployImage: { unit: "None", passive: false, requiredMetadata: [] },
    ecs_deployScheduledTask: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ecsLaunchType"],
    },
    ecs_deployService: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ecsLaunchType"],
    },
    ecs_deployTask: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ecsLaunchType"],
    },
    ecs_publishWizard: { unit: "None", passive: false, requiredMetadata: [] },
    ecs_openRepository: { unit: "None", passive: false, requiredMetadata: [] },
    ecs_deleteService: { unit: "None", passive: false, requiredMetadata: [] },
    ecs_editService: { unit: "None", passive: false, requiredMetadata: [] },
    ecs_deleteCluster: { unit: "None", passive: false, requiredMetadata: [] },
    ecs_stopTask: { unit: "Count", passive: false, requiredMetadata: [] },
    ecs_deleteScheduledTask: {
        unit: "Count",
        passive: false,
        requiredMetadata: [],
    },
    feedback_result: { unit: "None", passive: false, requiredMetadata: [] },
    file_editAwsFile: {
        unit: "None",
        passive: false,
        requiredMetadata: ["awsFiletype"],
    },
    iam_openRole: { unit: "None", passive: false, requiredMetadata: [] },
    iam_openGroup: { unit: "None", passive: false, requiredMetadata: [] },
    iam_openUser: { unit: "None", passive: false, requiredMetadata: [] },
    iam_open: {
        unit: "None",
        passive: false,
        requiredMetadata: ["iamResourceType"],
    },
    iam_create: {
        unit: "None",
        passive: false,
        requiredMetadata: ["iamResourceType"],
    },
    iam_delete: {
        unit: "None",
        passive: false,
        requiredMetadata: ["iamResourceType"],
    },
    iam_edit: {
        unit: "None",
        passive: false,
        requiredMetadata: ["iamResourceType"],
    },
    iam_createUserAccessKey: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    iam_deleteUserAccessKey: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    lambda_delete: { unit: "None", passive: false, requiredMetadata: [] },
    lambda_configure: { unit: "None", passive: false, requiredMetadata: [] },
    lambda_create: {
        unit: "None",
        passive: false,
        requiredMetadata: ["runtime"],
    },
    lambda_createProject: {
        unit: "None",
        passive: false,
        requiredMetadata: ["language", "templateName"],
    },
    lambda_goToHandler: { unit: "None", passive: false, requiredMetadata: [] },
    lambda_editFunction: {
        unit: "None",
        passive: false,
        requiredMetadata: ["lambdaPackageType"],
    },
    lambda_invokeRemote: { unit: "None", passive: false, requiredMetadata: [] },
    lambda_invokeLocal: {
        unit: "None",
        passive: false,
        requiredMetadata: ["lambdaPackageType", "debug"],
    },
    lambda_import: { unit: "None", passive: false, requiredMetadata: [] },
    lambda_updateFunctionCode: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    lambda_deploy: {
        unit: "None",
        passive: false,
        requiredMetadata: ["lambdaPackageType", "initialDeploy"],
    },
    lambda_publishWizard: { unit: "None", passive: false, requiredMetadata: [] },
    cloudformation_delete: { unit: "None", passive: false, requiredMetadata: [] },
    rds_getCredentials: {
        unit: "Milliseconds",
        passive: false,
        requiredMetadata: ["databaseCredentials", "databaseEngine"],
    },
    rds_openInstances: { unit: "None", passive: false, requiredMetadata: [] },
    rds_openSecurityGroups: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    rds_openSubnets: { unit: "None", passive: false, requiredMetadata: [] },
    rds_launchInstance: { unit: "None", passive: false, requiredMetadata: [] },
    rds_createSecurityGroup: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    rds_createSubnetGroup: { unit: "None", passive: false, requiredMetadata: [] },
    rds_deleteInstance: { unit: "None", passive: false, requiredMetadata: [] },
    rds_deleteSecurityGroup: {
        unit: "Count",
        passive: false,
        requiredMetadata: [],
    },
    rds_deleteSubnetGroup: {
        unit: "Count",
        passive: false,
        requiredMetadata: [],
    },
    rds_createConnectionConfiguration: {
        unit: "None",
        passive: false,
        requiredMetadata: ["databaseCredentials"],
    },
    redshift_getCredentials: {
        unit: "Milliseconds",
        passive: false,
        requiredMetadata: ["databaseCredentials"],
    },
    redshift_createConnectionConfiguration: {
        unit: "None",
        passive: false,
        requiredMetadata: ["databaseCredentials"],
    },
    sam_deploy: { unit: "None", passive: false, requiredMetadata: [] },
    sam_sync: {
        unit: "None",
        passive: false,
        requiredMetadata: ["syncedResources", "lambdaPackageType"],
    },
    sam_init: { unit: "None", passive: false, requiredMetadata: [] },
    schemas_view: { unit: "None", passive: false, requiredMetadata: [] },
    schemas_download: { unit: "None", passive: false, requiredMetadata: [] },
    schemas_search: { unit: "None", passive: false, requiredMetadata: [] },
    session_start: { unit: "None", passive: true, requiredMetadata: [] },
    session_end: { unit: "None", passive: true, requiredMetadata: [] },
    s3_copyBucketName: { unit: "None", passive: false, requiredMetadata: [] },
    s3_copyPath: { unit: "None", passive: false, requiredMetadata: [] },
    s3_copyUri: { unit: "None", passive: false, requiredMetadata: [] },
    s3_copyUrl: { unit: "None", passive: false, requiredMetadata: ["presigned"] },
    s3_createBucket: { unit: "None", passive: false, requiredMetadata: [] },
    s3_deleteBucket: { unit: "None", passive: false, requiredMetadata: [] },
    s3_deleteObject: { unit: "None", passive: false, requiredMetadata: [] },
    s3_createFolder: { unit: "None", passive: false, requiredMetadata: [] },
    s3_downloadObject: { unit: "None", passive: false, requiredMetadata: [] },
    s3_downloadObjects: { unit: "Count", passive: false, requiredMetadata: [] },
    s3_uploadObject: { unit: "None", passive: false, requiredMetadata: [] },
    s3_renameObject: { unit: "None", passive: false, requiredMetadata: [] },
    s3_uploadObjects: { unit: "Count", passive: false, requiredMetadata: [] },
    s3_openEditor: { unit: "None", passive: false, requiredMetadata: [] },
    s3_editObject: { unit: "Count", passive: false, requiredMetadata: [] },
    s3_openBucketProperties: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    s3_openMultipartUpload: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    toolkit_init: { unit: "None", passive: true, requiredMetadata: [] },
    toolkit_viewLogs: { unit: "None", passive: false, requiredMetadata: [] },
    sqs_openQueue: {
        unit: "None",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_createQueue: { unit: "None", passive: false, requiredMetadata: [] },
    sqs_sendMessage: {
        unit: "None",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_deleteMessages: {
        unit: "Count",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_subscribeSns: {
        unit: "None",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_configureLambdaTrigger: {
        unit: "None",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_editQueueParameters: {
        unit: "None",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_purgeQueue: {
        unit: "None",
        passive: false,
        requiredMetadata: ["sqsQueueType"],
    },
    sqs_deleteQueue: { unit: "None", passive: false, requiredMetadata: [] },
    sns_createTopic: { unit: "None", passive: false, requiredMetadata: [] },
    sns_createSubscription: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    sns_openTopic: { unit: "None", passive: false, requiredMetadata: [] },
    sns_openSubscriptions: { unit: "None", passive: false, requiredMetadata: [] },
    sns_deleteTopic: { unit: "None", passive: false, requiredMetadata: [] },
    sns_deleteSubscription: {
        unit: "Count",
        passive: false,
        requiredMetadata: [],
    },
    sns_publishMessage: { unit: "None", passive: false, requiredMetadata: [] },
    vpc_openRouteTables: { unit: "None", passive: false, requiredMetadata: [] },
    vpc_openGateways: { unit: "None", passive: false, requiredMetadata: [] },
    vpc_openACLs: { unit: "None", passive: false, requiredMetadata: [] },
    vpc_openSubnets: { unit: "None", passive: false, requiredMetadata: [] },
    vpc_openVPCs: { unit: "None", passive: false, requiredMetadata: [] },
    cloudwatchinsights_openEditor: {
        unit: "None",
        passive: false,
        requiredMetadata: ["insightsDialogOpenSource"],
    },
    cloudwatchinsights_executeQuery: {
        unit: "None",
        passive: false,
        requiredMetadata: ["insightsQueryTimeType", "insightsQueryStringType"],
    },
    cloudwatchinsights_saveQuery: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchinsights_retrieveQuery: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    cloudwatchinsights_openDetailedLogRecord: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    toolkit_getExternalResource: {
        unit: "None",
        passive: true,
        requiredMetadata: ["url"],
    },
    dynamicresource_getResource: {
        unit: "None",
        passive: false,
        requiredMetadata: ["resourceType"],
    },
    dynamicresource_listResource: {
        unit: "None",
        passive: false,
        requiredMetadata: ["resourceType"],
    },
    dynamicresource_selectResources: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    dynamicresource_copyIdentifier: {
        unit: "None",
        passive: false,
        requiredMetadata: ["resourceType"],
    },
    dynamicresource_mutateResource: {
        unit: "None",
        passive: false,
        requiredMetadata: ["resourceType", "dynamicResourceOperation"],
    },
    aws_experimentActivation: {
        unit: "None",
        passive: false,
        requiredMetadata: ["experimentId", "experimentState"],
    },
    aws_toolInstallation: {
        unit: "None",
        passive: true,
        requiredMetadata: ["toolId"],
    },
    aws_modifySetting: {
        unit: "None",
        passive: false,
        requiredMetadata: ["settingId"],
    },
    ui_click: { unit: "None", passive: false, requiredMetadata: ["elementId"] },
    deeplink_open: { unit: "None", passive: true, requiredMetadata: ["source"] },
    codewhisperer_codePercentage: {
        unit: "None",
        passive: true,
        requiredMetadata: [
            "codewhispererAcceptedTokens",
            "codewhispererLanguage",
            "codewhispererPercentage",
            "codewhispererTotalTokens",
            "successCount",
        ],
    },
    codewhisperer_securityScan: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererCodeScanLines",
            "codewhispererCodeScanSrcPayloadBytes",
            "codewhispererCodeScanSrcZipFileBytes",
            "codewhispererCodeScanTotalIssues",
            "codewhispererLanguage",
            "contextTruncationDuration",
            "artifactsUploadDuration",
            "codeScanServiceInvocationsDuration",
        ],
    },
    codewhisperer_serviceInvocation: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererCursorOffset",
            "codewhispererLanguage",
            "codewhispererLineNumber",
            "codewhispererTriggerType",
        ],
    },
    codewhisperer_blockedInvocation: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererCursorOffset",
            "codewhispererLanguage",
            "codewhispererLineNumber",
            "codewhispererTriggerType",
        ],
    },
    codewhisperer_userDecision: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererCompletionType",
            "codewhispererLanguage",
            "codewhispererRequestId",
            "codewhispererSuggestionIndex",
            "codewhispererSuggestionReferenceCount",
            "codewhispererSuggestionState",
            "codewhispererTriggerType",
        ],
    },
    codewhisperer_userTriggerDecision: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererFirstRequestId",
            "codewhispererCompletionType",
            "codewhispererLanguage",
            "codewhispererTriggerType",
            "codewhispererLineNumber",
            "codewhispererCursorOffset",
            "codewhispererSuggestionCount",
            "codewhispererSuggestionImportCount",
            "codewhispererTypeaheadLength",
            "codewhispererSuggestionState",
        ],
    },
    codewhisperer_userModification: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererCompletionType",
            "codewhispererLanguage",
            "codewhispererModificationPercentage",
            "codewhispererRequestId",
            "codewhispererSuggestionIndex",
            "codewhispererTriggerType",
        ],
    },
    codewhisperer_perceivedLatency: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "codewhispererRequestId",
            "codewhispererTriggerType",
            "codewhispererCompletionType",
            "codewhispererLanguage",
        ],
    },
    codewhisperer_clientComponentLatency: {
        unit: "None",
        passive: true,
        requiredMetadata: [
            "codewhispererRequestId",
            "codewhispererSessionId",
            "codewhispererPreprocessingLatency",
            "codewhispererCredentialFetchingLatency",
            "codewhispererPostprocessingLatency",
            "codewhispererFirstCompletionLatency",
            "codewhispererEndToEndLatency",
            "codewhispererAllCompletionsLatency",
            "codewhispererCompletionType",
            "codewhispererTriggerType",
            "codewhispererLanguage",
        ],
    },
    codecatalyst_createDevEnvironment: {
        unit: "None",
        passive: false,
        requiredMetadata: ["userId"],
    },
    codecatalyst_updateDevEnvironmentSettings: {
        unit: "None",
        passive: false,
        requiredMetadata: [
            "userId",
            "codecatalyst_updateDevEnvironmentLocationType",
        ],
    },
    codecatalyst_updateDevfile: {
        unit: "None",
        passive: false,
        requiredMetadata: ["userId"],
    },
    codecatalyst_localClone: {
        unit: "None",
        passive: false,
        requiredMetadata: ["userId"],
    },
    codecatalyst_connect: {
        unit: "None",
        passive: false,
        requiredMetadata: ["userId"],
    },
    codecatalyst_devEnvironmentWorkflowStatistic: {
        unit: "None",
        passive: true,
        requiredMetadata: ["userId", "codecatalyst_devEnvironmentWorkflowStep"],
    },
    vscode_executeCommand: {
        unit: "None",
        passive: true,
        requiredMetadata: ["command", "debounceCount"],
    },
    ssm_createDocument: { unit: "None", passive: false, requiredMetadata: [] },
    ssm_deleteDocument: { unit: "None", passive: false, requiredMetadata: [] },
    ssm_executeDocument: { unit: "None", passive: false, requiredMetadata: [] },
    ssm_openDocument: { unit: "None", passive: false, requiredMetadata: [] },
    ssm_publishDocument: {
        unit: "None",
        passive: false,
        requiredMetadata: ["ssmOperation"],
    },
    ssm_updateDocumentVersion: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    stepfunctions_createStateMachineFromTemplate: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    stepfunctions_downloadStateMachineDefinition: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    stepfunctions_executeStateMachine: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    stepfunctions_executeStateMachineView: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    stepfunctions_previewstatemachine: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    vscode_activeRegions: { unit: "Count", passive: true, requiredMetadata: [] },
    vscode_viewLogs: { unit: "None", passive: false, requiredMetadata: [] },
    aws_showExplorerErrorDetails: {
        unit: "None",
        passive: false,
        requiredMetadata: [],
    },
    aws_showRegion: { unit: "None", passive: false, requiredMetadata: [] },
    aws_hideRegion: { unit: "None", passive: false, requiredMetadata: [] },
    sam_detect: { unit: "None", passive: true, requiredMetadata: [] },
    cdk_explorerDisabled: { unit: "None", passive: false, requiredMetadata: [] },
    cdk_explorerEnabled: { unit: "None", passive: false, requiredMetadata: [] },
    cdk_appExpanded: { unit: "None", passive: false, requiredMetadata: [] },
    cdk_provideFeedback: { unit: "None", passive: false, requiredMetadata: [] },
    cdk_help: { unit: "None", passive: false, requiredMetadata: [] },
    cdk_refreshExplorer: { unit: "None", passive: false, requiredMetadata: [] },
    sam_attachDebugger: {
        unit: "None",
        passive: false,
        requiredMetadata: ["lambdaPackageType", "runtime", "attempts"],
    },
    sam_openConfigUi: { unit: "None", passive: false, requiredMetadata: [] },
};
var TelemetryBase = /** @class */ (function () {
    function TelemetryBase() {
    }
    Object.defineProperty(TelemetryBase.prototype, "apigateway_copyUrl", {
        /** Copying an API Gateway remote URL */
        get: function () {
            return this.getMetric("apigateway_copyUrl");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apigateway_invokeLocal", {
        /** Invoking one simulated API Gateway call using the SAM cli */
        get: function () {
            return this.getMetric("apigateway_invokeLocal");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apigateway_invokeRemote", {
        /** Calling a remote API Gateway */
        get: function () {
            return this.getMetric("apigateway_invokeRemote");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apigateway_startLocalServer", {
        /** Called when starting a local API Gateway server simulator with SAM. Only called when starting it for long running testing, not for single invokes */
        get: function () {
            return this.getMetric("apigateway_startLocalServer");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_openServiceUrl", {
        /** Open the service URL in a browser */
        get: function () {
            return this.getMetric("apprunner_openServiceUrl");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_copyServiceUrl", {
        /** Copy the service URL */
        get: function () {
            return this.getMetric("apprunner_copyServiceUrl");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_createService", {
        /** Create an App Runner service */
        get: function () {
            return this.getMetric("apprunner_createService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_pauseService", {
        /** Pause a running App Runner service */
        get: function () {
            return this.getMetric("apprunner_pauseService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_resumeService", {
        /** Resume a paused App Runner service */
        get: function () {
            return this.getMetric("apprunner_resumeService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_deleteService", {
        /** Delete an App Runner service */
        get: function () {
            return this.getMetric("apprunner_deleteService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_startDeployment", {
        /** Start a new deployment for an App Runner service */
        get: function () {
            return this.getMetric("apprunner_startDeployment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_viewApplicationLogs", {
        /** View the App Runner application logs (the logs for your running service) */
        get: function () {
            return this.getMetric("apprunner_viewApplicationLogs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "apprunner_viewServiceLogs", {
        /** View the App Runner service logs (the logs produced by App Runner) */
        get: function () {
            return this.getMetric("apprunner_viewServiceLogs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_copyArn", {
        /** Copy the ARN of an AWS resource */
        get: function () {
            return this.getMetric("aws_copyArn");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_deleteResource", {
        /** Delete an AWS resource */
        get: function () {
            return this.getMetric("aws_deleteResource");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_setCredentials", {
        /** Select a credentials profile */
        get: function () {
            return this.getMetric("aws_setCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_setRegion", {
        /** A region change occurred */
        get: function () {
            return this.getMetric("aws_setRegion");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_setPartition", {
        /** A partition change occurred */
        get: function () {
            return this.getMetric("aws_setPartition");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_openCredentials", {
        /** Open the credentials file */
        get: function () {
            return this.getMetric("aws_openCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_openUrl", {
        /** Opens a url */
        get: function () {
            return this.getMetric("aws_openUrl");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_saveCredentials", {
        /** Save credentials */
        get: function () {
            return this.getMetric("aws_saveCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_modifyCredentials", {
        /** Modify credentials (e.g. Add, Edit, Delete) */
        get: function () {
            return this.getMetric("aws_modifyCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_loadCredentials", {
        /** Load credentials from a credential source */
        get: function () {
            return this.getMetric("aws_loadCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_createCredentials", {
        /** Create a new credentials file */
        get: function () {
            return this.getMetric("aws_createCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_injectCredentials", {
        /** Inject selected AWS credentials into a third-party run (e.g. RunConfiguration) */
        get: function () {
            return this.getMetric("aws_injectCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_validateCredentials", {
        /** Validate credentials when selecting new credentials */
        get: function () {
            return this.getMetric("aws_validateCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_refreshCredentials", {
        /** Emitted when credentials are automatically refreshed by the AWS SDK or Toolkit */
        get: function () {
            return this.getMetric("aws_refreshCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_loginWithBrowser", {
        /** Called when a connection requires login using the browser */
        get: function () {
            return this.getMetric("aws_loginWithBrowser");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_help", {
        /** Open docs for the extension */
        get: function () {
            return this.getMetric("aws_help");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_helpQuickstart", {
        /** Open the quickstart guide */
        get: function () {
            return this.getMetric("aws_helpQuickstart");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_showExtensionSource", {
        /** Open the repo for the extension */
        get: function () {
            return this.getMetric("aws_showExtensionSource");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_refreshExplorer", {
        /** Refresh the AWS explorer window */
        get: function () {
            return this.getMetric("aws_refreshExplorer");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_expandExplorerNode", {
        /** Expand a service root node in the AWS explorer window */
        get: function () {
            return this.getMetric("aws_expandExplorerNode");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_reportPluginIssue", {
        /** Report an issue with the plugin */
        get: function () {
            return this.getMetric("aws_reportPluginIssue");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_deploy", {
        /** Called when deploying an application to Elastic Beanstalk */
        get: function () {
            return this.getMetric("beanstalk_deploy");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_publishWizard", {
        /** Called when user completes the Elastic Beanstalk publish wizard */
        get: function () {
            return this.getMetric("beanstalk_publishWizard");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_openApplication", {
        /** Open a window to view the status of the Beanstalk Application */
        get: function () {
            return this.getMetric("beanstalk_openApplication");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_openEnvironment", {
        /** Open a window to view the status of the Beanstalk Environment */
        get: function () {
            return this.getMetric("beanstalk_openEnvironment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_deleteApplication", {
        /** Called when user deletes a Beanstalk application */
        get: function () {
            return this.getMetric("beanstalk_deleteApplication");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_deleteEnvironment", {
        /** Called when user deletes a Beanstalk environment */
        get: function () {
            return this.getMetric("beanstalk_deleteEnvironment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_restartApplication", {
        /** Restart application server for a Beanstalk environment */
        get: function () {
            return this.getMetric("beanstalk_restartApplication");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_rebuildEnvironment", {
        /** Rebuild a Beanstalk environment */
        get: function () {
            return this.getMetric("beanstalk_rebuildEnvironment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "beanstalk_editEnvironment", {
        /** Edit configuration of a Beanstalk environment */
        get: function () {
            return this.getMetric("beanstalk_editEnvironment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_openDistribution", {
        /** Open a window to view the status of the CloudFront Distribution */
        get: function () {
            return this.getMetric("cloudfront_openDistribution");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_openStreamingDistribution", {
        /** Open a window to view the status of the CloudFront Streaming Distribution */
        get: function () {
            return this.getMetric("cloudfront_openStreamingDistribution");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_openInvalidationRequest", {
        /** Open a window to view the Cloudfront Invalidation requests */
        get: function () {
            return this.getMetric("cloudfront_openInvalidationRequest");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_deleteDistribution", {
        /** Called when user deletes a CloudFront Distribution */
        get: function () {
            return this.getMetric("cloudfront_deleteDistribution");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_deleteStreamingDistribution", {
        /** Called when user deletes a CloudFront Streaming Distribution */
        get: function () {
            return this.getMetric("cloudfront_deleteStreamingDistribution");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_createDistribution", {
        /** Create a CloudFront Distribution */
        get: function () {
            return this.getMetric("cloudfront_createDistribution");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudfront_createStreamingDistribution", {
        /** Create a CloudFront Streaming Distribution */
        get: function () {
            return this.getMetric("cloudfront_createStreamingDistribution");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_copyArn", {
        /** Copy the ARN of a CloudWatch Logs entity */
        get: function () {
            return this.getMetric("cloudwatchlogs_copyArn");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_open", {
        /** Open a CloudWatch Logs entity. ServiceType and source indicate where the request came from (example: while viewing an ECS container) */
        get: function () {
            return this.getMetric("cloudwatchlogs_open");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_openGroup", {
        /** Open the CloudWatch Logs group window. ServiceType indicates that it was opened from a different service (like directly from an ECS container) (Deprecated - use cloudwatchlogs_open) */
        get: function () {
            return this.getMetric("cloudwatchlogs_openGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_openStream", {
        /** Open a CloudWatch Logs stream in the window. ServiceType indicates that it was opened from a different service (like directly from an ECS container) (Deprecated - use cloudwatchlogs_open) */
        get: function () {
            return this.getMetric("cloudwatchlogs_openStream");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_delete", {
        /** Delete a CloudWatch Logs entity. */
        get: function () {
            return this.getMetric("cloudwatchlogs_delete");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_download", {
        /** Download a CloudWatch Logs entity. Value indicates the final size of the formatted stream in bytes. */
        get: function () {
            return this.getMetric("cloudwatchlogs_download");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_downloadStreamToFile", {
        /** Download a stream to a file on disk. Value indicates the final size of the formatted stream. (Deprecated - use cloudwatchlogs_download) */
        get: function () {
            return this.getMetric("cloudwatchlogs_downloadStreamToFile");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_openStreamInEditor", {
        /** Download a stream to memory then open in an editor. */
        get: function () {
            return this.getMetric("cloudwatchlogs_openStreamInEditor");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_viewCurrentMessagesInEditor", {
        /** Copy the currently open (possibly filtered) messages to an editor */
        get: function () {
            return this.getMetric("cloudwatchlogs_viewCurrentMessagesInEditor");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_wrapEvents", {
        /** Word wrap events off/on */
        get: function () {
            return this.getMetric("cloudwatchlogs_wrapEvents");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_tailStream", {
        /** Tail stream off/on */
        get: function () {
            return this.getMetric("cloudwatchlogs_tailStream");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_refresh", {
        /** Refresh a CloudWatch Logs entity */
        get: function () {
            return this.getMetric("cloudwatchlogs_refresh");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_refreshGroup", {
        /** Refresh group is pressed (Deprecated, use cloudwatchlogs_refresh) */
        get: function () {
            return this.getMetric("cloudwatchlogs_refreshGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_refreshStream", {
        /** Refresh stream is pressed (Deprecated, use cloudwatchlogs_refresh) */
        get: function () {
            return this.getMetric("cloudwatchlogs_refreshStream");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_filter", {
        /** Filters a CloudWatch Logs entity. */
        get: function () {
            return this.getMetric("cloudwatchlogs_filter");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_searchStream", {
        /** Called when a stream is searched */
        get: function () {
            return this.getMetric("cloudwatchlogs_searchStream");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_searchGroup", {
        /** Called when a group is searched */
        get: function () {
            return this.getMetric("cloudwatchlogs_searchGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchlogs_showEventsAround", {
        /** Show event around a time period in ms specified by Value */
        get: function () {
            return this.getMetric("cloudwatchlogs_showEventsAround");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudformation_createProject", {
        /** Called when creating a CloudFormation project */
        get: function () {
            return this.getMetric("cloudformation_createProject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudformation_deploy", {
        /** Called when deploying a CloudFormation template */
        get: function () {
            return this.getMetric("cloudformation_deploy");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudformation_publishWizard", {
        /** Called when user completes the CloudFormation template publish wizard */
        get: function () {
            return this.getMetric("cloudformation_publishWizard");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudformation_open", {
        /** Open a CloudFormation stack in the stack viewer */
        get: function () {
            return this.getMetric("cloudformation_open");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecommit_cloneRepo", {
        /** A repo is cloned from CodeCommit */
        get: function () {
            return this.getMetric("codecommit_cloneRepo");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecommit_createRepo", {
        /** A repo is created in CodeCommit */
        get: function () {
            return this.getMetric("codecommit_createRepo");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecommit_setCredentials", {
        /** A connection is established to CodeCommit to perform actions on repos */
        get: function () {
            return this.getMetric("codecommit_setCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamodb_createTable", {
        /** Create a DynamoDB table */
        get: function () {
            return this.getMetric("dynamodb_createTable");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamodb_deleteTable", {
        /** Delete a DynamoDB table */
        get: function () {
            return this.getMetric("dynamodb_deleteTable");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamodb_edit", {
        /** Modify a DynamoDB entity */
        get: function () {
            return this.getMetric("dynamodb_edit");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamodb_fetchRecords", {
        /** Fetch records from a DynamoDB table in the table browser */
        get: function () {
            return this.getMetric("dynamodb_fetchRecords");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamodb_openTable", {
        /** Open a DynamoDB table in the table browser */
        get: function () {
            return this.getMetric("dynamodb_openTable");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamodb_view", {
        /** View a DynamoDB entity */
        get: function () {
            return this.getMetric("dynamodb_view");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_changeState", {
        /** Change the state of an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_changeState");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_clearPrivateKey", {
        /** Remove the private key of an EC2 Key Pair from internal storage */
        get: function () {
            return this.getMetric("ec2_clearPrivateKey");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_connectToInstance", {
        /** Perform a connection to an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_connectToInstance");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_copyAmiToRegion", {
        /** Copy AMI image to another region */
        get: function () {
            return this.getMetric("ec2_copyAmiToRegion");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_createAmi", {
        /** Create an image from an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_createAmi");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_createElasticIp", {
        /** Create (allocate) an Elastic IP address */
        get: function () {
            return this.getMetric("ec2_createElasticIp");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_createKeyPair", {
        /** Create an EC2 Key Pair */
        get: function () {
            return this.getMetric("ec2_createKeyPair");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_createSecurityGroup", {
        /** Create an EC2 security group */
        get: function () {
            return this.getMetric("ec2_createSecurityGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_createSnapshot", {
        /** Create an EC2 volume snapshot */
        get: function () {
            return this.getMetric("ec2_createSnapshot");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_createVolume", {
        /** Create an EC2 volume */
        get: function () {
            return this.getMetric("ec2_createVolume");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_deleteAmi", {
        /** Delete (de-register) an AMI image */
        get: function () {
            return this.getMetric("ec2_deleteAmi");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_deleteElasticIp", {
        /** Delete (release) an Elastic IP address */
        get: function () {
            return this.getMetric("ec2_deleteElasticIp");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_deleteKeyPair", {
        /** Delete an EC2 Key Pair */
        get: function () {
            return this.getMetric("ec2_deleteKeyPair");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_deleteSecurityGroup", {
        /** Delete an EC2 security group */
        get: function () {
            return this.getMetric("ec2_deleteSecurityGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_deleteSnapshot", {
        /** Delete an EC2 Volume Snapshot */
        get: function () {
            return this.getMetric("ec2_deleteSnapshot");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_deleteVolume", {
        /** Delete an EC2 Volume */
        get: function () {
            return this.getMetric("ec2_deleteVolume");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editAmiPermission", {
        /** Edit AMI image permissions */
        get: function () {
            return this.getMetric("ec2_editAmiPermission");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editInstanceElasticIp", {
        /** Associate or disassociate an Elastic IP with an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_editInstanceElasticIp");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editInstanceShutdownBehavior", {
        /** Adjust the shutdown behavior of an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_editInstanceShutdownBehavior");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editInstanceTerminationProtection", {
        /** Adjust the termination protection of an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_editInstanceTerminationProtection");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editInstanceType", {
        /** Adjust the instance type of an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_editInstanceType");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editInstanceUserData", {
        /** Adjust an EC2 Instance's user data */
        get: function () {
            return this.getMetric("ec2_editInstanceUserData");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editSecurityGroupPermission", {
        /** Alter an EC2 security group permission */
        get: function () {
            return this.getMetric("ec2_editSecurityGroupPermission");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_editVolumeAttachment", {
        /** Attach (enabled = true) or detach a volume */
        get: function () {
            return this.getMetric("ec2_editVolumeAttachment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_exportPrivateKey", {
        /** Save the private key of an EC2 Key Pair out to disk */
        get: function () {
            return this.getMetric("ec2_exportPrivateKey");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_importPrivateKey", {
        /** Store the private key of an EC2 Key Pair in internal storage */
        get: function () {
            return this.getMetric("ec2_importPrivateKey");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_launchInstance", {
        /** Launch an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_launchInstance");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_openInstances", {
        /** Open a window to view EC2 Instances */
        get: function () {
            return this.getMetric("ec2_openInstances");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_openAMIs", {
        /** Open a window to view EC2 AMIs */
        get: function () {
            return this.getMetric("ec2_openAMIs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_openElasticIPs", {
        /** Open a window to view EC2 Elastic IPs */
        get: function () {
            return this.getMetric("ec2_openElasticIPs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_openKeyPairs", {
        /** Open to view EC2 Key pairs */
        get: function () {
            return this.getMetric("ec2_openKeyPairs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_openSecurityGroups", {
        /** Open a window to view EC2 Security Groups */
        get: function () {
            return this.getMetric("ec2_openSecurityGroups");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_openVolumes", {
        /** Open a window to view EC2 Volumes */
        get: function () {
            return this.getMetric("ec2_openVolumes");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_viewInstanceSystemLog", {
        /** View the system log of an EC2 Instance */
        get: function () {
            return this.getMetric("ec2_viewInstanceSystemLog");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_openCluster", {
        /** Open to view status of an ECS Cluster */
        get: function () {
            return this.getMetric("ecs_openCluster");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ec2_viewInstanceUserData", {
        /** View an EC2 Instance's user data */
        get: function () {
            return this.getMetric("ec2_viewInstanceUserData");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_enableExecuteCommand", {
        /** Called when ECS execute command is enabled */
        get: function () {
            return this.getMetric("ecs_enableExecuteCommand");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_disableExecuteCommand", {
        /** Called when ECS execute command is disabled */
        get: function () {
            return this.getMetric("ecs_disableExecuteCommand");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_runExecuteCommand", {
        /** Called when the ECS execute command is run */
        get: function () {
            return this.getMetric("ecs_runExecuteCommand");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecr_copyRepositoryUri", {
        /** Called when the user copies the repository uri from a node */
        get: function () {
            return this.getMetric("ecr_copyRepositoryUri");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecr_copyTagUri", {
        /** Called when the user copies the repository tag uri from a node. The tag uri is the repository uri + : + the tag name */
        get: function () {
            return this.getMetric("ecr_copyTagUri");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecr_createRepository", {
        /** Called when creating a new ECR repository */
        get: function () {
            return this.getMetric("ecr_createRepository");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecr_deleteRepository", {
        /** Called when deleting an existing ECR repository */
        get: function () {
            return this.getMetric("ecr_deleteRepository");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecr_deleteTags", {
        /** Called when deleting a tag in an ECR repository. The operation is a batch operation by default, value represents the number of tags deleted. */
        get: function () {
            return this.getMetric("ecr_deleteTags");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecr_deployImage", {
        /** Called when deploying an image to ECR */
        get: function () {
            return this.getMetric("ecr_deployImage");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_deployScheduledTask", {
        /** Called when deploying a scheduled task to an ECS cluster */
        get: function () {
            return this.getMetric("ecs_deployScheduledTask");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_deployService", {
        /** Called when deploying a service to an ECS cluster */
        get: function () {
            return this.getMetric("ecs_deployService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_deployTask", {
        /** Called when deploying a task to an ECS cluster */
        get: function () {
            return this.getMetric("ecs_deployTask");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_publishWizard", {
        /** Called when user completes the ECS publish wizard */
        get: function () {
            return this.getMetric("ecs_publishWizard");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_openRepository", {
        /** Open to view status of an ECS Repository */
        get: function () {
            return this.getMetric("ecs_openRepository");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_deleteService", {
        /** Called when user deletes an ECS service */
        get: function () {
            return this.getMetric("ecs_deleteService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_editService", {
        /** Edit configuration of an ECS service */
        get: function () {
            return this.getMetric("ecs_editService");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_deleteCluster", {
        /** Delete an ECS cluster */
        get: function () {
            return this.getMetric("ecs_deleteCluster");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_stopTask", {
        /** Stop ECS task(s) */
        get: function () {
            return this.getMetric("ecs_stopTask");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ecs_deleteScheduledTask", {
        /** Delete ECS Scheduled task(s) */
        get: function () {
            return this.getMetric("ecs_deleteScheduledTask");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "feedback_result", {
        /** Called while submitting in-IDE feedback */
        get: function () {
            return this.getMetric("feedback_result");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "file_editAwsFile", {
        /** Use authoring features such as autocompletion, syntax checking, and highlighting, for AWS filetypes (CFN, SAM, etc.). Emit this _once_ per file-editing session for a given file. Ideally this is emitted only if authoring features are used, rather than merely opening or touching a file. */
        get: function () {
            return this.getMetric("file_editAwsFile");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_openRole", {
        /** Open a window to view/edit IAM Role Policy */
        get: function () {
            return this.getMetric("iam_openRole");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_openGroup", {
        /** Open a window to view/edit IAM Group Policy */
        get: function () {
            return this.getMetric("iam_openGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_openUser", {
        /** Open a window to view/edit IAM User Configuration */
        get: function () {
            return this.getMetric("iam_openUser");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_open", {
        /** Open a window to view/edit an IAM resource */
        get: function () {
            return this.getMetric("iam_open");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_create", {
        /** Create an IAM resource */
        get: function () {
            return this.getMetric("iam_create");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_delete", {
        /** Delete an IAM resource */
        get: function () {
            return this.getMetric("iam_delete");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_edit", {
        /** Edits policy/configuration associated with an IAM resource */
        get: function () {
            return this.getMetric("iam_edit");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_createUserAccessKey", {
        /** Create Access Key for an IAM user */
        get: function () {
            return this.getMetric("iam_createUserAccessKey");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "iam_deleteUserAccessKey", {
        /** Delete Access Key for an IAM user */
        get: function () {
            return this.getMetric("iam_deleteUserAccessKey");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_delete", {
        /** called when deleting lambdas remotely */
        get: function () {
            return this.getMetric("lambda_delete");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_configure", {
        /** Called when opening the local configuration of a Lambda to edit */
        get: function () {
            return this.getMetric("lambda_configure");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_create", {
        /** Called when creating lambdas remotely */
        get: function () {
            return this.getMetric("lambda_create");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_createProject", {
        /** Called when creating a lambda project */
        get: function () {
            return this.getMetric("lambda_createProject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_goToHandler", {
        /** Jump to a lambda handler from elsewhere */
        get: function () {
            return this.getMetric("lambda_goToHandler");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_editFunction", {
        /** Called when creating lambdas remotely */
        get: function () {
            return this.getMetric("lambda_editFunction");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_invokeRemote", {
        /** Called when invoking lambdas remotely */
        get: function () {
            return this.getMetric("lambda_invokeRemote");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_invokeLocal", {
        /** Called when invoking lambdas locally (with SAM in most toolkits) */
        get: function () {
            return this.getMetric("lambda_invokeLocal");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_import", {
        /** Called when importing a remote Lambda function */
        get: function () {
            return this.getMetric("lambda_import");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_updateFunctionCode", {
        /** Called when updating a Lambda function's code outside the context of a SAM template */
        get: function () {
            return this.getMetric("lambda_updateFunctionCode");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_deploy", {
        /** Called when deploying a Lambda Function */
        get: function () {
            return this.getMetric("lambda_deploy");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "lambda_publishWizard", {
        /** Called when user completes the Lambda publish wizard */
        get: function () {
            return this.getMetric("lambda_publishWizard");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudformation_delete", {
        /** Called when deleting a cloudformation stack */
        get: function () {
            return this.getMetric("cloudformation_delete");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_getCredentials", {
        /** Called when getting IAM/SecretsManager credentials for a RDS database. Value represents how long it takes in ms. */
        get: function () {
            return this.getMetric("rds_getCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_openInstances", {
        /** Open a window to view RDS DB Instances */
        get: function () {
            return this.getMetric("rds_openInstances");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_openSecurityGroups", {
        /** Open a window to view RDS Security Groups */
        get: function () {
            return this.getMetric("rds_openSecurityGroups");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_openSubnets", {
        /** Open a window to view RDS Subnet Groups */
        get: function () {
            return this.getMetric("rds_openSubnets");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_launchInstance", {
        /** Launch a RDS DB instance */
        get: function () {
            return this.getMetric("rds_launchInstance");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_createSecurityGroup", {
        /** Create a RDS security group */
        get: function () {
            return this.getMetric("rds_createSecurityGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_createSubnetGroup", {
        /** Create a RDS subnet group */
        get: function () {
            return this.getMetric("rds_createSubnetGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_deleteInstance", {
        /** Delete a RDS DB instance */
        get: function () {
            return this.getMetric("rds_deleteInstance");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_deleteSecurityGroup", {
        /** Delete RDS security group(s) */
        get: function () {
            return this.getMetric("rds_deleteSecurityGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_deleteSubnetGroup", {
        /** Delete RDS subnet group(s) */
        get: function () {
            return this.getMetric("rds_deleteSubnetGroup");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "rds_createConnectionConfiguration", {
        /** Called when creating a new database connection configuration to for a RDS database. In Datagrip we do not get this infromation if it is created directly, so this is only counts actions. */
        get: function () {
            return this.getMetric("rds_createConnectionConfiguration");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "redshift_getCredentials", {
        /** Called when getting IAM/SecretsManager credentials for a Redshift database. Value represents how long it takes in ms. */
        get: function () {
            return this.getMetric("redshift_getCredentials");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "redshift_createConnectionConfiguration", {
        /** Called when creating a new database connection configuration to for a Redshift database. In Datagrip we do not get this infromation if it is created directly, so this only counts actions. */
        get: function () {
            return this.getMetric("redshift_createConnectionConfiguration");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sam_deploy", {
        /** Called when deploying a SAM application */
        get: function () {
            return this.getMetric("sam_deploy");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sam_sync", {
        /** Called when syncing a SAM application */
        get: function () {
            return this.getMetric("sam_sync");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sam_init", {
        /** Called when initing a SAM application */
        get: function () {
            return this.getMetric("sam_init");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "schemas_view", {
        /** Called when selecting an EventBridge schema to view */
        get: function () {
            return this.getMetric("schemas_view");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "schemas_download", {
        /** Called when downloading an EventBridge schema */
        get: function () {
            return this.getMetric("schemas_download");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "schemas_search", {
        /** Called when searching an EventBridge schema registry */
        get: function () {
            return this.getMetric("schemas_search");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "session_start", {
        /** Called when starting the plugin */
        get: function () {
            return this.getMetric("session_start");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "session_end", {
        /** Called when stopping the IDE on a best effort basis */
        get: function () {
            return this.getMetric("session_end");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_copyBucketName", {
        /** Copy the bucket name to the clipboard */
        get: function () {
            return this.getMetric("s3_copyBucketName");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_copyPath", {
        /** Copy the path of a S3 object to the clipboard */
        get: function () {
            return this.getMetric("s3_copyPath");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_copyUri", {
        /** Copy the S3 URI of a S3 object to the clipboard (e.g. s3://<bucketName>/abc.txt) */
        get: function () {
            return this.getMetric("s3_copyUri");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_copyUrl", {
        /** Copy the URL of a S3 object to the clipboard */
        get: function () {
            return this.getMetric("s3_copyUrl");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_createBucket", {
        /** Create a S3 bucket */
        get: function () {
            return this.getMetric("s3_createBucket");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_deleteBucket", {
        /** Delete a S3 bucket */
        get: function () {
            return this.getMetric("s3_deleteBucket");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_deleteObject", {
        /** Delete S3 object(s) */
        get: function () {
            return this.getMetric("s3_deleteObject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_createFolder", {
        /** Create an S3 folder */
        get: function () {
            return this.getMetric("s3_createFolder");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_downloadObject", {
        /** Download S3 object(s) */
        get: function () {
            return this.getMetric("s3_downloadObject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_downloadObjects", {
        /** Download multiple S3 objects */
        get: function () {
            return this.getMetric("s3_downloadObjects");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_uploadObject", {
        /** Upload S3 object(s) */
        get: function () {
            return this.getMetric("s3_uploadObject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_renameObject", {
        /** Rename a single S3 object */
        get: function () {
            return this.getMetric("s3_renameObject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_uploadObjects", {
        /** Upload multiple S3 objects */
        get: function () {
            return this.getMetric("s3_uploadObjects");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_openEditor", {
        /** Open a view of a S3 bucket */
        get: function () {
            return this.getMetric("s3_openEditor");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_editObject", {
        /** Edit or view one or more S3 objects in the IDE */
        get: function () {
            return this.getMetric("s3_editObject");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_openBucketProperties", {
        /** Open a window to view S3 bucket properties */
        get: function () {
            return this.getMetric("s3_openBucketProperties");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "s3_openMultipartUpload", {
        /** Open a window to view S3 Multipart upload */
        get: function () {
            return this.getMetric("s3_openMultipartUpload");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "toolkit_init", {
        /** The Toolkit has completed initialization */
        get: function () {
            return this.getMetric("toolkit_init");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "toolkit_viewLogs", {
        /** View logs for the toolkit */
        get: function () {
            return this.getMetric("toolkit_viewLogs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_openQueue", {
        /** Open an SQS queue. Initially opens to either the send message pane or poll messages pane. */
        get: function () {
            return this.getMetric("sqs_openQueue");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_createQueue", {
        /** Create a new SQS queue */
        get: function () {
            return this.getMetric("sqs_createQueue");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_sendMessage", {
        /** Send a message to an SQS queue */
        get: function () {
            return this.getMetric("sqs_sendMessage");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_deleteMessages", {
        /** Delete one or more messages from an SQS queue. Value indicates the number of messages that we tried to delete. */
        get: function () {
            return this.getMetric("sqs_deleteMessages");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_subscribeSns", {
        /** Subscribe the queue to messages from an sns topic */
        get: function () {
            return this.getMetric("sqs_subscribeSns");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_configureLambdaTrigger", {
        /** Configure the queue as a trigger for a Lambda */
        get: function () {
            return this.getMetric("sqs_configureLambdaTrigger");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_editQueueParameters", {
        /** Edit the Queue parameters */
        get: function () {
            return this.getMetric("sqs_editQueueParameters");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_purgeQueue", {
        /** Purge all messages from the queue */
        get: function () {
            return this.getMetric("sqs_purgeQueue");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sqs_deleteQueue", {
        /** Called when user deletes a SQS queue */
        get: function () {
            return this.getMetric("sqs_deleteQueue");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_createTopic", {
        /** Create a SNS Topic */
        get: function () {
            return this.getMetric("sns_createTopic");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_createSubscription", {
        /** Create a SNS Subscription */
        get: function () {
            return this.getMetric("sns_createSubscription");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_openTopic", {
        /** Open a window to view details of SNS Topic */
        get: function () {
            return this.getMetric("sns_openTopic");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_openSubscriptions", {
        /** Open a window to view SNS Subscriptions */
        get: function () {
            return this.getMetric("sns_openSubscriptions");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_deleteTopic", {
        /** Called when user deletes a SNS Topic */
        get: function () {
            return this.getMetric("sns_deleteTopic");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_deleteSubscription", {
        /** Called when user deletes SNS subscription(s) */
        get: function () {
            return this.getMetric("sns_deleteSubscription");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sns_publishMessage", {
        /** Publish message to a SNS topic */
        get: function () {
            return this.getMetric("sns_publishMessage");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vpc_openRouteTables", {
        /** Open a window to view VPC RouteTable */
        get: function () {
            return this.getMetric("vpc_openRouteTables");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vpc_openGateways", {
        /** Open a window to view VPC Internet Gateway */
        get: function () {
            return this.getMetric("vpc_openGateways");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vpc_openACLs", {
        /** Open a window to view VPC Network ACLs */
        get: function () {
            return this.getMetric("vpc_openACLs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vpc_openSubnets", {
        /** Open a window to view VPC Subnets */
        get: function () {
            return this.getMetric("vpc_openSubnets");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vpc_openVPCs", {
        /** Open a window to view VPC details */
        get: function () {
            return this.getMetric("vpc_openVPCs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchinsights_openEditor", {
        /** Open the insights query editor */
        get: function () {
            return this.getMetric("cloudwatchinsights_openEditor");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchinsights_executeQuery", {
        /** Start an insights query */
        get: function () {
            return this.getMetric("cloudwatchinsights_executeQuery");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchinsights_saveQuery", {
        /** Save query parameters to AWS */
        get: function () {
            return this.getMetric("cloudwatchinsights_saveQuery");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchinsights_retrieveQuery", {
        /** Retrieve list of available saved queries from AWS */
        get: function () {
            return this.getMetric("cloudwatchinsights_retrieveQuery");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cloudwatchinsights_openDetailedLogRecord", {
        /** Get all details for the selected log record */
        get: function () {
            return this.getMetric("cloudwatchinsights_openDetailedLogRecord");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "toolkit_getExternalResource", {
        /** The toolkit tried to retrieve blob data from a url */
        get: function () {
            return this.getMetric("toolkit_getExternalResource");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamicresource_getResource", {
        /** Open the dynamic resource model in the IDE */
        get: function () {
            return this.getMetric("dynamicresource_getResource");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamicresource_listResource", {
        /** Expand a Resource Type node */
        get: function () {
            return this.getMetric("dynamicresource_listResource");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamicresource_selectResources", {
        /** Change the list of available dynamic resources in the AWS Explorer */
        get: function () {
            return this.getMetric("dynamicresource_selectResources");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamicresource_copyIdentifier", {
        /** Copy the dynamic resource identifier */
        get: function () {
            return this.getMetric("dynamicresource_copyIdentifier");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "dynamicresource_mutateResource", {
        /** A dynamic resource mutation request completed */
        get: function () {
            return this.getMetric("dynamicresource_mutateResource");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_experimentActivation", {
        /** An experiment was activated or deactivated in the Toolkit */
        get: function () {
            return this.getMetric("aws_experimentActivation");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_toolInstallation", {
        /** An external tool was installed automatically */
        get: function () {
            return this.getMetric("aws_toolInstallation");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_modifySetting", {
        /** An setting was changed by users in the Toolkit. This metric can optionally provide the new state of the setting via settingState. */
        get: function () {
            return this.getMetric("aws_modifySetting");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ui_click", {
        /** User clicked/activated a UI element. This does not necessarily have to be an explicit mouse click. Any user action that has the same behavior as a mouse click can use this event. */
        get: function () {
            return this.getMetric("ui_click");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "deeplink_open", {
        /** User requested that a resource be opened in the browser using the deeplink service */
        get: function () {
            return this.getMetric("deeplink_open");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_codePercentage", {
        /** Percentage of user tokens against suggestions until 5 mins of time */
        get: function () {
            return this.getMetric("codewhisperer_codePercentage");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_securityScan", {
        /** Client side invocation of the CodeWhisperer Security Scan */
        get: function () {
            return this.getMetric("codewhisperer_securityScan");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_serviceInvocation", {
        /** Client side invocation of the CodeWhisperer service for suggestion */
        get: function () {
            return this.getMetric("codewhisperer_serviceInvocation");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_blockedInvocation", {
        /** Client side invocation blocked by another invocation in progress */
        get: function () {
            return this.getMetric("codewhisperer_blockedInvocation");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_userDecision", {
        /** User acceptance or rejection of each suggestion returned by the CodeWhisperer service request */
        get: function () {
            return this.getMetric("codewhisperer_userDecision");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_userTriggerDecision", {
        /** User decision aggregated at trigger level */
        get: function () {
            return this.getMetric("codewhisperer_userTriggerDecision");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_userModification", {
        /** Percentage of user modifications for the selected suggestion until a fixed period of time */
        get: function () {
            return this.getMetric("codewhisperer_userModification");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_perceivedLatency", {
        /** The duration from user last modification to the first recommendation shown in milliseconds */
        get: function () {
            return this.getMetric("codewhisperer_perceivedLatency");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codewhisperer_clientComponentLatency", {
        /** The latency from each CodeWhisperer components in milliseconds */
        get: function () {
            return this.getMetric("codewhisperer_clientComponentLatency");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecatalyst_createDevEnvironment", {
        /** Create an Amazon CodeCatalyst Dev Environment */
        get: function () {
            return this.getMetric("codecatalyst_createDevEnvironment");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecatalyst_updateDevEnvironmentSettings", {
        /** Update properties of a Amazon CodeCatalyst Dev Environment */
        get: function () {
            return this.getMetric("codecatalyst_updateDevEnvironmentSettings");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecatalyst_updateDevfile", {
        /** Trigger a devfile update on a Amazon CodeCatalyst dev environment */
        get: function () {
            return this.getMetric("codecatalyst_updateDevfile");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecatalyst_localClone", {
        /** Clone a Amazon CodeCatalyst code repository locally */
        get: function () {
            return this.getMetric("codecatalyst_localClone");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecatalyst_connect", {
        /** Connect to a Amazon CodeCatalyst dev environment */
        get: function () {
            return this.getMetric("codecatalyst_connect");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "codecatalyst_devEnvironmentWorkflowStatistic", {
        /** Workflow statistic for connecting to a dev environment */
        get: function () {
            return this.getMetric("codecatalyst_devEnvironmentWorkflowStatistic");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vscode_executeCommand", {
        /** Emitted whenever a registered Toolkit command is executed */
        get: function () {
            return this.getMetric("vscode_executeCommand");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ssm_createDocument", {
        /** An SSM Document is created locally */
        get: function () {
            return this.getMetric("ssm_createDocument");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ssm_deleteDocument", {
        /** An SSM Document is deleted */
        get: function () {
            return this.getMetric("ssm_deleteDocument");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ssm_executeDocument", {
        /** An SSM Document is deleted */
        get: function () {
            return this.getMetric("ssm_executeDocument");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ssm_openDocument", {
        /** An SSM Document is opened locally */
        get: function () {
            return this.getMetric("ssm_openDocument");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ssm_publishDocument", {
        /** SSM Document related metrics for create and update */
        get: function () {
            return this.getMetric("ssm_publishDocument");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "ssm_updateDocumentVersion", {
        /** SSM Document related metrics for updating document default version */
        get: function () {
            return this.getMetric("ssm_updateDocumentVersion");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "stepfunctions_createStateMachineFromTemplate", {
        /** */
        get: function () {
            return this.getMetric("stepfunctions_createStateMachineFromTemplate");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "stepfunctions_downloadStateMachineDefinition", {
        /** */
        get: function () {
            return this.getMetric("stepfunctions_downloadStateMachineDefinition");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "stepfunctions_executeStateMachine", {
        /** */
        get: function () {
            return this.getMetric("stepfunctions_executeStateMachine");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "stepfunctions_executeStateMachineView", {
        /** */
        get: function () {
            return this.getMetric("stepfunctions_executeStateMachineView");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "stepfunctions_previewstatemachine", {
        /** */
        get: function () {
            return this.getMetric("stepfunctions_previewstatemachine");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vscode_activeRegions", {
        /** Record the number of active regions at startup and when regions are added/removed */
        get: function () {
            return this.getMetric("vscode_activeRegions");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "vscode_viewLogs", {
        /** View the VSCode IDE logs */
        get: function () {
            return this.getMetric("vscode_viewLogs");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_showExplorerErrorDetails", {
        /** Called when getting more details about errors thrown by the explorer */
        get: function () {
            return this.getMetric("aws_showExplorerErrorDetails");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_showRegion", {
        /** Records a call to add a region to the explorer */
        get: function () {
            return this.getMetric("aws_showRegion");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "aws_hideRegion", {
        /** Records a call to remove a region from the explorer */
        get: function () {
            return this.getMetric("aws_hideRegion");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sam_detect", {
        /** Called when detecting the location of the SAM CLI */
        get: function () {
            return this.getMetric("sam_detect");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cdk_explorerDisabled", {
        /** Called when expanding the CDK explorer is disabled */
        get: function () {
            return this.getMetric("cdk_explorerDisabled");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cdk_explorerEnabled", {
        /** Called when the CDK explorer is enabled */
        get: function () {
            return this.getMetric("cdk_explorerEnabled");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cdk_appExpanded", {
        /** Called when the CDK explorer is expanded */
        get: function () {
            return this.getMetric("cdk_appExpanded");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cdk_provideFeedback", {
        /** Called when providing feedback for CDK */
        get: function () {
            return this.getMetric("cdk_provideFeedback");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cdk_help", {
        /** Called when clicking on help for CDK */
        get: function () {
            return this.getMetric("cdk_help");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "cdk_refreshExplorer", {
        /** Called when refreshing the CDK explorer */
        get: function () {
            return this.getMetric("cdk_refreshExplorer");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sam_attachDebugger", {
        /** Called after trying to attach a debugger to a local sam invoke */
        get: function () {
            return this.getMetric("sam_attachDebugger");
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TelemetryBase.prototype, "sam_openConfigUi", {
        /** Called after opening the SAM Config UI */
        get: function () {
            return this.getMetric("sam_openConfigUi");
        },
        enumerable: false,
        configurable: true
    });
    return TelemetryBase;
}());
exports.TelemetryBase = TelemetryBase;
//# sourceMappingURL=telemetry.gen.js.map