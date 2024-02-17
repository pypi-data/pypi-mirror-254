import io
import json
import logging
import sqlite3
import time
from contextlib import contextmanager
from multiprocessing import Value, Lock
from pathlib import Path

import cv2
import flickrapi
from flickrapi.auth import FlickrAccessToken

log = logging.getLogger(__name__)


class MuxingFailedException(Exception):
    pass


class SQLite:
    def __init__(self, db_name="hive.db"):
        if Path(db_name).exists():
            self.con = sqlite3.connect(db_name)
        else:
            self.con = sqlite3.connect(db_name)
            with self.con:
                self.con.execute("""
                    CREATE TABLE AGGREGATED (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        data json,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                    );
                """)

    def get_data(self):
        with self.con:
            return list(self.con.execute("SELECT * FROM AGGREGATED ORDER BY datetime(timestamp) DESC"))

    def add_data(self, data):
        with self.con:
            return self.con.execute(f"INSERT INTO AGGREGATED (data) VALUES ('{data}')")


class Flickr:
    current_uploads = Value('i', 0)
    current_uploads_lock = Lock()
    tasks = []
    api_key = u'8dfbe57f8720986d31b0a3a9a6a4ad47'
    api_secret = u'd97bc585b9c8f208'
    token = FlickrAccessToken("72157720847862160-7cd598444a7f6082", "b312ee0165b84592", "write")


    def __init__(self, max_parallel_uploads=5):
        self.max_parallel_uploads = max_parallel_uploads
        self.flickr = flickrapi.FlickrAPI(self.api_key, self.api_secret, token=self.token)
        self.flickr.authenticate_via_browser(perms='write')

    @contextmanager
    def _available_net(self):
        available = False
        while not available:
            self.current_uploads_lock.acquire()
            available = self.current_uploads.value < self.max_parallel_uploads
            if not available:
                self.current_uploads_lock.release()
                log.info("Upload pending - parallel uploads limit reached")
                time.sleep(1)
            else:
                self.current_uploads.value += 1
                self.current_uploads_lock.release()
        log.info("Current uploads: {} (max: {})".format(self.current_uploads.value, self.max_parallel_uploads))
        try:
            yield
        finally:
            self.current_uploads_lock.acquire()
            log.info("Upload finished")
            self.current_uploads.value -= 1
            self.current_uploads_lock.release()

    def get_photo_url(self, photo_id):
        data = json.loads(self.flickr.photos.getInfo(photo_id=photo_id, format='json'))["photo"]
        return f"https://farm{data['farm']}.staticflickr.com/{data['server']}/{data['id']}_{data['secret']}.jpg"

    def store_frame(self, frame, key):
        log.info("Storing frame at key {}".format(key))
        buf = io.BytesIO(cv2.imencode(".png", frame)[1])
        with self._available_net():
            raw = self.flickr.upload(filename=key, fileobj=buf, title=key, description=key, format="rest").decode()
            photo_id = raw[raw.index("<photoid>")+len("<photoid>"):raw.index("</photoid>")]

        result = self.get_photo_url(photo_id)
        log.info("Frame stored. URL: {}".format(result))
        return result

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return
