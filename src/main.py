# main.py

from core.window_manager import WindowManager
from core.taskbar_manager import TaskbarManager
from core.desktop_manager import DesktopManager
from config.config_loader import ConfigLoader
from ui.desktop_ui import DesktopUI
from ui.taskbar_ui import TaskbarUI
from utils.config_updater import ConfigUpdater
from utils.time_switcher import TimeSwitcher

def main():
    # Load the configuration files
    config_loader = ConfigLoader("config/ude-config.conf")
    
    # Initialize core components
    window_manager = WindowManager()
    taskbar_manager = TaskbarManager()
    desktop_manager = DesktopManager()
    
    # Initialize UI components
    desktop_ui = DesktopUI(desktop_manager)
    taskbar_ui = TaskbarUI(taskbar_manager)
    
    # Initialize utility functions
    config_updater = ConfigUpdater("config/ude-config.conf")
    time_switcher = TimeSwitcher(config_loader)
    
    # Start configuration monitoring
    config_updater.start_monitoring()
    
    # Main event loop for the desktop environment
    while True:
        # Handle time-based theme switching
        time_switcher.check_time_and_switch_theme()

        # Render the desktop and taskbar UI
        desktop_ui.render()
        taskbar
