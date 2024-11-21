inventario = []
ventas =[]
agotados = []
id_producto = 0

## agregue un producto al inventario con sus caracteristicas
def agregar_producto(nombre, precio, stock, categoria):
  global id_producto
  id_producto += 1
  inventario.append({'id':id_producto,'nombre': nombre, 'precio': precio, 'stock': stock, 'categoría': categoria})
  print(f"\nproducto agregado con ID: {id_producto}")

##elimina un producto del inventario por su id
def eliminar_productos(inventario, id_producto):
    global agotados 
    encontrado = False
    for producto in inventario:
        if producto["id"] == id_producto:
            inventario.remove(producto)
            print(f"\nProducto con ID {id_producto} eliminado :) ")
            encontrado = True
            if producto["stock"] == 0:
                agotados.append(producto["nombre"])
            break
    if not encontrado:
        print(f"\nno se encontro producto con el ID: {id_producto}")

##realiza una venta
def venta(cantidad, id_producto):  
    producto_encontrado = False
    for producto in inventario:
        if producto["id"] == id_producto:
            producto_encontrado = True
            if producto["stock"] >= cantidad:
                #calculo el precio total de la venta
                precio_total = producto["precio"] * cantidad
                #descuento el stock del producto
                producto["stock"] -= cantidad
                #agrego la venta a la lista de ventas
                ventas.append({"id producto": id_producto, "nombre": producto["nombre"], "cantidad": cantidad, "precio unitario": producto["precio"], "precio total": precio_total})
                print(f"\nventa realizada: {cantidad} unidades de {producto['nombre']} a ${producto['precio']} c/u. en total: ${precio_total}.")
                #verifico si el producto se agoto
                if producto["stock"] == 0:
                    agotados.append(producto['nombre'])
            else:
                print("\nNo hay suficiente stock para realizar la venta.")
            break
    if not producto_encontrado:
        print(f"\nNo se encontro un producto con ID {id_producto}.")

#actualiza el stock de un producto con el id :3
def actualizar_stock(id_producto, nuevo_stock):
    producto_encontrado = False
    for producto in inventario:
        if producto['id'] == id_producto:
            producto['stock'] += nuevo_stock  #actualiza el stock que no sumaba al stock anterior
            print(f"\nEl stock del producto con ID {id_producto} ha sido actualizado a {producto['stock']}.")
            producto_encontrado = True
            #si el stock es 0, el producto se agrega a la lista agotados
            if producto['stock'] == 0:
                agotados.append(producto['nombre'])
            break
    if not producto_encontrado:
        print(f"\nNo se encontró un producto con ID {id_producto}.")

#mostrar inventarioactualizado
def inventario_actualizado():
    print("\nInventario Actual:")
    if inventario:
        for producto in inventario:
            print(f"id: {producto['id']} - nombre: {producto['nombre']} - stock: {producto['stock']}")
    else:
        print("\nNo hay productos en el inventario.")

#Informe de Inventario
def informe(stock, agotados, ventas):
    print("\nInforme de Inventario")
    print("="*30)

    # Verifico stock
    print("\nProductos en Stock:")  #si hay productos muestro el stock
    if stock:
        for producto in stock:
            print(f"ID: {producto['id']} - nombre: {producto['nombre']} - stock: {producto['stock']}")
    else:
        print("\nNo hay productos en stock.")  #por si no hay productos

    # Productos agotados
    print("\nProductos Agotados:")  #imprimo agotados
    if agotados:
        for producto in agotados:
            print(f" - {producto}")
    else:
        print("\nNo hay productos agotados.")

    #ventas realizadas
    print("\nVentas Realizadas:")  #si hubo ventas informo
    if ventas:
        ingreso_total = 0
        for venta in ventas:
            print(f"- {venta['nombre']} x{venta['cantidad']} vendidos a ${venta['precio total']} cada uno ")
            ingreso_total += venta['cantidad'] * venta['precio total']
            
    else:
        print("\nNo hay ventas registradas.")

    print("="*30)


def menu():
    print("\n** gestion de inventario** ")
    print("1. Agregar un producto")
    print("2. Eliminar un producto")
    print("3. Realizar venta")
    print("4. Actualizar stock")
    print("5. imprimir inventario") #se comieron esta opcion 
    print("6. Ver informe de inventario")
    print("7. Salir")
    return input("\nseleccione una opcion: ")

def gestionar_inventario():
    while True:
        opcion = menu()

        if opcion == "1": #agregar
            nombre = str(input("\ningrese nombre del producto: "))
            precio = float(input("ingrese precio del producto: "))
            stock = int(input("ingrese cantidad de unidades: "))
            categoria = str(input("ingrese la categoria del producto: "))
            agregar_producto(nombre, precio, stock, categoria)


        elif opcion == "2": #eliminar
            id_producto_a_eliminar = int(input("\ningrese el ID del producto a eliminar: "))
            eliminar_productos(inventario, id_producto_a_eliminar)

        elif opcion == "3": #venta
            id_producto = int(input("\ningrese el ID del producto a vender: "))
            cantidad = int(input("ingrese la cantidad de unidades a vender: "))
            venta(cantidad, id_producto)

        elif opcion == "4": #actualizar stock
            id_producto_a_actualizar = int(input("\ningrese el ID del producto a actualizar: "))
            nuevo_stock = int(input("ingrese stock a agregar: "))
            actualizar_stock(id_producto_a_actualizar, nuevo_stock)
            
        elif opcion == "5": #imprimir inventario
            inventario_actualizado()

        elif opcion == "6":
            informe(inventario, agotados, ventas)

        elif opcion == "7": #cerrar aplicacion
            print("******cerrando la aplicacion*******")
            break
        else: #por si acaso
            print("\n****la opcion ingresada no es valida >:( \n ¡¡¡¡¡¡¡¡ingrese una opcion correcta!!!!!!!!!!!!!")

#programa principal:
gestionar_inventario()