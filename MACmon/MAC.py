import subprocess
import re

class MAC:
    def get_MAC(self, interface):
        output = subprocess.run(["ifconfig", interface], shell = False, capture_output = True)
        cmdResult = output.stdout.decode('utf-8')

        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        regex = re.compile(pattern)

        ans = regex.search(cmdResult)

        currentMAC = ans.group().split(" ")[1]

        return currentMAC

    def change_MAC(self, interface, newMAC):
        print("[+] Current MAC address is:", self.get_MAC(interface))

        # ifconfig wlano down
        output = subprocess.run(["ifconfig", interface, "down"], shell = False, capture_output = True)
        print(output.stderr.decode('utf-8'))
        
        # ifconfig wlan0 hw ether 00:11:22:33:44:55
        output = subprocess.run(["ifconfig", interface, "hw", "ether", newMAC], shell = False, capture_output = True)
        print(output.stderr.decode('utf-8'))
        
        # ifconfig wlan0 up
        output = subprocess.run(["ifconfig", interface, "up"], shell = False, capture_output = True)
        print(output.stderr.decode('utf-8'))
        
        newMAC = self.get_MAC(interface)
        print("[+] Updated MAC address is:", newMAC)

        return newMAC
    
    def get_mode(self, interface):
        pass
    
    def change_mode(self, interface):
        pass