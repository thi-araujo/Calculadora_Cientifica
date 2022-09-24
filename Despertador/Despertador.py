#===============================================Despertador=============================================================

#Cabeçalho
print('=' *80)
print()
print(' '*20, 'Despertador')
print()
print('='*80)
#_________________________________________________________________________________________________________________
# Versão do script: 0.1.1r
# Data da criação: 27/07/2022

# Autor: Thiago Araujo
# O script  não foi desenvolvido por mim, apenas realizei uma pequena modificação, o autor original é hackr.io,  extraido do
# site: https://hackr.io/blog/python-projects
import datetime

import os

import time

import datetime

import os

import time

import random

import webbrowser

# Se o arquivo de URL do vídeo no Youtube não existir, entao crie um

if not os.path.isfile("youtube_alarme_videos.txt"):

print('Criamdo "youtube_alarme_videos.txt"...')

with open("youtube_alarme_videos.txt", "w") as arquivo_alarme:
    arquivo_alarme.write("https://www.youtube.com/watch?v=35ywqydkzXM&ab_channel=Accept")

# Verificar se o usuário digitou um horário do alarme válido

def check_alarm_input(horario_do_alarme):

    if len(horario_do_alarme) == 1: # Formato hora
        if horario_do_alarme[0] < 24 and horario_do_alarme[0] >= 0:
            return True

    if len(horario_do_alarme) == 2: # Formato dos minutos
        if horario_do_alarme[0] < 24 and horario_do_alarme[0] >= 0 and \
           horario_do_alarme[1] < 60 and horario_do_alarme[1] >= 0:
            return True

    elif len(horario_do_alarme) == 3:  # Formato [Hora:Minuto:Segundos]
        if horario_do_alarme[0] < 24 and horario_do_alarme[0] >= 0 and \
           horario_do_alarme[1] < 60 and horario_do_alarme[1] >= 0 and \
           horario_do_alarme[2] < 60 and horario_do_alarme[2] >= 0:
            return True
            return False

# Obter entrada do usuário para a hora do alarme

    print("Defina um horário para o alarme (Ex. 06:30 ou 18:30:00)")

while True:
    alarme_input = input(">> ")
    try:
        horario_do_alarme = [int(n) for n in alarm_input.split(":")]
        if  check_alarm_input(horario_do_alarme):
            break
        else:
            raise ValueError
            except ValueError
            print("ERRO: Digite a hora no formato HH:MM ou HH:MM:SS")


# Convertendo a hora do alarme de [H:M] ou [H:M:S] para segundo

    segundos_hms = [3600, 60, 1] # Aqui calculamos o numero de segundos em uma hora, minutos e segundos

    alarme_segundos = sum([a * b for a, b in zip(segundos_hms_hms[:len(horario_do_alarme)], horario_do_alarme)])

# Obtém a hora atual do dia em segundos

    agora = datetime.datetime.now()
    hora_atual_segundos = sum([a * b for a, b in zip(segundos_hms, [now.hour, now.minute, now.second])])

# Calcula o número de segundos até o alarme disparar

    segundos_diferenca_tempo = alarme_segundos - hora_atual_segundos


# Se a diferença horária for negativa, defina o alarme para o dia seguinte
        if segundos_diferenca_tempo < 0:
            segundos_diferenca_tempo += 86400 #Numero de segundos em um dia

# Mostra  a quantidade de tempo até o alarme disparar
            print("Alarme definido para disparar em %s" datetime.timedelta(segundos_diferenca_tempo))

# Dormir ate o alarme disparar

            time.sleep(segundos_diferenca_tempo)

#Tempo para o alarme disparar
        print("Acordar")

# Carregar lista de possíveis URLs de vídeo do youtube

    with open("youtube_alarme_videos.txt", "r") as arquivo_alarme:
    videos = arquivo_alarme.readline()

# Abrir um vídeo aleatório da lista de videos do youtube
    webbrowser.open(random.choice(videos))









