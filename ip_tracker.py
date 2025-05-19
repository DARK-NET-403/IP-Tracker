#Tool Make By : Ariyan Rabbi(Dʌʀĸ-Nɘt)
#Don't Use My coded File And copy
#Are Your use copy my file Your Father 100 man
#use this tool and give me star
#Don't Copy my file

import requests
import os
import sys
import time
from pyfiglet import figlet_format

# Clear screen
os.system("cls" if os.name == "nt" else "clear")

# Typewriter effect
def type_line(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Centered line
def center_line(text, width=60):
    return text.center(width)

# Logo
print("\033[96m" + figlet_format("IP Tracker", font="slant"))

# Author Info
type_line("\033[94m╔════════════════════════════════════════════════╗")
type_line("\033[94m║\033[95m        Author: Ariyan Rabbi (Dʌʀĸ-Nɘt)         \033[94m║")
type_line("\033[94m╠════════════════════════════════════════════════╣")
type_line("\033[94m║\033[93m Facebook : facebook.com/share/12Ju91Lznxb/     \033[94m║")
type_line("\033[94m║\033[93m Telegram : t.me/DARK_NET_403                   \033[94m║")
type_line("\033[94m║\033[93m GitHub   : github.com/DARK-NET-403             \033[94m║")
type_line("\033[94m╚════════════════════════════════════════════════╝\n")

# Input
type_line("\033[92m┌═🌐 Enter IP/Domain (Leave blank for your own IP)")
target = input("\033[92m└══╼ \033[97m").strip()

# Choose URL
if not target:
    type_line("\n\033[96m[🛰️] Tracking your IP...\n", 0.03)
    url = "http://ip-api.com/json/"
else:
    type_line(f"\n\033[96m[🛰️] Tracking {target}...\n", 0.03)
    url = f"http://ip-api.com/json/{target}"

time.sleep(1.5)

def pretty_line(text):
    type_line("\033[92m" + text, 0.01)
    type_line("\033[90m" + "─" * 60, 0.001)

def safe_get(res, key):
    return res.get(key) if res.get(key) else "\033[91m❌ Not Found"

try:
    res = requests.get(url).json()

    if res['status'] == 'success':
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[96m" + figlet_format("IP Tracker", font="slant"))

        # Info box again
        type_line("\033[94m╔════════════════════════════════════════════════╗")
        type_line("\033[94m║\033[95m        Author: Ariyan Rabbi (Dʌʀĸ-Nɘt)         \033[94m║")
        type_line("\033[94m╠════════════════════════════════════════════════╣")
        type_line("\033[94m║\033[93m Facebook : facebook.com/share/12Ju91Lznxb/     \033[94m║")
        type_line("\033[94m║\033[93m Telegram : t.me/DARK_NET_40                    \033[94m║")
        type_line("\033[94m║\033[93m GitHub   : github.com/DARK-NET-403             \033[94m║")
        type_line("\033[94m╚════════════════════════════════════════════════╝\n")

        type_line("\033[92m" + "=" * 60)
        type_line("\033[92m" + center_line("✅ IP Information Found!"))
        type_line("\033[92m" + "=" * 60 + "\n")

        pretty_line(f"🌍 IP Address : {safe_get(res, 'query')}")
        pretty_line(f"🏳 Country     : {safe_get(res, 'country')}")
        pretty_line(f"🏙 Region      : {safe_get(res, 'regionName')}")
        pretty_line(f"🏘 City        : {safe_get(res, 'city')}")
        pretty_line(f"📮 ZIP Code   : {safe_get(res, 'zip')}")
        pretty_line(f"🛰 ISP         : {safe_get(res, 'isp')}")
        pretty_line(f"🏢 Org        : {safe_get(res, 'org')}")
        pretty_line(f"🕓 Timezone   : {safe_get(res, 'timezone')}")

        lat = res.get('lat')
        lon = res.get('lon')
        if lat and lon:
            location = f"{lat}, {lon}"
            maps_url = f"https://www.google.com/maps?q={lat},{lon}"
        else:
            location = "\033[91m❌ Not Found"
            maps_url = "\033[91m❌ Not Found"

        pretty_line(f"📍 Location   : {location}")
        pretty_line(f"🔗 Maps URL   : {maps_url}")

    else:
        type_line("\033[91m[❌] IP not found or invalid input!")

except Exception as e:
    type_line(f"\033[91m[‼️] Error: {e}")
