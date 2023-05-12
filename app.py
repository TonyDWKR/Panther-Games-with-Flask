from flask import Flask, render_template, request, redirect, session
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="panthergames"
)
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        user = mycursor.fetchone()
        mydb.commit()
        if user:
            print("ENTRO")
            return render_template('index.html')
        else:
            error = 'Nombre de usuario o contraseña incorrectos'
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/')
def index():  # put application's code here
    return render_template("login.html")


#          _  _               _
#         | |(_)             | |
#     ___ | | _   ___  _ __  | |_  ___  ___
#    / __|| || | / _ \| '_ \ | __|/ _ \/ __|
#   | (__ | || ||  __/| | | || |_|  __/\__ \
#    \___||_||_| \___||_| |_| \__|\___||___/
#
#

@app.route('/cliente_show')
def cliente_show():  # put application's code here
    mycursor.execute("SELECT * FROM clientes")
    myresult = mycursor.fetchall()
    cdx = {
        'clientes': myresult
    }
    return render_template("cliente_all/cliente_show.html", cdx=cdx)


@app.route('/cliente_add', methods=['GET', 'POST'])
def cliente_add():  # put application's code here
    if request.method == 'GET':
        return render_template("cliente_all/cliente_add.html")
    elif request.method == 'POST':
        sql = "INSERT INTO Clientes (nombreCliente, apellidoCliente, email, nombreUsuario, esMiembro) VALUES (%s, %s, %s, %s, %s)"

        checked = 'esMiembro' in request.form
        print(checked)
        if checked:
            esMiembro = 1
        else:
            esMiembro = 0

        val = (request.form['nombre'], request.form['apellido'], request.form['email'], request.form['nombreUsuario'],
               esMiembro,)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


@app.route('/cliente_delete/<int:id>/')
def cliente_delete(id):  # put application's code here
    sql = "DELETE FROM Clientes WHERE id_cliente = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    mydb.commit()
    return redirect("/cliente_show")


