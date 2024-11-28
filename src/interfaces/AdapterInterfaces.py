from abc import ABC, abstractmethod
from typing import List, Optional

from ..DTO.OrderDTO import OrderDTO

class OrderAdapterInterface(ABC):
    
    @abstractmethod
    def orderToJson(orderDTO: OrderDTO):
        pass
    
    