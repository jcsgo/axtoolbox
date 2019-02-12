# Insert your code here. 

def update():
	"""Updates axtoolbox to the latest version on the python command line."""
	import os
	os.system('pip install --upgrade git+git://github.com/jcsgo/axtoolbox.git')


def setup_encryption(varname:str, homedir:str="~"):
	encryption_prompt = """
	Please select encryption type:
	1 - AES
	2 - Base64
	"""
	encryption_method = input(encryption_prompt)

	key_prompt = """
	For added security, we require a key of any digit to
	increase the security of your password
	"""
	key = input(key_prompt)

	print('Your encryption method selected is: ', encryption_method)
	print('Your key is: ', key)

	import os
	os.chdir(os.path.expanduser(homedir))
	path = os.getcwd() 
	f= open("axtoolbox.config","w+")
	f.write(varname+' '+encryption_method+' '+key)
	f.close()

	return None;

