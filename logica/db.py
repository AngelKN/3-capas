from logica.vehiculo import vehiculo

vehiculos_db = [
    vehiculo(id=1, nombre="Camión 101", conductor="Carlos López", status="En movimiento", ruta="Ruta A", localizacion="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3024.2369522068784!2d-74.00857492409725!3d40.71279997139341!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zNDDCsDQyJzQ2LjEiTiA3NMKwMDAnMjEuNiJX!5e0!3m2!1ses!2sco!4v1731683106815!5m2!1ses!2sco"),
    vehiculo(id=2, nombre="Camión 102", conductor="Ana García", status="En mantenimiento", ruta="Ruta B", localizacion="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3305.6752736291683!2d-118.24627492441799!3d34.052199973157066!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMzTCsDAzJzA3LjkiTiAxMTjCsDE0JzM3LjMiVw!5e0!3m2!1ses!2sco!4v1731683705175!5m2!1ses!2sco"),
    vehiculo(id=3, nombre="Camioneta 201", conductor="Luis Pérez", status="Disponible", ruta="Ruta C", localizacion="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d2483.3170028598324!2d-0.1303749234808934!3d51.507399971813385!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zNTHCsDMwJzI2LjYiTiAwwrAwNyc0MC4xIlc!5e0!3m2!1ses!2sco!4v1731683774230!5m2!1ses!2sco"),
    vehiculo(id=4, nombre="Camioneta 202", conductor="María Herrera", status="En movimiento", ruta="Ruta D", localizacion="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d2625.084451493611!2d2.3496250763575826!3d48.85659997133188!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zNDjCsDUxJzIzLjgiTiAywrAyMScwNy45IkU!5e0!3m2!1ses!2sco!4v1731683800637!5m2!1ses!2sco"),
    vehiculo(id=5, nombre="Furgoneta 301", conductor="José Rivera", status="En carga", ruta="Ruta E", localizacion="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3240.492349171298!2d139.68912507565628!3d35.68949997258458!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMzXCsDQxJzIyLjIiTiAxMznCsDQxJzMwLjEiRQ!5e0!3m2!1ses!2sco!4v1731683831484!5m2!1ses!2sco"),
]

vehiculos_dict = {v.id: v for v in vehiculos_db}

def getVehiculos():
    return vehiculos_db
    
def getVehiculoId(id):
    return vehiculos_dict.get(id)