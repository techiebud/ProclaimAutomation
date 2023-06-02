#!/usr/bin/env python3
import requests
import json
import pickle
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
url = "http://192.168.7.62:52195/appCommand/authenticate"

payload = "{\n\n\"Password\" : \"tbud0906\"\n\n}"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)
json_object = json.loads(response.text.encode().decode('utf-8-sig'))

accessToken = json_object["proclaimAuthToken"]
pickleFile = open('authfile', 'wb')
pickle.dump(accessToken, pickleFile)
print(json_object["proclaimAuthToken"])

authToken = json_object["proclaimAuthToken"]
pickleFile.close()
print(response.text)


