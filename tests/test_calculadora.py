import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import conversor as cv  # noqa: E402
import formulas as fm  # noqa: E402
from expressao import ErroExpressao, avaliar, formatar, normalizar  # noqa: E402


class TestExpressao(unittest.TestCase):
    def assertCalcula(self, texto, esperado, graus=True):
        self.assertAlmostEqual(avaliar(texto, graus), esperado, places=9, msg=texto)

    def test_operacoes_basicas(self):
        self.assertCalcula("2 + 3 × 4", 14)
        self.assertCalcula("(2 + 3) × 4", 20)
        self.assertCalcula("10 ÷ 4", 2.5)
        self.assertCalcula("2,5 × 2", 5)
        self.assertCalcula("-3 + 5", 2)
        self.assertCalcula("7 − 10", -3)

    def test_potencia_raiz_fatorial_porcentagem(self):
        self.assertCalcula("2^10", 1024)
        self.assertCalcula("2^-1", 0.5)
        self.assertCalcula("√16", 4)
        self.assertCalcula("√(9+16)", 5)
        self.assertCalcula("5!", 120)
        self.assertCalcula("(2+1)!", 6)
        self.assertCalcula("200 × 15%", 30)
        self.assertCalcula("5 % 2", 0.1)  # % é porcentagem (5% × 2), não resto da divisão

    def test_funcoes_e_constantes(self):
        self.assertCalcula("sen(30)", 0.5)
        self.assertCalcula("cos(60)", 0.5)
        self.assertCalcula("tan(45)", 1)
        self.assertCalcula("asen(1)", 90)
        self.assertCalcula("sen(pi/2)", 1, graus=False)
        self.assertCalcula("log(1000)", 3)
        self.assertCalcula("ln(e)", 1)
        self.assertCalcula("π", math.pi)
        self.assertCalcula("abs(-4)", 4)

    def test_multiplicacao_implicita(self):
        self.assertCalcula("2π", 2 * math.pi)
        self.assertCalcula("2(3+1)", 8)
        self.assertCalcula("(1+1)(2+2)", 8)
        self.assertCalcula("2√9", 6)
        self.assertCalcula("3sen(90)", 3)

    def test_erros(self):
        casos = ["", "2 +", "1/0", "√-4", "log(0)", "(-8)^0.5", "tan(90)", "asen(2)", "171!",
                 "2.5!", "9^99999", "x + 1", "__import__('os')", "(1).real", "[1,2]", "2 ** 1e10"]
        for texto in casos:
            with self.assertRaises(ErroExpressao, msg=texto):
                avaliar(texto)

    def test_normalizar(self):
        self.assertEqual(normalizar("2π × √9"), "2*pi*raiz(9)")

    def test_formatar(self):
        self.assertEqual(formatar(0.1 + 0.2), "0,3")
        self.assertEqual(formatar(2.0), "2")
        self.assertEqual(formatar(-1234.5), "-1234,5")
        self.assertEqual(formatar(1 / 3), "0,3333333333")
        self.assertEqual(formatar(1.5e20), "1,5e+20")
        self.assertEqual(formatar(2.5e-12), "2,5e-12")
        self.assertEqual(formatar(0), "0")


