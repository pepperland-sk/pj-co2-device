import smbus2
import time

# I2Cバスの設定
I2C_BUS = 1
SCD30_ADDRESS = 0x61
SOFT_RESET_COMMAND = [0xD3, 0x04]

# I2Cバスの初期化
bus = smbus2.SMBus(I2C_BUS)

def soft_reset_scd30():
    # ソフトリセットコマンドを送信
    bus.write_i2c_block_data(SCD30_ADDRESS, SOFT_RESET_COMMAND[0], SOFT_RESET_COMMAND[1:])
    print("SCD30センサーをリセットしました。")

# SCD30センサーをリセット
soft_reset_scd30()

# リセット後、センサーが再起動するのを待つ
time.sleep(2)