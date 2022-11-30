import customtkinter
import socket
import hashlib

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login screen")


def register():
    print("Button Pressed!")
    exec(open("register.py").read())


def login():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    message = client.recv(1024).decode()
    client.send(entery1.get().encode())
    message = client.recv(1024).decode()
    client.send(entery2.get().encode())
    if client.recv(1024).decode() == "1":
        print("Dat hat Funktioniert!")

    else:
        print("Da war eine error")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entery1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entery1.pack(pady=12, padx=10)

entery2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entery2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me!")
checkbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Register new Account", command=register)
button.pack(pady=12, padx=10)

root.mainloop()
