from abc import ABC, abstractmethod

class CRUDSession(ABC):
    def __init__(self):
        self.db = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.close()

    @abstractmethod
    async def close(self):
        pass
    

    
