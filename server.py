import sqlite3
import hashlib
import socket
import threading
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Server Started")
print(ascii_banner)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()


def handle_conncetion(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()
    conn = sqlite3.connect("../userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("1".encode())
        print("Login sucess")


    else:
        c.send("0".encode())


while True:
    client, addr = server.accept()
    threading.Thread(target=handle_conncetion, args=(client,)).start()
