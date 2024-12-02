import os
import logging
from datetime import datetime, timedelta

from config import EMAIL_TO, EMAIL_CC, EMAIL_USERNAME, EMAIL_FICHA

# Funcao para gerar o titulo
def generate_title(user_name):
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_period = today

    start_date = start_of_week.strftime("%d/%m/%Y")
    end_date = end_of_period.strftime("%d/%m/%Y")
    
    title = f"Ficha de Trabalho {start_date} a {end_date} - {user_name}"
    return title

# Funcao para gerar o comando do Thunderbird
def generate_thunderbird_command(to_email, cc_email, user_name, file_path):
    title = generate_title(user_name)
    command = (
        f'thunderbird -compose "to=\'{to_email}\',cc=\'{cc_email}\','
        f'subject=\'{title}\',body=\'Segue em anexo ficha trabalho\','
        f'attachment=\'{file_path}\'"'
    )
    return command

def create_email_ficha():
    # Exemplo de uso
    to_email = EMAIL_TO
    cc_email = EMAIL_CC
    user_name = EMAIL_USERNAME
    file_path = EMAIL_FICHA

    command = generate_thunderbird_command(to_email, cc_email, user_name, file_path)
    print(command)

    # Executar o comando
    os.system(command)