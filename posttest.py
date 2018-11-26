import sys
import requests
import json



url = 'http://localhost:3000/oauth/token'
headers = {
	"Authorization": "Basic Y29uZmlkZW50aWFsQXBwbGljYXRpb246dG9wU2VjcmV0",
	
	"Content-Type": "application/x-www-form-urlencoded"

}


data = {
	"grant_type":"client_credentials"
}

r = requests.post(url, headers=headers, data=data)

print(r.text)
print(r.json)