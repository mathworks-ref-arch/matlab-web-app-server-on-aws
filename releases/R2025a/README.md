# MATLAB Web App Server on Amazon Web Services - R2025a

# Deployment Steps
Follow these steps to deploy the R2025a MATLAB Web App Server reference architecture on AWS. To deploy reference architectures for other releases, see [Deploy Reference Architecture for Your Release](/README.md#deploy-reference-architecture-for-your-release).

## Prerequisites
Before deploying MATLAB Web App Server within an existing Virtual Private Cloud (VPC), you must configure the VPC to enable connectivity. For details, see [Ensure connectivity in an existing VPC](#ensure-connectivity-in-an-existing-vpc).

## Step 1. Launch Template
Before launching the template, make sure that you have selected one of these supported AWS regions from the top navigation:<ul><li>**US East (N. Virginia)**</li><li>**Europe (Ireland)**</li><li>**Asia Pacific (Tokyo)**</li></ul>

Then, click the appropriate **Launch Stack** button to launch the stack configuration template for deploying resources onto your AWS account. You can deploy resources onto either a new or existing VPC.

| Release | New VPC | Existing VPC | Operating Systems |
|---------|---------| ------------ | ----------------- |
| R2025a | <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2025a_refarch/WebAppServer_new.yml" target="_blank">     <img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/> </a> | <a  href ="https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://matlab-web-app-server-templates.s3.amazonaws.com/r2025a_refarch/WebAppServer_existing.yml"  target ="_blank" >      <img  src ="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" /> </a> | Windows Server 2022 or Ubuntu 22.04 VM |

The AWS Management Console opens in your web browser.

>**NOTE:** Multiple versions of MATLAB Runtime are supported. For details, see [Deploy Reference Architecture for Your Release](/README.md#deploy-reference-architecture-for-your-release).

>**NOTE:** Creating a stack on AWS can take at least 20 minutes.

## Step 2. Configure the Stack
1. Provide values for parameters in the **Create Stack** page:

    | Parameter Name                         | Value                                                                                                                                                                                                                                                                                                                                                 |
    |----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Stack name**                         | Choose a name for the stack. This will be shown in the AWS console. <p><em>*Example*</em>: `Boston`</p>                                                                                                                                                                                                                                                                       |
    | |**Settings for Hosting MATLAB Web App Server**|
    | **Name of Existing Amazon EC2 Key Pair**          | Choose an existing Amazon EC2 key pair to connect to the EC2 instance hosting MATLAB Web App Server. If you do not have a key pair, create one. For details, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair). <p><em>*Example*</em>: `boston-keypair`</p>                                                                                   |
    | **IP Address of MATLAB Web App Server Administrator in CIDR Notation** | Specify the IP address of the administrator using CIDR notation. The administrator can remotely connect to the EC2 instance that hosts MATLAB Web App Server and administer it. The IP address can be a single IP address or a range of IP addresses. The format for this parameter is IP Address/Mask. <p><em>Example</em>: `x.x.x.x/32`<ul><li>Your public IP address can be found by searching for **"what is my ip address"** on the web. The mask determines the number of IP addresses to include.</li><li>A mask of 32 is a single IP address.</li><li>Use a [CIDR calculator](https://www.ipaddressguide.com/cidr) if you need a range of more than one IP address.</li><li>You may need to contact your IT administrator to determine which address is appropriate.</li></ul>**NOTE:** Restricting access to the server using an IP address is not a form of authentication. MATLAB Web App Server supports authentication using LDAP or OIDC. For details, see [Step 8](#step-8-configure-user-authentication).</p> |
    | **Do You Want to Use the Same IP Address Range to Access the MATLAB Web App Server Apps Home Page?**| Select, **Yes** or **No**. <ul><li>If you select **Yes**, the same IP address range specified above is configured to access the MATLAB Web App Server apps home page. Choose this option if you know that the same set of users will administer the server and access web apps on the apps home page.</li><li>If you select **No**, you must specify a new IP address range for the next parameter. Choose this option if the users accessing web apps on the apps home page are different from the users administering the server.</li></ul>
    | **IP Addresses Allowed to Access MATLAB Web App Server Apps Home Page** | Complete this parameter only if you selected **No** for the previous parameter. Specify the range of IP addresses that can access the MATLAB Web App Server apps home page in CIDR notation. The format for this parameter is IP Address/Mask.<p><em>*Example*</em>: `x.x.x.x/24`</p> |    
    | **EC2 Instance Type** | Choose the AWS EC2 instance type to use for the server. All AWS instance types are supported. For more information, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/). <p><em>*Example*</em>: `m6a.large`</p> |
    | **Operating System** | Choose between Windows (Windows Server) and Linux (Ubuntu). <p><p>**NOTE:** The admin portal interface and Keycloak authentication are only available on Linux.|
    ||**Settings for Network License Manager**|
    | **Password for Network License Manager** | Specify a password for the network license manager. Use this password to log in to the network license manager after the stack has been successfully created.<p>Deploying MATLAB Web App Server automatically deploys a network license manager.</p>|
    | **Confirm Password** | Reenter the password to log in to the network license manager. |

    >**Note**: Make sure you select US East (N.Virginia), EU (Ireland) or Asia Pacific (Tokyo) as your region from the navigation panel on top. Currently, US East, EU (Ireland), and Asia Pacific (Tokyo) are the only supported regions.

2. Tick the boxes to accept that the template uses IAM roles. For more information about IAM, see [IAM FAQ](https://aws.amazon.com/iam/faqs). 
  
3. Click the **Create** button. The CloudFormation service starts creating resources for the stack.
>**Note**: Clicking **Create** takes you to the *Stack Detail* page for your stack. Wait for the Status to reach **CREATE\_COMPLETE**. This can take up to 20 minutes.

## Step 3. Configure Existing VPC

>**Note**: If you are deploying to a new VPC, skip this step.

To deploy MATLAB Web App Server onto an existing VPC, select the **Existing VPC** template in [Step 1](#step-1-launch-template). In addition to the parameters listed in Step 2, you must also specify the following parameters.

| Parameter  | Value |
|----------------------------------|--------------------------------------------------------------------------------|
| Existing VPC ID | ID of your existing VPC. |
|Assign Public IP to EC2 Instance Hosting MATLAB Web App Server | Specify whether to assign a public IP address to the deployed EC2 instance. If you are deploying a new network license manager, the network license manager will be assigned the same type of IP address as the EC2 instance. <ul><li>If you select `Yes`, you must provide a public subnet in the parameter **Subnet for MATLAB Web App Server**.</li><li>If you select `No`, you must provide a private subnet for the parameter **Subnet for MATLAB Web App Server**.<p>Even if you select `No`, your MATLAB Web App Server apps home page is still accessible over the Internet. However, you cannot remotely connect to the EC2 instance hosting the server from outside the VPC.</li></ul><p><p>**Note:** You may need to configure an endpoint or public NAT gateway to ensure MATLAB Web App Server can access AWS services. For details, see [Ensure connectivity in an existing VPC](#ensure-connectivity-in-an-existing-vpc).</p> |
| Subnet for MATLAB Web App Server | Specify the ID of a public or private subnet within the existing VPC that will host the server. If you selected `Yes` for the previous parameter for assigning a public IP, choose a public subnet. Otherwise, choose a private subnet. |
| Public Subnet 1 | ID of an existing public subnet to host server resources. This subnet can be the same as the one hosting MATLAB Web App Server, as long as the subnet hosting the server is public. If the subnet hosting the server is private, then this subnet must be a different public subnet. |
   ||**Settings for Network License Manager**|
   | Port and IP Address of Existing Network License Manager | Optional parameter: Specify the port number and private DNS name or private IP address of the network license manager that has already been deployed to the existing VPC. Specify it in the format port@privateDNSname, for example, `27000@ip-172-30-1-89.ec2.internal` or `27000@172.30.1.89`. By default, the license manager uses port 27000. Leave this parameter blank if you are deploying a new network license manager.  |
   | Security Group of Existing Network License Manager | Optional parameter: Specify the security group of the network license manager that has already been deployed to the existing VPC. If you have an existing license manager and leave this parameter blank, you must add the security group manually using the instructions in [Use an existing network license manager in an existing VPC](#use-an-existing-network-license-manager-in-an-existing-vpc). Leave this parameter blank if you are deploying a new network license manager.|

### Use an existing network license manager in an existing VPC
For complete instructions on deploying the Network License Manager for MATLAB reference architecture, see [Network License Manager for MATLAB on Amazon Web Services](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).

If you want to use an existing network license manager in an existing VPC:
- Choose `No` for the *Deploy Network License Manager* step of the deployment.
- Specify the IP address of the existing network license manager in the `IP Address of Existing Network License Manager` step of the deployment. You can find the private IP address in the *Outputs* tab of the existing network license manager deployment. 
#### Add security group of the server VMs to the security group of the license manager
If you did not supply a security group in the parameter **Security Group of Existing Network License Manager** at the time of deployment, you must add the security group of the server VMs to the security group of the license manager.
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
1. Look for the key named `MATLABWebAppServerLicenseManager` and click the corresponding URL listed under value. This opens the Network License Manager for MATLAB Dashboard login page.
1. The username is **manager**. For the password, enter the password you entered for the **Password for Network License Manager** parameter while creating the stack in [Step 2](#step-2-configure-the-stack).
1. Follow the instructions on the home page of the network license manager to upload your MATLAB Web App Server license.

>**Note:** MATLAB Web App Server automatically starts after successfully uploading a valid license file.

## Step 6. Connect and Log In to the Admin Portal (Linux Server Only)
> **Note:** The Internet Explorer web browser is not supported for accessing the admin portal. 

The MALAB Web App Server admin portal provides a web-based interface to configure and manage the server instance on the cloud. The admin portal is only available for servers deployed on Ubuntu Linux.

1. In the Stack details for your stack, click the **Outputs** tab.
1. Look for the key named `AdminPortalUrl` and click the corresponding URL listed under **value**. This opens the admin portal Overview page.
1. The first time you access the admin portal, log in using the following username and password:

    <table>
      <tr><td>Username</td><td>matlab-webapps-admin</td></tr>
      <tr><td>Password</td><td>matlab-webapps-admin</td></tr>
    </table>

1. After logging in for the first time, you are prompted to change the password.


## Step 7. Open the MATLAB Web App Server Apps Home Page
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerAppsHomePage` and click the corresponding URL listed under value. This opens the apps home page.
1. On Linux servers, user authentication to the server home page is enabled by default. The default configuration includes three user accounts you can use to log in to the server home page. Each user belongs to one or more pre-configured groups, granting them specific permissions on the MATLAB Web App Server. For instance, the **MATLAB Web App Server Authors** group includes upload and delete permissions for the web apps in the `SampleApps` folder. For more information, see [Groups](https://www.keycloak.org/docs/latest/server_admin/index.html#proc-managing-groups_server_administration_guide) in the Keycloak documentation. 

    The default credentials for the user accounts are as follows.

    |Username |Password |
    |-|-|
    |`matlab-webapps-admin`|`matlab-webapps-admin`|
    |`matlab-webapps-author`|`matlab-webapps-author`|
    |`matlab-webapps-user`|`matlab-webapps-user`|

    After you log in to a user account for the first time, you are prompted to change the password.

To run applications on MATLAB Web App Server, you need to create web apps using MATLAB Compiler. For details, see [Web Apps](https://www.mathworks.com/help/compiler/webapps/create-and-deploy-a-web-app.html) in the MATLAB Compiler product documentation.

## Step 8. Configure User Authentication

### Linux Server
On Linux servers, user authentication to the admin portal and MATLAB Web App Server home page is administered by default through [Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html). Keycloak is a cloud native solution that provides authentication, authorization, and user management for applications and services. You can configure authentication using your identity provider with Keycloak or directly using LDAP or OIDC.

After you deploy MATLAB Web App Server, log in to the Keycloak administration console to configure user authentication and change the default admin credentials.
1. In the Stack details for your stack, click the **Outputs** tab.
1. Look for the key named `KeycloakConsoleUrl` and click the corresponding URL listed under **value**. This opens the Keycloak admin console.
1. Log into the Keycloak portal using the following username and password:

    <table>
      <tr><td><b>Username</b></td><td>keycloak-admin</td></tr>
      <tr><td><b>Password</b></td><td>keycloak-admin</td></tr>
    </table>

You can set up user authentication directly with Keycloak or federate with a third party identity provider. Add or modify groups and users as needed through your authentication provider. For more information, see [Managing users](https://www.keycloak.org/docs/latest/server_admin/index.html#assembly-managing-users_server_administration_guide) in the Keycloak documentation.

### Windows Server
On Windows servers, user authentication to the MATLAB Web App Server home page is not enabled by default. To enable OIDC authentication, see [Configure OIDC Authentication](#configure-oidc-authentication).<p>

# Common Tasks

## Upload Web Apps to AWS S3 Bucket
1. In the AWS management console, select the stack that you deployed. 
1. In the *Stack details* for your stack, click the **Outputs** tab.
1. Look for the key named `MATLABWebAppServerAppsS3Bucket`, and click the corresponding URL listed under value.
1. In the S3 console, click **apps**.
1. Click **Upload** > **Add Files** to select and upload web apps (`.ctf` files).
>**NOTE 1:** If you enable user authentication, you can upload web apps from the apps home page. To configure authentication, see [Step 8](#step-8-configure-user-authentication).<p>
>**NOTE 2:**  Only folders created within the `apps` root-level folder are supported. Subfolders within those folders are not supported.

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
1. Click the **Download remote desktop file** button to download the .rdp file.
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
On Linux servers, configure authentication using Keycloak in [Step 8](#step-8-configure-user-authentication). You can also use the following steps to configure OIDC authentication manually.

On Windows servers, use the following instructions.
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

On Linux servers, you can also download logs directly from the admin portal. For details, see [Step 6](#step-6-connect-and-log-in-to-the-admin-portal-linux-server-only).

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

## Ensure connectivity in an existing VPC
If you are deploying MATLAB Web App Server to an existing VPC, you must open the following ports in your VPC:

| Port | Description |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `443` | Required for communicating with MATLAB Web App Server apps home page. |
| `8000`, `9988` | Required for communication between MATLAB Web App Server controllers  and AWS services. These ports do not need to be open to the internet. |
| `27000` | Required for communication between the network license manager and MATLAB Web App Server. |
| `3389`, `22` | Required for Remote Desktop and Secure Connection functionality. This can be used for troubleshooting and debugging MATLAB Web App Server. |

 In addition, in order for Lambda functions present in the MATLAB Web App Server reference architecture to work in an existing VPC, you must configure connectivity based on whether you choose a public or a private subnet for your deployment.

### Use public NAT gateway when deploying to a private subnet
If you are using an existing VPC and deploying in a private subnet, consider using a public NAT gateway associated with a public subnet. This setup allows the Lambda functions to communicate with AWS services. For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the AWS documentation. 

### Create interface VPC endpoint when deploying to a public subnet
If you are using an existing VPC and deploying in a public subnet, then you must add an interface VPC endpoint to one of the public subnets in the VPC. You can check if such an endpoint already exists by navigating to the AWS Console, selecting **Endpoints**, and filtering by VPC ID for the VPC you are using for deployment. If no such endpoint is present, follow these steps:

1. Click **Create endpoint**.
1. Provide a name tag for the endpoint.
1. Select **Type** as `AWS services`.
1. In **Services**, select `com.amazonaws.<AWS Region>.ec2`. The region should match your VPC region. For instance, if your region is US East 1, select `com.amazonaws.us-east-1.ec2`.
1. In **Network settings**, select the VPC you are using for deployment.
1. Ensure that **Enable DNS** is checked to facilitate DNS resolution within the VPC.
1. In **Subnets**, select the public subnet where the endpoint will be configured.
1. In **Security groups**, select the security group to associate with the endpoint network interface. Ensure the following settings are applied to the security group:<p>
    
    <table>
    <tr>
      <th colspan="2">Inbound rules</th>
    </tr>
    <tr>
      <td><b>Type</b></td><td>All TCP</td>
    </tr>
    <tr>
      <td><b>Protocol</b></td><td>TCP</td>
    </tr>
    <tr>
      <td><b>Port Range</b></td><td>0 - 65535</td>
    </tr>
    <tr>
      <td><b>Source</b></td><td>VPC CIDR block range — allows internal VPC communication on any TCP port</td>
    </tr>
    </table>

    <table>
    <tr>
      <th colspan="2">Outbound rules</th>
    </tr>
    <tr>
      <td><b>Type</b></td><td>All traffic</td>
    </tr>
    <tr>
      <td><b>Protocol</b></td><td>All</td>
    </tr>
    <tr>
      <td><b>Port Range</b></td><td>All</td>
    </tr>
    <tr>
      <td><b>Destination</b></td><td>Anywhere (0.0.0.0/0) — allows all outbound traffic to any destination</td>
    </tr>
    </table>

For detailed information on creating endpoints, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html).

# Enhancement Request
Provide suggestions for additional features or capabilities using the following link: https://www.mathworks.com/solutions/cloud.html

# Technical Support
If you require assistance or have a request for additional features or capabilities, please contact [MathWorks Technical Support](https://www.mathworks.com/support/contact_us.html).