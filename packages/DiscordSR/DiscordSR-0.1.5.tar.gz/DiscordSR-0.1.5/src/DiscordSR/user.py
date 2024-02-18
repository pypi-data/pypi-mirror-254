import requests

def status( token: str, msg: str, **kwargs) -> dict:
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    text = msg
    jsonData = {
        "status": "online",
        "custom_status": {
            "text": text

        }
    }
    r = requests.patch(f"https://discord.com/api/v8/users/@me/settings", headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def send(token: str, channel_id: int, msg: str, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData= {
        "content": msg
    }
    r = requests.post(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def sticker_send(token: str, channel_id: int, sticker_id: list, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",
    }
    jsonData= {
        "content": "",
        "sticker_ids": sticker_id
    }
    r = requests.post(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def tts_send(token: str, channel_id: int, msg: str, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData= {
        "content": msg,
        "tts": "true"
    }
    r = requests.post(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def bump(token: str, server_id: int, channel_id: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/interactions"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData= {
        "type":2,
        "application_id":"302050872383242240",
        "guild_id":server_id,
        "channel_id":channel_id,
        "session_id":"2be1fde9927afc846dc7a671abfe294a",
        "data":{
            "version":"1051151064008769576",
            "id":"947088344167366698",
            "name":"bump",
            "type":1,
            "options":[],
            "application_command":{
                "id":"947088344167366698",
                "type":1,
                "application_id":"302050872383242240",
                "version":"1051151064008769576",
                "name":"bump",
                "description":"Pushes your server to the top of all your server's tags and the front page",
                "description_default":"Pushes your server to the top of all your server's tags and the front page",
                "integration_types":[0],
                "options":[],
                "description_localized":"このサーバーの表示順をアップするよ",
                "name_localized":"bump"
            },
            "attachments":[]
        },
        "nonce":"1193586197746679808",
        "analytics_location":"slash_ui"
    }
    r = requests.post(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def dissoku(token: str, server_id: int, channel_id: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/interactions"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData = {
        "type": 2,
        "application_id": "761562078095867916",
        "guild_id": str(server_id),
        "channel_id": str(channel_id),
        "session_id": "b9042397361b864260e6c64300ce238e",
        "data": {
            "version": "1020017533245468672",
            "id": "828002256690610256",
            "name": "dissoku",
            "type": 1,
            "options": [
            {
                "type": 1,
                "name": "up",
                "options": []
            }
            ],
            "application_command": {
            "id": "828002256690610256",
            "type": 1,
            "application_id": "761562078095867916",
            "version": "1020017533245468672",
            "name": "dissoku",
            "description": "...",
            "options": [
                {
                "type": 1,
                "name": "regist",
                "description": "You can register Server.",
                "options": [
                    {
                    "type": 4,
                    "name": "language",
                    "description": "...",
                    "required": "true",
                    "choices": [
                        {
                        "name": "en",
                        "value": 1,
                        "name_localized": "en"
                        },
                        {
                        "name": "ja",
                        "value": 2,
                        "name_localized": "ja"
                        }
                    ],
                    "description_localized": "...",
                    "name_localized": "language"
                    }
                ],
                "description_localized": "You can register Server.",
                "name_localized": "regist"
                },
                {
                "type": 1,
                "name": "ci",
                "description": "If you put channel that you want to make invite, you can make its invite link.",
                "options": [
                    {
                    "type": 7,
                    "name": "channel",
                    "description": "...",
                    "required": "true",
                    "channel_types": [0, 5],
                    "description_localized": "...",
                    "name_localized": "channel"
                    }
                ],
                "description_localized": "If you put channel that you want to make invite, you can make its invite link.",
                "name_localized": "ci"
                },
                {
                "type": 1,
                "name": "up",
                "description": "You can bump up your server(1hour cooldown)",
                "description_localized": "You can bump up your server(1hour cooldown)",
                "name_localized": "up"
                },
                {
                "type": 1,
                "name": "page",
                "description": "You can check your server page.",
                "description_localized": "You can check your server page.",
                "name_localized": "page"
                }
            ],
            "integration_types": [0],
            "description_localized": "...",
            "name_localized": "dissoku"
            },
            "attachments": []
        },
        "nonce": "1195714118288408576",
        "analytics_location": "slash_ui"
    }
    r = requests.post(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def normal_reaction(token: str, channel_id: int, msg_id: int, emoji, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{msg_id}/reactions/{emoji}/%40me?location=Message&type=0"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    r = requests.put(url, headers = header)
    try:
        return r.json()
    except:
        return r.status_code

def custom_reaction(token: str, channel_id: int, msg_id: int, emoji_name: str , emoji_id: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{msg_id}/reactions/{emoji_name}:{emoji_id}/%40me?location=Message&type=0"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    r = requests.put(url, headers = header)
    try:
        return r.json()
    except:
        return r.status_code

def report(token: str, server_id: int, user_id: int, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/reporting/user"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    jsonData= {
        "version":"1.0",
        "variant":"1",
        "language":"en",
        "breadcrumbs":[16,9,7,14],
        "elements":{
            "user_profile_select":[
                "photos","descriptors","name"
            ]
        },
        "guild_id":server_id,
        "user_id":user_id,
        "name":"user"
    }
    r = requests.post(url, headers = header, json=jsonData)
    try:
        return r.json()
    except:
        return r.status_code

def friend_RQ_Link_gen(token: str):
    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    }

    response = requests.post("https://discord.com/api/v9/users/@me/invites", headers=headers)

    if response.status_code == 200:
        invite_code = response.json()["code"]
        print(f"discord.gg/{invite_code}")
    else:
        print(response.text)