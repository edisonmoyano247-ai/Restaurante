from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    producto1 = Producto(
        "Menú Mediterraneo",
        "Bruschetta de tomate y albahaca; Salmón al horno con costra de hierbas y vegetales rostizados; Yogur griego natural, miel, fresas, arándanos y granola",
        8.50,
        2,
        True
    )

    producto2 = Producto(
        "Menú Mexicano",
        "Crema de elote (maíz) con un toque de chile poblano;Enchiladas verdes de pollo; Pastel de tres leche",
        7.85,
        1,
        False
    )

    producto3 = Producto(
        "Menú Italiano",
        "Ensalada Caprese; Risotto de champiñones y setas silvestres; Tiramisú tradicional",
        9.00,
        10,
        True
    )

    cliente1 = Cliente(
        "Edison Moyano", 
        "0999888777",
        True
    )
    cliente2 = Cliente(
        "María José",
        "0999555444",
        False
    )
    cliente3 = Cliente(
        "Mónica Arcos", 
        "0999577744",
        True
    )


    restaurante = Restaurante()

    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    restaurante.agregar_cliente(cliente3)

    print("Producto registrado en el sistema")
    restaurante.mostrar_producto()

    print("Cliente registrado en el sistema")
    restaurante.mostrar_cliente()

if __name__ == "__main__":
    main()