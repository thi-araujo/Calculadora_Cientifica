#=========================================Despertador=============================================================

#_________________________________________________________________________________________________________________

import datetime

import os

import time

import random

import webbrowser

# Se o arquivo de URL do vídeo no Youtube não existir, crie um

if not os.path.isfile("youtube_alarme_videos.txt"):

print('Criamdo "youtube_alarme_videos.txt"...')

with open("youtube_alarme_videos.txt", "w") as arquivo_alarme:
    arquivo_alarme.write("https://www.youtube.com/watch?v=35ywqydkzXM&ab_channel=Accept")

# Verificar se o usuário digitou um horário do alarme válido

def check_alarm_input(horario_do_alarme):

    if len(horario_do_alarme) == 1: # Formato hora
        if horario_do_alarme[0] < 24 and horario_do_alarme[0] >= 0:
            return True

    if len(horario_do_alarme) == 2: # Formato minutos
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
        if  check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
            except ValueError
            print("ERRO: Digite a hora no formato HH:MM ou HH:MM:SS")


# Convertento a hora do alarme de [H:M] ou [H:M:S] para segundo

    segundos_hms = [3600, 60, 1] # Numero de segundos em uma hora, minutos e segundos












