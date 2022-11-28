# -*- coding: utf-8 -*-
"""
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 
y dura 200 días, ¿qué día te reincorporás al trabajo?
"""

from datetime import date, timedelta

# Fecha de hoy
hoy = date.today()

# Creo un timedelta con valor = 200 días
dias = timedelta(days = 200)

# A la fecha de hoy le sumo el timedelta
reincoporacion = hoy + dias