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
        # print("Retornando DTO da order...")
        orderDto = self._orderDb.get(id)
        order = Order(orderDto.id, orderDto.itens, orderDto.status, orderDto.price)
        return order
    
    def createOrder(self, id : str, itens : dict, status: int, price: int) -> Optional[Order]: 
        orderDto = OrderDTO(id, itens, status, price)
        orderDtoDb = self._orderDb.create(orderDto)
        order = Order(orderDtoDb.id, orderDtoDb.itens, orderDtoDb.status, orderDtoDb.price)
        return order
    
    def deleteOrder(self, id: str) -> Optional[int]: 
        return True
    
    def changeOrderStatus(self, id: str, status: int) -> Optional[Order]: 
        orderDto = self._orderDb.Change(id, status)
        order = Order(orderDto.id, orderDto.itens, orderDto.status, orderDto.price)
        return order
        
        