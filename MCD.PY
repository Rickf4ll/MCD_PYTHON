import unittest
def mcd(nro1, nro2):
    a = nro1
    b = nro2
    while b != 0:
        a, b = b, a % b
    return a

def mcd(nro1, nro2):
    def hallar_divisores(n):
        divisores = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisores.append(i)
        return divisores

    divisores_nro1 = hallar_divisores(nro1)
    divisores_nro2 = hallar_divisores(nro2)

    divisores_comunes = []
    for divisor in divisores_nro1:
        if divisor in divisores_nro2:
            divisores_comunes.append(divisor)

    if divisores_comunes:
        return divisores_comunes[-1]
    else:
        return 1  # Si no hay divisores comunes, el MCD es 1 por definición

# Ejemplo de uso
class TestOperaciones(unittest.TestCase):
    def test_mcd(self):
        esperado = 12
        actual= mcd(24,36)
        self.assertEqual(actual,esperado)
if __name__ == '__main__':
    unittest.main()