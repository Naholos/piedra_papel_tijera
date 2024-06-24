import unittest
from piedra_papel_tijera import obtener_jugada_ordenador, determinar_ganador, validar_jugada_usuario

class TestPiedraPapelTijera(unittest.TestCase):

    def test_obtener_jugada_ordenador(self):
        jugada = obtener_jugada_ordenador()
        self.assertIn(jugada, ["piedra", "papel", "tijera"])

    def test_determinar_ganador(self):
        self.assertEqual(determinar_ganador("piedra", "tijera"), "Usuario")
        self.assertEqual(determinar_ganador("papel", "piedra"), "Usuario")
        self.assertEqual(determinar_ganador("tijera", "papel"), "Usuario")
        self.assertEqual(determinar_ganador("piedra", "papel"), "Ordenador")
        self.assertEqual(determinar_ganador("papel", "tijera"), "Ordenador")
        self.assertEqual(determinar_ganador("tijera", "piedra"), "Ordenador")
        self.assertEqual(determinar_ganador("piedra", "piedra"), "Empate")
        self.assertEqual(determinar_ganador("papel", "papel"), "Empate")
        self.assertEqual(determinar_ganador("tijera", "tijera"), "Empate")

    def test_validar_jugada_usuario(self):
        self.assertTrue(validar_jugada_usuario("piedra"))
        self.assertTrue(validar_jugada_usuario("papel"))
        self.assertTrue(validar_jugada_usuario("tijera"))
        self.assertFalse(validar_jugada_usuario("otro"))

if __name__ == "__main__":
    unittest.main()