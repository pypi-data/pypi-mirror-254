from .http_clients import _Documents, _Collections, _Identities, _References, _Sentences, _Configurations


class EntityAnalytics:
    def __init__(self, host):
        self.documents = _Documents(host)
        self.collections = _Collections(host)
        self.identities = _Identities(host)
        self.references = _References(host)
        self.sentences = _Sentences(host)
        self.configurations = _Configurations(host)
