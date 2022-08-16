mi_bool = (4 < 5) and (5 > 6)
print(mi_bool)

operdor_or = (10 == 9) or (3 == 3)
print(operdor_or)

texto = "Frase breve"
mi_bool = ('Frase' in texto) and ('breve' in texto)
print(mi_bool)

mi_bool = ('Frase' in texto) or ('Python' in texto)
print(mi_bool)

mi_bool = not('a' == 'a')
print(mi_bool)

num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2) and (num1 < num3)
print(mi_bool)

num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2) or (num1 < num3)
print(mi_bool)

texto = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not((palabra1 in texto) and (palabra2 in texto))
print(mi_bool)

