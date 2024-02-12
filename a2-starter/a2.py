# NAME
# EMAIL
# STUDENT ID

# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

from pathlib import Path
import json
from Profile import Profile, Post, DsuFileError, DsuProfileError

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
    try:
        profile.save(filename)
        print(f"Profile saved to {filename}")
    except DsuFileError as e:
        print(f"Failed to save profile: {e}")

def load_profile(filename):
    try:
        profile = Profile()
        profile.load(filename)
        print(f"Loaded profile from {filename}")
        return profile
    except (DsuFileError, DsuProfileError) as e:
        print(f"Failed to load profile: {e}")
        return None
    
def edit_profile(profile, args):
    for i in range(1, len(args), 2):
        if args[i] == '-usr':
            profile.username = args[i + 1]
        elif args[i] == '-pwd':
            profile.password = args[i + 1]
        elif args[i] == '-bio':
            profile.bio = args[i + 1]
        elif args[i] == '-addpost':
            profile.add_post(Post(args[i + 1]))
        elif args[i] == '-delpost':
            if profile.del_post(int(args[i + 1])):
                print("Post deleted.")
            else:
                print("Failed to delete post.")
    try:
        profile.save(filename)  # Assumes filename is stored or passed appropriately
        print("Profile updated.")
    except DsuFileError as e:
        print(f"Failed to update profile: {e}")

def print_profile(profile, args):
    if '-all' in args:
        print(f"Username: {profile.username}, Password: {profile.password}, Bio: {profile.bio}")
        for post in profile.get_posts():
            print(f"Post: {post.entry}, Timestamp: {post.timestamp}")




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

def delete_file(file_path):
    try:
        if file_path.suffix != ".dsu":
            raise ValueError("Can only delete .dsu files")
        file_path.unlink()
        print(f"{file_path} deleted")
    except FileNotFoundError:
        print("File not found")
    except ValueError as e:
        print(e)

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
            break
        elif command == 'C' and len(args) >= 4 and args[2] == '-n':
            create_profile(args[1], args[3])
        elif command == 'L' and len(args) >= 2:
            options = {args[i]: args[i + 1] for i in range(2, len(args), 2)}
            list_directory(args[1], options)
        elif command == 'D' and len(args) == 2:
            delete_file(Path(args[1]))
        elif command == 'R' and len(args) == 2:
            read_file(Path(args[1]))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
