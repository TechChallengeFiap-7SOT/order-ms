from src.adapters.OrderAdapter import OrderAdapter
from src.DTO.OrderDTO import OrderDTO

def test_order_adapter():
    adapter = OrderAdapter()
    
    itens = {"hamburger" : 1, "batata frita" : 2, "refrigerante" : 3}
    price = 50
    
    order = OrderDTO("123ABC", itens, 0, price)
    
    orderJson = adapter.orderToJson(order)
    
    assert type(orderJson) == dict
    assert orderJson["order_id"] == "123ABC"
    assert orderJson["order_itens"] == itens
    assert orderJson["order_status"] == 0
    assert orderJson["order_price"] == price

    