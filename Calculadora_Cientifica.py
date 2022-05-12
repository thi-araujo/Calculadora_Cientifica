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

        print("\t EQUAÇÃOD DE SEGUNDO GRAU: \n")
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

                a = input("Digite um valor para a: ")
                b = input("Digite um valor para b: ")

                resp = None

                resp = float(a) ** float(b)

                if resp:
                    print("\t RESULTADO: {0}".format(resp))

                    break

            if st == '2':
                print("\t RADIAÇÃO: \n")

            import math

            raiz = float(input("Digite um valor: "))
            radical = float(input("Digite o radical: "))

            if radical == '2':
                raiz2 = raiz ** (1 / 2)
                print("A raiz quadrada é:", raiz2)

            if radical == '3':
                raiz3 = raiz ** (1 / 3)
                print(usuario, "A raiz cúbica é:", raiz3)

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

                        v1 = input("DIGITEO COMPRIMENTO INICIAL: ")

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

                        v1 = input("DIGITE O COMPRIMENTOEM MILIMETROS: ")

                        resp = float(v1) / 10000
                        print(" COMPRIMENTO É:", resp)

                        break

                    if a == '6':
                        print("\t MM ----> CM\n")

                        import math

                        v1 = input("DIGITEO COMPRIMENTO EM MILIMETROS: ")

                        resp = float(v1) / 100
                        print("O COMPRIMENTO É:", resp)

                        break