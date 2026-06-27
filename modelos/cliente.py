class Cliente:

    def __init__(
        self, 
        nombre: str,
        telefono: int,
        frecuente:bool
        ):

        self.nombre = nombre
        self.telefono = telefono
        self.frecuente = frecuente
    
    def mostrar_informacion(self) -> str:
        return(
            f"Cliente: {self.nombre} |"
            f"Teléfono: {self.telefono} |"
            f"Frecuente: {self.frecuente}"
        )
    
    def __str__(self)-> str:
        return(
             f"{self.nombre}"
             f"(Tel: {self.telefono}) | "
             f"Frecuente: {self.frecuente}"
        )