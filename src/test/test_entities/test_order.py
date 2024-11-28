from ...entities.Order import Order
import uuid

def test_create_order():
    orderId = str(uuid.uuid4())
    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    orderStatus = 1
    price = 50

    order = Order(orderId, 
                itens, 
                orderStatus,
                price)
    
    assert order.id == orderId
    assert order.itens == itens
    assert order.status == orderStatus
    assert order.price == price