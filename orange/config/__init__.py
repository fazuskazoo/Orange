from configparser import ConfigParser
from pathlib import Path
import os

here = Path(__file__).parent
orangecfg = os.path.join(here,'orange.cfg')

config_object = ConfigParser()

config_object["INSTALL"] = {
        "system": False
}


def get_installed():
  if os.path.exists(orangecfg):
    with open(orangecfg, 'r') as conf:
      config_object.read(orangecfg)
      return config_object.getboolean("INSTALL", "system")
  else: # create the file
    _write_config()
    return False;

def set_installed(is_installed):
  if os.path.exists(orangecfg):
    config_object.set("INSTALL", "system",str(is_installed))
    _write_config()

def _write_config():
    with open(orangecfg,'w') as conf:
        return False
