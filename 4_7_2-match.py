from os import system
system("pip3 install requests")

import requests

def https_status(status):
    response = requests.get(url)
    status = response.status_code
    match status:
            case 401 | 403 | 404:
                return "error"
            case 200:
                return "nice job"
            case _:
                return "other meaning"

url = "https://www.google.com.ua/"
print(https_status(url))