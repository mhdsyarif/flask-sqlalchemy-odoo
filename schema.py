import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Partner as PartnerModel, User as UserModel

class Partner(SQLAlchemyObjectType):
    class Meta:
        model = PartnerModel
        interfaces = (relay.Node, )


class PartnerConnection(relay.Connection):
    class Meta:
        node = Partner

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = User


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User._meta.connection)
    all_partners = SQLAlchemyConnectionField(Partner._meta.connection)

schema = graphene.Schema(query=Query)