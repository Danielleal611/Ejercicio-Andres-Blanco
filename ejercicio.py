def calcular_precio_boletas():
    
    sala = input("Ingrese el tipo de sala (Dinamix, 3D o 2D): ")
    numero_boletas = int(input("Ingrese el número de boletas que desea comprar: "))
    hora = input("Ingrese la hora de la función (pico o no_pico): ")
    medio_pago = input("Ingrese el medio de pago (tarjeta o otro): ")
    reserva = input("¿Desea hacer una reserva? (si o no): ")
    
    
    if sala == "Dinamix":
        precio_sala = 18800
    elif sala == "3D":
        precio_sala = 15500
    elif sala == "2D":
        precio_sala = 11300
    else:
        print("Tipo de sala inválido.")
        return None
    
    
    descuento_boletas = 0
    recargo_reserva = 0
    descuento_pago = 0
    aumento_pico = 0
    
    if hora == "no_pico":
        descuento_hora = 0.1
        if numero_boletas >= 3:
            descuento_boletas = 500
    elif hora == "pico":
        if sala == "Dinamix":
            aumento_pico = 0.5
        else:
            aumento_pico = 0.25
    else:
        print("Hora inválida.")
        return None
    
    if medio_pago == "tarjeta":
        descuento_pago = 0.05
    
    if reserva == "si":
        recargo_reserva = 2000 * numero_boletas
        
    
    precio_total = (precio_sala * (1 + aumento_pico) * (1 - descuento_hora) 
                    - descuento_boletas + recargo_reserva) * (1 - descuento_pago)
    
   
    print("El precio total de las boletas es:", precio_total)
    return precio_total

calcular_precio_boletas()