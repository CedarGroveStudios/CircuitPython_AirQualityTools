# SPDX-FileCopyrightText: Copyright (c) 2023 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

"""Translate English AQI description to Español (Spanish).
Thank you to @jposada202020 for the translation!
"""


ENG_ESPANOL = {
    "Air Quality": "Calidad del aire",
    "ALARM": "ALARMA",
    "Alarm": "Alarma",
    "CALIBRATE": "CALIBRACIÓN",
    "DANGER": "PELIGRO",
    "ENGLISH": "ESPAÑOL",
    "GOOD": "BUENO",
    "HAZARDOUS": "PELIGROSO",
    "Indoor Air Quality": "Calidad del aire al interior",
    "INVALID": "INVÁLIDO",
    "LANGUAGE": "LENGUA",
    "LOW BATTERY": "BATERÍA BAJA",
    "MODERATE": "MODERADO",
    "OVERRANGE": "MÁXIMO",
    "POOR": "POBRE",
    "SENSITIVE": "SENSIBLE",
    "TEMPERATURE": "TEMPERATURA",
    "UNHEALTHY": "POCO SALUDABLE",
    "V UNHEALTHY": "INSALUBRE",
    "WARMUP": "PRECALENTAMIENTO",
    "WARNING": "ADVERTENCIA",
}


def interpret(enable=True, english_phrase=""):
    """Translate an English phrase.

    :param bool enable: Enable the translator. Defaults to True.
    :param str english_phrase: English phrase to be interpreted. Defaults to blank.
    """

    if enable:
        if english_phrase in ENG_ESPANOL:
            return ENG_ESPANOL[english_phrase]
    return english_phrase