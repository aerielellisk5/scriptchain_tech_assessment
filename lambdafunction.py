# write a sample package configuration in python to build an AWS lambda function
import boto3

client = boto3.client('lambda')

response = client.create_fucntion(
    FucntionName = "tech_assessment",
    Role = ARN, #this should be the ARN for the role created for this function
    Handler = 'lambda_function.lambda_handler',
    Runtimes='python3.10',
    Code={
        # zipfile or s3 bucket
        'S3Bucket': 'mytechassessments3bucket'
    }
    
)