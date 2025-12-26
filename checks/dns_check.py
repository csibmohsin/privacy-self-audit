import socket

def dns_check():
    try:
        resolver = socket.gethostbyname("dns.google")
        return {
            "public_dns": True,
            "dns_resolver": resolver
        }
    except:
        return {
            "public_dns": False,
            "dns_resolver": "local"
        }
