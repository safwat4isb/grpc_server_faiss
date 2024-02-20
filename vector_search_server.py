import grpc
from concurrent import futures
import numpy as np 
import faiss
from protobuf import vector_service_pb2,vector_service_pb2_grpc


class VectorSearchServicer(vector_service_pb2_grpc.VectorServiceServicer):
    def __init__(self):
        self.index = faiss.IndexFlatL2(512)  # Assuming 512-dimensional vectors
        self.vectors = []

    def LoadVectors(self, request, context):
        for vector_proto in request.vectors:
            vector = list(vector_proto.values)
            # print("Loaded vector:", vector)
            self.vectors.append(vector)
        self.index.add(np.array(self.vectors, dtype=np.float32))
        return vector_service_pb2.LoadResponse(message=f"{len(request.vectors)} vectors loaded successfully.")

    def SearchVector(self, request, context):
        query_vector = np.array(request.vector.values, dtype=np.float32).reshape(1, -1)
        # print("Query vector:", query_vector)
        top_k = request.top_k
        distances, indices = self.index.search(query_vector, top_k)
        results = []
        for i, (index, distance) in enumerate(zip(indices[0], distances[0])):
            results.append(vector_service_pb2.SearchResult(index=index, distance=distance))
        return vector_service_pb2.VectorResult(results=results)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vector_service_pb2_grpc.add_VectorServiceServicer_to_server(VectorSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
