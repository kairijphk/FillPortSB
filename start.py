import os
import sys
import time as t
print('''
░██████╗░█████╗░  ███████╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░
██╔════╝██╔══██╗  ██╔════╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝  █████╗░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
░╚═══██╗██║░░██╗  ██╔══╝░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝  ██║░░░░░██║███████╗███████╗███████╗██║░░██║
╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝''')
print('Running SC Filler Release 1.0')
valid = False
path = os.path.join(os.path.dirname(__file__), 'main.py')
while valid == False:
    number = input('How many bots would you like to send into SC?')
    try:
        number = int(number)
        valid = True
    except:
        print('invalid input, please try again')
for i in range(0,number):
    t.sleep(0.1)
    os.popen(path)
