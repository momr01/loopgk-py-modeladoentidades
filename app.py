from tareas.models import Tarea
from prioridades.models import Prioridad
from usuarios.models import Usuario

#creacion de prioridades
pr_alta = Prioridad("1", "Alta", "rojo")
pr_media = Prioridad("2", "Media", "amarillo")
pr_baja = Prioridad("3", "Baja", "verde")

#creacion de usuario
user_1 = Usuario("1", "Pablo", "Lopez", "analista de marketing", "pl@gmail.com", "123")

#creacion de tarea
tarea_1 = Tarea("1","Consultar información", "Buscar información relacionada al proyecto", "2022-10-29", "2022-11-29", "1", "2")

#test
print(pr_alta.color)
print(user_1.email)
print(tarea_1.descripcion)
