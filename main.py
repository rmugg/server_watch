#!/usr/bin/env python3
import os
import signal
import string
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import AppIndicator3
from gi.repository import Notify
from gi.repository import GObject
from configparser import ConfigParser
from pathlib import Path

server_checker = None
loaded_connections = []
parser = ConfigParser()

parser.read(os.path.abspath(__file__ + "/../settings.ini")) 
active_connection = int(parser.get('connections','default-connection'))

APPINDICATOR_ID = "server_watch"





#function definitions_____________________________________________________________________________________________________
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




def load_config():
	try:
		ip    = parser.get('connections',('ip-#').replace('#',str(len(loaded_connections))))
		mac   = parser.get('connections',('mac-#').replace('#',str(len(loaded_connections))))
		label = parser.get('connections',('label-#').replace('#',str(len(loaded_connections))))
		user  = parser.get('connections',('user-#').replace('#',str(len(loaded_connections))))
		
		loaded_connections.append({'ip':ip,
								   'mac':mac,
								   'label':label,
								   'user':user})
		load_config()
	except:
		
		print('\n-----------config has been loaded!-----------\n')
		print(loaded_connections)
		print('\n-----------  Connection amount:' + str(len(loaded_connections)) + '   -----------\n')
		



def check_server(active_connection):
	response = os.system('ping -c 1 ' + loaded_connections[active_connection]['ip'])
	if response == 0:
		indicator.set_icon(os.path.abspath(__file__ + "/../icons/active.png"))
		return "server up :)"
	else:
		indicator.set_icon(os.path.abspath(__file__ + "/../icons/inactive.png"))
		return "server down :(" 



def wake_server(event="none"):
	global active_connection
	mac = loaded_connections[active_connection]['mac']
	os.system(f'wakeonlan {mac}')



def open_terminal(source):
	global active_connection
	ip   = loaded_connections[active_connection]['ip']
	user = loaded_connections[active_connection]['user']
	os.system( (f"gnome-terminal --command 'ssh {user}@{ip}'"))
	

def next_connection(source):
	global server_checker
	global active_connection

	active_connection+=1
	if active_connection > len(loaded_connections) - 1:
		active_connection = 0;

	indicator.set_menu(menu_build(loaded_connections[active_connection])) #calls build function to add buttons
	indicator.set_label(loaded_connections[active_connection]['label'], "8")
	indicator.set_icon(os.path.abspath(__file__ + "/../icons/try.png"))

	#remove server_check from main loop and add the new connection server_check
	GObject.source_remove(server_checker)
	server_checker = GObject.timeout_add(7000, check_server, active_connection)



def quit(source):
	Notify.uninit()
	Gtk.main_quit()



def menu_build(connection):
	menu = Gtk.Menu()
	if connection['ip']:
		#open terminal
		item_terminal = Gtk.MenuItem(label="Open Terminal")
		item_terminal.connect('activate', open_terminal)
		menu.append(item_terminal)
		#refresh connection
		item_refresh = Gtk.MenuItem(label="Refresh") 
		item_refresh.connect('activate', check_server)
		menu.append(item_refresh)
	
	if connection['mac']:
		#wake server
		item_wake = Gtk.MenuItem(label="Wake")
		item_wake.connect('activate', wake_server)
		menu.append(item_wake)
	
	if len(loaded_connections) > 1:
		#next connection
		item_next = Gtk.MenuItem(label="Next")
		item_next.connect('activate', next_connection)
		menu.append(item_next)

	#quit script
	item_quit = Gtk.MenuItem(label="Quit")
	item_quit.connect('activate', quit)
	menu.append(item_quit)

	#show and return menu
	menu.show_all()										
	return menu



def main():	
	global server_checker
	load_config()

	indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
	indicator.set_label(loaded_connections[active_connection]['label'], "2")
	indicator.set_menu(menu_build(loaded_connections[active_connection])) #calls build function to add buttons
	
	Notify.init(APPINDICATOR_ID) #
	server_checker = GObject.timeout_add(7000, check_server, active_connection) #adds check_server to the gtk main loop to be called every x Secs/1000ms
	Gtk.main()


indicator = AppIndicator3.Indicator.new(   #creation of gtk app indicator named  -> 'indicator'
			APPINDICATOR_ID,
			os.path.abspath(__file__ + "/../icons/try.png"),
			AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)


# main of script__________________________________________________________________________________________________________
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


if __name__ == "__main__": 
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()

