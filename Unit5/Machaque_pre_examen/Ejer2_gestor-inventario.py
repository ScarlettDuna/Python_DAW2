productos = {"manzanas": 10, "peras": 5}

def gest_inventario(producto, cantidad):
    if producto in productos:
        productos[producto] += cantidad
    else:
        productos[producto] = cantidad

gest_inventario('zanahorias', 8)
gest_inventario('peras', 6)
print(productos)