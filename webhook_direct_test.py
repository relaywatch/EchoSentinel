# 🔐 Webhook Test – Public-Safe Version
# Replace 'your-webhook-url' with your private URL for testing

import requests
import json

# Placeholder URL – DO NOT use real webhook in public
url = "https://your-webhook-url"  # Replace this in private use

payload = {
    "message": "This is a test",
    "volatility": 0.99,
    "action": "flag"
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
except Exception as e:
    print("Webhook request failed:", e)
