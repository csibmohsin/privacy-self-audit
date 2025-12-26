import socket

def hostname_check():
    hostname = socket.gethostname()

    suspicious = any(x in hostname.lower() for x in ["admin", "user", "pc", "laptop"])

    return {
        "hostname": hostname,
        "hostname_leak": suspicious
    }
