# CloudEventProcessor
Python VS Code system that processes files in S3, logs events in DynamoDB, and sends notifications via SNS. Integrates AWS Lambda, CloudWatch, and EC2.

Files are uploaded to S3 from Python with VS Code. [S3 Script](subir_s3.py) ![S3](S3.png)

The lambda is coded so that every time a file is uploaded, it enters the DynamoDB database and creates an alert: [Lambda Script](lambda_function.py) ![DynamoDB](DynamoDB.png)

That can be seen in CloudWatch: ![Cloud Watch1](CloudWatch1.png)

![Cloud Watch2](CloudWatch2.png)

Or in the email via SNS: ![Gmail](Gmail.png)

An EC2 was configured to independently run the Python scripts that interact with S3 and view the files it contains: [EC2 Script](EC2.py) 
-
![EC2](EC2.png)


