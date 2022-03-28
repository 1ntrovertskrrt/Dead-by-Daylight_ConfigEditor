#Config Editor for Dead By Daylight
# Auth 1ntrovertskrrt


import os
import time
from pathlib import Path
home = str(Path.home())


def readConfigFileSteam(Engine): # Read Engine.ini file

    list = []
    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini", "r") as file:

        for value in file:
            list.append(value.rstrip('\r\n'))
    return list

def writeConfigFileSteam(Engine): # Add SSL Bypass into Engine.ini
    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini", "a") as file:
        file.write("\n[/Script/Engine.NetworkSettings] \nn.VerifyPeer=False")
        
    return

def removeConfigFilesSteam(Engine): # This Function for Remove the SSL Bypass and replace fresh engine.ini
    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini", "w") as file:
        file.write("[Core.System] \nPaths=../../../Engine/Content \nPaths=%GAMEDIR%Content \nPaths=../../../Engine/Plugins/Runtime/Bhvr/MirrorsAnalytics/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/OnlinePresence/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/PlatformsProviders/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/VersionNumber/Content \nPaths=../../../Engine/Plugins/Experimental/RemoteSession/Content \nPaths=../../../Engine/Plugins/Runtime/HoudiniEngine/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Substance/Content \nPaths=../../../Engine/Plugins/Enterprise/StaticMeshEditorExtension/Content \nPaths=../../../Engine/Plugins/Editor/MeshEditor/Content \nPaths=../../../Engine/Plugins/Experimental/GeometryCollectionPlugin/Content \nPaths=../../../Engine/Plugins/Experimental/ChaosSolverPlugin/Content \nPaths=../../../Engine/Plugins/Enterprise/DataprepEditor/Content \nPaths=../../../Engine/Plugins/Enterprise/DatasmithContent/Content \nPaths=../../../Engine/Plugins/Experimental/ModelingToolsEditorMode/Content \nPaths=../../../Engine/Plugins/Experimental/MeshModelingToolset/Content \nPaths=../../../Engine/Plugins/Experimental/GeometryProcessing/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/DBDUICore/Content \nPaths=../../../DeadByDaylight/Plugins/Wwise/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/DBDUIMobile/Content \nPaths=../../../Engine/Plugins/2D/Paper2D/Content \nPaths=../../../Engine/Plugins/Developer/TraceSourceFiltering/Content \nPaths=../../../Engine/Plugins/FX/Niagara/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/SentryIo/Content \nPaths=../../../Engine/Plugins/Developer/AnimationSharing/Content \nPaths=../../../Engine/Plugins/Editor/GeometryMode/Content \nPaths=../../../Engine/Plugins/Experimental/ChaosClothEditor/Content \nPaths=../../../Engine/Plugins/Experimental/ChaosNiagara/Content \nPaths=../../../Engine/Plugins/Media/MediaCompositing/Content \nPaths=../../../Engine/Plugins/MovieScene/MovieRenderPipeline/Content")
        
    return

def writeLowestGraphics(Engine): # This Function for adding Lowest Graphics Config to Engine.ini
    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini", "w") as file:
        file.write("""
[/Script/Engine.GarbageCollectionSettings]
IdealLightMapDensity=0.02
MaxLightMapDensity=0.05
gc.TimeBetweenPurgingPendingKillObjects=30
foliage.LODDistanceScale=0.9
foliage.DensityScale=0
r.ViewDistanceScale=0.845
r.AllowLandscapeShadows=0
r.EmitterSpawnRateScale=0.825
r.SeparateTranslucency=False
r.DefaultFeature.Bloom=False
r.DefaultFeature.AmbientOcclusion=False
r.DefaultFeature.AmbientOcclusionStaticFraction=False
r.DefaultFeature.MotionBlur=False
r.DefaultFeature.LensFlare=False
r.DefaultFeature.AntiAliasing=0
r.DistanceFieldShadowing=0
r.DistanceFieldAO=0
PerfIndexValues_ResolutionQuality=24 24 24 24
r.MipMapLODBias=0
r.LightShaftQuality=0
r.SSS.Scale=0
r.SSS.SampleSet=0
r.SSS.Quality=0
r.SkeletalMeshLODBias=2
r.StaticMeshLODDistanceScale=2.35
r.ShadowQuality=0
r.Shadow.CSM.MaxCascades=0
r.Shadow.MaxResolution=16
r.Shadow.DistanceScale=0.85
r.DepthOfFieldQuality=0
r.RenderTargetPoolMin=512
r.Upscale.Quality=0
r.MaxAnisotropy=0
r.TranslucencyLightingVolumeDim=1
r.SceneColorFormat=3
r.ParticleLightQuality=0

[/Script/Engine.NetworkSettings] 
n.VerifyPeer=False


        """)
        
        return 

