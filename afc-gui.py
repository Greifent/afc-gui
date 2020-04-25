#!/usr/bin/python3.7

import subprocess as sub

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

#==========================================================================================
#define function for adjusting text
def modelinfo_fun():

	modelinfo = sub.check_output("sudo asus-fan-control model-info", shell=True)

	modelinfo = modelinfo.decode("utf-8")

	modelinfo = modelinfo.replace("\n", " \n")

	modelinfo = "Those are the information of your model: \n" + modelinfo

	return(modelinfo)

def about_fun():

	about = sub.check_output("asus-fan-control about", shell=True)

	about = about.decode("utf-8")

	about = about.replace("\n", " \n")

	about = about.replace("github.com/dominiksalvet/asus-fan-control", '<a href="https://github.com/dominiksalvet/asus-fan-control" title="Click to found more">project page</a>')

	about = "Current version of asus-fan-control running: \n" + about

	return(about)

def gettemps_fun():

	gettemps = sub.check_output("sudo asus-fan-control get-temps", shell=True)

	gettemps = gettemps.decode("utf-8")

	gettemps = gettemps.replace("\n", " \n")

	gettemps = "Those are the active temperatures: \n" + gettemps

	gettemps = gettemps + " \n \n In the following section you can chose to set your own temperatures \n (enter 8 values separed by a space) \n or reimpost the default ones"

	return(gettemps)

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
		label.set_text(modelinfo_fun())
		vbox_left.pack_start(label, True, True, 0)

		label = Gtk.Label()
		label.set_markup(about_fun())
		vbox_left.pack_start(label ,True, True, 0)

		label = Gtk.Label()
		label.set_text(gettemps_fun())
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
		self.settemps.connect("clicked", self.whensettemps_clicked)
		vbox_right.pack_start(self.settemps, True, True, 0)

		self.default = Gtk.Button("Set default temperatures")
		self.default.connect("clicked", self.whendefault_clicked)
		vbox_right.pack_start(self.default, True, True, 0)

#end creating buttons
#==========================================================================================

		self.add(hbox)

#==========================================================================================
#definition of funcions called when button press

	def whensettemps_clicked(self, widget):
		sub.call("sudo asus-fan-control set-temps " + self.temperatures.get_text(), shell=True)

	def whendefault_clicked(self, widget):
		sub.call("sudo asus-fan-control set-temps default", shell=True)

#end of definition for functions called when button pressed
#==========================================================================================
#open window

window = asuswindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

#close window
#==========================================================================================
