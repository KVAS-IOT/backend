from loguru import logger
import paho.mqtt.client as mqtt

from config.environment_variables import MQTT_USERNAME, MQTT_PASSWORD, MQTT_ADDRESS, MQTT_PORT


class MQTTReaderService:
    _instance = None
    client = None

    labs_to_check: list[str] = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MQTTReaderService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self.client:
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

            self.client.on_connect = self._on_connect
            self.client.on_message = self._on_message

            self.client.connect(MQTT_ADDRESS, MQTT_PORT, 60)

            self.client.loop_start()
            logger.info("MQTT Reader Service started")

    @staticmethod
    def _on_connect(client: mqtt.Client, userdata, flags, reason_code, properties):
        logger.debug(f"Connected with result code {reason_code}")

        client.subscribe("kpi/+/metrics/attendance")

    def _on_message(self, client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
        logger.debug(f"Message received: {msg.payload}")
        logger.debug(f"Topic: {msg.topic}")
