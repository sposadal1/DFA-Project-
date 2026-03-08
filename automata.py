# Función de transición 
def funcion_transicion(estado, simbolo):
    if estado == "0137":
        if simbolo == "a": return "247"
        if simbolo == "b": return "8"
    
    elif estado == "247":
        if simbolo == "a": return "7"
        if simbolo == "b": return "58"
        
    elif estado == "7":
        if simbolo == "a": return "7"
        if simbolo == "b": return "8"
        
    elif estado == "58":
        if simbolo == "b": return "68"
        
    elif estado == "68":
        if simbolo == "b": return "8"
        
    elif estado == "8":
        if simbolo == "b": return "8"
        
    return None # Retorna None si no hay transición válida

# Verificación
def verificar_cadena(cadena):
    estado_inicial = "0137"
    estados_aceptacion = ("247", "58", "68", "8")
    estado = estado_inicial
    
    for simbolo in cadena:
        estado = funcion_transicion(estado, simbolo)
        if estado is None:
            return False 
            
    return estado in estados_aceptacion

# Validacion
def validar_cadena():
    error = ("\n\t¡Error!.." + 
             "\n\tSolo se aceptan cadenas formadas por" +
             "\n\t el alfabeto {a, b}" + "\n\tReingrese por favor..")
    
    while True:
        cadena = input("\nIngrese cadena a verificar ({a, b}) (o 's' para salir): ")
        
        if cadena.lower() == "s":
            return "s"
        
        # Validamos que cada caracter pertenezca al alfabeto
        es_valida = True
        for simbolo in cadena:
            if simbolo not in ("a", "b"):
                es_valida = False
                print(error)
                break
        
        if es_valida:
            return cadena

def main():
    
    cadena = validar_cadena()
    while cadena != "s":
        resultado = verificar_cadena(cadena)
        
        if resultado:
            print("\n\tLa cadena fue aceptada.")
        else:
            print("\n\tLa cadena fue rechazada.")
            
        cadena = validar_cadena()
    
    input("\n\tPresione <Enter> para finalizar..")

if __name__ == "__main__":
    main()