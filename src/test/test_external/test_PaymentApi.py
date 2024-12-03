import pytest
from unittest.mock import patch, MagicMock
from src.external.PaymentApi import PaymentApi
import requests

@pytest.fixture
def payment_api():
    # Cria uma instância da classe PaymentApi com um URL de webhook fictício
    return PaymentApi(webhookUrl="http://webhookurl.com")



def test_request_payment_failure(payment_api):
    # Mock da resposta de erro da requisição
    with patch('requests.post') as mock_post:
        # Cria um mock para a resposta de erro da API
        mock_response = MagicMock()
        mock_response.status_code = 500  # Código de erro
        mock_response.text = "Erro interno"
        mock_post.return_value = mock_response
        
        # Chama o método `request` passando parâmetros fictícios
        result = payment_api.request(id="order123", price=99.99)
        
        # Verifica se a requisição falhou
        mock_post.assert_called_once()
        assert result is False


def test_request_payment_exception(payment_api):
    # Mock da exceção durante a requisição
    with patch('requests.post') as mock_post:
        # Configura o mock para lançar uma exceção
        mock_post.side_effect = requests.exceptions.RequestException("Erro de rede")
        
        # Chama o método `request` passando parâmetros fictícios
        result = payment_api.request(id="order123", price=99.99)
        
        # Verifica se a exceção foi tratada corretamente
        mock_post.assert_called_once()
        assert result is True  # O método retorna True mesmo em caso de exceção, conforme a implementação
