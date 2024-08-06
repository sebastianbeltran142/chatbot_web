# modules/email_handler.py
from flask_mail import Mail, Message

def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.office365.com'  # o 'smtp.gmail.com' para Gmail
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'tu_email@dominio.com'
    app.config['MAIL_PASSWORD'] = 'tu_contraseña'
    app.config['MAIL_DEFAULT_SENDER'] = 'tu_email@dominio.com'

    mail = Mail(app)
    return mail

def enviar_correo(mail, email_destino, conversation, user_email):
    msg = Message('Historial de Conversación del Chatbot', recipients=[email_destino, user_email])
    msg.body = '\n'.join([f"{entry['nombre']}: {entry['mensaje']}" for entry in conversation])
    mail.send(msg)
