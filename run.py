from grove.grove_co2_scd30 import GroveCo2Scd30
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import asyncio
import os
import time
from datetime import datetime
import json

CONNECTION_STRING = os.environ.get('IOTHUB_CONNSTR')

sensor = GroveCo2Scd30()

async def send_telemetry():
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    await device_client.connect()
    print("Connection Success")
    
    while True:
        if sensor.get_data_ready_status():
            co2, temperature, humidity = sensor.read()
            msg = Message(json.dumps(f'{{"co2":{co2}, "temperature":{temperature},"humidity":{humidity}}}'))
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json;charset=utf-8"
            await device_client.send_message(msg)

            time.sleep(5)

if __name__ == "__main__":
    asyncio.run(send_telemetry())