import core as cr
import os

def agregar_credito(gestor):
    os.system('cls')
    print("****************************************")
    print("*      REGISTRO DE MATERIAS CGU        *")
    print("****************************************")

    try:
        nombre = input("Nombre de la materia: ")
        codigo = input("Código: ")
        creditos = int(input("Créditos: "))
        nota = float(input("Nota: "))
        periodo = input("Periodo (ej: 2025-1): ")
        
        print("¿Es materia optativa? (S/N): ")
        es_optativa = input().upper() == "S"
        
    except:
        print("Error en los datos ingresados")
        input("Presione enter...")
        return

    materia = cr.Materia(nombre, codigo, creditos, nota, periodo, es_optativa)
    gestor.agregar_materia(materia)

    print("Materia registrada correctamente")
    input("Presione enter...")

def VerData(gestor):
    os.system('cls')
    indice = 1
    print("-"*80)
    print(f"{'Item':<5} {'Materia':<20} {'Cred':<5} {'Nota':<5} {'Per':<10} {'Tipo':<10}")
    print("-"*80)

    for materia in gestor.obtener_todas():
        tipo = "Optativa" if materia.es_optativa else "Obligatoria"
        print(f"{indice:<5} {materia.nombre:<20} {materia.creditos:<5} {materia.nota:<5} {materia.periodo:<10} {tipo:<10}")
        indice += 1

    print("-"*80)
    input("Presione enter para continuar...")

def BuscarData(gestor):
    os.system('cls')

    if len(gestor.obtener_todas()) == 0:
        print("No hay materias registradas")
        input("Enter...")
        return

    VerData(gestor)

    items = input("Ingrese el número de la materia a editar (o 'salir'): ")

    if items.lower() == "salir":
        return

    try:
        idx = int(items) - 1
        materia = gestor.obtener_materia(idx)
        if materia is None:
            raise ValueError("Índice inválido")
    except:
        print("Error")
        input("Enter...")
        return

    print(f"Nombre ({materia.nombre}): ", end="")
    nuevo = input()
    if nuevo != "":
        materia.nombre = nuevo

    print(f"Código ({materia.codigo}): ", end="")
    nuevo = input()
    if nuevo != "":
        materia.codigo = nuevo

    print(f"Créditos ({materia.creditos}): ", end="")
    nuevo = input()
    if nuevo != "":
        materia.creditos = int(nuevo)

    print(f"Nota ({materia.nota}): ", end="")
    nuevo = input()
    if nuevo != "":
        materia.nota = float(nuevo)

    print(f"Periodo ({materia.periodo}): ", end="")
    nuevo = input()
    if nuevo != "":
        materia.periodo = nuevo

    print(f"¿Es optativa? ({materia.es_optativa}): ", end="")
    nuevo = input()
    if nuevo.upper() == "S":
        materia.es_optativa = True
    elif nuevo.upper() == "N":
        materia.es_optativa = False

    gestor.registrar_auditoria("editar", f"Materia {materia.nombre} editada")
    gestor.guardar_datos()

    print("Materia actualizada")
    input("Enter...")

def BorrarData(gestor):
    os.system('cls')

    if len(gestor.obtener_todas()) == 0:
        print("No hay materias registradas")
        input("Enter...")
        return

    VerData(gestor)

    items = input("Ingrese el número de la materia a eliminar (o 'salir'): ")

    if items.lower() == "salir":
        return

    try:
        idx = int(items) - 1
        rta = input("¿Desea eliminar la materia seleccionada? S/N: ").strip().upper()
        
        if rta == "S":
            if gestor.eliminar_materia(idx):
                print("Materia eliminada")
            else:
                print("Error al eliminar")
        elif rta == "N":
            print("Operación cancelada.")
        else:
            print("Entrada no válida.")
    except:
        print("Error al eliminar")

    input("Enter...")

def calcular_promedio(gestor):
    os.system('cls')

    promedio = gestor.calcular_promedio()

    if promedio == 0:
        print("No hay datos para calcular promedio")
    else:
        print(f"Promedio ponderado: {round(promedio, 2)}")

    input("Presione enter...")  
