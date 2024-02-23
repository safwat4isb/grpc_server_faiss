from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.grpc_client.client import stub
from app.grpc_client.vector_service_pb2 import Vector, VectorQuery
from app.grpc_client.vector_service_pb2_grpc import VectorServiceStub

import grpc

router = APIRouter()

@router.post("/insert/")
async def insert_vector(vector_values: List[float]):
    
    vector = Vector(values=vector_values)
    response = stub.InsertVector(vector)
    return {"message": response.message}

@router.post("/search/")
async def search_vector(query_vector_values: List[float], top_k: int = 5):
    query_vector = Vector(values=query_vector_values)
    request = VectorQuery(vector=query_vector, top_k=top_k)
    try:
        response = stub.SearchVector(request)
        results = [{"index": result.index, "distance": result.distance} for result in response.results]
        return {"results": results}
    except grpc.RpcError as rpc_error:
        raise HTTPException(status_code=500, detail=f"Error occurred during SearchVector RPC: {rpc_error}")
