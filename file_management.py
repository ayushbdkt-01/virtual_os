# file_management.py
import os
print("[File Management] Module Loaded")

class FileManager:
    def __init__(self, base_dir='data'):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def create_file(self, filename):
        filepath = os.path.join(self.base_dir, filename)
        if os.path.exists(filepath):
            print(f"Error: File '{filename}' already exists.")
        else:
            with open(filepath, 'w') as f:
                print(f"File '{filename}' created.")

    def delete_file(self, filename):
        filepath = os.path.join(self.base_dir, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"File '{filename}' deleted.")
        else:
            print(f"Error: File '{filename}' not found.")

    def read_file(self, filename):
        filepath = os.path.join(self.base_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                print(f.read())
        else:
            print(f"Error: File '{filename}' not found.")

    def write_file(self, filename, content):
        filepath = os.path.join(self.base_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
            print(f"Data written to '{filename}'.")

    def append_file(self, filename, content):
        filepath = os.path.join(self.base_dir, filename)
        with open(filepath, 'a') as f:
            f.write(content)
            print(f"Data appended to '{filename}'.")

file_manager = FileManager()
