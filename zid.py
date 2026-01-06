import datetime
import pyperclip

import configparser
import os

def get_config():
    """Reads settings from config.ini."""
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    
    defaults = {
        'format': '%Y%m%d%H%M%S',
        'prefix': '',
        'suffix': ''
    }
    
    if not os.path.exists(config_path):
        return defaults
    
    try:
        config.read(config_path)
        return {
            'format': config.get('Settings', 'format', fallback=defaults['format']),
            'prefix': config.get('Settings', 'prefix', fallback=defaults['prefix']),
            'suffix': config.get('Settings', 'suffix', fallback=defaults['suffix'])
        }
    except Exception:
        return defaults

def generate_zid(cfg=None):
    """Generates a ZID string based on the provided configuration."""
    if cfg is None:
        cfg = get_config()
    
    timestamp = datetime.datetime.now().strftime(cfg['format'])
    return f"{cfg['prefix']}{timestamp}{cfg['suffix']}"

def main():
    cfg = get_config()
    current_time = generate_zid(cfg)
    
    # Copy the string to the clipboard
    pyperclip.copy(current_time)
    
    # Print the string to the screen
    print(current_time)

if __name__ == "__main__":
    main()
