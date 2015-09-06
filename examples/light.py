#Script to turn a specific light on or off
#example to turn the Study light on the command line would be:
#/usr/bin/python ./light.py Study --on
#
#example to turn the Lounge light off:
#/usr/bin/python ./light.py Study --off

import lifx
import time
import sys
import argparse

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('name', help='name of light')
parser.add_argument('--off', action='store_true', help = 'turn the light off')
parser.add_argument('--on', action='store_true',help = 'turn the light on')

args = parser.parse_args()
print args.name
# Create the client and start discovery
lights = lifx.Client()

# Wait for discovery to complete
time.sleep(1)

# Turn all bulbs on
if args.on:
    for l in lights.get_devices():
        if l.label == args.name:
            print 'Turning on %s' % l.label
            l.power = True

# Turn all bulbs off
if args.off:
    for l in lights.get_devices():
        if l.label == args.name:
            print 'Turning off %s' % l.label
            l.power = False
