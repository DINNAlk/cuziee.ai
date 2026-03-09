from models.base_model import BaseExpertModel


class RelationshipModel(BaseExpertModel):
    def __init__(self):
        super().__init__(
            system_prompt= """
            You are a relationship expert.
            Help with love, communication, trust, breakups, jealousy and healthy relationships.
            Never promoter manipulation or toxic behavior.
            """
        )