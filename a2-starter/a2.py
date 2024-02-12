# NAME
# EMAIL
# STUDENT ID

# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

from pathlib import Path
import json

# Placeholder for the Profile class - replace with actual import
class Profile:
    def __init__(self, username, password, bio):
        self.username = username
        self.password = password
        self.bio = bio

    def save(self, filename):
        data = {
            'username': self.username,
            'password': self.password,
            'bio': self.bio
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

def create_profile(directory, name):
    print("Creating a new profile...")
    username = input("Username: ")
    password = input("Password: ")
    bio = input("Bio: ")

    profile = Profile(username, password, bio)
    filename = Path(directory) / f"{name}.dsu"
    profile.save(filename)
    print(f"Profile saved to {filename}")

def list_directory(path, options):
    files = []
    for file_path in Path(path).rglob("*"):
        if file_path.is_file():
            files.append(file_path)

    if '-f' in options:
        files = [file for file in files if file.is_file()]
    elif '-r' not in options:
        files = [file for file in files if file.parent == Path(path)]

    if '-s' in options:
        files = [file for file in files if options['-s'] in file.name]

    if '-e' in options:
        files = [file for file in files if file.suffix == options['-e']]

    files.sort()

    for file in files:
        print(file)

def create_file(directory, name):
    new_file = Path(directory) / f"{name}.dsu"
    new_file.touch()
    print(new_file)

def delete_file(file_path):
    if file_path.suffix != ".dsu":
        print("ERROR")
    elif file_path.exists():
        file_path.unlink()
        print(f"{file_path} DELETED")
    else:
        print("ERROR")

def read_file(file_path):
    try:
        if file_path.suffix != ".dsu":
            raise ValueError("Can only read .dsu files")
        if not file_path.exists():
            raise FileNotFoundError("File does not exist")
        with file_path.open() as file:
            content = file.read().strip()
            print(content if content else "File is empty")
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)

def main():
    while True:
        user_input = input("Enter command: ")
        args = user_input.split()
        command = args[0]

        if command == 'Q':
            print("Quitting the program.")
            break
        elif command == 'L':
            if len(args) < 2:
                print("Please provide a directory path.")
                continue

            directory_path = args[1]
            options = {arg: args[i + 1] for i, arg in enumerate(args[2:]) if arg.startswith('-')}

            list_directory(directory_path, options)
        elif command == 'C':
            if len(args) < 4 or args[2] != '-n':
                print("Invalid command. Usage: C [Directory] -n [name]")
                continue

            directory_path = args[1]
            name = args[3]

            create_file(directory_path, name)
        elif command == 'D':
            if len(args) < 2:
                print("Please provide a file path.")
                continue

            file_path = Path(args[1])
            read_file(file_path)
        else:
            print("Error")

if __name__ == "__main__":
    main()
