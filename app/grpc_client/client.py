import grpc
from app.grpc_client.vector_service_pb2_grpc import VectorServiceStub

# Connect to gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = VectorServiceStub(channel)