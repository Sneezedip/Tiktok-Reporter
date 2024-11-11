import os
try:
    from colorama import Fore,Style
except:
    print("Installing Libraries...")
    os.system("pip install -r requirements.txt")
    os.system("python3 main.py")
class StaticValues:
    WAITING = f"{Style.RESET_ALL}{Fore.YELLOW}[WAITING] {Style.BRIGHT}{Fore.WHITE}"
    SUCCESS = f"{Style.RESET_ALL}{Fore.GREEN}[SUCCESS] {Style.BRIGHT}{Fore.WHITE}"
    INFO = f"{Style.RESET_ALL}{Fore.BLUE}[INFO] {Style.BRIGHT}{Fore.WHITE}"
    WARNING = f"{Style.RESET_ALL}{Fore.RED}[WARNING] {Style.BRIGHT}{Fore.WHITE}"

    GATHERED_PROXIES = False

    REPORT_TYPES = {
        1: (90013, "Violence"),
        2: (90014, "Sexual Abuse"),
        3: (90016, "Animal Abuse"),
        4: (90017, "Criminal Activities"),
        5: (9020, "Hate"),
        6: (9007, "Bullying"),
        7: (90061, "Suicide Or Self-Harm"),
        8: (90064, "Dangerous Content"),
        9: (90084, "Sexual Content"),
        10: (90085, "Porn"),
        11: (90037, "Drugs"),
        12: (90038, "Firearms Or Weapons"),
        13: (9018, "Sharing Personal Info"),
        14: (90015, "Human Exploitation"),
        15: (91015, "Under Age")
    }

    REPORT_COUNT = 0
    TOTAL_REQUESTS = 0

    COOLDOWN = False