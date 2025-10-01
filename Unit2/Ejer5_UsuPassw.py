# programa que pide un número de usuario y una contraseña, si se introduce pepe y pepepwd muestra "has entrado al sistema"

usuario = input("Introduce tu nombre de usuario")
passwd = input("Introduce tu contraseña")

if usuario == "pepe" and passwd == "pepepwd":
    print("Has entrado al sistema")
else:
    print("Usuario incorrecto")