from grpc_server.protos import user_pb2, user_pb2_grpc
from user.models import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUsers(self, request, context):
        users = User.objects.all()
        user_list = [user_pb2.User(
            id=user.id, username=user.username, email=user.email) for user in users]
        return user_pb2.UserList(users=user_list)
