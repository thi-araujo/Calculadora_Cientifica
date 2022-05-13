# CALCULADORA CIENTÍFICA


print("=======================================CALCULADORA CIENTÍFICA==================================================")

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

# CALCULO CONTAS BÁSICAS

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
            un = input("COMPRIMENTO....: [1]\n"
                       "ÁREA...........: [2]\n"
                       "TEMPREATURA....: [3]\n"
                       "VOLUME.........: [4]\n"
                       "MASSA..........: [5]\n"
                       "DADOS..........: [6]\n"
                       "SAIR...........: [n]\n")

            if un == 'n':
                print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                exit()

                break

            if un == '1':
                print("\t COMPRIMENTO: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    a = input("M ----> Cm: [1]\n"
                              "M ----> Mm: [2]\n"
                              "Cm ---> M : [3]\n"
                              "Cm ---->mm: [4]\n"
                              "Mm ----> M: [5]\n"
                              "Mm ---->Cm: [6]\n"
                              "SAIR......: [n]\n")

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
                    b = input("ÁREA DO QUADRADO....: [q]\n"
                              "ÁREA DO RETÂNGULO...: [r]\n"
                              "ÁREA DO TRIÂNGULO...: [t]\n"
                              "ÁREA DO TRAPÉZIO....: [tp]\n"
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

                        resp = float(a) * float(b)
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

# CALCULO CONVERSÃO DE TEMPERATURA


            if un == '3':
                print("\t CONVERSOR DE TEMPERATURA: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    t = input("º CELSIUS ----> ºFAHRENHEIT....: [1]\n"
                              "º CELSIUS ----> KELVIN.........: [2]\n"
                              "º FAHRENHEIT ----> º CELSIUS...: [3]\n"
                              "º FAHRENHEIT ----> KELVIN......: [4]\n"
                              "KELVIN----> º CELSIUS..........: [5]\n"
                              "KELVIN ----> º FAHRENHEIT......: [6]\n"
                              "SAIR...........................: [n]\n")

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

# CALCULO CONVERSÃO DE VOLUMES

            if un == '4':
                print("\t CONVERSOR DE VOLUME: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    v = input("LITRO ----> MILILITRO..........: [1]\n"
                              "LITRO ----> METRO CÚBICO.......: [2]\n"
                              "LITRO ----> CENTÍMETRO CÚBICO..: [3]\n"
                              "MILILITRO----> LITRO...........: [4]\n"
                              "SAIR...........................: [n]\n")

                    if v == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
                        exit()

                    if v == '1':
                        print("\t LITRO ----> MILILITRO: \n")

                        a = input("DIGITE O VOLUME EM LITROS:")

                        resp = float(a) * 1000
                        print("O VOLUME EM ML É:", resp)

                        break

                    if v == '2':
                        print("\t LITRO ----> METRO CÚBICO:\n")

                        a = input("DIGTE O VOLUME EM LITROS: ")

                        resp = float(a) / 1000
                        print("O VOLUME EM M³ É:", resp)

                        break

                    if v == '3':
                        print("\t LITRO ----> CENTÍMETRO CÚBICO: \n")

                        a = input("DIGITE O VOLUME EM LITROS: ")

                        resp = float(a) * 1000
                        print("O VOLUME EM CM³ É:", resp)

                        break

                    if v == '4':
                        print("\t MILILITRO ----> LITRO: \n")

                        a = input("DIGITE O VOLUME EM MILILITROS: ")

                        resp = float(a) / 1000
                        print("O VOLUME EM L É:", resp)

                        break

# CALCULO CONVERSÃO DE MASSAS

            if un == '5':
                print("\t MASSA: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    a = input("TONELADAS ------> KG...: [1]\n"
                              "TONELADAS ------> G....: [2]\n"
                              "TONELADAS ------> MG...: [3]\n"
                              "QUILOGRAMAS ----> T....: [4]\n"
                              "QUILOGRAMAS ----> G....: [5]\n"
                              "QUILOGRAMAS ----> MG...: [6]\n"
                              "GRAMAS ---------> T....: [7]\n"
                              "GRAMAS ---------> KG...: [8]\n"
                              "GRAMAS ---------> MG...: [9]\n"
                              "SAIR ..................: [n]\n")

                    if a == 'n':
                        a
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
                        exit()
                        break

                    if a == '1':
                        print("\t TONELADA ----> KG:\n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) * 1000
                        print("A MASSA EM KG É:", resp)
                        break

                    if a == '2':
                        print("\t TONELADA ----> G: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) * 1000000
                        print("A MASSA EM G É:", resp)
                        break

                    if a == '3':
                        print("\t TONELADA ----> MG: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) * 1000000000
                        print("A MASSA EM MG É:", resp)
                        break

                    if a == '4':
                        print("\t QUILOGRAMAS ----> T: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) / 1000
                        print("A MASSA EM T É:", resp)
                        break

                    if a == '5':
                        print("\t QUILOGRAMAS ----> G: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) * 1000
                        print(" A MASSA EM G É:", resp)
                        break

                    if a == '6':
                        print("\t QUILOGRAMAS ----> MG: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) * 1000000
                        print("A MASSA EM MG É:", resp)
                        break

                    if a == '7':
                        print("\t GRAMAS ----> T: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) / 1000000
                        print("A MASSA EM T É:", resp)
                        break

                    if a == '8':
                        print("\t GRAMAS ----> KG: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) / 1000
                        print("A MASSA EM KG É:", resp)
                        break

                    if a == '9':
                        print("\t GRAMAS ----> MG: \n")

                        c = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(c) * 1000
                        print("A MASSA EM MG É:", resp)
                        break

# CALCULO DE CONVERSÃO DE DADOS

            if un == '6':
                print("\t DADOS: \n")

                print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

                while True:
                    d = input("BIT ---------> BYTE......: [1]\n"
                              "BYTE --------> MEGABYTE..: [2]\n"
                              "BYTE --------> GIGABYTE..: [3]\n"
                              "MEGABYTE ----> BITE......: [4]\n"
                              "MEGABYTE ----> GIGABYTE..: [5]\n"
                              "MEGABYTE ----> TERABYTE..: [6]\n"
                              "GIGABYTE ----> BYTE......: [7]\n"
                              "GIGABYTE ----> MEGABYTE..: [8]\n"
                              "GIGABYTE ----> TERABYTE..: [9]\n"
                              "TERABYTE ----> MEGABYTE..: [10]\n"
                              "TERABYTE ----> GIGABYTE..: [11]\n"
                              "SAIR: \n'n'\n")

                    if d == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
                        exit()
                        break

                    if d == '1':
                        print("\t BIT ----> BYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: \n")

                        resp = float(a) * 0.125

                        print("OS DADOS EM BYTES SÃO:", resp)
                        break

                    if d == '2':
                        print("\t BYTE ----> MEGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: \n")

                        resp = float(a) * 1000000

                        print("OS DADOS EM MEGABYTE SÃO:", resp)
                        break

                    if d == '3':
                        print("\t BYTE ----> GIGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: \n")

                        resp = float(a) * 125000000

                        print("OS DADOS EM GIGABYTES SÃO:", resp)
                        break

                    if d == '4':
                        print('\t MEGABYTE ----> BYTE: \n')

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) / 100000
                        print("OS DADOS EM BYTES SÃO: ", resp)
                        break

                    if d == '5':
                        print("\t MEGABYTE ----> GIGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) / 0.008
                        print("OS DADOS EM GIGABYTES SÃO:", resp)
                        break

                    if d == '6':
                        print("\t MEGABYTE ----> TERABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) / 0.000000125

                        print("OS DADOS EM TERABYTE SÃO:", resp)
                        break

                    if d == '7':
                        print("\t GIGABYTE ----> BYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) * 125000000

                        print("OS DADOS EM BYTES SÃO:", resp)
                        break

                    if d == '8':
                        print("\t GIGABYTE ----> MEGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) * 1000

                        print("OS DADOS EM MEGABYTES SÃO:", resp)
                        break

                    if d == '9':
                        print("\t GIGABYTE ----> TERABYTE: \n")

                        a = input('DIGITE O VALOR A SER CONVERTIDO: \n')

                        resp = float(a) / 0.000125

                        print("OS DADOS EM TERABYTES SÃO:", resp)
                        break

                    if d == '11':
                        print("\t TERABYTE ----> MEGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) * 1000000

                        print("OS DADOS EM MEGABYTES SÃO:", resp)
                        break

                    if d == '12':
                        print('\t TERABYTE ----> GIGABYTE: \n')

                        a = input('DIGITE O VALOR A SER CONVERTIDO: ')

                        resp = float(a) * 1000

                        print("OS DADOS EM GIGABYTES SÃO:", resp)
                        break


                    else:
                        print("\t CARACTERE INVÁLIDO!!!\n")

                        break

            break

        break

# CALCULO DA GEOMETRIA

    if start == '7':
        print("\t GEOMETRIA: \n")

        print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

        g = input("TEOREMA DE PITÁGORAS.........: [1]\n"
                  "SENO, COSSENO E TANGENTE.....: [2]\n"
                  "ÁREAS........................: [3]\n"
                  "PERÍMETRO....................: [4]\n"
                  "SEMELHANÇA ENTRE TRIÂNGULOS..: [5]\n"
                  "SAIR.........................: [n]\n")

        if g == 'n':
            print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
            exit()

            break

        if g == '1':
            import math

            print("\t TEOREMA DE PITÁGORAS: \n")

            a = float(input("DIGITEO VALOR DO CATETO 1: "))
            b = float(input("DIGITE O VALOR DO CATETO 2: "))

            resp = math.sqrt((a * a) + (b * b))

            print("O VALOR DA HIPOTENUSA É:", resp)
            break

        if g == '2':
            import math

            print("\t SENO, COSSENO E TANGENTE: \n")

            break

# CALCULO DAS ÁREAS

        if g == '3':
            print("\t ÁREAS: \n")

            print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

            o = input("ÁREA DO QUADRADO .......: [1]\n"
                      "ÁREA DO RETÂNGULO ......: [2]\n"
                      "ÁREA DO TRIÂNGULO ......: [3]\n"
                      "ÁREA DO TRAPÉZIO .......: [4]\n"
                      "ÁREA DO CUBO ...........: [5]\n"
                      "SAIR ...................: [n]\n")

            if o == 'n':
                print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
                exit()

                break

# CALCULO DA AREA DO QUADRADO

            if o == '1':
                print("\t ÁREA DO QUADRADO: \n")

                a = input("DIGITE O VALOR DE UM DOS LADOS DO QUADRADO: ")

                resp = float(a) * float(a)

                print("A ÁREA DO QUADRADO É:", resp)

                while True:
                    a = input(usuario, "\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE [N]\n PARA SAIR\n")

                    if a == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!! \n")
                        exit()
                        break


                    elif a:
                        print("\t CARACTERE INVÁLIDO!!\n")
                        continue

                    break

# CALCULO DA AREA DO RETANGULO

            if o == '2':
                print("\t ÁREA DO RETÂNGULO: \n")

                a = input("DIGITE O VALOR DA BASE DO RETÂNGULO: ")
                b = input("DIGITE O VALOR DO LADO DO TRIÂNGULO: ")

                resp = float(a) * float(b)

                print("A ÁREA DO RETÂNGULO É:", resp)

                while True:
                    a = input(usuario, "\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE [N]\n PARA SAIR\n")

                    if a == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                        exit()

                    elif a:
                        print('\t CARACTERE INVÁLIDO!!!\n')
                        continue

                    break

# CALCULO DA AREA DO TRIANGULO

            if o == '3':
                print("\t ÁREA DO TRIÂNGULO: \n")

                a = input("DIGITE O VALOR DA BASE DO TRIÂNGULO: ")
                b = input("DIGITE O VALOR DA ALTURA DO TRIÂNGULO: ")

                resp = (float(a) * float(b)) / 2

                print("A ÁREA DO TRIÂNGULO É:", resp)

                while True:
                    a = input(usuario, "\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE [N]\n PARA SAIR\n")

                    if a == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                        exit()

                    elif a:
                        print("\t CARACTERE INVÁLIDO!!!\n")
                        continue

                    break

# CALCULO DA AREA DO TRAPEZIO

            if o == '4':
                print("\t ÁREA DO TRAPÉZIO: \n")

                a = input("DIGITE O VALOR DA BASE MAIOR DO TRAPÉZIO: ")
                b = input("DIGITE O VALOR DA BASE MENOR DO TRAPÉZIO: ")
                c = input("DIGITE O VALOR DA ALTURA DO TRAPÉZIO: ")

                resp = ((float(a) + float(b)) * float(c)) / 2

                print("A ÁREA DO TRAPÉZIO É:", resp)

                while True:
                    a = input(usuario, "\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE [N]\n PARA SAIR\n")

                    if a == 'n':
                        print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")
                        exit()


                    elif a:
                        print("\t CARACTERE INVÁLIDO!!!\n")

                        continue

                    break

# CALCULO DA AREA DO CUBO

            if o == '5':
                print("\t ÁREA DO CUBO: \n")

                a = input("DIGITE O VALOR DO LADO DO QUADRADO: ")

                resp = float(a) * 6

                print("A ÁREA DO CUBO É:", resp)
                break

# CALCULO DE FUNÇÕES

    if start == '8':
        print("\t FUNÇÕES: \n")

        print(usuario, " \t PARA CONTINUAR, SELECIONE UMA DAS SEGUINTES OPÇÕES:\n")

        a = input("DESCOBRIR O VALOR DE Y ......: [1]\n"
                  "DESCOBRIR O VALOR DE X ......: [2]\n"
                  "SAIR ........................: [n]\n")

        if a == 'n':
            print(usuario, "\t OBRIGADO POR USAR ESTE PROGRAMA!!!\n")

            exit()

            break

        if a == '1':
            print('\t VALOR DE Y: \n')

            b = input("DIGITE O VALOR DE X: ")
            c = input("DIGITE O VALOR DE B: ")

            resp = float(c) + float(b)

            print("\t O VALOR DE Y É:", resp, "\n")

            break

        if a == '2':
            print("\t VALOR DE X: \n")

            b = input("DIGITE O VALOR DE Y: ")
            c = input('DIGITE O VALOR DE B: ')

            resp = float(c) - float(b)

            print('\t O VALOR DE X É:', resp, '\n')

            break


        else:
            print("\t CARACTERE INVÁLIDO!!!\n")
            continue

        break

# CALCULO VELOCIDADE MÉDIA

    if start == '9':
        print("\t VELOCIDADE MÉDIA: \n")

        a = input('DIGITE A DISTÂNCIA PERCORRIDA: ')
        b = input("DIGITE O TEMPO GASTO (EM HORAS): ")

        resp = float(a) / float(b)

        print("\t A VELOCIDADE MÉDIA É:", resp, "\n")

# ============================================TÉRMINO DO PROGRAMA==============================================================