#===== DAVLOPER : KALYAN KING

#==== TELIGERM LINK : https://t.me/KGF_TEAM_CBER

#===== TOOL : TARMUX SETUP 

import os
import sys
import time
import platform
import requests
import datetime
#=====Colours code <\>
BLACK   = "\033[0;30m"
RED     = "\033[0;31m"
GREEN   = "\033[0;32m"
YELLOW  = "\033[0;33m"
BLUE    = "\033[0;34m"
PURPLE  = "\033[0;35m"
CYAN    = "\033[0;36m"
WHITE   = "\033[0;37m"
BOLD_BLACK   = "\033[1;30m"
BOLD_RED     = "\033[1;31m"
BOLD_GREEN   = "\033[1;32m"
BOLD_YELLOW  = "\033[1;33m"
BOLD_BLUE    = "\033[1;34m"
BOLD_PURPLE  = "\033[1;35m"
BOLD_CYAN    = "\033[1;36m"
BOLD_WHITE   = "\033[1;37m"
UNDER_RED    = "\033[4;31m"
UNDER_GREEN  = "\033[4;32m"
UNDER_YELLOW = "\033[4;33m"
UNDER_BLUE   = "\033[4;34m"
UNDER_CYAN   = "\033[4;36m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_PURPLE  = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"
LIGHT_RED     = "\033[91m"
LIGHT_GREEN   = "\033[92m"
LIGHT_YELLOW  = "\033[93m"
LIGHT_BLUE    = "\033[94m"
LIGHT_PURPLE  = "\033[95m"
LIGHT_CYAN    = "\033[96m"
LIGHT_WHITE   = "\033[97m"
RESET = "\033[0m"

RUN_TIME = datetime.datetime.now().strftime("%d-%m-%Y  |  %I:%M:%S %p")

# ━━━ GET PUBLIC IP ━━━
try:
    USER_IP = requests.get("https://api.ipify.org").text
except:
    USER_IP = "Unavailable"

# ━━━ COLORS ━━━
GREEN  = "\033[0;32m"
CYAN   = "\033[0;36m"
YELLOW = "\033[0;33m"
RED    = "\033[0;31m"
RESET  = "\033[0m"

# ━━━ Banner ━━━
banner = (
    "\033[1;31m </ "
    "\033[1;32mWELCOME "
    "\033[1;33mTO "
    "\033[1;34mKGF "
    "\033[1;36mTERMUX "
    "\033[1;35mSET-UP "
    "\033[1;91mTOOL "
    "\033[1;31m/> \033[0m"
)

for ch in banner:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.03)

print()
os.system('espeak -a 300 "Welcome to K G F Termux Setup Tool"')
time.sleep(2)
print(f" {LIGHT_GREEN} YOUR IP : {USER_IP} ")
os.system(f'espeak -a 300 " YOUR IP {USER_IP}"')
time.sleep(2)
os.system("xdg-open https://t.me/KGF_TEAM_CBER")
time.sleep(2)
os.system("clear")

# ━━━ LOGO ━━━
logo = f"""
{GREEN} SSSSS  EEEEEEE TTTTTTT UU   UU PPPPPP  
SS      EE        TTT   UU   UU PP   PP 
 SSSSS  EEEEE     TTT   UU   UU PPPPPP  
     SS EE        TTT   UU   UU PP      
 SSSSS  EEEEEEE   TTT    UUUUU  PP {LIGHT_RED} TARMUX SETUP       
{RESET}
"""

# ━━━ INFO TEXT ━━━
print(f"{LIGHT_PURPLE}DEVELOPER : KALYAN KING{RESET}")
print(f"{GREEN} YOUR IP    : {YELLOW}{USER_IP}{RESET}")
print(f"{UNDER_CYAN}TOOL      : TARMUX SETUP{RESET}")
print(f"{BOLD_WHITE}TEAM      : KGF CYBER TEAM{RESET}")
print(f"{GREEN} RUN TIME     : {YELLOW}{RUN_TIME}{RESET}")
print(f"{LIGHT_BLUE}VERSION   : 0.1  {RESET}NEW")

# ━━━ LIST OF PACKAGES ━━━
packages = [
    "aiofiles", "android", "ansicolors", "ansiwrap", "APScheduler", "astroid", 
    "async-generator", "async-timeout", "asyncio", "attrs", "audiostream",
    "barcode", "beautifulsoup4", "Brotli", "bs4", "cachetools", "requests",
    "pyfiglet", "uuid", "secrets", "datetime", "string", "webbrowser",
    "hashlib", "colorama", "pafy", "json", "argparse", "InstagramAPI",
    "generate_user_agent", "threading", "cairocffi", "CairoSVG", "certifi",
    "cffi", "chardet", "charset-normalizer", "click", "cloudscraper", "colorama",
    "colored", "colour", "cryptography", "dataclasses", "decorator", "emoji",
    "Faker", "Flask", "fonttools", "future", "geopy", "gitdb", "GitPython",
    "gTTS", "h11", "h2", "html5lib", "httpx", "idna", "imageio", "IMDbPY",
    "instaloader", "itsdangerous", "jedi", "Jinja2", "Kivy", "kivymd", "lazy-object-proxy",
    "numpy", "openai", "openpyxl", "pandas", "parsedatetime", "Pillow", "prettytable",
    "protobuf", "psutil", "pycryptodomex", "pyfiglet", "pygame", "pymongo", "PyQt5",
    "Pyrogram", "pyTelegramBotAPI", "python-dotenv", "pytube", "qrcode", "redis",
    "requests-oauthlib", "rich", "scapy", "schedule", "scipy", "selenium", "six",
    "SQLAlchemy", "telebot", "telegram", "telegraph", "Telethon", "tqdm", "trio",
    "typing_extensions", "ua-parser", "urllib3", "validators", "wget", "yfinance",
    "youtube-dl", "yt-dlp", "zipp"
]

# ━━━ MENU FUNCTION ━━━
def Manu():
    while True:
        os.system("clear")
        print(logo)
        print(f"{BG_GREEN}[1] TARMUX SETUP{RESET}")
        print(f"{LIGHT_PURPLE}[2] EXIT TOOL{RESET}")

        choice = input("\nEnter YOUR Choice : ")

        if choice == "1":
            print("\nStarting Termux Setup... 🔧\n")
            # ━━ Step 1: Update & Upgrade ━━
            print("Updating & Upgrading Termux packages...\n")
            os.system("pkg update -y && pkg upgrade -y")
            time.sleep(1)

            # ━━ Step 2: Install all Python packages ━━
            for pkg in packages:
                print(f"Installing {pkg}...")
                os.system(f"pip install {pkg}")
                time.sleep(0.1)

            print("\n✅ All packages installed successfully!")
            input("\nPress Enter to go back to menu...")

        elif choice == "2":
            print("\nThanks for using KGF Tool ❤️")
            break

        else:
            print("\nInvalid Option! Try Again...")
            time.sleep(1)

# ━━━ RUN MENU ━━━
Manu()