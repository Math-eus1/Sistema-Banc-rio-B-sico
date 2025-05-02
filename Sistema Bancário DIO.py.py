from datetime import *
from math import *
import random



def banco():
    print('''
    =========================================
          Seja Bem vindo ao Banco União
    =========================================
    ''')
banco()

print("\n","-"*42,"\n Olá! Mais uma vez, seja bem vindo!\n","-"*42)

usuario = {}

def cadastro(usuario):

    nome = input('\nDigite seu nome completo: ')

    cpf = ((input("Digite seu CPF (somente números): ")))
    while len(cpf) < 11:
        cpf = ((input("Digite seu CPF (somente números): ")))

    endereco = input("Digite seu endereço: ")
    num_casa = int(input("Digite o número da sua casa: "))
    num_senha = int(input("Digite uma senha (somente números): "))
    codigo = random.randint(101, 998)
    num_conta = random.randint(101101100, 989898980)

    usuario["Nome"] = nome
    usuario["CPF"] = cpf
    usuario["Endereço"] = endereco
    usuario["Número"] = num_casa
    usuario["Senha"] = num_senha
    usuario["Código"] = codigo
    usuario["Número da conta"] = num_conta

cadastro(usuario)

def login(usuario):
    logar = '''
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    Agora vamos finalizar o cadastro da conta bancária
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        '''
    print(logar)
    confirmar_cpf = int(input("Confirme o CPF que você havia digitado: "))
    confirmar_senha = int(input("Confirme sua senha de 6 dígitos (somente números): "))
    if confirmar_cpf != usuario["CPF"] and confirmar_senha != usuario["Senha"]:
        print("Dados Inválidos")
        confirmar_cpf = int(input("Confirme o CPF que você havia digitado: "))
        confirmar_senha = int(input("Confirme sua senha (somente números): "))
        if confirmar_cpf != usuario["CPF"] and confirmar_senha != usuario["Senha"]:
            print("dados inválidos novamente! Tente novamente mais tarde!")
            exit()
        else:
            print("~"*70)
            print("Ótimo! Agora vamos disponibilizar seu código e número da conta: ")
            print("~"*70)
            print(f"Seu código é {usuario["Código"]}, e seu número da conta é {usuario["Número da conta"]}")
            servicos(saldo, limite_por_operacao_financeira, extrato_saida, extrato_entrada, operacao, LIMITE_OPERACAO, usuario)
            
    else:
        print("~"*70)
        print("Ótimo! Agora vamos disponibilizar seu código e número da conta: ")
        print("~"*70)
        print(f"Seu código é {usuario["Código"]}, e seu número da conta é {usuario["Número da conta"]}")
        servicos(saldo, limite_por_operacao_financeira, extrato_saida, extrato_entrada, operacao, LIMITE_OPERACAO, usuario)



menu = '''
----------------------------------------------------------------
Digite o número correspondente à operação que deseja realizar:
----------------------------------------------------------------
[1] - Depósito
.
[2] - Saque
.
[3] - Visualizar Extrato
.
[4] - Visualizar informações da sua conta
.
[5] - Sair dos Serviços

Digite: '''

menu_limite_transacao = '''
----------------------------------------------------------------
Digite o número correspondente à operação que deseja realizar:
----------------------------------------------------------------
[1] - Visualizar Extrato
.
[2] - Visualizar informações da sua conta
.
[3] - Sair dos Serviços

Digite: '''

print()

saldo = 0
limite_por_operacao_financeira = 500
extrato_saida = []
extrato_entrada = []
operacao = 0
LIMITE_OPERACAO = 10


