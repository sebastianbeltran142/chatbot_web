import random

def agregar_opciones_adicionales(respuesta):
    opciones_adicionales = [
        "Espero que esta respuesta sea de utilidad.",
        "Si requieres alguna ayuda o pregunta, házmela saber.",
        "¿Hay algo más en lo que pueda asistirte?",
        "Estoy aquí para ayudarte con cualquier otra consulta que tengas.",
        "No dudes en preguntar si necesitas más información."
    ]
    opcion_adicional = random.choice(opciones_adicionales)
    return f"{respuesta} {opcion_adicional}"
