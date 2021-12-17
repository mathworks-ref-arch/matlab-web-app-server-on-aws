# MATLAB Web App Server on Amazon Web Services

# Requirements

Before starting, you need the following:

-   A MATLAB® Web App Server™ license. For more information, see [Configure MATLAB Web App Server Licensing on the Cloud](https://www.mathworks.com/help/webappserver/ug/configure-server-license-on-cloud.html). To configure a license for use on the cloud, you need the MAC address of the network license manager on the cloud. For more information, see [Get License Server MAC Address](#get-network-license-manager-mac-address).


-   An Amazon Web Services™ (AWS) account with an IAM user identity.
-   A Key Pair for your AWS account in the US East (N. Virginia), EU (Ireland) or Asia Pacific (Tokyo) region. For more information, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html).

# Costs
You are responsible for the cost of the AWS services used when you create cloud resources using this guide. Resource settings, such as instance type, will affect the cost of deployment. For cost estimates, see the pricing pages for each AWS service you will be using. Prices are subject to change.


# Introduction
The following guide will help you automate the process of running MATLAB
Web App Server on the Amazon Web Services (AWS) Cloud. The automation is
accomplished using an AWS CloudFormation template. The template is a JSON
file that defines the resources needed to deploy and manage MATLAB Web App
Server on AWS.
For information about AWS templates, see [AWS CloudFormation Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). <br>

The default MATLAB Web App Server deployment template deploys a network license manager to manage MATLAB Web App Server licenses. 

