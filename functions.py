# Function file #

import subprocess

def start():
    macAddress = osInput()
    subprocess.call("ifconfig wlan0 down", shell=True)
    subprocess.call("ifconfig wlan0 hw ether" + macAddress, shell=True)
    subprocess.call("ifconfig wlan0 up" + macAddress, shell=True)


def osInput():
    macAddress = str(input("Please input a new MAC address in correct format (e.g 11:22:33:44:55:66)" + "\n"))
    return macAddress