def servicos(saldo, limite_por_operacao_financeira, extrato_saida, extrato_entrada, operacao, LIMITE_OPERACAO, usuario):
    while True:            
            digite_servico = int(input(menu))

            if digite_servico == 1:
                print("Serviço escolhido: DEPÓSITO ")
                print("-"*70)
                while operacao > LIMITE_OPERACAO:
                    print("O limite de transações diárias foi atingido, volte a operar amanhã!")
                    digite_servico = int(input(menu_limite_transacao))
                    if digite_servico == 1:
                        print("Serviço escolhido: VISUALIZAR EXTRATO ")
                        print("-"*70)
                        print("Extrato de saques:")
                        for saida in extrato_saida:
                            print(f"Saque de R${saida}")
                        print("-"*70)
                        print("Extrato de depósitos:")
                        for entrada in extrato_entrada:
                            print(f"Depósito de R${entrada}")
                        print("-"*70)
                        print(f"Seu saldo atualmente é: R${saldo}")

                    elif digite_servico == 2:
                        print("Serviço escolhido: VISUALIZAR INFORMAÇÕES DA CONTA ")
                        for c, v in usuario.items():
                            print(f"{c}: {v}")
                                    
                    elif digite_servico == 3:
                        print("Muito Obrigado por utilizar o Banco União! Volte sempre!")
                        break
                    
                else:
                    quant_deposito = float(input("Quanto deseja depositar? R$"))
                    if quant_deposito < 0:
                        print("Por favor, digite um valor válido para o depósito!")
                    else:
                        saldo += quant_deposito
                        operacao += 1
                        extrato_entrada.append(quant_deposito)
                        print(f"Depósito de R${quant_deposito:.2f} realizado com sucesso às {datetime.now()}!")
                        print()
                        print(f"Seu saldo atualmente é: R${saldo:.2f}")


            elif digite_servico == 2:
                print("Serviço escolhido: SAQUE ")
                print("-"*30)
                if operacao > LIMITE_OPERACAO:
                    print("O limite máximo de saques diários foi atingido, favor selecionar outro serviço.")
                    #while True:
                    digite_servico = int(input(menu_limite_transacao))

                    if digite_servico == 1:
                        print("Serviço escolhido: VISUALIZAR EXTRATO ")
                        print("-"*70)
                        print("Extrato de saques:")
                        for saida in extrato_saida:
                            print(f"Saque de R${saida} | {datetime.now()}")
                        print("-"*70)
                        print("Extrato de depósitos:")
                        for entrada in extrato_entrada:
                            print(f"Depósito de R${entrada} | {datetime.now()}")
                        print("-"*70)
                        print(f"Seu saldo atualmente é: R${saldo}")

                    if digite_servico == 2:
                        print("Serviço escolhido: VISUALIZAR INFORMAÇÕES DA CONTA ")
                        for c, v in usuario.items():
                            print(f"{c}: {v}")
                                    
                    elif digite_servico == 3:
                        print("Muito Obrigado por utilizar o Banco União! Volte sempre!")
                        break
                                    
                # break
                else:
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
                                operacao += 1
                                extrato_saida.append(valor_saque)
                                print(f"Saque de R${valor_saque} realizado com sucesso às {datetime.now()}!")
                                print()
                                print()
                                print(f"Seu saldo atualmente é: R${saldo}")
                                print("-"*70)
                                    
                
            elif digite_servico == 3:
                print("Serviço escolhido: VISUALIZAR EXTRATO ")
                print("-"*70)
                print("Extrato de saques:")
                for saida in extrato_saida:
                    print(f"Saque de R${saida} | {datetime.now()}")
                print("-"*70)
                print("Extrato de depósitos:")
                for entrada in extrato_entrada:
                    print(f"Depósito de R${entrada} | {datetime.now()}")
                print("-"*70)
                print(f"Seu saldo atualmente é: R${saldo}")

            elif digite_servico == 4:
                print("Serviço escolhido: VISUALIZAR INFORMAÇÕES DA CONTA ")
                for c, v in usuario.items():
                    print(f"{c}: {v}")
                                                    
            elif digite_servico == 5:
                print("Muito Obrigado por utilizar o Banco União! Volte sempre!")
                break

login(usuario)