The template for using an existing VPC for deployment provides an option to either deploy a network license manager or use a network license manager that has already been deployed. For details, see [How Do I Use An Existing VPC to Deploy MATLAB Web App Server?](#how-do-i-use-an-existing-vpc-to-deploy-matlab-web-app-server).

# Prepare Your AWS Account
1. If you do not have an AWS account, create one at https://aws.amazon.com by following the on-screen instructions.
2. Use the regions selector in the navigation bar to choose **US-EAST (N. Virginia)**, **EU (Ireland)** or **Asia Pacific (Tokyo)**, as the region where you want to deploy MATLAB Web App Server.
3. Create a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in that region. A key pair is necessary since it is the only way to connect to the EC2 instance as an administrator.
4. If necessary, [request a service limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-) for the Amazon EC2 instance type or VPCs.  You might need to do this if you already have existing deployments that use that instance type or you think you might exceed the [default limit](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) with this deployment.

# Deployment Steps

## Step 1. Launch the Template
Click the **Launch Stack** button to deploy resources on AWS. This will open the AWS Management Console in your web browser.

| Release | Windows Server 2019 or Ubuntu 18.04  |
|---------------|------------------------|
| MATLAB R2021b | <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://joeywebapplambdaarchive.s3.amazonaws.com/WebAppServer_new.yml" target="_blank">     <img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/> </a> |

>**NOTE:** Mulitple versions of MATLAB Runtime are supported. For details, see [Supported MATLAB Runtime Versions](#what-versions-of-matlab-runtime-are-supported).

>**NOTE:** Creating a stack on AWS can take at least 20 minutes.
><!--For other releases, see [How do I launch a template that uses a previous MATLAB release?](#how-do-i-launch-a-template-that-uses-a-previous-matlab-release)-->

## Step 2. Configure the Stack
1. Provide values for parameters in the **Create Stack** page:

    | Parameter Name                         | Value                                                                                                                                                                                                                                                                                                                                                 |
    |----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Stack name**                         | Choose a name for the stack. This will be shown in the AWS console. <p><em>*Example*</em>: `Boston`</p>                                                                                                                                                                                                                                                                       |
    | |**Settings for Hosting MATLAB Web App Server**|
    | **Name of Existing Amazon EC2 Key Pair**          | Choose an existing Amazon EC2 key pair to connect to the EC2 instance hosting MATLAB Web App Server. If you do not have a key pair, create one. For details, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair). <p><em>*Example*</em>: `boston-keypair`</p>                                                                                   |
    | **IP Address of MATLAB Web App Server Administrator in CIDR Notation** | Specify the IP address of the administrator using CIDR notation. The administrator can remotely connect to the EC2 instance that hosts MATLAB Web App Server and administer it. The IP address can be a single IP address or a range of IP addresses. The format for this field is IP Address/Mask.The format for this field is IP Address/Mask. <p><em>Example</em>: `x.x.x.x/32`<ul><li>This is the public IP address which can be found by searching for **"what is my ip address"** on the web. The mask determines the number of IP addresses to include.</li><li>A mask of 32 is a single IP address.</li><li>Use a [CIDR calculator](https://www.ipaddressguide.com/cidr) if you need a range of more than one IP addresses.</li><li>You may need to contact your IT administrator to determine which address is appropriate.</li></ul>**NOTE:** Restricting access to the server using an IP address is not a form of authentication. MATLAB Web App Server supports authentication using LDAP and OIDC. For details, see [Authentication](https://www.mathworks.com/help/webappserver/ug/authentication.html).</p> |
    | **Do You Want to Use the Same IP Address Range to Access the MATLAB Web App Server Apps Home Page?**| Select, **Yes** or **No**. <ul><li>If you select **Yes**, the same IP address range specified above is configured to access the MATLAB Web App Server apps homepage. Choose this option if you know that the same set of users will administer the server and access web apps on the apps home page.</li><li>If you select **No**, you must specify a new IP address range in the next field. Choose this option if the users accessing web apps on the apps home page are different from the users administering the server.</li></ul>
    | **IP Addresses Allowed to Access MATLAB Web App Server Apps Home Page** | Complete this field only if you selected **"No"** in the previous field. Specify the range of IP addresses that can access the MATLAB Web App Server apps home page in CIDR notation. The format for this field is IP Address/Mask.<p><em>*Example*</em>: `x.x.x.x/24`</p> |
    | **ARN of SSL Certificate** | Specify the Amazon Resource Name (ARN) of the SSL certificate you uploaded to the AWS Ceritifcate Manager. The ARN facilitates connecting to the apps home page using an HTTPS connection.<p><em>*Example*</em>: <code>arn:aws:acm:us-east-1:012345678910:certificate/666abcd6-ab6c-6ab6-a666-a666666bcd66</code> </p><p>To retrieve an ARN:</p><ul><li>Type "Certificate Manager" in the search box at the top of the web page and hit Enter. This automatically takes you to the AWS Certificate Manager.</li><li>Select the certificate you uploaded based on Certificate ID, or Domain name, or Name tag .</li><li>Copy the ARN from the "Certificate status" section at the top.</li></ul><p>For more information, see [Create Self-signed Certificate](/README.md#create-self-signed-certificate) and [Upload Self-signed Certificate to AWS Certificate Manager](/README.md#upload-self-signed-certificate-to-aws-certificate-manager).
    | **EC2 Instance Type** | Choose the AWS EC2 instance type to use for the server. All AWS instance types are supported. For more information, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/). <p><em>*Example*</em>: `m5.xlarge`</p> |
    | **Operating System** | Choose between Windows (Windows Server) and Linux (Ubuntu).  |
    ||**Settings for Network License Manager**|
    | **Password for Network License Manager** | Specify a password for the network license manager. Use this password to log in to the network license manager after the stack has been successfully created.<p>Deploying MATLAB Web App Server automatically deploys a network license manager.</p>|
    | **Confirm Password** | Reenter the password to log in to the network license manager. |

    >**Note**: Make sure you select US East (N.Virginia), EU (Ireland) or Asia Pacific (Tokyo) as your region from the navigation panel on top. Currently, US East, EU (Ireland), and Asia Pacific (Tokyo) are the only supported regions.

2. Tick the boxes to accept that the template uses IAM roles. For more information about IAM, see [IAM FAQ](https://aws.amazon.com/iam/faqs). 
  
3. Click the **Create** button. The CloudFormation service starts creating resources for the stack.
>**Note**: Clicking **Create** takes you to the *Stack Detail* page for your stack. Wait for the Status to reach **CREATE\_COMPLETE**. This can take up to 20 minutes.

## Step 3. Upload License File
1. Click **Outputs** in the *Stack details* for your stack.
1. Look for the key named `MATLABWebAppServerLicenseManager` and click the corresponding URL listed under value. This will take you to Network License Manager for MATLAB Dashboard login page.
1. The username is **manager**. For the password, enter the password you entered in the **Password for Network License Manager** field while creating the stack in [Step 2](#step-2-configure-the-stack).
1. Follow the instructions on the home page of the network license manager to upload your MATLAB Web App Server license.

>**Note:** MATLAB Web App Server automatically starts after succesfully uploading a valid license file.

## Step 4. Open the MATLAB Web App Server Apps Home Page
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerAppsHomePage` and click the corresponding URL listed under value. This opens the apps home page.

You are now ready to use MATLAB Web App Server on AWS. 

To run applications on MATLAB Web App Server, you need to create web apps using MATLAB Compiler. For details, see [Web Apps](https://www.mathworks.com/help/compiler/webapps/create-and-deploy-a-web-app.html) in the MATLAB Compiler product documentation.

# Common Tasks
## Upload Web Apps to AWS S3 Bucket
1. In the AWS management console, select the stack that you deployed. 
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerAppsS3Bucket`, and click the corresponding URL listed under value.
1. In the S3 console, click **apps**.
1. Click **Upload** > **Add Files** to select and upload web apps (`.ctf` files).
>**NOTE:** If you enable OIDC authentication, you can upload web apps from the apps home page. Any apps you upload via the apps home page are not synchornized with S3 bucket. To enable OIDC authentication, see [Configure OIDC Authentication](#configure-oidc-authentication).

## Get Password to EC2 Instance Hosting MATLAB Web App Server
1. In the AWS management console, select the stack you deployed. 
1. In the Stack Detail for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerEC2Instance` and click the corresponding URL listed under value. This will take you to the server instance (`matlab-webapp-server-vm`) page. 
1. Click the **Connect** button at the top.
1. In the *Connect to instance* dialog, choose **Get Password**.
1. Click **Choose File** to navigate and select the private key file (`.pem` file) for the key pair that you used while creating the stack in [Step 2](#step-2-configure-the-stack).
1. Click **Decrypt Password**. The console displays the password for the instance in the *Connect to instance* dialog.
1. Copy the password to the clipboard.

## Connect to EC2 Instance Hosting MATLAB Web App Server Using Remote Desktop
1. In the AWS management console, select the stack you deployed. 
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerEC2Instance` and click the corresponding URL listed under value. This will take you to the server instance (`matlab-webapp-server-vm`) page. 
1. Click the value under Instance ID to view the instance summary. 
1. Click the **Connect** button at the top.
1. In the *Connect to instance* dialog, click  the **RDP client** tab.
1. Click the **Download remote desktop file** button to download a .rdp file.
1. Use the .rdp file to remotely connect to EC2 instance using the following credentials:
* Username: Administrator
* Password: The decrypted password. For details, see [Get Password to EC2 Instance](#get-password-to-ec2-instance).

## Connect to EC2 Instance Hosting MATLAB Web App Server Using SSH
1. In the AWS management console, select the stack you deployed. 
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerEC2Instance` and click the corresponding URL listed under value. This will take you to the server instance (`matlab-webapp-server-vm`) page. 
1. Click the value under Instance ID to view the instance summary. 
1. Click the **Connect** button at the top.
1. In the *Connect to instance* dialog, click  the **SSH client** tab.
1. Follow the instructions on the page to SSH to the EC2 instance.

## Find Setup and Configuration Files
| Task                  | Relevant Files                                            | Details                            |
|-----------------------|-----------------------------------------------------------|------------------------------------|
| Server Administration | `webapps-start`, `webapps-stop`, `webapps-restart`, `webapps-status` | [Command-Line Scripts Documentation](https://www.mathworks.com/help/webappserver/server-management.html) |
| Authentication        | `webapps_authn.json`                                        | [Authentication Documentation](https://www.mathworks.com/help/webappserver/ug/authentication.html)       |
| Role-Based Access     | `webapps_app_roles.json`                                    | [Role-Based Access Documentation](https://www.mathworks.com/help/webappserver/ug/role-based-access.html)    |
| Policy-Based Access   | `webapps_acc_ctl.json`                                      | [Policy-Based Access Documentation](https://www.mathworks.com/help/webappserver/ug/policy-based-access.html)  |

## Configure OIDC Authentication
1. Connect to the EC2 instance hosting MATLAB Web App Server. For details, see:
    * [Connect to EC2 Instance Hosting MATLAB Web App Server Using Remote Desktop](#connect-to-ec2-instance-hosting-matlab-web-app-server-using-remote-desktop)
    * [Connect to EC2 Instance Hosting MATLAB Web App Server Using SSH](#connect-to-ec2-instance-hosting-matlab-web-app-server-using-ssh).
1. Follow the instructions on the [Authentication](https://www.mathworks.com/help/webappserver/ug/authentication.html) page in the MathWorks documentation.
    >**NOTE:** SSL is enabled when you deploy the stack.   
1. For the `redirectUrl`, use the URL created as part of your stack.
    * In the AWS management console, select the stack you deployed. 
    * In the *Stack details* for your stack, click the **Outputs** tab.
    * Look for the key named `MATLABWebAppServerOIDCRedirectUrl` and copy the corresponding URL listed under value.
    * Use this URL in the `webapps_authn.json` file.

## Create Self-signed Certificate
For information on creating a self-signed certificate, see [Create and Sign an X509 Certificate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html).

## Upload Self-signed Certificate to AWS Certificate Manager

1. Open the AWS Certificate Manager.
2. Click the button at the top of the page to **Import a certificate**.
3. Copy the contents of the `.crt` file containing the certificate into the field labeled **Certificate body**.
4. Copy the contents of the `.pem` file containing the private key into the field labeled **Certificate private key**.
5. Leave the field labeled **Certificate chain** blank.
6. Click the button labeled **Review and import**.
7. Review the settings and click the **Import** button.
8. Copy the value of the Amazon Resource Name (ARN) field from the **Details** section of the certificate.

The ARN value that you copied should be pasted into the **ARN of SSL Certificate** parameter of the template in [Step 2](#step-2-configure-the-stack).

## View Logs
Logs are available in AWS CloudWatch. 
1. In the AWS management console, select the stack you deployed. 
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. To view logs related to the cloud console and the MATLAB Web App Server workers, look for the key named `MATLABWebAppServerLogGroup`, and click the corresponding URL listed under value.

## Get Network License Manager MAC Address
1. In the AWS management console, select the stack that you deployed. 
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerLicenseManager`, and click the corresponding URL listed under value.
1. Log in to the Network License Manager for MATLAB dashboard using the following credentials:<br>
Username: **manager**<br>
Password: Enter the password you provided while creating the stack.
1. Click **Administration** > **Manage License**.
1. Copy the license server MAC address displayed at the top.

When you deploy the MATLAB Web App Server reference architecture a network license manager is automatically deployed. You can also use an existing license manager that is located in the same VPC and the security group of the MATLAB Web App Server EC2 instance. For detials, see [Network License Manager for MATLAB](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).

>**NOTE**: The license manager MAC address is available only after the stack creation is complete.

## Delete Your Stack
To delete the stack:
1. Log in to the AWS Console.
3. Go to the CloudFormation page and select the stack you created.
3. Click **Delete**.

# FAQ

## How do I use an existing VPC to deploy MATLAB Web App Server?

Use the following templates to launch the reference architecture within an existing VPC and subnet. The templates provide an option to deploy the Network License Manager for MATLAB to manage MATLAB Web App Server licenses.

| Release | Windows Server 2019 or Ubuntu 18.04 VM |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R2021b | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://joeywebapplambdaarchive.s3.amazonaws.com/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" />  </a> |

In addition to the parameters specified in the section [Configure the Stack](#step-2-configure-the-stack), you will need to specify the following parameters in the template to use your existing VPC.

| Parameter  | Value |
|----------------------------------|--------------------------------------------------------------------------------|
| Existing VPC ID | ID of your existing VPC. |
| IP address range of existing VPC | IP address range from the existing VPC. To find the IP address range: <ol><li>Log in to the AWS Console.</li><li>Navigate to the VPC dashboard and select your VPC.</li><li>Click the **CIDR blocks** tab.</li><li>The **IPv4 CIDR Blocks** gives the IP address range.</li></ol> |
|Assign Public IP to EC2 Instance Hosting MATLAB Web App Server | Specify whether the deployed EC2 instance must use a public IP address. If you select "No", you must provide a private subnet in the field "Subnet for MATLAB Web App Server". |
| Subnet for MATLAB Web App Server | Specify the ID of a public or private subnet within the existing VPC that will host the server. |
| Public Subnet 1 ID | ID of an existing public subnet to host server resources. This subnet can be the same as the one hosting MATLAB Web App Server, as long as the subnet hosting the server is public. If the subnet hosting the server is private, then this subnet must be a different public subnet. |
| Public Subnet 2 ID | ID of an existing public subnet to to host server resources. This subnet must be different from Public Subnet 1.|

You will also need to open the following ports in your VPC:

| Port | Description |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `443` | Required for communicating with MATLAB Web App Server apps home page. |
| `8000`, `9988` | Required for communication between MATLAB Web App Server controllers  and AWS services. These ports do not need to be open to the internet. |
| `27000` | Required for communication between the network license manager and MATLAB Web App Server. |
| `3389`, `22` | Required for Remote Desktop and Secure Connection functionality. This can be used for troubleshooting and debugging MATLAB Web App Server. |

### How to use an existing network license manager in an existing VPC?
If you want to use an exisiting network license manager:
- Choose `No` for the *Deploy Network License Manager* step of the deployment.
- Specify the IP address of the existing network license manager in the `IP Address of Existing Network License Manager` step of the deployment. 

To use an existing network license manager, you must add the security group of the server VMs to the security group of the license manager.
1. In the AWS management console, select the stack where the network license manager is deployed.
1. In the *Stack details* for your stack, click **Resources**.
1. Look for the **Logical ID** named ```SecurityGroup``` and click the corresponding URL listed under **Physical ID**. This will take you to the security group details.
1. Click the **Inbound Rules** tab, then click **Edit Inbound Rules**.
1. Click **Add Rule**.
1. In the **Type** dropdown, select ```All TCP```.
1. In the **Source**, search and add the ```MatlabWebappServerCloudStackSg``` security group. 
1. Click **Save Rules**.

## What versions of MATLAB Runtime are supported?

| Release | MATLAB Runtime | MATLAB Runtime | MATLAB Runtime | MATLAB Runtime |  
|---------------|----------------|----------------|----------------|----------------|
| MATLAB R2021b |  R2020a | R2020b | R2021a |  R2021b |  

# Enhancement Request
Provide suggestions for additional features or capabilities using the following link: https://www.mathworks.com/cloud/enhancement-request.html

# Technical Support
If you require assistance or have a request for additional features or capabilities, please contact [MathWorks Technical Support](https://www.mathworks.com/support/contact_us.html).
