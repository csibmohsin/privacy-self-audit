def score_privacy(data):
    score = 100
    reasons = []

    if data.get("hosting"):
        score -= 30
        reasons.append("IP belongs to hosting / cloud network")

    if data.get("proxy"):
        score -= 20
        reasons.append("Proxy or VPN detected")

    if data.get("public_dns"):
        score -= 10
        reasons.append("Public DNS resolver in use")

    if data.get("hostname_leak"):
        score -= 10
        reasons.append("Hostname reveals system identity")

    if score < 50:
        level = "HIGH EXPOSURE"
    elif score < 70:
        level = "MODERATE EXPOSURE"
    else:
        level = "GOOD"

    return score, level, reasons
