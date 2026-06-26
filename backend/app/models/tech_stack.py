from dataclasses import dataclass


@dataclass
class TechStack:

    name: str

    category: str

    confidence: float

    detected_by: str

    def to_dict(self):

        return {

            "name": self.name,

            "category": self.category,

            "confidence": self.confidence,

            "detected_by": self.detected_by

        }