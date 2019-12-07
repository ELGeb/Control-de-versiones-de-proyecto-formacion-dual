# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:14:15 2019

@author: DULCE
"""

import pyaudio
import wave

#EJEMPLO DE GRABADORA DE SONIDO CON "pyaudio".
#IMPORTAMOS LIBRERIAS NECESARIAS
import pyaudio
import wave
"ESTE PROGRMA GRABA UN AUDIO DE 10s Y LO GUARDA"

#DEFINIMOS PARAMETROS
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
duracion=10
name= input("Ingresa el nombre: ")
archivo= name + ".wav"

#INICIAMOS "pyaudio"
audio=pyaudio.PyAudio()

#INICIAMOS GRABACIÓN
stream=audio.open(format=FORMAT,channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("grabando...")
frames=[]

for i in range(0, int(RATE/CHUNK*duracion)):
    data=stream.read(CHUNK)
    frames.append(data)
print("grabación terminada")

#DETENEMOS GRABACIÓN
stream.stop_stream()
stream.close()
audio.terminate()

#CREAMOS/GUARDAMOS EL ARCHIVO DE AUDIO
waveFile = wave.open(archivo, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()