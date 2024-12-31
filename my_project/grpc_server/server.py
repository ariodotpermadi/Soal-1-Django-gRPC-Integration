import grpc
from concurrent import futures
from grpc_server.protos import user_pb2_grpc
from grpc_server.services import UserService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
