import re
from MAC import MAC

def help():
    print("\n+++++++++++++++++++++++ MACmon +++++++++++++++++++++++\n")
    print("--interface    -i       : Set the interface name")
    print("--getMAC       -gmac    : GET MAC address")
    print("--changeMAC    -cmac    : CHANGE MAC address")
    print("--getMODE      -gmode   : GET Interface MODE")
    print("--changeMODE   -cmode   : CHANGE Interface MODE")
    print("exit                    : EXIT\n")

def rectify_command(command):
    mc = MAC()
    commandList = re.split("\s", command)

    if commandList[0] != "macmon":
        print("Invalid command!")
        return -1
    
    if commandList[1] == 'exit':
        return 'exit'
    
    if '-h' in commandList or '--help' in commandList:
        help()

    if '-i' in commandList or '--interface' in commandList:
        for i in range(1, len(commandList)):
            if '-i' == commandList[i] or '--interface' == commandList[i]:
                interface = commandList[i+1]
    
    if '-gmac' in commandList or '--getMAC' in commandList:
        macAddr = mc.get_MAC(interface)
        print("Current MAC Address of " + interface + " interface is " + macAddr)

    if '-cmac' in commandList or '--changeMAC' in commandList:
        mc.change_MAC(interface)
    
    if '-gmode' in commandList or '--getMODE' in commandList:
        mc.get_mode(interface)
    
    if '-cmode' in commandList or '--changeMODE' in commandList:
        mc.change_mode(interface)