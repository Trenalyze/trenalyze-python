from trenalyze_python import Trenalyze

token = "w0bW6GuaQjKUog5GXOJb"
sender = "2347019491161"
receiver = "2348157002782"
msgtext = "From Trenalyze Python Module"

trenalyze = Trenalyze(token, sender, receiver, msgtext, True)

print(trenalyze.send())