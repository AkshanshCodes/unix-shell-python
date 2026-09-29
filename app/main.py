import sys


def main():
    builtins = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        command = input()
        parts = command.split()
        if command == "exit":
            break
        elif parts[0] == "echo":
            print(command[5:])
        elif parts[0] == "type":
            if parts[1] in builtins:
                print(f"{parts[1]} is a shell builtin")
            else:
                print(f"{parts[1]}: not found")
        else:
            print(f"{command}: command not found")
        
if __name__ == "__main__":
    main()
