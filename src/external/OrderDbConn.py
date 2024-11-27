from ..interfaces.ExternalInterfaces import OrderExternalInterface
from ..DTO.OrderDTO import OrderDTO

import sqlite3

from typing import List, Optional
import json

class OrderDbConnector(OrderExternalInterface):
    
    def __init__(self):
        super().__init__()
    
    def create(self, orderDTO: OrderDTO) -> Optional[OrderDTO]:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Orders (id, items, status, price) VALUES (?, ?, ?, ?)",
            (orderDTO.id, json.dumps(orderDTO.itens), orderDTO.status, orderDTO.price)
        )
        conn.commit()
        conn.close()

        return orderDTO
    
    def get(self, orderID: str) -> Optional[OrderDTO]:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Orders WHERE id = ?", (orderID,))
        row = cursor.fetchone()
        conn.close()

        if row:
            order = OrderDTO(row[0],
                             json.loads(row[1]),
                             row[2],
                             row[3])
            return order
        else:
            return None  # Retorna None se o pedido não for encontrado
    
    
    def Delete(self, orderID: str) -> Optional[int]:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Orders WHERE id = ?", (orderID,))
        conn.commit()
        conn.close()

        return True
    
    
    def Change(self, orderID: str, orderStatus: int) -> Optional[OrderDTO]:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        
        # Verificar se o pedido existe
        cursor.execute("SELECT * FROM Orders WHERE id = ?", (orderID,))
        row = cursor.fetchone()
        
        if row:
            # Alterar o status
            cursor.execute("UPDATE Orders SET status = ? WHERE id = ?", (orderStatus, orderID))
            conn.commit()

            # Retornar a ordem atualizada
            order = OrderDTO(row[0],
                             json.loads(row[1]),
                             row[2],
                             row[3])
            conn.close()
            return order
        else:
            conn.close()
            return None  # Se o pedido não existir
        
        