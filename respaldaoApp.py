from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/ver_form', methods=['GET', 'POST'])
def ver_form():  # put application's code here
    if request.method == 'POST':
        if 'vehicle1' in request.form:
            vehicle1 = request.form['vehicle1']
        else:
            vehicle1 = None

        if 'vehicle2' in request.form:
            vehicle2 = request.form['vehicle2']
        else:
            vehicle2 = None

        if 'vehicle3' in request.form:
            vehicle3 = request.form['vehicle3']
        else:
            vehicle3 = None

        if 'fav_language' in request.form:
            radio = request.form['fav_language']
        else:
            radio = None
        cdx = {
        'nombre': request.form['fname'],
        'apellido': request.form['lname'],
        'vehiculo1': vehicle1,
        'vehiculo2': vehicle2,
        'vehiculo3': vehicle3,
        'radio': radio

    }
    return render_template("ver_form.html", cdx=cdx)

@app.route('/ver_datos')
def ver_datos():  # put application's code here
    arreglo = ["manzana", "pera", "durazno", "higo", "ciruela"]
    diccionario = {"Ana":87, "Juan":90.2, "Miguel":60, "Pedro":78}
    cdx = {
        "var1": 123.45,
        "arreglo": arreglo,
        "dicci":diccionario
    }
    return render_template("ver_datos.html", cdx=cdx)

@app.route('/ver_arreglo/<int:pos>/')
def ver_arreglo(pos):  # put application's code here

    return f"posición {arreglo[pos]}"

arreglo = ["manzana", "pera", "durazno", "higo", "ciruela"]


if __name__ == '__main__':
    app.run()
