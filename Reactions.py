#!/usr/bin/python2.7
# coding: utf-8
import os
import gtk
import pynotify
import appindicator

__author__ = "TiagoDanin"
__contact__ = "tiagojdanin@outlook.com"
__copyright__ = "(c) 2016 TiagoDanin"
__license__ = "GPLv3" #View in https://github.com/TiagoDanin/Indicator-Reactions/blob/master/LICENSE

class main_indicator:
	def __init__(self):
		self.ind = appindicator.Indicator ("Indicator-Reactions",
											"Indicator-Reactions",
											appindicator.CATEGORY_APPLICATION_STATUS)
		self.ind.set_status(appindicator.STATUS_ACTIVE)
		self.ind.set_label("Reactions")

		self.menu = gtk.Menu()
		self.menu_list()

		self.about = gtk.MenuItem("About")
		self.menu.append(self.about)
		self.about.connect("activate", self.about_view)
		self.about.show()

		self.exit = gtk.MenuItem("Exit")
		self.menu.append(self.exit)
		self.exit.connect("activate", self.exit_fun)
		self.exit.show()

		self.ind.set_menu(self.menu)

	def menu_list(self):
		table = {}
		table['( ﾟヮﾟ)'] = "( ﾟヮﾟ)"
		table['(⌐■_■)'] = " (⌐■_■)"
		table['¯\_(ツ)_/¯'] = "¯\_(ツ)_/¯"
		table['( ͡° ͜ʖ ͡°)'] = "( ͡° ͜ʖ ͡°)"
		table['つ ◕_◕ ༽つ'] = "つ ◕_◕ ༽つ"
		table['┌（┌ ＾o＾）┐'] = "┌（┌ ＾o＾）┐"
		table['┬──┬◡ﾉ(° -°ﾉ)'] = "┬──┬◡ﾉ(° -°ﾉ)"
		table['(╯°□°）╯︵ ┻━┻'] = "(╯°□°）╯︵ ┻━┻"
		for v in table:
			self.v = gtk.MenuItem(v)
			self.menu.append(self.v)
			self.v.connect("activate", self.clip, table[v])
			self.v.show()

	def clip(self, _, data):
		clipboard = gtk.clipboard_get()
		clipboard.set_text(str(data))
		clipboard.store()
		self.notif()

	def notif(self):
		pynotify.init(">-<")
		self.tit = 'Copied!'
		self.body = 'Copied to Clipboard (Use Ctrl + V)'
		new_notif = pynotify.Notification(self.tit, self.body)
		new_notif.show()

	def about_view(self, _):
		about_ = gtk.AboutDialog()
		about_ .set_name("Indicator-Reactions")
		about_ .set_version("0.1")
		about_ .set_comments("Simple indicator with Reactions ¯ \ _ (ツ) _/¯")
		about_ .set_website("https://TiagoDanin.github.io/Indicator-Reactions")
		about_ .set_website_label("Website")
		about_ .set_authors(["TiagoDanin"])

		about_ .run()
		about_ .destroy()

	def exit_fun(self, _):
		exit(0)

def main():
	main_indicator()
	gtk.main()
	exit(0)

if __name__ == "__main__":
	main()
