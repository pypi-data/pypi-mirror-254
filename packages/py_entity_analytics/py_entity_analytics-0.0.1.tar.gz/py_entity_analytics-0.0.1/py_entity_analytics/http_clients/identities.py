from .http_base import _HttpBase


class _Identities(_HttpBase):

    def get_by_id(self, identity_id):
        return self._get(path=f"entity-analytics/v2/identities/{identity_id}")
