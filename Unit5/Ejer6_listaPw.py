lista=["1234", "admin", "password", "segura", "admin123", "secreta", "admin"]
print("Lista de contraseñas actuales: ", lista)
password = input("Introduce tu contraseña")
if password in lista:
    print("Esa contraseña ya la has usado: ", lista.count(password), " veces")
    # Pide una nueva contraseña y cambiala por esta repetida
    password = input("Introduce una contraseña deferente")
    if password not in lista:
        lista[lista.index("admin")] = password

else:
    print("Muy bien, nueva contraseña")