import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from ..models import User as UserModel
from ..graphql.object import UserObject as User
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = graphene.List(
    lambda: User, complete=graphene.Boolean(), user_id=graphene.Int(),title=graphene.String(),time=graphene.Date())
    def resolve_users(self, info, complete=None):
        query = User.get_query(info)
        if complete:
           query = query.filter(UserModel.complete == complete)
        elif complete==False:
           query=query.filter(UserModel.complete == complete)
        return query.all()

    all_users = SQLAlchemyConnectionField(User.connection)
