import os
global aprobados
global reprobados

DB = "./db/"
ASIGNATURAS = "./db/asig/"


def ingreso():
    names = open("names.txt", "a")
    asignatura = " "
    notesaving = 0
    promedios = " "
    x = 0
    global reprobados
    global aprobados

    reprobados = 0
    aprobados = 0

    estudiantes = input("¿Cuantos estudiantes desea ingresar?: ")

    try:
        estudiantes = int(estudiantes)
    except ValueError:
        print("La opción debe ser numérica \n.")
        exit()

    while x < estudiantes:
        db = open("./db/datos.txt", "a")
        nombre = input("Ingrese el nombre del estudiante: ")
        print("Escoja la asignatura")
        print("Cálculo(1)")
        print("Programación (2)")
        print("Ética (3)")
        asig = input(": ")

        try:
            asig = int(asig)
        except ValueError:
            print("La opción debe ser numérica. \n")
            exit()

        nota1 = input("Ingrese la primera nota:")
        nota2 = input("Ingrese la segunda nota:")
        nota3 = input("Ingrese la tercera nota:")

        try:
            nota1 = float(nota1)
        except ValueError:
            print("La nota debe ser numérica \n.")
        try:
            nota2 = float(nota2)
        except ValueError:
            print("La nota debe ser numérica \n.")
        try:
            nota3 = float(nota3)
        except ValueError:
            print("La nota debe ser numérica \n.")
            exit()

        if asig == 1:
            asignatura = "Cálculo"
            notesaving = 1
        elif asig == 2:
            asignatura = "Programación"
            notesaving = 2
        elif asig == 3:
            asignatura = "Ética"
            notesaving = 3
        elif asig > 3 or asig < 1:
            print("Esas asignaturas no existen \n")
            exit()

        if notesaving == 1:
            path = (ASIGNATURAS + "calculo.txt")
            promedios = open(path, 'a')
        elif notesaving == 2:
            path = (ASIGNATURAS + "programacion.txt")
            promedios = open(path, 'a')
        elif notesaving == 3:
            path = (ASIGNATURAS + "etica.txt")
            promedios = open(path, 'a')
        else:
            print("Ni idea que ha sucedido, autodestruyendose en 5..4..3..2..1..0")
            print("KABOOOOOM!")
            exit()

        estudiante = list((nombre, asignatura, nota1, nota2, nota3))

        if (estudiante[2]) >= 1.0 and estudiante[2] <= 7.0:
            pass
        else:
            print("la/s notas no están dentro del rango valido. \n")
            exit()
        if (estudiante[3]) >= 1.0 and estudiante[3] <= 7.0:
            pass
        else:
            print("la/s notas no están dentro del rango valido. \n")
            exit()
        if (estudiante[4]) >= 1.0 and estudiante[4] <= 7.0:
            pass
        else:
            print("la/s notas no están dentro del rango valido. \n")
            exit()

        promedio = ((estudiante[2]) + (estudiante[3]) + (estudiante[4]))/3
        estudiante.append(promedio)

        promedio = str(promedio)
        promedios.write(promedio)
        promedios.write("\n")

        promedio = float(promedio)

        if promedio >= 4:
            estado = 'aprobó'
            aprobados = aprobados + 1
            text = "\nEl estudiante no deberá realizar nuevamente la asignatura.\n"
        else:
            estado = "reprobó"
            reprobados += reprobados + 1
            text = "\nEl estudiante deberá realizar nuevamente la asignatura. \n"

        estudiante.append(estado)

        print("El estudiante: " + estudiante[0] + " De la asignatura: " + estudiante[1])
        print("Obtuvo un promedio de: " + str(promedio) + " por lo que " + estado + " la asignatura.")
        print(text)

        db.write("Nombre:" + str(estudiante[0]) + ". \n Asignatura: " + str(estudiante[1]) + ". \n Notas 1: " +
                 str(estudiante[2]) + ". \n Nota2: " + str(estudiante[3]) + ". \n Nota3: " + str(estudiante[4])
                 + ". \n Promedio: " + str(estudiante[5]) + ". \n Estado de la materia: " + str(estudiante[6]) + "\n")

        destino = (DB + (estudiante[0]) + ".txt")
        destino = str(destino)
        os.rename(DB + "datos.txt", destino)

        names.write(estudiante[0] + "\n")

        x += 1

        if x == estudiantes:
            print("Hubieron " + str(aprobados) + " estudiantes aprobados y "
                  + str(reprobados) + " estudiantes reprobados.")
            db.close()
            names.close()
            promedios.close()
            menu()
        else:
            pass


