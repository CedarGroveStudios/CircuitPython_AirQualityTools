# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_pm25_aqi`
================================================================================

Calculate the EPA Air Quality Index (AQI) from a PM2.5 particulate concentration.


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
RED    = 0xFF0000  # Unhealthy
YELLOW = 0xFFFF00  # Moderate
BLUE   = 0x0000FF  # Invalid
ORANGE = 0xFFA500  # Sensitive
GREEN  = 0x00FF00  # Good
PURPLE = 0x800080  # Very Unhealthy
MAROON = 0x800000  # Hazardous, Overrange

# AQI breakpoint list
#  PM2.5 min, PM2.5 max, AQI min, AQI max, AQI color, AQI description
BREAKPOINTS = [
    (350,  500, 400, 500, MAROON, 'HAZARDOUS'),
    (250,  350, 300, 400, MAROON, 'HAZARDOUS'),
    (150,  250, 200, 300, PURPLE, 'V UNHEALTHY'),
    ( 55,  150, 150, 200, RED,    'UNHEALTHY'),
    ( 35,   55, 100, 150, ORANGE, 'SENSITIVE'),
    ( 12,   35,  50, 100, YELLOW, 'MODERATE'),
    (  0,   12,   0,  50, GREEN,  'GOOD'),
]
# fmt: on


def map_range(x, in_min, in_max, out_min, out_max):
    """Maps and constrains an input value from one range of values to another.
    (from adafruit_simpleio)

    :param float x: The input value to map to the input range.
    :param float in_min: The minimum value of the input range.
    :param float in_max: The maximum value of the input range.
    :param float out_min: The minimum value of the output range.
    :param float out_max: The maximum value of the output range.

    :return: The output value mapped to the output range
    :rtype: float
    """

    in_range = in_max - in_min
    in_delta = x - in_min
    if in_range != 0:
        mapped = in_delta / in_range
    elif in_delta != 0:
        mapped = in_delta
    else:
        mapped = 0.5
    mapped *= out_max - out_min
    mapped += out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)


def pm25_ppm_to_quality(pm25_ppm):
    """Calculate EPA Air Quality Index (AQI) as derived from PM2.5 particulate
    concentration. Returns a data valid flag, calculated air quality index
    (AQI), the RGB warning color integer value, and the corresponding US English
    description or warning.

    NOTE: The calculated AQI returned by this function should ideally be
    measured using the 24-hour PM2.5 concentration average. Calculating a AQI
    without averaging will result in higher AQI values than expected.

    :param float pm25_ppm: Particulate matter 2.5 sensor value. Range 0
    to 500ppm. No default.
    """

    if pm25_ppm < 0:
        return False, -1, BLUE, "INVALID"

    if pm25_ppm > 500:
        return False, -1, MAROON, "OVERRANGE"

    # Check sensor reading using EPA breakpoints
    for _, (pm25_min, pm25_max, aqi_min, aqi_max, aqi_color, aqi_desc) in enumerate(
        BREAKPOINTS
    ):
        if pm25_ppm > pm25_min:
            aqi_value = int(map_range(pm25_ppm, pm25_min, pm25_max, aqi_min, aqi_max))

            return True, aqi_value, aqi_color, aqi_desc

    return False, -1, BLUE, "INVALID"
