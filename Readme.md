# MQTT Publish Program using AWS Lambda
I study MQTT Publish and Subscribe.
Now I use AWS Lambda and AWS IoT, and I send the message using MQTT Publish.

# Requirement
- Python 3.6
- MQTT Library(paho-mqtt)(https://qiita.com/areaz_/items/d488fb948de090a7b4c8)
- Certification of AWS IoT(https://qiita.com/areaz_/items/d488fb948de090a7b4c8)

# Change point of lambda_mqtt_publish.py

# Lambda settings
Please make the file of "lambda.json" with reference to the following information.

```
{
  "name": "MQTT_Publisher_using_AWS_Lambda"
  "description": "AWS Lambda is published to AWS IoT using MQTT"
  "region": <<Region>>
  "handler": "lambda-mqtt-subscribe.main"
  "role": <<IAM Role for AWS Lambda>>
  "timeout": 300,
  "memory": 128
}
```

|Item|Description|
|-----|-----|
|<<Region>>|[Watch AWS Document](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions)|
|<<IAM Role for AWS Lambda>>|Please write AWSLambdaBasicExecutionRole on your AWS Account|

# Test Execute

# Upload the Lambda Function

