import requests

RECAPTCHA_SECRET_KEY = '6LcQOQwqAAAAAIiEDhZ0jR_PG8HojjNA0Z0r4s3B'  # Reemplaza con tu clave secreta de reCAPTCHA

def validar_recaptcha(captcha_response):
    """Valida el reCAPTCHA con la clave secreta."""
    recaptcha_validation = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={'secret': RECAPTCHA_SECRET_KEY, 'response': captcha_response}
    ).json()
    
    return recaptcha_validation.get('success', False)
