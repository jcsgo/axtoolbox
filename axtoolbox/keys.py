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
import os

def encrypt_text(password):
    obj = AES.new('a$j*$%!GEer9#45%', AES.MODE_CFB, 'o%r_#D&JD^%DHKds')
    ciphertext = obj.encrypt(password.encode('utf-8'))
    return ciphertext


def decrypt_text(encrypted_password):
    obj2 = AES.new('a$j*$%!GEer9#45%', AES.MODE_CFB, 'o%r_#D&JD^%DHKds')
    password = obj2.decrypt(encrypted_password)
    return password.decode('utf-8')


def setup_encryption(varname: str):
    cwd = os.getcwd()
    value_prompt = "Please enter your {varname}: ".format(varname=varname)
    ciphertext = encrypt_text(input(value_prompt))

    # define path where config file is stored
    path = os.path.join(os.path.expanduser('~'), 'axtoolbox')
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

    # defining config name and content
    config_name = "axtoolbox_"+varname+".config"

    # writing configuration
    f = open(config_name, "wb")
    f.write(ciphertext)
    f.close()

    # indicate the file has been written
    print(config_name + ' successfully obscured.')

    # return to original wd
    os.chdir(cwd)


def get_decryption(varname: str):
    cwd = os.getcwd()
    # define path where config file is stored
    path = os.path.join(os.path.expanduser('~'), 'axtoolbox')
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

    # defining config name and content
    config_name = "axtoolbox_" + varname + ".config"

    # writing configuration
    f = open(config_name, "rb")
    line = f.read()
    password = decrypt_text(line)
    f.close()
    return password

    # return to original wd
    os.chdir(cwd)
