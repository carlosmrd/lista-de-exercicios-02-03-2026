import math


def menu():
    print("Selecione um exercício:")
    print("1. Variáveis Simples")
    print("2. Entrada de Dados")
    print("3. Operações Matemáticas Básicas")
    print("4. Loja Virtual")
    print("5. Adivinhação")
    print("6. Notas Finais")
    print("7. Peso Ideal")
    print("8. Sistema de Loja com Pagamento")
    print("0. Sair")

    while True:
        try:
            opcao = int(input("Selecione uma opção: "))
            break
        except ValueError:
            print("Valor inválido")

    match opcao:
        case 1:
            VariaveisSimples()
        case 2:
            EntradaDeDados()
        case 3:
            OperaçõesMatematicasBasicas()
        case 4:
            LojaVirtual()

def VariaveisSimples():
# Crie um programa que demonstra o uso de variáveis básicas (inteiros, floats, strings e
# booleanos). Após entender como funciona, modifique o programa para incluir mais dois
# tipos de variáveis: uma lista e um dicionário.

    print("\nTemos 6 tipos de varíaveis básicas, aqui está um exemplo de cada uma delas")
    inteiros = 1
    floats = 1.5
    strings = "Exemplo"
    booleans = True
    lista = ["inteiros", "floats", "strings", "booleans", "lista", "dicionario"]
    dicionario = {
        "inteiros": "Números inteiros",
        "floats": "Números reais",
        "strings": "Texto",
        "booleans": "Valores lógicos",
        "Lista": "Conjunto de dados",
        "Dicionario": "Conjunto de dados em pares de chave e valor"
    }

    print(inteiros, type(inteiros))
    print(floats, type(floats))
    print(strings, type(strings))
    print(booleans, type(booleans))
    print(lista, type(lista))
    print(dicionario, type(dicionario))

    PromptRetornar()

def EntradaDeDados():
#O programa irá solicitar que o usuário insira um nome e um número. Verificar se o
#número digitado é par ou ímpar, validar se o nome contém mais de 3 caracteres. Se
#não, peça para o usuário digitar novamente.

    while True:
        nome = input("\nInsira um nome: ")
        if len(nome) < 3:
            print("Nome inválido, mínimo de 3 caracteres")
        else:
            break

    while True:
        try:
            numero = int(input("Insira um número: "))
            break
        except ValueError:
            print("Valor inválido")

    if numero % 2 == 0:
        print(numero, " é par.")
    else:
        print(numero, "é ímpar.")

    PromptRetornar()

def OperaçõesMatematicasBasicas():
#Descrição: Um programa que realiza operações matemáticas básicas (soma, subtração,
#multiplicação, divisão, raiz quadrada e logaritmo) entre dois números fornecidos
#pelo usuário.

    print("\nOperações matemáticas básicas entre dois valores.")

    while True:
        try:
            primeiroValor = float(input("Primeiro valor: "))
            break
        except ValueError:
            print("Valor inválido")

    print("Possíveis operações:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz Quadrada")
    print("6. Logaritmo")

    while True:
        try:
            operacao = int(input("Selecione a operação: "))
            break
        except ValueError:
            print("Valor inválido")

    if operacao != 5 and operacao != 6:
        while True:
            try:
                segundoValor = float(input("Segundo valor: "))
                break
            except ValueError:
                print("Valor inválido")

    match operacao:
        case 1:
            resultado = primeiroValor + segundoValor
        case 2:
            resultado = primeiroValor - segundoValor
        case 3:
            resultado = primeiroValor * segundoValor
        case 4:
            resultado = primeiroValor / segundoValor
        case 5:
            resultado = math.sqrt(primeiroValor)
        case 6:
            resultado = math.log(primeiroValor)

    print("O resultado é", resultado)

    PromptRetornar()

def LojaVirtual():
#Uma loja virtual apresenta ao usuário a possibilidade de escolher entre diferentes
#produtos (mínimo de 3) e suas quantidades, calcular o valor total de um pedido e
#incluirdescontos baseados na quantidade de itens (5) comprados e adicione a opção de
#calcular ofrete baseado em correio, transportadora e motoboy.
    produtos = {
        "Teclado": 95.60,
        "Monitor": 730.90,
        "Notebook": 2450.95,
        "Mouse sem fio": 110.30,
        "Mouse com fio": 50.95
    }

    print("\nBem vindo! Produtos disponíveis:")
    for index, (produto, valor) in enumerate(produtos.items()):
        print(f"ID: {index + 1}. {produto} - R${valor:.2f}")

    carrinho = {}

    while True:
        try:
            idProduto = int(input("Insira o ID do produto a adicionar ao carrinho: "))
            if idProduto < 0 or idProduto > len(produtos):
                print("Produto inexistente.")
            else:
                while True:
                    try:
                        quantidade = int(input("Selecione a quantidade: "))
                        if quantidade < 0:
                            print("Valor inválido")
                        else:

                            break
                    except ValueError:
                        print("Valor inválido")
        except ValueError:
            print("Valor inválido")




def PromptRetornar():
    while True:
        try:
            option = str(input("\nDeseja retornar ao menu? (S/N) "))
            if option.lower() == "s" or option.lower() == "n":
                break
            else: print("Valor inválido")
        except: print("Valor inválido")

    match option:
        case "s":
            menu()
        case "n":
            exit()

if __name__ == "__main__":
    menu()