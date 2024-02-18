# **pipall**
A [**python**](https://www.python.org) script for executing **pip** commands across many or all packages.
<br />
<br />
<br />
<br />
​<br />
# Installation
With `git` [GitHub](https://github.com):
```
git clone https://github.com/IrtsaDevelopment/pipall.git
```
With `pip` [PyPi](https://pypi.org/project/idev-pipall/)
```
pip install idev-pipall
```
<br />
<br />
<br />
<br />
<br />
<br />

# Usage
<br />
<br />

### Within the CMD/Terminal
If installed with **GIT**:
```
python pipall.py [-h] {install,uninstall,update} ...
```
If installed with **PIP**:
```
pipall [-h] {install,uninstall,update} ...
```
<br />

Utilize `-h` or `--help` parameter for additional help.
```
usage: pipall [-h] {install,uninstall,update} ...

positional arguments:
  {install,uninstall,update}

options:
  -h, --help            show this help message and exit
```
```
usage: pipall install [-h] [-p PACKAGES] [-f FILE]

options:
  -h, --help            show this help message and exit
  -p PACKAGES, --packages PACKAGES
                        List of packages separated by "," to install.
  -f FILE, --file FILE  File referencing a list of packages to be installed.
```
```
usage: pipall uninstall [-h] [-p PACKAGES] [-f FILE] [-o] [-a]

options:
  -h, --help            show this help message and exit
  -p PACKAGES, --packages PACKAGES
                        List of packages separated by "," to uninstall.
  -f FILE, --file FILE  File referencing a list of packages to be uninstalled.
  -o, --outdated        Uninstalls all outdated packages.
  -a, --all             Uninstalls all packages (except for a select few).
```
```
usage: pipall.py update [-h] [-p PACKAGES] [-f FILE] [-o] [-a]

options:
  -h, --help            show this help message and exit
  -p PACKAGES, --packages PACKAGES
                        List of packages separated by "," to update.
  -f FILE, --file FILE  File referencing a list of packages to be updated.
  -o, --outdated        Updates all outdated packages.
  -a, --all             Updates all packages.
```
<br />
<br />
<br />
<br />
<br />
<br />

# Examples
```
pipall install -p idev-pytermcolor,idev-steganopy

- Will attempt to install all packages provided.
```
```
pipall uninstall -f uninstallpackages.txt

- Will attempt to uninstall all packages provided in the text file.
```
```
pipall update -a

- Will attempt to update all packages you currently have installed.
```
```
pipall update -o

- Will attempt to update all outdated packages you currentl have installed.
```