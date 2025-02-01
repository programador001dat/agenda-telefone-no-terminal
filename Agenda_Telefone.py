import os
import pyfiglet
import time

x = pyfiglet.figlet_format("TO ADD", font="digital")
y = pyfiglet.figlet_format("VIEW CONTACT", font="digital")
w = pyfiglet.figlet_format("MENU AGENDA",font="digital")




os.system("clear")

class Android_telefone:

    def __init__(self, initial):

        self.initial = initial
        print(initial)

    def Code_contact(**kwargs):

        print("\t.........")
        print("\t| ..... |")
        print("\t| .   . |]\tAgenda para programadores.")
        print("\t| ..... |]\tLinguagem Python3.")
        print("\t|_______|")
        print("\t| 3 2 1 |")
        print("\t| 4 5 6 |")
        print("\t| 7 8 9 |")
        print("\t|   0   |")
        print("\t|.......|")

        kwargs = {
            "caio":"18997433857",
            "email":"programador001dat@hotmail.com"
              }
        print("\n")
        for i,r in kwargs.items():
            print("\t{} {}".format(i, r))
            pass
        print("...........................................")

    def Code_add():

        new_contact = str(input("[+]nome completo: "))
        telephone = int(input("[+]celular\\telefone: "))
        email = str(input("[+]digite o email: "))
        string = str(input("[+]marcar algum evento: "))

        x = open("new_contact.txt", "a")
        x.write(f"Nome:{new_contact}\tTelefone:{telephone}\tE-mail:{email}\nEvento:{string}\n\n...........................................\n")
        print("==> savedata.")
        time.sleep(3)

    def Code_View():

        try:
            x = open("new_contact.txt","r")
            return print(x.read())
            x.close()
            print("\n\n")

        except:
            print(">>nenhum contato...\n\n")

    def Code_Menu():

        while True:



            print(w)
            print("[1]add new contact.")
            print("[2]view contact.")
            code = input("#: ")

            if(code == "1"):
                os.system("clear")
                print(x)
                Codigo_dev.Code_add()

            elif(code == "2"):
                os.system("clear")
                print(y)
                Codigo_dev.Code_View()

            else:
                quit()


Codigo_dev = Android_telefone

Codigo_dev(initial="[+]Android v1.0 AGENDA")

Codigo_dev.Code_contact()

Codigo_dev.Code_Menu()
