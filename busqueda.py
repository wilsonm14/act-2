def ordenar_por_valor_atencion(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = arreglo[j].valor_atencion_unitario * arreglo[j].cantidad
            val2 = arreglo[j+1].valor_atencion_unitario * arreglo[j+1].cantidad
            if val1 < val2:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def buscar_por_cedula(arreglo, cedula):
    for c in arreglo:
        if c.cedula == cedula:
            return c
    return None