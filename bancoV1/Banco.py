#Variáveis
escolhas=0
Total = 0
extrato = []
Limite = 500
SemSaque = "Não possui dinheiro em conta"
ValorSacado = 0
#Classes
class Banco():
    def saque(self, valorDeSaque):
        global Total
        global Limite
        if Total <= 0 or Total - valorDeSaque < 0:
            print(f"{SemSaque}")
        elif Limite - valorDeSaque < 0:
            print("Você chegou ao limite de saque")
        else:
            print(f"Você sacou R$ {valorDeSaque}")
            extrato.append(valorDeSaque*-1)
            Total -= valorDeSaque
            Limite -=valorDeSaque
    def deposito(self, valorDeDeposito):
        if valorDeDeposito > 0:
            extrato.append(valorDeDeposito)
            global Total
            Total += valorDeDeposito
            print(f"Valor R$ {valorDeDeposito} foi depositado")
        else:
            print("Não é possível depositar R$0 ou menos")
    def arrumarextrato(self):
        global Total
        i = 0
        for i in range(len(extrato)):
            preco = "R$"
            if preco in str(extrato[i]):
                pass
            else:
                extrato.insert(i,"R$ " + str(extrato[i]))
                extrato.pop(i+1)         
        print(f"Extrato da conta(positivos depósito e negativos saques) {extrato}")
        print(f"Total em conta: R${Total}")

while escolhas==0:
    escolhas = int(input("1.Depósito\n2.Saque\n3.Extrato\n4.Sair\n"))
    match escolhas:
        case 1:
            valorDeDeposito = int(input("Qual valor deseja depositar?\n"))
            Banco().deposito(valorDeDeposito)
            escolhas = 0
        case 2:
            valorDeSaque = int(input("Qual valor deseja sacar?\n"))
            Banco().saque(valorDeSaque)
            escolhas = 0
        case 3:
            Banco().arrumarextrato()
            escolhas = 0
        case 4:
            quit("tchau")
        case _:
            print("Só números de 1 a 4")
            escolhas = 0
            