import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import json
from os import path

def go():
    install()
    print("go orange!")
     

def install():
    config = 'start.json'
    system = { "system": True }
    js = json.JSONEncoder().encode(system)
    if path.exists(config):
        with open(config,'r') as config_file:
            start = json.load(config_file)
            jl = json.loads(start)  
            if jl['system']:
                print("system libraries installed")
            else:
                install_system()
    else: 
        with open(config,'w') as config_file:
            json.dump(js, config_file)
        install_system()

def install_system():
    print("installing sytem...")


def show_window():
  print("...show_window")
  window = Gtk.Window(title="Hello World")
  window.show()
  window.connect("destroy", Gtk.main_quit)
  Gtk.main()


if __name__ == "__main__":
    show_window()
