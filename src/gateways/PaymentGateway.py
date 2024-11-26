from ..interfaces.GatewaysInterfaces import PaymentGatewayInterface
from ..interfaces.ExternalInterfaces import PaymentExternalInterface

class PaymentGateway(PaymentGatewayInterface):
    def __init__(self, payment: PaymentExternalInterface):
        super().__init__()
        self._payment = payment
        
    def requestPayment(self, id: int, price: int):
         status = self._payment.request(id, price)
         return
        