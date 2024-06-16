from grove.grove_co2_scd30 import GroveCo2Scd30
import time

T_offset = 3 # 気温計の補正値
sensor = GroveCo2Scd30()
sensor.set_temperature_offset(T_offset)
print(f"SCD30センサーのオフセットを実行しました。value: {T_offset}")
