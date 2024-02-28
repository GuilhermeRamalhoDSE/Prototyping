from ninja import Schema

class ClientIn(Schema):
    name: str
    email: str
    address: str
    phone: str

class ClientOut(Schema):
    id: int
    name: str
    email: str
    address: str
    phone: str
