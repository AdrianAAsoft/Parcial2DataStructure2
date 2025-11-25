#Este archivo de codigo se encarga de los metodos de ordenamiento 

#Metodo Bubble sort 
def bsort(lista, key):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(lista[j]) > key(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    return lista

#Metodo insertion sort 
def isort(lista, key):
    for i in range(1, len(lista)):
        key_item = lista[i]
        j = i - 1

        while j >= 0 and key(lista[j]) > key(key_item):
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key_item
    return lista

#Metodo Quick sort
def qsort(lista,key):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[len(lista) // 2] 
    menor = [x for x in lista if key(x) < key(pivot)]
    medio = [x for x in lista if key(x) == key(pivot)]
    mayor = [x for x in lista if key(x) > key(pivot)]
    return qsort(menor,key) + medio + qsort(mayor,key)

#Metodo binary search 
def BiSearch(lista, key):
    #defino los limites 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = izq +(der - izq) // 2
        producto = lista[medio]
        if producto.id == key:
            return producto   #Si mi id fue encontrado retorno el producto 
        elif producto.id  < key: 
            izq = medio + 1
        else:
            der = medio -1 
    return None   #no retornara nada si no lo encuentra