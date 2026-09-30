import sys
import os


def main():
    builtins = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        parts = command.split()
        if command == "exit":
            break
        elif parts[0] == "echo":
            print(command[5:])
        elif parts[0] == "type":
            target = parts[1]
            # Check if it's a shell builtin
            if target in builtins:
                print(f"{target} is a shell builtin")
            else:
                # Get PATH
                path = os.environ.get("PATH", "")
                directories = path.split(os.pathsep)
                found = False
                # Search every directory in PATH
                for directory in directories:
                    full_path = os.path.join(directory, target)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{target} is {full_path}")
                        found = True
                        break
                # Nothing found in PATH
                if not found:
                    print(f"{target}: not found")
        else:
            print(f"{command}: command not found")
            
if __name__ == "__main__":
    main()