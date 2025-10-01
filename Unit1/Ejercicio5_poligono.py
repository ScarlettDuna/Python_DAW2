# Perímetro de un polígono, dada una base b y una altura h, es igual a
base = float(input("Dime la base: "))
altura = float(input("Dime la altura: "))
perimetro = base * 2 + altura * 2
area = base * altura

print("Resultado: \nArea: ", area, "\nPerímetro: ", perimetro)
# ("Resultado: \nArea: %f \nPerímetro: %f" %(area, perimetro))
# print("Resultado: \nArea: %d \nPerímetro: %d" %(area, perimetro))

print(f"Resultado: \nArea= {area:.2f} \nPerímetro= {perimetro:.2f}")