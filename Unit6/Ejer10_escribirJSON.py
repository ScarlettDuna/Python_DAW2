import json
persona = {
    'nombre': 'Marta',
    'edad':28,
    'profesión': 'CM'
}

with open('files/persona.json', 'w', encoding='utf-8') as f:
    json.dump(persona, f, indent=4, ensure_ascii=False)
print('Fichero json generado correctamente')

with open('files/persona.json', 'r', encoding='utf-8') as f2:
    datos = json.load(f2)

datos['edad'] = 29
datos['ciudad'] = 'Madrid'

with open('files/persona.json', 'w', encoding='utf-8') as f3:
    json.dump(datos, f3, indent=4, ensure_ascii=False)
print('Fichero json actualizado correctamente')