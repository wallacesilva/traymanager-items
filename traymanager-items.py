#!/usr/bin/env python

# found on <http://files.majorsilence.com/rubbish/pygtk-book/pygtk-notebook-html/pygtk-notebook-latest.html#SECTION00430000000000000000>
# simple example of a tray icon application using PyGTK

import gtk
import subprocess
from subprocess import call

DEBUG = True

def message(data=None):
    "Function to display messages to the user."
  
    msg=gtk.MessageDialog(None, gtk.DIALOG_MODAL,
        gtk.MESSAGE_INFO, gtk.BUTTONS_OK, data)
    msg.run()
    msg.destroy()

def exec_comm(cmd):
    msg_return = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    if DEBUG:
        print msg_return
    return msg_return

def apache_start(data=None):
    # call(["gksudo", "service apache2 start"])
    message(exec_comm("gksudo service apache2 start"))

def apache_stop(data=None):
    # call(["gksudo", "service apache2 stop"])
    message(exec_comm("gksudo service apache2 stop"))

def mysql_start(data=None):
    # call(["gksudo", "service mysql start"])
    message(exec_comm("gksudo service mysql start"))

def mysql_stop(data=None):
    # call(["gksudo", "service mysql stop"])
    message(exec_comm("gksudo service mysql stop"))

def mega_start(data=None):
    exec_comm("exec megasync &")

def mega_stop(data=None):
    exec_comm("exec killall megasync &")

def open_app(data=None):
    message(data)
 
def close_app(data=None):
    # message(data)
    dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,
                                   gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO,
                                   "Quit application?")
    dialog.set_title("Confirmation")

    response = dialog.run()
    dialog.destroy()

    if response == gtk.RESPONSE_YES:
        gtk.main_quit()
        return False # returning False makes "destroy-event" be signalled
                     # for the window.
    else:
        return True # returning True avoids it to signal "destroy-event"
    gtk.main_quit()
 
def make_menu(event_button, event_time, data=None):
    menu = gtk.Menu()
    # open_item = gtk.MenuItem("Open App")
    apache_start_item = gtk.MenuItem("Start Apache2")
    apache_stop_item = gtk.MenuItem("Stop Apache2")
    mysql_start_item = gtk.MenuItem("Start Mysql")
    mysql_stop_item = gtk.MenuItem("Stop Mysql")
    megasync_start_item = gtk.MenuItem("Start Megasync")
    megasync_stop_item = gtk.MenuItem("Stop Megasync")
    close_item = gtk.MenuItem("Close")
  
    #Append the menu items  
    # menu.append(open_item)
    menu.append(apache_start_item)
    menu.append(apache_stop_item)
    menu.append(mysql_start_item)
    menu.append(mysql_stop_item)
    menu.append(megasync_start_item)
    menu.append(megasync_stop_item)
    menu.append(close_item)
    
    #add callbacks
    # open_item.connect_object("activate", open_app, "Open App")
    apache_start_item.connect_object("activate", apache_start, "Start Apache2 Service")
    apache_stop_item.connect_object("activate", apache_stop, "Stop Apache2 Service")
    mysql_start_item.connect_object("activate", mysql_start, "Start Mysql Service")
    mysql_stop_item.connect_object("activate", mysql_stop, "Stop Mysql Service")
    megasync_start_item.connect_object("activate", mega_start, "Start Megasync")
    megasync_stop_item.connect_object("activate", mega_stop, "Stop Megasync")
    close_item.connect_object("activate", close_app, "Close App")

    #Show the menu items
    # open_item.show()
    apache_start_item.show()
    apache_stop_item.show()
    mysql_start_item.show()
    mysql_stop_item.show()
    megasync_start_item.show();
    megasync_stop_item.show();
    close_item.show()
  
    #Popup the menu
    menu.popup(None, None, None, event_button, event_time)
 
def on_right_click(data, event_button, event_time):
    make_menu(event_button, event_time)
 
def on_left_click(event):
    message("Welcome to TrayManager Services Manager")

if __name__ == '__main__':
    icon = gtk.status_icon_new_from_stock(gtk.STOCK_ABOUT)
    icon.connect('popup-menu', on_right_click)
    icon.connect('activate', on_left_click)
    gtk.main()
