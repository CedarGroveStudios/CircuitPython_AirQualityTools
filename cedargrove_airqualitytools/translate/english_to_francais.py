# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

"""Translate English AQI description to Français (French).
Thank you to @DavidGlaude for the translation!
"""


ENG_FRANCAIS = {
    "Air Quality": "Qualité de l'air",
    "ALARM": "ALARME",
    "Alarm": "Alarme",
    "CALIBRATE": "ÉTALONNAGE",
    "DANGER": "DANGER",
    "ENGLISH": "FRANÇAIS",
    "GOOD": "BON",
    "HAZARDOUS": "RISQUÉ",
    "Indoor Air Quality": "Qualité de l'air intérieur",
    "INVALID": "INVALIDE",
    "LANGUAGE": "LANGUE",
    "LOW BATTERY": "BATTERIE FAIBLE",
    "MODERATE": "MODÉRÉ",
    "OVERRANGE": "MAXIMUM",
    "POOR": "PAUVRES",
    "SENSITIVE": "SENSIBLE",
    "TEMPERATURE": "TEMPÉRATURE",
    "UNHEALTHY": "MALSAIN",
    "V UNHEALTHY": "TRÈS MALSAIN",
    "WARMUP": "PRÉCHAUFFE",
    "WARNING": "ATTENTION",
}


def interpret(enable=True, english_phrase=""):
    """Translate an English phrase.

    :param bool enable: Enable the translater. Defaults to True.
    :param str english_phrase: English phrase to be interpreted. Defaults to blank.
    """

    if enable:
        if english_phrase in ENG_FRANCAIS:
            return ENG_FRANCAIS[english_phrase]
    return english_phrase
