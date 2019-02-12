# keys.py
# keys is a collection of functions to help 'not hardcode' your password
# especially important in a server environment with multiple users
#
# this module assumes that the user already has a protected system that
# already protects any forced entry to their local machine and hence config
# files are saved on the local machine
#
# 1. Select encryption methods and saving it on a configuration file
# 2. Find ways to decrypt saved variables (not limited to passwords)

from Crypto.Cipher import AES


def encrypt_text(password):
    obj = AES.new('a$j*$%!GEer9#45%', AES.MODE_CFB, 'o%r_#D&JD^%DHKds')
    ciphertext = obj.encrypt(password)
    return ciphertext


def decrypt_text(encrypted_password):
    obj2 = AES.new('a$j*$%!GEer9#45%', AES.MODE_CFB, 'o%r_#D&JD^%DHKds')
    password = obj2.decrypt(encrypted_password)
    return password


def setup_encryption(varname:str, homedir:str = "~"):
    value_prompt = """
    Please enter the plain text to be protected: 
    """
    ciphertext = encrypt_text(input(value_prompt))

    # define path where config file is stored
    import os
    os.chdir(os.path.expanduser(homedir))

    # defining config name and content
    config_name = "axtoolbox_"+varname+".config"

    # writing configuration
    f = open(config_name,"w+")
    f.write(str(ciphertext))
    f.close()

    # indicate the file has been written
    print(config_name + ' successfully obscured.')
    return None;


def get_decryption(varname:str, homedir:str = "~"):
    # define path where config file is stored
    import os
    os.chdir(os.path.expanduser(homedir))

    # defining config name and content
    config_name = "axtoolbox_" + varname + ".config"

    # writing configuration
    f = open(config_name, "r")
    line = f.read()
    password = decrypt_text(line)
    f.close()
    return password;
