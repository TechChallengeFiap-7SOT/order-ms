from ....usecases.OrderUseCases import OrderUseCases
from ....DTO.OrderDTO import OrderDTO
from ....entities.Order import Order
from unittest.mock import Mock

def test_get_order():
    
    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderId = "12345"
    orderGet= Order("12345", itens, 3, price)

    orderGateway = Mock()
    orderGateway.getOrder.return_value  =  orderGet
    
    order = OrderUseCases.getORder(orderId, orderGateway)
    
    assert type(order) == Order
    assert order == orderGet
    

    