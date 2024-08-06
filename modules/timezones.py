from datetime import datetime
import pytz
import re

def obtener_hora_local():
    now = datetime.now()
    hora_actual = now.strftime('%H:%M:%S del día %d-%m-%Y')
    return f"La hora local es {hora_actual}"

def obtener_hora(pais):
    # Eliminar signos de interrogación y exclamación
    pais = re.sub(r'[?!]', '', pais).strip().lower()

    zonas_horarias = {
        'españa': 'Europe/Madrid',
        'mexico': 'America/Mexico_City',
        'argentina': 'America/Argentina/Buenos_Aires',
        'colombia': 'America/Bogota',
        'peru': 'America/Lima',
        'chile': 'America/Santiago',
        'brasil': 'America/Sao_Paulo',
        'francia': 'Europe/Paris',
        'alemania': 'Europe/Berlin',
        'japon': 'Asia/Tokyo',
        'china': 'Asia/Shanghai',
        'india': 'Asia/Kolkata',
        'australia': 'Australia/Sydney',
        'estados unidos': 'America/New_York',
        'venezuela': 'America/Caracas'
    }

    zona_horaria = zonas_horarias.get(pais)
    if zona_horaria:
        zona = pytz.timezone(zona_horaria)
        hora_local = datetime.now(zona)
        return f"La hora en {pais} es {hora_local.strftime('%H:%M:%S del día %d-%m-%Y')}"
    else:
        return "No se pudo encontrar la zona horaria para el país especificado."

# Ejemplo de uso:
# print(obtener_hora_local())
# print(obtener_hora('españa'))
