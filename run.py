from trenalyze_python import Trenalyze

token = "w0bW6GuaQjKUog5GXOJb"
sender = "2347019491161"
receiver = "2348157002782"
msgtext = "From Trenalyze Python Module Happy Birthday"

trenalyze = Trenalyze()
trenalyze.setToken(token)
trenalyze.setSender(sender)
trenalyze.setReceiver(receiver)
trenalyze.setMsgtext(msgtext)
trenalyze.setDebug(True)

print(trenalyze.sendMessage())