class TestFormulas(unittest.TestCase):
    def test_circulo(self):
        self.assertAlmostEqual(fm.area_circulo(2), 4 * math.pi)
        self.assertAlmostEqual(fm.comprimento_circulo(1), 2 * math.pi)
        with self.assertRaises(fm.ErroFormula):
            fm.area_circulo(0)

    def test_bhaskara(self):
        self.assertEqual(fm.bhaskara(1, -5, 6), (1, [2.0, 3.0]))
        self.assertEqual(fm.bhaskara(1, 2, 1), (0, [-1.0]))
        delta, raizes = fm.bhaskara(1, 0, 1)
        self.assertEqual(delta, -4)
        self.assertEqual(raizes, [complex(0, -1), complex(0, 1)])
        with self.assertRaises(fm.ErroFormula):
            fm.bhaskara(0, 1, 1)

    def test_pitagoras(self):
        self.assertEqual(fm.pitagoras(3, 4, 0), ("Hipotenusa", 5.0))
        self.assertEqual(fm.pitagoras(0, 4, 5), ("Cateto", 3.0))
        for lados in ((3, 0, 0), (3, 4, 5), (6, 0, 5)):
            with self.assertRaises(fm.ErroFormula, msg=lados):
                fm.pitagoras(*lados)

    def test_trigonometria(self):
        r = fm.triangulo_retangulo(30, 10)
        self.assertAlmostEqual(r["seno"], 0.5)
        self.assertAlmostEqual(r["cateto oposto"], 5)
        with self.assertRaises(fm.ErroFormula):
            fm.triangulo_retangulo(90, 10)

    def test_funcao_afim_velocidade_raiz(self):
        self.assertEqual(fm.funcao_afim_y(2, 3, 4), 11)
        self.assertEqual(fm.funcao_afim_x(2, 3, 11), 4)
        self.assertEqual(fm.velocidade_media(150, 2), 75)
        self.assertAlmostEqual(fm.raiz_indice(27, 3), 3)
        self.assertAlmostEqual(fm.raiz_indice(-27, 3), -3)
        for chamada in (lambda: fm.funcao_afim_x(0, 1, 2), lambda: fm.velocidade_media(10, 0),
                        lambda: fm.raiz_indice(-16, 2)):
            with self.assertRaises(fm.ErroFormula):
                chamada()

    def test_todas_as_formulas_calculam(self):
        exemplos = {"r": 2, "a": 1, "b": 4, "c": 6, "base": 2, "exp": 3, "x": 27, "n": 3, "y": 4,
                    "h": 5, "angulo": 30, "hipotenusa": 10, "l": 3, "B": 6, "s": 100, "t": 2}
        for formula in fm.FORMULAS:
            valores = {chave: exemplos[chave] for chave, _ in formula.campos}
            if formula.nome == "Teorema de Pitágoras":
                valores = {"a": 3, "b": 4, "h": 0}
            if formula.nome == "Equação do 2º grau":
                valores = {"a": 1, "b": -5, "c": 6}
            linhas = formula.calcular(valores)
            self.assertTrue(linhas, formula.nome)
            self.assertTrue(all(isinstance(r, str) and isinstance(v, str) for r, v in linhas))

    def test_texto_das_raizes_complexas(self):
        formula = next(f for f in fm.FORMULAS if f.nome == "Equação do 2º grau")
        linhas = dict(formula.calcular({"a": 1, "b": 2, "c": 5}))
        self.assertEqual(linhas["x1 (complexa)"], "-1 − 2i")
        self.assertEqual(linhas["x2 (complexa)"], "-1 + 2i")


class TestConversor(unittest.TestCase):
    def test_conversoes(self):
        casos = [
            (1, "Comprimento", "Metro (m)", "Centímetro (cm)", 100),
            (5, "Comprimento", "Milímetro (mm)", "Centímetro (cm)", 0.5),
            (1, "Área", "Hectare (ha)", "Metro quadrado (m²)", 10000),
            (2, "Volume", "Litro (L)", "Mililitro (mL)", 2000),
            (1, "Volume", "Metro cúbico (m³)", "Litro (L)", 1000),
            (1, "Massa", "Tonelada (t)", "Quilograma (kg)", 1000),
            (500, "Massa", "Miligrama (mg)", "Grama (g)", 0.5),
            (16, "Dados", "Bit (b)", "Byte (B)", 2),
            (1, "Dados", "Gigabyte (GB)", "Megabyte (MB)", 1000),
            (1, "Dados", "Gibibyte (GiB)", "Mebibyte (MiB)", 1024),
            (100, "Temperatura", "Celsius (°C)", "Fahrenheit (°F)", 212),
            (32, "Temperatura", "Fahrenheit (°F)", "Kelvin (K)", 273.15),
            (0, "Temperatura", "Kelvin (K)", "Celsius (°C)", -273.15),
            (-40, "Temperatura", "Celsius (°C)", "Fahrenheit (°F)", -40),
        ]
        for valor, categoria, de, para, esperado in casos:
            self.assertAlmostEqual(cv.converter(valor, categoria, de, para), esperado, places=9,
                                   msg=f"{valor} {de} -> {para}")

    def test_ida_e_volta(self):
        for categoria, unidades in cv.CATEGORIAS.items():
            nomes = list(unidades)
            for de in nomes:
                for para in nomes:
                    ida = cv.converter(123.456, categoria, de, para)
                    self.assertAlmostEqual(cv.converter(ida, categoria, para, de), 123.456, places=6)

    def test_erros(self):
        with self.assertRaises(ValueError):
            cv.converter(-1, "Temperatura", "Kelvin (K)", "Celsius (°C)")
        with self.assertRaises(ValueError):
            cv.converter(-5, "Massa", "Grama (g)", "Quilograma (kg)")
        with self.assertRaises(ValueError):
            cv.converter(1, "Massa", "Grama (g)", "Metro (m)")


if __name__ == "__main__":
    unittest.main()
