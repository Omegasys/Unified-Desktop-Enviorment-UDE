# taskbar_ui.py

class TaskbarUI:
    def __init__(self, taskbar_manager):
        self.taskbar_manager = taskbar_manager
    
    def display(self):
        """Render the taskbar on the screen."""
        for item in self.taskbar_manager.taskbar_items:
            item.display_on_taskbar()
    
    def interact(self):
        """Handle user interactions with the taskbar (e.g., clicking, dragging)."""
        pass
