#!/usr/bin/env python3

import subprocess as sub

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

#==========================================================================================
#define function for adjusting text

#end define function for adjusting text
#==========================================================================================

class asuswindow(Gtk.Window):

	def __init__(self):

#==========================================================================================
#setting window dimentions

		Gtk.Window.__init__(self, title="asus-fan-control")
		Gtk.Window.set_default_size(self, 400, 325)
		Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

		hbox = Gtk.Box(spacing=10)
		hbox.set_homogeneous(False)
		vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		vbox_left.set_homogeneous(False)
		vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		vbox_right.set_homogeneous(False)

		hbox.pack_start(vbox_left, True, True, 0)
		hbox.pack_start(vbox_right, True, True, 0)

#end settind window dimentions
#==========================================================================================
#add labels
		label = Gtk.Label()
		label.set_text("Test")
		vbox_left.pack_start(label, True, True, 0)

		label = Gtk.Label()
		label.set_markup("Test")
		vbox_left.pack_start(label ,True, True, 0)

		label = Gtk.Label()
		label.set_text("Test")
		vbox_right.pack_start(label, True, True, 0)

#end add labels
#==========================================================================================
#add temperature input

		self.temperatures = Gtk.Entry()
		self.temperatures.set_text("")
		vbox_right.pack_start(self.temperatures, True, True, 0)

#end add temperature input
#==========================================================================================
#creating buttons		

		self.settemps = Gtk.Button("Set custom temps")
		
		vbox_right.pack_start(self.settemps, True, True, 0)

		self.default = Gtk.Button("Set default temperatures")
		
		vbox_right.pack_start(self.default, True, True, 0)

#end creating buttons
#==========================================================================================

		self.add(hbox)

#==========================================================================================
#definition of funcions called when button press

#end of definition for functions called when button pressed
#==========================================================================================
#open window

window = asuswindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

#close window
#==========================================================================================
