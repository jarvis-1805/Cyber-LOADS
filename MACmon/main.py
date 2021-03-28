import commands

def main():
    
    commands.help()

    cmd = -1
    while cmd != 'exit':
        command = input("> ")
        cmd = commands.rectify_command(command)

if __name__ == "__main__":
    main()