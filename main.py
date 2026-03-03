import math
import random

#Menu
def menu():

    while True:
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
        try:
            opcao_menu = int(input("Selecione uma opção: "))
            break
        except ValueError:
            print("Opção inválida")

    match opcao_menu:
        case 1:
            variaveis_simples()
        case 2:
            entrada_de_dados()
        case 3:
            operacoes_matematicas_basicas()
        case 4:
            loja_virtual()
        case 5:
            adivinhacao()
        case 6:
            notas_finais()
        case 7:
            peso_ideal()
        case 8:
            sistema_loja_com_pagamento()
        case _:
            print("Opção inválida")

#Exercício 1
def variaveis_simples():
#Crie um programa que demonstra o uso de variáveis básicas (inteiros, floats, strings e
#booleanos). Após entender como funciona, modifique o programa para incluir mais dois
#tipos de variáveis: uma lista e um dicionário.

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

    retornar_ao_menu()

#Exercício 2
def entrada_de_dados():
#O programa irá solicitar que o usuário insira um nome e um número. Verificar se o
#número digitado é par ou ímpar, validar se o nome contém mais de 3 caracteres. Se
#não, peça para o usuário digitar novamente.

    while True:
        nome = input("\nInsira um nome: ")
        if len(nome) < 3:
            print("Nome inválido, mínimo de 3 caracteres.")
        else:
            print("O nome inserido tem mais de 3 caracteres.")
            break

    while True:
        try:
            numero = int(input("\nInsira um número: "))
            break
        except ValueError:
            print("Valor inválido")

    if numero % 2 == 0:
        print(numero, " é par.")
    else:
        print(numero, "é ímpar.")

    retornar_ao_menu()

#Exercício 3
def operacoes_matematicas_basicas():
#Descrição: Um programa que realiza operações matemáticas básicas (soma, subtração,
#multiplicação, divisão, raiz quadrada e logaritmo) entre dois números fornecidos
#pelo usuário.

    print("\nOperações matemáticas básicas entre dois valores.")

    while True:
        try:
            primeiro_valor = float(input("Primeiro valor: "))
            break
        except ValueError:
            print("Valor inválido")

    while True:
        print("\nPossíveis operações:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Logaritmo")
        try:
            operacao = int(input("Selecione a operação: "))
            break
        except ValueError:
            print("Operação inválida")

    while True:
        match operacao:
            case 1 | 2 | 3 | 4:
                while True:
                    try:
                        segundo_valor = float(input("Segundo valor: "))
                        break
                    except ValueError:
                        print("Valor inválido")
                if operacao == 1:
                    resultado = primeiro_valor + segundo_valor
                    print("\nO resultado é", resultado)
                    break
                elif operacao == 2:
                    resultado = primeiro_valor - segundo_valor
                    print("\nO resultado é", resultado)
                    break
                elif operacao == 3:
                    resultado = primeiro_valor * segundo_valor
                    print("\nO resultado é", resultado)
                    break
                else:
                    if segundo_valor == 0:
                        print("\nNão é possível dividir por zero.")
                        break
                    resultado = primeiro_valor / segundo_valor
                    print("\nO resultado é", resultado)
                    break
            case 5:
                if primeiro_valor == 0:
                    print("\nNão é possível dividir por zero.")
                    break
                resultado = math.sqrt(primeiro_valor)
                print("\nO resultado é", resultado)
                break
            case 6:
                if primeiro_valor == 0:
                    print("\nNão é possível dividir por zero.")
                    break
                resultado = math.log(primeiro_valor)
                print("\nO resultado é", resultado)
                break
            case _:
                print("Operação inválida")
                continue

    retornar_ao_menu()

