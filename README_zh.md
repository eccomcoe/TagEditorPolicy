使用Tag来标记管理AWS云上资源是一项最佳实践，但是在大规模环境中管理Tag又是一个非常具有挑战的工作，尤其是对于AWS上百种资源类型，每种类型的Tag操作都有所不同。因此AWS提供了Tag Editor工具来帮助用户完成这一工作, Tag Editor支持常见的140多种AWS资源类型，避免了要通过不同的API管理资源Tag的困扰，是非常强大的工具。
通过Tag Editor来管理AWS资源Tag，除了需要TagEditor本身的权限以外，还需要被管理的AWS服务资源类型对应的Tag操作API，比如要给Amazon EC2实例添加标签，就需要Amazon EC2的CreateTags操作权限，详见：https://docs.aws.amazon.com/tag-editor/latest/userguide/gettingstarted.html
然而AWS并没有提供一个IAM Managed Policy覆盖所有Tag Editor支持的资源类型，逐个服务查看API文档将是一个比较耗时的工程，因此特此将实际用到的AWS资源类型的Tag操作权限整理到这个代码仓库，共享给大家参考。

支持列表：
| 资源类型 |已包含在policy中|
| --- | --- |
| AWS Amplify |     |
| Amazon API Gateway |     |
| Amazon AppFlow |     |
| Amazon AppStream |     |
| AWS AppSync |     |
| AWS App Mesh |     |
| Amazon Athena |✔|
| AWS Audit Manager |     |
| Amazon Aurora |     |
| Auto Scaling |     |
| AWS Backup |     |
| AWS Batch |     |
| Amazon Braket |     |
| AWS Certificate Manager |✔|
| AWS Private Certificate Authority |     |
| AWS Cloud9 |     |
| Amazon Cloud Directory |     |
| AWS Cloud Map |     |
| AWS CloudFormation |     |
| Amazon CloudFront |     |
| AWS CloudHSM |     |
| AWS CloudTrail |     |
| Amazon CloudWatch (alarms only) |✔|
| Amazon CloudWatch Events |✔|
| Amazon CloudWatch Logs |✔|
| Amazon CloudWatch Synthetics |     |
| AWS CodeArtifact |     |
| AWS CodeBuild |✔|
| AWS CodeCommit |     |
| AWS CodeDeploy |     |
| Amazon CodeGuru Profiler |     |
| Amazon CodeGuru Reviewer |     |
| AWS CodePipeline |     |
| AWS CodeStar |     |
| AWS CodeStar Connections |     |
| Amazon Cognito Identity |     |
| Amazon Cognito user pools |     |
| Amazon Comprehend |     |
| AWS Config |     |
| Amazon Connect |     |
| AWS Data Exchange |     |
| Amazon Data Lifecycle Manager |     |
| AWS Data Pipeline |     |
| AWS Database Migration Service |     |
| AWS DataSync |     |
| AWS Device Farm |     |
| AWS Direct Connect |     |
| AWS Directory Service |     |
| Amazon DynamoDB |✔|
| Amazon Elastic Block Store (Amazon EBS) |     |
| Amazon Elastic Compute Cloud (Amazon EC2) |✔|
| EC2 Image Builder |     |
| Amazon Elastic Container Registry (Amazon ECR) |✔|
| Amazon Elastic Container Service (Amazon ECS) |✔|
| Amazon Elastic Kubernetes Service (Amazon EKS) |✔|
| Amazon Elastic Kubernetes Service (Amazon EKS) |     |
| Amazon Elastic File System (Amazon EFS) |✔|
| Elastic Load Balancing |✔|
| Amazon Elastic Inference |     |
| Amazon ElastiCache |✔|
| AWS Elemental MediaLive |     |
| AWS Elemental MediaPackage |     |
| AWS Elemental MediaPackage VoD |     |
| AWS Elemental MediaTailor |     |
| Amazon EMR |✔|
| Amazon EMR on EKS (EMR containers) |     |
| Amazon EventBridge Schema |     |
| AWS Firewall Manager |     |
| Amazon Forecast |     |
| Amazon Fraud Detector |     |
| Amazon FSx |     |
| Amazon GameLift |     |
| Amazon S3 Glacier |     |
| AWS Global Accelerator |     |
| AWS Ground Station |     |
| AWS Glue |     |
| Amazon GuardDuty |     |
| AWS Identity and Access Management (IAM) |✔|
| IAM Access Analyzer |     |
| Amazon Inspector |     |
| Amazon Interactive Video Service |     |
| AWS IoT Analytics |     |
| AWS IoT Core |     |
| AWS IoT Device Defender |     |
| AWS IoT Device Management |     |
| AWS IoT Events |     |
| AWS IoT Greengrass |     |
| AWS IoT 1-Click |     |
| AWS IoT SiteWise IoT Sitewise |     |
| AWS IoT Secure Tunneling |     |
| AWS IoT Things Graph |     |
| AWS IoT Wireless |     |
| Amazon Kendra |     |
| AWS Key Management Service (AWS KMS) |✔|
| Amazon Kinesis |     |
| Amazon Managed Service for Apache Flink |     |
| Amazon Kinesis Data Firehose |     |
| AWS Lambda |✔|
| Amazon Lex |     |
| AWS Marketplace |     |
| AWS License Manager |     |
| Amazon Lightsail |     |
| Amazon Macie |     |
| Amazon Machine Learning |     |
| Amazon Managed Blockchain |     |
| AWS Elemental MediaConnect |     |
| Amazon MQ |✔|
| Amazon Managed Streaming for Apache Kafka (Amazon MSK) |✔|
| Amazon Neptune |     |
| AWS Network Manager |     |
| Amazon OpenSearch Service |✔|
| AWS OpsWorks |     |
| AWS OpsWorks CM |     |
| AWS Organizations |     |
| AWS Outposts |     |
| Amazon Pinpoint |     |
| Amazon Quantum Ledger Database (Amazon QLDB) |     |
| Amazon Relational Database Service (Amazon RDS) |✔|
| Amazon Redshift |✔|
| AWS Resource Access Manager |     |
| AWS Resource Groups |     |
| AWS RoboMaker |     |
| Amazon Route 53 |     |
| Amazon Route 53 Resolver |     |
| Amazon Simple Storage Service (Amazon S3) (buckets only) |✔|
| Amazon SageMaker |✔|
| Savings Plans |     |
| AWS Secrets Manager |     |
| AWS Security Hub |     |
| Service Catalog |     |
| Service Quotas |     |
| Amazon Simple Email Service (Amazon SES) |     |
| Amazon Simple Notification Service (Amazon SNS) |✔|
| Amazon Simple Queue Service (Amazon SQS) |✔|
| Amazon Simple Workflow Service |     |
| AWS Step Functions |     |
| AWS Storage Gateway |     |
| AWS Systems Manager |     |
| AWS Transfer for FTP |     |
| Amazon Virtual Private Cloud (Amazon VPC) |     |
| AWS WAF |     |
| AWS WAF Regional |     |
| Amazon WorkSpaces |     |
| AWS X-Ray |     |
|     |     |

使用方法：
直接通过CloudFormation模板TagEditorPolicy.json部署，并在需要使用TagEditor的IAM user或IAM role关联即可。
或者可以将TagEditorPolicy.json合并到您自己的CloudFormation模板中。

欢迎您将用到的tag操作权限提交pull request合并进来。