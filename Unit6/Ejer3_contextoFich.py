# El estándar de python es usar with
# Su gran ventaja es que no es necesario en close()
with open("files/salida.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1: configuración inicial\n")
    f.write("Línea 2: proceso finalizado\n")
# Al llegar aquí el fichero se ha cerrado automáticamente
print("Fichero salida.txt generado correctamente")

# Concatenar
with open("files/salida.txt", "a", encoding="utf-8") as f:
    f.write("Línea 3: añadida desde append \n")
# varias líneas a la vez
dias = ["Lunes\n", "Martes\n", "Miércoles\n", "Jueves\n", "Viernes\n"]
with open("files/diasSemana.txt", "w", encoding="utf-8") as f:
    f.writelines(dias)
    