#Exercício 4
def loja_virtual():
#Uma loja virtual apresenta ao usuário a possibilidade de escolher entre diferentes
#produtos (mínimo de 3) e suas quantidades, calcular o valor total de um pedido e
#incluirdescontos baseados na quantidade de itens (5) comprados e adicione a opção de
#calcular o frete baseado em correio, transportadora e motoboy.

    produtos = {
        "Teclado": 95.60,
        "Monitor": 730.90,
        "Notebook": 2450.95,
        "Mouse sem fio": 110.30,
        "Mouse com fio": 50.95
    }

    ids = list(produtos.keys())

    carrinho = {}

    print("\nBem vindo!")

    while True:
        print("Produtos disponíveis:")

        for index, (produto, valor) in enumerate(produtos.items(), start=1):
            print(f"ID: {index} - {produto} - R${valor:.2f}")

        try:
            id_produto = int(input("\nInsira o ID do produto a adicionar ao carrinho: "))
            if id_produto < 0 or id_produto > len(produtos):
                print("Produto inexistente.")
            else:
                try:
                    quantidade = int(input("\nSelecione a quantidade: "))
                    if quantidade < 0:
                        print("Valor inválido")
                    else:
                        produto_escolhido = ids[id_produto - 1]
                        carrinho[produto_escolhido] = carrinho.get(produto_escolhido, 0) + quantidade

                        print("\nCarrinho atual:")
                        for nome, qtd in carrinho.items():
                            print(f"{nome}: {qtd} un.")


                        opcao_mais_itens = str(input("\nDeseja adicionar mais itens? (S/N) "))
                        if opcao_mais_itens.lower() == "s" or opcao_mais_itens.lower() == "n":
                            if opcao_mais_itens != "s":
                                break
                        else:
                            print("Valor inválido")

                except ValueError:
                    print("Valor inválido")

        except ValueError:
            print("Valor inválido")

    total_itens = sum(carrinho.values())
    subtotal = sum(produtos[nome] * qtd for nome, qtd in carrinho.items())

    if total_itens >= 5:
        print("\nDesconto de 10% aplicável devido a compra de 5 ou mais itens.")
        valor_final = subtotal
        valor_final -= subtotal * 0.10
    else:
        valor_final = subtotal

    valor_entrega = None

    while True:
        print("\nOpções de entrega:")
        print(f"1. Correios: R${total_itens * 12:.2f}")
        print(f"2. Transportadora: R${total_itens * 10:.2f}")
        if total_itens <= 3:
            print(f"3. Motoboy: R${total_itens * 5:.2f}")
        try:
            opcao_entrega = int(input("\nSelecione a forma de entrega: "))
            if opcao_entrega < 0:
                print("Opção inválida")
            else:
                match opcao_entrega:
                    case 1:
                        valor_entrega = total_itens * 12
                        break
                    case 2:
                        valor_entrega = total_itens * 10
                        break
                    case 3:
                        if total_itens <= 3:
                            valor_entrega = total_itens * 5
                            break
                        else:
                            print("Opção não aplicável para compras com 4 ou mais itens.")
                        continue
                    case _:
                        print("Opção inválida")
                        continue

        except ValueError:
            print("Opção inválida")

    print("\nResumo do pedido:")
    print(f"Itens no total: {total_itens}")
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Desconto: R${subtotal * 0.10:.2f}")
    print(f"Entrega: R${valor_entrega:.2f}")
    print(f"Total final: R${valor_final + valor_entrega:.2f}")

    retornar_ao_menu()

#Exercício 5
def adivinhacao():
#Um programa que permite ao usuário adivinhar um número e recebe feedback se o palpite
#foi maior ou menor que o número correto. Expanda o programa para incluir diferentes
#níveis de dificuldade (fácil, médio, difícil), onde o intervalo de números varia.

    valor_min = None
    valor_max = None

    while True:
        print(f"\nTente adivinhar o número secreto! Escolha a dificuldade:")
        print(f"1. Fácil - Entre 1 e 10")
        print(f"2. Médio - Entre 1 e 25")
        print(f"3. Difícil - Entre 1 e 100")
        try:
            dificuldade = int(input("Selecione uma opção: "))
            match dificuldade:
                case 1:
                    valor_min = 1
                    valor_max = 10
                    break
                case 2:
                    valor_min = 1
                    valor_max = 25
                    break
                case 3:
                    valor_min = 1
                    valor_max = 100
                    break
                case _:
                    print("Opção inválida")
                    continue
        except ValueError:
            print("Opção inválida")

    numero_aleatorio = random.randint(valor_min, valor_max)

    while True:
        try:
            palpite = int(input("\nInsira seu palpite: "))
            if palpite < valor_min:
                print(f"O número não pode ser menor que {valor_min:.0f}.")
            elif palpite > valor_max:
                print(f"O número não pode ser maior que {valor_max:.0f}.")
            elif palpite > numero_aleatorio:
                print(f"O número secreto é menor que {palpite:.0f}.")
            elif palpite < numero_aleatorio:
                print(f"O número secreto é maior que {palpite:.0f}.")
            else:
                print(f"Você acertou! O número era {numero_aleatorio:.0f}.")
                break

        except ValueError:
            print("Valor inválido")

    retornar_ao_menu()

