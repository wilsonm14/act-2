class PilaContingencia:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, cliente):
        self.elementos.append(cliente)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def ordenar_por_fecha(self):
        n = len(self.elementos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.elementos[j].fecha < self.elementos[j + 1].fecha:
                    self.elementos[j], self.elementos[j + 1] = self.elementos[j + 1], self.elementos[j]

    def remover_por_cedula(self, cedula):
        self.elementos = [c for c in self.elementos if c.cedula != cedula]

    def generar_informe(self):
        print("\nInforme Contingencia Extracciones Urgentes")
        if self.esta_vacia():
            print("Pila vacia.")
        else:
            # Imprimimos desde la base hasta la cima para que el usuario vea el orden lógico
            for c in self.elementos:
                print(f"Cedula: {c.cedula}, Nombre: {c.nombre}, Fecha: {c.fecha}")