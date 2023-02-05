import graphene
from backend.__init import db
from ..graphql.object import UserObject as User
from ..models import User as UserModel

class UserMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        time=graphene.Date()
        complete=graphene.Boolean()
        id=graphene.Int()
        

    user = graphene.Field(lambda: User)

    def mutate(self, info, complete,title):
       user = UserModel(complete=complete,title=title)

       db.session.add(user)
       db.session.commit()

       return UserMutation(user=user)
class Mutation(graphene.ObjectType):
   mutate_user = UserMutation.Field()