import requests
from datetime import datetime, timezone

def timeout(token: str, server_id: int, user_id: int, mode: int, **kwargs) -> dict:
    utc_now = datetime.now(timezone.utc)
    utc_now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    if mode <= 0 or mode >= 7:
        raise ValueError
    if mode == 1: #switch文？なにそれおいしいの？（ あ　ほ　く　さ
        disabledate = f"{utc_now.strftime('%Y-%m-%dT%H:')}{utc_now.minute+1}{utc_now.strftime(':%S.%fZ')}"
    elif mode == 2:
        disabledate = f"{utc_now.strftime('%Y-%m-%dT%H:')}{utc_now.minute+5}{utc_now.strftime(':%S.%fZ')}"
    elif mode == 3:
        disabledate = f"{utc_now.strftime('%Y-%m-%dT%H:')}{utc_now.minute+10}{utc_now.strftime(':%S.%fZ')}"
    elif mode == 4:
        disabledate = f"{utc_now.strftime('%Y-%m-%dT')}{utc_now.hour+1}{utc_now.strftime(':%M:%S.%fZ')}"
    elif mode == 5:
        disabledate = f"{utc_now.strftime('%Y-%m-')}{utc_now.day+1}{utc_now.strftime('T%H:%M:%S.%fZ')}"
    elif mode == 6:
        disabledate = f"{utc_now.strftime('%Y-%m-')}{utc_now.day+7}{utc_now.strftime('T%H:%M:%S.%fZ')}"
        
    url = f"https://discord.com/api/v9/guilds/{server_id}/members/{user_id}"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData = {
        "communication_disabled_until": disabledate
        #"communication_disabled_until":"2024-01-13T19:12:55.595Z"
    }
    r = requests.patch(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def untimeout(token: str, server_id: int, user_id: int, **kwargs) -> dict:
    utc_now = datetime.now(timezone.utc)
    now = utc_now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    url = f"https://discord.com/api/v9/guilds/{server_id}/members/{user_id}"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData = {
        "communication_disabled_until": now
    }
    r = requests.patch(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def kick(token: str, server_id: int, user_id: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/guilds/{server_id}/members/{user_id}"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    r = requests.delete(url, headers = header)
    try:
        return r.json()
    except:
        return r.status_code

def ban(token: str, server_id: int, user_id: int, deletemsg_time: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/guilds/{server_id}/bans/{user_id}"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData= {
        "delete_message_seconds": deletemsg_time
    }
    r = requests.put(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def all_reaction_delete(token: str, channel_id: int, msg_id: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{msg_id}/reactions"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    r = requests.delete(url, headers = header)
    try:
        return r.json()
    except:
        return r.status_code
