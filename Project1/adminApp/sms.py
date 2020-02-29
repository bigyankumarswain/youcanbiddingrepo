
def sendSMS(contactno,message):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "1H7BMEzLF5wGQcyO9ShoCKZutpl8k0RrT3IibfUDexdnPamNWqGog4c1JiNe8HtrlSOBXU3qxCMsfKn0",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    s1 = response.text
    return s1