import time
import sys
from colorama import Fore, Style, init

from checks.ip_check import ip_check
from checks.dns_check import dns_check
from checks.hostname_check import hostname_check
from scoring import score_privacy

init(autoreset=True)

# ---------------- UI ----------------

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
██████╗ ██████╗ ██╗██╗   ██╗ █████╗  ██████╗██╗   ██╗
██╔══██╗██╔══██╗██║██║   ██║██╔══██╗██╔════╝╚██╗ ██╔╝
██████╔╝██████╔╝██║██║   ██║███████║██║      ╚████╔╝ 
██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║██║       ╚██╔╝  
██║     ██║  ██║██║ ╚████╔╝ ██║  ██║╚██████╗   ██║   
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝   ╚═╝   

        PRIVACY SELF-AUDIT TOOL
        Tracking & Exposure Analyzer
-------------------------------------------------------
""")


def spinner(task):
    for _ in range(6):
        for c in "|/-\\":
            sys.stdout.write(f"\r{Fore.YELLOW}{task}... {c}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r")


def section(title):
    print("\n" + Fore.BLUE + Style.BRIGHT + f"[ {title.upper()} ]")
    print(Fore.BLUE + "-" * (len(title) + 6))


def privacy_bar(score):
    bars = score // 10
    color = Fore.GREEN
    if score < 70:
        color = Fore.YELLOW
    if score < 50:
        color = Fore.RED

    print(color + "Privacy Meter: [" + "█" * bars + " " * (10 - bars) + f"] {score}/100")


# ---------------- MAIN ----------------

def run_audit():
    banner()

    spinner("Checking public IP")
    ip_data = ip_check()

    spinner("Analyzing DNS exposure")
    dns_data = dns_check()

    spinner("Checking system identity leaks")
    host_data = hostname_check()

    report = {}
    report.update(ip_data)
    report.update(dns_data)
    report.update(host_data)

    score, level, reasons, recommendations = score_privacy(report)

    # -------- OUTPUT --------

    section("Network Identity")
    print("Public IP        :", ip_data.get("public_ip"))
    print("ISP              :", ip_data.get("isp"))
    print("Hosting Network  :", ip_data.get("hosting"))
    print("Proxy / VPN      :", ip_data.get("proxy"))

    section("DNS & Routing")
    print("Public DNS Used  :", dns_data.get("public_dns"))
    print("DNS Resolver     :", dns_data.get("dns_resolver"))

    section("System Identity")
    print("Hostname         :", host_data.get("hostname"))
    print("Hostname Leaked  :", host_data.get("hostname_leak"))

    print("\n" + "=" * 60)
    privacy_bar(score)

    level_color = Fore.GREEN
    if level == "MODERATE EXPOSURE":
        level_color = Fore.YELLOW
    if level == "HIGH EXPOSURE":
        level_color = Fore.RED

    print(level_color + Style.BRIGHT + f"PRIVACY STATUS: {level}")
    print("=" * 60)

    section("Why this result?")
    if not reasons:
        print(Fore.GREEN + "No major privacy risks detected.")
    else:
        for r in reasons:
            print(Fore.RED + "- " + r)

    section("How to improve privacy")
    if not recommendations:
        print(Fore.GREEN + "Your setup already follows good privacy practices.")
    else:
        for rec in recommendations:
            print(Fore.YELLOW + "- " + rec)

    print(Fore.CYAN + "\nAudit complete. Awareness is protection.")


if __name__ == "__main__":
    run_audit()
