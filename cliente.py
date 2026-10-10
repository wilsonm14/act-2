class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha = fecha
        self.valor_cita = self.calcular_valor_cita()
        self.valor_atencion_unitario = self.calcular_valor_atencion_unitario()
        self.total_pagar = self.calcular_total_pagar()

    def calcular_valor_cita(self):
        tc = self.tipo_cliente.strip().lower()
        if tc == "particular":
            return 80000
        elif tc == "eps":
            return 5000
        elif tc == "prepagada":
            return 30000
        return 0

    def calcular_valor_atencion_unitario(self):
        tc = self.tipo_cliente.strip().lower()
        ta = self.tipo_atencion.strip().lower()
        
        if tc == "particular":
            if ta == "limpieza": return 60000
            elif ta == "calzas": return 80000
            elif ta == "extraccion": return 100000
            elif ta == "diagnostico": return 50000
        elif tc == "eps":
            if ta == "limpieza": return 0
            elif ta == "calzas": return 40000
            elif ta == "extraccion": return 40000
            elif ta == "diagnostico": return 0
        elif tc == "prepagada":
            if ta == "limpieza": return 0
            elif ta == "calzas": return 10000
            elif ta == "extraccion": return 10000
            elif ta == "diagnostico": return 0
        return 0

    def calcular_total_pagar(self):
        return self.valor_cita + (self.valor_atencion_unitario * self.cantidad)

    def mostrar_informacion(self):
        print(f"Cedula: {self.cedula} | Nombre: {self.nombre} | Telefono: {self.telefono} | Atencion: {self.tipo_atencion} | Prioridad: {self.prioridad} | Fecha: {self.fecha} | Total: ${self.total_pagar}")        