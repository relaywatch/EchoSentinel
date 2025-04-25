import requests
import json

def send_flag_event(payload: dict, webhook_url=None):
    try:
        # 🔁 This is the temporary relay vault endpoint
        endpoint = "https://echo-relay.glitch.me/flag"
        headers = {"Content-Type": "application/json"}
        requests.post(endpoint, data=json.dumps(payload), headers=headers)
        print("[LOG] Flag sent to vault")
    except Exception as e:
        print("[LOG ERROR]", str(e))
