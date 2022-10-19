# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_heat_index`
================================================================================

Calculate the heat (comfort) index from ambient temperature and humidity.


* Author(s): JG

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools.git"


# Heat Index breakpoint list
#   Temperatures in Celsius
#   (heat index temperature minimum, maximum, summary, detail, additional detail)
BREAKPOINTS = (
    (-99, 26, "Safe", ": Heat index is not a factor.", ""),
    (
        26,
        32,
        "Caution",
        ": Fatigue is possible with prolonged exposure and activity. ",
        "Continuing activity could result in heat cramps.",
    ),
    (
        32,
        41,
        "Extreme Caution",
        ": Heat cramps and heat exhaustion are possible. ",
        "Continuing activity could result in heat stroke.",
    ),
    (
        41,
        54,
        "DANGER",
        ": Heat cramps and heat exhaustion are likely. ",
        "Heat stroke is probable with continued activity.",
    ),
    (54, 99, "EXTREME DANGER", ": Heat stroke is imminent. ", ""),
)


def heat_index(deg_c, humidity, verbose=False):
    """Calculate heat index temperature from ambient temperature (Celsius) and
    humidity (percent). Returns the calculated heat index (Celsius) and summary
    description. Detailed description is provided if verbose=True.
    Source: https://en.wikipedia.org/wiki/Heat_index

    :param float deg_c: The ambient temperature in Celsius. No default.
    :param float humidity: The ambient humidity in the range of 0 to 100
    percent. No default.
    """

    t = ((9 / 5) * deg_c) + 32  # Dry-bulb temperature in degrees Fahrenheit
    r = humidity  # Percentage value between 0 and 100

    # Fahrenheit coefficients
    c = (
        0,
        -42.379,
        2.04901523,
        10.14333127,
        -0.22475541,
        -0.00683783,
        -0.05481717,
        0.00122874,
        0.00085282,
        -0.00000199,
    )

    # Formula (Fahrenheit method, +/-1.3F: Rothfusz NWS-SR90-23, 1990)
    # https://www.weather.gov/media/ffc/ta_htindx.PDF
    h_index_f = round(
        c[1]
        + (c[2] * t)
        + (c[3] * r)
        + (c[4] * t * r)
        + (c[5] * t**2)
        + (c[6] * r**2)
        + (c[7] * t**2 * r)
        + (c[8] * t * r**2)
        + (c[9] * t**2 * r**2),
        1,
    )
    # Convert heat index value to degrees Celsius
    h_index_c = round((h_index_f - 32) * (5 / 9), 1)

    # Select message from list
    for minimum, maximum, summary, detail_1, detail_2 in enumerate(BREAKPOINTS):
        if h_index_c < maximum:
            if verbose:
                return h_index_c, summary + detail_1 + detail_2
            return h_index, summary

    return h_index_c, "Invalid heat index value."
