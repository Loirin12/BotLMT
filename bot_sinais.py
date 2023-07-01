import time
import datetime
from telegram import Bot
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater
from telegram.ext import JobQueue

TOKEN = '6110959072:AAEa3Dx89yDa8lf06D5s1rBN1RFzTrqMoVw'

def enviar_sinal():
    # Defina o seu próprio padrão de sinal aqui
    sinal = "Meu padrão personalizado de sinal"

    # Inicializa o bot do Telegram
    bot = Bot(token=6110959072:AAEa3Dx89yDa8lf06D5s1rBN1RFzTrqMoVw)

    # ID do chat ou grupo onde o sinal será enviado
    chat_id = '-997689919'

    # Cria o botão "Aposte Aqui" com o link da plataforma
    plataforma_url = "https://mobile.apostaganha.bet/#/cassino/mines"  # Substitua pelo link da plataforma desejada
    botao_aposte_aqui = InlineKeyboardButton(text="Aposte Aqui", url=plataforma_url)

    # Cria o layout do teclado inline
    keyboard = InlineKeyboardMarkup([[botao_aposte_aqui]])

    # Envia o sinal para o chat ou grupo do Telegram com o botão
    message = bot.send_message(chat_id=chat_id, text=sinal, reply_markup=keyboard)

    print("Sinal enviado para o Telegram!")

    # Agenda o envio da mensagem de expiração após dois minutos
    job_queue = JobQueue(bot)
    job_queue.run_once(enviar_mensagem_expiracao, 120, context=message)

def enviar_mensagem_expiracao(context):
    message = context.job.context
    chat_id = message.chat_id
    bot = context.job.context.bot

    # Envia a mensagem de expiração do sinal
    mensagem_expiracao = "O sinal expirou."
    bot.send_message(chat_id=chat_id, text=mensagem_expiracao)

def main():
    
    # Inicializa o bot e o job_queue
    updater = Updater(token=TOKEN, use_context=True)
    job_queue = updater.job_queue

    # Agenda o envio do sinal a cada 5 minutos
    job_queue.run_repeating(enviar_sinal, interval=300, first=0)

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot em execução
    updater.idle()

# Arquivo bot_sinais.py

# Importe as informações de login do arquivo login_info.py
from login_info import username, password

# Use as informações de login no seu código
def login():
    # Código para fazer o login usando as informações de username e password
    print("Fazendo login com o nome de usuário:", username)
    print("Senha:", password)

# Chame a função de login
login()

if __name__ == '__main__':
    main()
    
