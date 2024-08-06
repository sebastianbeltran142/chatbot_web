# modules/math.py

def evaluar_operacion(pregunta, operacion):
    try:
        resultado = eval(operacion)
        mensaje_respuesta = f"La operación matemática de {pregunta} es {resultado}. \n\nEspero sea de utilidad"
        return mensaje_respuesta
    except Exception as e:
        return f"Error al evaluar la operación: {str(e)}"
