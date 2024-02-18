"""MQTT Protocol Handler
This module allows you to easily use the MQTT Protocol based on paho-mqtt public module for the memoco-edge applications.

This module allows you to use a MQTTCLient as connector in order to connect to a remote or local broker.

This client also automatically convert python dict payload with class Encoder to ensure correct json encoding.

How To use
--------------
1) Create a new MQTTClient instance with the following parameters:
    - host: the broker remote address (ex: "broker.emqx.io"/"memoco.emea.cumulocity.com"). (default to localhost)
    - port: 1883, 8883, 9009 (default to 9009)
    - client_id (optionnal for local bus): if not set a random client will be assigned.
    - username (optional)
    - password (optional)

2) Subscribing:
    You can subscribe to a specific topics using the subscribe method passing the topic's str as the first argument. Additionnaly you can set one or more callback(s) that will be called with the received message from this topics.
    Note that the callbacks will always received a dict version of the payload as the first arg, the topics as the seconds arg and eventually kwargs if set in the subscribe method.
    Use unsubscribe(topic) to remove subscription.

3) Publication:
    Publishing to the mqtt broker is straightforware by calling :
    publish(topic, data, qos)

The MQTTClient use Pre-defined topics dataclass (see topics file)

"""
from iot_protocols.mqtt.topics import *
from iot_protocols.mqtt.client import MQTTMessageEncoder, to_json_string, from_json_string, UserData, MQTTClient