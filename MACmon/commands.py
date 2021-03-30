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

    commandDic = {  '-i': None,
                    '--interface': None,
                    '-gmac': None,
                    '--getMAC': None,
                    '-cmac': None,
                    '--changeMAC': None,
                    '-gmode': None,
                    '--getMODE': None,
                    '-cmode': None,
                    '--changeMODE': None
                }
    
    if '-h' in commandList or '--help' in commandList:
        help()
        return -1

    for i in range(1, len(commandList)):
        if '-i' == commandList[i] or '--interface' == commandList[i]:
            commandDic['-i'] = commandList[i+1]
            commandDic['--interface'] = commandList[i+1]

        if '-cmac' == commandList[i] or '--changeMAC' == commandList[i]:
            commandDic['-cmac'] = commandList[i+1]
            commandDic['--changeMAC'] = commandList[i+1]

        if '-cmode' == commandList[i] or '--changeMODE' == commandList[i]:
            commandDic['-cmode'] = commandList[i+1]
            commandDic['--changeMODE'] = commandList[i+1]

    if '-gmac' in commandList or '--getMAC' in commandList:
        macAddr = mc.get_MAC(commandDic['-i'])
        if macAddr is not None:
            print("[+] Current MAC Address is " + macAddr)

    if '-cmac' in commandList or '--changeMAC' in commandList:
        if '-cmac' is not None  and '--changeMAC' is not None:
            newMAC = mc.change_MAC(commandDic['-i'], commandDic['-cmac'])
    
    if '-gmode' in commandList or '--getMODE' in commandList:
        mode = mc.get_mode(commandDic['-i'])
        if mode is not None:
            print("[+] Current Mode is " + mode)
    
    if '-cmode' in commandList or '--changeMODE' in commandList:
        if '-cmode' is not None  and '--changeMODE' is not None:
            newMODE = mc.change_mode(commandDic['-i'], commandDic['-cmode'])