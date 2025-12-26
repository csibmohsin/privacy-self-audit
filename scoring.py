def score_privacy(data):
    score = 100
    reasons = []
    recommendations = []

    if data.get("hosting"):
        score -= 30
        reasons.append("IP belongs to a hosting / cloud network")
        recommendations.append("Avoid using cloud or VPS networks for personal browsing")

    if data.get("proxy"):
        score -= 20
        reasons.append("Proxy or VPN detected")
        recommendations.append("Ensure VPN provider is trustworthy and privacy-focused")

    if data.get("public_dns"):
        score -= 10
        reasons.append("Public DNS resolver in use")
        recommendations.append("Consider privacy-focused DNS (Quad9, NextDNS, AdGuard)")

    if data.get("hostname_leak"):
        score -= 10
        reasons.append("Hostname reveals system identity")
        recommendations.append("Rename device hostname to a neutral name")

    if score < 50:
        level = "HIGH EXPOSURE"
    elif score < 70:
        level = "MODERATE EXPOSURE"
    else:
        level = "GOOD"

    return score, level, reasons, recommendations
