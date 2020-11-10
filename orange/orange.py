import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def go():
    print("go orange!")


def show_window():
  window = Gtk.Window(title="Hello World")
  window.show()
  window.connect("destroy", Gtk.main_quit)
  Gtk.main()


if __name__ == "__main__":
    go()
    show_window()
