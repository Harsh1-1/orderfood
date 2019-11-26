import requests

class Flock():

    def __init__(self):
        pass

    # This function is used to send a message to a person on flock
    def send_message(self,fromToken, toUserId, message):
        r = requests.get("https://api.flock.co/v1/chat.sendMessage?to=" + toUserId + "&text=" + message + "&token=" + fromToken)
        return r.status_code