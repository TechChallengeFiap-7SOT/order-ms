from abc import ABC, abstractmethod
from typing import List, Optional

from ..DTO.OrderDTO import OrderDTO
class ExampleAdapterInterfaces(ABC):
    
    @abstractmethod 
    def example(x: str) -> Optional[1]: 
        pass
    
class OrderAdapterInterface(ABC):
    
    @abstractmethod
    def orderToJson(orderDTO: OrderDTO):
        pass
    
    