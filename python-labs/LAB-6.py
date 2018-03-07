#import the neccessary modules

import time
import sys
import getpass
import paramiko

#setup the variables used in the script 
 
ip = '10.10.10.1'
username = "admin"
password = getpass.getpass()

#Execute the main part of the code

login_url = 'https://{}/api/aaaLogin.json'.format(ip)
name_pwd = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
json_credentials = json.dumps(name_pwd)

# log in to API - Disable login warnings

requests.packages.urllib3.disable_warnings()  
post_response = requests.post(login_url, data=json_credentials, verify=False)

# extract token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']
cookies = {}
cookies['APIC-cookie'] = auth_token
return cookies