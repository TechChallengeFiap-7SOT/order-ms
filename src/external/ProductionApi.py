from ..interfaces.ExternalInterfaces import ProductionExternalInterface
from ..DTO.OrderDTO import OrderDTO

class ProductionApi(ProductionExternalInterface):
    
    def __init__(self):
        super().__init__()
    
    def requestProductionAPi(self, orderDTO: OrderDTO):
        print("Chamando microserviço de produção de pedido...")
        return True