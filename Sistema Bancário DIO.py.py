def banco():
    print('''
    =========================================
          Seja Bem vindo ao Banco União
    =========================================
    ''')
banco()

print("\n","-"*42,"\n Olá! Mais uma vez, seja bem vindo!\n","-"*42)

menu = '''
----------------------------------------------------------------
Dgite o número correspondente à operação que deseja realizar:
----------------------------------------------------------------
[1] - Depósito
.
[2] - Saque
.
[3] - Visualizar Extrato
.
[4] - Sair dos Serviços

Digite: '''

menu_limite_saque = '''
----------------------------------------------------------------
Digite o número correspondente à operação que deseja realizar:
----------------------------------------------------------------
[1] - Depósito
.
[3] - Visualizar Extrato
.
[4] - Sair dos Serviços

Digite: '''

print()

saldo = 100
limite_por_operacao_financeira = 500
extrato_saida = []
extrato_entrada = []
numero_saques = 0
LIMITE_SAQUE = 3

def servicos(saldo, limite_por_operacao_financeira, extrato_saida, extrato_entrada, numero_saques, LIMITE_SAQUE):
    while True:

        digite_servico = float(input(menu))

        if digite_servico == 1:
            print("Serviço escolhido: DEPÓSITO ")
            print("-"*30)
            quant_deposito = float(input("Quanto deseja depositar? R$"))
            if quant_deposito < 0:
                print("Por favor, digite um valor válido para o depósito!")
            else:
                saldo += quant_deposito
                extrato_entrada.append(quant_deposito)
                print(f"Depósito de R${quant_deposito:.2f} realizado com sucesso!")
                print()
                print(f"Seu saldo atualmente é: R${saldo:.2f}")


        elif digite_servico == 2:
            print("Serviço escolhido: SAQUE ")
            print("-"*30)
            if numero_saques > 3:
                print("O limite máximo de saques diários foi atingido, favor selecionar outro serviço.")
            valor_saque = float(input("Qual o valor que deseja sacar da sua conta? R$"))

            if valor_saque <= 0:
                print("Por favor, digite um valor válido para o saque!")

            else:
                if valor_saque > saldo:
                    print("Não é possível realizar o saque desejado, uma vez que a solicitação é maior do que consta no seu saldo.")

                else:
                    if valor_saque > limite_por_operacao_financeira:
                        print("Perdão, o Limite máximo para saque por operação financeira é R$ 500,00.")

                    else:
                        saldo -= valor_saque
                        numero_saques += 1
                        extrato_saida.append(valor_saque)
                        saques_restantes = LIMITE_SAQUE - numero_saques
                        print(f"Saque de R${valor_saque} realizado com sucesso!")
                        print()
                        print()
                        print(f"Seu saldo atualmente é: R${saldo}")
                        print(f"Hoje você só tem mais {saques_restantes} saques restantes.")
                        print("-"*30)


                
                        if saques_restantes <= 0:
                            print("O limite máximo de saques diários foi atingido, favor selecionar outro serviço.")
                            while True:

                                digite_servico = float(input(menu_limite_saque))


                                if digite_servico == 1:
                                    print("Serviço escolhido: DEPÓSITO ")
                                    print("-"*30)
                                    quant_deposito = int(input("Quanto deseja depositar? R$"))
                                    if quant_deposito < 0:
                                        print("Por favor, digite um valor válido para o depósito!")
                                    else:
                                        saldo += quant_deposito
                                        extrato_entrada.append(quant_deposito)
                                        print(f"Depósito de R${quant_deposito} realizado com sucesso!")
                                        print()
                                        print(f"Seu saldo atualmente é: R${saldo}")



                                elif digite_servico == 3:
                                    print("Serviço escolhido: VISUALIZAR EXTRATO ")
                                    print("-"*30)
                                    print("Extrato de saques:")
                                    for saida in extrato_saida:
                                        print(f"Saque de R${saida}")
                                    print("-"*30)
                                    print("Extrato de depósitos:")
                                    for entrada in extrato_entrada:
                                        print(f"Saque de R${entrada}")
                                    print("-"*30)
                                    print(f"Seu saldo atualmente é: R${saldo}")

                                
                                elif digite_servico == 4:
                                    print("Muito Obrigado por utilizar o Banco União! Volte sempre!")
                                    break
                                
                            break
                                   
            
        elif digite_servico == 3:
            print("Serviço escolhido: VISUALIZAR EXTRATO ")
            print("-"*30)
            print("Extrato de saques:")
            for saida in extrato_saida:
                print(f"Saque de R${saida}")
            print("-"*30)
            print("Extrato de depósitos:")
            for entrada in extrato_entrada:
                print(f"Saque de R${entrada}")
            print("-"*30)
            print(f"Seu saldo atualmente é: R${saldo}")

                                                
        elif digite_servico == 4:
            print("Muito Obrigado por utilizar o Banco União! Volte sempre!")
            break

servicos(saldo, limite_por_operacao_financeira, extrato_saida, extrato_entrada, numero_saques, LIMITE_SAQUE)

