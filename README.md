Bem  Vindo: Assistente pessoal em Python.



# Comando para dar Tail no log do Windows
Get-Content .\assistente.log -Wait -Encoding UTF8

# Comando para gerar o executavel com Icon
pyinstaller --onefile --icon=.\assets\clean-orion.ico .\src\main.py

# O Executava precisa criar um arquivo de log




pip install pyinstaller

# Assistente Pessoal

Este é um projeto de assistente pessoal desenvolvido em Python, que utiliza reconhecimento de voz e síntese de fala para interagir com o usuário.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

## Instalação

Antes de executar o projeto, certifique-se de que você tenha o Python instalado em sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

### Dependências

Este projeto depende das seguintes bibliotecas Python:

- `logging`
- `gtts`
- `playsound`
- `os`
- `speech_recognition`
- `datetime`
- `webbrowser`

### Instalação das Dependências

Para instalar as dependências necessárias, você pode utilizar o arquivo `requirements.txt`. Primeiramente, crie um arquivo `requirements.txt` com o seguinte conteúdo:

```plaintext
gtts==2.2.4
playsound==1.2.2
SpeechRecognition==3.8.1
```

### Em seguida, execute o seguinte comando para instalar todas as dependências listadas:

pip install -r requirements.txt

# Para executar o assistente pessoal, utilize o arquivo main.py. Ele inicializa o assistente e começa a escutar os comandos de voz.

python main.py

### Comandos Suportados

Horas: Informa a hora atual.
Sair: Encerra o assistente.
Consulta: Abre uma consulta no navegador com base no número informado.
Email: Inicia a criação de um novo e-mail.