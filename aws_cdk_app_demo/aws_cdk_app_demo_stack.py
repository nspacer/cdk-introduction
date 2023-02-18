from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_sqs as sqs,
    aws_lambda as lambda_function,
    aws_ec2 as ec2,
    Duration
)
from constructs import Construct
import aws_cdk as cdk


class AwsCdkAppDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
            self, "AwsCdkAppDemoQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name="cdk_queue"
        )

        function = lambda_function.Function(
            self, "Democdkfunction",
            function_name="lambda_cdk",
            runtime=lambda_function.Runtime.PYTHON_3_9,
            code=lambda_function.Code.from_asset('./lambda_code_demo'),
            handler="demo_lambda.lambda_handler"
        )

        """
        vpc = ec2.Vpc.from_lookup(
            self,
            "vpc",
            vpc_id="vpc-01961b1baea92b32f",
        )
        server = cdk.aws_ec2.Instance(
            self,
            "ec2-instance",
            instance_name="demo-cdk-instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage().lookup(name="Amazon Linux 2 with letsencrypt fix"),
            vpc=vpc
        )
        """
        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True,
                           bucket_name="demo-bucket-name-beyond-the-cloud",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL
                           )
        """
        bucket2 = s3.Bucket(self, "MySecondBucket", versioned=True,
                           bucket_name="demo-bucket-name-beyond-the-cloud-766576576",
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           auto_delete_objects=True)
                           """
