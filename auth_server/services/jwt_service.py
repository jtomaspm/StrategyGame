import random
import string
import jwt

from ..models.payload_data import PayloadData

def get_jwt_token(payload : PayloadData, secret : str) -> str:
    return jwt.encode(payload.__dict__, secret)
    
def decode_jwt_token(token : str, secret : str) -> PayloadData: 
    header_data = jwt.get_unverified_header(token)
    return PayloadData(**jwt.decode(
        token,
        secret,
        algorithms=[header_data["alg"]]))

def get_refresh_token() -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=20))