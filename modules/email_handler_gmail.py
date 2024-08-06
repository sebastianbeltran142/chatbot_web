import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def enviar_correo_gmail(user_email, conversation, gmail_user, gmail_password, corporate_email, logo_path):
    try:
        print("Iniciando el envío de correo...")  # Monitoreo
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = f"{user_email}, {corporate_email}"
        msg['Subject'] = 'Historial de Conversación del Chatbot'

        # Formatear la conversación en HTML
        formatted_conversation = "<br>".join(conversation.split("\n"))
        html = f"""
        <html>
        <body>
            <p>Hola, a continuación te envío la interacción del usuario y el chatbot mediante el siguiente mensaje:</p>
            <div style="margin-bottom: 20px;">
                {formatted_conversation}
            </div>
            <p>Uno de nuestros asesores estará encantado de contactarlo por este medio. Nos puedes contactar por este medio de celular para el seguimiento de tu caso o duda: 3110011011.</p>
            <p>Estamos para servirte.</p>
            <p>Cordialmente,</p>
            <p>Equipo de la empresa</p>
            <p>Dirección: [Tu dirección aquí]</p>
            <p>Teléfono: [Tu teléfono aquí]</p>
            <img src="cid:logo-final" style="width: 200px;">
        </body>
        </html>
        """
        
        msg.attach(MIMEText(html, 'html'))

        # Adjuntar el logo de la empresa
        with open(logo_path, 'rb') as img:
            logo = MIMEImage(img.read())
            logo.add_header('Content-ID', '<logo_empresa>')
            msg.attach(logo)

        print(f"Preparando servidor SMTP...")  # Monitoreo
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        print(f"Login exitoso con el servidor SMTP...")  # Monitoreo

        text = msg.as_string()
        server.sendmail(gmail_user, [user_email, corporate_email], text)
        server.quit()

        print("Correo enviado exitosamente.")  # Monitoreo
        return "Correo enviado exitosamente."
    except Exception as e:
        error_message = f"Error al enviar el correo: {str(e)}"
        print(error_message)  # Monitoreo
        return error_message

# Ejemplo de uso
# enviar_correo_gmail("usuario@example.com", "Esta es una conversación\nde prueba.", "tu_correo@gmail.com", "tu_contraseña", "correo_corporativo@example.com", "/path/to/static/logo-empresa.png")
