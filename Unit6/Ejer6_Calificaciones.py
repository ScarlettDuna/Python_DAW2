total = 0
media = 0
masAlta = 0
masBaja = 10
contador = 0
with (open("files/notas.txt", "r", encoding="utf-8") as notas,
      open("files/resultados.txt", "w", encoding="utf-8") as resultados):
    for line in notas:
        nota = float(line.split(',')[1])
        total += nota
        contador += 1
        if nota > masAlta: masAlta = nota
        if nota < masBaja: masBaja = nota

    if contador != 0: media = total / contador
    resultados.writelines(f"Nota más alta {masAlta} \nNota más baja: {masBaja} \nMedia: {media}")