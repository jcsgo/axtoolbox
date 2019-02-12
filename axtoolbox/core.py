# Insert your code here. 

def update():
	import os
	os.system('pip install --upgrade git+git://github.com/jcsgo/axtoolbox.git')


def setup_encryption(varname:str):
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

	return None;

