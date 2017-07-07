import sublime
import sublime_plugin
import os
class ConvertPythonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.file_name() == None:
			sublime.error_message("Save the file first to perform the conversion.\n")
		else:
			self.view.run_command('save')
			os.system("python 2to3.py -w "+self.view.file_name())
			
