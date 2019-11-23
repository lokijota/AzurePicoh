from picoh import picoh
import threading
from azure.iot.device import IoTHubDeviceClient
import time
from random import randint, random
import pythoncom 

RECEIVED_MESSAGES = 0
CONNECTION_STRING = "HostName=visionaijota.azure-devices.net;DeviceId=picoh;SharedAccessKey=<your access key>"

# Create an IoT Hub client
def iothub_client_init():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

# print received messages to the console
def message_listener(client):
    global RECEIVED_MESSAGES
    pythoncom.CoInitialize() #fix to Picoh speech issue

    while True:
        message = client.receive_message()
        RECEIVED_MESSAGES += 1
        print("Message received")
        # print( "    Data: «{}»".format(message.data) )
        # print( "    Properties: {}".format(message.custom_properties))
        # print( "    Total calls received: {}".format(RECEIVED_MESSAGES))
        print(message.data.decode('utf-8'))

        picoh.say(message.data.decode('utf-8'))
        picoh.setEyeShape("Heart")
        picoh.move(picoh.HEADTURN, randint(3, 7))
        picoh.move(picoh.HEADNOD, randint(4, 7))
        picoh.baseColour(random() * 10, random() * 10, random() * 10)
        picoh.wait(1)
        picoh.setEyeShape("Eyeball")
        

# initialize the client and wait to receive cloud-to-device message
def iothub_client_sample_run():
    try:
        client = iothub_client_init()

        message_listener_thread = threading.Thread(target=message_listener, args=(client,))
        message_listener_thread.daemon = True
        message_listener_thread.start()

        while True:
            time.sleep(1000)

    except KeyboardInterrupt:
        print ( "IoTHubDeviceClient sample stopped" )

# main function
if __name__ == '__main__':
    print ( "Starting the IoT Hub Python sample..." )
    print ( "IoTHubDeviceClient waiting for commands, press Ctrl-C to exit" )
    print ("Reseting the PICOH")
    picoh.reset()
    picoh.say("The Picoh is alive")
    picoh.setEyeBrightness(5)

    iothub_client_sample_run()