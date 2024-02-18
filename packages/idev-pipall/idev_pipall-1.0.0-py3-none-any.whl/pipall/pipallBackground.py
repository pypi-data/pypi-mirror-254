#Imports
import argparse

from time import sleep






#Parser Declaration
backgroundpars = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
backgroundpars.add_argument('text')






#Main Function
def Main():
    global backgroundpars

    loadingText = ['/', '-', '\\', '|']
    text = vars(backgroundpars.parse_args())['text']

    loading = 0
    while True:
        print(text, end = '')
        print(loadingText[loading % 4])
        sleep(0.2)
        print('\x1b[1A\x1b[2K\x1b[1A')
        loading += 1
        






if __name__ == '__main__': Main()    