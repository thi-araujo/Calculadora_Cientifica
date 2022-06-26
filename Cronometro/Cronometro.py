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

t = input("Digite o tempo em segundos: ")