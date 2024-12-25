#CAPA DE DATOS

# Importa la clase 'vehiculo' desde el módulo 'logica.vehiculo'
from logica.vehiculo import vehiculo

# Crea una lista de objetos 'vehiculo' con información de diferentes vehículos
vehiculos_db = [
    vehiculo(
        id=1,
        nombre="Camión 101",
        conductor="Carlos López",
        status="En movimiento",
        ruta="Ruta A",
        localizacion="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13447.976956931191!2d-74.006!3d40.7128!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259af18b173d3:0x6457a5d62265f89!2sNew+York,+NY,+USA!5e0!3m2!1ses-419!2sco!4v1731820343211!5m2!1ses-419!2sco",
        velocidad=70,
        nivel_combustible=60,
        kilometraje=45000,
        temperatura_motor=95,
        comportamiento_conduccion="Normal"
    ),
    vehiculo(
        id=2,
        nombre="Camión 102",
        conductor="Ana García",
        status="En mantenimiento",
        ruta="Ruta B",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3302.7111384896585!2d-118.2436834846066!3d34.052235823421634!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c2c7d6b9d3b5f9:0x637b1ed32b3f60a!2sLos+Angeles,+CA,+USA!5e0!3m2!1ses-419!2sco!4v1731820415666!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=40,
        kilometraje=60000,
        temperatura_motor=0,
        comportamiento_conduccion="No aplica"
    ),
    vehiculo(
        id=3,
        nombre="Camioneta 201",
        conductor="Luis Pérez",
        status="Disponible",
        ruta="Ruta C",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10481.291363582305!2d-0.12775882321338118!3d51.50739945127439!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4876036b2b5e5cfb:0x3a56a39e7d2d3c7b!2sLondon,+UK!5e0!3m2!1ses-419!2sco!4v1731820449189!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=85,
        kilometraje=15000,
        temperatura_motor=0,
        comportamiento_conduccion="No aplica"
    ),
    vehiculo(
        id=4,
        nombre="Camioneta 202",
        conductor="María Herrera",
        status="En movimiento",
        ruta="Ruta D",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2624.301109518488!2d2.352221547233174!3d48.8566144931918!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e671c7228c41e5:0xb8d769bd2e5e000!2sParis,+France!5e0!3m2!1ses-419!2sco!4v1731820480599!5m2!1ses-419!2sco",
        velocidad=65,
        nivel_combustible=70,
        kilometraje=18000,
        temperatura_motor=88,
        comportamiento_conduccion="Normal"
    ),
    vehiculo(
        id=5,
        nombre="Furgoneta 301",
        conductor="José Rivera",
        status="En carga",
        ruta="Ruta E",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3242.8352904342965!2d139.69170683558045!3d35.68948777259711!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188c0e703a7f6f:0xe1031a8a03a6f1e!2sTokyo,+Japan!5e0!3m2!1ses-419!2sco!4v1731820513311!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=95,
        kilometraje=7000,
        temperatura_motor=0,
        comportamiento_conduccion="No aplica"
    ),
    vehiculo(
        id=6,
        nombre="Furgoneta 302",
        conductor="Rosa Martínez",
        status="En movimiento",
        ruta="Ruta F",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d19323.451262419093!2d144.96305782508083!3d-37.81361129475532!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81:0x5045675218cee20!2sMelbourne,+Australia!5e0!3m2!1ses-419!2sco!4v1731820541511!5m2!1ses-419!2sco",
        velocidad=50,
        nivel_combustible=75,
        kilometraje=22000,
        temperatura_motor=82,
        comportamiento_conduccion="Normal"
    ),
    vehiculo(
        id=7,
        nombre="Tráiler 401",
        conductor="Mario Gómez",
        status="Disponible",
        ruta="Ruta G",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62328.64547154153!2d74.35535591280196!3d31.549714100877228!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391903d101c157e3:0x9d99efc567f4eb7e!2sLahore,+Pakistan!5e0!3m2!1ses-419!2sco!4v1731820582911!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=50,
        kilometraje=30000,
        temperatura_motor=0,
        comportamiento_conduccion="No aplica"
    ),
     vehiculo(
        id=8,
        nombre="Camión 104",
        conductor="Paola Ramírez",
        status="En pausa",
        ruta="Ruta H",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62328.64547154153!2d74.35535591280196!3d31.549714100877228!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391903d101c157e3:0x9d99efc567f4eb7e!2sLahore,+Pakistan!5e0!3m2!1ses-419!2sco!4v1731820582911!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=30,
        kilometraje=14500,
        temperatura_motor=0,
        comportamiento_conduccion="Descanso"
    ),
    vehiculo(
        id=9,
        nombre="Furgoneta 303",
        conductor="Gabriel Díaz",
        status="En revisión",
        ruta="Ruta I",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62328.64547154153!2d74.35535591280196!3d31.549714100877228!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391903d101c157e3:0x9d99efc567f4eb7e!2sLahore,+Pakistan!5e0!3m2!1ses-419!2sco!4v1731820582911!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=40,
        kilometraje=7000,
        temperatura_motor=0,
        comportamiento_conduccion="No aplica"
    ),
    vehiculo(
        id=10,
        nombre="Camión 105",
        conductor="Lucía Méndez",
        status="En movimiento",
        ruta="Ruta J",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62328.64547154153!2d74.35535591280196!3d31.549714100877228!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391903d101c157e3:0x9d99efc567f4eb7e!2sLahore,+Pakistan!5e0!3m2!1ses-419!2sco!4v1731820582911!5m2!1ses-419!2sco",
        velocidad=55,
        nivel_combustible=85,
        kilometraje=22000,
        temperatura_motor=88,
        comportamiento_conduccion="Normal"
    ),
    vehiculo(
        id=11,
        nombre="Camioneta 203",
        conductor="Manuel Ortiz",
        status="Disponible",
        ruta="Ruta K",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62328.64547154153!2d74.35535591280196!3d31.549714100877228!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391903d101c157e3:0x9d99efc567f4eb7e!2sLahore,+Pakistan!5e0!3m2!1ses-419!2sco!4v1731820582911!5m2!1ses-419!2sco",
        velocidad=0,
        nivel_combustible=60,
        kilometraje=3000,
        temperatura_motor=0,
        comportamiento_conduccion="No aplica"
    ),
    vehiculo(
        id=12,
        nombre="Camión 106",
        conductor="Ricardo Vargas",
        status="En tránsito",
        ruta="Ruta L",
        localizacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62328.64547154153!2d74.35535591280196!3d31.549714100877228!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391903d101c157e3:0x9d99efc567f4eb7e!2sLahore,+Pakistan!5e0!3m2!1ses-419!2sco!4v1731820582911!5m2!1ses-419!2sco",
        velocidad=65,
        nivel_combustible=50,
        kilometraje=35000,
        temperatura_motor=92,
        comportamiento_conduccion="Precaución"
    )
]

