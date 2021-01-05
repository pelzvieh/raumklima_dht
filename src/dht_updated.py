#!/usr/bin/python3
import time
import board
import adafruit_dht
import datetime

# Initial the dht device, with data pin connected to:
try:
    dhtDevice = adafruit_dht.DHT22(board.D4)
except RuntimeError as error:
    print("Init failed, aborting to read out: {}".format(error.args[0]))
    sys.exit(1)

attempt = 1
while True:
    try:
        success = False
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        print(
            "{{\n    \"temperature\": {temperature_c:.1f},\n    \"humidity\": {humidity},\n    \"timestamp\": \"{timestamp}\"\n}}\n".format(
              temperature_c=temperature_c, humidity=humidity, timestamp=timestamp
            ),
            file=open('/var/lib/dht_updated/dht.json', 'w')
        )

        success=True
        attempt=1

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        if attempt > 10:
            print("{}: {}".format(attempt, error.args[0]))
        attempt=attempt+1

    time.sleep(60.0 if success else 2.0)

