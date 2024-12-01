from src.usecases.ProductionUseCases import ProductionUseCases
from src.entities.Order import Order
from unittest.mock import Mock
import pytest

def test_request_production():

    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    orderInitial = Order("12345", itens, 1, price)

    productionGateway = Mock()
    productionGateway.requestProduction.return_value = True

    orderGateway = Mock()

    requestorder = ProductionUseCases.requestProduction(orderInitial, productionGateway, orderGateway)

    assert requestorder == orderInitial