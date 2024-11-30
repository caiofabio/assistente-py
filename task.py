import logging
import webbrowser
from assistant import speak
from config import TASK_URL_BASE

def open_task(command):
    try:
        task_number = command.split("consulta")[1].strip()
        url = f"{TASK_URL_BASE}{task_number}"
        webbrowser.open(url)
        speak(f"Abrindo consulta {task_number}")
    except IndexError:
        logging.error("Número da consulta não encontrado no comando.")
        speak("Desculpe, não consegui encontrar o número da consulta.")
