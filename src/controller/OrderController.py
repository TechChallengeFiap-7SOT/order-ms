from ..usecases.OrderUseCases import OrderUseCases
from ..usecases.PaymentUseCases import PaymentUseCases
from ..usecases.ProductionUseCases import ProductionUseCases
from ..DTO.OrderDTO import OrderDTO

from ..interfaces.ExternalInterfaces import OrderExternalInterface, PaymentExternalInterface, ProductionExternalInterface
from ..interfaces.AdapterInterfaces import OrderAdapterInterface
from ..gateways.OrderGateway import OrderGateway
from ..gateways.PaymentGateway import PaymentGateway
from ..gateways.ProductionGateway import ProductionGateway
from ..entities.Order import Order

class OrderController:
    
    @staticmethod
    def makeOrder(orderDTO: OrderDTO, 
                  orderDb: OrderExternalInterface, 
                  paymentExternal: PaymentExternalInterface,
                  orderAdapter: OrderAdapterInterface):
        
        orderGateway = OrderGateway(orderDb)
        # paymentGateway = PaymentGateway(paymentExternal)
        
        order = OrderUseCases.createOrder(orderDTO, orderGateway)

        paymentStatus = OrderController.requestPayment(order.id, paymentExternal, orderDb)#PaymentUseCases.requestPayment(order, paymentGateway)
        
        order = OrderUseCases.pendentPaymentStatus(order, orderGateway)
        
        orderDTO = OrderDTO(order.id, order.itens, order.status, order.price)
        
        response = orderAdapter.orderToJson(orderDTO)
        
        return response
    
    @staticmethod
    def requestPayment(orderId: str, paymentExternal: PaymentExternalInterface, orderDb: OrderExternalInterface):
        orderGateway = OrderGateway(orderDb)
        order = OrderUseCases.getORder(orderId, orderGateway)
        
        paymentGateway = PaymentGateway(paymentExternal)
        paymentStatus = PaymentUseCases.requestPayment(order, paymentGateway)
        return paymentStatus
    
    @staticmethod
    def getOrder(orderId: str,
                     orderDb: OrderExternalInterface,
                     orderAdapter: OrderAdapterInterface):
        
        orderGateway = OrderGateway(orderDb)
        order = OrderUseCases.getORder(orderId, orderGateway)
        orderDTO = OrderDTO(order.id, order.itens, order.status, order.price)
        response = orderAdapter.orderToJson(orderDTO)
        
        return response
    
    @staticmethod
    def confirmOrderPayment(orderId: str,  
                     orderDb: OrderExternalInterface):
        
        orderGateway = OrderGateway(orderDb)
        orderDTO = orderGateway.getOrder(orderId)
        order = OrderController.OrderDtoToEntitie(orderDTO)
        
        confirmedPaymentOrder = OrderUseCases.confirmPaymentStatus(order, orderGateway)
                
        return "{'status' : 'ok'}"
    
    @staticmethod
    def requestOrderProduction(orderId: str, 
                               orderDb: OrderExternalInterface,
                               productionExternal: ProductionExternalInterface):
        
        orderGateway = OrderGateway(orderDb)
        orderDTO = orderGateway.getOrder(orderId)
        order = OrderController.OrderDtoToEntitie(orderDTO)
        
        productionGateway = ProductionGateway(productionExternal)
        
        order = ProductionUseCases.requestProduction(order, productionGateway ,orderGateway)
        
        return "{'status' : 'ok'}"
        
    
    @staticmethod 
    def OrderDtoToEntitie(orderDto: OrderDTO):
        order = Order(orderDto.id,
                      orderDto.itens,
                      orderDto.status,
                      orderDto.price)
        
        return order