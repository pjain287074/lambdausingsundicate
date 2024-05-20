
You may obtain temporary credentials to access the AWS infrastructure here.
Open API Specification, Documenting
Architecture:

New Tool: Swagger UI
Swagger UI allows anyone — be it your development team or your end consumers — to visualize and interact with the API’s resources without having any of the implementation logic in place.

It’s automatically generated from your OpenAPI (formerly known as Swagger) Specification, with the visual documentation making it easy for back end implementation and client side consumption.


The Goal Of This Task is...
To migrate the Task 10's API from Syndicate Deployment Resources to Open API Specification v3, document it, and deploy the Swagger UI for the API.

Resources Names
Stick to the following resources naming in order to pass the task:

Swagger UI: task11_api_ui
S3 website hosting: api-ui-hoster
AWS Lambda: api_handler
Cognito UserPool: 'simple-booking-userpool'
API Gateway REST API: 'task11_api', stage: 'api'
DynamoDB: 'Tables'
DynamoDB: 'Reservations'
Lambda Versions & Aliases
Please, make sure that your deployment resources do not define Lambda to be deployed with Version (Lambda Version) and Alias (Lambda Alias). It is required for the task verification to pass. Note, that usage of the Lambda Versions & Aliases is a best practice of lambdas management, so do not neglect to deep dive into versions and aliases management.

AWS-syndicate:
- Make sure you have aws-syndicate installed. If not - follow the installation instructions provided in the installation tutorial.

For this task you should:
Set Up the Project:
Generate Syndicate configuration for the task11 project using command:
   syndicate generate config
Copy the 'task10' project and rename the copy to 'task11'.
Don't include syndicate configuration directory named ".syndicate-config-..." and the project state file .syndicate when you copy 'task10' project.

Make sure that API Gateway resource is renamed accordingly in deployment_resources.json.
Adjust Java dependencies if lambda runtime is Java.
Enable CORS:
Ensure CORS is enabled for all resources.
All responses of your lambda function must contain the next headers:
    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*',
    'Accept-Version': '*'
Build and Deploy Project with the Syndicate Tool:
Build a bundle and deploy the project to AWS using the Syndicate CLI.
Export to OAS v3:
Export the API Gateway resource to OpenAPI Specification v3 using the command:
   syndicate export --resource_type api_gateway --dsl oas_v3
This command generates the $api-id_oas_v3.json file containing the definition of the API Gateway deployed in AWS Account in Open API Specification v3 format.

By default, the file will be saved to sub-folder "export" of your project folder.

Resolve Resource Definition Duplication:
Open the deployment_resources.json file.
Locate the resource named 'task11_api' of type 'api_gateway'.
Delete this resource from the JSON file.
Save the changes.
Removing this resource ensures that the outdated API Gateway configuration is not included in the deployment process for Task 11.

Enhance Documentation:
Make your API gateway well-documented by editing previously exported OpenAPI specification file:
Add request and response schemas to the OpenAPI specification.
Document possible errors thrown.
Add summary and description to resource methods.
Update the security schema:
1) Locate Security Schema Section:
- Identify the "securitySchemes" section within the OAS file, where the API Gateway security schema is defined
2) Find "x-amazon-apigateway-authorizer" Object:
- Locate the specific security scheme object named "x-amazon-apigateway-authorizer" within the "securitySchemes" section.
3) Replace "providerARNs" Property:
- Within the "x-amazon-apigateway-authorizer" object, replace the existing "providerARNs" property with "x-syndicate-cognito-userpool-names": ["cognito_userpool_name"].
UserPool's ARN is not available at the time of deployment provisioning, so replacing the "providerARNs" property with a placeholder for the Cognito UserPool name simplifies deployment process.

This placeholder is later replaced with the actual ARN during deployment, making the integration smoother.

You can find more details on Security Schema for OAS Document here.

Update API Gateway:
Build a bundle:
    syndicate build
And update API Gateway:
    syndicate update -types api_gateway_oas_v3
Add S3 Bucket for Swagger UI Hosting:
Execute the following command to generate the necessary metadata for the S3 bucket:
   /// Replace <bucket_name> with a suitable name for your S3 bucket.
   syndicate generate meta s3_bucket --resource_name <bucket_name> --static_website_hosting True
