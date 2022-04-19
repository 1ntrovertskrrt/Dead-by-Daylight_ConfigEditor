# Dead by Daylight Config Editor
# Auth 1ntrovertskrrt / Rizky

import os
import time
import colorama

from colorama import Fore

from Platfrom.Steam import *
from Platfrom.EpicGames import *

colorama.init()

def intro(): # Just ASCII art LOL
    
    print(Fore.BLUE + """

░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░  ███████╗██████╗░██╗████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░  ██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░  █████╗░░██║░░██║██║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗  ██╔══╝░░██║░░██║██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝  ███████╗██████╔╝██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░  ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                    Config Editor Installer
                                No Ban Chance for using those!
                                    Author 1ntrovertskrrt
    """)
def github():
    print(Fore.CYAN + '                          Github: https://github.com/RizkyNugroho666')

def menu(): # Select Platfrom Menu
    intro()
    github()
    print(Fore.WHITE + "Select your Platfrom!")
    print("1. Steam")
    print("2. Epic Games")
    print("3. Exit")
    return

def main():
    menu()
    command = ""
    while command != "3":
        try:
            command = str(input("Enter Numbers: "))
        except:
            print()
        if command == "1": # If 1, enter steam platfrom menu
            os.system('cls')
            print(Fore.BLUE + 'Select Configs')
            print(Fore.WHITE + f'1. SSL Bypass (Only for Steam | {Fore.RED} Highly Recommended{Fore.WHITE})')
            print('2. Lower Graphics')
            print('3. Potato Graphics')
            print('4. Higher FOV (For Steam Need SSL Bypass)')
            print('5. Ultra+ Graphics')
            print('6. Wallhack (only remove some wall textures)')
            print('7. Remove all Configs (Restore to default settings)')
            print('0. Back')

            command = str(input("Select your configs: "))
            if command == "1":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeSSLBypassSteam()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
    
            elif command == "2":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeLowestGraphicsSteam()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "3":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeFPSOptimizerSteam()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "4":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeFOVSteam()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()

            elif command == "5":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeUltraSteam()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "6":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeWallhackSteam()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()

            elif command == "7":
                print(Fore.GREEN + 'Removing your configs...')
                time.sleep(2)
                removeAllConfigsSteam()
                print('Config Successfully Removed')
                time.sleep(2)
                os.system('cls')
                return main()

            elif command == "0":
                os.system('cls')
                return main()

            else:
                print(f"{Fore.RED}Command not valid!{Fore.WHITE}")
                time.sleep(1.5)
                return main()

        elif command == "3": # Program Closed
            break

        if command == "2": # If 1, enter Epic Games platfrom menu
            os.system('cls')
            print(Fore.BLUE + 'Select Configs')
            print(Fore.WHITE + '1. SSL Bypass (Only for Steam)')
            print('2. Lower Graphics')
            print('3. Potato Graphics')
            print('4. Higher FOV')
            print('5. Ultra+ Graphics')
            print('6. Wallhack (only remove some wall textures')
            print('7. Remove all Configs (Restore to default)')
            print('0. Back')

            command = str(input("Select your configs: "))
            if command == "1":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeSSLBypassEGS()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
    
            elif command == "2":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeLowestGraphicsEGS()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "3":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeFPSOptimizerEGS()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "4":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeSSLFOVEGS()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "5":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeUltraEGS()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()
                 
            elif command == "6":
                print(Fore.GREEN + 'Changing your configs...')
                time.sleep(2)
                writeWallhackEGS()
                print('Config Successfully Installed')
                time.sleep(2)
                os.system('cls')
                return main()

            elif command == "7":
                print(Fore.GREEN + 'Removing your configs...')
                time.sleep(2)
                removeAllConfigsEGS()
                print('Config Successfully Removed')
                time.sleep(2)
                os.system('cls')
                return main()

            elif command == "0":
                os.system('cls')
                return main()

            else:
                print(f"{Fore.RED}Command not valid!{Fore.WHITE}")
                time.sleep(1.5)
                return main()

        elif command == "3": # Program Closed
            break

        else:
            print(f"{Fore.RED}Command not valid!{Fore.WHITE}")
            time.sleep(1.5)
            return main()

main()
