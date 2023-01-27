import os
print('''
░██████╗░█████╗░  ███████╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░
██╔════╝██╔══██╗  ██╔════╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝  █████╗░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
░╚═══██╗██║░░██╗  ██╔══╝░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝  ██║░░░░░██║███████╗███████╗███████╗██║░░██║
╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝''')
print('Running SC Filler Release 1.0')
valid = False
path = "main.py"
while valid == False:
    number = input('How many bots would you like to send into SC?')
    try:
        number = int(number)
        valid = True
    except:
        print('invalid input, please try again')
for i in range(0,number):
    os.popen(path)