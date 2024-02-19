import json

from requests import get, post


class _HttpBase:
    def __init__(self, host):
        self.host = host

    def _post(self, path, data, files=None):
        response = post(
            url=f"{self.host}/{path}",
            data=data,
            files=files
        )

        response.raise_for_status()

        return json.loads(response.content)

    def _get(self, path):
        response = get(url=f"{self.host}/{path}")
        response.raise_for_status()

        return json.loads(response.content)
