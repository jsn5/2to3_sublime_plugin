import sublime
import sublime_plugin
import os
class ConvertPythonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("sudo apt-get install 2to3")
		os.system("2to3 -w "+self.view.file_name())
