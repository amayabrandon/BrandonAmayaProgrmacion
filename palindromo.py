import unittest

def es_palindromo(letra):
  palindromo=[]
  # Convertir a minúsculas texto ingresado
  letra=letra.lower()
  # eliminar espacios, puntos y comas
  for x in letra:
    palindromo.append(x)

  palindromo = [x for x in palindromo if x != " " and x != "." and x != ","and x != ":"]
  # Invertir la palabra procesada
  comparacion = palindromo[::-1]
  # Comparar si la palabra es igual a su inversa
  return palindromo==comparacion

class TestPalindromo(unittest.TestCase):
    def test_palindromo_simple(self):
        self.assertTrue(es_palindromo("radar"))

    def test_palindromo_con_espacios(self):
        self.assertTrue(es_palindromo("A nut for a jar of tuna"))

    def test_palindromo_con_puntuacion(self):
        self.assertTrue(es_palindromo("A man, a plan, a canal: Panama"))

    def test_palindromo_vacio(self):
        self.assertTrue(es_palindromo(""))

    def test_palindromo_un_caracter(self):
        self.assertTrue(es_palindromo("a"))
        
    def test_no_palindromo(self):
        self.assertFalse(es_palindromo("hola mundo"))
        

if __name__ == '__main__':
    unittest.main()