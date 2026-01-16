DatosCliente = {
    'nombre': 'Carlos',
    'contacto': {
        'email': 'carlos@ejemplo.com',
        'telefono': '555.1234'
    },
    'pedidos': [
        {'id': 'P001',
         'total': 54.78},
        {'id': 'P002',
         'total': 23.54},
    ]
}

# Mostrar email
email_cliente = DatosCliente['contacto']['email']
print(f'Email: {email_cliente}')

totalPedido1 = DatosCliente['pedidos'][0]['total']
print(f'Total pedido 1: {totalPedido1}€')