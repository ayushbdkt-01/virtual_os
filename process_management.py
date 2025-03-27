
# # process_management.py
# print("[Process Management] Module Loaded")

# class Process:
#     def __init__(self, pid, name, state="Ready"):
#         self.pid = pid
#         self.name = name
#         self.state = state

#     def __str__(self):
#         return f"PID: {self.pid}, Name: {self.name}, State: {self.state}"


# class ProcessManager:
#     def __init__(self):
#         self.process_list = []
#         self.pid_counter = 1

#     def create_process(self, process_name):
#         process = Process(self.pid_counter, process_name)
#         self.process_list.append(process)
#         print(f"Process Created: {process}")
#         self.pid_counter += 1

#     def terminate_process(self, pid):
#         for process in self.process_list:
#             if process.pid == pid:
#                 self.process_list.remove(process)
#                 print(f"Process Terminated: {process}")
#                 return
#         print(f"Process with PID {pid} not found.")

#     def list_processes(self):
#         if not self.process_list:
#             print("No active processes.")
#         else:
#             for process in self.process_list:
#                 print(process)

# process_manager = ProcessManager()


# process_management.py
print("[Process Management] Module Loaded")

class Process:
    def __init__(self, pid, name, state="Ready"):
        self.pid = pid
        self.name = name
        self.state = state

    def __str__(self):
        return f"PID: {self.pid}, Name: {self.name}, State: {self.state}"


class ProcessManager:
    def __init__(self):
        self.process_list = []
        self.ready_queue = []
        self.running_process = None
        self.pid_counter = 1

    def create_process(self, process_name):
        process = Process(self.pid_counter, process_name)
        self.process_list.append(process)
        self.ready_queue.append(process)
        print(f"Process Created: {process}")
        self.pid_counter += 1
        self.schedule_process()

    def terminate_process(self, pid):
        for process in self.process_list:
            if process.pid == pid:
                self.process_list.remove(process)
                if process in self.ready_queue:
                    self.ready_queue.remove(process)
                if self.running_process == process:
                    self.running_process = None
                    print(f"Running process terminated: {process}")
                    self.schedule_process()
                else:
                    print(f"Process Terminated: {process}")
                return
        print(f"Process with PID {pid} not found.")

    def list_processes(self):
        if not self.process_list:
            print("No active processes.")
        else:
            for process in self.process_list:
                print(process)

    def schedule_process(self):
        if not self.running_process and self.ready_queue:
            self.running_process = self.ready_queue.pop(0)
            self.running_process.state = "Running"
            print(f"Process Scheduled: {self.running_process}")

process_manager = ProcessManager()
