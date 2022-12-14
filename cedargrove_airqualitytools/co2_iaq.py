# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_co2_iaq`
================================================================================

Calculate the Indoor Quality Index (IAQ) from a CO2 concentration.


* Author(s): JG

Implementation Notes
--------------------

**Hardware:**

* Adafruit Adafruit PMSA003I Air Quality Breakout PID #4632
* Adafruit PM2.5 Air Quality Sensor and Breadboard Adapter Kit PID #3686
* Adafruit PM2.5 Air Quality Sensor with I2C Interface PID #4505

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools.git"

# fmt: off

# AQI color palette
RED    = 0xFF0000
YELLOW = 0xFFFF00
BLUE   = 0x0000FF
ORANGE = 0xFFA500
GREEN  = 0x00FF00

# IAQ breakpoint list
#  CO2 ppm minimum, IAQ color, IAQ description
BREAKPOINTS = [
    (5000, RED,    "DANGER"),
    (2000, ORANGE, "WARNING"),
    (1000, YELLOW, "POOR"),
    ( 100, GREEN,  "GOOD"),
]
# fmt: on


def co2_ppm_to_quality(co2_ppm):
    """Calculate the Indoor Air Quality Index (IAQ) as derived from CO2 ppm
    concentration. Returns a data valid flag, CO2 input concentration value, the
    RGB warning color integer value, and the corresponding US English
    description or warning.

    :param float co2_ppm: The CO2 concentration value in ppm. Range is 0
    to 6000 ppm. No default value.
    """

    if co2_ppm < 0:
        return False, -1, BLUE, "INVALID"

    if co2_ppm > 6000:
        return False, -1, RED, "OVERRANGE"

    # Check sensor reading using EPA breakpoints
    for _, (co2_ppm_min, iaq_color, iaq_desc) in enumerate(BREAKPOINTS):
        if co2_ppm > co2_ppm_min:
            return True, co2_ppm, iaq_color, iaq_desc

    return False, -1, BLUE, "INVALID"
