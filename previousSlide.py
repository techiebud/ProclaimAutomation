import requests
import pickle

url = "http://192.168.7.62:52195/appCommand/perform?appCommandName=previousSlide"
payload = ''

pickleFile = open('authfile', 'rb')
accessToken = pickle.load(pickleFile)

headers = {
  'ProclaimAuthToken': accessToken
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
pickleFile.close()
