from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+pg8000://postgres:postgres@localhost:5432/dev-odoo11", client_encoding='utf8')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Partner(Base):
    __tablename__ = 'res_partner'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class User(Base):
    __tablename__ = 'res_users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    partner_id = Column(Integer,ForeignKey('res_partner.id'))
    partner = relationship(
        Partner,
        backref=backref('res_partners',
                        uselist=True,
                        cascade='delete,all'))