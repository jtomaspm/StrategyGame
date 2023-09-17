from ..dal.models.user import User
from ..dal.database_context import DatabaseContext
from ..settings import DATABASE_URL
from ..models.login_model import LoginModel
from ..models.register_model import RegisterModel


def login(credentials: LoginModel):
    return {"status": "Logged in"}

def register(credentials: RegisterModel):
    with DatabaseContext(DATABASE_URL) as db_context:
        record = User()
        record.email = credentials.email
        db_record = db_context.get(record)
        if db_record:
            return {"status": "Username already taken"}
        else:
            record.name = credentials.name
            record.email = None
            db_record = db_context.get(record)
            if db_record:
                return {"status": "Email already taken"}
            else:
                db_context.add(record)
                db_context.commit()
    return {"status": "Registered"}