# config_loader.py
import configparser

class ConfigLoader:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
    
    def get(self, section, option):
        """Fetch a configuration value."""
        return self.config.get(section, option)
    
    def set(self, section, option, value):
        """Set a configuration value."""
        self.config.set(section, option, value)
        with open('ude-config.conf', 'w') as configfile:
            self.config.write(configfile)