def visualizar():
    def options():
        print("###########################################################################")
        print("¿Qué desea hacer?, Escoja una opción:\n")
        print("##(1) Mostrar la información de un estudiante.")
        print("##(2) Mostrar los promedios general de todas las asignaturas.")
        print("##(3) Mostrar el nombre de un estudiante, sus asignaturas y notas,"
              "\n      cuando el promedio sea mayor a 4.0.")
        print("##(4) Mostrar el promedio más alto obtenido junto al nombre del estudiante,"
              "\n      asignatura y sus calificaciones.")
        print("##(5) Listar los archivos existentes en la DB.")
        print("###########################################################################")
        valor = input(":")
        try:
            valor = int(valor)
        except ValueError:
            print("La opción debe ser numérica.")
            exit()
        return valor

    def unexistent():
        print("La opción no ha sido programada aún.")
        exit()

    def listing():
        archivos = os.listdir(DB)

        for file in archivos:
            print(file)

    opcion = options()

    def allstudents():
        archivos = os.listdir(DB)
        value = input("Escoja el archivo mediante su nombre y extensión \'ejemplo.txt\':")

        if value in archivos:
            print("El archivo existe.")
        else:
            print("El archivo no existe.")
            exit()

        estudiante = open(DB + value, 'r')
        estudiante = estudiante.read()
        print("\n" + estudiante + "\n")

    def promedioslisting():
        print("Escoja una asignatura:")
        print("(1) Cálculo")
        print("(2) Ética")
        print("(3) Programación")
        materia = input(":")

        try:
            materia = int(materia)
        except ValueError:
            print("La opción debe ser numérica.")
            exit()

        if materia == 1:
            archivo = open(ASIGNATURAS + "calculo.txt", "r")
            promedio = 0
            counter = len(archivo.readlines())

            for linea in archivo.readlines():
                linea = int(linea)
                print("Valor de la linea " + str(counter))
                print(linea)
                promedio = (promedio + linea)

            promedio = (promedio/counter)
            asignatura = "Cálculo"
            promedio = str(promedio)
            print("promedio str:"+promedio)
            return promedio, asignatura

        elif materia == 2:
            pass
        elif materia == 3:
            pass

    if opcion == 1:
        print("Mostrando archivos existentes en la DB:\n")
        listing()
        allstudents()
        exit()
    elif opcion == 2:
        promedioasig, asign = promedioslisting()
        print("El promedio total de la asignatura: " + asign + " es de: " + promedioasig)
    elif opcion == 3:
        unexistent()
    elif opcion == 4:
        unexistent()
    elif opcion == 5:
        listing()
    else:
        print("\nEsa opción no existe.\n")
        exit()


def menu():
    print("#####################################################")
    print("Bienvenido al gestor de notas, Escoja un a opción: \n")
    print("1: Ingresar nuevos datos. \n")
    print("2: Mostrar información guardada. \n")
    print("3: Salir del gestor.")
    print("##################################################### \n")
    opcion = input("Introduzca su opción: ")

    try:
        opcion = int(opcion)

    except ValueError:
        print("La opción debe ser numérica.")
        exit()

    if opcion is None:
        print("La opcion no puede ser nula.")
        exit()
    elif opcion <= 0 or opcion > 3:
        print("Esa opción no existe. \n")
        exit()
    elif opcion == 1:
        print("Opción escogida " + str(opcion) + "\n")
        ingreso()
    elif opcion == 2:
        print("Opción escogida " + str(opcion) + "\n")
        visualizar()
    elif opcion == 3:
        print("Opción escogida " + str(opcion) + "\n")
        print("Gracias por usar el gestor :D.")
        exit()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nGestor Cerrado de manera forzosa. \n")
