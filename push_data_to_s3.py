import boto3, argparse

# Input parameters
parser = argparse.ArgumentParser()
parser.add_argument("-file_path", "--file_path", help="path off the file to push to s3")
parser.add_argument("-bucket_name", "--bucket_name", help="name of s3 bucket")
parser.add_argument("-aws_profile", "--aws_profile", help="profile name of the aws configuration / credentials")

args = parser.parse_args()
file_path = args.file_path
bucket_name = args.bucket_name
aws_profile = args.aws_profile

# Create session and connect to s3 resource
session = boto3.Session(profile_name=aws_profile)
s3 = session.resource('s3')

# Upload the file
data = open(file_path, 'rb')
file_name = os.path.basename(file_path)
s3.Bucket(bucket_name).put_object(Key=file_name, Body=data)

