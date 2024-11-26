from ..interfaces.GatewaysInterfaces import OrderGatewayInterface
from ..interfaces.ExternalInterfaces import OrderExternalInterface
from ..entities.Order import Order
from ..DTO.OrderDTO import OrderDTO

from typing import List, Optional

class OrderGateway(OrderGatewayInterface):
    
    def __init__(self, orderDb: OrderExternalInterface):
        super().__init__()
        self._orderDb = orderDb
        
    def getOrder(self, id: str) -> Optional[Order]: 
        print("Retornando DTO da order...")
        return True
    
    def createOrder(self, id : str, itens : dict, status: int, price: int) -> Optional[Order]: 
        orderDto = OrderDTO(id, itens, status, price)
        status = self._orderDb.create(orderDto)
        return status
    
    def deleteOrder(self, id: str) -> Optional[int]: 
        return True
    
    def changeOrderStatus(self, id: str, status: int) -> Optional[Order]: 
        return True
        
        