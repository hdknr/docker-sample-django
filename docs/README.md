# AWS

## 1.IAM

### IAM Role: Fargate (Task Role)


FargetFirehosePolicy:

~~~json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "firehose:PutRecordBatch",
            "Resource": "*"
        }
    ]
}
~~~

Trust Relationship: "Service" == `ecs-tasks.amazonaws.com`:

~~~json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
~~~

### IAM Role: ecsTaskExecutionRole(Task Execution Role)

ECS-SecretsManager-Permission:

- Sysmtem Manager Parameter Store (String / SecureString)

~~~json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "secretsmanager:GetSecretValue",
                "ssm:GetParameters"
            ],
            "Resource": [
                "arn:aws:kms:ap-northeast-1:{your-aws-id}:key/10d2672b-8fdf-46f5-a561-7614433ab6d9",
                "arn:aws:secretsmanager:*:{your-aws-id}:secret:*",
                "arn:aws:ssm:*:{your-aws-id}:parameter/*"
            ]
        }
    ]
}
~~~

## 2. S3: Bucket for Log files

- create S3 bucket:   `spinwp` 


## 3. Kinesis: Data Firehose delivery streams(Container -> S3)

- Name: `djdocker-s3`
- S3 Bucket: `spinwp`
- Prefix: `djdocker/`

## 4. ECR: Docker Repository

-  Private Repositry: `djdocker`
-  URI: `{your AWS ID}.dkr.ecr.ap-northeast-1.amazonaws.com/djdocker`


## 5. ECS: Cluster

-  `Networking` with `AWS Fargate`


### ECS: Task

- Name: `djdocker`
- Task Role: `Fargate`
- Network Mode: `awsvpc`
- Conpatibility: `Fargate`
- Task Execution Role: `ecsTaskExecutionRole`

Log Router:

- Firelens: True
- Type: `fluentbit`
- Image: `906394416424.dkr.ecr.ap-northeast-1.amazonaws.com/aws-for-fluent-bit:latest`

#### ECS Task: Container `djdocker`

- Name: `djdocker`
- Image: `{your AWS ID}.dkr.ecr.ap-northeast-1.amazonaws.com/djdocker`
- Memory: Soft 300MB
- Port Mapping: 

Storage Log:

- Logging: `awsfirelens`
- `delivery_stream`: `djdocker-s3`
- region: `ap-northeast-1`
- Name: `firehose`

