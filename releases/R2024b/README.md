# MATLAB Web App Server on Amazon Web Services - R2024b

# Deployment Steps
Follow these steps to deploy the R2024b MATLAB Web App Server reference architecture on AWS. To deploy reference architectures for other releases, see [Deploy Reference Architecture for Your Release](/README.md#deploy-reference-architecture-for-your-release). 
## Step 1. Launch Template
Before launching the template, make sure that you have selected one of these supported AWS regions from the top navigation:<ul><li>**US East (N. Virginia)**</li><li>**Europe (Ireland)**</li><li>**Asia Pacific (Tokyo)**</li></ul>

Then, click the appropriate **Launch Stack** button to launch the stack configuration template for deploying resources onto your AWS account. You can deploy resources onto either a new or existing VPC.

| Release | New VPC | Existing VPC | Operating Systems |
|---------|---------| ------------ | ----------------- |
| R2024b | <a href="https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/quickcreate?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2024b_refarch/WebAppServer_new.yml" target="_blank">     <img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/> </a> | <a  href ="https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2024b_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" /> </a> | Windows Server 2022 or Ubuntu 22.04 VM |

The AWS Management Console opens in your web browser.

>**NOTE:** Mulitple versions of MATLAB Runtime are supported. For details, see [Deploy Reference Architecture for Your Release](/README.md#deploy-reference-architecture-for-your-release).

>**NOTE:** Creating a stack on AWS can take at least 20 minutes.


## Step 2. Configure the Stack
1. Provide values for parameters in the **Create Stack** page:

    | Parameter Name                         | Value                                                                                                                                                                                                                                                                                                                                                 |
    |----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Stack name**                         | Choose a name for the stack. This will be shown in the AWS console. <p><em>*Example*</em>: `Boston`</p>                                                                                                                                                                                                                                                                       |
    | |**Settings for Hosting MATLAB Web App Server**|
    | **Name of Existing Amazon EC2 Key Pair**          | Choose an existing Amazon EC2 key pair to connect to the EC2 instance hosting MATLAB Web App Server. If you do not have a key pair, create one. For details, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair). <p><em>*Example*</em>: `boston-keypair`</p>                                                                                   |
    | **IP Address of MATLAB Web App Server Administrator in CIDR Notation** | Specify the IP address of the administrator using CIDR notation. The administrator can remotely connect to the EC2 instance that hosts MATLAB Web App Server and administer it. The IP address can be a single IP address or a range of IP addresses. The format for this field is IP Address/Mask. <p><em>Example</em>: `x.x.x.x/32`<ul><li>This is the public IP address which can be found by searching for **"what is my ip address"** on the web. The mask determines the number of IP addresses to include.</li><li>A mask of 32 is a single IP address.</li><li>Use a [CIDR calculator](https://www.ipaddressguide.com/cidr) if you need a range of more than one IP addresses.</li><li>You may need to contact your IT administrator to determine which address is appropriate.</li></ul>**NOTE:** Restricting access to the server using an IP address is not a form of authentication. MATLAB Web App Server supports authentication using LDAP and OIDC. For details, see [Authentication](https://www.mathworks.com/help/webappserver/ug/authentication.html).</p> |
    | **Do You Want to Use the Same IP Address Range to Access the MATLAB Web App Server Apps Home Page?**| Select, **Yes** or **No**. <ul><li>If you select **Yes**, the same IP address range specified above is configured to access the MATLAB Web App Server apps homepage. Choose this option if you know that the same set of users will administer the server and access web apps on the apps home page.</li><li>If you select **No**, you must specify a new IP address range in the next field. Choose this option if the users accessing web apps on the apps home page are different from the users administering the server.</li></ul>
    | **IP Addresses Allowed to Access MATLAB Web App Server Apps Home Page** | Complete this field only if you selected **"No"** in the previous field. Specify the range of IP addresses that can access the MATLAB Web App Server apps home page in CIDR notation. The format for this field is IP Address/Mask.<p><em>*Example*</em>: `x.x.x.x/24`</p> |    
    | **EC2 Instance Type** | Choose the AWS EC2 instance type to use for the server. All AWS instance types are supported. For more information, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/). <p><em>*Example*</em>: `m6a.large`</p> |
    | **Operating System** | Choose between Windows (Windows Server) and Linux (Ubuntu).  |
    ||**Settings for Network License Manager**|
    | **Password for Network License Manager** | Specify a password for the network license manager. Use this password to log in to the network license manager after the stack has been successfully created.<p>Deploying MATLAB Web App Server automatically deploys a network license manager.</p>|
    | **Confirm Password** | Reenter the password to log in to the network license manager. |

    >**Note**: Make sure you select US East (N.Virginia), EU (Ireland) or Asia Pacific (Tokyo) as your region from the navigation panel on top. Currently, US East, EU (Ireland), and Asia Pacific (Tokyo) are the only supported regions.

2. Tick the boxes to accept that the template uses IAM roles. For more information about IAM, see [IAM FAQ](https://aws.amazon.com/iam/faqs). 
  
3. Click the **Create** button. The CloudFormation service starts creating resources for the stack.
>**Note**: Clicking **Create** takes you to the *Stack Detail* page for your stack. Wait for the Status to reach **CREATE\_COMPLETE**. This can take up to 20 minutes.

## Step 3. Configure Existing VPC

>**Note**: If you are deploying to a new VPC, skip this step.

To deploy MATLAB Web App Server onto an existing VPC, specify these additional parameters.

| Parameter  | Value |
|----------------------------------|--------------------------------------------------------------------------------|
| Existing VPC ID | ID of your existing VPC. |
|Assign Public IP to EC2 Instance Hosting MATLAB Web App Server | Specify whether the deployed EC2 instance must use a public IP address. If you select "No", you must provide a private subnet in the field "Subnet for MATLAB Web App Server". <p>**Note:** Even after you select "No", your MATLAB Web App Server apps home page is still accessible over the Internet. However, you cannot remotely connect to the EC2 instance hosting the server from outside the VPC.</p> |
| Subnet for MATLAB Web App Server | Specify the ID of a public or private subnet within the existing VPC that will host the server. If you selected "Yes" in the previous field for assigning a public IP, choose a public subnet. Otherwise, choose a private subnet. |
| Public Subnet 1 | ID of an existing public subnet to host server resources. This subnet can be the same as the one hosting MATLAB Web App Server, as long as the subnet hosting the server is public. If the subnet hosting the server is private, then this subnet must be a different public subnet. |
   ||**Settings for Network License Manager**|
   | Port and IP Address of Existing Network License Manager | Optional parameter: Specify the port number and private DNS name or private IP address of the network license manager that has already been deployed to the existing VPC. Specify it in the format port@privateDNSname, for example, `27000@ip-172-30-1-89.ec2.internal` or `27000@172.30.1.89`. By default, the license manager uses port 27000. Leave this field blank if you are deploying a new network license manager.  |
   | Security Group of Existing Network License Manager | Optional parameter: Specify the security group of the network license manager that has already been deployed to the existing VPC. Leave this field blank if you are deploying a new network license manager. If you have an existing license manager and leave this blank, you must add the security group manually using the instructions in [Use an existing network license manager in an existing VPC](#use-an-existing-network-license-manager-in-an-existing-vpc).|

You will also need to open the following ports in your VPC:

| Port | Description |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `443` | Required for communicating with MATLAB Web App Server apps home page. |
| `8000`, `9988` | Required for communication between MATLAB Web App Server controllers  and AWS services. These ports do not need to be open to the internet. |
| `27000` | Required for communication between the network license manager and MATLAB Web App Server. |
| `3389`, `22` | Required for Remote Desktop and Secure Connection functionality. This can be used for troubleshooting and debugging MATLAB Web App Server. |

### Use an existing network license manager in an existing VPC
For complete instructions on deploying the Network License Manager for MATLAB reference architecture, see [Network License Manager for MATLAB on Amazon Web Services](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).

If you want to use an existing network license manager in an existing VPC:
- Choose `No` for the *Deploy Network License Manager* step of the deployment.
- Specify the IP address of the existing network license manager in the `IP Address of Existing Network License Manager` step of the deployment. You can find the private IP address in the *Outputs* tab of the existing network license manager deployment. 
#### Add security group of the server VMs to the security group of the license manager
If you did not supply a security group in the field **Security Group of Existing Network License Manager** at the time of deployment, you must add the security group of the server VMs to the security group of the license manager.
1. In the AWS management console, select the external security group that is nested in the network license manager stack you created. If it is not present in the stack list, ensure the **View nested** option is enabled.<p>For example: `mluser-nlm-MWSecurityGroupExternal-8JJX66NUZDD8`</p>
1. In the *Stack details* for the external security group stack, click **Resources**.
1. Look for the **Logical ID** named ```SecurityGroup``` and click the corresponding URL listed under **Physical ID**. This will take you to the security group details.
1. Select the security group. Click the **Inbound Rules** tab, then click **Edit Inbound Rules**.
1. Click **Add Rule**.
1. In the **Type** dropdown, select ```All TCP```.
1. In the **Source**, search and add the ```matlab-webapp-server-sg``` security group. 
1. Click **Save Rules**.

## Step 4. Create Stack
Review or edit your stack details. You must select the acknowledgements to create IAM resources. Otherwise, the deployment produces a `Requires capabilities : [CAPABILITY_IAM]` error and fails to create resources. For more information about IAM, see [IAM FAQ](https://aws.amazon.com/iam/faqs).

Click the **Create** button. The CloudFormation service starts creating resources for the stack.
>**Note**: Clicking **Create** takes you to the *Stack Detail* page for your stack. Wait for the Status to reach **CREATE\_COMPLETE**. This can take up to 20 minutes.

## Step 5. Upload License File
1. Click **Outputs** in the *Stack details* for your stack.
1. Look for the key named `MATLABWebAppServerLicenseManager` and click the corresponding URL listed under value. This will take you to Network License Manager for MATLAB Dashboard login page.
1. The username is **manager**. For the password, enter the password you entered in the **Password for Network License Manager** field while creating the stack in [Step 2](#step-2-configure-the-stack).
1. Follow the instructions on the home page of the network license manager to upload your MATLAB Web App Server license.

>**Note:** MATLAB Web App Server automatically starts after succesfully uploading a valid license file.


## Step 6. Open the MATLAB Web App Server Apps Home Page
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
>**NOTE 1:** If you enable OIDC authentication, you can upload web apps from the apps home page. Any apps you upload via the apps home page are not synchornized with S3 bucket. To enable OIDC authentication, see [Configure OIDC Authentication](#configure-oidc-authentication).
>**NOTE 2:**  Only folders created within the APPS root level folder are supported. Subfolders within those folders are not supported.

## Get Password to EC2 Instance Hosting MATLAB Web App Server
1. In the AWS management console, select the stack you deployed. 
1. In the Stack Detail for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerEC2Instance` and click the corresponding URL listed under value. This will take you to the server instance (`matlab-webapp-server-vm`) page. 
1. Click the **Connect** button at the top.
1. In the *Connect to instance* dialog, click the **RDP client** tab and then click **Get Password**.
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
* Password: The decrypted password. For details, see [Get Password to EC2 Instance](#get-password-to-ec2-instance-hosting-matlab-web-app-server).

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

When you deploy the MATLAB Web App Server reference architecture, a network license manager is automatically deployed. You can also use an existing license manager that is located in the same VPC and the security group of the MATLAB Web App Server EC2 instance. For details, see [Network License Manager for MATLAB](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).

>**NOTE**: The license manager MAC address is available only after the stack creation is complete.

## Delete Your Stack
To delete the stack:
1. Log in to the AWS Console.
3. Go to the CloudFormation page and select the stack you created.
3. Click **Delete**.

# Enhancement Request
Provide suggestions for additional features or capabilities using the following link: https://www.mathworks.com/solutions/cloud.html

# Technical Support
If you require assistance or have a request for additional features or capabilities, please contact [MathWorks Technical Support](https://www.mathworks.com/support/contact_us.html).