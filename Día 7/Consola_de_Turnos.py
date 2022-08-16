class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'El cliente es {self.nombre} {self.apellido}\nBalance de cuenta: {self.balance}'

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Saldo insuficiente")

#Código para elegir depositar, retirar o salir

def crear_cliente():
    nombre_cl = input('Ingrese su nombre: ')
    apellido_cl = input('Ingrese su apellido: ')
    numero_cuenta = input('Ingrese su número de cuenta: ')
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio():
   mi_cliente = crear_cliente()
   opcion = 0

   while opcion != 'S':
       deposito = 'D'
       Retiro = 'R'
       Salir = 'S'
       print(f'Elije: \nDepositar {deposito},\nRetirar {Retiro} o \nSalir {Salir}:\n')
       opcion = input().upper()

       if opcion == 'D':
           monto_deposito = int(input("Monto a depositar: "))
           mi_cliente.depositar(monto_deposito)
       elif opcion == 'R':
           monto_retiro = int(input("Monto a retirar: "))
           mi_cliente.retirar(monto_retiro)
           print(mi_cliente)

   print("Gracias por operar en Banco Python")

inicio()