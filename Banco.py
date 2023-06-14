saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
LIMITE_SAQUES = 3


def sacar():
        global saldo, extrato, numero_saques
        print("Saque")
        valor = float(input("Qual é o o valor do Saque? "))
       
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou você não tem saldo suficiente.")

        elif excedeu_limite: 
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0: 
            saldo -= valor 
            extrato += "Saque: R$ {} ".format(valor) 
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")


def depositar():
    global saldo, extrato
    print("Depósito")
    valor = float(input("Qual é o o valor do desposito? "))

    if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

    else:
            print("Operação falhou, o valor informado é invalido.")          
         


def exibir_extrato():
    global extrato, saldo
    print("\n ======================= EXTRATO =======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\n========================================================")
    print("\nSaldo: R$ {}".format(saldo))
    print("==========================================================")


def criar_usuario(usuarios):
    cpf = input('Informe o seu CPF')
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        print("já existe usuario com esse CPF!")
        return
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe qual é a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Qual é o seu endereço: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("==== Usuario criado com sucesso! ====")

def filtrar_usarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] = cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


         

menu = """"

[d] depositar 
[s] sacar 
[e] extrato
[q] sair 
[nu] novo usuario


=> """

while True:

    opcao = input(menu)

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "nu":
         criar_usuario(usuarios)
    elif opcao == "e":
        exibir_extrato()
    
    elif opcao == "q":
        break
    else:
        print("Opção invalida, por favor selecione novamente a operação desejada.")