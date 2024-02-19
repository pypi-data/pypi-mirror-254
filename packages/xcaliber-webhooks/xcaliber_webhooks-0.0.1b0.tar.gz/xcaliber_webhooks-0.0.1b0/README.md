# Introduction
Verify webhook events from xcaliber

# Usage:
Install package using following command - pip install xcaliber_webhooks
Use the below example to verify webhook -
from xcaliber_webhooks import Webhook

secret="" //secret key for webhook
webhook = Webhook(secret)
headers = {
"svix-id": "",
"svix-timestamp": "",
"svix-signature": "",
}
payload = '{}' //sample payload
webhook.verify(payload, headers)