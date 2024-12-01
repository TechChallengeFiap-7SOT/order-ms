from src.usecases.PaymentUseCases import PaymentUseCases
from src.entities.Order import Order
from unittest.mock import Mock
import pytest

def test_request_payment():
    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderInitial = Order("12345", itens, 1, price)

    paymentGateway = Mock()
    paymentGateway.requestPayment.return_value = True

    status = PaymentUseCases.requestPayment(orderInitial, paymentGateway)

    assert status == True
    
    wrongPrice = -50
    wrongOrder = Order("12345", itens, 1, wrongPrice)

    with pytest.raises(Exception) as excinfo:
        status = PaymentUseCases.requestPayment(wrongOrder, paymentGateway)

    assert str(excinfo.value) == "O preço da order não por ser menor ou igual a 0."