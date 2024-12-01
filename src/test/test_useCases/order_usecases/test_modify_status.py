import pytest
from ....usecases.OrderUseCases import OrderUseCases
from ....DTO.OrderDTO import OrderDTO
from ....entities.Order import Order
from unittest.mock import Mock

def test_confirm_payment_status():

    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderInitial = Order("12345", itens, 1, price)

    newOrderStatus = 2

    orderChanged = Order("12345", itens, newOrderStatus, price)
    orderGateway = Mock()
    orderGateway.changeOrderStatus.return_value  =  orderChanged

    #Alterando o Id de 1 para 2

    order = OrderUseCases.modifyStatus(orderInitial, newOrderStatus, orderGateway)
    assert order.status == newOrderStatus
    
    #Alterando o Id de 2 para 2 -> deve lançar um erro, pois o ID é o mesmo.

    with pytest.raises(Exception) as excinfo:
        OrderUseCases.modifyStatus(order, newOrderStatus, orderGateway)
    
    assert str(excinfo.value) == "O pedido atual já tem o mesmo status que o informado."