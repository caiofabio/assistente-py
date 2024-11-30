import logging
from assistant import speak, get_audio, detectWakeWord, detectCommand, tell_time, exit_assistant
from task import open_task

def email(command):
    speak(f"Criando um novo e-mail, qual o assunto?")

# Dicionário de comandos e suas palavras-chave e funções associadas
commands = {
    "time": (["horas", "time"], tell_time),
    "exit": (["sair", "exit", "quit"], exit_assistant),
    "task": (["consulta", "task"], open_task),
    "email": (["email", "e-mail", "i-mail"], email)
}

def main():    
    logging.info("Iniciando assistente pessoal...")
    speak("Olá! Me chamo Órion, Como posso ajudar?")

    while True:
        logging.info("Escutando comandos...")
        command = get_audio()
        
        if not detectWakeWord(command):
            continue

        logging.info(f"Palavra de ativacao detectada: {command}")
        for key, (keywords, func) in commands.items():
            if detectCommand(keywords, command):
                func(command)
                break

if __name__ == "__main__":
    main()
