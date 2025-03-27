# virtual_os

# Virtual Operating System (VOS)

## 📌 Project Overview
The **Virtual Operating System (VOS)** is a simplified simulation of an operating system that provides basic functionalities including:

- **Process Management**: Creation, termination, and scheduling of processes using First-Come-First-Serve (FCFS).
- **Memory Management**: Simulated paging-based memory management.
- **File Management**: Creation, deletion, reading, writing, and appending files.
- **Shell Interface**: Command-line interface to interact with the system.

This project is developed using **Python** and is designed to demonstrate how an OS manages its core functionalities.

---

## 🧑‍💻 Features

### ✔️ **Process Management**
- Create and manage processes.
- Implement process scheduling using the **FCFS** algorithm.
- Terminate processes and manage the ready queue.

### ✔️ **Memory Management**
- Manage memory using a **Paging** technique.
- Allocate and deallocate memory for processes.
- Display memory usage.

### ✔️ **File Management**
- Create, delete, read, write, and append files.
- Simulate basic file operations within a virtual directory.

### ✔️ **Shell Interface**
- Provides a user-friendly command-line interface for interacting with the system.

---

## 🛠️ Project Structure
```bash
Virtual-Operating-System/
├── shell.py               # Main entry point (Command-line Interface)
├── process_management.py  # Process Management using FCFS
├── memory_management.py   # Paging-based Memory Management
├── file_management.py     # File Operations Management
├── utils.py               # Utility functions (if applicable)
└── README.md              # Project Documentation
```

---

## 🚀 Installation and Usage

1. **Clone the Repository:**
```bash
git clone https://github.com/your-repo/Virtual-Operating-System.git
cd Virtual-Operating-System
```

2. **Run the Project:**
```bash
python shell.py
```

3. **Example Commands:**
```bash
create_process Process1
allocate_memory 128
create_file file1.txt
write_file file1.txt "Hello, VOS!"
read_file file1.txt
terminate_process 1
exit
```

---

## 🧑‍💻 Supported Commands

### ➡️ **Process Management**
- `create_process <name>` - Create a new process.
- `terminate_process <pid>` - Terminate a specific process.
- `list_processes` - List all processes.

### ➡️ **Memory Management**
- `allocate_memory <size>` - Allocate memory (in MB).
- `free_memory <size>` - Free allocated memory.
- `display_memory` - Show memory status.

### ➡️ **File Management**
- `create_file <filename>` - Create a new file.
- `delete_file <filename>` - Delete a file.
- `read_file <filename>` - Read file contents.
- `write_file <filename> <content>` - Write data to a file.
- `append_file <filename> <content>` - Append data to a file.

### ➡️ **General**
- `exit` - Exit the shell.

---

## ⚙️ Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.

---

## 📧 Contact
For questions or feedback, contact **Chetan Pandey** at [your-email@example.com](mailto:your-email@example.com).

Happy coding! 😊

