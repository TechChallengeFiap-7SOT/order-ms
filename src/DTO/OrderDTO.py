from dataclasses import dataclass

@dataclass
class OrderDTO:
    
    id: int
    itens: dict
    status: int
    price: int