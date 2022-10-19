
'''
carrito={}

ban="s" #bandera/inicializo el while

total=0 #variable total para sumar al final

while ban=="s":
 articulo=str(input("nombre del articulo: \n"))
 precio=float(input("precio del articulo: $"))

 carrito[articulo]=precio

 ban=str(input("¿Quiere seguir comprando?: s/n ")) #interruptor para seguir comprando o no


for i in carrito: #for para sacar el total de los articulos que compré
  print(i + str(carrito[i])) #imprimo el articulo y el precio / convierto a str el float del carrito
  total +=carrito[i] #suma el valor de la clave(diccionario)

print("total a pagar: $"+ str(total))

'''
''''
factura = {}  # diccionario

ban = "s"  # bandera

pendiente = 0

cobrado = 0

while ban == "s":
    # en la opcion me da un error cuando lo ejecuto pero no se cual es :/
    opcion = input("MENU\n¿Que opcion desea realizar?:\n 1-Agregar Factura\n 2-Pagar Factura\n 3-SALIR\n")

    if opcion == "1":
        num_factura = int(input("Agregar Factura: \n Numero de Factura: \n"))
        valor = float(input("Importe de la Factura\n"))
        factura[num_factura] = valor
        pendiente += valor
        print("Pendiente: $" + str(pendiente))
        print("Pagó hoy: $" + str(cobrado) + "\n\n")

    elif opcion == "2":
        num_factura = int(input("PAGAR FACTURA: \n Escribe el numero de la factura: "))

    if num_factura in factura:
        pendiente -= factura[num_factura]
        cobrado += factura[num_factura]
    # aqui iria el else que puse al final pero me daba error


    elif opcion == "3":  # revisar opcion 3 no me da el pendiente
        print("Pendiente: $" + str(pendiente))
        print("Pagó hoy: $" + str(cobrado) + "\n\n")
        ban == "n"  # bandera para salir del ciclo while


  # else:  # else dudoso puede ir antes del elif de la opcion 3?
        #print("No se encontró la factura!")



print("Pendiente: $" + str(pendiente))  # print final
print("Pagó hoy: $" + str(cobrado) + "\n\n")

'''
'''
cant_num = 0

usuario=input("INGRESE SU NOMBRE DE USUARIO: ")

cant_num = int(input("Ingrese su identificacion de DNI por favor: "))
for i in range(cant_num):
    numN = int(input("ingrese su identificacion de usuario: "))
    suma = 1
    for i in range(2, (numN // 2) + 1):

        if (numN / i) == 0:
            suma += i

        if (suma > numN):
            print(f'el numero:{numN} es diferente: ')
        elif (suma > numN):
            print(f'el numero: {numN} es abundante:')

        else:
            (suma == numN)
            print(f'el numero: {numN} es perfecto: ')

        print('divisiores',i)
        
        
   '''
'''
from IPython.display import clear_output

print("")
print("┌───────────────────────────────────────────────────────────────┐")
print("│ 🏥 Bienvenidos al sistema de historias clínicas del hospital 🏥 │")
print("└───────────────────────────────────────────────────────────────┘")
print("")
print("")
# **********************
# * VARIABLES GLOBALES *
# **********************
running = True
# database = []
database = [{'nombre': 'Juan', 'historia': 'resfrio'},
            {'nombre':'Rodolfo','historia':'dolor de garganta'},
            {'nombre': 'pedro', 'historia': 'dolor de muela'}]


# **********************
# *     FUNCIONES      *
# **********************
def show_menu():
    print("")
    print("")
    print("\t\t🔵  1 - Cargar paciente")
    print("\t\t🔵  2 - Buscar paciente")
    print("\t\t🔵  3 - Listar pacientes")
    print("\t\t🔵  4 - Salir")
    print("")
    res = input("INGRESE UNA OPCION ➡️ ")
    clear_output()
    return res


def response_validate(response):
    validated = False
    num_res = 0

    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4:
            msg = "esta en rango"
            validated = True
        else:
            msg = "fuera de rango"
    else:
        msg = "Entrada incorrecta"

    return validated, num_res, msg


def alta_paciente():
    name = input("Ingrese el nombre del paciente ➡️ ")
    history = input("Ingrese la historia clínica del paciente ➡️ ")
    paciente = {"nombre": name, "historia": history}
    database.append(paciente)


# **********************
# *  PRINCIPAL         *
# **********************

while running:
    response = show_menu()
    validated, num_res, msg = response_validate(response)
    if validated:
        if num_res == 1:
            alta_paciente()
        elif num_res == 2:
            name = input("Ingrese el nombre del paciente  ➡️ ")
            i = 0
            while i < len(database) and database[i]["nombre"].lower() != name.lower():
                i += 1
            if i < len(database):
                print("")
                print("Paciente encontrado!")
                print("PACIENTE ENCONTADO | H. CLINICA ➡️ ", database[i]["historia"])
                print("")
            else:
                print("Paciente no encontrado 😔")
        elif num_res == 3:
            print("")
            print("┌─────────────────────────────┐")
            print("│   LISTADO DE PACIENTES      │")
            print("└─────────────────────────────┘")
            print("")
            for x in range(len(database)):
                print("Nombre ➡️ ".ljust(10), database[x]["nombre"], "\t Historia C ➡️ ".ljust(10),
                      database[x]["historia"])

            print("FIN DE LISTA")
        else:
            running = False
    else:
        print(msg)

print("")
print("Aplicación finalizada")
print("")
# import os
# os.system('clear')

'''
'''
def multiplica_por_5(numero):
    print(f'{numero} * 5={numero * 5}')

print("Comienzo de programa...")
multiplica_por_5(7)
print("Siguiente...")
multiplica_por_5(113)
print("FIN")
'''
#def es_par(num):
   #if num/2==0:
    #print("es par")
   #else:
    #print("es impar")

'''
import random as randint
def generar():
    for generar in range(0, 1000):

        print(generar)



numero=generar()
print(numero)

'''

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad

 class Empleado(Persona):
     def __init__(self,nombre, apellido, edad, puesto):
       self.nombre
       self.apellido
       self.edad
       self.puesto
       return Persona













