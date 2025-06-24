colegio = {
    "estudiantes": [
        {
            "usuario": "",
            "genero": "",
            "codigo": ""
        }
    ]
}
def validacion_str(mensaje:str):
    try:
        x = str(input(mensaje))
        return x 
    except ValueError:
        print("Error, ingresaste un caracter no valido.")
def validacion_int(mensaje:str):
    try:
        x = int(input(mensaje))
        return x 
    except ValueError:
        print("Error, ingresaste un caracter no valido.")
def validacion_float(mensaje:str):
    try:
        x = float(input(mensaje))
        return x 
    except ValueError:
        print("Error, ingresaste un caracter no valido.")
def nombre_usuario(mensaje:str):
    nombre = validacion_str(mensaje)
    return nombre
def validacion_genero(mensaje:str):
    sexo = validacion_str(mensaje).upper()
    if sexo == "F":
        return sexo
    elif sexo == "M":
        return sexo
    else:
        print("Error, ingresaste un caracter no valido. Porfavor ingrese M o F.")

def validacion_contraseña(mensaje:str):
    contraseña = validacion_str(mensaje)
    x = len(contraseña)
    if x == 8:
        print("COntraseña correcta.")
        return contraseña
    else:
        print("Contraseña invalida. Intente otra.")
    return contraseña


def ingresar_usuario():
    nombre = nombre_usuario("Ingrese nombre de usuario: ")
    genero = validacion_genero("Ingrese sexo del usuario (F o M): ")
    contraseña = validacion_contraseña("Ingrese contraseña (minimo 8 caracteres): ")
    estudiante_nuevo = {
        "usuario": nombre,
        "genero": genero,
        "codigo": contraseña,
    }
    colegio["estudiantes"].append(estudiante_nuevo)
    print("Usuario ingresado con exito!!")
    return estudiante_nuevo

def buscar_usuario():
    buscar = validacion_str("Ingrese usuario a buscar: ")
    for i in colegio['estudiantes']:
        if i['usuario'].lower() == buscar.lower():
            print(f"El sexo del usuario es: ", {i['genero']}, "y la contraseña es: ",{i['codigo']}, ".") 
            return buscar, i 
    else: 
        print("Usuario no encontrado.")

def eliminar_usuario():
    print("")
    nombre = nombre_usuario("Ingrese el usaurio a eliminar: ")
    for i in colegio["estudiantes"]:
        if i['usuario'].lower() == nombre.lower():
            del colegio["estudiantes"]
            print("se eliminara el usuario.")
            return i, nombre
    else:
        print("No se pudo eliminar usuario!")

def salir():
    while True:
        print("Saliendo.")
        print("Tenga buen día.")
        break

def menu():
    while True:
        print("***Menú***")
        print("[1]- Ingresar usuario.")
        print("[2]- Buscar usuario.")
        print("[3]- Eliminar usuario.")
        print("[4]- Salir.")
        opcion = validacion_int("--> ")
        if opcion == 1:
            ingresar_usuario()
        elif opcion == 2:
            buscar_usuario()
        elif opcion == 3:
            eliminar_usuario()
        elif opcion == 4:
            salir()
            break
        else:
            print("Error, no es posible esa opción.")
            continue

menu()