import requests

class guild_mynick_class:
    def guild_mynick(token: str, server_id: int, nick: str, **kwargs) -> dict:
        url = f"https://discord.com/api/v9/guilds/{server_id}/members/@me"
        header = {
            "authorization": token,
            'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
        }
        json = {
            "nick": nick
        }
        r = requests.patch(url, headers=header, json=json)
        try:
            return r.json()
        except:
            return r.status_code

def guild_IDnick(token: str, server_id: int, user_id: int, nick: str, **kwargs) -> dict:
    url = f"https://discord.com/api/v9/guilds/{server_id}/members/{user_id}"
    header = {
        "authorization": token,
        'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8"
    }
    json = {
        "nick": nick
    }
    r = requests.patch(url, headers=header, json=json)
    try:
        return r.json()
    except:
        return r.status_code
