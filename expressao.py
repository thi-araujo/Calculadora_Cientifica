"""Avaliador seguro de expressões matemáticas.

Não usa eval(): a expressão é convertida em árvore sintática (ast) e só
números, operadores aritméticos, constantes e funções da lista permitida são
aceitos. Qualquer outra coisa (nomes de variáveis, atributos, importações)
gera ErroExpressao.

Aceita a notação brasileira e a da calculadora:
    2,5 × 4    10 ÷ 4    2^10    √16    5!    50%    2π    sen(30)
"""

from __future__ import annotations

import ast
import math
import operator
import re

MAX_EXPOENTE = 10_000
MAX_FATORIAL = 170  # 171! já não cabe num float


class ErroExpressao(ValueError):
    pass


def _fatorial(n: float) -> float:
    if n != int(n) or n < 0:
        raise ErroExpressao("fatorial só existe para inteiros não negativos")
    if n > MAX_FATORIAL:
        raise ErroExpressao(f"fatorial grande demais (máximo {MAX_FATORIAL}!)")
    return float(math.factorial(int(n)))


def _raiz(x: float) -> float:
    if x < 0:
        raise ErroExpressao("raiz quadrada de número negativo não é real")
    return math.sqrt(x)


def _log(x: float) -> float:
    if x <= 0:
        raise ErroExpressao("logaritmo só existe para números positivos")
    return math.log10(x)


def _ln(x: float) -> float:
    if x <= 0:
        raise ErroExpressao("logaritmo só existe para números positivos")
    return math.log(x)


def _funcoes(graus: bool) -> dict:
    entrada = math.radians if graus else (lambda x: x)
    saida = math.degrees if graus else (lambda x: x)

    def tangente(x):
        if graus and (x - 90) % 180 == 0:
            raise ErroExpressao("tangente de 90° (e múltiplos ímpares) não existe")
        return math.tan(entrada(x))

    def inversa(funcao, nome):
        def calcular(x):
            if funcao is not math.atan and not -1 <= x <= 1:
                raise ErroExpressao(f"{nome} só aceita valores entre -1 e 1")
            return saida(funcao(x))
        return calcular

    return {
        "sen": lambda x: math.sin(entrada(x)), "sin": lambda x: math.sin(entrada(x)),
        "cos": lambda x: math.cos(entrada(x)),
        "tan": tangente, "tg": tangente,
        "asen": inversa(math.asin, "arco seno"), "asin": inversa(math.asin, "arco seno"),
        "acos": inversa(math.acos, "arco cosseno"),
        "atan": inversa(math.atan, "arco tangente"),
        "raiz": _raiz, "sqrt": _raiz,
        "log": _log, "ln": _ln,
        "abs": abs, "fat": _fatorial,
    }


CONSTANTES = {"pi": math.pi, "e": math.e}

_OPERADORES = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
               ast.Div: operator.truediv, ast.Mod: operator.mod, ast.Pow: operator.pow}


def normalizar(texto: str) -> str:
    """Converte a notação da calculadora para a sintaxe do Python."""
    t = texto.strip().lower()
    t = t.replace("×", "*").replace("÷", "/").replace("−", "-").replace("^", "**").replace("π", "pi")
    t = t.replace("√", "raiz").replace(",", ".")
    t = re.sub(r"\s+", "", t)
    # raiz9 -> raiz(9)  (√ seguido de número, sem parênteses)
    t = re.sub(r"raiz(-?\d+(?:\.\d+)?)", r"raiz(\1)", t)
    # 5! -> fat(5)   (5)! -> fat((5))
    t = re.sub(r"(\d+(?:\.\d+)?)!", r"fat(\1)", t)
    t = re.sub(r"(\([^()]*\))!", r"fat(\1)", t)
    # 50% -> (50/100)
    t = re.sub(r"(\d+(?:\.\d+)?)%", r"(\1/100)", t)
    # multiplicação implícita: 2pi, 2(3), )(, )2, pi(…)
    t = re.sub(r"(\d|\))(?=[a-z(])", r"\1*", t)
    t = re.sub(r"\)(?=\d)", r")*", t)
    t = re.sub(r"\b(pi|e)(?=\()", r"\1*", t)
    return t


def avaliar(texto: str, graus: bool = True) -> float:
    """Calcula a expressão e devolve um float. Levanta ErroExpressao em qualquer problema."""
    if not texto.strip():
        raise ErroExpressao("expressão vazia")
    codigo = normalizar(texto)
    try:
        arvore = ast.parse(codigo, mode="eval")
    except SyntaxError:
        raise ErroExpressao("expressão incompleta ou mal escrita") from None
    funcoes = _funcoes(graus)

    def calcular(no: ast.AST) -> float:
        if isinstance(no, ast.Expression):
            return calcular(no.body)
        if isinstance(no, ast.Constant) and isinstance(no.value, (int, float)) and not isinstance(no.value, bool):
            return float(no.value)
        if isinstance(no, ast.Name) and no.id in CONSTANTES:
            return CONSTANTES[no.id]
        if isinstance(no, ast.UnaryOp) and isinstance(no.op, (ast.USub, ast.UAdd)):
            valor = calcular(no.operand)
            return -valor if isinstance(no.op, ast.USub) else valor
        if isinstance(no, ast.BinOp) and type(no.op) in _OPERADORES:
            esquerda, direita = calcular(no.left), calcular(no.right)
            if isinstance(no.op, ast.Pow):
                if abs(direita) > MAX_EXPOENTE:
                    raise ErroExpressao("expoente grande demais")
                if esquerda < 0 and direita != int(direita):
                    raise ErroExpressao("potência fracionária de número negativo não é real")
            if isinstance(no.op, (ast.Div, ast.Mod)) and direita == 0:
                raise ErroExpressao("divisão por zero")
            try:
                return float(_OPERADORES[type(no.op)](esquerda, direita))
            except OverflowError:
                raise ErroExpressao("resultado grande demais") from None
        if (isinstance(no, ast.Call) and isinstance(no.func, ast.Name) and no.func.id in funcoes
                and len(no.args) == 1 and not no.keywords):
            try:
                return float(funcoes[no.func.id](calcular(no.args[0])))
            except (ValueError, OverflowError) as erro:
                if isinstance(erro, ErroExpressao):
                    raise
                raise ErroExpressao("valor fora do domínio da função") from None
        if isinstance(no, ast.Name):
            raise ErroExpressao(f"\"{no.id}\" não é uma função ou constante conhecida")
        raise ErroExpressao("operação não permitida")

    resultado = calcular(arvore)
    if math.isinf(resultado) or math.isnan(resultado):
        raise ErroExpressao("resultado grande demais")
    return resultado


def formatar(numero: float, casas: int = 10) -> str:
    """Formata no padrão brasileiro: vírgula decimal, sem zeros sobrando.

    Números muito grandes ou muito pequenos usam notação científica (1,5e+20).
    Valores como 0.1 + 0.2 aparecem como 0,3.
    """
    if numero == 0:
        return "0"
    if abs(numero) >= 1e15 or abs(numero) < 1e-9:
        texto = f"{numero:.{casas}e}"
        mantissa, expoente = texto.split("e")
        mantissa = mantissa.rstrip("0").rstrip(".")
        return f"{mantissa}e{int(expoente):+d}".replace(".", ",")
    arredondado = round(numero, casas)
    if arredondado == int(arredondado):
        return f"{int(arredondado)}"
    texto = f"{arredondado:.{casas}f}".rstrip("0").rstrip(".")
    return texto.replace(".", ",")
