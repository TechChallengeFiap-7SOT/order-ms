from ..interfaces.ExternalInterfaces import PaymentExternalInterface
from ..DTO.OrderDTO import OrderDTO

import requests

from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()



class PaymentApi(PaymentExternalInterface):
    
    def __init__(self, webhookUrl):
        super().__init__()
        self._webhookUrl = webhookUrl
        self._paymentApiUrl = os.getenv("PAYMENT_SERVICE_URL")
        
    def request(self, id, price):
        # print("Fazendo requisição para pagamento...")
        # print("Webhook gerada: {}/{}/confirm".format(self._webhookUrl, id))
        
        # Payload JSON
        payload = {
            "id_pedido" : id,
            "valor": price,
            "urlCallback" : "{}/{}".format(self._webhookUrl, id)
        }
        print(payload["urlCallback"])
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer seu_token_aqui"  # Token de autenticação, se necessário
        }

        try:
            # Enviando a requisição POST com o payload JSON
            response = requests.post(self._paymentApiUrl, json=payload, headers=headers)

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