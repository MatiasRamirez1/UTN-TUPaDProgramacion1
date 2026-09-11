### EJERCICIO 1 ###

print("\nEJERCICIO 1\n-------------------\n")

print("Este es un simulador de compras.")

totalSinDescuentosEj1 = 0
totalConDescuentosEj1 = 0
ahorroEj1 = 0
promedioEj1 = 0
nombreEj1 = input("Ingrese su nombre: ").strip()

while True:
    if nombreEj1 == "":
        nombreEj1 = input("Ingresó un carácter vacío. Por favor, intente nuevamente e ingrese su nombre correctamente: ").strip()
        continue
    if nombreEj1.isalpha() == False:
        nombreEj1 = input("Ingresó un carácter numérico. Por favor, intente nuevamente e ingrese sólo letras: ").strip()
        continue
    break

productosEj1 = input("Ingrese la cantidad de productos que desea comprar: ").strip()

while True:
    if "." in productosEj1 or "," in productosEj1:
        productosEj1 = input("Ingresó un número decimal. Por favor, intente nuevamente e ingrese un número entero mayor a 0: ").strip()
        continue
    if productosEj1 == "":
        productosEj1 = input("Ingresó un carácter vacío. Por favor, intente nuevamente e ingrese un número entero mayor a 0: ").strip()
        continue
    if "-" in productosEj1:
        productosEj1 = input("Ingresó un número negativo. Por favor, intente nuevamente e ingrese un número entero mayor a 0: ").strip()
        continue    
    if productosEj1.isdigit() == False:
        productosEj1 = input("Ingresó un carácter no numérico. Por favor, intente nuevamente e ingrese un número mayor a 0: ").strip()
        continue
    productosEj1 = int(productosEj1)
    if productosEj1 <= 0:
        productosEj1 = input("Por favor, intente nuevamente e ingrese un número de productos positivo mayor a 0: ").strip()
        continue
    break

for i in range(productosEj1):
    precioEj1 = input(f"Ingrese el precio del producto {i+1}: ").strip()

    while True: 
        if "." in precioEj1 or "," in precioEj1:
            precioEj1 = input("Ingresó un número decimal. Por favor, intente nuevamente e ingrese un número entero positivo: ").strip()
            continue
        if precioEj1 == "":
            precioEj1 = input("Ingresó un carácter vacío. Por favor, intente nuevamente e ingrese un número entero positivo: ").strip()
            continue
        if "-" in precioEj1:
            precioEj1 = input("Ingresó un número negativo. Por favor, intente nuevamente e ingrese un número entero positivo: ").strip()
            continue    
        if precioEj1.isdigit() == False:
            precioEj1 = input("Ingresó un carácter no numérico. Por favor, intente nuevamente e ingrese un número entero positivo: ").strip()
            continue
        precioEj1 = int(precioEj1)
        if precioEj1 <= 0:
            precioEj1 = input("Por favor, intente nuevamente e ingrese un número de productos positivo mayor a 0: ").strip()
            continue
        break

    totalSinDescuentosEj1 += precioEj1 

    descuentoEj1 = input(f"¿Posee algun descuento para el producto {i+1}? (s/n): ")

    while True:
        if descuentoEj1 != "s" and descuentoEj1 != "n" and descuentoEj1 != "S" and descuentoEj1 != "N":
            print("Debe indicar si posee o no un descuento, ingrese las letras 's' para Sí o 'n' para No.")
            descuentoEj1 = input(f"¿Posee algun descuento para el producto {i+1}? (s/n): ")
            continue
        break

    
    if descuentoEj1 == "s":
        ahorroEj1 += precioEj1 * 0.1
        precioEj1 = precioEj1 * 0.9

    totalConDescuentosEj1 += precioEj1

promedioEj1 = float(totalConDescuentosEj1 / productosEj1)

print(f"\n===================================")
print("         LISTA DE COMPRAS")
print("===================================")

print(f"Nombre                       : {nombreEj1}")
print(f"Total sin descuentos         : $ {totalSinDescuentosEj1}")
print(f"Total con descuentos         : $ {totalConDescuentosEj1}")
print(f"Ahorro                       : $ {ahorroEj1}")
print(f"Promedio por producto        : $ {promedioEj1:.2f}")

