from .http_base import _HttpBase
from ..utils.linking_configuration import LinkingConfiguration

import requests
import json


class _Documents(_HttpBase):
    def link_document(self, documents, config: LinkingConfiguration):
        config.print_summary()

        path = f"entity-analytics/v2/collections/{config.collection}/documents/link"
        files = [('documents', (f'{doc["title"]}.txt', doc["text"])) for doc in documents]
        data = config.to_request_data()

        response = requests.post(f"{self.host}/{path}", files=files, data=data)

        response.raise_for_status()

        return json.loads(response.content)

    def get_by_id(self):
        pass

    def get_by_title(self):
        pass

    def list_documents(self):
        pass

    def delete_document(self):
        pass
