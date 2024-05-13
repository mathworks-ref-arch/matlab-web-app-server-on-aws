# MATLAB Web App Server on Amazon Web Services

# Requirements

Before starting, you need the following:

-   A MATLAB® Web App Server™ license. To configure a license for use on the cloud, you must obtain the MAC address of the network license manager after deployment to the cloud. For details, see [Configure MATLAB Web App Server Licensing on the Cloud](https://www.mathworks.com/help/webappserver/ug/configure-server-license-on-cloud.html).
-   An Amazon Web Services™ (AWS) account with an IAM user identity.
-   A Key Pair for your AWS account in the US East (N. Virginia), EU (Ireland) or Asia Pacific (Tokyo) region. For more information, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html).

# Costs
You are responsible for the cost of the AWS services used when you create cloud resources using this guide. Resource settings, such as instance type, affect the cost of deployment. For cost estimates, see the pricing pages for each AWS service you will be using. Prices are subject to change.


# Introduction
Use this guide to automate running MATLAB Web App Server on the Amazon Web Services (AWS) Cloud using an AWS CloudFormation template. The template is a YAML file that defines the resources required to deploy and manage MATLAB Web App Server on AWS. For information about AWS templates, see [AWS CloudFormation Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). <br>

The default MATLAB Web App Server deployment template uses the Network License Manager for MATLAB reference architecture to manage MATLAB Web App Server licenses. The template for using an exisitng VPC for the deployment provides an option to either deploy the Network License Manager or use your own license server. For more information about the Network License Manager for MATLAB reference architecture, see [Network License Manager for MATLAB on Amazon Web Services](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).

