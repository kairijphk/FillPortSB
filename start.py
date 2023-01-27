import os
print('''
░██████╗░█████╗░  ███████╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░
██╔════╝██╔══██╗  ██╔════╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝  █████╗░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
░╚═══██╗██║░░██╗  ██╔══╝░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝  ██║░░░░░██║███████╗███████╗███████╗██║░░██║
╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝''')
valid = False
while valid == False:
    number = input('How many bots would you like to send into SC?')
    try:
        number = int(number) - 1
        valid = True
    except:
        print('invalid input, please try again')
for i in range(0,number):
    os.system('main.py')
