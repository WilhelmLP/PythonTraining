#Diccionarios
#Sirven para almacenar valores sin conocer su ubicación exacta, sino su relación con
#una clave que debe de ser unica y exacta

diccionario = {'c1': 'Valor1', 'c2': 'Valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'Guillermo', 'apellido': 'Linares', 'peso': 125, 'talla': 1.68}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}, 'c4': True}
print(dic['c2'][1])

dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2['c2'][1].upper())

#Agregar elementos al diccionario o modificarlos
dic3 = {1: 'a', 2: 'b', 3: 'c'}
print(dic3)

dic3[4] = 'D'
print(dic3)

dic3[2] = 'B'
print(dic3)

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

#Conocer las llaves y claves
print(dic3.keys())
print(dic3.values())
print(dic3.items())

mi_dic = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])