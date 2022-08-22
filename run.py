# Importing the Trenalyze class from the trenalyze_python module.
from trenalyze__python import Trenalyze

# The API key for the Trenalyze API.
token = "w0bW6GuaQjKUog5GXOJb"

# This is the sender's phone number.
sender = "2347019491161"

# This is the receiver's phone number.
receiver = "2348157002782"

# This is the message text.
msgtext = "From Trenalyze Python Module Happy Birthday"

mediaurl = "https://trenalyze.com/users/1/avatar.png"

# create an array of buttons that will be sent to the user
buttons = [
    {
        "index": "1",
        "urlButton": {
            "displayText": "Click Me",
            "url": "https://www.google.com"
        }
    }
]

# Creating an instance of the Trenalyze class.
trenalyze = Trenalyze()

# Setting the API key for the Trenalyze API.
trenalyze.setToken(token)

# Setting the sender's phone number.
trenalyze.setSender(sender)

# Setting the receiver's phone number.
trenalyze.setReceiver(receiver)

# Setting the message text.
trenalyze.setMsgtext(msgtext)

# Setting the media url.
trenalyze.setMediaUrl(mediaurl)

#setting the buttons
trenalyze.setButtons(buttons)

# Setting the debug mode to True/False.
trenalyze.setDebug(True)

# Sending the message.
print(trenalyze.sendMessage())