from tkinter import Tk,Label,Button,Entry
from Tela_Principal import Tela_Principal
from Tela_Registro import Tela_Registro

def Tela_Inicial():
    TelaInicial = Tk()
    TelaInicial.geometry(newGeometry="800x600")
    TelaInicial.config()
    UserEntryLabel = Label(TelaInicial, text="Username:",bg="black",fg="white")
    UserEntryLabel.pack()
    UserEntry = Entry()
    UserEntry.pack()
    PassEntryLabel = Label(TelaInicial, text="Password:",bg="black",fg="white")
    PassEntryLabel.pack()
    PassEntry = Entry(TelaInicial, show="*")
    PassEntry.pack()
    BotaoLogin = Button(TelaInicial, text="Login", command=Tela_Principal)
    BotaoLogin.pack()
    BotaoRegistro = Button(TelaInicial, text="Register",command=Tela_Registro)
    BotaoRegistro.pack()
    TelaInicial.configure(background="black")
    TelaInicial.mainloop()
Tela_Inicial()