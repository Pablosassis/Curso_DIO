import os
from tinydb import TinyDB,Query,where
#Variáveis
escolhas=0
Total = 0
extrato = []
Limite = 500
Cpf = 0
Username = ""
Password = ""
conta = 0
db = TinyDB("db.json")
dbQuery = Query()

#Classes
class Banco():
    def saque(self, valorDeSaque):
        global Total
        global Limite
        if Total <= 0 or Total - valorDeSaque < 0:
            return "Não possui dinheiro em conta"
        elif Limite - valorDeSaque < 0:
            return "Você chegou ao limite de saque"
        else:
            extrato.append(valorDeSaque*-1)
            Total -= valorDeSaque
            Limite -=valorDeSaque
            return f"Você sacou R$ {valorDeSaque}"
    def deposito(self, valorDeDeposito):
        if valorDeDeposito > 0:
            extrato.append(valorDeDeposito)
            global Total
            Total += valorDeDeposito
            return f"Valor R$ {valorDeDeposito} foi depositado"
        else:
            return "Não é possível depositar R$0 ou menos"
    def arrumarextrato(self):
        global Total
        i = 0
        ArrumarExtrato = extrato.copy()
        for i in range(len(ArrumarExtrato)):
            preco = "R$"
            if preco in str(ArrumarExtrato[i]):
                pass
            else:
                ArrumarExtrato.insert(i,"R$ " + str(ArrumarExtrato[i]))
                ArrumarExtrato.pop(i+1)         
        print(f"Extrato da conta(positivos depósito e negativos saques) {ArrumarExtrato}")
        return f"Total em conta: R${Total}"
    def criar_usuario(self, Cpf, Username, Password):
        global db
        global dbQuery
        if Cpf in db.search(dbQuery.CPF == Cpf):
            return print("CPF Already in use")
        elif Username in db.search(dbQuery.USERNAME == Username):
            return "Username Already in use"
        else:
            db.insert({"CPF": Cpf, "USERNAME": Username, "PASSWORD": Password})
            pass

# while True:
#     try:
#         escolhas = int(input("1.Depósito\n2.Saque\n3.Extrato\n4.Criar Conta\n5.Sair\n"))
#         match escolhas:
#             case 1:
#                 try:
#                     valorDeDeposito = float(input("Qual valor deseja depositar?\n"))
#                     Banco().deposito(valorDeDeposito)
#                 except ValueError:
#                     print("Somente números\n")
#             case 2:
#                 try:
#                     valorDeSaque = float(input("Qual valor deseja sacar?\n"))
#                     Banco().saque(valorDeSaque)
#                 except ValueError:
#                     print("Somente números\n")
#             case 3:
#                 Banco().arrumarextrato()
#             case 4:
#                 try:
#                     CpfCadastro = int(input("Qual Cpf deseja cadastrar?\n"))
#                     Banco().criar_usuario(CpfCadastro)
#                 except ValueError:
#                     print("Somente números\n")
#             case 5:
#                 quit("tchau")
#             case _:
#                 print("Só números de 1 a 5\n")
#     except ValueError:
#         print("Somente numeros de 1 a 5\n")