# theme_loader.py

class ThemeLoader:
    def __init__(self, theme_name):
        self.theme_name = theme_name
        self.theme = self.load_theme()
    
    def load_theme(self):
        """Load the selected theme from the config directory."""
        theme_path = f'config/themes/{self.theme_name}/theme.conf'
        theme_config = ConfigLoader(theme_path)
        return theme_config
    
    def apply_theme(self):
        """Apply the loaded theme (e.g., colors, icons, background)."""
        # Here you would load the actual theme and apply it to the environment.
        pass
