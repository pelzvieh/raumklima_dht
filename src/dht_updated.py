#!/usr/bin/python3
import sys
import time
import datetime
import pathlib

platform_dir = pathlib.PosixPath('/sys/devices/platform/')
if not platform_dir.is_dir():
    print("/sys/devices/platform/ is not a directory", file=sys.stderr)
    sys.exit(1)
dht11_device_path = next(next(platform_dir.glob('dht11*')).glob('iio:device*'))
temperature_path = dht11_device_path / 'in_temp_input'
humidity_path = dht11_device_path / 'in_humidityrelative_input'
if not temperature_path.is_file() or not humidity_path.is_file():
    print(f"No char device files found at {temperature_path} or {humidity_path}", file=sys.stderr)
    sys.exit(2)

attempt = 1
while True:
    try:
        success = False
        with open(temperature_path, "r") as temperature_file:
            temperature_c = float(next(temperature_file)) / 1000.0
        with open(humidity_path, "r") as humidity_file:
            humidity = float(next(humidity_file)) / 1000.0
        timestamp = datetime.datetime.now().timestamp()
        success = True
        with open('/var/lib/dht_updated/dht.json', 'w') as output_file:
            print(
                f"{{\n    \"temperature\": {temperature_c},\n    \"humidity\": {humidity},\n"
                f"    \"timestamp\": \"{timestamp}\"\n}}\n",
                file=output_file
            )
        attempt=1

    except Exception as error:
        if attempt > 10:
            print("{}: {}".format(attempt, error))
        attempt=attempt+1

    time.sleep(60.0 if success else 1.0)
