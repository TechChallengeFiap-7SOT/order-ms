from ..interfaces.ExternalInterfaces import PaymentExternalInterface
from ..DTO.OrderDTO import OrderDTO

class PaymentApi(PaymentExternalInterface):
    
    def __init__(self, webhookUrl):
        super().__init__()
        self._webhookUrl = webhookUrl
        
    def request(self, id, price):
        print("Fazendo requisição para pagamento...")
        print("Webhook gerada: {}/{}/confirm".format(self._webhookUrl, id))
        return True