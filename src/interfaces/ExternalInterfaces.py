from abc import ABC, abstractmethod
from typing import List, Optional

from ..DTO.OrderDTO import OrderDTO

class OrderExternalInterface:
    
    @abstractmethod
    def get(orderID: str):
        pass
    
    @abstractmethod
    def create(orderDTO: OrderDTO):
        pass
    
    @abstractmethod
    def Delete(orderID: str):
        pass
    
    @abstractmethod
    def Change(orderID: str, orderStatus: int):
        pass

class PaymentExternalInterface:
    
    @abstractmethod
    def request(id, price):
        pass