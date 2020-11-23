import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess as s
import json
from os import path

def go():
    feedback = install2()
    show_window(feedback)

def install2():
  process = s.Popen(['sudo', 'apt-get', 'install', 'vim'], 
                           stdout=s.PIPE,
                           universal_newlines=True)

  return_code = "no"
  while True:
    output = process.stdout.readline()
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            pass
        break


  return return_code 

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


def show_window(feedback):
  print("...show_window")
  window = Gtk.Window(title=feedback)
  window.show()
  window.connect("destroy", Gtk.main_quit)
  Gtk.main()


if __name__ == "__main__":
    go()
