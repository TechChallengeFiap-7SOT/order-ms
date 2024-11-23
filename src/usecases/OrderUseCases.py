from ..entities.Order import Order
from ..interfaces.GatewaysInterfaces import OrderGatewayInterface
from ..DTO.OrderDTO import OrderDTO

import uuid

class OrderUseCases:
    
    @staticmethod
    def createOrder(OrderDTO: OrderDTO, orderGateway: OrderGatewayInterface):

        orderId = uuid.uuid4()
        orderStatus = 1

        newOrder = Order(orderId, 
                         OrderDTO.itens, 
                         orderStatus,
                         OrderDTO.price)
        
        try:
            status = orderGateway.createOrder(newOrder.id, 
                                            newOrder.itens, 
                                            newOrder.status, 
                                            newOrder.price)
        except:
            raise Exception("Houve um problema ao salvar uma ordem criada no repositório de dados.")
                
        return newOrder

    @staticmethod
    def modifyStatus(orderId: str, newOrderStatus: int, orderGateway: OrderGatewayInterface):
        orderDto = orderGateway.getOrder(orderId)

        order = Order(orderDto.id, 
                      orderDto.itens, 
                      orderDto.status,
                      orderDto.price)
        
        if (order.status == newOrderStatus):
            raise Exception("O pedido atual já tem o mesmo status que o informado.")
        
        order.status = newOrderStatus

        orderGateway.changeOrderStatus(order.id, order.status)