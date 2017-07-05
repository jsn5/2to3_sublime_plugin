import sublime
import sublime_plugin
import os
class ConvertPythonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("python 2to3.py -w "+self.view.file_name())
