import requests
from requests.structures import CaseInsensitiveDict

class Trenalyze:
    def __init__(self, token, sender, receiver, msgtext):
        self.token = token
        self.sender = sender
        self.receiver = receiver
        self.msgtext = msgtext

    def __getUrl(self):
        url = "https://trenalyze.com/api/send"
        return url

    def __sendRequest(self):
        data = """
        {
            "token": self.token,
            "sender": self.sender,
            "receiver": self.receiver,
            "msgtext": self.msgtext
        }
        """
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = 'application/json'
        resp = requests.post(self.__getUrl(), headers=headers, data=data)
        return resp.status_code
    
    def send(self):
        return self.__sendRequest()

