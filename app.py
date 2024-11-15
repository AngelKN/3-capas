from flask import Flask, jsonify, send_from_directory, render_template, request
import os.path
import logica.db as db


app = Flask(__name__)

@app.route('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('img'),imagen)

@app.route("/styles/<archivocss>")
def css(archivocss):
    return send_from_directory(os.path.join('styles'),archivocss)

@app.route("/scripts/<js>")
def js(js):
    return send_from_directory(os.path.join('scripts'),js)

@app.route('/', methods=['GET', 'POST'])
def get_vehicles():
    select = None
    if request.method == 'POST':
        vehiculoId = request.form.get('vehiculoId')
        if vehiculoId:
            select = db.getVehiculoId(int(vehiculoId))
    
    return render_template('index.html', db=db.vehiculos_db, select=select)

if __name__ == '__main__':
    app.run(debug=True)
