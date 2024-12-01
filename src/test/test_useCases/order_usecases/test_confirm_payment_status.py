from ....usecases.OrderUseCases import OrderUseCases
from ....DTO.OrderDTO import OrderDTO
from ....entities.Order import Order
from unittest.mock import Mock

def test_confirm_payment_status():

    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderInitial = Order("12345", itens, 2, price)
    orderChanged = Order("12345", itens, 3, price)
    
    orderGateway = Mock()

    orderGateway.changeOrderStatus.return_value  =  orderChanged

    order = OrderUseCases.confirmPaymentStatus(orderInitial, orderGateway)

    assert order.status == 3