@app.route('/cliente_change/<int:id>/', methods=['GET', 'POST'])
def cliente_change(id):  # put application's code here
    if request.method == 'GET':
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM Clientes WHERE id_cliente ='{id}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(f"myresult ={myresult[0]}")
        clientes = myresult[0]
        cdx = {
            'id': clientes[0],
            'nombre': clientes[1],
            'apellido': clientes[2],
            'email': clientes[3],
            'nombreUsuario': clientes[4],
            'esMiembro': clientes[5]
        }
        return render_template("cliente_all/cliente_change.html", cdx=cdx)
    elif request.method == 'POST':
        mycursor = mydb.cursor()
        checked = 'esMiembro' in request.form
        print(checked)
        if checked:
            esMiembro = 1
        else:
            esMiembro = 0
        sql = f"UPDATE Clientes SET nombreCliente = %s, apellidoCliente = %s, email = %s, nombreUsuario = %s, esMiembro = %s  WHERE id_cliente = %s"
        val = (request.form['nombre'], request.form['apellido'], request.form['email'], request.form['nombreUsuario'],
               esMiembro, id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


#           _      _               _
#          (_)    | |             (_)
#   __   __ _   __| |  ___   ___   _  _   _   ___   __ _   ___   ___
#   \ \ / /| | / _` | / _ \ / _ \ | || | | | / _ \ / _` | / _ \ / __|
#    \ V / | || (_| ||  __/| (_) || || |_| ||  __/| (_| || (_) |\__ \
#     \_/  |_| \__,_| \___| \___/ | | \__,_| \___| \__, | \___/ |___/
#                                _/ |               __/ |
#                               |__/               |___/

@app.route('/videojuego_show')
def videjuego_show():  # put application's code here
    mycursor.execute("SELECT * FROM videojuegos")
    myresult = mycursor.fetchall()
    cdx = {
        'videojuegos': myresult
    }
    return render_template("videojuego_all/videojuego_show.html", cdx=cdx)


@app.route('/videojuego_delete/<int:id>/')
def videojuego_delete(id):  # put application's code here
    sql = "DELETE FROM Videojuegos WHERE id_videojuego = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    mydb.commit()
    return redirect("/videojuego_show")


@app.route('/videojuego_add', methods=['GET', 'POST'])
def videojuego_add():  # put application's code here
    if request.method == 'GET':
        return render_template("videojuego_all/videojuego_add.html")
    elif request.method == 'POST':
        sql = "INSERT INTO Videojuegos (nombreVideojuego, desarrolladorVideojuego, clasificaciónVideojuego, añoSalidaVideojuego) VALUES (%s, %s, %s, %s)"
        val = (
        request.form['nombre'], request.form['desarrollador'], request.form['clasificacion'], request.form['añoSalida'])
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


@app.route('/videojuego_change/<int:id>/', methods=['GET', 'POST'])
def videojuego_change(id):  # put application's code here
    if request.method == 'GET':
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM Videojuegos WHERE id_videojuego ='{id}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(f"myresult ={myresult[0]}")
        videojuegos = myresult[0]
        cdx = {
            'id': videojuegos[0],
            'nombre': videojuegos[1],
            'desarrollador': videojuegos[2],
            'clasificacion': videojuegos[3],
            'añoSalida': videojuegos[4],
        }
        return render_template("videojuego_all/videojuego_change.html", cdx=cdx)
    elif request.method == 'POST':
        mycursor = mydb.cursor()
        sql = f"UPDATE Videojuegos SET nombreVideojuego = %s, desarrolladorVideojuego = %s, clasificaciónVideojuego = %s, añoSalidaVideojuego = %s WHERE id_videojuego = %s"
        val = (
        request.form['nombre'], request.form['desarrollador'], request.form['clasificacion'], request.form['añoSalida'],
        id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


#               _                   _
#              (_)                 | |
#    _ __ ___   _   ___  _ __ ___  | |__   _ __  ___   ___
#   | '_ ` _ \ | | / _ \| '_ ` _ \ | '_ \ | '__|/ _ \ / __|
#   | | | | | || ||  __/| | | | | || |_) || |  | (_) |\__ \
#   |_| |_| |_||_| \___||_| |_| |_||_.__/ |_|   \___/ |___/
#
#
@app.route('/miembro_show')
def miembro_show():  # put application's code here
    mycursor.execute("SELECT * FROM Miembros")
    myresult = mycursor.fetchall()
    cdx = {
        'miembros': myresult
    }
    return render_template("miembro_all/miembro_show.html", cdx=cdx)


@app.route('/miembro_delete/<int:id>/')
def miembro_delete(id):  # put application's code here
    sql = "DELETE FROM Miembros WHERE id_miembro = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    mydb.commit()
    return redirect("/miembro_show")


@app.route('/miembro_add', methods=['GET', 'POST'])
def miembro_add():  # put application's code here
    if request.method == 'GET':
        sql = f"SELECT id_cliente FROM Clientes"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        cdx = {
            'clientes': myresult
        }
        return render_template("miembro_all/miembro_add.html", cdx=cdx)
    elif request.method == 'POST':
        sql = "INSERT INTO Miembros (id_cliente, miembroDesde, miembroHasta) VALUES (%s, %s, %s)"
        val = (request.form['id_cliente'], request.form['miembroDesde'], request.form['miembroHasta'])
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


@app.route('/miembro_change/<int:id>/', methods=['GET', 'POST'])
def miembro_change(id):  # put application's code here
    if request.method == 'GET':
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM Miembros WHERE id_miembro ='{id}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(f"myresult ={myresult[0]}")
        miembros = myresult[0]
        cdx = {
            'id': miembros[0],
            'id_cliente': miembros[1],
            'miembroDesde': miembros[2],
            'miembroHasta': miembros[3],
        }

        sql = f"SELECT id_cliente FROM Clientes"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        cdxCliente = {
            'clientes': myresult
        }

        return render_template("miembro_all/miembro_change.html", cdx=cdx, cdxCliente=cdxCliente)
    elif request.method == 'POST':
        mycursor = mydb.cursor()
        sql = f"UPDATE Miembros SET id_cliente = %s, miembroDesde = %s, miembroHasta = %s WHERE id_miembro = %s"
        val = (request.form['id_cliente'], request.form['miembroDesde'], request.form['miembroHasta'], id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


#                       _
#                      | |
#   __   __ ___  _ __  | |_  __ _  ___
#   \ \ / // _ \| '_ \ | __|/ _` |/ __|
#    \ V /|  __/| | | || |_| (_| |\__ \
#     \_/  \___||_| |_| \__|\__,_||___/
#
#
@app.route('/venta_show')
def venta_show():  # put application's code here
    mycursor.execute("SELECT * FROM Ventas")
    myresult = mycursor.fetchall()
    cdx = {
        'ventas': myresult
    }
    return render_template("venta_all/venta_show.html", cdx=cdx)


@app.route('/venta_delete/<int:id>/')
def venta_delete(id):  # put application's code here
    sql = "DELETE FROM Ventas WHERE id_venta = %s"
    adr = (id,)
    mycursor.execute(sql, adr)
    mydb.commit()
    return redirect("/venta_show")


@app.route('/venta_add', methods=['GET', 'POST'])
def venta_add():  # put application's code here
    if request.method == 'GET':
        sql = f"SELECT nombreCliente FROM Clientes"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        cdx = {
            'clientes': myresult
        }
        sql = f"SELECT nombreVideojuego FROM Videojuegos"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        cdx2 = {
            'videojuegos': myresult
        }
        return render_template("venta_all/venta_add.html", cdx=cdx, cdx2=cdx2)
    elif request.method == 'POST':
        sql = "INSERT INTO Ventas (nombreVideojuego, nombreCliente, precioUnitario, cantidad, precioFinal, fechaVenta) VALUES (%s, %s, %s, %s, %s, %s)"

        precioUnitario = request.form.get("precioUnitario")

        cantidad = request.form.get("cantidad")

        precioTotal = float(precioUnitario) * int(cantidad)

        val = (request.form['nombreVideojuego'], request.form['nombreCliente'], request.form['precioUnitario'],
               request.form['cantidad'], precioTotal, request.form['fechaVenta'])
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."


@app.route('/venta_change/<int:id>/', methods=['GET', 'POST'])
def venta_change(id):  # put application's code here
    if request.method == 'GET':
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM Ventas WHERE id_venta ='{id}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(f"myresult ={myresult[0]}")
        ventas = myresult[0]
        cdx = {
            'id': ventas[0],
            'nombreVideojuego': ventas[1],
            'nombreCliente': ventas[2],
            'precioUnitario': ventas[3],
            'cantidad': ventas[4],
            'precioFinal': ventas[5],
            'fechaVenta': ventas[6]
        }

        sql = f"SELECT nombreCliente FROM Clientes"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        cdxCliente = {
            'clientes': myresult
        }

        sql = f"SELECT nombreVideojuego FROM Videojuegos"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        cdxVideojuegos = {
            'videojuegos': myresult
        }

        return render_template("venta_all/venta_change.html", cdx=cdx, cdxCliente=cdxCliente,
                               cdxVideojuegos=cdxVideojuegos)
    elif request.method == 'POST':
        mycursor = mydb.cursor()
        sql = f"UPDATE Ventas SET nombreVideojuego = %s, nombreCliente = %s, precioUnitario = %s, cantidad = %s, precioFinal = %s, fechaVenta = %s WHERE id_venta = %s"
        precioUnitario = request.form.get("precioUnitario")

        cantidad = request.form.get("cantidad")

        precioTotal = float(precioUnitario) * int(cantidad)
        val = (request.form['nombreVideojuego'], request.form['nombreCliente'], request.form['precioUnitario'],
               request.form['cantidad'], precioTotal, request.form['fechaVenta'], id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/home")
    else:
        return "Metodo no compatible..."
