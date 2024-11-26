from ..interfaces.ExternalInterfaces import OrderExternalInterface
from ..DTO.OrderDTO import OrderDTO

class OrderDbConnector(OrderExternalInterface):
    
    def __init__(self):
        super().__init__()
        
    def get(self, orderID: str):
        return True
    
    
    def create(self, orderDTO: OrderDTO):
        return True
    
    
    def Delete(self, orderID: str):
        return True
    
    
    def Change(self, orderID: str, orderStatus: int):
        return True