"""
Unittest es un modulo de Python que sirve para probar el código y así hacer pruebas unitarias
"""
import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen día'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'Buen Día')


if __name__ == '__main__':
    unittest.main()


