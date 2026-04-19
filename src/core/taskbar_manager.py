# taskbar_manager.py

class TaskbarManager:
    def __init__(self):
        self.taskbar_items = []

    def add_taskbar_item(self, item):
        """Add a window or application to the taskbar."""
        self.taskbar_items.append(item)

    def remove_taskbar_item(self, item):
        """Remove an item from the taskbar."""
        self.taskbar_items.remove(item)

    def display_taskbar(self):
        """Render the taskbar with its items."""
        for item in self.taskbar_items:
            item.render()