def removeAllConfigs(Engine): # Remove all configs
    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini", "w") as file:
        file.write("[Core.System] \nPaths=../../../Engine/Content \nPaths=%GAMEDIR%Content \nPaths=../../../Engine/Plugins/Runtime/Bhvr/MirrorsAnalytics/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/OnlinePresence/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/PlatformsProviders/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/VersionNumber/Content \nPaths=../../../Engine/Plugins/Experimental/RemoteSession/Content \nPaths=../../../Engine/Plugins/Runtime/HoudiniEngine/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Substance/Content \nPaths=../../../Engine/Plugins/Enterprise/StaticMeshEditorExtension/Content \nPaths=../../../Engine/Plugins/Editor/MeshEditor/Content \nPaths=../../../Engine/Plugins/Experimental/GeometryCollectionPlugin/Content \nPaths=../../../Engine/Plugins/Experimental/ChaosSolverPlugin/Content \nPaths=../../../Engine/Plugins/Enterprise/DataprepEditor/Content \nPaths=../../../Engine/Plugins/Enterprise/DatasmithContent/Content \nPaths=../../../Engine/Plugins/Experimental/ModelingToolsEditorMode/Content \nPaths=../../../Engine/Plugins/Experimental/MeshModelingToolset/Content \nPaths=../../../Engine/Plugins/Experimental/GeometryProcessing/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/DBDUICore/Content \nPaths=../../../DeadByDaylight/Plugins/Wwise/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/DBDUIMobile/Content \nPaths=../../../Engine/Plugins/2D/Paper2D/Content \nPaths=../../../Engine/Plugins/Developer/TraceSourceFiltering/Content \nPaths=../../../Engine/Plugins/FX/Niagara/Content \nPaths=../../../DeadByDaylight/Plugins/Runtime/Bhvr/SentryIo/Content \nPaths=../../../Engine/Plugins/Developer/AnimationSharing/Content \nPaths=../../../Engine/Plugins/Editor/GeometryMode/Content \nPaths=../../../Engine/Plugins/Experimental/ChaosClothEditor/Content \nPaths=../../../Engine/Plugins/Experimental/ChaosNiagara/Content \nPaths=../../../Engine/Plugins/Media/MediaCompositing/Content \nPaths=../../../Engine/Plugins/MovieScene/MovieRenderPipeline/Content")
        
    return

