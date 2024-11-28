from ..controller.OrderController import OrderController
from ..DTO.OrderDTO import OrderDTO
from ..external.OrderDbConn import OrderDbConnector
from ..external.PaymentApi import PaymentApi
from ..external.ProductionApi import ProductionApi
from ..adapters.OrderAdapter import OrderAdapter

from flask import Flask, jsonify, request


# Cria a aplicação Flask
app = Flask(__name__)

class ApiHandler():
    
    @staticmethod
    @app.route('/order', methods=['POST'])
    def makeOrder():
        
        data = request.get_json()

        # Validar se todos os campos necessários estão presentes
        if not data or 'order_itens' not in data or 'order_price' not in data:
            return jsonify({"error": "Invalid request, missing 'order_itens' or 'order_price'"}), 400
        
        order_items = data['order_itens']
        order_price = data['order_price']
        
        order = OrderDTO(None, order_items, 0, order_price)
        
        orderDbConn = OrderDbConnector()
        paymentApi = PaymentApi("localhost:5000/webhook")
        orderAdapter = OrderAdapter()
        
        response = OrderController.makeOrder(order,orderDbConn, paymentApi, orderAdapter)
        
        # print(response)
        return jsonify(response)
    
    @staticmethod
    @app.route('/order/<orderId>', methods=['GET'])
    def getOrder(orderId):
        orderDbConn = OrderDbConnector()
        orderAdapter = OrderAdapter()
        
        response = OrderController.getOrder(orderId, orderDbConn, orderAdapter)
        
        return response
    
        
    @staticmethod
    @app.route('/webhook/<orderId>', methods=['GET'])
    def webhookApi(orderId):
        
        orderDbConn = OrderDbConnector()
        response = OrderController.confirmOrderPayment(orderId, orderDbConn)
        
        productionApi = ProductionApi()
        response = OrderController.requestOrderProduction(orderId, orderDbConn, productionApi)
        
        return response