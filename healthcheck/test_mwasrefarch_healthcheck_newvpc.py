# Health Check tests for MATLAB Web App Server Reference Architecture

import refarch_testtools.deploy as deploy
import sys
import re
import requests
import datetime
import urllib
import random
from datetime import date
import json

def main(keypairname, password, ipAddress, location_arg, platform_arg):
    # Reference architectures in production.
    ref_arch_name = 'matlab-web-app-server-on-aws'
    parameters = [{'ParameterKey': 'KeyPairName', 'ParameterValue': keypairname},
                  {'ParameterKey': 'AdminIPAddress', 'ParameterValue': ipAddress},
                  {'ParameterKey': 'Password', 'ParameterValue': password},
                  {'ParameterKey': 'ConfirmPassword', 'ParameterValue': password},
                  {'ParameterKey': 'WorkerSystem', 'ParameterValue': platform_arg},
                  {'ParameterKey': 'UseSameIPForClient', 'ParameterValue': 'Yes'}]

    # Find latest MATLAB release from Github page and get template url text
    res = requests.get(f"https://github.com/mathworks-ref-arch/{ref_arch_name}/blob/master/releases/")

    # Deploy a stack for the latest two releases
    latest_releases = [re.findall("releases/(R\d{4}[ab]\\b)", res.text)[-1], re.findall("releases/(R\d{4}[ab]\\b)", res.text)[-2]]
    number_of_releases = 1
    for i in range(number_of_releases):
        matlab_release = latest_releases[i]
        print("Testing Health Check Release: " + matlab_release + "\n")
        github_base_dir = "https://raw.githubusercontent.com/mathworks-ref-arch"

        # Getting template url from .json file
        template_url_path = f"{github_base_dir}/{ref_arch_name}/main/releases/{matlab_release}/templates.json"
        response = urllib.request.urlopen(template_url_path)
        template_json = json.loads(response.read())
        template_url = template_json["WebAppServer_new.yml"]

        stack_name = "mwas-refarch-health-check-" + matlab_release + date.today().strftime('%m-%d-%Y') + str(random.randint(1,101))
        ct = datetime.datetime.now()
        print("Date time before deployment of stack:-", ct)

        # Deploying the stack
        try:
            print("deploying the stack")
            stack = deploy.deploy_stack(template_url, parameters, location_arg, stack_name)
            print("success deploying the stack")
        except Exception as e:
            raise (e)
        finally:
            # Delete the deployment
            print("deleting the stack")
            deploy.delete_stack(stack)
            print("success deleting the stack")
            ct = datetime.datetime.now()
            print("Date time after deployment and deletion of stack:-", ct)
            print("\n\n")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
