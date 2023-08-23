#!/usr/bin/env python

import gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
import os

class OpenTerminator(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        self.file_names = []


    def menu_activate_cb(self, menu, file):
        """Called when the user selects the menu."""
        try:
            path = file.get_location().get_path()
            os.system("terminator --working-directory='{0}'".format(path))
        except AttributeError: # it is a list of elements
            dir_list = [f.get_location().get_path() for f in file if f.is_directory()]
            os.system("terminator --command='echo -e \"Something went wrong. Send an issue on git with what you attempted\nPath = {0}\" && bash || bash'".format(dir_list[0]))


    def define_menu_helper(self, name, window, file):
        item = Nautilus.MenuItem(name="OpenTerminator::" + name,
                                 label="Open in Terminator" ,
                                 tip="Opens current directory in terminator",
                                 icon="nautilus-terminator")
        item.connect('activate', self.menu_activate_cb, file)
        return item,

    def get_background_items(self, window, file):
        return self.define_menu_helper("Background", window, file)
