menu = """"

[d] depositar 
[s] sacar 
[e] extrato
[q] sair 


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Qual é o o valor do desposito? "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, o valor informado é invalido.")

    elif opcao == "s":
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

    elif opcao == "e":
       print("\n ======================= EXTRATO =======================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print("\n========================================================")
       print("\nSaldo: R$ {}".format(saldo))
       print("==========================================================")

    elif opcao == "q":
        break
    else:
        print("Opção invalida, por favor selecione novamente a operação desejada.")