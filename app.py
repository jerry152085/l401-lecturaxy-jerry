import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Genera valores aleatorios entre -100 y 100 para los ejes simulando el hardware
    ejeX = random.randint(-100, 100)
    ejeY = random.randint(-100, 100)
    
    # Renderiza la matriz pasando las variables necesarias
    return render_template('index.html', ejeX=ejeX, ejeY=ejeY)

@app.route('/mensaje')
def mensaje():
    ejeX = random.randint(-100, 100)
    ejeY = random.randint(-100, 100)
    return render_template('mensaje.html', ejeX=ejeX, ejeY=ejeY)

@app.route('/info')
def info():
    ejeX = random.randint(-100, 100)
    ejeY = random.randint(-100, 100)
    return render_template('info.html', ejeX=ejeX, ejeY=ejeY)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
