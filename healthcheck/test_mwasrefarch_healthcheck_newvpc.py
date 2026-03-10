# Health Check tests for MATLAB Web App Server Reference Architecture
# Mathworks 2023-2026

import refarch_testtools.deploy as deploy
import refarch_testtools.git_utils as git_utils
import sys
import requests
import datetime
import urllib.request
import random
from datetime import date
import json
import traceback


def main(keypairname, password, location_arg, platform_arg, git_token):
    # Reference architectures in production.
    ref_arch_name = 'matlab-web-app-server-on-aws'
    branch_name = git_utils.get_current_branch()
    
    ipAddress = requests.get("https://api.ipify.org").text + "/32"
    
    parameters = [
        {'ParameterKey': 'KeyPairName', 'ParameterValue': keypairname},
        {'ParameterKey': 'AdminIPAddress', 'ParameterValue': ipAddress},
        {'ParameterKey': 'Password', 'ParameterValue': password},
        {'ParameterKey': 'ConfirmPassword', 'ParameterValue': password},
        {'ParameterKey': 'WorkerSystem', 'ParameterValue': platform_arg},
        {'ParameterKey': 'UseSameIPForClient', 'ParameterValue': 'Yes'}
    ]
    
    # With a GitHub token
    headers = {
        'Authorization': f'token {git_token}'
    }
    
    # Use GitHub API which has clearer rate limits
    api_url = f"https://api.github.com/repos/mathworks-ref-arch/{ref_arch_name}/contents/releases?ref={branch_name}"
    res = requests.get(api_url, headers=headers)
    
    if res.status_code != 200:
        print(f"Error fetching releases from GitHub API: {res.status_code}")
        print(f"Response: {res.text}")
        raise Exception(f"Failed to fetch releases from GitHub API")
    
    files = res.json()
    # Extract release names from file names and sort to get latest
    releases = sorted([f['name'] for f in files if f['name'].startswith('R')], reverse=True)
    
    if len(releases) < 2:
        print(f"Warning: Found only {len(releases)} release(s). Expected at least 2.")
    
    # Get the two latest releases (but only deploy one as per original code)
    latest_releases = releases[:2]
    number_of_releases = 1
    
    for i in range(number_of_releases):
        if i >= len(latest_releases):
            print(f"Warning: Only {len(latest_releases)} releases available, skipping index {i}")
            continue
            
        matlab_release = latest_releases[i]
        print(f"Testing Health Check Release: {matlab_release}\n")
        
        github_base_dir = "https://raw.githubusercontent.com/mathworks-ref-arch"
        # Getting template url from .json file
        template_url_path = f"{github_base_dir}/{ref_arch_name}/{branch_name}/releases/{matlab_release}/templates.json"
        
        try:
            response = urllib.request.urlopen(template_url_path)
            template_json = json.loads(response.read())
            template_url = template_json["WebAppServer_new.yml"]
        except Exception as e:
            print(f"Error fetching template URL from {template_url_path}: {e}")
            raise e
        
        stack_name = f"mwas-refarch-health-check-{matlab_release}-{date.today().strftime('%m-%d-%Y')}-{random.randint(1,101)}"
        
        ct = datetime.datetime.now()
        print(f"Date time before deployment of stack: {ct}")
        
        stack = None
        # Deploying the stack
        try:
            print("Deploying the stack")
            stack = deploy.deploy_stack(template_url, parameters, location_arg, stack_name)
            print("Success deploying the stack")
        except Exception as e:
            print(f"Error deploying stack: {e}")
            traceback.print_exc()
            raise e
        finally:
            # Delete the deployment
            if stack:
                print(f"Deleting the stack: {stack_name}")
                deploy.delete_stack(stack)
                print("Success deleting the stack")
                ct = datetime.datetime.now()
                print(f"Date time after deployment and deletion of stack: {ct}")
                print("\n\n")
            else:
                print("No stack to delete")


if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Error: Missing required arguments")
        print("Usage: python script.py <keypairname> <password> <location> <platform> <git_token>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
