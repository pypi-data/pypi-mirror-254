import logging
import os
import dataclasses
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from home_link.models import Entity


class Firebase:
    _instance = None
    _initialize = False

    def __init__(self) -> None:
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def init_firebase(self, cert_json: str):
        if cert_json is None or not os.path.exists(cert_json):
            raise Exception("error file %s firebase certificate not exist!", cert_json)
        self.cert_json = cert_json
        cred = credentials.Certificate(self.cert_json)
        logging.info("initialize firebase")
        try:
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self._initialize = True
        except ValueError as err:
            logging.error("error initialize firebase, cause: %s", err)

    @property
    def is_initialize(self) -> bool:
        return self._initialize

    def publish(self, device_name: str, new_entity: Entity):
        logging.info("publish new entity %s to firebase db collection %s", new_entity.name, device_name)
        try:
            self.db.collection(device_name).add(dataclasses.asdict(new_entity))
        except Exception as err:
            logging.error("error publish new entity %s to firebase db, cause: %s", device_name, err)
