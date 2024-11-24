from ..entities.Order import Order

from ..interfaces.ExternalInterfaces import PaymentExternalInterface
class PaymentUseCases:
    
    @staticmethod
    def requestPayment(order: Order, paymentExternal: PaymentExternalInterface):
        try:
            payment = paymentExternal.requestPayment(order.id, order.price)
        except (E):
            raise Exception("Houve um problema ao requisitar o pagamento ao serviço de pagamento.")

    @staticmethod
    def confirmPayment():
        pass