#Exercício 6
def notas_finais():
#Um programa que calcula as somas das notas de provas e trabalhos e determina se o
#aluno foi aprovado, está em recuperação, ou foi reprovado. Adicione a funcionalidade
#de calcular médias trimestrais e uma média anual ao final.

    total_ano = 0.0

    print("Insira as notas de cada avaliação.")

    for trimestre in range(0, 4):
        print(f"\n{trimestre}º trimestre.")

        while True:
            try:
                prova1 = float(input("Prova 1 (0 a 30): "))
                if 0 <= prova1 <= 30:
                    break
                print("Valor inválido")
            except ValueError:
                print("Valor inválido")

        while True:
            try:
                prova2 = float(input("Prova 2 (0 a 30): "))
                if 0 <= prova2 <= 30:
                    break
                print("Valor inválido")
            except ValueError:
                print("Valor inválido")

        while True:
            try:
                trabalho = float(input("Trabalho (0 a 40): "))
                if 0 <= trabalho <= 40:
                    break
                print("Valor inválido")
            except ValueError:
                print("Valor inválido")

        total_trimestre = prova1 + prova2 + trabalho
        total_ano += total_trimestre

        print(f"Média do {trimestre}º trimestre: {total_trimestre:.1f}/100")

    media_anual = total_ano / 4
    print(f"\nMédia anual: {media_anual:.1f}/100")

    if media_anual >= 70:
        print("Situação: Aluno Aprovado")
    else:
        print("Situação: Aluno Reprovado")

    retornar_ao_menu()

#Exercício 7
def peso_ideal():
#Um programa que calcula o peso ideal baseado na altura e sexo do usuário, também calcular
#o IMC (Índice de Massa Corporal) e fazer recomendações baseadas no resultado.
#Homens
#Peso_Ideal=(Altura_cm−100)−Altura_cm−1504Peso\_Ideal = (Altura\_{cm} - 100) -\frac{Altura\_{cm} - 150}{4}Peso_Ideal=(Altura_cm−100)−4Altura_cm−150
#Mulheres
#Peso_Ideal=(Altura_cm−100)−Altura_cm−1502Peso\_Ideal = (Altura\_{cm} - 100) -\frac{Altura\_{cm} - 150}{2}Peso_Ideal=(Altura_cm−100)−2Altura_cm−150
#IMC=(Altura (cm)/100)2Peso (kg)

    print("Calculadora para IMC e peso ideal.")

    while True:
        sexo = input("Sexo (M/F): ").strip().lower()
        if sexo in ("m", "f"):
            break
        else:
            print("Valor inválido. Digite M ou F.")

    while True:
        try:
            altura_cm = float(input("Altura em cm: "))
            if altura_cm < 0:
                print("Valor inválido")
            else:
                break
        except ValueError:
            print("Valor inválido")

    while True:
        try:
            peso = float(input("Peso em kg: "))
            if peso < 0:
                print("Valor inválido")
            else:
                break
        except ValueError:
            print("Valor inválido")

    if sexo == "m":
        valor_peso_ideal = (altura_cm - 100) - ((altura_cm - 150) / 4)
    else:
        valor_peso_ideal = (altura_cm - 100) - ((altura_cm - 150) / 2)

    altura_m = altura_cm / 100
    imc = peso / math.pow(altura_m, 2)

    print(f"\nSeu peso ideal: {valor_peso_ideal:.1f}kg")
    print(f"Seu IMC: {imc:.1f}kg/m²")

    if imc < 18.5:
        print("Classificação: Abaixo do peso.")
    elif imc < 25:
        print("Classificação: Peso normal.")
    elif imc < 30:
        print("Classificação: Sobrepeso.")
    else:
        print("Classificação: Obesidade.")

    retornar_ao_menu()

