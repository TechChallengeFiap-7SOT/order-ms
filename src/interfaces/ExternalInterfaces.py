from abc import ABC, abstractmethod
from typing import List, Optional


class PaymentExternalInterface(ABC):
    
    @abstractmethod 
    def requestPayment(id: int, price: int) -> Optional[int]: 
        pass
    
class ProductionExternalInterface(ABC):
    
    @abstractmethod
    def requestProduction(id: int, itens: dict) -> Optional[bool]:
        pass