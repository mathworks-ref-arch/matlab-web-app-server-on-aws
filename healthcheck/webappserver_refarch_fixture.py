# This is fixture that is used for MATLAB Web App Server Ref Arch tests on AWS.
# Mathworks 2022

from util import RefArchTest
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import refarch_testtools.deploy as deploy
import refarch_testtools.s3_operations as s3_op
import lm_dashboard_operations as LMDashboardOp
import refarch_testtools.config as config
import refarch_testtools.webapps_homepage_operations as hp_op
from datetime import datetime

import os.path
import re
import time
import warnings
import unittest
import urllib3
import requests
import boto3
from botocore.exceptions import NoCredentialsError
import os
# NOTES: Maximum 30 second wait time
WAIT_TIME = 30

class MWASRefArchAutoTestFixture(RefArchTest):
    def __init__(self, region, param_file, platform, template_environ, existingvpc):
        self.region = region
        self.param_file_name = param_file
        self.param_file = self._get_param_path(self.param_file_name)
        self.platform = {'WorkerSystem' : platform}
        self.template_url = os.environ[template_environ]
        self.existingvpc = existingvpc

    def setUp(self):
        extra_parameters = self.platform
        if self.existingvpc:
            params_file_for_vpc = "create_vpc_params.json"
            vpcparam_file = self._get_param_path(params_file_for_vpc)

            # Deploy a stack for creating VPC with 2 subnets
            existing_template_url = "https://matlab-web-app-server-templates.s3.amazonaws.com/r2022a_refarch/VPCStack.yml"
            self.existingstack = deploy.deploy_stack(existing_template_url, vpcparam_file, self.region, "existingvpc")
            time.sleep(90)
            vpc_id = deploy.get_stack_output_value(self.existingstack, 'VPCID')
            vpc_cidr = deploy.get_stack_output_value(self.existingstack, 'VPCCIDR')
            subnet1 = deploy.get_stack_output_value(self.existingstack, 'Subnet1')
            subnet2 = deploy.get_stack_output_value(self.existingstack, 'Subnet2')
            subnet3 = deploy.get_stack_output_value(self.existingstack, 'Subnet3')
            vpc_parameters = {'ExistingVPC' : vpc_id, 'ExistingVPCAddress' : vpc_cidr,
            'ExistingSubnet1': subnet1, 'ExistingSubnet2': subnet2, 'ExistingSubnet3' : subnet3, 'DeployLicenseServer' : "Yes", "ExistingLicenseServer" : '0.0.0.0'}
            extra_parameters.update(vpc_parameters)
        self.stack = deploy.deploy_stack(self.template_url, self.param_file, self.region, "mwasRefArchAutoTest", extra_parameters)

    def upload_license(self):
        # Get license file path and license manager URL to login and upload license
        splitString=self.template_url.split('/')
        release = 'R' + splitString[3][1:6]
        licensefilepath = f"\\\\mathworks\\inside\\labs\\dev\\it_tracker\\install\\passcodes\\{release}\\license10.lic"
        # licensefilepath = os.path.join(os.path.dirname(__file__), "licensefile")
        licensemanager_dashboardurl = deploy.get_stack_output_value(self.stack, 'MATLABWebAppServerLicenseManager')

        # Get credentials from the parameter file
        parameters = config.read_template_parameter_file(self._get_param_path(self.param_file_name))
        username = "manager"
        password = config.get_param_value(parameters, "Password")
        
        # Login to Network License Manager Dashboard
        session = requests.Session()
        LMDashboardOp.login_to_licensemanager_dashboard(
        session, licensemanager_dashboardurl, username, password)
        LMDashboardOp.upload_license_using_license_file(
                session, licensemanager_dashboardurl, licensefilepath)

    def upload_ctfs(self):
        # Get path to CTFs and bucket
        file_path = os.path.dirname(__file__)
        self.ctfpath = os.path.join(file_path, "CTFs")
        s3_url = deploy.get_stack_output_value(self.stack, 'MATLABWebAppServerAppsS3Bucket')
        s3_op.uploadCTFtoS3(self.ctfpath, "apps/", s3_url)

    def launch_homepage(self):
        # Launch and verify home page
        self.homepageurl = deploy.get_stack_output_value(self.stack, "MATLABWebAppServerAppsHomePage")
        self.driver.get(self.homepageurl)
        assert "MATLAB Web Apps" in self.driver.title, print("MATLAB Web Apps Home Page launch unsuccessful")
        print(str(datetime.now()) + ': MATLAB Web Apps Home Page successfully launched')

    def start_webdriver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.get_chrome_browser_executable_path()
        
        # Ignore warnings
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Create webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="91.0.4472.19").install()), options=options)

    def page_interactions(self):
        # Launch and verify home page
        self.launch_homepage()

        # Launch and verify diagnostics
        hp_op.verify_diagnostics(self.driver)
        print(str(datetime.now()) + ': Diagnostics Page successfully launched')

        # Verify CTF upload in diagnostics
        hp_op.verify_ctf_upload(self.driver, self.ctfpath)
        print(str(datetime.now()) + ': Verified CTF uploads exist in Diagnostics')

        # Verify CTF status messages in diagnostics
        # self.webapp_count = hp_op.verify_ctf_status(self.driver, self.template_url)
        hp_op.verify_ctf_status(self.driver, self.template_url)
        print(str(datetime.now()) + ': Verified CTF upload success messages in Diagnostics')

        # Return to home page
        self.driver.find_element(By.CLASS_NAME, "bannerTitleLink").click()

    def webapps_launch(self):
         # Verify successful launch of web apps on home page
        webapp_count = hp_op.num_webapps(self.driver, self.homepageurl)
        if webapp_count > 0:
            hp_op.verify_webapps_launch(self.driver)
            print(str(datetime.now()) + ': All Web Apps loaded successfully')

    def ctf_error(self):
        # Launch and verify home page
        self.launch_homepage()

        # Wait until web apps show up on home page
        hp_op.wait_until(self.driver, By.CSS_SELECTOR, ".CardContainer.appStatusOk", "Timeout error while waiting for web apps visibility")
        
        # Launch Error App
        apps = self.driver.find_elements(By.CLASS_NAME, "FormattedSectionLink")
        titles = self.driver.find_elements(By.CLASS_NAME, "appTitle")
        error_app = None
        for i in range(len(apps)):
            if titles[i].text == "ErrorApp":
                error_app = apps[i].get_attribute('href')
        if not error_app:
            raise Exception("Error CTF not found")
        log_buttons = hp_op.launch_webapp(error_app, self.driver)

        # Wait for web app to lead
        time.sleep(5)
        hp_op.wait_until(self.driver, By.CLASS_NAME, "mwTextLine", "Timeout error while waiting for web app to load")
        
        # Throw error and warning
        webapp_buttons = self.driver.find_elements(By.CLASS_NAME, "mwTextLine")
        for button in webapp_buttons:
            if button.text == "Throw an Error":
                button.click()
            elif button.text == "Throw warning":
                button.click()
        
        # Assert error and warning thrown
        hp_op.wait_for_log_content(log_buttons[1], self.driver, 3)

        # Gather log output content
        log_messages = self.driver.find_elements(By.CLASS_NAME, "logOutContent")
        log_messages = list(map(lambda x: x.text, log_messages))

        # Check for session created successfully message
        warning = False
        for message in log_messages:
            if 'Warning: warn!' in message:
                warning = True
        error = self.driver.find_elements(By.CLASS_NAME, "logErrorContent")
        assert error
        assert warning
        print(str(datetime.now()) + ': Errors and Warnings verified')

    def quit_webdriver(self):
        # Exit
        self.driver.quit()

    def tearDown(self):
        deploy.delete_stack(self.stack)
        if self.existingvpc :
            deploy.delete_stack(self.existingstack)