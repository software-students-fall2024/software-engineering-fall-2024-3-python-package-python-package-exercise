# -*- coding: utf-8 -*-

# SPANISH

neutral = [
    "Funciona en mi máquina, pero quizás el entorno del servidor sea diferente.",
"¿Has probado a añadir más comentarios a tu código?",
"¿Has probado a encender y apagar tu ordenador de nuevo?",
]

javascript = [
"¿Has probado a añadir más puntos y comas? A JavaScript le encantan.",
"El CSS está luchando con JavaScript de nuevo.",
"Probablemente se deba a que el código se está ejecutando en modo descuidado en lugar de en modo estricto.",
]

python = [
    "Debe ser un problema de Python 2 vs. Python 3.",
"El entorno virtual debe estar funcionando mal.",
"Funcionó cuando lo ejecuté sin pytest.",
]

matlab = [ 
    "Es un error de redondeo; a MATLAB le encanta su precisión de punto flotante.",
"Podría ser una discrepancia en la dimensión de la matriz. MATLAB es muy exigente con eso.",
"Creo que el servidor de licencias de MATLAB debe estar inactivo nuevamente.",
]

jokes_en = {
    "neutral": neutral,
    "python": python,
    "javascript": javascript,
    "matlab": matlab,
    "all": neutral + javascript + python + matlab,
}