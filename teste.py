from dataclasses import dataclass

@dataclass
class ItemDto:
    name: str
    location: str
    description: str = ""

x = ItemDto("Teste", "Av. 123")
y = ItemDto("Teste", "Av. 123")

print(x == y)