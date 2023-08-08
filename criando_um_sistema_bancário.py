menu= f"""

[d] Depósito
[s] Sacar
[e] Extrato
[q] Saír

=> """

saldo=0
limite = 500
extrato = ""
número_saques=0
LIMITE_SAQUE= 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo+= valor
            extrato += f"Depósito: R${valor:.2f}\n"
       
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao=="s":
        valor= float(input("Informe o valor do saque:"))

        excedeu_saldo = valor> saldo

        excedeu_limite = valor>limite

        excedeu_saque = número_saques>= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excedeu o limite.")
        
        elif excedeu_saque:
            print("Operação falhou! Número de saques excedido.")
      
        elif valor>0:
            saldo -= valor
            extrato+= f"Saque: R${valor:.2f}\n"
            número_saques += 1
       
        else:
            print("Operação falhou! o valor informador é inválido.")
   
    
    elif opcao == "e":
        print("\n============= EXTRATO============")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao== "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a opção desejada.")

