from ...usecases.OrderUseCases import OrderUseCases
from ...DTO.OrderDTO import OrderDTO
from ...entities.Order import Order
from unittest.mock import Mock

def test_create_order():
    
    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    order = OrderDTO(None, itens, 0, price)
    
    orderGateway = Mock()
    orderExample = Order("12345",itens,1,price)
    orderGateway.createOrder.return_value  =  orderExample
    
    order = OrderUseCases.createOrder(order, orderGateway)
    
    assert type(order) == Order
    assert order == orderExample
    

    