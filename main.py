from colorama import Fore, init
from datetime import datetime
from pystyle import *
import requests, aiohttp, asyncio, json, time, os, pyfade, pyfiglet

ascii = pyfiglet.figlet_format("OGU Checker")
Anime.Fade(Center.Center(ascii), Colors.red_to_purple,
Colorate.Vertical, time=True, enter=True)

with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'No usernames found!\n Make sure to paste them into usernames.txt and save.')
        quit()\
            
async def check():
    session = requests.Session()
    for username in usernames:
        c = session.get(f'https://ogu.gg/{username}', headers={'Connection': 'keep-alive', 'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}, timeout=60)        
        check = c.status_code
        if check == 404:
            print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_blue, text = f"+ Username {username} is not taken"))
            with open('available.txt', "a") as x:
                x.write(f"{username}\n")
        elif check == 200:
            print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, text = f"""- Username {username} is claimed."""))
        else:
            print(f" [?] Unknown Error . . . - {check}")
    
    print(f"\n Done. Available Usernames are saved in available.txt!\n Press Enter to exit.\n")
    input()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check())
