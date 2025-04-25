import requests
import json

url = "https://webhook.site/833440dc-c6d5-472e-8b76-3206541438fa"  # <- Replace this with yours

payload = {
    "message": "This is a test",
    "volatility": 0.99,
    "action": "flag"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
