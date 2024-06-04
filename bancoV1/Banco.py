#Variáveis
escolhas=0
Total = 0
extrato = []
Limite = 500
Cpf = set([])
conta = 0
#Classes
class Banco():
    def saque(self, valorDeSaque):
        global Total
        global Limite
        if Total <= 0 or Total - valorDeSaque < 0:
            print("Não possui dinheiro em conta")
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
        ArrumarExtrato = extrato.copy()
        for i in range(len(ArrumarExtrato)):
            preco = "R$"
            if preco in str(ArrumarExtrato[i]):
                pass
            else:
                ArrumarExtrato.insert(i,"R$ " + str(ArrumarExtrato[i]))
                ArrumarExtrato.pop(i+1)         
        print(f"Extrato da conta(positivos depósito e negativos saques) {ArrumarExtrato}")
        print(f"Total em conta: R${Total}")
    def criar_usuario(self, CpfCadastro):
        if len(str(CpfCadastro)) >11 or len(str(CpfCadastro)) < 11:
            print("CPF inválido\n")
        elif CpfCadastro in Cpf:
            print("CPF já cadastrado\n")
        else:
            Cpf.add(CpfCadastro)
            CpfCadastro = str(CpfCadastro)
            print(f"Criada a conta no Cpf ***.***.***-{CpfCadastro[9:11]}\n")
            print(Cpf)
        pass


while True:
    try:
        escolhas = int(input("1.Depósito\n2.Saque\n3.Extrato\n4.Criar Conta\n5.Sair\n"))
        match escolhas:
            case 1:
                try:
                    valorDeDeposito = float(input("Qual valor deseja depositar?\n"))
                    Banco().deposito(valorDeDeposito)
                except ValueError:
                    print("Somente números\n")
            case 2:
                try:
                    valorDeSaque = float(input("Qual valor deseja sacar?\n"))
                    Banco().saque(valorDeSaque)
                except ValueError:
                    print("Somente números\n")
            case 3:
                Banco().arrumarextrato()
            case 4:
                try:
                    CpfCadastro = int(input("Qual Cpf deseja cadastrar?\n"))
                    Banco().criar_usuario(CpfCadastro)
                except ValueError:
                    print("Somente números\n")
            case 5:
                quit("tchau")
            case _:
                print("Só números de 1 a 5\n")
    except ValueError:
        print("Somente numeros de 1 a 5\n")