from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.Order import Order

class OrderGatewayInterface(ABC):

    @abstractmethod 
    def getOrder(id: str) -> Optional[Order]: 
        pass
    
    @abstractmethod 
    def createOrder(id : str, itens : dict, status: int, price: int) -> Optional[Order]: 
        pass
    
    @abstractmethod 
    def deleteOrder(id: str) -> Optional[int]: 
        pass
    
    @abstractmethod 
    def changeOrderStatus(id: str, status: int) -> Optional[Order]: 
        pass
    

class PaymentGatewayInterface(ABC):
    
    @abstractmethod 
    def requestPayment(id: int, price: int) -> Optional[int]: 
        pass
    
class ProductionGatewayInterface(ABC):
    
    @abstractmethod
    def requestProduction(order: Order) -> Optional[bool]:
        pass
