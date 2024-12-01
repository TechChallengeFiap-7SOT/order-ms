from ..entities.Order import Order
from ..usecases.OrderUseCases import OrderUseCases
from ..interfaces.GatewaysInterfaces import PaymentGatewayInterface

class PaymentUseCases:
    
    @staticmethod
    def requestPayment(order: Order, paymentGateway: PaymentGatewayInterface):
        if order.price <= 0:
            raise Exception("O preço da order não por ser menor ou igual a 0.")

        # try:
        status = paymentGateway.requestPayment(order.id, order.price)
        # except:
        #     raise Exception("Houve um problema ao requisitar o pagamento ao serviço de pagamento.")
        
        return status

    @staticmethod
    def confirmPayment():
        pass