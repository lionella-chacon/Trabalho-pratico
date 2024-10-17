saida = ''

#soma
def adicao(a,b):
    return a + b
#subtração
def subtracao(a,b):
    return a - b

#multiplicação
def multiplicacao(a,b):
    return a * b
#divisão
def divisao(a,b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return a // b
#calculadora
def calculadora (a,b, operacao):
    print(calculadora)
    if operacao == '+' or operacao.lower() == "soma":
        return a + b
    elif operacao == "-" or operacao.lower() == "subtracao":
        return a - b
    elif operacao == "*" or operacao.lower() == "multiplicacao":
        return a * b
    elif operacao == "//" or operacao.lower() == "divisao":
        if b != 0:
            return a // b
        else:
            print('Não foi possível realizar a divisão por 0')
#Verificando a operação
saida = ''
while saida != 'n':
    numero1 = input('Digite o primeiro número ou n para sair: ')
    if numero1.lower() == 'n':
        print('Você saiu')
        break
    numero2 = input('Digite o segundo número ou n para sair: ')
    if numero2.lower() == 'n':
        print('Você saiu')
        break

    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
    except ValueError:
        print('Dados inválidos')
        continue
    #Chamando a função
    operacao = input('Digite a operação desejada (soma +, subtração -, multiplicação *, divisão//)')
    resultado = calculadora(numero1, numero2, operacao)
    print(f'Resultado da operação: {resultado}')
    saida = input('Deseja continuar? Digite s para sim ou n para não: ').lower()