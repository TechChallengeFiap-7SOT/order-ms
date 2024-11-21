class Order:
    def __init__(self,id : int, itens : dict, status: int, price: int):
        self._id = id
        self._itens = itens
        self._status = status
        self._price = price
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def itens(self) -> dict:
        return self._itens
    
    @property
    def status(self) -> int:
        return self._status
    
    @status.setter
    def status(self, status) -> int:
        self._status = status
        
    @property
    def price(self) -> int:
        return self._price
        
        