
# shell.py
print("[Shell] Module Loaded")
from process_management import process_manager
from memory_management import memory_manager
from file_management import file_manager

def start_shell():
    print("Virtual OS Shell Started. Type 'exit' to quit.")
    while True:
        command = input("$ ")
        if command == "exit":
            print("Exiting Virtual OS Shell.")
            break
        elif command.startswith("create_process"):
            _, name = command.split(" ", 1)
            process_manager.create_process(name)
        elif command.startswith("terminate_process"):
            _, pid = command.split(" ", 1)
            process_manager.terminate_process(int(pid))
        elif command == "list_processes":
            process_manager.list_processes()
        elif command.startswith("allocate_memory"):
            _, size = command.split(" ", 1)
            memory_manager.allocate_memory(int(size))
        elif command.startswith("free_memory"):
            _, size = command.split(" ", 1)
            memory_manager.free_memory(int(size))
        elif command.startswith("create_file"):
            _, name = command.split(" ", 1)
            file_manager.create_file(name)
        elif command.startswith("delete_file"):
            _, name = command.split(" ", 1)
            file_manager.delete_file(name)
        else:
            print(f"Command not recognized: {command}")
