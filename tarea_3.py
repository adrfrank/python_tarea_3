#!/usr/bin/env python
# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
from datetime import datetime

class HelloWorld:

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.

    def printHour(self):
    	strh = str(datetime.today())
    	print strh
    	self.label.set_text(strh)

    def hello(self, widget, data=None):
        self.printHour()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(10)
        self.window.set_title("Tarea 3 - Intefaz grafica GTK")
        self.label = gtk.Label("De click para obtener la hora")
        self.button = gtk.Button("Click!")
        self.button.connect("clicked", self.hello, None)
        self.container = gtk.Fixed()
        self.container.set_size_request(300, 200)
        self.container.show()
        self.container.put(self.label,40,40)
        self.container.put(self.button, 0,0)
        self.window.add(self.container)

        self.button.show()
        self.label.show()
        self.window.show()

    def main(self):
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
