from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cuadrado():
    area = None
    perimetro = None

    if request.method == 'POST':
        lado = float(request.form['lado'])
        area = lado * lado
        perimetro = 4 * lado

    return render_template('cuadrado.html', area=area, perimetro=perimetro)

if __name__ == '__main__':
    app.run(debug=True)