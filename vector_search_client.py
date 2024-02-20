import grpc
from protobuf import vector_service_pb2,vector_service_pb2_grpc
import random

def load_vectors(stub):
    vectors = [] 
    # Populate vectors with placeholder data
    for i in range(10):  # Load 10 vectors for example
        # Generate random values for each vector
        vector_values = [random.uniform(0.0, 1.0) for _ in range(512)]  # Random values between 0 and 1 for each dimension
        vector = vector_service_pb2.Vector(values=vector_values)
        print("Sending vector to load:", vector_values)
        vectors.append(vector)
    response = stub.LoadVectors(vector_service_pb2.VectorBatch(vectors=vectors))
    print("LoadVectors response:", response.message)


     
def search_vector(stub):
    # Generate a random query vector
    query_vector_values = [random.uniform(0.0, 1.0) for _ in range(512)]  # Random values between 0 and 1 for each dimension
    query_vector = vector_service_pb2.Vector(values=query_vector_values)
    print("Sending query vector:", query_vector_values)
    request = vector_service_pb2.VectorQuery(vector=query_vector, top_k=5)  # Search top 5 nearest neighbors
    try:
        response = stub.SearchVector(request)
        print("SearchVector response:")
        for result in response.results:
            print("Index:", result.index, "Distance:", result.distance)
    except grpc.RpcError as rpc_error:
        print(f"Error occurred during SearchVector RPC: {rpc_error}")

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = vector_service_pb2_grpc.VectorServiceStub(channel)
    load_vectors(stub)
    search_vector(stub)

if __name__ == '__main__':
    run()