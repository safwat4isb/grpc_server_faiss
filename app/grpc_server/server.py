import grpc
from concurrent import futures
from app.grpc_client import vector_service_pb2,vector_service_pb2_grpc
from app.grpc_server.vector_service import VectorSearchServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vector_service_pb2_grpc.add_VectorServiceServicer_to_server(VectorSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()