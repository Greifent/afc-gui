#!/usr/bin/env python3

import subprocess as sub

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

#==========================================================================================
#define function for adjusting text
#def modelinfo_fun():

#	modelinfo = sub.check_output("sudo asus-fan-control model-info", shell=True)

#	modelinfo = modelinfo.decode("utf-8")

#	modelinfo = modelinfo.replace("\n", " \n")

#	modelinfo = "Those are the information of your model: \n" + modelinfo

#	return(modelinfo)

#def about_fun():

#	about = sub.check_output("asus-fan-control about", shell=True)

#	about = about.decode("utf-8")

#	about = about.replace("\n", " \n")

#	about = about.replace("github.com/dominiksalvet/asus-fan-control", '<a href="https://github.com/dominiksalvet/asus-fan-control" title="Click to found more">project page</a>')	#create link to asus-fan-control project

#	about = "Current version of asus-fan-control running: \n" + about

#	return(about)

#def gettemps_fun():

#	gettemps = sub.check_output("sudo asus-fan-control get-temps", shell=True)

#	gettemps = gettemps.decode("utf-8")

#	gettemps = gettemps.replace("\n", " \n")

#	gettemps = "Those are the active temperatures: \n" + gettemps

#	gettemps = gettemps + " \n \n In the following section you can chose to set your own temperatures \n (enter 8 values separed by a space) \n or reimpost the default ones"

#	return(gettemps)

#end define function for adjusting text
#==========================================================================================

class asuswindow(Gtk.Window):

	def __init__(self):

#==========================================================================================
#setting window dimentions

		Gtk.Window.__init__(self, title="asus-fan-control")		#set title
		Gtk.Window.set_default_size(self, 400, 325)			#set main window dimentions
		Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)	#set where the window create: center screen

		hbox = Gtk.Box(spacing=10)					#pixels between buttons
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
		label = Gtk.Label()						#add label for model info
		label.set_text("model info")
		vbox_left.pack_start(label, True, True, 0)

		label = Gtk.Label()						#add label for about under mode info
		label.set_markup("about")
		vbox_left.pack_start(label ,True, True, 0)

		label = Gtk.Label()						#add label for get temps right to mode info
		label.set_text("get temps")
		vbox_right.pack_start(label, True, True, 0)

#end add labels
#==========================================================================================
#add temperature input

		self.temperatures = Gtk.Entry()					#input for manual temperature insert
		self.temperatures.set_text("")
		vbox_right.pack_start(self.temperatures, True, True, 0)

#end add temperature input
#==========================================================================================
#creating buttons

		self.settemps = Gtk.Button("Set custom temps")			#create button fot set temps, see comment above for temps
		self.settemps.connect("clicked", self.whensettemps_clicked)
		vbox_right.pack_start(self.settemps, True, True, 0)

		self.default = Gtk.Button("Set default temperatures")		#create button for default temps
		self.default.connect("clicked", self.whendefault_clicked)
		vbox_right.pack_start(self.default, True, True, 0)

		self.loadfiles = Gtk.Button("Load preset")			#create button to load temps from file
		self.loadfiles.connect("clicked", self.whenloadfiles_clicked)
		vbox_right.pack_start(self.loadfiles, True, True, 0)

#end creating buttons
#==========================================================================================

		self.add(hbox)							#add label, input, buttons to window

#==========================================================================================
#definition of funcions called when button press

	def whensettemps_clicked(self, widget):
		#sub.call("sudo asus-fan-control set-temps " + self.temperatures.get_text(), shell=True)			#set temps from previous input
		print ("Set temps")

	def whendefault_clicked(self, widget):
		#sub.call("sudo asus-fan-control set-temps default", shell=True)						#set default temps
		print ("Default")

	def whenloadfiles_clicked(self, widget):
		dialog = Gtk.FileChooserDialog(										#create window for file selection
			"Select a .afc file",										#add title
			self,
			Gtk.FileChooserAction.OPEN,
			(
				Gtk.STOCK_CANCEL,									#add Cancel button and Ok button
				Gtk.ResponseType.CANCEL,
				Gtk.STOCK_OPEN,
				Gtk.ResponseType.OK,
			),
		)

		response = dialog.run()

		if response == Gtk.ResponseType.OK:									#if file is selected and Ok button is pressed
			self.linkpreset = dialog.get_filename()								#get file path
			file = open(dialog.get_filename(), "r")								#open file
			global preset
			preset = file.read()										#read file, save it in preset: a global variable
			file.close()
			preset = preset.replace("\n", "")
			dialogConf = ConfirmTemps(self)									#call confirm window, see below
			response = dialogConf.run()

			if response == Gtk.ResponseType.OK:								#if the confirm return is Ok
				#sub.call("sudo asus-fan-control set-temps " + preset, shell=True)			#apply the temperature from the file
				print ("set temps " + preset)

			dialogConf.destroy()										#destroy confirm window

		dialog.destroy()											#destroy selection window

#create confirm window

class ConfirmTemps(Gtk.Dialog):
	def __init__(self, parent):											#create confirm window
		Gtk.Dialog.__init__(											#add title
			self,
			"Preset",
			parent,
			0,
			(
				Gtk.STOCK_CANCEL,									#add buttons: Ok and Cancel
				Gtk.ResponseType.CANCEL,
				Gtk.STOCK_OK,
				Gtk.ResponseType.OK,
			),
		)

		self.set_default_size(150, 100)										#set window size
		label = Gtk.Label("Those temperatures will be loaded: \n" + preset + " \n")				#show loaded temps

		box= self.get_content_area()
		box.add(label)
		self.show_all()												#show window, labels and buttons

#end create confirm window


#end of definition for functions called when button pressed
#==========================================================================================
#open window

window = asuswindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

#close window
#==========================================================================================
