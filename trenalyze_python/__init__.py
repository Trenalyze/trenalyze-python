import requests
from requests.structures import CaseInsensitiveDict
import json

class Trenalyze:
    def __init__(self):
        pass

    def setToken(self, token):
        self.token = token
    
    def setSender(self, sender):
        self.sender = sender

    def setReceiver(self, receiver):
        self.receiver = receiver
    
    def setMsgtext(self, msgtext):
        self.msgtext = msgtext

    def setDebug(self, debug = False):
        self.debug = debug

    def __getUrl(self):
        url = "https://trenalyze.com/api/send"
        return url

    def __sendRequest(self):

        try:
            headers = CaseInsensitiveDict()
            headers['Content-Type'] = 'application/json'

            url = self.__getUrl()

            data = {
                "sender": self.sender,
                "token": self.token,
                "receiver": self.receiver,
                "msgtext": self.msgtext
            }
            
            resp = requests.post(url = self.__getUrl(), data=json.dumps(data), headers=headers)
            if resp.status_code == 200:
                return resp.json()
            else:
                if self.debug == True:
                    return "Error: {}".format(resp.status_code)
                else:
                    return "Sorry an Error Occured. Kindly enable debug mode to see more details"
        except Exception as e:
            if self.debug == True:
                return "Error: {}".format(e)
            else:
                return "Sorry an Error Occured. Kindly enable debug mode to see more details"

    def sendMessage(self):
        #make sure sender and receiver are numbers and its not empty
        if self.sender == "":
            return "Sender cannot be empty"

        #if receiver is empty
        if self.receiver == "":
            return "Receiver cannot be empty"

        #if sender is not a number
        if not self.sender.isdigit():
            return "Sender must me a valid Phone Number"

        #if receiver is not a number
        if not self.receiver.isdigit():
            return "Receiver must me a valid Phone Number"

        #if token is empty
        if self.token == "":
            return "Token is Required"

        #if token length is less than 32
        if len(self.token) < 20:
            return "Invalid Token. Kindly Re Confirm Token"
            
        return self.__sendRequest()

