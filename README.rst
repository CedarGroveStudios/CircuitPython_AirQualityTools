Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A collection of CircuitPython helpers used for the calculation of air quality levels.

CO2_IAQ calculates the Indoor Air Quality Index (IAQ) as derived from a CO2 ppm
concentration measurement. Returns a data valid flag, CO2 input concentration
value, the RGB warning color integer value, and the corresponding US English
description or warning.

PM25_AQI calculates EPA Air Quality Index (AQI) as derived from PM2.5
particulate concentration. Returns a data valid flag, calculated air quality
index, the RGB warning color integer value, and the corresponding US English
description or warning.

.. image:: https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/blob/main/media/WARNING.jpg

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_airqualitytools

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    from cedargrove_airqualitytools.pm25_aqi import concentration_to_aqi
    from cedargrove_airqualitytools.translate.english_to_francais import interpret

    TRANSLATE = True  # Enable language translator

    # Read some sensor values
    PM25_CONCENTRATION = 10  # PM2.5 concentration of 10ppm; GOOD AQI
    CO2_CONCENTRATION = 1450  # CO2 concentration of 1450ppm; HAZARDOUS IAQ

    # Calculate the quality and description
    _, aqi_value, _, aqi_desc = pm25_ppm_to_quality(PM25_CONCENTRATION)
    _, iaq_value, -, iaq_desc = co2_ppm_to_quality(CO2_CONCENTRATION)

    # Print the AQI, description, and translation
    print(f"PM2.5 AQI = {aqi_value} : {aqi_desc}")
    print(interpret(TRANSLATE, aqi_desc))

    # Print the IAQ, description, and translation
    print(f"CO2 IAQ = {iaq_value} : {iaq_desc}")
    print(interpret(TRANSLATE, iaq_desc))



Documentation
=============
API documentation for this library can be found on `Read the Docs <https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/blob/main/media/pseudo_readthedocs_airqualitytools.pdf/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/CircuitPython_AirQualityTools/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
