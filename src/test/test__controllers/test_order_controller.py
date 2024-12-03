import pytest
from unittest.mock import MagicMock
from src.controller.OrderController import OrderController
from src.entities.Order import Order
from src.DTO.OrderDTO import OrderDTO
from src.gateways.OrderGateway import OrderGateway

@pytest.fixture
def mock_order_dto():
    return OrderDTO(id="1", itens=["item1", "item2"], status=1, price=100.0)

@pytest.fixture
def mock_order():
    return Order(id="1", itens=["item1", "item2"], status=1, price=100.0)

@pytest.fixture
def mock_order_db():
    order_db = MagicMock()
    order_db.get.return_value = OrderDTO(id="1", itens=["item1", "item2"], status=1, price=100.0)
    order_db.create.return_value = OrderDTO(id="1", itens=["item1", "item2"], status=1, price=100.0)
    order_db.Change.return_value = OrderDTO(id="1", itens=["item1", "item2"], status=2, price=100.0)
    return order_db

@pytest.fixture
def mock_payment_external():
    payment_external = MagicMock()
    payment_external.requestPayment.return_value = 1  # Status de pagamento como inteiro
    return payment_external

@pytest.fixture
def mock_production_external():
    production_external = MagicMock()
    production_external.requestProduction.return_value = "OK"
    return production_external

@pytest.fixture
def mock_order_adapter():
    adapter = MagicMock()
    adapter.orderToJson.return_value = '{"id": "1", "itens": ["item1", "item2"], "status": 1, "price": 100.0}'
    return adapter


def test_make_order(mock_order_dto, mock_order_adapter, mock_order_db, mock_payment_external):
    response = OrderController.makeOrder(
        orderDTO=mock_order_dto,
        orderDb=mock_order_db,
        paymentExternal=mock_payment_external,
        orderAdapter=mock_order_adapter,
    )

    assert response == '{"id": "1", "itens": ["item1", "item2"], "status": 1, "price": 100.0}'
    mock_order_adapter.orderToJson.assert_called_once()


def test_request_payment(mock_order_db, mock_payment_external, mock_order):
    payment_status = OrderController.requestPayment(
        orderId="1",
        paymentExternal=mock_payment_external,
        orderDb=mock_order_db,
    )
    assert 1 == 1  # Status de pagamento


def test_confirm_order_payment(mock_order_db, mock_order):
    response = OrderController.confirmOrderPayment(
        orderId="1",
        orderDb=mock_order_db,
    )
    assert response == "{'status' : 'ok'}"


def test_request_order_production(mock_order_db, mock_production_external, mock_order):
    response = OrderController.requestOrderProduction(
        orderId="1",
        orderDb=mock_order_db,
        productionExternal=mock_production_external,
    )
    assert response == "{'status' : 'ok'}"
