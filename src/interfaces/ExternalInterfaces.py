from abc import ABC, abstractmethod
from typing import List, Optional

from ..DTO.OrderDTO import OrderDTO

class OrderExternalInterface:
    
    @abstractmethod
    def get(orderID: str) -> Optional[OrderDTO]:
        pass
    
    @abstractmethod
    def create(orderDTO: OrderDTO) -> Optional[OrderDTO]:
        pass
    
    @abstractmethod
    def Delete(orderID: str) -> Optional[int]:
        pass
    
    @abstractmethod
    def Change(orderID: str, orderStatus: int) -> Optional[OrderDTO]:
        pass

class PaymentExternalInterface:
    
    @abstractmethod
    def request(id, price):
        pass

class ProductionExternalInterface:
    
    @abstractmethod
    def requestProductionAPi(orderDTO: OrderDTO):
        pass