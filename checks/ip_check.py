import requests

def ip_check():
    try:
        data = requests.get("http://ip-api.com/json").json()
        return {
            "public_ip": data.get("query"),
            "isp": data.get("isp"),
            "hosting": data.get("hosting"),
            "proxy": data.get("proxy")
        }
    except:
        return {
            "public_ip": "unknown",
            "isp": "unknown",
            "hosting": False,
            "proxy": False
        }
