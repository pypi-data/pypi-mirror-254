# Wirepas DLMS tool

This repository contains tools to validate the integration of Wirepas dlms app.


## Wirepas DLMS Tool library

The purpose of the [Wirepas DLMS Integration Tool Python library](./wirepas_dlms_tool/) is to provide tools to validate the DLMS app and the meter compatibility. It is not designed to be used as a HES.<br>
It works as an interface to both the Gurux Python library (to read DLMS/COSEM compatible meters) and the Wirepas MQTT library, and including the specifications of the DLMS app environment.


## Installation

### Install from PyPi

This package is available from [PyPi](https://pypi.org/project/wirepas-dlms-tool/).

```
pip install wirepas-dlms-tool
```

### Install from the source

This wheel can be install from source directly if you need modifications.

pip install -e .


## Main principles

The library contains modules to abstract the meters and their NIC in a Wirepas network in order to listen to their traffic and to exchange messages with them from a HES perspective.

In fact, the DLMSNetworkInterface class provides a network interface to communicate with the NIC through the NIC server or directly with the meters in pass-through inside a Wirepas network.
Especially, it redirects the messages from gateways to the corresponding meter objects representing the meters themselves with their NIC.
Futhermore, it also updates locally their network informations (gateway and sink ids) when receiving a message so that meters are always up-to-date.

When a DLMS message is received from an unknown node, the associated meter object is created automatically before redirecting its message.
Put together, it means that it is possible to wait for meters first messages to generate their related meter object.
However, in the case of a proactive communication (requesting the meter), it is still possible to reference the meters manually, as having to wait for a first message for their network information can take unecessary time if we already know their node id, gateway id, sink id.

When requesting a meter, the associated meter object request methods must be used. A response object containing the response error code, the meter response payload, the value that was queried and the xml representation of the response message is returned when the physical meter answers.


When a message is received from the physical meter, the message is either:
* An unencrypted NIC status word message asserting a sink route change or a provisioning request.
* An encrypted data notification.
* A response to a request.
* Something that couldn't be parsed for various reasons (wrong credentials, malformed DLMS packets, ...).

And, in both cases, the message is returned in a different function called by the associated meter object, in order to separate the use cases of the user.


## Examples

Example of an on-demand request to a meter:
```
# Use for connection to the MQTT.
wni = WirepasNetworkInterface(<mqtt informations>)

# Our network interface to communication with meters.
dni = DLMSNetworkInterface(wni)

# Creation of a meter object.
my_meter = dni.create_meter(node_id=12345678, meter_configuration=my_meter_configuration,
                            gateway="my_gw", sink="my_sink")

# Get meter response of a get device ID request in pass-through in US association.
response = my_meter.get_meter_device_ID(AssociationLevelEnum.US_ASSOCIATION)

# Verification of the correctness of the response with the error code.
assert response.error_code == ErrorCodeEnum.RES_OK

# We can print the response message as a xml string and also its device ID we requested.
print(response.xml)
print(f"The device ID of the meter is {response.value}")
```

Example of listening to unknown meters for its notifications:
```
# Function to be used when receiving a notification from meters.
def default_notification_cb(meter, notification):
    print(f"A notification has been received from {meter.node_id}:")
    print(notification.xml)

# Function to be used when a message could not be parsed.
def unparsed_cb(meter, payload: bytes):
    print(f"An unknown DLMS message has been received from {meter.node_id} "
          "in {meter.gateway_id}/{meter.sink_id}.")

# Use for connection to the MQTT.
wni = WirepasNetworkInterface(<mqtt informations>)

# Our network interface to communication with meters.
dni = DLMSNetworkInterface(wni, default_notification_cb=default_notification_cb,
                           default_unparsed_cb=unparsed_cb)

# Creation of a meter objects that handles the real meter messages.
dni.create_meter(node_id=12345678, meter_configuration=my_meter_configuration,
                 gateway="my_gw", sink="my_sink")
```


License
-------

Licensed under the Apache License, Version 2.0.
