import hashlib
import json

from enum import Enum
from time import time


class EventKind(Enum):
    SET_METADATA = 0
    TEXT_NOTE = 1
    RECOMMEND_SERVER = 2


class Event:
    def __init__(self, pubkey, content, tags=None, created_at=None):
        self.pubkey = pubkey.lower()
        self.created_at = created_at or int(time())
        self.kind = 0
        self.tags = tags or []
        self.content = content
        self.sig = 0

    @property
    def id(self):
        data = [0, self.pubkey, self.created_at, self.kind, self.tags, self.content]
        jd = json.dumps(data).encode("utf-8")
        return hashlib.sha256(jd).hexdigest()
