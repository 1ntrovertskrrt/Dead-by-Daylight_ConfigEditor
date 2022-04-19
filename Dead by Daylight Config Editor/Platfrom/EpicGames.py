# Config Editor Installer for Dead By Daylight
# Auth 1ntrovertskrrt

from pathlib import Path
home = str(Path.home())

def writeSSLBypassEGS():  # Add SSL Bypass

    with open('Resources\sslbypass.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return

def writeFPSOptimizerEGS():  # Add FPS Optimizer

    with open('Resources\FPS Optimizer.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return

def writeLowestGraphicsEGS():  # Add Lowend Graphics

    with open('Resources\lowend pc config.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return

def writeSSLFOVEGS():  # Add SSL+FOV 

    with open('Resources\SSL+FOV.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'a') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return

def writeWallhackEGS():  # Add Wallhack

    with open('Resources\sslbypass.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return

def writeUltraEGS():  # Add Ultra+ graphics

    with open('Resources\\UltraSettings.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return

def removeAllConfigsEGS(): # Remove all configs

    with open('Resources\default.ini','r') as firstfile, open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\EGS\Engine.ini",'w') as secondfile:
        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)
    return
