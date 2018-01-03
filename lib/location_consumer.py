import paho.mqtt.client as mqtt
import ssl
import json
from lumada.exception.asset_client_exception import AssetClientException

""" Location Consumer

Establishes a connection to Lumada and subscribes to the Event channel.
Extracts location data from the message payload.

Refer to the MqttCommunicationChannel class in the python lumada sdk for more
information
"""
class LocationConsumer:
    # Initialize and oonfigure client
    def __init__(self, host, username, password, asset_id, topics, port=8883):
        self._client = mqtt.Client(transport="ssl")
        self._asset_id = asset_id
        self._topics = topics
        self._host = host
        self._port = port

        self._client.on_connect = self._on_connect
        self._client.on_message = self._on_message
        self._client.on_subscribe = self._on_subscribe

        self._client.username_pw_set(username, password)
        self._client.tls_set_context(ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2))
        self._client.tls_insecure_set(True)

    def _on_connect(self, client, userdata, flags, rc):
        if (rc != 0):
           raise AssetClientException(message="Unknown connection error", cause="Return Code: %s" % rc)
        print("Connected")
        
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        sc = client.subscribe(self._topics)
        
	# The callback for when a message is received from the server.
    def _on_message(self, client, userdata, msg):
        print("Message Received. Extracting location data")
        location_data = self._extract_location_data(msg.payload)
        print("Received location alert for: " + location_data['latitude'])

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed")

    def _on_log(self, client, userdata, level, buf):
        print(buf)

    def _extract_location_data(self, payload):
        return json.loads(payload)['data']

    def connect(self):
        # client.on_log = self._on_log
        print("Connecting to client")
        self._client.connect(host=self._host, port=self._port, keepalive=60)
        self._client.loop_forever()