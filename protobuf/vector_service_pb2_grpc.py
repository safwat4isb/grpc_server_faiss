# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vector import vector_service_pb2 as vector_dot_vector__service__pb2


class VectorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadVectors = channel.unary_unary(
                '/vectorsearch.VectorService/LoadVectors',
                request_serializer=vector_dot_vector__service__pb2.VectorBatch.SerializeToString,
                response_deserializer=vector_dot_vector__service__pb2.LoadResponse.FromString,
                )
        self.SearchVector = channel.unary_unary(
                '/vectorsearch.VectorService/SearchVector',
                request_serializer=vector_dot_vector__service__pb2.VectorQuery.SerializeToString,
                response_deserializer=vector_dot_vector__service__pb2.VectorResult.FromString,
                )


class VectorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LoadVectors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchVector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadVectors': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadVectors,
                    request_deserializer=vector_dot_vector__service__pb2.VectorBatch.FromString,
                    response_serializer=vector_dot_vector__service__pb2.LoadResponse.SerializeToString,
            ),
            'SearchVector': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchVector,
                    request_deserializer=vector_dot_vector__service__pb2.VectorQuery.FromString,
                    response_serializer=vector_dot_vector__service__pb2.VectorResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vectorsearch.VectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VectorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LoadVectors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vectorsearch.VectorService/LoadVectors',
            vector_dot_vector__service__pb2.VectorBatch.SerializeToString,
            vector_dot_vector__service__pb2.LoadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchVector(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vectorsearch.VectorService/SearchVector',
            vector_dot_vector__service__pb2.VectorQuery.SerializeToString,
            vector_dot_vector__service__pb2.VectorResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
