# CloudEventProcessor
Python VS Code system that processes files in S3, logs events in DynamoDB, and sends notifications via SNS. Integrates AWS Lambda, CloudWatch, and EC2.

Files are uploaded to S3 from Python with VS Code.
The lambda is coded so that every time a file is uploaded, it enters the DynamoDB database and creates an alert that can be seen in CloudWatch or in the email via SNS.