The template for using an existing VPC for deployment provides an option to either deploy a network license manager or use a network license manager that has already been deployed. For details, see [How Do I Use An Existing VPC to Deploy MATLAB Web App Server?](#how-do-i-use-an-existing-vpc-to-deploy-matlab-web-app-server).


# Prepare Your AWS Account
1. If you do not have an AWS account, create one at https://aws.amazon.com by following the on-screen instructions.
2. Use the regions selector in the navigation bar to choose **US-EAST (N. Virginia)**, **EU (Ireland)** or **Asia Pacific (Tokyo)**, as the region where you want to deploy MATLAB Web App Server.
3. Create a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in that region. A key pair is necessary since it is the only way to connect to the EC2 instance as an administrator.
4. If necessary, [request a service limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-) for the Amazon EC2 instance type or VPCs.  You might need to do this if you already have existing deployments that use that instance type or you think you might exceed the [default limit](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) with this deployment.

# Deploy Reference Architecture for Your Release
To deploy the reference architecture, select your MATLAB Web App Server release from the table and follow the instructions to deploy the server using the provided template. A deployment of MATLAB Web App Server supports MATLAB Runtime versions up to six releases back.
| Release | Supported MATLAB Runtime Versions |
| ------- | --------------------------------- |
| [R2024a](releases/R2024a/README.md) | R2024a, R2023b, R2023a, R2022b, R2022a, R2021b |
| [R2023b](releases/R2023b/README.md) | R2023b, R2023a, R2022b, R2022a, R2021b |
| [R2023a](releases/R2023a/README.md) | R2023a, R2022b, R2022a, R2021b, R2021a, R2020b |
| [R2022b](releases/R2022b/README.md) | R2022b, R2022a, R2021b, R2021a, R2020b, R2020a |
| [R2022a](releases/R2022a/README.md) | R2022a, R2021b, R2021a, R2020b, R2020a, R2019b |
| [R2021b](releases/R2021b/README.md) | R2021b, R2021a, R2020b, R2020a |
> **Note**: MathWorks provides templates for only the six most recent releases of MATLAB Web App Server. Earlier templates are removed and are no longer supported.
# Architecture and Resources
Deploying this reference architecture creates several resources in your
resource group.

### Resources

| Resource Type                                                              | Number of Resources | Description                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AWS EC2 Instance                                                           | 2                   | This resource consists of two virtual machines (VMs):<ul><li>A VM that hosts the MATLAB Web App Server.</li><li>A VM that hosts the Network License Manager for MATLAB. For more information, see [Network License Manager for MATLAB](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).</li></ul>   |
| S3 Bucket                                                                  | 1                  | S3 storage bucket created during the creation of the stack. This resource stores the applications deployed to the reference architecture.                                                                                                                                                                                                  |
| Virtual Private Cluster (VPC)                                              | 1                   | Enables resources to communicate with each other.                                           |
| CloudWatch | 1 | Enables viewing of logs. |



# FAQ

## How do I use an existing VPC to deploy MATLAB Web App Server?

Use the following templates to launch the reference architecture within an existing VPC and subnet. The templates provide an option to deploy the Network License Manager for MATLAB to manage MATLAB Web App Server licenses.

| Release | Launch Button | Operating Systems |
|---------|---------------|-------------------|
| R2024a | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2024a_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> | Windows Server 2022 or Ubuntu 22.04 VM |
| R2023b | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2023b_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> | Windows Server 2022 or Ubuntu 22.04 VM |
| R2023a | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2023a_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> | Windows Server 2019 or Ubuntu 18.04 VM |
| R2022b | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2022b_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> | Windows Server 2019 or Ubuntu 18.04 VM |
| R2022a | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2022a_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> | Windows Server 2019 or Ubuntu 18.04 VM |
| R2021b | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2021b_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> | Windows Server 2019 or Ubuntu 18.04 VM |

In addition to the parameters specified in the section [Configure the Stack](#step-2-configure-the-stack), you will need to specify the following parameters in the template to use your existing VPC.

| Parameter  | Value |
|----------------------------------|--------------------------------------------------------------------------------|
| Existing VPC ID | ID of your existing VPC. |
|Assign Public IP to EC2 Instance Hosting MATLAB Web App Server | Specify whether the deployed EC2 instance must use a public IP address. If you select "No", you must provide a private subnet in the field "Subnet for MATLAB Web App Server". <p>**Note:** Even after you select "No", your MATLAB Web App Server apps home page is still accessible over the Internet. However, you cannot remotely connect to the EC2 instance hosting the server from outside the VPC.</p> |
| Subnet for MATLAB Web App Server | Specify the ID of a public or private subnet within the existing VPC that will host the server. |
| Public Subnet 1 ID | ID of an existing public subnet to host server resources. This subnet can be the same as the one hosting MATLAB Web App Server, as long as the subnet hosting the server is public. If the subnet hosting the server is private, then this subnet must be a different public subnet. |
| Public Subnet 2 ID | ID of an existing public subnet to host server resources. This subnet must be different from Public Subnet 1.|
   ||**Settings for Network License Manager**|
   | Port and IP Address of Existing Network License Manager | Optional parameter: Specify the port number and private DNS name or private IP address of the network license manager that has already been deployed to the existing VPC. Specify it in the format port@privateDNSname, for example, `27000@ip-172-30-1-89.ec2.internal` or `27000@172.30.1.89`. By default, the license manager uses port 27000. Leave this field blank if you are deploying a new network license manager.  |
   | Security Group of Existing Network License Manager | Optional parameter: Specify the security group of the network license manager that has already been deployed to the existing VPC. Leave this field blank if you are deploying a new network license manager. |

You will also need to open the following ports in your VPC:

| Port | Description |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `443` | Required for communicating with MATLAB Web App Server apps home page. |
| `8000`, `9988` | Required for communication between MATLAB Web App Server controllers  and AWS services. These ports do not need to be open to the internet. |
| `27000` | Required for communication between the network license manager and MATLAB Web App Server. |
| `3389`, `22` | Required for Remote Desktop and Secure Connection functionality. This can be used for troubleshooting and debugging MATLAB Web App Server. |

### How to use an existing network license manager in an existing VPC?
If you want to use an existing network license manager:
- Choose `No` for the *Deploy Network License Manager* step of the deployment.
- Specify the IP address of the existing network license manager in the `IP Address of Existing Network License Manager` step of the deployment. You can find the private IP address in the *Outputs* tab of the existing network license manager deployment. 

To use an existing network license manager, you must add the security group of the server VMs to the security group of the license manager.
1. In the AWS management console, select the stack where the network license manager is deployed.
1. In the *Stack details* for your stack, click **Resources**.
1. Look for the **Logical ID** named ```SecurityGroup``` and click the corresponding URL listed under **Physical ID**. This will take you to the security group details.
1. Click the **Inbound Rules** tab, then click **Edit Inbound Rules**.
1. Click **Add Rule**.
1. In the **Type** dropdown, select ```All TCP```.
1. In the **Source**, search and add the ```matlab-webapp-server-sg``` security group. 
1. Click **Save Rules**.


# Enhancement Request
Provide suggestions for additional features or capabilities using the following link: https://www.mathworks.com/solutions/cloud.html

# Technical Support
If you require assistance or have a request for additional features or capabilities, please contact [MathWorks Technical Support](https://www.mathworks.com/support/contact_us.html).