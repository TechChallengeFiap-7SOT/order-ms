from ..controller.OrderController import OrderController
from ..DTO.OrderDTO import OrderDTO
from ..external.OrderDbConn import OrderDbConnector
from ..external.PaymentApi import PaymentApi
from ..external.ProductionApi import ProductionApi
from ..adapters.OrderAdapter import OrderAdapter

class ApiHandler():
    
    @staticmethod
    def makeOrder():
        
        order = OrderDTO(None, {"hamburger" : 1, "refrigerante" : 2}, 0, 15.67)
        
        orderDbConn = OrderDbConnector()
        paymentApi = PaymentApi("localhost:5000/webhook")
        orderAdapter = OrderAdapter()
        
        response = OrderController.makeOrder(order,orderDbConn, paymentApi, orderAdapter)
        
        # print(response)
        return response
    
    @staticmethod
    def webhookApi(orderId):
        
        orderDbConn = OrderDbConnector()
        response = OrderController.confirmOrderPayment(orderId, orderDbConn)
        
        response = OrderController.requestOrderProduction(orderId, orderDbConn, ProductionApi)
        
        return response