from Productos import GProductos  #Importar funcion GProductos de archivo Productos
from FOrdenamiento import bsort, qsort, isort
import time

def mostrar_productos(lista):
    print("\n===== LISTA DE PRODUCTOS =====")
    for p in lista:
        print(p)

def elegir_criterio():
    print("\n--- MEtodos de Ordenamiento ---")
    print("1. Precio (Ascendente)")
    print("2. Calificación Promedio (Descendente)")
    print("3. ID (Ascendente)")

    while True:
        op = input("Seleccione una opcion: ")

        if op == "1":
            return lambda p: p.precio
        elif op == "2":
            return lambda p: -p.rating
        elif op == "3":
            return lambda p: p.id
        else:
            print("Opcion no valida, reintente.")

if __name__ == "__main__" :
    print("Completando el catalogo de 50 productos aleatorios...\n")
    productos = GProductos()

    while True:
        print("\n======= MENU PRINCIPAL =======")
        print("1. Ordenar con Bubble Sort")
        print("2. Ordenar con Quick Sort")
        print("3. Ordenar con Insertion Sort")
        print("4. Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            key = elegir_criterio()
            tiempoIni = time.time()
            productos = bsort(productos, key)
            tiempofin = time.time()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            print("\nProductos ordenados con Bubble Sort.")
            mostrar_productos(productos)

        elif opcion == "2":
            key = elegir_criterio()
            tiempoIni = time.time()
            productos = qsort(productos, key)
            tiempofin = time.time()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            print("\nProductos ordenados con Quick Sort.")
            mostrar_productos(productos)

        elif opcion == "3":
            key = elegir_criterio()
            tiempoIni = time.time()
            productos = isort(productos, key)
            tiempofin = time.time()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            print("\nProductos ordenados con Insertion Sort.")
            mostrar_productos(productos)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opcion no existe, intente nuevamente.")

