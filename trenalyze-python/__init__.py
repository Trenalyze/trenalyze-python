import requests
from requests.structures import CaseInsensitiveDict

url = "https://trenalyze.com/api/send"

headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/json'

data = """
{
    "token": "w0bW6GuaQjKUog5GXOJb",
    "sender": "2347019491161",
    "receiver": "2348157002782",
    "msgtext": "Testing load balancer live real"
}
"""

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)