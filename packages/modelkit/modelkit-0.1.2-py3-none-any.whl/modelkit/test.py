import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("clustree-training-anonymous")
bucket.upload_file(__file__, "toto")
