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
