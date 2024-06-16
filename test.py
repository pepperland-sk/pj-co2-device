from grove.grove_co2_scd30 import GroveCo2Scd30
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
# import asyncio
import os
import time

CONNECTION_STRING = os.environ['IOTHUB_CONNSTR']

sensor = GroveCo2Scd30()

def send_telemetry():
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    
    while True:
        if sensor.get_data_ready_status():
            co2, temperature, humidity = sensor.read()
            msg = Message(f"co2:{co2},temperature:{temperature},humidity:{humidity}")
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"

            print(f"Sending message: {msg}")
            device_client.send_message(msg)
            print("Message sent")

            time.sleep(5)

if __name__ == "__main__":
    send_telemetry()

# while True:
#         if sensor.get_data_ready_status():
#             co2, temperature, humidity = sensor.read()
#             print(f"CO2 concentration is {co2:.1f} ppm")
#             print(f"Temperature in Celsius is {temperature:.2f} C")
#             print(f"Relative Humidity is {humidity:.2f} %")
#             break