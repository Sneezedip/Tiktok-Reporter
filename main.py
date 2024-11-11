import os
import time
import threading
import random
from datetime import datetime
try:
    from colorama import Style,Fore
    import tls_client
    import random
    from fake_useragent import UserAgent
    from Static.Methods import StaticMethods
    from Static.Values import StaticValues
    from Handler.ErrorHandler import Handler
except:
    print("Installing Libraries...")
    os.system("pip install -r requirements.txt")
    os.system("python3 main.py")

class Program:
    def _clear(self):
        os.system("cls") if os.name == 'nt' else os.system("clear")

    def main(self):
        self._clear()
        while True:
            print(f"{StaticValues.WAITING}Enter the victim URL or @ ➤ ",end="")
            self.victim = input()
            self.victim = StaticMethods.get_userData(self.victim,"id")
            if "Invalid" in self.victim:
                print(f"{StaticValues.WARNING} Invalid URL or @!")
            else:
                break
        self._clear()
        print(f"{StaticValues.SUCCESS}Valid User!")
        print(f"{StaticValues.WAITING}Gathering User Data..")
        self.victim_data = {
            "id" : StaticMethods.get_userData(self.victim,"id"),
            "nickname" : StaticMethods.get_userData(self.victim,"nickname"),
            "secUid" : StaticMethods.get_userData(self.victim,"secUid"),
        }
        print(f"{StaticValues.SUCCESS}Success!")
        self._clear()
        print(f"{StaticValues.WAITING}Select an Option to report the victim.")
        for key, value in StaticValues.REPORT_TYPES.items():
            print(f"{key}: {value[1]}")
        while True:
            self.report_type = Handler.integer_handler(f"{Fore.YELLOW}➤ {Fore.RESET}",1,15)
            if self.report_type in StaticValues.REPORT_TYPES:
                break
        self.payload = StaticMethods._getpayload(datetime.now().timestamp(),UserAgent().random,random.randint(7000000000000000000,9999999999999999999),random.randint(7000000000000000000,9999999999999999999),self.victim_data,self.report_type)
    def report(self):
        while True:
            session = tls_client.Session(
                    client_identifier="chrome_106"
                )
            response = session.get("https://www.tiktok.com/aweme/v2/aweme/feedback/", params=self.payload)
            
            StaticValues.TOTAL_REQUESTS += 1
            if "Thanks for your feedback" in response.text or response.status_code == 200:
                StaticValues.REPORT_COUNT += 1
                self._clear()
                print(f"{StaticValues.SUCCESS}{self.victim_data["nickname"]} Reported {StaticValues.REPORT_COUNT} Times! ({(StaticValues.REPORT_COUNT/StaticValues.TOTAL_REQUESTS)*100}% Success Rate)")
            else:  
                print(f"{StaticValues.WARNING}Error ({(StaticValues.REPORT_COUNT/StaticValues.TOTAL_REQUESTS)*100}% Success Rate)")
                StaticValues.COOLDOWN = True
                break
    
if __name__ == "__main__":
    threads = []
    StaticMethods.check_version("0.0.3")
    os.system("cls") if os.name == 'nt' else os.system("clear")
    StaticMethods.vk()
    os.system("cls") if os.name == 'nt' else os.system("clear")
    StaticMethods.is_first_run()
    StaticMethods.show_credits()
    t_a = Handler.integer_handler(f"{StaticValues.WAITING}THREADS AMOUNT ➤ ")
    time.sleep(1)
    program = Program()
    program.main()
    for _ in range(t_a):
        t = threading.Thread(target=program.report)
        threads.append(t)
        t.start()
    for thread in threads:
        if not StaticValues.COOLDOWN:
            thread.join()
        else:
            print(f"{StaticValues.WAITING}Cooldown detected. Waiting 10 seconds..")
            time.sleep(10)
            StaticValues.COOLDOWN = False
