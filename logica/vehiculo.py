#CAPA DE LOGICA DE NEGOCIO

#Clase Vehiculo
class vehiculo:
    # Método inicializador (constructor) para crear una instancia de la clase 'vehiculo'
    def __init__(self, id, nombre, conductor, status, ruta, localizacion, velocidad, nivel_combustible, kilometraje, temperatura_motor, comportamiento_conduccion):
        #Asignamos el valor del parámetro  al atributo de la instancia 
        self.id = id
        self.nombre = nombre
        self.conductor = conductor
        self.status = status
        self.ruta = ruta
        self.localizacion = localizacion
        self.velocidad = velocidad
        self.nivel_combustible = nivel_combustible
        self.kilometraje = kilometraje
        self.temperatura_motor = temperatura_motor
        self.comportamiento_conduccion = comportamiento_conduccion

