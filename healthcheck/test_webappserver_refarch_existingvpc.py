# Test for MATLAB WebApps Server Reference Architecture AWS on Windows where existing VPC is used for stack creation.
# Mathworks 2023

import refarch_testtools.deploy as deploy
import warnings
import time
import unittest
import re
import requests
import urllib
import json
import datetime
import random
from datetime import date
import sys

def main(keypairname, password, ipAddress, SSLCertificateARN, location_arg, platform_arg):
   # Reference architectures in production.
   # Deploy a stack for creating VPC with 2 subnets
    existing_template_url = "https://matlab-web-app-server-templates.s3.amazonaws.com/r2022a_refarch/VPCStack.yml"
    vpc_parameters  = [{"ParameterKey": "AllowPublicIP",
                            "ParameterValue": "Yes"}]
    existingstack = deploy.deploy_stack(existing_template_url, vpc_parameters, location_arg, "existingvpc")
    time.sleep(90)
    vpc_id = deploy.get_stack_output_value(existingstack, 'VPCID')
    vpc_cidr = deploy.get_stack_output_value(existingstack, 'VPCCIDR')
    subnet1 = deploy.get_stack_output_value(existingstack, 'Subnet1')
    subnet2 = deploy.get_stack_output_value(existingstack, 'Subnet2')
    subnet3 = deploy.get_stack_output_value(existingstack, 'Subnet3')
    ref_arch_name = 'matlab-web-app-server-on-aws'
    parameters = [{'ParameterKey': 'KeyPairName', 'ParameterValue': keypairname},
                  {'ParameterKey': 'AdminIPAddress', 'ParameterValue': ipAddress},
                  {'ParameterKey': 'Password', 'ParameterValue': password},
                  {'ParameterKey': 'ConfirmPassword', 'ParameterValue': password},
                  {'ParameterKey': 'SSLCertificateARN', 'ParameterValue': SSLCertificateARN},
                  {'ParameterKey': 'WorkerSystem', 'ParameterValue': platform_arg},
                  {'ParameterKey': 'WorkerInstanceType', 'ParameterValue': 'm5.xlarge'},
                  {'ParameterKey': 'UseSameIPForClient', 'ParameterValue': 'Yes'},
                  {'ParameterKey': 'ExistingVPC', 'ParameterValue': vpc_id},
                  {'ParameterKey': 'ExistingVPCAddress', 'ParameterValue': vpc_cidr},
                  {'ParameterKey': 'ExistingSubnet1', 'ParameterValue': subnet1},
                  {'ParameterKey': 'ExistingSubnet2', 'ParameterValue': subnet2},
                  {'ParameterKey': 'ExistingSubnet3', 'ParameterValue': subnet3},
                  {'ParameterKey': 'DeployLicenseServer', 'ParameterValue': 'Yes'},
                  {'ParameterKey': 'ExistingLicenseServer', 'ParameterValue': '0.0.0.0'}]

    # Find latest MATLAB release from Github page and get template url text
    res = requests.get(f"https://github.com/mathworks-ref-arch/{ref_arch_name}/blob/master/releases/")

    # Deploy a stack for the latest two releases
    latest_releases = [re.findall("main/releases/(R\d{4}[ab]\\b)", res.text)[-1], re.findall("main/releases/(R\d{4}[ab]\\b)", res.text)[-2]]
    number_of_releases = 2
    for i in range(number_of_releases):
        matlab_release = latest_releases[i]
        print("Testing Health Check Release: " + matlab_release + "\n")
        github_base_dir = "https://raw.githubusercontent.com/mathworks-ref-arch"

        # Getting template url from .txt file
        # NOTE for code cleanup: Delete this branch after next release
        if matlab_release == "R2021b":
            template_url_path = f"{github_base_dir}/{ref_arch_name}/master/releases/{matlab_release}/templates.txt"
            file = urllib.request.urlopen(template_url_path)
            template_url = file.readline().decode("utf-8").rstrip()

        # Getting template url from .json file
        else:
            template_url_path = f"{github_base_dir}/{ref_arch_name}/main/releases/{matlab_release}/templates.json"
            response = urllib.request.urlopen(template_url_path)
            template_json = json.loads(response.read())
            template_url = template_json["WebAppServer_existing.yml"]
        stack_name = "mwas-refarch-health-check-existing-vpc" + matlab_release + date.today().strftime('%m-%d-%Y') + str(random.randint(1,101))
        ct = datetime.datetime.now()
        print("Date time before deployment of stack:-", ct)

        # Deploying the stack
        try:
            print("deploying the stack")
            stack = deploy.deploy_stack(template_url, parameters, location_arg, stack_name)
            print("success deploying the stack")
        except Exception as e:
            raise (e)

        # Delete the deployment
        print("deleting the stack")
        deploy.delete_stack(stack)
        print("success deleting the stack")
        ct = datetime.datetime.now()
        print("Date time after deployment and deletion of stack:-", ct)
        print("\n\n")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
