class Usuario:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.informacion_tarjeta_credito = {}
        self.puntos = 0

    def agregar_tarjeta_credito(self, marca, numero, vencimiento, cvv):
        self.informacion_tarjeta_credito = {
            "marca": marca,
            "numero": numero,
            "vencimiento": vencimiento,
            "cvv": cvv
        }

    def comprar_articulo(self, precio):
        if self.informacion_tarjeta_credito:
            self.puntos += precio // 10
            return True
        return False

    def canjear_puntos(self, puntos_requeridos):
        if self.puntos >= puntos_requeridos:
            self.puntos -= puntos_requeridos
            return True
        return False

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Premio:
    def __init__(self, nombre, puntos_requeridos):
        self.nombre = nombre
        self.puntos_requeridos = puntos_requeridos

usuarios = {}

def crear_usuario(nombre_usuario):
    if nombre_usuario not in usuarios:
        usuarios[nombre_usuario] = Usuario(nombre_usuario)
        print(f"Usuario '{nombre_usuario}' creado.")
    else:
        print("Nombre de usuario ya existe.")

def agregar_informacion_tarjeta(nombre_usuario, marca, numero, vencimiento, cvv):
    usuario = usuarios.get(nombre_usuario)
    if usuario:
        usuario.agregar_tarjeta_credito(marca, numero, vencimiento, cvv)
        print("Información de tarjeta agregada.")
    else:
        print("Usuario no encontrado.")

def comprar_articulo(nombre_usuario, precio):
    usuario = usuarios.get(nombre_usuario)
    if usuario:
        if usuario.comprar_articulo(precio):
            print("Compra exitosa.")
        else:
            print("Información de tarjeta faltante.")
    else:
        print("Usuario no encontrado.")

def canjear_puntos(nombre_usuario, puntos_requeridos):
    usuario = usuarios.get(nombre_usuario)
    if usuario:
        if usuario.canjear_puntos(puntos_requeridos):
            print("Puntos canjeados.")
        else:
            print("Puntos insuficientes.")
    else:
        print("Usuario no encontrado.")

productos = [
    Producto("Cafetera", 150),
    Producto("Bolso", 3000),
    Producto("Cama", 50),
    Producto("Computadora", 85000),
    Producto("Celular", 300),
    Producto("Camara", 5000),
    Producto("Disco duro", 2500)
]

premios = [
    Premio("Cafetera", 10),
    Premio("Bolso", 5),
    Premio("Cama", 20),
    Premio("Computadora", 50),
    Premio("Camara", 25),
    Premio("Celular", 30),
    Premio("Disco duro", 25)
]

while True:
    print("\n1. Crear Cuenta")
    print("2. Agregar Información de Tarjeta")
    print("3. Comprar Artículo")
    print("4. Canjear Puntos por Premio")
    print("5. Mostrar Productos")
    print("6. Mostrar Premios")
    print("7. Salir")
    
    eleccion = input("Seleccione una opción: ")
    
    if eleccion == "1":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        crear_usuario(nombre_usuario)
    elif eleccion == "2":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        marca = input("Ingrese la marca de la tarjeta: ")
        numero = input("Ingrese el número de tarjeta: ")
        vencimiento = input("Ingrese la fecha de vencimiento: ")
        cvv = input("Ingrese el CVV: ")
        agregar_informacion_tarjeta(nombre_usuario, marca, numero, vencimiento, cvv)
    elif eleccion == "3":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        usuario = usuarios.get(nombre_usuario)
        if usuario:
            print("Productos Disponibles:")
            for indice, producto in enumerate(productos, start=1):
                print(f"{indice}. {producto.nombre} - ${producto.precio}")
            eleccion_producto = int(input("Seleccione un producto para comprar: "))
            if 1 <= eleccion_producto <= len(productos):
                producto_seleccionado = productos[eleccion_producto - 1]
                comprar_articulo(nombre_usuario, producto_seleccionado.precio)
            else:
                print("Elección de producto inválida.")
        else:
            print("Usuario no encontrado.")
    elif eleccion == "4":
        nombre_usuario = input("Ingrese nombre de usuario: ")
        usuario = usuarios.get(nombre_usuario)
        if usuario:
            print("Premios Disponibles:")
            for indice, premio in enumerate(premios, start=1):
                print(f"{indice}. {premio.nombre} - {premio.puntos_requeridos} puntos")
            eleccion_premio = int(input("Seleccione un premio para canjear: "))
            if 1 <= eleccion_premio <= len(premios):
                premio_seleccionado = premios[eleccion_premio - 1]
                canjear_puntos(nombre_usuario, premio_seleccionado.puntos_requeridos)
            else:
                print("Elección de premio inválida.")
        else:
            print("Usuario no encontrado.")
    elif eleccion == "5":
        print("Productos Disponibles:")
        for indice, producto in enumerate(productos, start=1):
            print(f"{indice}. {producto.nombre} - ${producto.precio}")
    elif eleccion == "6":
        print("Premios Disponibles:")
        for indice, premio in enumerate(premios, start=1):
            print(f"{indice}. {premio.nombre} - {premio.puntos_requeridos} puntos")
    elif eleccion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción válida.")