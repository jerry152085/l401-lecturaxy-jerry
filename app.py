from flask import Flask, render_template
import random  # Esto va a inventar los números

app = Flask(__name__)

@app.route('/')
def index():
    # Inventamos valores de X e Y entre -10 y 10 cada vez que entras
    ejeX = round(random.uniform(-10.0, 10.0), 2)
    ejeY = round(random.uniform(-10.0, 10.0), 2)
    
    # Se los mandamos a tu pantalla
    return render_template('index.html', ejeX=ejeX, ejeY=ejeY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
