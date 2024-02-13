# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME
# EMAIL
# STUDENT ID


def user_interface():
    print("Welcome! Please choose an option:")
    print("c - Create a new DSU file")
    print("l - Load an existing DSU file")
    print("admin - Enter Admin mode for advanced commands")
    choice = input("Your choice (c/l/admin): ").strip().lower()

    if choice == 'c':
        directory = input("Enter the directory where the file should be created: ")
        name = input("What is the name of the new DSU file? ")
        create_profile(directory, name)
    elif choice == 'l':
        filename = input("Enter the full path to the DSU file you would like to load: ")
        load_profile(Path(filename))
    elif choice == 'admin':
        return True  # Proceed to admin_mode function
    else:
        print("Invalid choice. Please try again.")
    return False  # Stay in user mode

def admin_mode():
    print("Welcome to Admin mode! Please choose an option:")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'q':
            break
    # Handle admin commands here, similar to the main function's logic
    # This is a placeholder for actual admin command processing
    print("Admin command processing is not implemented in this example.")