Estados = ["En movimiento", "En tránsito", "Disponible", "En revisión", "En pausa"]

# Crea un diccionario de vehículos, utilizando el 'id' de cada vehículo como clave
vehiculos_dict = {v.id: v for v in vehiculos_db}

# Función que retorna la lista completa de vehículos
def getVehiculos():
    return vehiculos_db

# Función que busca un vehículo por su 'id' en el diccionario y lo retorna
def getVehiculoId(id):
    return vehiculos_dict.get(id)

def setVehiculoId(vehiculo):
    
    if getVehiculoId(vehiculo.id):
        vehiculos_dict.get(vehiculo.id).nombre = vehiculo.nombre
        vehiculos_dict.get(vehiculo.id).conductor = vehiculo.conductor
        vehiculos_dict.get(vehiculo.id).status = vehiculo.status
        vehiculos_dict.get(vehiculo.id).ruta = vehiculo.ruta
        vehiculos_dict.get(vehiculo.id).velocidad = vehiculo.velocidad
        vehiculos_dict.get(vehiculo.id).nivel_combustible = vehiculo.nivel_combustible
        vehiculos_dict.get(vehiculo.id).kilometraje = vehiculo.kilometraje
        vehiculos_dict.get(vehiculo.id).temperatura_motor = vehiculo.temperatura_motor
        vehiculos_dict.get(vehiculo.id).comportamiento_conduccion = vehiculo.comportamiento_conduccion
        
        return True
    else:
        return False
    
def deleteVehiculoId(id):
    vehiculos_dict.pop(id)