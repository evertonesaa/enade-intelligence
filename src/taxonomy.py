"""
ENADE Intelligence
Taxonomy Module

Defines macro areas and subareas used to classify
Engineering questions from ENADE exams.
"""

from typing import Dict, List


MACRO_AREAS: Dict[str, List[str]] = {
    "Fenomenos de Transporte": [
        "Mecanica dos Fluidos",
        "Transferencia de Calor",
        "Transferencia de Massa"
    ],

    "Operacoes Unitarias": [
        "Destilacao",
        "Absorcao",
        "Extracao",
        "Filtracao",
        "Secagem",
        "Evaporacao",
        "Peneiramento"
    ],

    "Termodinamica": [
        "Equilibrio de Fases",
        "Propriedades Termodinamicas",
        "Energia Livre"
    ],

    "Reatores": [
        "Cinetica Quimica",
        "Reatores CSTR",
        "Reatores PFR"
    ],

    "Balancos de Massa e Energia": [
        "Balanco de Massa",
        "Balanco de Energia"
    ],

    "Controle de Processos": [
        "Instrumentacao",
        "Controle PID",
        "Malhas de Controle"
    ],

    "Engenharia Ambiental": [
        "Tratamento de Efluentes",
        "Controle de Emissoes"
    ],

    "Formacao Geral": [
        "Etica",
        "Sociedade",
        "Impactos Tecnologicos"
    ]
}