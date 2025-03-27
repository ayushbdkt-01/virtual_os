import streamlit as st
from process_management import ProcessManager
from memory_management import MemoryManager
from file_management import FileManager

process_manager = ProcessManager()
memory_manager = MemoryManager()
file_manager = FileManager()

def process_section():
    st.header("Process Management")
    action = st.selectbox("Select Action", ["Create Process", "Terminate Process", "List Processes"])

    if action == "Create Process":
        process_name = st.text_input("Enter Process Name")
        if st.button("Create Process"):
            process_manager.create_process(process_name)

    elif action == "Terminate Process":
        pid = st.number_input("Enter Process ID", min_value=1, step=1)
        if st.button("Terminate Process"):
            process_manager.terminate_process(pid)

    elif action == "List Processes":
        if st.button("Show Processes"):
            process_manager.list_processes()

def memory_section():
    st.header("Memory Management")
    action = st.selectbox("Select Action", ["Allocate Memory", "Free Memory", "Display Memory"])

    if action == "Allocate Memory":
        size = st.number_input("Enter Memory Size (MB)", min_value=1, step=1)
        if st.button("Allocate Memory"):
            memory_manager.allocate_memory(size)

    elif action == "Free Memory":
        size = st.number_input("Enter Memory Size to Free (MB)", min_value=1, step=1)
        if st.button("Free Memory"):
            memory_manager.free_memory(size)

    elif action == "Display Memory":
        if st.button("Show Memory Status"):
            memory_manager.display_memory()

def file_section():
    st.header("File Management")
    action = st.selectbox("Select Action", ["Create File", "Delete File", "Read File", "Write File", "Append File"])

    if action == "Create File":
        filename = st.text_input("Enter File Name")
        if st.button("Create File"):
            file_manager.create_file(filename)

    elif action == "Delete File":
        filename = st.text_input("Enter File Name")
        if st.button("Delete File"):
            file_manager.delete_file(filename)

    elif action == "Read File":
        filename = st.text_input("Enter File Name")
        if st.button("Read File"):
            file_manager.read_file(filename)

    elif action == "Write File":
        filename = st.text_input("Enter File Name")
        content = st.text_area("Enter Content")
        if st.button("Write File"):
            file_manager.write_file(filename, content)

    elif action == "Append File":
        filename = st.text_input("Enter File Name")
        content = st.text_area("Enter Content to Append")
        if st.button("Append File"):
            file_manager.append_file(filename, content)

def main():
    st.title("Virtual Operating System")
    tab1, tab2, tab3 = st.tabs(["Process Management", "Memory Management", "File Management"])

    with tab1:
        process_section()
    with tab2:
        memory_section()
    with tab3:
        file_section()

if __name__ == "__main__":
    main()
