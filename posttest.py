import sys
import requests
import json
import base64





def post_():

	username = sys.argv[1]
	password = sys.argv[2]
	host = sys.argv[3]

	hash_ = base64.b64encode(username + ':' + password)
	auth_hash = "Basic %s"%hash_

	print (auth_hash)

	if host[-1] == '/':
		url = host + 'oauth/token'
	else:
		url = host + '/oauth/token'

	headers = {
		"Authorization": auth_hash,
		
		"Content-Type": "application/x-www-form-urlencoded"
	}

	data = {
		"grant_type":"client_credentials"
	}

	r = requests.post(url, headers=headers, data=data)

	print(r.text)
	at = r.json()['access_token']
	print(at)
	f = open('accessToken.txt','w')
	f.write(at)
	f.close()


def get_():

	f = open(sys.argv[1],'r')
	at = f.read()
	auth_hash = "Bearer %s"%at
	host = sys.argv[2]

	headers = {
		"Authorization": auth_hash,

	}

	r = requests.get(host, headers=headers)
	print(r.text)

if __name__ == '__main__':
	
	if len(sys.argv) == 4:
		post_()
	elif len(sys.argv) == 3:
		get_()
	else:
		print('argumrnt error')