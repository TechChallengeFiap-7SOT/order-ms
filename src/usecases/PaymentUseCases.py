from ..entities.Order import Order
from ..usecases.OrderUseCases import OrderUseCases
from ..interfaces.GatewaysInterfaces import PaymentGatewayInterface

class PaymentUseCases:
    
    @staticmethod
    def requestPayment(order: Order, paymentGateway: PaymentGatewayInterface):
        # try:
        status = paymentGateway.requestPayment(order.id, order.price)
        # except:
        #     raise Exception("Houve um problema ao requisitar o pagamento ao serviço de pagamento.")
        
        return status

    @staticmethod
    def confirmPayment():
        pass