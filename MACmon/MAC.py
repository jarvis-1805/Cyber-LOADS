import subprocess

# ifconfig wlano down
# ifconfig wlan0 hw ether 00:11:22:33:44:55
# ifconfig wlan0 up

class MAC:
    def __init__(self):
        self.MAC = ""

    def get_MAC(self, interface):
        output = subprocess.run(["ifconfig", interface], shell = False, capture_output = True)
        finalOutput = output.stdout.decode('utf-8')
        return finalOutput
    
    def change_MAC(self, interface):
        pass
    
    def get_mode(self, interface):
        pass
    
    def change_mode(self, interface):
        pass