#!/bin/bash
mydir="$(dirname "$0")"
/usr/bin/pip3 install -U Adafruit-Blinka && "${mydir}"/dht_updated.py

