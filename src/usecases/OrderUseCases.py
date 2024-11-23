from ..entities.Order import Order
from ..interfaces.GatewaysInterfaces import OrderGatewayInterface
from ..DTO.OrderDTO import OrderDTO

class OrderUseCases:
    
    @staticmethod
    def createOrder(OrderDTO: OrderDTO):
        newOrder = Order(OrderDTO.id, 
                         OrderDTO.itens, 
                         OrderDTO.status,
                         OrderDTO.price)
    
    @staticmethod
    def modifyStatus():
        pass