from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel
productosModel = ProductosModel()
@app.route("/productos")
def productos():
    productosModel = ProductosModel()

    productos = productosModel.traerTodos()

    

    return render_template("productos/index.html", productos = productos)

@app.route('/productos/crear',methods= ['GET', 'POST'])
def crear_producto():
    #Esta función me sirve para mostrar el formulario de cración
    #Y también para crear un nuevo producto
    #Estos pasos se identifican con los metodos

    if request.method == 'GET':
        #Mostramos el formulario de creación
        return render_template("productos/crear.html")
    

    #Acá se muestra la creación del producto        
    nombre = request.form.get('nombre')
    

    
    productosModel.crear(nombre)

    return redirect(url_for('productos'))
