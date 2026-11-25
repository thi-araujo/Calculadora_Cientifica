"""Conversor de unidades: as seis categorias da calculadora original.

Cada unidade tem um fator para a unidade base da categoria. Temperatura é a
exceção, com fórmulas próprias.
"""

from __future__ import annotations

CATEGORIAS: dict[str, dict[str, float]] = {
    "Comprimento": {
        "Quilômetro (km)": 1000, "Metro (m)": 1, "Centímetro (cm)": 0.01, "Milímetro (mm)": 0.001,
        "Milha (mi)": 1609.344, "Pé (ft)": 0.3048, "Polegada (in)": 0.0254,
    },
    "Área": {
        "Quilômetro quadrado (km²)": 1e6, "Hectare (ha)": 1e4, "Metro quadrado (m²)": 1,
        "Centímetro quadrado (cm²)": 1e-4, "Milímetro quadrado (mm²)": 1e-6, "Alqueire paulista": 24200,
    },
    "Volume": {
        "Metro cúbico (m³)": 1000, "Litro (L)": 1, "Mililitro (mL)": 0.001, "Centímetro cúbico (cm³)": 0.001,
        "Galão americano (gal)": 3.785411784,
    },
    "Massa": {
        "Tonelada (t)": 1e6, "Quilograma (kg)": 1000, "Grama (g)": 1, "Miligrama (mg)": 0.001,
        "Libra (lb)": 453.59237, "Onça (oz)": 28.349523125,
    },
    "Dados": {
        "Bit (b)": 1 / 8, "Byte (B)": 1,
        "Kilobyte (kB)": 1e3, "Megabyte (MB)": 1e6, "Gigabyte (GB)": 1e9, "Terabyte (TB)": 1e12,
        "Kibibyte (KiB)": 2 ** 10, "Mebibyte (MiB)": 2 ** 20, "Gibibyte (GiB)": 2 ** 30, "Tebibyte (TiB)": 2 ** 40,
    },
    "Temperatura": {"Celsius (°C)": 0, "Fahrenheit (°F)": 0, "Kelvin (K)": 0},
}

ZERO_ABSOLUTO_C = -273.15


def _para_celsius(valor: float, unidade: str) -> float:
    if unidade.startswith("Celsius"):
        return valor
    if unidade.startswith("Fahrenheit"):
        return (valor - 32) * 5 / 9
    return valor + ZERO_ABSOLUTO_C


def _de_celsius(valor: float, unidade: str) -> float:
    if unidade.startswith("Celsius"):
        return valor
    if unidade.startswith("Fahrenheit"):
        return valor * 9 / 5 + 32
    return valor - ZERO_ABSOLUTO_C


def converter(valor: float, categoria: str, de: str, para: str) -> float:
    unidades = CATEGORIAS.get(categoria)
    if unidades is None or de not in unidades or para not in unidades:
        raise ValueError("unidade desconhecida")
    if categoria == "Temperatura":
        celsius = _para_celsius(valor, de)
        if celsius < ZERO_ABSOLUTO_C - 1e-9:
            raise ValueError("abaixo do zero absoluto (−273,15 °C)")
        return _de_celsius(celsius, para)
    if valor < 0:
        raise ValueError("valor negativo não faz sentido nesta categoria")
    return valor * unidades[de] / unidades[para]
