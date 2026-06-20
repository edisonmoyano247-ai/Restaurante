from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

Producto1 = Producto(
    "Menú Mediterraneo",
    "Bruschetta de tomate y albahaca; Salmón al horno con costra de hierbas y vegetales rostizados; Yogur griego natural, miel, fresas, arándanos y granola",
    8.50
)

Producto2 = Producto(
    "Menú Mexicano",
    "Crema de elote (maíz) con un toque de chile poblano;Enchiladas verdes de pollo; Pastel de tres leche",
    7.85
)
Producto3 = Producto(
    "Menú Italiano",
    "Ensalada Caprese; Risotto de champiñones y setas silvestres; Tiramisú tradicional",
    9.00
)

cliente1 = Cliente("Edison Moyano", 
                   "0999888777")
cliente2 = Cliente("María José",
                    "0999555444")
cliente3 = Cliente("Mónica Arcos", 
                   "0999577744")


restaurante = Restaurante()

restaurante.agregar_producto(Producto1)
restaurante.agregar_producto(Producto2)
restaurante.agregar_producto(Producto3)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)
restaurante.agregar_cliente(cliente3)

print("Registrado en el sistema")

restaurante.mostrar_producto()
restaurante.mostrar_cliente()