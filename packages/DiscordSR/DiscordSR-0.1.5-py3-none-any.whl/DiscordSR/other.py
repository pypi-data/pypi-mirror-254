import requests

def token_check(self, token: str, **kwargs) -> dict:
    headers = {"Authorization": token}
    r = requests.get("https://discordapp.com/api/v9/users/@me/library", headers=headers)
    if r.status_code == 200:
        re = "vaild"
    else:
        re = "invaild"
    result = {
        "status_code": r.status_code,
        "json": r.json(),
        "result": re
    }
    return result

def nitro_check(code: str, **kwargs) -> dict:
    r = requests.get("https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if r.status_code == 200:
        return "vaild"
    else:
        return "invaild"

def botlink_gen(botid: int, **kwargs) -> dict:
    return f"https://discord.com/api/oauth2/authorize?client_id={str(botid)}&permissions=8&scope=bot"