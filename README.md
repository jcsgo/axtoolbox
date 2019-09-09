# axtoolbox
This is a toolbox specific for analytics usage in python. Several functions are written here to save some time. Specifically:

### Avoiding hardcoding passwords --> refer to `keys.py`
Instead of hardcoding username and passwords, you can now obscure them in your code. Username and password details will be encrypted and can be recalled using functions within keys.py.

### Installing and updating `axtoolbox`
To install, run:
```
pip install git+git://github.com/jcsgo/axtoolbox.git
```
To update, run:
```
pip install --upgrade git+git://github.com/jcsgo/axtoolbox.git
```
### Setting Up `axtoolbox` To Store Passwords
On your python console:
```
import axtoolbox as axt
axt.setup_encryption('example-username')
```
You will be asked to type in your password/or the text you want to store under this name

On your python console:
```
import axtoolbox as axt
axt.setup_encryption('example-username')
```
You will be asked to type in your password/or the text you want to store under this name.

### Using `axtoolbox` To Call Stored Passwords
After setup above and also on your python console:
```
import axtoolbox as axt
axt.get_decryption('example-username')
```
