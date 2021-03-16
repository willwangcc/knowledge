<h1 align="center">
<br>
	<a href="https://www.wikiwand.com/en/AWS_Lambda">
  <img src="https://i.imgur.com/HKyTpmg.png" alt="AWS lambda use case" width=42%">
  </a>
  <br><br>
AWS Lambda 
  <br><br>
</h1>


> Run code without thinking about servers. Pay only for the compute time you consume. [[AWS](https://aws.amazon.com/lambda/)]


## Why 

AWS Lambda lets you run code without provisioning or **managing servers**. You **pay only for the compute time** you consume.

With Lambda, 

* you can run code for virtually any type of application or backend service - all with **zero administration**. 
* Just upload your code and Lambda takes care of everything required to run and **scale your code with high availability**. 
* You can set up your code to automatically **trigger** from other AWS services or call it directly from any web or mobile app.

## How 

* [How AWS Lambda Works?](https://insisivecloud.io/blogs/aws/how-to-get-the-ball-rolling-with-aws-lambda)
* [The Ultimate Guide](https://www.serverless.com/aws-lambda)

### Use Case 

* ✅ DO: use it as a **plugin** for other AWS services. For example for processing **image** after uploading to S3 or send alert after a regex trigger on Cloudwatch(AWS logging service).
* 👎 DO NOT: use AWS Lambda as a **gernal EC2 host**. 
* ⚠️ LIMITATION: If you need to access a "State" for exmaple by connecting to DynamoDB, it can get very expensive. 

## What

### Overview

AWS Lambda is an **event-driven**, **serverless** computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced in November 2014.

The purpose of Lambda, as compared to **AWS EC2**, is to simplify building **smaller, on-demand applications that are responsive to events and new information**. AWS targets starting a Lambda instance within milliseconds of an event. Node.js, Python, Java, Go, Ruby, and C# (through .NET Core) are all officially supported as of 2018. In late 2018, custom runtime support was added to AWS Lambda, giving developers the ability to run a Lambda in the language of their choice.

AWS Lambda supports securely running native Linux executables via calling out from a supported runtime such as Node.js. For example, Haskell code can be run on Lambda.

AWS Lambda was designed for use cases such as **image or object uploads to Amazon S3**, updates to **DynamoDB** tables, responding to website clicks or reacting to sensor readings from an IoT connected device. AWS Lambda can also be used to automatically provision back-end services triggered by custom HTTP requests, and "spin down" such services when not in use, to save resources. These custom HTTP requests are configured in AWS API Gateway, which can also handle authentication and authorization in conjunction with AWS Cognito.

Unlike Amazon EC2, which is priced by the hour but metered by the second, AWS Lambda is metered in increments of 100 milliseconds. Usage amounts below a documented threshold fall within the AWS Lambda free tier - which does not expire 12 months after account signup, unlike the free tier for other AWS services.

In 2019, at AWS' annual cloud computing conference (AWS re:Invent), the AWS Lambda team announced "Provisioned Concurrency", a feature that "keeps functions initialized and hyper-ready to respond in double-digit milliseconds." The Lambda team described Provisioned Concurrency as "ideal for implementing interactive services, such as web and mobile backends, latency-sensitive microservices, or synchronous APIs."


### Glossary

* **plug-in**: In computing, a plug-in (or plugin, add-in, addin, add-on, or addon) is a software **component** that adds a specific **feature** to an existing computer program. When a program supports plug-ins, it enables **customization**.
* **EC2**: Amazon Elastic Compute Cloud (Amazon EC2) is a web **service** that provides secure, **resizable** compute **capacity** in the cloud. 
* **DynamoDB**: Amazon DynamoDB is a **key-value** and **document** database that delivers **single-digit millisecond** performance at any **scale**. 

## FAQs

### Q: What is evolution of AWS Lambda?

A: AWS Lambda sparked the rise of serverless computing in the cloud. Explore how the function-as-a-service platform developed over time with this [infographic](https://searchcloudcomputing.techtarget.com/infographic/Follow-the-evolution-of-AWS-Lambda).

