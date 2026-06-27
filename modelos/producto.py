class Producto:
    def __init__(self,
        nombre: str,
        ingredientes: str, 
        precio: float,
        cantidad: int,
        disponible: bool
        ):


        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    def mostrar_informacion(self) -> str:
        return( 
            f"Nombre:{self.nombre} |"
            f"Ingredientes:{self.ingredientes} |"
            f"${self.precio:.2f} | "
            f"Stock: {self.cantidad}"
        )
        
    def __str__(self):
        return(
             f"{self.nombre} |"
             f"{self.ingredientes} |"
             f"${self.precio:.2f} |"
             f" Cantidad: {self.cantidad}"
        )