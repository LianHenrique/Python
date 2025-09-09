def ftest(s):
    # Verifica se a string pode ser convertida para float, tratando vírgulas como pontos
    try:
        float(s.replace(",", "."))  # troca ',' por '.' para aceitar entrada no estilo PT-BR
        return True
    except ValueError:
        return False

def calculadora ():
    repeticao = True  # controla o loop principal
    numero1 = 0
    numero2 = 0
    escolha = ""
    operador = ""
    respostaposta = 0  # <-- provavelmente você quis escrever 'resposta' aqui

    while(repeticao):
        clear(100)  # limpa o terminal
        print("\nCalculadora\n")
        entrada = True

        # ENTRADA DO PRIMEIRO NÚMERO
        while(entrada):
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            escolha = input("Numero: ")
            if(ftest(escolha)):  # verifica se é número válido
                numero1 = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha != "!" and escolha.lower() != "r"):
                print("\nErro, numero invalido!")
            else:
                entrada = False  # sai se for ! ou r

        if(escolha not in ["!", "r", "R"]):
            entrada = True
        clear(100)

        # ENTRADA DO SEGUNDO NÚMERO
        while(entrada):
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            escolha = input("Numero: ")
            if(ftest(escolha)):
                numero2 = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha != "!" and escolha.lower() != "r"):
                print("\nErro, numero invalido!")
            else:
                entrada = False

        if(escolha not in ["!", "r", "R"]):
            entrada = True
        clear(100)

        # ESCOLHA DA OPERAÇÃO
        while(entrada):
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            print("1-Somar")
            print("2-Subtrair")
            print("3-Multiplicar")
            print("4-Dividir\n")
            escolha = input("Escolha: ")

            # ERRO AQUI ↓↓↓
            if(escolha.isnumeric()):  # aqui você usou 'esc.isnumeric()' antes — erro de digitação
                if(int(escolha) > 4 or int(escolha) < 1):
                    print("\nErro, operador invalido!")
                elif(int(escolha) == 1):
                    respostaposta = numero1 + numero2
                    operador = "+"
                    entrada = False
                elif(int(escolha) == 2):
                    respostaposta = numero1 - numero2
                    operador = "-"
                    entrada = False
                elif(int(escolha) == 3):
                    respostaposta = numero1 * numero2
                    operador = "*"
                    entrada = False
                elif(int(escolha) == 4):
                    respostaposta = numero1 / numero2
                    operador = "/"
                    entrada = False
            elif(escolha not in ["!", "r", "R"]):
                print("\nErro, operador invalido!")
            else:
                entrada = False

        # EXIBE O RESULTADO
        if(escolha not in ["!", "r", "R"]):
            entrada = True
            clear(100)
            while(entrada):
                print("Digite ! para sair\n")
                print("Digite R para Reiniciar\n")
                print(f"Resultado: {numero1} {operador} {numero2} = {respostaposta}\n")
                escolha = input("Escolha: ")
                if(escolha.lower() not in ["r", "!"]):
                    clear(100)
                    print("Erro, escolha invalida!\n")
                else:
                    entrada = False

        if(escolha == "!"):
            clear(100)
            rep = False  # ERRO: variável 'rep' não existe — você deveria usar 'repeticao = False'


def imc ():
    repeticao = True
    escolha = ""
    altura = 0
    peso = 0

    while(repeticao):
        entrada = True

        # ALTURA
        while(entrada):
            clear(100)
            print("\nIMC\n")
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            print("Digite sua altura (m)\n")
            escolha = input("Altura: ")
            if(ftest(escolha)):
                altura = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha not in ["!", "r", "R"]):
                print("Erro, altura inválida!")
            else:
                entrada = False

        if(escolha != "!"):
            entrada = True

        # PESO
        while(entrada):
            clear(100)
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            print("Digite seu peso (kg)\n")
            escolha = input("Peso: ")  # estava com texto "alturaura" — erro de digitação
            if(ftest(escolha)):
                peso = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha not in ["!", "r", "R"]):
                print("Erro, peso inválido!")
            else:
                entrada = False

        # CALCULA IMC
        if(escolha not in ["!", "r", "R"]):
            resposta = peso / (altura ** 2)
            clear(100)
            entrada = True
            while(entrada):
                # Exibe categoria baseada no IMC
                if(resposta < 16):
                    print("\nMagreza grave\n")
                elif(resposta < 17):
                    print(f"Magreza moderada {resposta:,.2f}")
                elif(resposta < 18.5):
                    print(f"Magreza leve {resposta:,.2f}")
                elif(resposta < 25):
                    print(f"Saudável {resposta:,.2f}")
                elif(resposta < 30):
                    print(f"Sobrepeso {resposta:,.2f}")
                elif(resposta < 35):
                    print(f"Obesidade grau I {resposta:,.2f}")
                elif(resposta < 40):
                    print(f"Obesidade grau II {resposta:,.2f}")
                else:
                    print(f"Obesidade grau III {resposta:,.2f}")

                print("Digite ! para sair\n")
                print("Digite R para Reiniciar\n")
                escolha = input("Escolha: ")
                if(escolha.lower() not in ["r", "!"]):
                    clear(100)
                    print("Erro, escolha invalida!")
                else:
                    entrada = False

        if(escolha == "!"):
            repeticao = False


def clear(times):
    """Simula a limpeza da tela no terminal imprimindo várias linhas"""
    if isinstance(times, int):
        for i in range(times):
            print()


entrada = True
while(entrada):
    clear(100)
    print("Menu\n")
    print("1-Calculadora\n")
    print("2-IMC\n")
    escolha = input("Escolha: ")
    if(escolha.isnumeric()):
        if(int(escolha) == 1):
            clear(100)
            calculadora()
        elif(int(escolha) == 2):
            clear(100)
            imc()
        else:
            print("Erro, escolha não existe!")
    else:
        print("Erro, escolha invalida!")