#Imports
import argparse
import subprocess
import pipall.pipallBackground

from os import path
from tempfile import TemporaryFile
from PyTermColor.Color import printColor as printc






#Parser Declaration
pipallParser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
pipallSubParser = pipallParser.add_subparsers(dest = 'command')

installParser = pipallSubParser.add_parser('install')
uninstallParser = pipallSubParser.add_parser('uninstall')
updateParser = pipallSubParser.add_parser('update')


installParser.add_argument('-p', '--packages', help = 'List of packages separated by "," to install.')
installParser.add_argument('-f', '--file', help = 'File referencing a list of packages to be installed.')

uninstallParser.add_argument('-p', '--packages', help = 'List of packages separated by "," to uninstall.')
uninstallParser.add_argument('-f', '--file', help = 'File referencing a list of packages to be uninstalled.')
uninstallParser.add_argument('-o', '--outdated', help = 'Uninstalls all outdated packages.', action='store_true')
uninstallParser.add_argument('-a', '--all', help = 'Uninstalls all packages (except for a select few).', action='store_true')

updateParser.add_argument('-p', '--packages', help = 'List of packages separated by "," to update.')
updateParser.add_argument('-f', '--file', help = 'File referencing a list of packages to be updated.')
updateParser.add_argument('-o', '--outdated', help = 'Updates all outdated packages.', action='store_true')
updateParser.add_argument('-a', '--all', help = 'Updates all packages.', action='store_true')










#Global Variables
pipallBackgroundPath = path.abspath(pipall.pipallBackground.__file__)






#Extra Functions
def pri(x: int = 1):
    print('\n' * x)



def clearLine(): print('\x1b[1A\x1b[2K\x1b[1A')



def Error(errorType: str, value: str):
    print('\n')
    printc(errorType, 'red', end = ': ')
    printc(value, 'lightyellow')
    quit()



def CollectPackages(argument: str = None) -> list:
    command = ['pip', 'list']
    if argument: command.append(argument)

    loadingProcess = subprocess.Popen(['python', pipallBackgroundPath, 'Collecting Packages...   '])
    with TemporaryFile() as Packages:
        searchProcess = subprocess.Popen(command, stdout = Packages)
        searchProcess.wait()
        Packages.seek(0)
        Packages = [package.split(' ')[0] for package in Packages.read().decode().split('\n')[2:]][:-1]
    
    loadingProcess.kill()
    clearLine()
    print('Collecting Packages ', end = '')
    if len(Packages) == 0: 
        printc('✗', 'red')
        Error('RuntimeError', 'No Packages have been found.')
    printc('✓', 'green')
    
    return Packages



def ParsePackagesFile(filePath: str) -> list:
    try:
        with open(filePath, 'r', errors = 'ignore') as f: Packages = [line.strip() for line in f.readlines()]
    except Exception as exception: Error('FileError', 'Could not Parse File.\n' + str(exception))
    return Packages



def ParsePackagesString(packageString: str) -> list:
    try: Packages = packageString.replace(' ','').split(',')
    except Exception as exception: Error('RuntimeError', 'Could not Parse Packages.\n' + str(exception))
    return Packages


    





#Install Command
def Install(argument: str, value: str):
    match argument:
        case 'packages':
            try: Packages = value.replace(' ','').split(',')
            except KeyboardInterrupt: raise KeyboardInterrupt
            except Exception as exception: Error('RuntimeError', 'Could not Parse Packages.\n' + str(exception))
        case 'file': Packages = ParsePackagesFile(value)

    
    success = 0
    pri()
    print('Installing Packages:')
    try:
        for package in Packages:
            loadingProcess = subprocess.Popen(['python', pipallBackgroundPath, '   - {}...   '.format(package)])

            try:
                uninstallProcess = subprocess.Popen(['pip', 'install', package, '-q'])
                uninstallProcess.wait()
                loadingProcess.kill()
                finish = ('✓', 'green')
            except: finish = ('✗', 'red')
        
            success += {('✓', 'green') : 1, ('✗', 'red') : 0}[finish]
            loadingProcess.kill()
            clearLine()
            print('   - {} '.format(package), end='')
            printc(*finish)
    
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: Error('RuntimeError', 'Could not Install Packages.\n' + str(exception))

    pri()
    print('Successfully Uninstalled {}/{} Packages.'.format(str(success), str(len(Packages))))






