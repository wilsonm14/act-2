from collections import deque

class ColaAtencion:
    def __init__(self):
        self.turnos = deque()

    def esta_vacia(self):
        return len(self.turnos) == 0

    def encolar(self, cliente):
        self.turnos.append(cliente)

    def desencolar(self):
        if not self.esta_vacia():
            return self.turnos.popleft()
        return None
    def remover_por_cedula(self, cedula):
        self.turnos = deque([c for c in self.turnos if c.cedula != cedula])

    def mostrar_agenda(self):
        print("\nAgenda (Cola)")
        if self.esta_vacia():
            print("La cola esta vacia.")
        else:
            for idx, c in enumerate(self.turnos, 1):
                print(f"{idx}. {c.nombre} - {c.tipo_atencion} - {c.prioridad}")