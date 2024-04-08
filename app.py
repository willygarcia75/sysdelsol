from flask import Flask, render_template, request
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


@app.route('/form', methods=['GET', 'POST'])
def loginForm():
    resultado ="Falso"
    if request.method == 'POST':
        usuario           = request.form['usuario']
        contraseña        = request.form['contraseña']
        if usuario == "admin" and contraseña=="1234":
            resultado = "Verdadero"
        
        # en la siguiente linea estaba devolviendo resultado para usar un "if" en el html
        # pero no es necesario porque estoy usando el if acá mismo o sea el "resultado=resultado"
        # return render_template('selectturno.html', resultado=resultado)
        # ahora para probar devuelvo "contador"
            # contador = leerdb()
           # print(leerdbturnos())
           # contador=1234 #esto hay que sacarlo

            # return render_template('selectturno.html')
            return render_template('reservas.html')
        else:
            return render_template('loggin.html', msg = "Login Incorrecto")
    else:
#        return render_template('loggin.html', msg = "Login Pero con GET")
        return render_template('loggin.html')


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