print("-----------------------------------")


### EJERCICIO 2 ###


usuarioCorrectoEj2 = "alumno"
claveCorrectaEj2 = "python123"
contadorIntentosEj2 = 0
accesoEj2 = False

while contadorIntentosEj2 <= 3:

    usuarioIngresadoEj2 = input("Ingrese su usuario: ")
    claveIngresadaEj2 = input("Ingrese su clave: ")

    if usuarioCorrectoEj2 != usuarioIngresadoEj2 or claveCorrectaEj2 != claveIngresadaEj2:
        print("\nError. Credenciales inválidas.")
        print(f"Intentos: {contadorIntentosEj2 + 1} / 3.\n")
        contadorIntentosEj2 += 1
    else:
        accesoEj2 = True
        print("\n=================\nAcceso concedido.\n=================\n")
        break

    if contadorIntentosEj2 == 3:
        print("=========================================================\nCuenta bloqueada por superar el número máximo de intentos.\n=========================================================\n")
        break

while accesoEj2 == True:

    print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir\n")

    while True:
        opcionesMenuEj2 = input("Ingrese la opción deseada: ").strip()

        if opcionesMenuEj2 == "":
            print("Error, ingresó un caracter vacío.")
            continue

        if opcionesMenuEj2.isdigit() == False:
            print("Error, ingresó un caracter no numérico.")
            continue

        opcionesMenuEj2 = int(opcionesMenuEj2)

        if not 1 <= opcionesMenuEj2 <= 4:
            print("Error, ingrese un número en el rango 1-4.")
            continue

        break

    if opcionesMenuEj2 == 1:
        print("\n================================\nEstado de inscripción: INSCRIPTO.\n================================\n")
    elif opcionesMenuEj2 == 2:
        while True:
            nuevaClaveEj2 = input("Ingrese su nueva clave (al menos 6 caracteres): ")
            if len(nuevaClaveEj2) < 6:
                print("Error, la clave debe tener como mínimo 6 caracteres.")
                continue
            else:
                print("Clave modificada con éxito.")
                claveCorrectaEj2 = nuevaClaveEj2
                break
    elif opcionesMenuEj2 == 3:
        print("\n======================\nPersevera y triunfarás.\n======================\n")
    else:
        break


### EJERCICIO 3 ###

turnoLunes1 = ""
turnoLunes2 = ""
turnoLunes3 = ""
turnoLunes4 = ""
turnoMartes1 = ""
turnoMartes2 = ""
turnoMartes3 = ""

while True:
    nombreEj3 = input("Ingrese su nombre: ")
    if not nombreEj3.isalpha():
        print("Error, ingrese solo letras.")
        continue
    else:
        break


