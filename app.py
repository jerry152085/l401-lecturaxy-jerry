from flask import Flask, render_template
import random  # Esto va a inventar los números

app = Flask(__name__)

@app.route('/')
def index():
    # Inventamos valores de X e Y entre -10 y 10 cada vez que entras
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    
    # Se los mandamos a tu pantalla principal
    return render_template('index.html', ejeX=ejeX, ejeY=ejeY)

# Nueva pestaña 1: Información de Datos (Vista Alternativa de tu compañero jfpc)
@app.route('/info')
def info():
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    return render_template('info.html', ejeX=ejeX, ejeY=ejeY)

# Nueva pestaña 2: Mensajes del Sistema
@app.route('/mensaje')
def mensaje():
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    return render_template('mensaje.html', ejeX=ejeX, ejeY=ejeY)
# Nueva pestaña 3: Visualización de Javier
# Ruta de compatibilidad para el proyecto de Javier
@app.route('/matrix')
def matrix():
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    return render_template('index.html', ejeX=ejeX, ejeY=ejeY)
@app.route('/javier')
def javier():
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    return render_template('javier.html', ejeX=ejeX, ejeY=ejeY)

# Nueva pestaña 4: Visualización de Luis
@app.route('/luis')
def luis():
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    return render_template('luis.html', ejeX=ejeX, ejeY=ejeY)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
