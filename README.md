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

The default MATLAB Web App Server deployment template uses the Network License Manager for MATLAB reference architecture to manage MATLAB Web App Server licenses. The template for using an existing VPC for the deployment provides an option to either deploy the Network License Manager or use your own license server. For more information about the Network License Manager for MATLAB reference architecture, see [Network License Manager for MATLAB on Amazon Web Services](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).


# Prepare Your AWS Account
1. If you do not have an AWS account, create one at https://aws.amazon.com by following the on-screen instructions.
2. Use the regions selector in the navigation bar to choose **US EAST (N. Virginia)**, **EU (Ireland)** or **Asia Pacific (Tokyo)** as the region where you want to deploy MATLAB Web App Server.
3. Create a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in that region. A key pair is necessary since it is the only way to connect to the EC2 instance as an administrator.
4. If necessary, [request a service limit increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-) for the Amazon EC2 instance type or VPCs.  You might need to do this if you already have existing deployments that use that instance type or you think you might exceed the [default limit](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) with this deployment.

# Deploy Reference Architecture for Your Release
To deploy the reference architecture, select your MATLAB Web App Server release from the table and follow the instructions to deploy the server using the provided template. A deployment of MATLAB Web App Server supports MATLAB Runtime versions up to six releases back.
| Release | Supported MATLAB Runtime Versions |
| ------- | --------------------------------- |
| [R2025a](releases/R2025a/README.md) | R2025a, R2024b, R2024a, R2023b, R2023a*, R2022b* |
| [R2024b](releases/R2024b/README.md) | R2024b, R2024a, R2023b, R2023a*, R2022b*, R2022a* |
| [R2024a](releases/R2024a/README.md) | R2024a, R2023b, R2023a, R2022b, R2022a, R2021b |
| [R2023b](releases/R2023b/README.md) | R2023b, R2023a, R2022b, R2022a, R2021b |
| [R2023a](releases/R2023a/README.md) | R2023a, R2022b, R2022a, R2021b, R2021a, R2020b |
| [R2022b](releases/R2022b/README.md) | R2022b, R2022a, R2021b, R2021a, R2020b, R2020a |

> \*When the server is configured to use MATLAB Runtime versions prior to R2023b, the `unsafe-inline` attribute is set in the `script-src` directive of the Content Security Policy on the server and cannot be disabled. This allows web apps with embedded JavaScript to execute on the server. These runtimes are disabled by default starting in R2024b. You can enable them using the [webapps-runtime](https://www.mathworks.com/help/webappserver/ref/webappsruntime.html) command.

**Note**: MathWorks provides templates for only the six most recent releases of MATLAB Web App Server. Earlier templates are removed and are no longer supported.

# Architecture and Resources
Deploying this reference architecture creates several resources in your
resource group.

![Cluster Architecture](/releases/R2024a/images/mwas-ref-arch-aws-architecture-diagram.png?raw=true)

*Architecture on AWS*

### Resources

| Resource Type                                                              | Number of Resources | Description                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AWS EC2 Instance                                                           | 2                   | This resource consists of two virtual machines (VMs):<ul><li>A VM that hosts the MATLAB Web App Server.</li><li>A VM that hosts the Network License Manager for MATLAB. For more information, see [Network License Manager for MATLAB](https://github.com/mathworks-ref-arch/license-manager-for-matlab-on-aws).</li></ul>   |
| S3 Bucket                                                                  | 1                  | S3 storage bucket created during the creation of the stack. This resource stores the applications deployed to the reference architecture.                                                                                                                                                                                                  |
| Virtual Private Cloud (VPC)                                              | 1                   | Enables resources to communicate with each other.                                           |
| CloudWatch | 1 | Enables viewing of logs. |


# Enhancement Request
Provide suggestions for additional features or capabilities using the following link: https://www.mathworks.com/solutions/cloud.html

# Technical Support
If you require assistance or have a request for additional features or capabilities, please contact [MathWorks Technical Support](https://www.mathworks.com/support/contact_us.html).