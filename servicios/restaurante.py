class Restaurante:

    def __init__(self):
        
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente) -> None:
        self.clientes.append(cliente)

       
    def mostrar_producto(self):
        print("\n---MENÚ DEL RESTAURANTE---")
        for producto in self.productos:
            print(producto)

    def mostrar_cliente(self):
        print("\n---CLIENTES REGISTRADOS---")
        for cliente in self.clientes:
            print(cliente)
    


