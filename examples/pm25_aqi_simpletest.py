# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

from cedargrove_airqualitytools.pm25_aqi import pm25_ppm_to_quality
from cedargrove_airqualitytools.co2_iaq import co2_ppm_to_quality
from cedargrove_airqualitytools.translate.english_to_francais import interpret

TRANSLATE = True  # Enable language translator

# Read some sensor values
PM25_CONCENTRATION = 10  # PM2.5 concentration of 10ppm; GOOD AQI
CO2_CONCENTRATION = 1450  # CO2 concentration of 1450ppm; POOR IAQ

# Calculate the quality and description
_, aqi_value, _, aqi_desc = pm25_ppm_to_quality(PM25_CONCENTRATION)
_, iaq_value, _, iaq_desc = co2_ppm_to_quality(CO2_CONCENTRATION)

# Print the AQI, description, and translation
print(f"PM2.5 AQI = {aqi_value} : {aqi_desc}")
print(interpret(TRANSLATE, aqi_desc))

# Print the IAQ, description, and translation
print(f"CO2 IAQ = {iaq_value} : {iaq_desc}")
print(interpret(TRANSLATE, iaq_desc))
