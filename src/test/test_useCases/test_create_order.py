from ...usecases.OrderUseCases import OrderUseCases
from ...DTO.OrderDTO import OrderDTO
from unittest.mock import Mock

def test_create_order():
    
    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    order = OrderDTO(None, itens, 0, price)
    
    orderGateway = Mock()
    orderGateway.createOrder.return_value  =  {}
    
    order = OrderUseCases.createOrder(order,)

    