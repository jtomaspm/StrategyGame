
from sqlmodel import SQLModel, Session, create_engine


class DatabaseContext:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(database_url)

    def apply_migrations(self):
        SQLModel.metadata.create_all(self.engine)

    def __enter__(self):
        self.session = Session(self.engine)
        return self

    def commit(self):
        if self.transaction:
            self.transaction.commit()
        self.session.commit()

    def rollback(self):
        self.session.rollback()
        
    def add(self, model: SQLModel):
        self.session.add(model)
        
    def delete(self, model: SQLModel):
        self.session.delete(model)
    
    def get(self, model: SQLModel):
        return self.session.get(model)
    
    def query(self, model: SQLModel):
        return self.session.query(model)

    def begin_transaction(self):
        self.transaction = self.session.begin()
        return self.transaction

    def end_transaction(self):
        self.transaction.close()
        self.transaction = None

    def commit_transaction(self):
        self.transaction.commit()

    def __exit__(self, *args):
        self.transaction.close()
        self.session.close()