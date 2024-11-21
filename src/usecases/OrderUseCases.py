from ..entities.Order import Order
from ..interfaces.GatewaysInterfaces import OrderGatewayInterface

class OrderUseCases:
    
    @staticmethod
    def createOrder(id : int, itens : dict, status: int, price: int):
        newOrder = Order(id, itens, status, price)
    
    @staticmethod
    def modifyStatus():
        pass