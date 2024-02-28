from ninja import Schema

class ClienteIn(Schema):
    name: str
    email: str
    address: str
    telephone: str

class ClienteOut(Schema):
    id: int
    name: str
    email: str
    address: str
    telephone: str
