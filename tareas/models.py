from usuarios.models import Usuario
from datetime import datetime

class Tarea:
    def __init__(self, id_tarea, titulo, descripcion, fecha_inicio, fecha_limite, id_usuario, id_prioridad):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_inicio = self.convertir_fecha(fecha_inicio)
        self.fecha_limite = self.convertir_fecha(fecha_limite)
        self.id_usuario = id_usuario 
        self.id_prioridad = id_prioridad

    def convertir_fecha(self, fecha):
        return datetime. strptime(fecha, '%Y-%m-%d')
