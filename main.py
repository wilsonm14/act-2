from collections import deque
from busqueda import buscar_por_cedula, ordenar_por_valor_atencion
from cliente import Cliente
from cola_atencion import ColaAtencion
from pila_contingencia import PilaContingencia

def registrar_cliente():
    print("\nRegistrar Cliente")
    
    while True:
        cedula = input("Cedula: ").strip()
        if cedula:
            break
        print("Error: La cedula no puede estar vacia.")

    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
        print("Error: El nombre no puede estar vacio.")

    while True:
        telefono = input("Telefono: ").strip()
        if telefono:
            break
        print("Error: El telefono no puede estar vacio.")
    
    while True:
        tipo_cliente = input("Tipo de cliente (particular / eps / prepagada): ").strip().lower()
        if tipo_cliente in ["particular", "eps", "prepagada"]:
            break
        print("Error: Ingrese unicamente 'particular', 'eps' o 'prepagada'.")

    while True:
        tipo_atencion = input("Tipo de atencion (limpieza / calzas / extraccion / diagnostico): ").strip().lower()
        if tipo_atencion in ["limpieza", "calzas", "extraccion", "diagnostico"]:
            break
        print("Error: Ingrese un tipo de atencion valido de la lista.")
    
    if tipo_atencion in ["limpieza", "diagnostico"]:
        cantidad = 1
        print("Cantidad asignada automaticamente a 1.")
    else:
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de {tipo_atencion} a realizar: "))
                if cantidad > 0:
                    break
                print("La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un numero entero valido.")

    while True:
        prioridad = input("Prioridad de atencion (normal / urgente): ").strip().lower()
        if prioridad in ["normal", "urgente"]:
            break
        print("Error: Ingrese unicamente 'normal' o 'urgente'.")   

    while True:
        fecha = input("Fecha de la cita (AAAA-MM-DD): ").strip()
        if fecha:
            break
        print("Error: La fecha no puede estar vacia.")

    return Cliente(cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha)

def main():
    arreglo = deque()
    cola_diaria = ColaAtencion()
    pila_urgentes = PilaContingencia()

    while True:
        print("\nBDD Consultorio Odontologico")
        print("1. Registrar usuario")
        print("2. Consultar usuario por CC")
        print("3. Lista de usuarios ordenados por valor de atencion")
        print("4. Ver totales generales del consultorio")
        print("5. Agenda (Cola)")
        print("6. Plan de Contingencia (Pila)")
        print("7. Salir")

        opc = input("Seleccione una opcion: ").strip()
        
        if opc == "1":
            nuevo = registrar_cliente()
            arreglo.append(nuevo)
            cola_diaria.encolar(nuevo)
            
            if nuevo.tipo_atencion.lower() == "extraccion" and nuevo.prioridad.lower() == "urgente":
                pila_urgentes.apilar(nuevo)
                
            print("Cliente registrado con exito.")
            
        elif opc == "2":
            if not arreglo:
                print("No hay clientes registrados.")
            else:
                ordenar_por_valor_atencion(arreglo)
                cedula = input("Ingrese la cedula a buscar: ").strip()
                encontrado = buscar_por_cedula(arreglo, cedula)
                if encontrado:
                    print("Cliente encontrado:")
                    encontrado.mostrar_informacion()
                else:
                    print(f"No se encontro el cliente con cedula {cedula}.")
                    
        elif opc == "3":
            if not arreglo:
                print("No hay clientes registrados.")
            else:
                ordenar_por_valor_atencion(arreglo)
                print("Lista de clientes ordenados por valor de atencion:")
                for c in arreglo:
                    c.mostrar_informacion()
                    
        elif opc == "4":
            if not arreglo:
                print("No hay clientes registrados.")
            else:
                total_clientes = len(arreglo)
                ingresos = 0
                extracciones = 0
                for c in arreglo:
                    ingresos += c.total_pagar
                    if c.tipo_atencion.lower() == "extraccion":
                        extracciones += 1

                print("Registro")
                print(f"Total clientes: {total_clientes}")
                print(f"Total ingresos: ${ingresos}")
                print(f"Clientes para extraccion: {extracciones}")
                
        elif opc == "5":
            cola_diaria.mostrar_agenda()
            if not cola_diaria.esta_vacia():
                atender = input("Desea atender al siguiente cliente de la cola? (s/n): ").strip().lower()
                if atender == 's':
                    atendido = cola_diaria.desencolar()
                    pila_urgentes.remover_por_cedula(atendido.cedula)
                    print(f"Atendiendo a: {atendido.nombre}.")

        elif opc == "6":
            pila_urgentes.ordenar_por_fecha()
            pila_urgentes.generar_informe()
            if not pila_urgentes.esta_vacia():
                llamar = input("Desea llamar al cliente urgente de la pila? (s/n): ").strip().lower()
                if llamar == 's':
                    urgente = pila_urgentes.desapilar()
                    print(f"Llamando de urgencia a: {urgente.nombre}")
        elif opc == "6":
            pila_urgentes.ordenar_por_fecha()
            pila_urgentes.generar_informe()
            if not pila_urgentes.esta_vacia():
                llamar = input("Desea llamar al cliente urgente de la pila? (s/n): ").strip().lower()
                if llamar == 's':
                    urgente = pila_urgentes.desapilar()
                    cola_diaria.remover_por_cedula(urgente.cedula)
                    print(f"Llamando de urgencia a: {urgente.nombre}.")

        elif opc == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()