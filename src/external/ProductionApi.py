from ..interfaces.ExternalInterfaces import ProductionExternalInterface
from ..DTO.OrderDTO import OrderDTO

import requests

from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()



class ProductionApi(ProductionExternalInterface):
    
    def __init__(self):
        super().__init__()
        self._productionApiUrl = os.getenv("PRODUCTION_SERVICE_URL")
    
    def requestProductionAPi(self, orderDTO: OrderDTO):
        
        # Payload JSON
        payload = {
            "pedido_id": orderDTO.id,
            # "order_itens": orderDTO.itens,
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer seu_token_aqui"  # Token de autenticação, se necessário
        }

        try:
            # Enviando a requisição POST com o payload JSON
            response = requests.post(self._productionApiUrl, json=payload, headers=headers)

            # Verificando a resposta
            if response.status_code == 200:
                print("Requisição bem-sucedida!")
                print("Resposta:", response.json())  # Converte a resposta para JSON
                return True
            else:
                print(f"Erro na requisição. Código de status: {response.status_code}")
                print("Mensagem de erro:", response.text)
                return False

        except requests.exceptions.RequestException as e:
            print("Erro ao fazer a requisição:", e)
        
        return True