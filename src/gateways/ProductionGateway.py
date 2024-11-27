from ..interfaces.GatewaysInterfaces import ProductionGatewayInterface
from ..interfaces.ExternalInterfaces import ProductionExternalInterface
from ..entities.Order import Order
from ..DTO.OrderDTO import OrderDTO

from typing import List, Optional

class ProductionGateway(ProductionGatewayInterface):
    def __init__(self, productionExternal: ProductionExternalInterface):
        super().__init__()
        self._productionExternal = productionExternal 
    
    def requestProduction(self, order: Order) -> Optional[bool]:
        
        orderDTO = OrderDTO(order.id,
                            order.itens,
                            order.status,
                            order.price)
        
        productionStatus = self._productionExternal(orderDTO)
        
        return productionStatus