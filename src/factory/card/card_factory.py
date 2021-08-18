from src.card.plaincard import Card

class AbstractCardFactory:
    
    def make(self, holdername: str) -> Card:
        raise NotImplementedError
