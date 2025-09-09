def ftest(s):
    # retorna se é float ou não
    try:
        float(s.replace(",", ".")) # formata para float
        return True
    except ValueError:
        return False

def calculadora ():

    repeticao = True
    numero1 = 0
    numero2 = 0
    escolha = ""
    operador = ""
    respostaposta = 0

    while(repeticao):
        clear(100)
        print("\nCalculadora\n")
        entrada = True
        while(entrada):
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            escolha = input("Numero: ")
            if(ftest(escolha)):
                numero1 = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha != "!" and escolha != "r" and escolha != "R"):
                print("\nErro, numero invalida!")
            else:
                entrada = False
        if(escolha != "!" and escolha != "r" and escolha != "R"):
            entrada = True
        clear(100)
        while(entrada):
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            escolha = input("Numero: ")
            if(ftest(escolha)):
                numero2 = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha != "!" and escolha != "r" and escolha != "R"):
                print("\nErro, numero invalida!")
            else:
                entrada = False
        if(escolha != "!" and escolha != "r" and escolha != "R"):
            entrada = True
        clear(100)
        while(entrada):
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            print("1-Somar")
            print("2-Subtrair")
            print("3-Multiplicar")
            print("4-Dividir\n")
            escolha = input("Escolha: ")
            if(esc.isnumeric()):
                if(int(escolha) > 4 or int(escolha) < 0):
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
            elif(escolha != "!" and escolha != "r" and escolha != "R"):
                print("\nErro, operador invalido!")
            else:
                entrada = False

        if(escolha != "!" and escolha != "r" and escolha != "R"):
            entrada = True
            clear(100)
            while(entrada):
                print("Digite ! para sair\n")
                print("Digite R para Reiniciar\n")
                print(f"respostautado: {numero1} {operador} {numero2} = {respostaposta}\n")
                escolha = input("Escolha: ")
                if(escolha != "R" and escolha != "r" and escolha != "!"):
                    clear(100)
                    print("Erro, escolha invalida!\n")
                else:
                    entrada = False
        if(escolha == "!"):
            clear(100)
            rep = False

def imc ():
    repeticao = True
    escolha = ""
    altura = 0
    peso = 0
    while(repeticao):
        entrada = True
        while(entrada):
            clear(100)
            print("\nIMC\n")
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            print("Digite sua alturaura (m)\n")
            escolha = input("alturaura: ")
            if(ftest(escolha)):
                altura = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha != "!" and escolha != "r" and escolha != "R"):
                print("Erro, alturaura invalida!")
            else:
                entrada = False

        if(escolha != "!"):
            entrada = True

        while(entrada):
            clear(100)
            print("Digite ! para sair\n")
            print("Digite R para Reiniciar\n")
            print("Digite sua pesoo (kg)\n")
            escolha = input("alturaura: ")
            if(ftest(escolha)):
                peso = float(escolha.replace(",", "."))
                entrada = False
            elif(escolha != "!" and escolha != "r" and escolha != "R"):
                print("Erro, alturaura invalida!")
            else:
                entrada = False

        if(escolha != "!" and escolha != "r" and escolha != "R"):
            resposta = peso / (altura ** 2)
            clear(100)
            entrada = True
            while(entrada):
                if(resposta < 16):
                    print("\nMagreza grave\n")
                elif(resposta >= 16 and resposta < 17):
                    print(f"Magreza moderada {resposta:,.2f}")
                elif(resposta >= 17 and resposta < 18.5):
                    print(f"Magreza leve {resposta:,.2f}")
                elif(resposta >= 18.5 and resposta < 25):
                    print(f"Saudavel {resposta:,.2f}")
                elif(resposta >= 25 and resposta < 30):
                    print(f"Sobrepesoo {resposta:,.2f}")
                elif(resposta >= 30 and resposta < 35):
                    print(f"Obesidade grau I {resposta:,.2f}")
                elif(resposta >= 35 and resposta < 40):
                    print(f"Obesidade grau II {resposta:,.2f}")
                elif(resposta >= 40):
                    print(f"Obesidade grau III {resposta:,.2f}")
                print("Digite ! para sair\n")
                print("Digite R para Reiniciar\n")
                escolha = input("Escolha: ")
                if(escolha != "!" and escolha != "r" and escolha != "R"):
                    clear(100)
                    print("Erro, escolha invalida!")
                else:
                    entrada = False
        if(escolha == "!"):
            repeticao = False

def clear(times):
    """simulates the cleanning of the IDLE"""
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
        print("Erro, escolha invaluda!")