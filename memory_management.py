# memory_management.py
print("[Memory Management with Paging] Module Loaded")

class Page:
    def __init__(self, page_id, size):
        self.page_id = page_id
        self.size = size
        self.allocated = False

    def __str__(self):
        status = "Allocated" if self.allocated else "Free"
        return f"Page ID: {self.page_id}, Size: {self.size}MB, Status: {status}"


class MemoryManager:
    def __init__(self, total_memory=1024, page_size=128):
        self.total_memory = total_memory
        self.page_size = page_size
        self.pages = [Page(i, page_size) for i in range(total_memory // page_size)]

    def allocate_memory(self, size):
        pages_needed = (size + self.page_size - 1) // self.page_size
        free_pages = [page for page in self.pages if not page.allocated]

        if len(free_pages) >= pages_needed:
            for i in range(pages_needed):
                free_pages[i].allocated = True
            print(f"Allocated {size}MB using {pages_needed} pages.")
        else:
            print("Memory allocation failed. Not enough free pages available.")

    def free_memory(self, size):
        pages_to_free = (size + self.page_size - 1) // self.page_size
        allocated_pages = [page for page in self.pages if page.allocated]

        if len(allocated_pages) >= pages_to_free:
            for i in range(pages_to_free):
                allocated_pages[i].allocated = False
            print(f"Freed {size}MB using {pages_to_free} pages.")
        else:
            print("Error: Cannot free more memory than allocated.")

    def display_memory(self):
        print("Memory Status:")
        for page in self.pages:
            print(page)

memory_manager = MemoryManager()
