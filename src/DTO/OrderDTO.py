from dataclasses import dataclass

@dataclass
class OrderDTO:
    
    id: str = None
    itens: dict
    status: int = None
    price: int