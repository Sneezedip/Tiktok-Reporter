import os
import sys
import time
try:
    import requests,webbrowser,tempfile
    from colorama import Fore,Style
    from Static.Values import StaticValues
    import re,urllib,json
    from bs4 import BeautifulSoup
    import hashlib
    import subprocess
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import zipfile
    from tqdm import tqdm
    import shutil
except:
    print("Installing Libraries...")
    os.system("pip install -r requirements.txt")
    os.system("python3 main.py")
class StaticMethods:
    @staticmethod
    def get_proxies():
        with open('proxies.txt', 'w') as f:
            pass

        response = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies')
        
        if response.status_code == 200:
            with open('proxies.txt', 'a') as f:
                proxies = response.text.strip().split('\n')
                for proxy in proxies:
                    f.write(proxy.strip() + '\n')
        else:
            return
        return 1
    @staticmethod
    def  is_first_run():
        """Check if it's the first run of the program"""
        file_path = os.path.join(tempfile.gettempdir(), 'TtkReporter.txt')
        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                file.write("Don't Worry, this isn't a virus, just a check to see if it's your first time. :)")
            print(f"{StaticValues.INFO}First Time Detected. Welcome! (This won't appear anymore){Style.RESET_ALL}")
            webbrowser.open("https://discord.gg/nAa5PyxubF")

    @staticmethod
    def show_credits():
        """Display program credits"""
        print(f"{StaticValues.INFO}{Fore.BLUE}Provided to you by {Fore.CYAN}Sneezedip.{Style.RESET_ALL}")
        print(f"{StaticValues.INFO}{Fore.BLUE}Join Our Discord For More Tools! {Fore.GREEN}"
            f"https://discord.gg/nAa5PyxubF{Style.RESET_ALL}")
    @staticmethod   
    def get_match(match,url):
        format = re.search(rf'{match}', url)
        if format:
            format_x = format.group(1)
            return urllib.parse.unquote(format_x)
    @staticmethod
    def _solve_name(user):
        if "https" in user and "@" in user:
            return user
        elif not "https" in user and "@" in user:
            return f"https://www.tiktok.com/{user}"
        elif not "https" in user and not "@" in user:
            return f"https://www.tiktok.com/@{user}"
    @staticmethod
    def get_userData(user,infotype):
        def data(a,infotype):
            soup = BeautifulSoup(a, "html.parser")
            script_tag = soup.find("script", {"id": "__UNIVERSAL_DATA_FOR_REHYDRATION__"})
            if script_tag:
                data = json.loads(script_tag.string)
                try:
                    return data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"][infotype]
                except KeyError:
                    return "Invalid Profile. Check Username/Url"
        from bs4 import BeautifulSoup
        import json
        response = requests.get(StaticMethods._solve_name(user))
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find("script", {"id": "__UNIVERSAL_DATA_FOR_REHYDRATION__"})
            if script_tag:
                return data(response.text,infotype)
            else:
                os.system("cls") if os.name == 'nt' else os.system("clear")
                print(f"{StaticValues.WAITING}Gathering User Info With Selenium.. (this will take longer than normal)")
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--enable-unsafe-swiftshader")
                driver = webdriver.Chrome(options=options)
                driver.get(StaticMethods._solve_name(user))
                time.sleep(3)

                page_source = driver.page_source
                driver.quit()
                os.system("cls") if os.name == 'nt' else os.system("clear")
                return data(page_source,infotype)        
        else:
            raise Exception("Internal Error")
    @staticmethod
    def _getpayload(timestamp,useragent,deviceID,odinId,victim_data,report_type):
        return {
            "WebIdLastTime" : timestamp,
            "aid" : 1988,
            "app_language" : "en",
            "app_name" : "tiktok_web",
            "r_language": "en-US",
            "browser_name": "Mozilla",
            "browser_online": True,
            "browser_platform": "Win32",
            "browser_version": useragent,
            "channel": "tiktok_web",
            "cookie_enabled": True,
            "current_region": "PT",
            "data_collection_enabled": True,
            "device_id": deviceID,
            "device_platform": "web_pc",
            "focus_state": True,
            "from_page": "user",
            "history_len": 2,
            "is_fullscreen": False,
            "is_page_visible": True,
            "lang": "en",
            "nickname": victim_data["nickname"],
            "object_id": victim_data["id"],
            "odinId": odinId,
            "os": "windows",
            "owner_id": victim_data["id"],
            "priority_region": "",
            "reason": report_type,
            "referer": "",
            "region": "PT",
            "report_type": "user",
            "screen_height": 1080,
            "screen_width": 1920,
            "secUid": victim_data["secUid"],
            "target": victim_data["id"],
            "tz_name": "Atlantic/Azores",
            "user_is_login": False,
            "webcast_language": "en",
            }
    def Activate(sha256_hash,file_path,UUID):
        response = requests.get(f"https://sneezedip.pythonanywhere.com/get_key2?uuid={UUID.split("-")[4]}").json()
        print(f'{StaticValues.WARNING}Program not Activated.')
        print(f'''{Fore.CYAN} This program is free of use, but you need an activation key to continue!\n
            Please join the discord and go to the \'get-key\' channel and insert this command{Style.RESET_ALL}''')
        print(f'{Fore.RED}/reportkey {response['response']}{Fore.RESET}')
        while True:
            activation = input(f"{Fore.YELLOW}[Waiting] {Fore.WHITE}Please enter Activation Key >>> ")
            response = requests.get(f"https://sneezedip.pythonanywhere.com/validate_activation2?uuid={UUID.split("-")[4]}&key={activation}")
            if 'Valid' in response.json()['response']:
                print('Activating the program.')
                sha256_hash.update(activation.encode('utf-8'))
                with open(file_path,"w")as file:
                    file.write(sha256_hash.hexdigest())
                return True  
    def vk():
        sha256_hash = hashlib.sha256()
        file_path = os.path.join(tempfile.gettempdir(), 'rb_sneez.txt')
        UUID = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        if not os.path.isfile(file_path):
            StaticMethods.Activate(sha256_hash,file_path,UUID)
        else:
            with open(file_path,"r")as file:
                response = requests.get(f"https://sneezedip.pythonanywhere.com/compare2?uuid={UUID.split("-")[4]}&rk={file.read()}")
                try:
                    if 'valid' in response.json()['response']:
                        return True
                except:
                    StaticMethods.Activate(sha256_hash,file_path,UUID)     
                else: 
                    StaticMethods.Activate(sha256_hash,file_path,UUID)  
    def download(download_url, destination='.'):
        """Download and extract a file from the given URL"""
        print(f'{StaticValues.INFO}Downloading new version, please wait...{Style.RESET_ALL}')

        response = requests.get(download_url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        zip_path = os.path.join(destination, "downloaded_file.zip")

        with open(zip_path, 'wb') as file:
            with tqdm(total=total_size, unit='B', unit_scale=True,
                    desc=f"{StaticValues.WAITING}Downloading "
                        f"{'New Version' if 'Sneezedip' in download_url else 'Tesseract'} {Style.RESET_ALL}") as pbar:
                for data in response.iter_content(1024):
                    file.write(data)
                    pbar.update(len(data))

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            total_files = len(zip_ref.infolist())
            with tqdm(total=total_files, unit='file',
                    desc=f"{StaticValues.WAITING}Extracting "
                        f"{'New Version' if 'Sneezedip' in download_url else 'Tesseract'}{Style.RESET_ALL}") as pbar:
                for file in zip_ref.infolist():
                    zip_ref.extract(file, destination)
                    pbar.update(1)
        os.remove(zip_path)

        if 'Sneezedip' in download_url:
            with os.scandir('Tiktok-Reporter-main') as entries:
                for entry in entries:
                    if entry.is_dir():
                        with os.scandir(entry) as entries_folder:
                            for entry_folder in entries_folder:
                                try:
                                    os.replace(f"Tiktok-Reporter-main/{entry.name}/{entry_folder.name}",
                                            f"./{entry.name}/{entry_folder.name}")
                                except Exception as e:
                                    print(e)
                                continue
                    if entry.is_file():
                        try:
                            os.replace(f"Tiktok-Reporter-main/{entry.name}", f"./{entry.name}")
                        except Exception as e:
                            print(e)
                        continue
            shutil.rmtree("Tiktok-Reporter-main")
        print(f'{StaticValues.SUCCESS}{Fore.WHITE}{"New Version" if "Sneezedip" in download_url else "Tesseract"}'
            f' Downloaded and Extracted Successfully!{Style.RESET_ALL}')
        print(f'{StaticValues.WARNING}{Fore.WHITE}Please Restart the program!{Style.RESET_ALL}')

    def check_version(current_version):
        """Check if a new version of the program is available"""
        response = requests.get("https://raw.githubusercontent.com/Sneezedip/Tiktok-Reporter/main/VERSION")
        if response.text.strip() != current_version:
            while True:
                u = input(f"{StaticValues.WARNING}"
                        f"NEW VERSION FOUND. Want to update? (y/n){Style.RESET_ALL}").lower()
                if u == "y":
                    StaticMethods.download("https://codeload.github.com/Sneezedip/Tiktok-Reporter/zip/refs/heads/main", "./")
                    sys.exit(1)
                elif u == "n":
                    return
    
    
