# importando a biblioteca
import speech_recognition as sr
import os


# import required modules
import subprocess


# importando o audio da pasta "audio"
audioPath = "./audio"
for dir, subDir, file in os.walk(audioPath):
    for file in file:

        # instanciando e limitando o threshold
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 10

        # converte de mp3 para wav
        src = os.path.join(os.path.realpath(dir), file)
        subprocess.call(['ffmpeg', '-i', src,
                         'teste.wav'])
        # converted = AudioSegment.from_mp3("audio.mp3")
        # converted.export(file[:-4], format="wav")
        # guarda o audio em uma variável
        # audio = sr.AudioFile(os.path.join(os.path.realpath(dir), wav))
        # print(converted)
        # try:
        #     with audio as source:
        #         audio = recognizer.record(source)

        #     # transformar o audio em texto
        #     text = recognizer.recognize_google(
        #         audio_data=audio, language="Pt-Br")
        # except:
        #     text = "Ocorreu um erro"

        # # salvar o texto em um arquivo txt
        # textFile = open("transcrições.txt", "a", encoding="UTF-8")
        # textFile.write(
        #     "\n"
        #     + "\n"
        #     + "--------------------"
        #     + file
        #     + "--------------------"
        #     + "\n"
        #     + "\n"
        # )
        # textFile.write(text + "\n"
        #                + "\n")
        # textFile.close()

        # print("Concluido")