This command will create metadata for an S3 bucket suitable for hosting a static website, which will be used to serve the Swagger UI.

Add Swagger UI Resource to Deployment Resources:
Ensure your OpenAPI specification (OAS v3) is stored inside the 'task11' project directory.
Execute the following command to generate the Swagger UI resource:
    syndicate generate swagger_ui 
        --name <swagger_ui_name> /// Replace <swagger_ui_name> with a suitable name for your Swagger UI resource.
        --path_to_spec <relative_path_to_oas_v3.json> /// Specify the <relative_path_to_oas_v3.json> as the relative path to your OAS v3 JSON file inside the 'task11' project directory.
        --target_bucket <s3_bucket_name> /// Replace <s3_bucket_name> with the name of the S3 bucket created for Swagger UI hosting.
Example:

syndicate generate swagger_ui 
    --name <swagger_ui_name> 
    --path_to_spec <export/$api-id_oas_v3.json> 
    --target_bucket <s3_bucket_name>
This command will generate the Swagger UI resource configuration, including the necessary links to the OAS v3 JSON file and the S3 bucket for hosting.

Build and Deploy Syndicate Bundle:
Execute the following commands to build and deploy the new resources (swagger_ui and s3_bucket) to AWS.

Build a bundle:
    syndicate build
And deploy the new resources (swagger_ui and s3_bucket):
   syndicate deploy -types s3_bucket -types swagger_ui
This command deploys the S3 bucket for Swagger UI hosting and uploads the Swagger UI files to the bucket.
- Only the swagger_ui and s3_bucket resources will be deployed, as specified.
- Ensure that the deployment process completes successfully to make the Swagger UI accessible.

Access Swagger UI:
Find the Bucket website endpoint in aws-syndicate deployment logs or by navigating to the S3 Service in the AWS Management Console.
Select the bucket specified for Swagger UI hosting.
Navigate to Properties.
Find the Static website hosting pane (located at the bottom of the page).
Verify API Documentation:
- Check if every API Endpoint (resources & methods) is carefully described.
- Ensure that request & response models, authentication, and possible errors are documented accurately.
- The Swagger UI should be useful for creating API tests and integrating with your API.
Testing:
Ensure all the application's features are available and work as expected via Swagger UI.
Completing these steps successfully will migrate Task 10's API to OpenAPI Specification v3, document it thoroughly, and deploy Swagger UI for easy testing and integration.

Related Questions:
Check your theoretical knowledge on the topic by answering the following questions:

What is the significance of using OpenAPI Specification (OAS) v3 in AWS API Gateway integration?

Why is it important to enable CORS (Cross-Origin Resource Sharing) in web APIs, and how is it configured in AWS API Gateway?

In the context of AWS API Gateway, what are the benefits of exporting an API to OpenAPI Specification v3, and how does it support API documentation and client-side integration?

How does the AWS Syndicate facilitate the deployment and management of AWS resources for API development, and what are the steps involved in setting up and deploying a project with AWS Syndicate?


You may obtain temporary credentials to access the AWS infrastructure here.
Task verification
Verification resource naming
The goal of task verification is to make sure that the infrastructure created within the task meets the task requirements.
During the process, resources are created in the Verification Account, with the standardized suffix and prefix added automatically to their names.
Your prefix: cmtr-66b88a3a-
Your suffix: -test
Region: eu-central-1 (Frankfurt)
For example, if you describe a resource called "resource", its full name will be: cmtr-66b88a3a-resource-test
To find your resources easily, use the full name generated by the system.
Now you can solve the given problem. After that use buttons below to verify your solution. Verification can take several minutes.
Note: Please make sure to place your completed task files in a folder named task11 within your Git repository's project root. Please provide the link to your Git account for the completed task in the input below, in order to submit it.

•••••••••••••••••••••••••••••••••••••••••••••••••••••••
Input your Git account. For private repositories, use: 'http(s)://<username>:<deploy_token>@<repository_url>'
For public repositories, use:'http(s)://<repository_url>'
Please choose lambda runtime for verification:
Python
In order to proceed with a new verification or finish the current task, it's important to first destroy the resources from the previous task. To do this, please use the "Destroy Resources" button provided.