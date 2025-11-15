# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    for i in range(0,n):   # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
        for j in range(i,n):    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
            if n[min_idx]> n[j]: #   Al terminar el barrido, pasar a fase "swap".
                min_idx=j
        return{"a": min_idx, "b": j, "swap": False, "done": False}
  # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    temp=n[i]    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    n[i]=n[min_idx]
    n[min_idx]=temp    #
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}
