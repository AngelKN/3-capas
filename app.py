# Importación de módulos necesarios para el funcionamiento de la aplicación Flask
from flask import Flask, jsonify, send_from_directory, render_template, request
import os.path
import data.db as db  # Importando el módulo de lógica de la base de datos

# Creación de la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para servir imágenes desde el directorio 'img'
@app.route('/img/<imagen>')
def imagenes(imagen):
    # Devuelve la imagen solicitada desde el directorio 'img'
    return send_from_directory(os.path.join('img'), imagen)

# Ruta para servir archivos CSS desde el directorio 'styles'
@app.route("/styles/<archivocss>")
def css(archivocss):
    # Devuelve el archivo CSS solicitado desde el directorio 'styles'
    return send_from_directory(os.path.join('styles'), archivocss)

# Ruta para servir archivos JavaScript desde el directorio 'scripts'
@app.route("/scripts/<js>")
def js(js):
    # Devuelve el archivo JavaScript solicitado desde el directorio 'scripts'
    return send_from_directory(os.path.join('scripts'), js)

# Ruta principal para mostrar y seleccionar vehículos
@app.route('/', methods=['GET', 'POST'])
def get_vehicles():
    select = None  # Variable para almacenar el vehículo seleccionado
    if request.method == 'POST':  # Si el método de la solicitud es POST
        vehiculoId = request.form.get('vehiculoId')  # Obtener el ID del vehículo del formulario
        if vehiculoId:
            # Llamar a la función 'getVehiculoId' para obtener el vehículo con el ID proporcionado
            select = db.getVehiculoId(int(vehiculoId))
    
    # Renderizar la plantilla 'index.html' con los datos de vehículos y el vehículo seleccionado
    return render_template('index.html', db=db.vehiculos_db, select=select)

# Ejecutar la aplicación en modo de depuración si este script es el principal
if __name__ == '__main__':
    app.run(debug=True)
