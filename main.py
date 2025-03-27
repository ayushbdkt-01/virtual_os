# main.py
import os

# Main entry point
if __name__ == "__main__":
    print("Welcome to the Virtual Operating System!")
    print("Initializing modules...")

    # Importing modules
    import process_management
    import memory_management
    import file_management
    import shell

    print("Initialization complete. Starting shell...")
    shell.start_shell()

