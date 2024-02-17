from typing import Optional, Mapping, Any

try:
    import bson
    import pymongo
    from bson.objectid import ObjectId
except Exception:
    bson = None
    pymongo = None
    ObjectId = None
from .mongo import MongoWorkflowDbClient


class PyMongoWorkflowDbClient(MongoWorkflowDbClient, register_name="pymongo"):
    """Client of an external Mongo database for storing workflow executions."""

    def connect(self, url: str, database: str, collection: str):
        if pymongo is None:
            return
        client = pymongo.MongoClient(url, serverSelectionTimeoutMS=1000)
        self._client = client
        self._collection = client[database][collection]

    def disconnect(self, *args, **kw):
        self._collection = None
        if self._client is not None:
            self._client.close()
            self._client = None

    def generateWorkflowId(self, oid: Optional[str] = None) -> ObjectId:
        return ObjectId(oid=oid)

    def generateActorId(self, oid: Optional[str] = None) -> ObjectId:
        return ObjectId(oid=oid)

    def _appendActorInfo(self, actorInfo: dict):
        self._safe_update_one(
            {"_id": self._workflowId}, {"$push": {"actors": actorInfo}}
        )

    def _sanitize(self, value: Any) -> Any:
        if isinstance(value, Mapping):
            return {k: self._sanitize(v) for k, v in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [self._sanitize(v) for v in value]
        if not any(isinstance(value, t) for t in bson._BUILT_IN_TYPES):
            return repr(value)
        return value
