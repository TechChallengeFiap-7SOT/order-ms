import pytest
import sqlite3
import json
from src.external.OrderDbConn import OrderDbConnector
from src.DTO.OrderDTO import OrderDTO
from unittest.mock import patch


@pytest.fixture
def setup_database():
    # Configura o banco de dados em memória e cria a tabela Orders
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Orders (
            id TEXT PRIMARY KEY,
            items TEXT,
            status INTEGER,
            price REAL
        )
    """)
    conn.commit()
    conn.close()


@pytest.fixture
def order_db_connector(monkeypatch, setup_database):
    # Mock do caminho do banco de dados para usar :memory:
    monkeypatch.setenv('DATABASE_URL', ':memory:')
    return OrderDbConnector()


@pytest.fixture
def sample_order():
    return OrderDTO(
        id="order123",
        itens=["item1", "item2"],
        status=1,
        price=99.99
    )


def test_create_order(order_db_connector, sample_order):
    with patch("sqlite3.connect") as mock_connect:
        # Mock da conexão
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Executa o método de criação
        created_order = order_db_connector.create(sample_order)

        # Verifica se o método foi chamado com os argumentos corretos
        mock_cursor.execute.assert_called_with(
            "INSERT INTO Orders (id, items, status, price) VALUES (?, ?, ?, ?)",
            (sample_order.id, json.dumps(sample_order.itens), sample_order.status, sample_order.price)
        )
        mock_conn.commit.assert_called_once()
        assert created_order == sample_order


def test_get_order(order_db_connector, sample_order):
    with patch("sqlite3.connect") as mock_connect:
        # Mock da conexão
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = (
            sample_order.id,
            json.dumps(sample_order.itens),
            sample_order.status,
            sample_order.price
        )

        # Executa o método de busca
        retrieved_order = order_db_connector.get(sample_order.id)

        # Verifica se o método foi chamado corretamente
        mock_cursor.execute.assert_called_with(
            "SELECT * FROM Orders WHERE id = ?", (sample_order.id,)
        )
        assert retrieved_order.id == sample_order.id
        assert retrieved_order.itens == sample_order.itens
        assert retrieved_order.status == sample_order.status
        assert retrieved_order.price == sample_order.price


def test_delete_order(order_db_connector, sample_order):
    with patch("sqlite3.connect") as mock_connect:
        # Mock da conexão
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Executa o método de exclusão
        result = order_db_connector.Delete(sample_order.id)

        # Verifica se o método foi chamado corretamente
        mock_cursor.execute.assert_called_with(
            "DELETE FROM Orders WHERE id = ?", (sample_order.id,)
        )
        mock_conn.commit.assert_called_once()
        assert result is True


def test_change_order_status(order_db_connector, sample_order):
    with patch("sqlite3.connect") as mock_connect:
        # Mock da conexão
        mock_conn = mock_connect.return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = (
            sample_order.id,
            json.dumps(sample_order.itens),
            sample_order.status,
            sample_order.price
        )

        # Executa o método de alteração
        updated_order = order_db_connector.Change(sample_order.id, 2)

        # Verifica se o método foi chamado corretamente
        mock_cursor.execute.assert_any_call(
            "SELECT * FROM Orders WHERE id = ?", (sample_order.id,)
        )
        mock_cursor.execute.assert_any_call(
            "UPDATE Orders SET status = ? WHERE id = ?", (2, sample_order.id)
        )
        mock_conn.commit.assert_called_once()
        assert updated_order.status == 1
