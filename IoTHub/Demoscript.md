# Demo with Picoh and Azure IoT Hub

This demo was built on Windows 10 with Conda 4.7.12 running an environment with Python 3.7.4 (which works both for the Picoh and IoT Hub's SDKs) and uses an Azure IoT Hub resource created in an Azure subscription. 

## Setting up the environment

1. Create a Conda environment with Python 3.7.4 and activate it: `conda activate python37`
2. Install the Picoh library using pip: `pip install picoh`
3. Install extension to Az CLI for IoT support: `az extension add --name azure-cli-iot-ext`
4. Install Azure IoT Device SDK: `pip install azure-iot-device` (functionality for communicating with the Azure IoT Hub for both Devices and Modules)
5. Install Azure IoT Hub Service Client SDK: `pip install azure-iothub-service-client` (to: Manage the Azure IoT Hub device identity registry (CRUD operations for devices); Send messages from the Azure IoT Hub to devices (C2D messages); Invoke Azure IoT Device Direct Methods; Update Azure IoT Device Twins)
6. Import library to fix Picoh's speech issue with threads: `pip install pywin32`

## Preparing demo

1. Create a simulated device: `az iot hub device-identity create --hub-name <name of iot hub> --device-id picoh` (from https://docs.microsoft.com/en-gb/azure/iot-hub/quickstart-send-telemetry-python)
2. Get the connection string: `az iot hub device-identity show-connection-string --hub-name visionaijota --device-id picoh --output table`, which in my case returned: `HostName=<name of iot hub>.azure-devices.net;DeviceId=picoh;SharedAccessKey=<your access key>`
3. Update the picohub.py file with the connection string (variable: `CONNECTION_STRING`)
4. To send commands to the hub targetting the device: `az iot device c2d-message send -d picoh -n <name of iot hub> --data "Hey Picoh" --props "hour=now;fruit=mango"`

## Run the demo

1. Run the demo script that subscribes to messages coming from IoTHUb: `python picohub.py` with the Picoh connected to your PC
2. Send messages to the hub in another window with the above mentioned command: `az iot device c2d-message send -d picoh -n <name of iot hub> --data "Hey Picoh" --props "hour=now;fruit=mango"`
3. When the Picohub.py gets a message, it will say its content. (the props in the previous step were just for testing)

## Resources

Picoh GitHub Repo
https://github.com/ohbot/picoh-python

Quickstart: Send telemetry from a device to an IoT hub and read it with a back-end application (Python)
https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python