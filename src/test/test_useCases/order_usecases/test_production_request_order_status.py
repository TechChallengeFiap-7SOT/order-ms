import pytest
from ....usecases.OrderUseCases import OrderUseCases
from ....DTO.OrderDTO import OrderDTO
from ....entities.Order import Order
from unittest.mock import Mock

def test_confirm_payment_status():

    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderInitial = Order("12345", itens, 1, price)



    orderChanged = Order("12345", itens, 3, price)
    orderGateway = Mock()
    orderGateway.changeOrderStatus.return_value  =  orderChanged


    ############# VALIDANDO SE O STATUS MUDA DE 3 PARA 4 ####################
    order = OrderUseCases.productionRequestOrderStatus(orderInitial, orderGateway)
    assert order.status == 4
    ##########################################################################


    ############# VALIDANDO SE OCORRE UM ERRO AO TENTAR COLOCAR ESSE STATUS EM UMA ORDER QUE JA ESTA COM ELE OU A CIMDA DELE ####################
    with pytest.raises(Exception) as excinfo:
        OrderUseCases.productionRequestOrderStatus(order, orderGateway)
    
    assert str(excinfo.value) == "Essa order já teve sua solicitação de produção feita."
    ##########################################################################


   