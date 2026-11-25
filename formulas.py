"""Fórmulas do menu da calculadora original, como funções puras.

Cada fórmula é descrita em FORMULAS (nome, campos e função de cálculo), e a
interface monta o formulário a partir dessa lista.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from typing import Callable

from expressao import formatar


class ErroFormula(ValueError):
    pass


def _positivo(valor: float, nome: str) -> float:
    if valor <= 0:
        raise ErroFormula(f"{nome} precisa ser maior que zero")
    return valor


# --------------------------------------------------------------------------
# Funções
# --------------------------------------------------------------------------

def area_circulo(raio: float) -> float:
    return math.pi * _positivo(raio, "o raio") ** 2


def comprimento_circulo(raio: float) -> float:
    return 2 * math.pi * _positivo(raio, "o raio")


def bhaskara(a: float, b: float, c: float) -> tuple[float, list[complex | float]]:
    """Raízes de ax² + bx + c = 0. Devolve (delta, raízes); raízes complexas quando delta < 0."""
    if a == 0:
        raise ErroFormula("com a = 0 não é equação do 2º grau")
    delta = b * b - 4 * a * c
    if delta > 0:
        r = math.sqrt(delta)
        return delta, sorted([(-b - r) / (2 * a), (-b + r) / (2 * a)])
    if delta == 0:
        return delta, [-b / (2 * a)]
    r = cmath.sqrt(delta)
    return delta, [(-b - r) / (2 * a), (-b + r) / (2 * a)]


def pitagoras(cateto_a: float = 0, cateto_b: float = 0, hipotenusa: float = 0) -> tuple[str, float]:
    """Recebe dois lados (o terceiro em branco/zero) e devolve (nome, valor) do que falta."""
    informados = sum(v > 0 for v in (cateto_a, cateto_b, hipotenusa))
    if informados != 2:
        raise ErroFormula("preencha exatamente dois dos três lados")
    if hipotenusa == 0:
        return "Hipotenusa", math.hypot(cateto_a, cateto_b)
    cateto = cateto_a or cateto_b
    if cateto >= hipotenusa:
        raise ErroFormula("a hipotenusa precisa ser maior que o cateto")
    return "Cateto", math.sqrt(hipotenusa ** 2 - cateto ** 2)


def triangulo_retangulo(angulo_graus: float, hipotenusa: float) -> dict[str, float]:
    if not 0 < angulo_graus < 90:
        raise ErroFormula("o ângulo precisa estar entre 0° e 90°")
    _positivo(hipotenusa, "a hipotenusa")
    rad = math.radians(angulo_graus)
    return {"seno": math.sin(rad), "cosseno": math.cos(rad), "tangente": math.tan(rad),
            "cateto oposto": hipotenusa * math.sin(rad), "cateto adjacente": hipotenusa * math.cos(rad)}


def funcao_afim_y(a: float, b: float, x: float) -> float:
    return a * x + b


def funcao_afim_x(a: float, b: float, y: float) -> float:
    if a == 0:
        raise ErroFormula("com a = 0 a função é constante: x não pode ser isolado")
    return (y - b) / a


def velocidade_media(distancia_km: float, tempo_h: float) -> float:
    return distancia_km / _positivo(tempo_h, "o tempo")


def potencia(base: float, expoente: float) -> float:
    if base < 0 and expoente != int(expoente):
        raise ErroFormula("potência fracionária de número negativo não é real")
    try:
        return base ** expoente
    except (OverflowError, ZeroDivisionError):
        raise ErroFormula("resultado fora do alcance") from None


def raiz_indice(radicando: float, indice: float) -> float:
    if indice == 0:
        raise ErroFormula("o índice não pode ser zero")
    if radicando < 0:
        if indice == int(indice) and int(indice) % 2 == 1:
            return -((-radicando) ** (1 / indice))
        raise ErroFormula("raiz de índice par de número negativo não é real")
    return radicando ** (1 / indice)


# --------------------------------------------------------------------------
# Descrição para a interface
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Formula:
    grupo: str
    nome: str
    expressao: str  # a fórmula escrita, mostrada na tela
    campos: tuple[tuple[str, str], ...]  # (chave, rótulo)
    calcular: Callable[[dict[str, float]], list[tuple[str, str]]]
    opcionais: tuple[str, ...] = ()  # campos que podem ficar em branco (valem 0)


def _f(n: float) -> str:
    return formatar(n, 6)


def _raizes_texto(v):
    delta, raizes = bhaskara(v["a"], v["b"], v["c"])
    linhas = [("Δ (delta)", _f(delta))]
    if len(raizes) == 1:
        linhas.append(("Raiz dupla x", _f(raizes[0])))
    elif isinstance(raizes[0], complex):
        linhas.append(("Raízes reais", "não existem (Δ < 0)"))
        for i, r in enumerate(raizes, 1):
            sinal = "+" if r.imag >= 0 else "−"
            linhas.append((f"x{i} (complexa)", f"{_f(r.real)} {sinal} {_f(abs(r.imag))}i"))
    else:
        linhas += [(f"x{i}", _f(r)) for i, r in enumerate(raizes, 1)]
    return linhas


def _trig_texto(v):
    r = triangulo_retangulo(v["angulo"], v["hipotenusa"])
    return [(k.capitalize(), _f(val)) for k, val in r.items()]


def _pitagoras_texto(v):
    nome, valor = pitagoras(v.get("a", 0), v.get("b", 0), v.get("h", 0))
    return [(nome, _f(valor))]


FORMULAS = [
    Formula("Círculo", "Área do círculo", "A = π · r²", (("r", "Raio"),),
            lambda v: [("Área", _f(area_circulo(v["r"])))]),
    Formula("Círculo", "Comprimento da circunferência", "C = 2 · π · r", (("r", "Raio"),),
            lambda v: [("Comprimento", _f(comprimento_circulo(v["r"])))]),
    Formula("Álgebra", "Equação do 2º grau", "ax² + bx + c = 0", (("a", "a"), ("b", "b"), ("c", "c")),
            _raizes_texto),
    Formula("Álgebra", "Potência", "bⁿ", (("base", "Base"), ("exp", "Expoente")),
            lambda v: [("Resultado", _f(potencia(v["base"], v["exp"])))]),
    Formula("Álgebra", "Raiz de índice n", "ⁿ√x", (("x", "Radicando"), ("n", "Índice")),
            lambda v: [("Resultado", _f(raiz_indice(v["x"], v["n"])))]),
    Formula("Álgebra", "Função afim: valor de y", "y = a·x + b", (("a", "a"), ("b", "b"), ("x", "x")),
            lambda v: [("y", _f(funcao_afim_y(v["a"], v["b"], v["x"])))]),
    Formula("Álgebra", "Função afim: valor de x", "x = (y − b) / a", (("a", "a"), ("b", "b"), ("y", "y")),
            lambda v: [("x", _f(funcao_afim_x(v["a"], v["b"], v["y"])))]),
    Formula("Geometria", "Teorema de Pitágoras", "h² = a² + b²  (deixe em branco o lado que falta)",
            (("a", "Cateto a"), ("b", "Cateto b"), ("h", "Hipotenusa")), _pitagoras_texto,
            opcionais=("a", "b", "h")),
    Formula("Geometria", "Seno, cosseno e tangente", "triângulo retângulo",
            (("angulo", "Ângulo (graus)"), ("hipotenusa", "Hipotenusa")), _trig_texto),
    Formula("Geometria", "Área do quadrado", "A = l²", (("l", "Lado"),),
            lambda v: [("Área", _f(_positivo(v["l"], "o lado") ** 2))]),
    Formula("Geometria", "Área do retângulo", "A = b · h", (("b", "Base"), ("h", "Altura")),
            lambda v: [("Área", _f(_positivo(v["b"], "a base") * _positivo(v["h"], "a altura")))]),
    Formula("Geometria", "Área do triângulo", "A = b · h / 2", (("b", "Base"), ("h", "Altura")),
            lambda v: [("Área", _f(_positivo(v["b"], "a base") * _positivo(v["h"], "a altura") / 2))]),
    Formula("Geometria", "Área do trapézio", "A = (B + b) · h / 2",
            (("B", "Base maior"), ("b", "Base menor"), ("h", "Altura")),
            lambda v: [("Área", _f((_positivo(v["B"], "a base maior") + _positivo(v["b"], "a base menor"))
                                    * _positivo(v["h"], "a altura") / 2))]),
    Formula("Geometria", "Cubo", "área = 6 · a²  ·  volume = a³", (("a", "Aresta"),),
            lambda v: [("Área total", _f(6 * _positivo(v["a"], "a aresta") ** 2)), ("Volume", _f(v["a"] ** 3))]),
    Formula("Física", "Velocidade média", "Vm = Δs / Δt", (("s", "Distância (km)"), ("t", "Tempo (h)")),
            lambda v: [("Velocidade média", f"{_f(velocidade_media(v['s'], v['t']))} km/h"),
                       ("Em m/s", f"{_f(velocidade_media(v['s'], v['t']) / 3.6)} m/s")]),
]
