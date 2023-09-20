## Intro:
Using tags to label and manage resources on AWS Cloud is a best practice, but managing tags in large-scale environments can be very challenging, especially for the hundreds of resource types on AWS, each with different tag operations. Therefore, AWS provides the Tag Editor tool to help users complete this task. Tag Editor supports over 140 common AWS resource types, avoiding the hassle of managing resource tags through different APIs and is a powerful tool.

To manage AWS resource tags with Tag Editor, in addition to the permissions required by TagEditor itself, you also need the corresponding tag operation API for the AWS service resource type being managed. For example, to add tags to an Amazon EC2 instance, you need the Amazon EC2 CreateTags operation permission. For more details, see: https://docs.aws.amazon.com/tag-editor/latest/userguide/gettingstarted.html

However, AWS does not provide an IAM Managed Policy that covers all resource types supported by Tag Editor, and checking the API documentation for each service would be a time-consuming process. Therefore, I have compiled the tag operation permissions for the AWS resource types actually used in this code repository and shared them with everyone for reference.

## Included resource types：
| resource types |Included in policy|
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

## Usage:

You can directly deploy the CloudFormation template TagEditorPolicy.json, and associate it with the IAM user or IAM role that needs to use TagEditor.
Alternatively, you can merge TagEditorPolicy.json into your own CloudFormation template.

You are welcome to submit a pull request to merge any tag operation permissions you have used.



