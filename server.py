import socket
import threading
import time
import asyncio

hostname= socket.gethostname()
host =socket.gethostbyname(hostname)
port = 8000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host, port))
s.listen()
conn, addr = s.accept()
#Üzenet küldés
def messaging():
    message=input(">>")
    while message.lower().strip()!="quit":
        conn.send(message.encode())
        message=input(">>")
    conn.close()

with conn:
    print(f"Connected by {addr} + conn:{conn}")
    thread_server_message=threading.Thread(target=messaging)
    thread_server_message.daemon=True
    thread_server_message.start()
    while True:
        data=conn.recv(1024).decode()
        if(data):
            print("got data!")
        print(data)
        print(">>")
        
            

