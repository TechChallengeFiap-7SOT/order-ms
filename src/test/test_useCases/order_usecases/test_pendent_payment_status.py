import pytest
from ....usecases.OrderUseCases import OrderUseCases
from ....DTO.OrderDTO import OrderDTO
from ....entities.Order import Order
from unittest.mock import Mock

def test_confirm_payment_status():

    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderInitial = Order("12345", itens, 1, price)



    orderChanged = Order("12345", itens, 2, price)
    orderGateway = Mock()
    orderGateway.changeOrderStatus.return_value  =  orderChanged


    ############# VALIDANDO SE O STATUS MUDA DE 1 PARA 2 ####################
    order = OrderUseCases.pendentPaymentStatus(orderInitial, orderGateway)
    assert order.status == 2
    ##########################################################################


    ############# VALIDANDO SE OCORRE UM ERRO AO TENTAR COLOCAR ESSE STATUS EM UMA ORDER QUE JA ESTA COM ELE ####################
    with pytest.raises(Exception) as excinfo:
        OrderUseCases.pendentPaymentStatus(order, orderGateway)
    
    assert str(excinfo.value) == "Essa order já está com o status 'pagamento pendente'."
    ##########################################################################


    ############# VALIDANDO SE OCORRE UM ERRO AO TENTAR COLOCAR ESSE STATUS EM UMA ORDER QUE ESTÁ COM UM STATUS MAIOR QUE ELE ####################
    with pytest.raises(Exception) as excinfo:
        order.status = 3
        OrderUseCases.pendentPaymentStatus(order, orderGateway)

    assert str(excinfo.value) == "Essa order já está com o status a cima do pagamento pendente."
    ##########################################################################