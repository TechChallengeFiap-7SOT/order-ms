from ..entities.Order import Order
from ..interfaces.GatewaysInterfaces import OrderGatewayInterface
from ..DTO.OrderDTO import OrderDTO

import uuid

class OrderUseCases:
    
    @staticmethod
    def createOrder(OrderDTO: OrderDTO, orderGateway: OrderGatewayInterface):

        orderId = str(uuid.uuid4())
        orderStatus = 1

        newOrder = Order(orderId, 
                         OrderDTO.itens, 
                         orderStatus,
                         OrderDTO.price)
        
        # try:
        status = orderGateway.createOrder(newOrder.id, 
                                            newOrder.itens, 
                                            newOrder.status, 
                                            newOrder.price)
        # except():
        #     raise Exception("Houve um problema ao salvar uma ordem criada no repositório de dados.")
                
        return newOrder
    
    @staticmethod
    def getORder(orderId: str, orderGateway: OrderGatewayInterface):
        order = orderGateway.getOrder(orderId)
        return order

    @staticmethod
    def confirmPaymentStatus(order: Order, orderGateway: OrderGatewayInterface):
        if order.status >= 3:
            raise Exception("Essa order já teve seu pagamento confirmado.")
        
        newOrder = OrderUseCases.modifyStatus(order, 3, orderGateway)
        return newOrder
    
    @staticmethod
    def productionRequestOrderStatus(order: Order, orderGateway: OrderGatewayInterface):
        print(order.status)
        if order.status >= 4:
            raise Exception("Essa order já teve sua solicitação de produção feita.")
        
        newOrder = OrderUseCases.modifyStatus(order, 4, orderGateway)
        return newOrder
    
    @staticmethod
    def pendentPaymentStatus(order: Order, orderGateway: OrderGatewayInterface):
        if order.status == 2:
            raise Exception("Essa order já está com o status 'pagamento pendente'.")
        elif order.status > 2:
            raise Exception("Essa order já está com o status a cima do pagamento pendente.")
            
        
        newOrder = OrderUseCases.modifyStatus(order, 2, orderGateway)
        return newOrder

    @staticmethod
    def modifyStatus(order: Order, newOrderStatus: int, orderGateway: OrderGatewayInterface):
        if (order.status == newOrderStatus):
            raise Exception("O pedido atual já tem o mesmo status que o informado.")
        
        order.status = newOrderStatus

        status = orderGateway.changeOrderStatus(order.id, order.status)
        
        if not status:
            raise Exception("Houve um problema ao mudar o status da order {}".format(order.id))
        
        return order