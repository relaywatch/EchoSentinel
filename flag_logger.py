import requests
import json

def send_flag_event(payload: dict, webhook_url: str):
    try:
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        print("[LOG] Webhook response:", response.status_code)
        return response.status_code
    except Exception as e:
        print("[LOG ERROR]", str(e))
        return None
