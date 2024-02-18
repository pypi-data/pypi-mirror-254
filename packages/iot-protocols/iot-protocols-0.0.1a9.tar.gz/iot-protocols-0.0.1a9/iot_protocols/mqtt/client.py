from __future__ import annotations
from dataclasses import dataclass, field

import logging
import json
import datetime
import time
from typing import Any, List
import dataclasses

import paho.mqtt.client as mqtt


FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


class DatetimeEncoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()

    @staticmethod
    def load_from_datetime(pairs):
        d = {}
        for k, v in pairs.items():
            try:
                d[k] = datetime.datetime.fromisoformat(v)
            except (ValueError, TypeError):
                d[k] = v
        return d
    

class MQTTMessageEncoder(json.JSONEncoder):
        
        def default(self, o):
            if isinstance(o, (datetime.datetime, datetime.date)):
                return o.isoformat()
            
            if dataclasses.is_dataclass(o):
                return o.__dict__
            
            return super().default(o)
        

def to_json_string(value: dict) -> str:
    """to_json_string converts a dict to a dumps json string.

    datetime object or spectial object are converted into string.
    Args:
        value (dict): dict containing values.
    """
    try:
        value_as_json = json.dumps(value, cls=MQTTMessageEncoder)
        return value_as_json
    except Exception as err:
        logging.error(f"Fail to convert to json string : {err}")

def from_json_string(string_value: str | bytes | dict) -> dict:
    """from_json_string converts a json encoded string to a dict value.

    Args:
        string_value (str): the json str encoded value.

    Returns:
        dict: result as a dict object.
    """
    # Return empty dict if null-bytes message
    try:
        if len(string_value) == 0:
            return {}

        if isinstance(string_value, bytes):
            string_value = json.loads(
                string_value.decode('utf-8'),
            )

        if isinstance(string_value, dict):
            return string_value
        
        return json.loads(
            string_value,
            object_hook=DatetimeEncoder.load_from_datetime,
        )

    except json.decoder.JSONDecodeError as err:
        logging.error(f"Fail to decode value from content : {err}")


@dataclass
class UserData:
    """ A class containing information about the MQTT user"""
    id: int # The id of actors using the mqtt bus
    name: str # Name (also identify) of the user.
    type: str # Type of the actor.


class MQTTClient:
    """ 
    author: Delhaye Adrien
    The MQTTCLient class provide a simplified MQTT client based on the paho.mqtt.client class to allows a Actors to connect to the MQTT bus and subscribe or publish data. Each subscription can be linked to one or more callback function that allows to linked the class business job to the bus.
    """

    PROTOCOL = mqtt.MQTTv311

    def __init__(self, host: str="127.0.0.1", port: int=1883, client_id: str = "", username: str = None, password: str = None):

        # Creating Paho MQTT instance
        self._connected_flag = False
        self._client = mqtt.Client(
            client_id=client_id,
            protocol=self.PROTOCOL
        )

        self._host = host
        self._port = port

        self._client.on_connect = self._on_connect
        self._client.on_disconnect = self._on_disconnect
        self._client.on_publish = self._on_publish
        self._client.on_subscribe = self._on_subscribe

        # Allows to re-subscribe to saved topics.
        self._suscribed_topics = {}

    def connect(self):
        """Connect to the MQTT broker."""

        self._client.connect(
            host=self._host,
            port=self._port
        )
        self._client.loop_start()
        logging.debug(f"MQTT Client connected on {self._host}:{self._port}")
        
    @property
    def subscribed_topics(self):
        return self._suscribed_topics
    
    def is_connected(self):
        return self._connected_flag

    def _on_connect(self, client, userdata, flags, rc):
        """_on_connect is executed as soon as a connextion as been made to the broker. Set the connected flag to true.

        Args:
            client (mqtt.Client): the client instance for the connection.
            userdata (): /
            flags (_type_): the response flags sent by the broker.
            rc (int): the connection result.
        """
        logging.debug(f"Connection made to the broker : {mqtt.connack_string(rc)}")
        if rc != mqtt.CONNACK_ACCEPTED:
            logging.error(f"Connection failed : {rc}")
            raise IOError("Couldn't establish an mqtt connection to the broker.")

        # Ensure that in case of connection loss, the already set topics are re-subscribed on reconnection.
        for topic, callbacks in self._suscribed_topics.items():
            self.subscribe(
                topic=topic,
                callbacks=callbacks
            )

        self._connected_flag = True

    def _on_disconnect(self, client, userdata, rc):
        """Set Flag to false then try to reconnect"""

        logging.debug(f"Disconnecting : {userdata}")
        self._connected_flag = False

        reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
        while reconnect_count < MAX_RECONNECT_COUNT:
            logging.info("Reconnecting in %d seconds...", reconnect_delay)
            time.sleep(reconnect_delay)

            try:
                self._client.reconnect()
                logging.info("Reconnected successfully!")
                return
            except Exception as err:
                logging.error("%s. Reconnect failed. Retrying...", err)

            reconnect_delay *= RECONNECT_RATE
            reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
            reconnect_count += 1
        logging.info(f"Reconnect failed after {reconnect_count} attempts. Exiting...")

    def _on_publish(self, client, userdata, mid):
        logging.debug(f"Message published by {client} with {mid}")

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        logging.debug(f"Subscribed to {client} with {userdata}  and qos: {granted_qos}")

    def publish(self, topic: str, data: dict, qos=2) -> mqtt.MQTTMessageInfo:
        """publish a value the the specified topic.

        Args:
            topic (str): a topic string like 'devices/<id>/measures
            data (dict): a dict containing the value to send.
        """

        result = self._client.publish(
            topic=str(topic),
            payload=to_json_string(data),
            qos=qos
        )
        return result
    
    def subscribe(self, topic: str, callbacks: callable | List[callable], **kwargs):
        """subscribe any function with the specified topics. 
        When a message from the topic is received, the function will
        be called with the message content + topic str.
        e.g. : def func(*, userdata: cls,  msg: dict, *args, **kwargs)

        Args:
            topic (str): topic to subscribe
            callbacks (callable or list of callable): a callback or list of callback function that can handle the message from topic. The 
            function should have a definition similar to :
                def func(*, userdata: /, message: /, *args, **kwargs)
        """
        topic = str(topic)
        if not isinstance(callbacks, list):
            callbacks = [callbacks]
   
        try:
            self._client.subscribe(
                topic=topic,
                qos=2,
                
            )
            for callback in callbacks:
                cb = mqtt_callback(callback, topic=topic, **kwargs)
                self._client.message_callback_add(
                    sub=topic,
                    callback=cb
                )
            self._suscribed_topics[topic] = callbacks

        except Exception as err:
            logging.error(f"Could not subscribe to the topic {topic}({type(topic)}) : {err}")

    def unsubscribe(self, topic: str):
        """unsubscribe from a specified topic.

        Args:
            topic (str): topic to unsubscribe.
        """
        if self.is_connected():
            try:
                self._client.message_callback_remove(
                    sub=topic
                )
            except Exception as err:
                logging.error(f"Could not unubscribe from topic {topic} : {err}")
            self._suscribed_topics[topic] = False
            
    def start(self):
        self._client.loop_start()
 
    def stop(self):
        self._client.loop_stop()


def mqtt_callback(func: callable, **kwargs) -> callable:
        def new_func(client, userdata, message, **kwargs):
            data = from_json_string(message.payload)
            func(data, message.topic, **kwargs)
        return new_func