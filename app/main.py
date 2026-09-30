import sys
import os
import subprocess


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
            target = parts[1]

            if target in builtins:
                print(f"{target} is a shell builtin")

            else:
                path = os.environ.get("PATH", "")
                directories = path.split(os.pathsep)

                for directory in directories:
                    full_path = os.path.join(directory, target)

                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{target} is {full_path}")
                        break

                else:
                    print(f"{target}: not found")

        else:
            path = os.environ.get("PATH", "")
            directories = path.split(os.pathsep)

            for directory in directories:
                full_path = os.path.join(directory, parts[0])

                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    subprocess.run(parts)
                    break

            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()