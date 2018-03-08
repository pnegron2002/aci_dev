import simplejson as json
import requests
import sys



# create cookie array from token

def Get_Token(ip ='192.168.10.1'):
	login_url = 'https://{}/api/aaaLogin.json'.format(ip)
	name_pwd = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'NXos12345'}}}
	json_credentials = json.dumps(name_pwd)

	# log in to API
	requests.packages.urllib3.disable_warnings()  
	post_response = requests.post(login_url, data=json_credentials, verify=False)

	# extract token from login response structure
	auth = json.loads(post_response.text)
	login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
	auth_token = login_attributes['token']
	cookies = {}
	cookies['APIC-cookie'] = auth_token
	return cookies


#if __name__ == '__main__':
#	print('Login Script')
#Get_Token()
	