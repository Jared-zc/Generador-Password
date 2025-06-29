import random
import string

def interpretar_respuesta(respuesta):
    """Interpreta diversas formas de 'sí'"""
    return respuesta.strip().lower() in ["sí", "si"]

def generar_contraseña(longitud, incluir_numeros, incluir_simbolos, incluir_mayusculas, incluir_minusculas):
    caracteres = ""
    
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
        
    if not caracteres:
        return None # No se ha seleccionado ningún tipo de carácter
    
    return '' .join(random.choice(caracteres) for _ in range(longitud))
        
def main():
    print("Generador de Contraseñas Personalizado")
    
    incluir_numeros = interpretar_respuesta(input("¿Desea Incluir Números? (sí/no): "))
    incluir_simbolos = interpretar_respuesta(input("¿Desea incluir símbolos? (sí/no): "))
    incluir_mayusculas = interpretar_respuesta(input("¿Desea incluir letras mayúsculas? (sí/no): "))
    incluir_minusculas = interpretar_respuesta(input("¿Desea incluir letras minúsculas? (sí/no): "))
    
    if not any([incluir_numeros, incluir_simbolos, incluir_mayusculas, incluir_minusculas]):
        print("Error: No se ha seleccionado ningún tipo de carácter para generar la contraseña.")
        return
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser mayor que cero.")
            return
    except ValueError:
        print("Error: La longitud debe ser un número entero.")
        return

    contraseña = generar_contraseña(longitud, incluir_numeros, incluir_simbolos, incluir_mayusculas, incluir_minusculas)
    
    if contraseña:
        print(f"\nContraseña generada: {contraseña}")
    else:
        print("No se pudo generar la contraseña. Verifique las opciones seleccionadas.")

if __name__ == "__main__":
    main()