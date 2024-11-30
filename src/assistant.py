import logging
from gtts import gTTS
import playsound
import os
import speech_recognition as sr
from datetime import datetime

# Configurar o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='../log/assistente.log', filemode='w', encoding='utf-8')

def speak(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    tts.save(filename)
    
    try:
        playsound.playsound(filename, True)
    except Exception as e:
        logging.error(f"Erro ao reproduzir áudio: {e}")
    
    try:
        os.remove(filename)
    except Exception as e:
        logging.error(f"Erro ao remover o arquivo: {e}")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logging.info("Escutando...")
         # Ajustar o tempo de pausa antes de considerar que a fala terminou
        r.pause_threshold = 1.0 
        # Limite de tempo para frase completa
        r.phrase_time_limit = 20
        audio = r.listen(source)
        try:
            said = r.recognize_google(audio, language='pt-BR')
            logging.info(f"Voce falou: {said}")
            return said.lower()
        except Exception as e:
            logging.error(f"Desculpe, Nao entendi: {e}")
            return ""

def tell_time(command):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    logging.info("Informando as horas:")
    speak(f"Agora são {current_time}")

def detectWakeWord(command):
    wake_words = ["ori", "ore", "orei", "orey", "ory", "oree", "orio", "oreo", "orion"]
    for word in wake_words:
        if word in command:
            return True
    return False

def detectCommand(command_list, command):
    return any(keyword in command.lower() for keyword in command_list)

def exit_assistant():
    speak("Até logo!")
    exit()
