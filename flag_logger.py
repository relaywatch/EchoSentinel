import requests

def send_flag_event(payload: dict, webhook_url: str):
    try:
        response = requests.post(webhook_url, json=payload)
        print(f"[LOG] Flag sent: {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"[LOG ERROR] {str(e)}")
        return None
