###Importacion de la libreria Json

import json

#Guardar
def guardar_archivo(Clientes):
    with open("Clientes.json","w") as file:
        json.dump(Clientes,file,indent=4)
        print("Datos guardados correctamente\n")

#Cargar
def cargar_archivo(Clientes):
    try:
        with open("Clientes.json", "r") as file:
            Clientes = json.load(file)
            print("Datos cargados correctamente\n")
            return Clientes
    except:
        print("No hay datos guardados\n")
        return [] 

#Crear Cliente.
def Crear_Cliente(Clientes):##Ingresar dentro de los parentecis el nombre de la lista.
    try:
        Id = input("Ingrese su numero de ID: ")
        Name = input("Ingrese su Nombre: ")
        Age = int(input("Ingrese su Edad: "))
        Plan =input("Ingrese su Plan (Mensual,Trimestral,Anual) ")
        Status =input("Ingrese su Estado (Activo/Inactivo)")

        Cliente={
            "id":Id,
            "name":Name,
            "age":Age,
            "plan":Plan,
            "status":Status
        }
        Clientes.append(Cliente)
        print("Cliente Agregado Correctament. ")
        
    except:
        print("Error: Datos Incorrectos ") 
#Mostrar Lista
def Mostar_Lista(Clientes):
    if len(Clientes)==0:
        print("No hay Clientes Registrados. ")
    else:
        for Cliente in Clientes:
            print(f"ID:{Cliente["id"]} | Nombre:{Cliente["name"]} | Edad:{Cliente["age"]} | Plan:{Cliente["plan"]} | Estado:{Cliente["status"]}")         

#Buscar
def Buscar_CLiente(Clientes):
    x = input("Ingresa ID o Nombre: ")

    for c in Clientes:
        if c["id"] == x or c["name"] == x:
            print(c)
            return

    print("No se pudo encontrar.")

#Actualizar
def Actualizar_Cliente(Clientes):
    id = input("ID a Actualizar:" )
    for c in Clientes:
            if c["id"] == id:
                c["name"]=input("Actualizacion del Nombre: ")
                c["age"]=int(input("Edad Actualizada: "))
                c["plan"]=input("Actualizacion del Plan: ")
                c["status"]=input("Actualizacion de Estado: ")
                print("Actualizado\n")
                return
            
    print("No se a encontrado\n")

#Eliminar
def Eliminar_Cliente(Clientes):
    id = input("ID a Eliminar: ")
    for c in Clientes:
        if c["id"] == id:
            Clientes.remove(c)
            print("Eliminado\n")
            return
        print("No encontrado:")

def menu():
    #Lista de Clientes
    Clientes=[]
    op = 0

    while op !=8:
        print("----- GYM CLIENT SYSTEM -----")
        print("1. Crear Cliente")
        print("2. Lista de Clientes")
        print("3.Buscar")
        print("4.Actualizar")
        print("5.Eliminar")
        print("6.Guardar")
        print("7.Cargar Datos")
        print("8.Cerrar")


        op = input("Choose an option: ") 

        if op == "1":
            Crear_Cliente(Clientes)
        elif op == "2":
            Mostar_Lista(Clientes)  
        elif op == "3":
            Buscar_CLiente(Clientes)
        elif op == "4":
            Actualizar_Cliente(Clientes)
        elif op == "5":
            Eliminar_Cliente(Clientes)
        elif op =="6":
            guardar_archivo(Clientes)
        elif op == "7":
            Clientes=cargar_archivo(Clientes)        
        elif op == "8":
            print("Cerrando\n")
            
        else:
            print("Opcion no Valida\n")    
               



menu()            