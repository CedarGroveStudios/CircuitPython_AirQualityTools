# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

"""Translate English AQI description to Deutsch (German).
Thank you to @effiksmusic for the translation!
"""


ENG_DEUTSCH = {
    "Air Quality": "Luftqualität",
    "ALARM": "ALARM",
    "Alarm": "Alarm",
    "CALIBRATE": "KALIBRIEREN",
    "DANGER": "GEFAHR",
    "ENGLISH": "DEUTSCH",
    "GOOD": "GUT",
    "HAZARDOUS": "GEFÄHRLICH",
    "Indoor Air Quality": "Raumluftqualität",
    "INVALID": "UNGÜLTIG",
    "LANGUAGE": "SPRACHE",
    "LOW BATTERY": "BATTERIE LEER",
    "MODERATE": "MÄSSIG",
    "OVERRANGE": "ÜBER MAXIMUM",
    "POOR": "SCHLECHT",
    "SENSITIVE": "SENSIBEL",
    "TEMPERATURE": "TEMPERATUR",
    "UNHEALTHY": "UNGESUND",
    "V UNHEALTHY": "SEHR UNGESUND",
    "WARMUP": "VORBEREITUNG",
    "WARNING": "WARNUNG",
}


def interpret(enable=True, english_phrase=""):
    """Translate an English phrase.

    :param bool enable: Enable the translater. Defaults to True.
    :param str english_phrase: English phrase to be interpreted. Defaults to blank.
    """

    if enable:
        if english_phrase in ENG_DEUTSCH:
            return ENG_DEUTSCH[english_phrase]
    return english_phrase
