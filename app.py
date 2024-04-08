from flask import Flask, render_template
import mysql.connector
from datetime import datetime, timedelta,date


from app import create_app,db

app = create_app()
app.app_context().push()


# esta funcion se usa para agregar un dia cuando estoy en el html
#
@app.template_filter('add_day')
def add_day(value):
    return (value + timedelta(days=1))

@app.route('/')
def inicio():
    return render_template('index.html')

# por ahora trabajamos en esta ruta (dejando la ruta principal en este archivo) 
# a futuro la idea es hacer las rutas más prolijas en  carpetas RESOURCES 
# lo hacermos así para poder debugear más fácil el front end

@app.route('/reservas')
def reservas():
    dias = 5
    diam =  date.today()
    fechas = diamando(diam, dias) 
    print(fechas)

   # dia2mando= diamando + datetime.timedelta(days=1)
    #print(diamando.strftime('%m / %d / %Y'))

    #return render_template("reservas.html", dia = diamando)
    return render_template("reservas.html", dia = fechas)

def diamando(tod,dias):
    fechas = []
    
    for ii in range(dias):
        tid = timedelta(days=ii)
        fech = str( tod + tid)
        fechas.append(fech)
#    print(fechas)
    return fechas

if __name__ == "__main__":

    
    app.run(debug=True, host = "0.0.0.0", port=5000)
    print("Hola! IT's ALIVEEEEEEE!!!")
