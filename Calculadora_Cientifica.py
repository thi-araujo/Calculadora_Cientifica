# CALCULADORA CIENTÍFICA


print("CALCULADORA CINTÍFICA!!!")

usuario = input(" DIGITE SEU NOME POR FAVOR: \n")

print("\t BEM VINDO", usuario)

print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

while True:
    start = input("Para CONTAS BÁSICAS........: [1] \n "
                  "Para CÍRCULOS..............: [2] \n "
                  "Para EQUAÇÃO DO 2° GRAU....: [3] \n"
                  "Para RAÍZES E POTÊNCIAS....: [4] \n"
                  "Para CONVERSOR DE UNIDADE..: [5] \n"
                  "Para GEOMETRIA.............: [6] \n"
                  "Para FUNÇÃO................: [7] \n"
                  "Para VELOCIDADE MÉDIA......: [8] \n"
                  "Para SAIR DO PROGRAMA......: [N] \n")

    if start == 'n':
        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
        exit()

    if start == '1':

        print("\t CONTAS BÁSICAS: \n")

        import math

        primeiro = input("\t DIGITE O PRIMEIRO NÚMERO:\n ")
        segundo = input("\t DIGITE O SEGUNDO NÚMERO:\n ")
        operacao = input("\t DIGITE A OPERÇÃO:\n ")

        resultado = None
        if operacao == '+':
            resultado = float(primeiro) + float(segundo)
        elif operacao == "-":
            resultado = float(primeiro) - float(segundo)
        elif operacao == "*":
            resultado = float(primeiro) * float(segundo)
        elif operacao == "/":
            resultado = float(primeiro) / float(segundo)
        else:
            print(usuario, "\t IMPOPSSÍVEL REALIZAR ESSA OPERAÇÃO!!!\n ")

        if resultado:
            print("\t RESULTADO: {0}".format(resultado))

            break

        continue

    # FIM DESSA PARTE DO PROGRAMA

    if start == '2':
        print("\t CIRCULOS: \n")

        print(usuario, "\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPÇÕES: \n")

        a = input("ÁREA DO CIRCULO ----> \n'1'\n"
                  "COMPRIMENTO DO CIRCULO ----> \n'2'\n"
                  "SAIR ----> \n'n'\n")

        if a == 'n':
            print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")

            exit()

        if a == '1':
            print("\t ÁREA DO CIRCULO: \n")

            import math

            pi = 3.14

            r = input("DIGITE O VALOR DO RAIO: ")

            resp = (float(r) * float(r)) * pi

            print("\t A ÁREA DO CIRCULO É:", resp, "\n")

            break

        if a == '2':
            print("\t COMPRIMENTO DO CIRCULO: \n")

            import math

            pi = 3.14

            r = input("DIGITE O VALOR DO RAIO: ")

            resp = (float(r) * 2) * pi

            print("\t O COMPRIMENTO DO CIRCULO É:", resp, "\n")

            break


        else:
            print("\t CARACTERE INVÁLIDO!!!\n")

            continue

    if start == '3':

        print("\t EQUAÇÃO DE SEGUNDO GRAU: \n")
        import math

        a = int(input("DIGITE UM VALOR PARA  a: "))
        b = int(input("DIGITE UM VALOR PARA  b: "))
        c = int(input("DIGITE UM VALOR PARA  c: "))

        delta = b * b - 4 * a * c

        if delta < 0:
            print("\t ESTA OPERAÇÃO NÃO POSSUÍ RAÍZES REAIS\n ")
        elif delta == 0:
            raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
            print("\t A EQUAÇÃO POSSUÍ APENAS UMA RAIZ REAL", raiz)
        elif delta > 0:
            raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
            print("\t  AS RAÍZES DA EQUAÇÃO SÃO:", raiz1, "E", raiz2)

            break

    if start == '4':
        print("\t RADIAÇÃO E POTÊNCIAÇÃO: \n")
        print("PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES: ")

        while True:
            st = input("Potênciação: \n'1'\n"
                       "Radiação: \n'2'\n"
                       "SAIR: \n'n'\n")

            if st == 'n':
                print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
                exit()

                break

            if st == '1':
                print("\t POTÊNCIAS: \n")

                import math

                a = input("DIGITE UM VALOR PARA a: ")
                b = input("DIGITE UM VALOR PARA b: ")

                resp = None

                resp = float(a) ** float(b)

                if resp:
                    print("\t RESULTADO: {0}".format(resp))

                    break

            if st == '2':
                print("\t RADIAÇÃO: \n")

            import math

            raiz = float(input("DIGITE UM VALOR: "))
            radical = float(input("DIGITE O RADICAL: "))

            if radical == '2':
                raiz2 = raiz ** (1 / 2)
                print("A Raiz Quadrada é:", raiz2)

            if radical == '3':
                raiz3 = raiz ** (1 / 3)
                print(usuario, "A Raiz Cúbica é:", raiz3)

            else:
                print(usuario, "\t CARACTERE INVÁLIDO!!!\n")

    if start == '6':
        print("\t CONVERSSOR DE UNIDADE: \n")
        print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

        while True:
            un = input("Comprimento: \n'1'\n"
                       "Área: \n'2'\n"
                       "Temperatura: \n'3'\n"
                       "Volume: \n'4'\n"
                       "Massa: \n'5'\n"
                       "Dados: \n'6'\n"
                       "SAIR: \n'n'\n")

            if un == 'n':
                print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                exit()

                break

            if un == '1':
                print("\t COMPRIMENTO: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    a = input("M ----> Cm: \n'1'\n"
                              "M ----> Mm: \n'2'\n"
                              "Cm ----> M: \n'3'\n"
                              "Cm ----> mm: \n'4'\n"
                              "Mm ----> M: \n'5'\n"
                              "Mm ----> Cm: \n'6'\n"
                              "SAIR: \n'n'\n")

                    if a == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                        exit()

                        break

                    if a == '1':
                        print("\t M ----> CM\n")

                        import math

                        v1 = input("DIGITE O COMPRIMENTO INICIAL: ")

                        resp = float(v1) * (100)
                        print(" O COMPRIMENTO É:", resp)

                        break

                    if a == '2':
                        print("\t M ----> MM\n")

                        import math

                        v1 = input("DIGITE O COMPRIMENTO INICIAL: ")

                        resp = float(v1) * 10000
                        print("O COMPRIMENTO É:", resp)

                        break

                    if a == '3':
                        print("\t CM ----> M\n")

                        import math

                        v1 = input("DIGITEO COMPRIMENTO EM CENTÍMETROS: ")

                        resp = float(v1) / 100
                        print("O COMPRIMENTO É:", resp)

                        break

                    if a == '4':
                        print("\t CM ----> MM\n")

                        import math

                        v1 = input("DIGITE O COMPRIMENTO EM CENTÍMETROS: ")

                        resp = float(v1) * 100
                        print("O COMPRIMENTO É:", resp)

                        break

                    if a == '5':
                        print("\t MM ----> M\n")

                        import math

                        v1 = input("DIGITE O COMPRIMENTO EM MILIMETROS: ")

                        resp = float(v1) / 10000
                        print(" COMPRIMENTO É:", resp)

                        break

                    if a == '6':
                        print("\t MM ----> CM\n")

                        import math

                        v1 = input("DIGITE O COMPRIMENTO EM MILIMETROS: ")

                        resp = float(v1) / 100
                        print("O COMPRIMENTO É:", resp)

                        break

            if un == '2':
                print("\t ÁREA: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    b = input("ÁREA DO QUADRADO: \n'q'\n"
                              "ÁREA DO RETÂNGULO: \n'r'\n"
                              "ÁREA DO TRIÂNGULO: \n't'\n"
                              "ÁREA DO TRAPÉZIO: \n'tp'\n"
                              "SAIR: \n'n'\n")

                    if b == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                        exit()

                        break

                    if b == 'q':
                        print("\t ÁREA DO QUADRADO: \n")

                        import math

                        a = input("DIGITE UM DOS LADOS DO QUADRADO: ")

                        resp = float(a) * float(a)
                        print("A ÁREA DO QUADRADO É:", resp)

                        break

                    if b == 'r':
                        print("\t ÁREA DO RETÂNGULO: ")

                        import math

                        a = input("DIGITE O LADO A DO RETÂNGULO: ")
                        b = input("DIGITE O LADO B DO RETÂNGULO: ")

                        resp = float(A) * float(b)
                        print("A ÁREA DO RETÂNGULO É:", resp)

                        break

                    if b == 't':
                        print("\t ÁREA DO TRIÂNGULO: \n")

                        import math

                        a = input("DIGITE O VALOR DA BASE DO TRIÂNGULO: ")
                        b = input("DIGITE O VALOR DA ALTURA DO TRIÂNGULO: ")

                        resp = (float(a) * float(b)) / 2
                        print("A ÁREA DO TRIÂNGULO É:", resp)

                        break

                    if b == 'tp':
                        print("\t ÁREA DO TRAPÉZIO: \n")

                        import math

                        a = input("DIGITE O VALOR DA BASE DO TRAPÉZIO: ")
                        b = input("Digite O VALOR DA PARTE SUPERIOR DO TRAPÉZIO: ")
                        h = input("Digite O VALOR DA ALTURA DO TRAPÉZIO: ")

                        resp = (float(a) + float(b) * float(h)) / 2
                        print("A ÁREA DO TRAPÉZIO É:", resp)

                        break

                    break

            if un == '3':
                print("\t CONVERSOR DE TEMPERATURA: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    t = input("º CELSIUS ----> ºFAHRENHEIT: \n'1'\n"
                              "º CELSIUS ----> KELVIN: \n'2'\n"
                              "º FAHRENHEIT ----> º CELSIUS: \n'3'\n"
                              "º FAHRENHEIT ----> KELVIN: \n'4'\n"
                              "KELVIN----> º CELSIUS: \n'5'\n"
                              "KELVIN ----> º FAHRENHEIT: \n'6'\n"
                              "SAIR: \n'n'\n")

                    if t == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                        exit()

                        break

                    if t == '1':
                        print("\t ºCELSIUS ----> ºFAHRENHEIT: \n")

                        import math

                        a = input("DIGITE A TEMPERATURA EM GRAUS CELSIUS: ")

                        resp1 = float(a) * 9

                        resp = (float(resp1) + 160) / 5
                        print("A TEMPERATURA EM ºF É:", resp)

                        break

                    if t == '2':
                        print("\t CELSIUS ----> KELVIN: \n")

                        import math

                        a = input("DIGITE A TEMPERATURA EM GRAUS CELSIUS: ")

                        resp = float(a) + 273
                        print("A TEMPERATURA EM K É:", resp)

                        break

                    if t == '3':
                        print("\t FAHRENHEIT ----> CELSIUS: \n")

                        import math

                        a = input("DIGITE A TEMPERATURA EM GRAUS FAHRENHEIT: ")

                        resp1 = float(a) * 5

                        resp = (float(resp1) - 160) / 9
                        print("A TEMPERATURA EM ºC É:", resp)

                        break

                    if t == '4':
                        print("\t FAHRENHEIT ----> KELVIN: \n")

                        import math

                        a = input("DIGITE A TEMPERATURA EM GRAUS FAHRENHEIT: ")

                        resp1 = float(a) + 459.67

                        resp = float(resp1) / 1.8
                        print("A TEMPERATURA EM K É:", resp)

                        break

                    if t == '5':
                        print("\t KELVIN ----> CELSIUS: \n")

                        import math

                        a = input("DIGITE A TEMPERATURA EM GRAUS KELVIN: ")

                        resp = float(a) - 273
                        print(" A TEMPERETURA EM ºC É:", resp)

                        break

                    if t == '6':
                        print("\t KELVIN ----> FAHRENHEIT: \n")

                        import math

                        a = input("DIGITE A TEMPERATURA EM GRAUS KELVIN: ")

                        resp1 = float(a) * 1.8

                        resp = float(resp1) - 459.67
                        print("A TEMPERATURA EM ºF É:", resp)

                        break
