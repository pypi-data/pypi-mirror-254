import requests

def webhook_create(token: str, channel_id: int, name: str, **kwargs) -> dict:
    jsonData = {
            "name": name
        }
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/webhooks", headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def webhook_send(webhook_url: str, msg: str, name: int, **kwargs) -> dict:
    jsonData = {
            'content': text
        }
    header = {
        'username': name,
        'avatar_url': "",
        'Content-Type': 'application/json'
        }
    r = requests.post(webhook_url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def webhook_delete(webhook: str, **kwargs) -> dict:
    r = requests.delete(webhook)
    try:
        return r.json()
    except:
        return r.status_code
