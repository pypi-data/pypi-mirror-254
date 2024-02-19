# SMS Message AWS Local Python Package

A Python package for sending SMS messages using AWS Simple Notification Service (SNS).

## Installation

You can install this package using pip:

```bash
pip install sms-message-aws-sns-local
```

## Usage

To send an SMS message using this package, you can use the following code snippet:

```py
from sms_aws_local_python_package.SendAwsSms import SmsMessageAwsSns

phone_number = "+1234567890"  # Replace with the recipient's phone number
message = "Hello, this is an SMS message from AWS SNS!"

message_id = SmsMessageAwsSns().send(phone_number, message)
if message_id:
    print(f"SMS sent successfully. Message ID: {message_id}")
else:
    print("Failed to send SMS.")
# Replace +1234567890 with the recipient's phone number and customize the message variable as needed.
```

## Configuration

Before using the package, make sure to configure your AWS credentials.  
You can do this using AWS CLI or by setting environment variables:

```
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=your_aws_region
```
