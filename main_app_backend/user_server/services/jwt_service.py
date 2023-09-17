import jwt

from ..models.payload_data import PayloadData

    
def decode_jwt_token(token : str, secret : str) -> PayloadData: 
    header_data = jwt.get_unverified_header(token)
    return PayloadData(**jwt.decode(
        token,
        secret,
        algorithms=[header_data["alg"]]))