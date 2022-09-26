import colorama, time, pystyle
from pystyle import Colors, Colorate, Box
from colorama import Fore, Style, Back
import os

def cls():
   os.system('cls' if os.name=='nt' else 'clear')

def logo():
  print(Colorate.Vertical(Colors.red_to_blue, f"""       ▄▄▄    ██▒   █▓▄▄▄█████▓    ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
      ▒████▄ ▓██░   █▒▓  ██▒ ▓▒   ▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
      ▒██  ▀█▄▓██  █▒░▒ ▓██░ ▒░   ▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
      ░██▄▄▄▄██▒██ █░░░ ▓██▓ ░    ▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
       ▓█   ▓██▒▒▀█░    ▒██▒ ░    ▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
       ▒▒   ▓▒█░░ ▐░    ▒ ░░      ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
        ▒   ▒▒ ░░ ░░      ░       ░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
        ░   ▒     ░░    ░         ░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
            ░  ░   ░                     ░      ░         ░  ░        ░               ░ ░      ░ ░      ░  ░      ░  
                  ░                                                                                                  """))
  print(Colorate.Vertical(Colors.red_to_blue,
                          "[CAT/1] DISCORD TOOLS\n[CAT/2] DEADLY TOOLS\n[CAT/3] Generators\n[CAT/4] Null Currently"
  ))


def discord():
  cls()
  print(Colorate.Vertical(Colors.red_to_blue,"""      ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
      ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
      ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
      ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
      ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
       ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
       ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
       ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
         ░     ░        ░  ░ ░          ░ ░     ░        ░                    ░ ░      ░ ░      ░  ░      ░  
       ░                   ░                           ░                                                     """))
  print(Colorate.Vertical(Colors.red_to_blue,"[1] AVT Nuker\n[2] AVT Account Nuker\n[3] Webhook Spammer\n[4] Vanity Checker\n[5] Discord BruteForcer"))


def deadly():
  print(Colorate.Vertical(Colors.red_to_blue,"""      ▓█████▄ ▓█████ ▄▄▄      ▓█████▄  ██▓   ▓██   ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
      ▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌▓██▒    ▒██  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
      ░██   █▌▒███  ▒██  ▀█▄  ░██   █▌▒██░     ▒██ ██░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
      ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌▒██░     ░ ▐██▓░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
      ░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓ ░██████▒ ░ ██▒▓░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
       ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▓  ░  ██▒▒▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
       ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒ ░ ░ ▒  ░▓██ ░▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
       ░ ░  ░    ░    ░   ▒    ░ ░  ░   ░ ░   ▒ ▒ ░░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
         ░       ░  ░     ░  ░   ░        ░  ░░ ░                     ░ ░      ░ ░      ░  ░      ░  
       ░                       ░              ░ ░                                                    """))
  print(Colorate.Vertical(Colors.red_to_blue,"[6] Ip Tracker"))

def deadly2():
  print(Colorate.Vertical(Colors.red_to_blue,"""       ▄▄▄     ▄▄▄█████▓ ██▒   █▓     ▄████ ▓█████  ███▄    █   ██████ 
      ▒████▄   ▓  ██▒ ▓▒▓██░   █▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▒██    ▒ 
      ▒██  ▀█▄ ▒ ▓██░ ▒░ ▓██  █▒░   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒░ ▓██▄   
      ░██▄▄▄▄██░ ▓██▓ ░   ▒██ █░░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒
       ▓█   ▓██▒ ▒██▒ ░    ▒▀█░     ░▒▓███▀▒░▒████▒▒██░   ▓██░▒██████▒▒
       ▒▒   ▓▒█░ ▒ ░░      ░ ▐░      ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
        ▒   ▒▒ ░   ░       ░ ░░       ░   ░  ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░
        ░   ▒    ░           ░░     ░ ░   ░    ░      ░   ░ ░ ░  ░  ░  
            ░  ░              ░           ░    ░  ░         ░       ░  
                             ░                                         """))
  print(Colorate.Vertical(Colors.red_to_blue,"[10] Nitro Generator\n[11] Nitro Checker\n[12] Password Generator"))
  










logo()
while True:
    q = input("\n\n"+Fore.RED+">"+Fore.MAGENTA+"> "+Fore.RED)
    if q == "0":
      cls()
      logo()
    elif q == "cat2":
      cls()
      deadly()
    elif q == "cat1":
      cls()
      discord()
    elif q == "cat3":
      cls()
      deadly2()
    elif q == "1":
      cls()
      import nukebot
    elif q == "2":
      cls()
      print("There is no account nuker yet.")
    elif q == "3":
      import webspam
    elif q == "6":
      import iptracker
    elif q  == "11":
      import nitroc
    elif q == "10":
      import nitrog
    elif q == "5":
      import discordbruite
    elif q == "exit":
      quit()
    elif q == "12":
      import passwordgen
    elif q == "4":
      import vanitycheck
    elif q == "inf":
      print(Colorate.Vertical(Colors.black_to_white,
        "CREATED BY LEVIATHAN, DOOM, SHREK, BORDER\nFIND SUPPORT AT - https://discord.gg/BafFbsgFRz\nNUKER BY SHREK\nMENU BY DOOM\nLEVIATHAN HAS NOTHING DONE YET\nBORDER ERROR SUPPORTER\nHAVE FUN"
      ))
    else:
      print(f"{q} is not a valid choice.")
