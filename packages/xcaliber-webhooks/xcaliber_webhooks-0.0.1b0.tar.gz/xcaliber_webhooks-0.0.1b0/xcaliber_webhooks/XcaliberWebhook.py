from svix.webhooks import Webhook

class XcaliberWebhook:
    def __init__(self,secret):
        self.__xcaliberWebhook=Webhook(secret)
    def verify(self,payload,headers):
        return self.__xcaliberWebhook.verify(payload,headers)