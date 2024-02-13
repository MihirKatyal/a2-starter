# ui.py
# Mihir Katyal
# mkatyal@uci.edu
# 19099879

def user_interface():
    print("Welcome! Please choose an option:")
    print("c - Create a new DSU file")
    print("l - Load an existing DSU file")
    print("admin - Enter Admin mode for advanced commands")
    choice = input("Your choice (c/l/admin): ").strip().lower()

    return choice

def admin_mode():
    print("Welcome to Admin mode! Please choose an option:")
    # Admin mode command prompt is handled in a2.py

