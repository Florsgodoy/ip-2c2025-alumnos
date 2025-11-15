# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

# lista de elementos y variables de control
items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    #reinicio los contadores para empezar el bubble
    i = 0
    j = 0

def step():
    global items, n,i,j

    #si se hicieron todas las pasadas, se termina el ordenamiento 
    if i >= n-1:
        return {"done": True}
    
    #indices de los elementos a comparar 
    a= j
    b= j + 1
    swap= False 

    #si el elemento es "a" es mayor que el elemento "b", se intercambian
    if items[a] > items[b]: 
        items[a], items[b] = items[b], items[a]
        swap= True

    #paso al siguiente par de elementos
    j= j + 1 

    #si llego al final de la pasada, paso al siguiente 
    if j >= n - i -1:
        i = i + 1
        j= 0

    #informacion necesaria para la visualizacion
    return{
        "a":a, #posicion del primer elemento
        "b":b, #posicion del segundo elemento
        "swap": swap, #si hubo intercambio
        "done": False, #si se termino o no
    }
