import asyncio
import json
from loguru import logger
import paho.mqtt.client as mqtt

from config.environment_variables import MQTT_USERNAME, MQTT_PASSWORD, MQTT_ADDRESS, MQTT_PORT
from dtos.AttendanceDTOs import AttendanceAddDTO
from dtos.LabDTOs import LabGetDTO
from services.LabService import LabService


class MQTTReaderService:
    _instance = None
    client = None

    labs_to_check: list[LabGetDTO] = []

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

            self.loop = asyncio.get_event_loop()

            asyncio.run_coroutine_threadsafe(self.update_labs_to_check(), self.loop)

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

        asyncio.run_coroutine_threadsafe(self.process_message(msg), self.loop)

    def get_suitable_lab_from_topic(self, topic: str) -> LabGetDTO:
        lab_from_topic = topic.split("/")[1]

        suitable_lab = None
        for lab in self.labs_to_check:
            if lab.name.lower() == lab_from_topic:
                suitable_lab = lab
                break

        return suitable_lab

    async def process_message(self, msg: mqtt.MQTTMessage):
        lab_from_topic = msg.topic.split("/")[1]

        lab_to_insert = self.get_suitable_lab_from_topic(msg.topic)

        if not lab_to_insert:
            logger.error(f"Lab {lab_from_topic} not found")
            return

        payload = json.loads(msg.payload)
        logger.debug(f"Payload: {payload}")


        await LabService.update_lab_last_update_time(lab_to_insert.id, payload["update_time"])


    async def update_labs_to_check(self):
        self.labs_to_check = await LabService.get_all_labs()