while True:
    print("\nElija una de las siguientes opciones:")
    print("""        1. Reservar turno
        2. Cancelar turno (por nombre)
        3. Ver agenda del día
        4. Ver resumen general
        5. Cerrar sistema\n
    """)
    opcionesEj3 = input("Ingrese la opción deseada: ").strip()

    if opcionesEj3 == "":
        print("Error, ingresó un caracter vacío.")
        continue

    if opcionesEj3.isdigit() == False:
        print("Error, ingresó un caracter no numérico.")
        continue

    opcionesEj3 = int(opcionesEj3)

    if not 1 <= opcionesEj3 <= 5:
        print("Error, ingrese un número en el rango 1-5.")
        continue

    if opcionesEj3 == 1:

        while True:
            diaTurnoEj3 = input("Elija el día para reservar un turno (1 = Lunes o 2 = Martes): ")
            if diaTurnoEj3 == "":
                print("Error, ingresó un caracter vacío.")
                continue
            
            if diaTurnoEj3.isdigit() == False:
                print("Error, ingresó un caracter no numérico.")
                continue
            
            diaTurnoEj3 = int(diaTurnoEj3)
            
            if not 1 <= diaTurnoEj3 <= 2:
                print("Error, ingrese los números 1 para reservar un turno el día Lunes o 2 para Martes.")
                continue
            
            break

        while True:
            pacienteEj3 = input("Ingrese el nombre del paciente: ")
            if not pacienteEj3.isalpha():
                print("Error, ingrese solo letras.")
                continue
            else:
                break

        if diaTurnoEj3 == 1:
            if pacienteEj3 == turnoLunes1 or pacienteEj3 == turnoLunes2 or pacienteEj3 == turnoLunes3 or pacienteEj3 == turnoLunes4:
                print("El paciente ya tiene un turno agendado este día.")
                continue
            elif turnoLunes1 == "":
                turnoLunes1 = pacienteEj3
                print("Turno agendado el día lunes. Primer turno.")
                continue
            elif turnoLunes2 == "":
                turnoLunes2 = pacienteEj3
                print("Turno agendado el día lunes. Segundo turno.")
                continue
            elif turnoLunes3 == "":
                turnoLunes3 = pacienteEj3
                print("Turno agendado el día lunes. Tercer turno.")
                continue
            elif turnoLunes4 == "":
                turnoLunes4 = pacienteEj3
                print("Turno agendado el día lunes. Cuarto turno.")
                continue
            else:
                print("No hay turnos disponibles el día lunes.")
                continue
        elif diaTurnoEj3 == 2:
            if pacienteEj3 == turnoMartes1 or pacienteEj3 == turnoMartes2 or pacienteEj3 == turnoMartes3:
                print("El paciente ya tiene un turno agendado este día.")
                continue
            elif turnoMartes1 == "":
                turnoMartes1 = pacienteEj3
                print("Turno agendado el día martes. Primer turno.")
                continue
            elif turnoMartes2 == "":
                turnoMartes2 = pacienteEj3
                print("Turno agendado el día martes. Segundo turno.")
                continue
            elif turnoMartes3 == "":
                turnoMartes3 = pacienteEj3
                print("Turno agendado el día martes. Tercer turno.")
                continue
            else:
                print("No hay turnos disponibles el día martes.")
                continue

    elif opcionesEj3 == 2:

        while True:
            cancelarTurnoEj3 = input("Elija el día para cancelar un turno (1 = Lunes o 2 = Martes): ")
            if cancelarTurnoEj3 == "":
                print("Error, ingresó un caracter vacío.")
                continue
            
            if cancelarTurnoEj3.isdigit() == False:
                print("Error, ingresó un caracter no numérico.")
                continue
            
            cancelarTurnoEj3 = int(cancelarTurnoEj3)
            
            if not 1 <= cancelarTurnoEj3 <= 2:
                print("Error, ingrese los números 1 para cancelar un turno el día Lunes o 2 para Martes.")
                continue
            
            break

        while True:
            pacienteEj3 = input("Ingrese el nombre del paciente: ")
            if not pacienteEj3.isalpha():
                print("Error, ingrese solo letras.")
                continue
            else:
                break
            
        if cancelarTurnoEj3 == 1:
            if pacienteEj3 == turnoLunes1:
                turnoLunes1 = ""
                print("Turno 1 del día lunes cancelado.")
            elif pacienteEj3 == turnoLunes2:
                turnoLunes2 = ""
                print("Turno 2 del día lunes cancelado.")
            elif pacienteEj3 == turnoLunes3:
                turnoLunes3 = ""
                print("Turno 3 del día lunes cancelado.")
            elif pacienteEj3 == turnoLunes4:
                turnoLunes4 = ""
                print("Turno 4 del día lunes cancelado.")
            else:
                print(f"El paciente {pacienteEj3} no tiene un turno agendado el día Lunes.")
        elif cancelarTurnoEj3 == 2:
            if pacienteEj3 == turnoMartes1:
                turnoMartes1 = ""
                print("Turno 1 del día martes cancelado.")
            elif pacienteEj3 == turnoMartes2:
                turnoMartes2 = ""
                print("Turno 2 del día martes cancelado.")
            elif pacienteEj3 == turnoMartes3:
                turnoMartes3 = ""
                print("Turno 3 del día martes cancelado.")
            else:
                print(f"El paciente {pacienteEj3} no tiene un turno agendado el día Martes.")

    elif opcionesEj3 == 3:

        print("\n============\n   TURNOS\n============\n")
        # print(f"Lunes:\n  -Turno 1: {turnoLunes1}\n  -Turno 2: {turnoLunes2}\n  -Turno 3: {turnoLunes3}\n  -Turno 4: {turnoLunes4}\n")
        # print(f"Martes:\n  -Turno 1: {turnoMartes1}\n  -Turno 2: {turnoMartes2}\n  -Turno 3: {turnoMartes3}\n")

        print("Lunes:")
        if turnoLunes1 != "":
            print(f"     -Turno 1: {turnoLunes1}.")
        else:
            print("     -Turno 1: Libre.")
        if turnoLunes2 != "":
            print(f"     -Turno 2: {turnoLunes2}.")
        else:
            print("     -Turno 2: Libre.")
        if turnoLunes3 != "":
            print(f"     -Turno 3: {turnoLunes3}.")
        else:
            print("     -Turno 3: Libre.")
        if turnoLunes4 != "":
            print(f"     -Turno 4: {turnoLunes4}.")
        else:
            print("     -Turno 4: Libre.")
        print("Martes:")
        if turnoMartes1 != "":
            print(f"     -Turno 1: {turnoMartes1}.")
        else:
            print("     -Turno 1: Libre.")
        if turnoMartes2 != "":
            print(f"     -Turno 2: {turnoMartes2}.")
        else:
            print("     -Turno 2: Libre.")
        if turnoMartes3 != "":
            print(f"     -Turno 3: {turnoMartes3}.")
        else:
            print("     -Turno 3: Libre.")

    elif opcionesEj3 == 4:

        turnosTotalesLunes = 0

        if turnoLunes1 != "" and turnoLunes2 != "" and turnoLunes3 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 4
        elif turnoLunes1 != "" and turnoLunes2 != "" and turnoLunes3 != "":
            turnosTotalesLunes = 3
        elif turnoLunes2 != "" and turnoLunes3 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 3
        elif turnoLunes1 != "" and turnoLunes3 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 3
        elif turnoLunes1 != "" and turnoLunes2 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 3
        elif turnoLunes1 != "" and turnoLunes2 != "":
            turnosTotalesLunes = 2
        elif turnoLunes2 != "" and turnoLunes3 != "":
            turnosTotalesLunes = 2
        elif turnoLunes3 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 2
        elif turnoLunes1 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 2
        elif turnoLunes1 != "" and turnoLunes3 != "":
            turnosTotalesLunes = 2
        elif turnoLunes2 != "" and turnoLunes4 != "":
            turnosTotalesLunes = 2
        elif turnoLunes1 != "":
            turnosTotalesLunes = 1
        elif turnoLunes2 != "":
            turnosTotalesLunes = 1
        elif turnoLunes3 != "":
            turnosTotalesLunes = 1
        elif turnoLunes4 != "":
            turnosTotalesLunes = 1

        turnosTotalesMartes = 0

        if turnoMartes1 != "" and turnoMartes2 != "" and turnoMartes3 != "":
            turnosTotalesMartes = 3
        elif turnoMartes1 != "" and turnoMartes2 != "":
            turnosTotalesMartes = 2
        elif turnoMartes1 != "" and turnoMartes3 != "":
            turnosTotalesMartes = 2
        elif turnoMartes2 != "" and turnoMartes3 != "":
            turnosTotalesMartes = 2
        elif turnoMartes1 != "":
            turnosTotalesMartes = 1
        elif turnoMartes2 != "":
            turnosTotalesMartes = 1
        elif turnoMartes3 != "":
            turnosTotalesMartes = 1

        diaConMasTurnos = ""
        if turnosTotalesLunes < turnosTotalesMartes:
            diaConMasTurnos = "El día con más turnos ocupados es el martes."
        elif turnosTotalesLunes > turnosTotalesMartes:
            diaConMasTurnos = "El día con más turnos ocupados es el lunes."
        else:
            diaConMasTurnos = "Ambos días tienen la misma cantidad de turnos ocupados."

        print("\n===================\n  RESUMEN GENERAL\n===================\n")
        print(f"Turnos ocupados día LUNES: {turnosTotalesLunes}")
        print(f"Turnos disponibles día LUNES: {4 - turnosTotalesLunes}")
        print(f"Turnos ocupados día MARTES: {turnosTotalesMartes}")
        print(f"Turnos disponibles día MARTES: {3 - turnosTotalesMartes}")
        print(diaConMasTurnos)

    else:
        break


