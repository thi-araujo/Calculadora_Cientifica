import time

# Função do cronometro:

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:2d}:{:02d}' .format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print("Lift off")

# Solicite ao usuário para digitar o período de contagem regressiva em segundos:
t = input("Digite o tempo em segundos: ")

# Chamada da função
countdown(int(t))