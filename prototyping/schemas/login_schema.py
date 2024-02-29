from ninja import Schema

class AuthSchema(Schema):
    email: str
    password: str
