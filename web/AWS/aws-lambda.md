# Lambda


![lambda](https://i.imgur.com/m9LzODV.png)

> Run code without thinking about servers. Pay only for the compute time you consume. 
> 
> -- [AWS](https://aws.amazon.com/lambda/)


## Why 

AWS Lambda lets you run code without provisioning or **managing servers**. You **pay only for the compute time** you consume.

With Lambda, 

* you can run code for virtually any type of application or backend service - all with **zero administration**. 
* Just upload your code and Lambda takes care of everything required to run and **scale your code with high availability**. 
* You can set up your code to automatically **trigger** from other AWS services or call it directly from any web or mobile app.

## What

* **plug-in**: In computing, a plug-in (or plugin, add-in, addin, add-on, or addon) is a software **component** that adds a specific **feature** to an existing computer program. When a program supports plug-ins, it enables **customization**.
* **EC2**: Amazon Elastic Compute Cloud (Amazon EC2) is a web **service** that provides secure, **resizable** compute **capacity** in the cloud. 
* **DynamoDB**: Amazon DynamoDB is a **key-value** and **document** database that delivers **single-digit millisecond** performance at any **scale**. 

## How 

* ✅ DO: use it as a **plugin** for other AWS services. For example for processing **image** after uploading to S3 or send alert after a regex trigger on Cloudwatch(AWS logging service).
* 👎 DO NOT: use AWS Lambda as a **gernal EC2 host**. 
* ⚠️ LIMITATION: If you need to access a "State" for exmaple by connecting to DynamoDB, it can get very expensive. 