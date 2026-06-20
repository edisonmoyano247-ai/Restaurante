# modelos/producto.py

class Producto:
    def __init__(self, nombre, ingredientes, precio):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} | {self.ingredientes} | {self.precio}"
        
    def __str__(self):
        return f"{self.nombre}  {self.ingredientes}  {self.precio}"