def writeFPSOptimizer(Engine):
    with open(f"{home}\AppData\Local\DeadbyDaylight\Saved\Config\WindowsNoEditor\Engine.ini", "w") as file:
        file.write("""
[/Script/Engine.GarbageCollectionSettings]
IdealLightMapDensity=0.02
MaxLightMapDensity=0.05
gc.TimeBetweenPurgingPendingKillObjects=16
foliage.LODDistanceScale=0.1
foliage.DensityScale=0
grass.DensityScale=0
r.Streaming.Boost=0
r.Streaming.MipBias=0
BoostPlayerTextures=0
r.ViewDistanceScale=0.675
r.AllowLandscapeShadows=0
r.AmbientOcclusionMaxQuality=0
r.EmitterSpawnRateScale=0.310
r.SeparateTranslucency=False
r.DefaultFeature.Bloom=False
r.DefaultFeature.AmbientOcclusion=False
r.DefaultFeature.AmbientOcclusionStaticFraction=False
r.DefaultFeature.MotionBlur=False
r.DefaultFeature.LensFlare=False
r.DefaultFeature.AntiAliasing=0
r.DistanceFieldShadowing=0
r.DistanceFieldAO=0
PerfIndexValues_ResolutionQuality=8 8 8 8
r.MipMapLODBias=4
r.MSAA.CompositingSampleCount=0
r.LightShaftQuality=0
r.SSS.Scale=0
r.SSS.SampleSet=0
r.SSS.Quality=0
r.SkeletalMeshLODBias=5
r.StaticMeshLODDistanceScale=20
r.ShadowQuality=0
r.Shadow.CSM.MaxCascades=0
r.Shadow.MaxResolution=2
r.Shadow.DistanceScale=0.1
r.DepthOfFieldQuality=0
r.RenderTargetPoolMin=256
r.Upscale.Quality=0
r.MaxAnisotropy=0
r.TranslucencyLightingVolumeDim=1
r.VolumetricFog=0
r.SceneColorFormat=3
r.ParticleLightQuality=0

[/Script/Engine.NetworkSettings] 
n.VerifyPeer=False

         """)
        
        return



def intro(): # Just ASCII art LOL
    
    print("""

░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░  ███████╗██████╗░██╗████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░  ██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░  █████╗░░██║░░██║██║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗  ██╔══╝░░██║░░██║██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝  ███████╗██████╔╝██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░  ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                    Config Editor Installer
                            DISCLAIMER : No Ban Chance for using those!
                                    Author 1ntrovertskrrt
    """)


def menu(): # Select Platfrom Menu
    intro()
    print("Select your choice!")
    print("1. Install SSL Bypass Steam")
    print("2. Remove SSL Bypass")
    print("3. DBD Configs")
    print("4. Remove all Configs")
    print("5. Exit")
    return

menu()

command = ""
while command != "5":
    command = input("Enter Numbers: ")

    if command == "1": # install SSL Bypass
        write_ConfigSteam = writeConfigFileSteam("Engine.ini")
        time.sleep(1)
        print("SSL Bypass Successfully Installed!")
        time.sleep(2)
        os.system('cls')
        menu()

    if command == "2": # remove SSL Bypass
        removeSSLBypassSteam = removeConfigFilesSteam("Engine.ini")
        print("Deleting your SSL Bypass...")
        time.sleep(1)
        print("SSL Bypass has been removed!")
        time.sleep(2)
        os.system('cls')
        menu()

    if command == "3": # DBD Config Menu
        os.system('cls')
        print("Select your Dead by Daylight Configs")
        print("1. Lowest Graphics Settings")
        print("2. FPS Optimizer")
        print("3. FOV Jesus Config (Not Available)")
        print("9. back")
        command = input("Enter: ")

        if command == "1": # adding Lowest Graphics Config
            time.sleep(2)
            addLowestGraphicsConfig = writeLowestGraphics("Engine.ini")
            print("Lowest Graphics Config has been installed!")
            time.sleep(1)
            os.system("cls")
            menu()

        if command == "2": # adding FPS Optimizer Config
            time.sleep(2)
            addFPSOptimizer = writeFPSOptimizer("Engine.ini")
            print("FPS Optimizer Config has been installed!")
            time.sleep(1)
            os.system("cls")
            menu()
            

        if command == "3": # Currently not available
            os.system("cls")
            print("This config currently not available")
            time.sleep(2)
            os.system("cls")
            menu()

        if command == "9": # back
            menu()
        
    if command == "4": # Remove all configs and reset to default
        time.sleep(2)
        clearAllConfigs = removeAllConfigs("Engine.ini")
        print("Config has been restored to default!")
        time.sleep(1)
        os.system("cls")
        menu()

    if command == "5": # program closed
        break
