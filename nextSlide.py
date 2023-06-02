#!/usr/bin/env python3
import requests
import pickle
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
url = "http://192.168.7.62:52195/appCommand/perform?appCommandName=nextSlide"
payload = ''

pickleFile = open('authfile', 'rb')
accessToken = pickle.load(pickleFile)

headers = {
  'ProclaimAuthToken': accessToken
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
pickleFile.close()
