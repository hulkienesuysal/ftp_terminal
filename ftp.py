from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
from socket import gethostbyname
from os import getcwd
from time import sleep

print("Geliştirici: @D1STANG3R\n")

print("""----------------FTP (FILE TRANSFER PROTOKOL)----------------
    INFO: Ftp'ye username ve password tanımlamak için aşağıdaki yerleri doldurunuz. 
    INFO: Ftp'yi herkese açmak için 'enter' tuşuna basıp, username ve password bölümünü boş bırakınız.
""")

username=str(input("Username: "))
password=str(input("Password: "))

authorizer = DummyAuthorizer()

if username=="" and password=="":
    def guest():
        print("""
    INFO: Sadece dosya okuma modu için '1' i
    INFO: Tam yetki (Okuma,Yazma,Silme,Değiştirme) için '2' yi tuşlayınız...
        """)
        mode=str(input("Choise: "))
        if mode=="1":
            authorizer.add_anonymous(getcwd(), perm="elr")
        elif mode=="2":
            authorizer.add_anonymous(getcwd(), perm="elradfmwMT")
        else:
            print("Choice Wrong! Try Again")
            sleep(2)
            guest()
    guest()

else:
    def user():
        print("""
    INFO: Sadece dosya okuma modu için '1' i
    INFO: Tam yetki (Okuma,Yazma,Silme,Değiştirme) için '2' yi tuşlayınız...
            """)
        mode=str(input("Choise: "))
        if mode=="1":
            authorizer.add_user(username, password, getcwd(), perm="elr")
        elif mode=="2":
            authorizer.add_user(username, password, getcwd(), perm="elradfmwMT")
        else:
            print("Choice Wrong! Try Again")
            sleep(2)
            user()
    user()

print("\nShared Folder: {}".format(getcwd()))
print("FTP connect adress: ftp://{}:21\n".format(gethostbyname(socket.gethostname())))

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((gethostbyname(socket.gethostname()), 21), handler)
server.serve_forever()
