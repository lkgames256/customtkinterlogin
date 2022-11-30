import customtkinter
import socket

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def register():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.178.100", 9990))

    message = client.recv(1024).decode()
    client.send(entery1.get().encode())
    message = client.recv(1024).decode()
    client.send(entery2.get().encode())
    print(client.recv(1024).decode())


def login():
    exit(0)


root = customtkinter.CTk()
root.geometry("500x450")
root.title("Register Screen")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Register", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entery1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entery1.pack(pady=12, padx=10)

entery2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entery2.pack(pady=12, padx=10)

entery2 = customtkinter.CTkEntry(master=frame, placeholder_text="Repeat Password", show="*")
entery2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Register", command=register)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me!")
checkbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login to Account", command=login)
button.pack(pady=22, padx=10)

root.mainloop()
