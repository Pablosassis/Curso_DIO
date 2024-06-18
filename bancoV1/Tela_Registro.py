from tkinter import Tk,Entry,Label,Button

def Tela_Registro():
    TelaRegistro = Tk()
    LabelCpf = Label(TelaRegistro, text="CPF:")
    LabelCpf.pack()
    EntryCpf = Entry(TelaRegistro)
    EntryCpf.pack()
    LabelUsuario = Label(TelaRegistro, text="Username:")
    LabelUsuario.pack()
    EntryUsuario = Entry(TelaRegistro)
    EntryUsuario.pack()
    LabelPassword = Label(TelaRegistro, text="Password:")
    LabelPassword.pack()
    EntryPassword = Entry(TelaRegistro, show="*")
    EntryPassword.pack()
    LabelPassword2 = Label(TelaRegistro, text="Confirm Password")
    LabelPassword2.pack()
    EntryPassword2 = Entry(TelaRegistro, show="*")
    EntryPassword2.pack()
    BotaoConfirmar = Button(TelaRegistro, text="Confirm")
    BotaoConfirmar.pack()
    TelaRegistro.mainloop()
    