### EJERCICIO 4 ###


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

nombre = input("Ingrese el nombre del agente: ")

while not nombre.isalpha():
    print("Error: el nombre solo debe contener letras.")
    nombre = input("Ingrese nuevamente el nombre del agente: ")

print()
print("====================================")
print("       ESCAPE ROOM: LA BÓVEDA")
print("====================================")
print("Bienvenido/a, agente", nombre)
print("Tu objetivo es abrir las 3 cerraduras.")
print()

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    print("------------------------------------")
    print("ESTADO DE LA BÓVEDA")
    print("------------------------------------")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas, "/ 3")
    print("Alarma:", alarma)
    print("Código parcial:", codigo_parcial)
    print("------------------------------------")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: debe ingresar una opción entre 1 y 3.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    if opcion == 1:

        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:

            print()
            print("¡La cerradura se trabó!")
            print("Se activa la alarma automáticamente.")
            alarma = True

        else:

            if energia < 40:

                print()
                print("¡La energía está por debajo de 40!")
                print("Existe riesgo de activar la alarma.")

                numero = input("Ingrese un número del 1 al 3: ")

                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    print("Error: debe ingresar un número entre 1 y 3.")
                    numero = input("Ingrese un número del 1 al 3: ")

                numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡Elegiste 3! ¡La alarma se activó!")

                else:
                    if cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print("¡Cerradura abierta!")

            else:

                if cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("¡Cerradura abierta!")

    elif opcion == 2:

        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        print()
        print("Iniciando hackeo...")

        for paso in range(1, 5):

            codigo_parcial += "A"

            print("Paso", paso, "/ 4 - Código:", codigo_parcial)

        if len(codigo_parcial) >= 8:

            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Hackeo exitoso!")
                print("¡Se abrió una cerradura automáticamente!")

        else:
            print("El código todavía no es suficiente.")

    elif opcion == 3:

        forzar_seguidas = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        print()
        print("Has descansado.")
        print("Recuperaste 15 puntos de energía.")

        if alarma:
            energia -= 10
            print("Como la alarma está activada, perdiste 10 de energía extra.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:

        print()
        print("====================================")
        print("      ¡SISTEMA BLOQUEADO!")
        print("====================================")
        print("La alarma está activa y queda poco tiempo.")
        print("La bóveda se bloqueó.")
        print("¡DERROTA!")
        print("====================================")

        tiempo = 0

if cerraduras_abiertas == 3:

    print()
    print("====================================")
    print("           ¡VICTORIA!")
    print("====================================")
    print("Agente", nombre)
    print("¡Has abierto las 3 cerraduras!")
    print("Energía restante:", energia)
    print("Tiempo restante:", tiempo)
    print("====================================")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:

    print()
    print("DERROTA POR BLOQUEO DE LA ALARMA.")

elif energia <= 0:

    print()
    print("====================================")
    print("           ¡DERROTA!")
    print("====================================")
    print("Te quedaste sin energía.")
    print("====================================")

elif tiempo <= 0:

    print()
    print("====================================")
    print("           ¡DERROTA!")
    print("====================================")
    print("Se acabó el tiempo.")
    print("====================================")


## EJERCICIO 5 ###


print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print()
print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador:

        print()
        print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:

            if vida_enemigo < 20:
                danio = ataque_pesado * 1.5
                print("¡Golpe Crítico!")
            else:
                danio = float(ataque_pesado)

            vida_enemigo -= danio

            print("¡Atacaste al enemigo por", danio, "puntos de daño!")

        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:

            if pociones > 0:
                vida_jugador += 30

                if vida_jugador > 100:
                    vida_jugador = 100

                pociones -= 1

                print("¡Te curaste 30 puntos de vida!")
                print("Pociones restantes:", pociones)

            else:
                print("¡No quedan pociones!")

        if vida_enemigo > 0:

            vida_jugador -= danio_enemigo

            print("¡El enemigo te atacó por 12 puntos de daño!")

        turno_gladiador = True

        if vida_jugador > 0 and vida_enemigo > 0:
            print()
            print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print()
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print()
    print("DERROTA. Has caído en combate.")
