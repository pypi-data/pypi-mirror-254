from typing import List, Dict, Any

from tabulate import tabulate


class LinkingConfiguration:
    def __init__(
            self,
            collection: str = "default",
            async_mode: bool = False,
            test_mode: bool = True,
            debug_mode: bool = True,
            overwrite_if_exists: bool = False,
            use_ai_scorer: bool = False,
            include_text: bool = False,
            extract_coref: bool = True,
            ghost_creation_threshold: float = 50,
            ner_extractors: List[str] = ["mBERT"],
            relation_extractor_type: str = "OpenIE",
            include_identity_fields: str = "aliases,references,relations,digitalAliases,confidenceScoreExplainer",
            num_of_near_identities: int = 1,
    ):
        self.collection = collection
        self.async_mode = async_mode
        self.test_mode = test_mode
        self.debug_mode = debug_mode
        self.overwrite_if_exists = overwrite_if_exists
        self.use_ai_scorer = use_ai_scorer
        self.include_text = include_text
        self.extract_coref = extract_coref
        self.ghost_creation_threshold = ghost_creation_threshold
        self.ner_extractors = ner_extractors
        self.relation_extractor_type = relation_extractor_type
        self.num_of_near_identities = num_of_near_identities
        self.include_identity_fields = include_identity_fields

    def to_request_data(self) -> Dict[str, Any]:
        return {
            "asyncMode": self.async_mode,
            "testMode": self.test_mode,
            "debugMode": self.debug_mode,
            "overwriteIfExists": self.overwrite_if_exists,
            "useAiScorer": self.use_ai_scorer,
            "includeText": self.include_text,
            "extractCoref": self.extract_coref,
            "ghostCreationThreshold": self.ghost_creation_threshold,
            "nerExtractors": self.ner_extractors,
            "relationExtractorType": self.relation_extractor_type,
            "numOfNearIdentities": self.num_of_near_identities,
            "includeIdentityFields": self.include_identity_fields,

        }

    def update_from_dict(self, config_dict: Dict[str, Any]):
        for key, value in config_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def print_summary(self):
        headers = ["Attribute", "Value"]
        data = [(key, value.split(",") if isinstance(value, str) and "," in value else value)
                for key, value in vars(self).items()]

        table = tabulate(data, headers=headers, tablefmt="fancy_grid", maxcolwidths=[30, 10],
                         colalign=("center", "center"))

        print("📗 Linking Configuration Summary 📗")
        print(table)
