# Death Event Prediction Model

## Mini Project Part A

For this project, you will train a XGBoost model to predict survival of patients with heart failure. After that, you will save the trained model, create a Gradio-based app, build & push docker image to ECR, and deploy the application with ECS. Please refer to the Demo session - ECR ECS held on May 4th for this mini-project.

* Step 1: Go through the mini-project notebook M7_NB_MiniProject_1_Patient_Survival_Prediction_using_XGBoost shared along with this document and understand the problem statement. [ 1 point ]
  * 1.1 Perform model training
  * 1.2 Save the trained model on your system
* Step 2: Create Gradio-based application for Patient Survival Prediction within Colab notebook [ 2 points ]
  * 2.1 Load the trained model
  * 2.2 Create Gradio application based on instructions given in the notebook
  * 2.3 Create ‘requirements.txt’, and ‘app.py’ files on your system
* Step 3: Dockerize the Gradio application on Cloud9 [ 1 point ]
  * 3.1 Access your AWS Management Console from LMS - as per steps given at last of this document
  * 3.2 Create a new environment on Cloud9
  * 3.3 Upload the trained model, ‘requirements.txt’, and ‘app.py’ files on Cloud9 environment
  * 3.4 Create a Dockerfile to dockerize the application
  * 3.5 Build a docker image for survival prediction
    * Make sure the image size is below 3GB, if you are using AWS account provided by TS
* Step 4: Run docker container on Cloud9 and access the application [ 1 point ]
  * 4.1 Run a new container using the docker image created above
  * 4.2 Access the application via publicIP of EC2 instance associated with the Cloud9 environment
    * Make sure the Security Group attached with the EC2 instance has the application port (eg.8001) open for inbound traffic
  * 4.3 Debug and re-create image if the application is giving error
* Step 5: Push docker image to ECR [ 2 points ]
  * 5.1 Create a new Private Repository on ECR
  * 5.2 Push the docker image present on Cloud9 environment to your ECR repository
* Step 6: Deploy application with ECS [ 2 points ]
  * 6.1 Create a new Cluster (Ignore any namespace warning showing up during the cluster creation)
  * 6.2 Create a Task Definition
    * For a docker image of size ~2GB, use 4GB, 1vCPU as memory and cpu requirements respectively
  * 6.3 Create a Service (Ignore any autoscaling warning showing up during the service creation)
  * 6.4 Once the service is deployed, access the application via publicIP associated with the Task running in your service
* Step 7: CAUTION ! Clean up [ 1 point ]
  * 7.1 Delete/Terminate/Release the resources created on AWS for this mini-project
    * Cloud9
      * Environment
      * EC2 instance associated
    * ECR
      * Images
      * Repository
    * ECS
      * Service
      * Cluster
      * Task Definition

## Mini Project Part B

* Step 1: Make sure you have attempted the previous mini-project, MiniProject-1 Part-A

* Step 2: Create an Elastic IP [ 1 point ]
  * 2.1 Create an Elastic IP, to be used for accessing the application

* Step 3: Create a Network Load Balancer [ 1 point ]
  * 3.1 Create a Network Load Balancer(NLB) to handle sudden and volatile traffic patterns while using a single static/elastic IP
  * 3.2 Give Network mapping details
  * 3.3 In the Listeners and routing section, create a new Target group

* Step 4: Create an Image Repository on ECR [ 1 point ]
* Step 5: Create resources on ECS [ 2 points ]
  * 5.1 Create a new Cluster
  * 5.2 Create a Task Definition
    * For a docker image of size ~2GB, use 4GB, 1vCPU as memory and cpu requirements respectively
    * Download the task definition json file
  * 5.3 Create a Service
    * NOTE: In Deployment configuration, the Desired tasks should be kept 0 initially because once the Service is created it will try to deploy the ECR image which was mentioned in the Task definition json(using the ‘latest’ tag by default), and if the image repo is empty, the service deployment will fail and service might not be created successfully, which inturn will fail the ci/cd workflow when trying to access that service. To avoid failure, desired tasks are kept 0. The service will be updated(desired tasks = 1) once the ci/cd workflow reaches the ‘Deploy’ job, and the image is pushed to ECR by the workflow. If the image is already present on your ECR repository with the ‘latest’ tag, you can set ‘desired tasks=1’.
    * In Networking, select the same subnet you have specified while creating your Network Load Balancer.
    * In Load balancing, select the Network Load Balancer you created.
* Step 6: Create a GitHub Repository [ 2 points ]
  * 6.1 Create a new GitHub repository and add files for your project
  * 6.2 Add your task definition json file to the repository as well
  * 6.3 Add your AWS IAM user credentials to GitHub Secrets
  * 6.4 Create a GitHub Actions workflow to deploy app with ECR and ECS
  * [OPTIONAL] Add steps for train, and test jobs as well within the workflow
* Step 7: Run the workflow [ 1 point ]
  * 7.1 Run your workflow
    * NOTE: Once the workflow reaches deploy job, and image is pushed to ECR,update the service with desired tasks=1 if its sets to 0 previously
  * 7.2 Access your application running on Elastic IP address
* 8: Make changes to your code on GitHub and rerun the workflow [ 1 point ]
  * 8.1 Check if the changes being reflected on the same Elastic IP after successful run of your workflow
* Step 9: CAUTION ! Clean up [ 1 point ]
  * 9.1 Delete/Terminate/Release the resources created on AWS for this mini-project
    * Cloud9
      * Environment
      * EC2 instance associated
  * ECR
    * Images
    * Repository
  * ECS
    * Service
    * Cluster
    * Task Definitions
  * Load Balancer
  * Target Group
  * Elastic IP
