# Insert your code here. 

def update():
	"""Updates axtoolbox to the latest version on the python command line."""
	import os
	os.system('pip install --upgrade git+git://github.com/jcsgo/axtoolbox.git')


def setup_encryption(varname:str, homedir:str="~"):
	"""Setups encryption settings and saves it in your local directory"""
	encryption_prompt = """
	Please select encryption type:
	1 - AES
	2 - Base64
	"""
	encryption_requirements = [1,2]
	encryption_method = input(encryption_prompt)
	# create error function to check if encryption is within requirement list:
	# encryption_requirements

	key_prompt = """
	For added security, we require a key of any digit to
	increase the security of your password
	"""
	key = input(key_prompt)
	# create error function to check if key does not contain spaces

	import os
	import re

	os.chdir(os.path.expanduser(homedir))
	path = os.getcwd()

	config_name = "axtoolbox_"+varname+".config"
	f= open(config_name,"w+")
	f.write(varname+' '+encryption_method+' '+key)
	f.close()

	return None;
	