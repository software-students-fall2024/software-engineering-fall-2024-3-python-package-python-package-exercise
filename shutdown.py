import os
import sys
import time
import platform
def shutdown_system():
    system_os = platform.system()
    print("computer will shutdown in 20 second, please save your important files ASAP!!")
    time.sleep(20)
    if system_os == "Windows":
        os.system("shutdown /s /t 1")
    else: 
        os.system("sudo shutdown -h now")
        
        
shutdown_system()
