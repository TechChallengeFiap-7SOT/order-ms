from ..DTO.OrderDTO import OrderDTO
from ..interfaces.AdapterInterfaces import OrderAdapterInterface

import json

class OrderAdapter(OrderAdapterInterface):
    def __init__(self):
        super().__init__()
    
    def orderToJson(self, order: OrderDTO):
        
        value = {
            "order_id" : order.id,
            "order_itens" :  order.itens,
            "order_status" : order.status,
            "order_price" : order.price
        }   

        
        # return json.dumps(value)
        return value