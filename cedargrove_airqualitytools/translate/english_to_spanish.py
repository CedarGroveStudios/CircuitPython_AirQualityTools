# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

"""Translate English AQI description to Español (Spanish).
Thank you to @jposada202020 for the translation!
"""


ENG_SPANISH = {
    "Air Quality": "Calidad del aire",
    "ALARM": "ALARMA",
    "Alarm": "Alarma",
    "CALIBRATE": "CALIBRACION",
    "DANGER": "PELIGRO",
    "ENGLISH": "ESPAÑOL",
    "GOOD": "BUENO",
    "HAZARDOUS": "PELIGROSO",
    "Indoor Air Quality": "Calidad del aire al interior",
    "INVALID": "INVALIDO",
    "LANGUAGE": "LENGUA",
    "LOW BATTERY": "BATERIA BAJA",
    "MODERATE": "MODERADO",
    "OVERRANGE": "MAXIMO",
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
        if english_phrase in ENG_SPANISH:
            return ENG_SPANISH[english_phrase]
    return english_phrase
