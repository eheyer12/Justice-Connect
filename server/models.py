from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
    
class Client(db.Model, SerializerMixin):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

    #Add relationship
    cases = db.relationship('Case', back_populates='client', cascade='all, delete-orphan')
    lawyers = association_proxy('cases', 'lawyer', creator=lambda l: Case(lawyer = l))

    #Add serialization
    serialize_rules = ('-cases.client',)

    #Add validation
    @validates('username')
    def validate_name(self, key, value):
        if len(value) < 8:
            raise ValueError(f"{key} must be at least 8 characters long.")
        return value

    def __repr__(self):
        return f"<Client {self.id}>"

class Lawyer(db.Model, SerializerMixin):
    __tablename__ = 'lawyers'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    
    lawfirm_id = db.Column(db.Integer, db.ForeignKey('lawfirms.id'))

    #Add relationship
    cases = db.relationship('Case', back_populates='lawyer', cascade='all, delete-orphan')
    clients = association_proxy('cases', 'client', creator=lambda c: Case(client = c))
    lawfirm = db.relationship('Lawfirm', back_populates='lawyers')

    #Add serialization
    serialize_rules = ('-cases.lawyers',)

    #Add validation

    def __repr__(self):
        return f"<Lawyer {self.id}>"
    
class Lawfirm(db.Model, SerializerMixin):
    __tablename__ = 'lawfirms'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    rank = db.Column(db.String)

    # Add relationship
    lawyers = db.relationship('Lawyer', back_populates='lawfirm', cascade='all, delete-orphan')

    # Add serialization
    serialize_rules = ('-lawyers.lawfirm',)

    # Add validation
    @validates('rank')
    def validate_rank(self, key, value):
        if value < 1:
            raise ValueError(f"{key} must be at greater than 0.")
        return value

    def __repr__(self):
        return f'<Lawfirm {self.id}>'

class Case(db.Model, SerializerMixin): 
    __tablename__ = 'cases'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyers.id'))

    #Add relationship
    client = db.relationship('Client', back_populates='cases')
    lawyer = db.relationship('Lawyer', back_populates='cases')

    #Add serialization
    serialize_rules = ('-client', '-lawyer')

    #Add validation
    
    def __repr__(self):
        return f'<Case {self.id}>'
