from fastapi import FastAPI
from app.api.vector import router as vector_router
from app.grpc_server.server import serve
from app.grpc_server.vector_service import VectorSearchServicer

app = FastAPI()

app.include_router(vector_router, prefix="/v1")

if __name__ == '__main__':
    serve()