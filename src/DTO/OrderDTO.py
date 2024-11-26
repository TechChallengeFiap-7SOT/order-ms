from dataclasses import dataclass

@dataclass
class OrderDTO:
    
    id: str 
    itens: dict
    status: int 
    price: int