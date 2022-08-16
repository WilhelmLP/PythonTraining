import datetime

mi_hora = datetime.time(17, 35, 50, 1500)
print(mi_hora)

mi_dia = datetime.date(2022, 7, 24)
print(mi_dia)
print(mi_dia.ctime())
print(mi_dia.today())

mi_fecha_hora = datetime.datetime(2065, 5, 15, 22, 10, 15, 2500)
print(mi_fecha_hora)

mi_fecha_hora = mi_fecha_hora.replace(month = 12)
print(mi_fecha_hora)

#Calculando edad
nacimiento = datetime.date(1995, 3, 5)
defuncion = datetime.date(2095, 6, 19)

vida = defuncion - nacimiento
print(vida)

#Calculando horas de descanso
despierta = datetime.datetime(2022, 10, 5, 7, 30)
duerme = datetime.datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia.seconds)

#minutos = datetime.time(20, 43, 17)
minutos = datetime.datetime.now().minute
print(minutos)