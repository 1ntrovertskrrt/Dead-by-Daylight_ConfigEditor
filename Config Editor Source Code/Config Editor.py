import os
import time
import colorama
import webbrowser

from colorama import Fore
from Lib.Steam import *
from Lib.EpicGames import *
from Lib.MicorosftStore import *

colorama.init()

def openDiscord():
    url = 'https://discord.gg/suuab4gntN'

    webbrowser.open(url)

    return

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
    print(Fore.CYAN + '                            Discord: https://discord.gg/suuab4gntN')

def menu(): # Select Platfrom Menu
    intro()
    github()
    print(Fore.WHITE + "Select your Platfrom!")
    print("1. Steam")
    print("2. Epic Games")
    print("3. Microsoft Store")
    print("4. Exit")
    return

def main():
    menu()
    command = ""
    while command != "4":
        try:
            command = str(input("Enter Numbers: "))
        except:
            print()
        
        try:

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
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeSSLBypassSteam()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    time.sleep(2)
                    os.system('cls')
                    return main()
        
                elif command == "2":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeLowestGraphicsSteam()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "3":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeFPSOptimizerSteam()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "4":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeFOVSteam()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()

                elif command == "5":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeUltraSteam()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "6":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeWallhackSteam()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()

                elif command == "7":
                    print(Fore.GREEN + 'Restoring your configs...')
                    time.sleep(2)
                    removeAllConfigsSteam()
                    print('Config Successfully Restored')
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

            elif command == "4": # Program Closed
                openDiscord()
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
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeSSLBypassEGS()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
        
                elif command == "2":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeLowestGraphicsEGS()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "3":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeFPSOptimizerEGS()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "4":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeFOVEGS()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "5":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeUltraEGS()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "6":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeWallhackEGS()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()

                elif command == "7":
                    print(Fore.GREEN + 'Restoring your configs...')
                    time.sleep(2)
                    removeAllConfigsEGS()
                    print('Config Successfully Restored')
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


            if command == "3": 
                os.system('cls')
                print(Fore.BLUE + 'Select Configs')
                print(Fore.WHITE + f'1. SSL Bypass (Only for Steam)')
                print('2. Lower Graphics')
                print('3. Potato Graphics')
                print('4. Higher FOV (For Steam Need SSL Bypass)')
                print('5. Ultra+ Graphics')
                print('6. Wallhack (only remove some wall textures)')
                print('7. Remove all Configs (Restore to default settings)')
                print('0. Back')

                command = str(input("Select your configs: "))
                if command == "1":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeSSLBypassWinGDK()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    time.sleep(2)
                    os.system('cls')
                    return main()
        
                elif command == "2":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeLowestGraphicsWinGDK()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "3":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeFPSOptimizerWinGDK()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "4":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeFOVWinGDK()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()

                elif command == "5":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeUltraWinGDK()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()
                    
                elif command == "6":
                    print(Fore.GREEN + 'Deleting your previous configs...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nInstalling SSL Bypass...')
                    time.sleep(1.5)
                    print(Fore.GREEN + '\nChanging your configs...')
                    time.sleep(2)
                    writeWallhackWinGDK()
                    print(Fore.BLUE + '\nConfig Successfully Installed')
                    os.system('cls')
                    return main()

                elif command == "7":
                    print(Fore.GREEN + 'Restoring your configs...')
                    time.sleep(2)
                    removeAllConfigsWinGDK()
                    print('Config Successfully Restored')
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

            else:
                print(f"{Fore.RED}Command not valid!{Fore.WHITE}")
                time.sleep(1.5)
                return main()

        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + "Can't find your config location!")
            time.sleep(2)
            os.system('cls')
            return main()

main()