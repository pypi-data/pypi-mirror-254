from .http_base import _HttpBase


class _Collections(_HttpBase):
    def create(self, collection_name, collection_id=None):
        try:
            collection = self.get_by_name(collection_name)
        except:
            collection = None

        if collection:
            return collection

        body = {"name": collection_name}
        if collection_id:
            body["id"] = collection_id

        return self._post(path="entity-analytics/v2/collections", data=body)

    def get_by_name(self, collection_name):
        return self._get(path=f"entity-analytics/v2/collections/name/{collection_name}")

    def get_by_id(self, collection_id):
        return self._get(path=f"entity-analytics/v2/collections/{collection_id}")
