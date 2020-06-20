import os
from gpiozero import Button
import paho.mqtt.publish

def main(args=None):

    # Settings
    readingFile = 'reading.txt'
    reading = 0

    # Init button
    sensor = Button(17)

    # Open reading file
    file = open(readingFile, 'r')
    reading = float(file.read())
    file.close()

    print "Initial reading: {}".format(reading)

    prevPressed = False

    # Create infinite loop
    while True:

        if sensor.is_pressed:
            if prevPressed == False:
                pressed = True

                reading += 0.001 

                print "Reading: {}".format(reading)

                file = open(readingFile, 'w')
                file.write(str(reading))
                file.close()

		paho.mqtt.publish.single(
                	"watermeter/reading",
			reading,
                	hostname="hass01"
		)


        else:
            pressed = False

        prevPressed = pressed
    

if __name__ == "__main__":
    main()
