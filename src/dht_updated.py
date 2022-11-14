#!/usr/bin/python3
import time
import datetime
from pigpio_dht import DHT22

gpio=4

# Initial the dht device, with data pin connected to:
try:
    dhtDevice = DHT22(gpio, timeout_secs=5)
except RuntimeError as error:
    print("Init failed, aborting to read out: {}".format(error.args[0]))
    sys.exit(1)

attempt = 1
while True:
    try:
        success = False
        result = dhtDevice.read()
        timestamp = datetime.datetime.now().timestamp()
        success = result['valid']
        if success:
            print(
                "{{\n    \"temperature\": {temperature_c},\n    \"humidity\": {humidity},\n    \"timestamp\": \"{timestamp}\"\n}}\n".format(
                  temperature_c=result['temp_c'], humidity=result['humidity'], timestamp=timestamp
                ),
                file=open('/var/lib/dht_updated/dht.json', 'w')
            )

        attempt=1

    except Exception as error:
        if attempt > 10:
            print("{}: {}".format(attempt, error.args[0]))
        attempt=attempt+1

    time.sleep(60.0 if success else 2.0)
