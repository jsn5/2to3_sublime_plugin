import sublime,sublime_plugin
import subprocess
class ConvertPythonCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):
		lang = self.view.settings().get('syntax')
		if not 'python' in lang.lower():
			return()
	
		self.view.run_command('save')
		path = self.view.file_name()
		#execute 2to3
		PIPE = subprocess.PIPE
		p = subprocess.Popen(['2to3', '-w', path], stdout=PIPE, stderr=PIPE)
		p.wait()
		out, err = p.communicate()