#Exercício 8
def sistema_loja_com_pagamento():
#Crie um sistema de loja onde o usuário pode escolher produtos, calcular o total, e optar
#por pagamento à vista ou parcelado. Adicione taxas de juros para pagamentos parcelados.

    produtos = {
        "Teclado": 95.60,
        "Monitor": 730.90,
        "Notebook": 2450.95,
        "Mouse sem fio": 110.30,
        "Mouse com fio": 50.95
    }

    ids = list(produtos.keys())
    carrinho = {}

    juros_ao_mes = None
    parcelas = None

    print("\nBem vindo!")

    while True:
        print("\nProdutos disponíveis:")
        for index, (produto, valor) in enumerate(produtos.items(), start=1):
            print(f"ID: {index} - {produto} - R${valor:.2f}")

        try:
            id_produto = int(input("\nInsira o ID do produto: "))
        except ValueError:
            print("Valor inválido")
            continue

        if not (1 <= id_produto <= len(produtos)):
            print("Produto inexistente.")
            continue

        try:
            quantidade = int(input("Selecione a quantidade: "))
        except ValueError:
            print("Valor inválido")
            continue

        if quantidade <= 0:
            print("Valor inválido")
            continue

        produto_escolhido = ids[id_produto - 1]
        carrinho[produto_escolhido] = carrinho.get(produto_escolhido, 0) + quantidade

        print("\nCarrinho atual:")
        for nome, qtd in carrinho.items():
            print(f"{nome}: {qtd} un.")

        opcao = input("\nDeseja adicionar mais itens? (S/N) ").lower()
        if opcao != "s":
            break

    subtotal = sum(produtos[nome] * qtd for nome, qtd in carrinho.items())
    print(f"\nSubtotal: R${subtotal:.2f}")

    while True:
        print("\nFormas de pagamento:")
        print("1. À vista (10% de desconto)")
        print("2. Parcelado (juros compostos ao mês)")

        try:
            forma = int(input("Selecione a forma de pagamento: "))
        except ValueError:
            print("Opção inválida")
            continue

        if forma == 1:
            total_final = subtotal * 0.90
            print(f"\nTotal à vista (com desconto): R${total_final:.2f}")
            break

        elif forma == 2:
            while True:
                try:
                    parcelas = int(input("Número de parcelas (max. 12): "))
                except ValueError:
                    print("Valor inválido")
                    continue

                if not (2 <= parcelas <= 12):
                    print("Valor inválido")
                    continue
                break

            while True:
                try:
                    juros_ao_mes = float(input("Juros ao mês em %: "))
                except ValueError:
                    print("Valor inválido")
                    continue

                if juros_ao_mes < 0:
                    print("Valor inválido")
                    continue
                break

            i = juros_ao_mes / 100.0
            montante = subtotal * ((1 + i) ** parcelas)
            valor_parcela = montante / parcelas

            print(f"\nTotal parcelado: R${montante:.2f}")
            print(f"{parcelas}x de R${valor_parcela:.2f}")
            break

        else:
            print("Opção inválida")

    retornar_ao_menu()

def retornar_ao_menu():

    while True:
        opcao_retorno = str(input("\nDeseja retornar ao menu? (S/N) "))
        if opcao_retorno.lower() == "s" or opcao_retorno.lower() == "n":
            break
        else: print("Valor inválido")

    match opcao_retorno.lower():
        case "s":
            menu()
        case "n":
            exit()

if __name__ == "__main__":
    menu()