import requests.exceptions

from Base import app

import requests
import json
import pickle
import os


class ProclaimAPI:
    _ipAddress = ''
    _passcode = ''

    #  _changeDirection = 'next'
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of ProclaimAPI.")
        return super().__new__(cls)

    def __init__(self, x):
        print("2. Initialize the new instance of ProclaimAPI.")

        self.Method = x
        config = app.read_config()

        self._ipAddress = config['Proclaim_API_Settings']['IP_Address']
        self._passcode = config['Proclaim_API_Settings']['passcode']
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self._performAction()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(method={self.Method})"

    def _performAction(self):
        print(self.Method)

        match self.Method:
            case app.ProclaimAction.Authenticate:
                print("proclaim authenticate")
                self._authenticate()
            case app.ProclaimAction.NextSlide:
                print("next slide")
                self._changeSlide('next')
            case app.ProclaimAction.PreviousSlide:
                print("previous slide")
                self._changeSlide('previous')

    def _authenticate(self):
        print("authenticate")
        url = f'http://{self._ipAddress}/appCommand/authenticate'
        print(self._ipAddress)
        # payload = "{\n\n\"Password\" : \"tbud0906\"\n\n}"
        payload = "{\n\n\"Password\" : \"" + f"{self._passcode}" + "\"\n\n}"
        # print(f"payload {payload}")
        headers = {
            'Content-Type': 'text/plain'
        }

        # noinspection PyBroadException
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
        except requests.exceptions.HTTPError as err:
            print("HTTP Error")
        except requests.exceptions.Timeout as e:
            print("Request Time Out")
        except requests.exceptions.RequestsWarning as e:
            print("Request Warning")
        except:
            print("Unable to execute Proclaim API all")
        else:

            json_object = json.loads(response.text.encode().decode('utf-8-sig'))

            accessToken = json_object["proclaimAuthToken"]
            pickleFile = open('authfile', 'wb')
            pickle.dump(accessToken, pickleFile)
            print(json_object["proclaimAuthToken"])

            pickleFile.close()
            print(response.text)

    def _changeSlide(self, direction):
        url = f"http://{self._ipAddress}/appCommand/perform?appCommandName={direction}Slide"

        payload = ''

        pickleFile = open('authfile', 'rb')
        accessToken = pickle.load(pickleFile)

        headers = {
            'ProclaimAuthToken': accessToken
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        pickleFile.close()
