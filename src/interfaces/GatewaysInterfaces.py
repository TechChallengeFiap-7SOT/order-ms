from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.Order import Order

class OrderGatewayInterface(ABC):

    @abstractmethod 
    def getOrder(id: int) -> Optional[Order]: 
        pass
    
    @abstractmethod 
    def createOrder(id : int, itens : dict, status: int, price: int) -> Optional[Order]: 
        pass
    
    @abstractmethod 
    def deleteOrder(id: int) -> Optional[int]: 
        pass
    
    @abstractmethod 
    def changeOrderStatus(id: int, status, int) -> Optional[Order]: 
        pass

class PaymentGatewayInterface(ABC):
    
    @abstractmethod 
    def requestPayment(id: int, price: int) -> Optional[int]: 
        pass
    
class ProductionGatewayInterface(ABC):
    
    @abstractmethod
    def requestProduction(id: int, itens: dict) -> Optional[bool]:
        pass