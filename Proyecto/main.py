from Productos import GProductos  #Importar funcion GProductos de archivo Productos
from FOrdenamiento import bsort, qsort, isort, BiSearch    #Importar funciones del archivo con los metodos
import time  #Libreria para medir tiempo

def mostrar_productos(lista):
    print("\n===== LISTA DE PRODUCTOS =====")
    for p in lista:
        print(p)

def elegir_criterio():
    print("\n--- Metodos de Ordenamiento ---")
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
        print("4. Busqueda binaria")
        print("5. Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            key = elegir_criterio()
            tiempoIni = time.perf_counter()
            productos = bsort(productos, key)
            tiempofin = time.perf_counter()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            print("\nProductos ordenados con Bubble Sort: ")
            mostrar_productos(productos)

        elif opcion == "2":
            key = elegir_criterio()
            tiempoIni = time.perf_counter()
            productos = qsort(productos, key)
            tiempofin = time.perf_counter()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            print("\nProductos ordenados con Quick Sort: ")
            mostrar_productos(productos)

        elif opcion == "3":
            key = elegir_criterio()
            tiempoIni = time.perf_counter()
            productos = isort(productos, key)
            tiempofin = time.perf_counter()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            print("\nProductos ordenados con Insertion Sort: ")
            mostrar_productos(productos)
        
        elif opcion == "4":
            tiempoIni = time.perf_counter()
            try:
                idS = int(input("Ingrese el ID a buscar (1-50): "))
            except idS < 1:
                print("ID fuera de rango, debe ser mayor a 0")
                continue
            except ValueError:
                print("ID invalido. Debe ser un entero.")
                continue
            
            tiempoIni = time.perf_counter()
            busqueda = BiSearch(productos, idS)
            tiempofin = time.perf_counter()
            print(f"\nTiempo de ejecucion: {tiempofin - tiempoIni:.6f} segundos")
            
            if busqueda: 
                print("Producto encontrado: "+ str(busqueda))
            else:
                print("--No se encontro el Id mencionado, por lo tanto no existe el producto.--")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opcion no existe, intente nuevamente.")

