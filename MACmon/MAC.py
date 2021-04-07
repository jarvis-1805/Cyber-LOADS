import subprocess
import re

class MAC:
    def get_MAC(self, interface):
        output = subprocess.run(["ifconfig", interface], shell = False, capture_output = True)
        cmdResult = output.stdout.decode('utf-8')

        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        regex = re.compile(pattern)

        ans = regex.search(cmdResult)

        if ans is not None:
            currentMAC = ans.group().split(" ")[1]
            return currentMAC
        
        return None

    def change_MAC(self, interface, newMAC):
        print("[+] Current MAC address is:", self.get_MAC(interface))

        # ifconfig wlan0 down
        output = subprocess.run(["ifconfig", interface, "down"], shell = False, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))
        
        # ifconfig wlan0 hw ether 00:11:22:33:44:55
        output = subprocess.run(["ifconfig", interface, "hw", "ether", newMAC], shell = False, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))
        
        # ifconfig wlan0 up
        output = subprocess.run(["ifconfig", interface, "up"], shell = False, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))
        
        newMAC = self.get_MAC(interface)
        print("[+] Updated MAC address is:", newMAC)

        return newMAC
    
    def get_mode(self, interface):
        output = subprocess.run(["iwconfig", interface], shell = False, capture_output = True)
        cmdResult = output.stdout.decode('utf-8')

        pattern = r'Mode:(\w+)'

        regex = re.compile(pattern)

        ans = regex.search(cmdResult)

        if ans is not None:
            currentMODE = ans.group().split(":")[1]
            return currentMODE

        return None

    def change_mode(self, interface, newMODE):
        print("[+] Current MODE is:", self.get_mode(interface))

        # ifconfig wlan0 down
        output = subprocess.run(["ifconfig", interface, "down"], shell = False, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))
        
        print("[+] Killing Network Manager...")
        # airmon-ng check kill
        output = subprocess.run(["airmon-ng check kill"], shell = True, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))
        if output:
            print(output.stdout.decode('utf-8'))

        # iwconfig wlan0 mode monitor
        output = subprocess.run(["iwconfig", interface, "mode", newMODE], shell = False, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))

        # ifconfig wlan0 up
        output = subprocess.run(["ifconfig", interface, "up"], shell = False, capture_output = True)
        if output.stderr.decode('utf-8'):
            print(output.stderr.decode('utf-8'))
        
        newMODE = self.get_mode(interface)
        print("[+] Updated Mode is:", newMODE)

        return newMODE