#Uninstall Command
def Uninstall(argument: str, value: str):
    def subuninstall(package):
        try:
            uninstallProcess = subprocess.Popen(['pip', 'uninstall', '-y', package, '-q'])
            uninstallProcess.wait()
            return True
        except: return False


    match argument:
        case 'packages':
            InstalledPackages = CollectPackages()
            Packages = ParsePackagesString(value)
        case 'file': Packages = ParsePackagesFile(value)
        case 'outdated' : Packages = CollectPackages('--outdated')
        case 'all': Packages = CollectPackages()
    
    success = 0
    
    ExclusionList = ['pip', 'setuptools', 'idev-pytermcolor', 'idev-pipall']
    try:
        for package in ExclusionList: Packages.pop(package)
    except: pass

    pri()
    print('Uninstalling Packages:')
    try:
        for package in Packages:
            loadingProcess = subprocess.Popen(['python', pipallBackgroundPath, '   - {}...   '.format(package)])

            match argument:
                case 'outdated' | 'all': finish = {True : ('✓', 'green'), False : ('✗', 'red')}[subuninstall(package)]
                case _:
                    if package in InstalledPackages: finish = {True : ('✓', 'green'), False : ('✗', 'red')}[subuninstall(package)]
                    else:
                        print()
                        finish = ('✗', 'red')
        
            success += {('✓', 'green') : 1, ('✗', 'red') : 0}[finish]
            loadingProcess.kill()
            clearLine()
            print('   - {} '.format(package), end='')
            printc(*finish)
    
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: Error('RuntimeError', 'Could not Uninstall Packages.\n' + str(exception))

    pri()
    print('Successfully Uninstalled {}/{} Packages.'.format(str(success), str(len(Packages))))
    if argument == 'all': Error('Warning', 'This package along with the dependency "idev-pytermcolor" was not uninstalled.\nIf you wish to uninstall them, you must use "pip uninstall idev-pipall && pip uninstall idev-pytermcolor')








#Update Command
def Update(argument: str, value: str):
    def subupdate(package):
        try:
            updateProcess = subprocess.Popen(['pip', 'install', package, '-U', '-q'])
            updateProcess.wait()
            return True
        except: return False


    match argument:
        case 'packages':
            InstalledPackages = CollectPackages()
            Packages = ParsePackagesString(value)
        case 'file': Packages = ParsePackagesFile(value)
        case 'outdated': Packages = CollectPackages('--outdated')
        case 'all': Packages = CollectPackages()
    
    success = 0
    Packages.pop('pip')

    pri()
    try:
        for package in Packages:
            loadingProcess = subprocess.Popen(['python', pipallBackgroundPath, '   - {}...   '.format(package)])

            match argument:
                case 'outdated' | 'all': finish = {True : ('✓', 'green'), False : ('✗', 'red')}[subupdate(package)]
                case _:
                    if package in InstalledPackages: finish = {True : ('✓', 'green'), False : ('✗', 'red')}[subupdate(package)]
                    else:
                        print()
                        finish = ('✗', 'red')
            
            success += {('✓', 'green') : 1, ('✗', 'red') : 0}[finish]
            loadingProcess.kill()
            clearLine()
            print('   - {} '.format(package), end='')
            printc(*finish)
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: Error('RuntimeError', 'Could not Update Packages.\n' + str(exception))

    pri()
    print('Successfully Updated {}/{} Packages.'.format(str(success), str(len(Packages))))










#Main Function
def Main():
    arguments = vars(pipallParser.parse_args())
    arguments = {argument : arguments[argument] for argument in arguments if arguments[argument]}

    if arguments:
        command = arguments['command']
        arguments.pop('command')
        if len(arguments) > 1: Error('ArgumentError', 'Too many arguments have been passed.\n' + ','.join([argument for argument in arguments]))
    
        argument = list(arguments.keys())[0]
        value = arguments[argument]

        match command:
            case 'update': Update(argument, value)
            case 'install': Install(argument, value)
            case 'uninstall': Uninstall(argument, value)
            case _: pass






if __name__ == '__main__': Main()