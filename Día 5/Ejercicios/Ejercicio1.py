def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma > 15:
        print(f'El número es {suma} y es mayor que 15')
    elif suma < 10:
        print(f'El número es {suma} y es menor que 10')
    elif suma < 15 and suma > 10:
        print(f'El número es {suma} y está entre 10 y 15')
    else:
        print('Inserte un número valido')

print(devolver_distintos(1,3,5))

#Otra solución

def devolver_distintos_rel(a,b,c):
    suma = a + b + c
    lista = [a,b,c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        list.sort()
        return lista[1]

print(devolver_distintos_rel(2,4,1))