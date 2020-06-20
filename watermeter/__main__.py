from gpiozero import Button
import yaml
import paho.mqtt.publish

def main(args=None):

    # open config file
    with open('config.yaml', 'r') as configFile:
        config = yaml.load(configFile)
    reading = 0

    # Init button
    sensor = Button(config['meter']['gpioPin'])

    # Open reading file
    dataFile = open(config['dataFile'], 'r')
    reading = float(dataFile.read())
    file.close()

    print "Initial reading: {}".format(reading)

    prevPressed = False

    # Create infinite loop
    while True:

        if sensor.is_pressed:
            if prevPressed == False:
                pressed = True

                # Increase reading
                reading += config['meter']['increase']

                print "Reading: {}".format(reading)

                # Open reading file and store reading
                dataFile = open(config['dataFile'], 'r')
                reading = float(dataFile.read())
                file.close()

                # Push reading to MQTT server
                paho.mqtt.publish.single(
                    config['mqtt']['topic'],
                    reading,
                    hostname=config['mqtt']['host'],
                    port=config['mqtt']['port'],
                    client_id=config['mqtt']['client'],
                    #auth={
                    #    'username': config['mqtt']['auth']['username'],
                    #    'password': config['mqtt']['auth']['password']
                    #},
                )

        else:
            pressed = False

        prevPressed = pressed

if __name__ == "__main__":
    main()