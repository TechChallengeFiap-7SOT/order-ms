from ..interfaces.GatewaysInterfaces import ProductionGatewayInterface, OrderGatewayInterface
from ..entities.Order import Order

from ..usecases.OrderUseCases import OrderUseCases

class ProductionUseCases():
    
    @staticmethod
    def requestProduction(order: Order, productionGateway: ProductionGatewayInterface, orderGateway: OrderGatewayInterface):
        productionStatus = productionGateway.requestProduction(order)
        
        if productionStatus:
            order = OrderUseCases.productionRequestOrderStatus(order, orderGateway)
        
        return order
    