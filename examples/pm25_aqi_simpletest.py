# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: Unlicense

from cedargrove_pm25_aqi.pm25_aqi import concentration_to_aqi
from cedargrove_pm25_aqi.translate.english_to_francais import interpret

pm25_measurement = 10  # PM2.5 concentration of 10ppm; GOOD quality

data_valid, aqi_value, aqi_color, aqi_desc = concentration_to_aqi(pm25_measurement)

print(aqi_value, aqi_desc)  # Print the AQI and description
print(interpret(True, aqi_desc))  # Provide the description in Français (French)
