# window_manager.py

class WindowManager:
    def __init__(self):
        self.windows = []
    
    def add_window(self, window):
        """Adds a new window to the system."""
        self.windows.append(window)
    
    def remove_window(self, window):
        """Removes a window from the system."""
        self.windows.remove(window)
    
    def manage_windows(self):
        """Adjust window positions, size, and other interactions."""
        for window in self.windows:
            window.update_position()
            window.update_size()
