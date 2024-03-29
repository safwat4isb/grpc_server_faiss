# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/vector_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprotobuf/vector_service.proto\x12\x0cvectorsearch\"\x18\n\x06Vector\x12\x0e\n\x06values\x18\x01 \x03(\x02\"4\n\x0bVectorBatch\x12%\n\x07vectors\x18\x01 \x03(\x0b\x32\x14.vectorsearch.Vector\"\x1f\n\x0cLoadResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"B\n\x0bVectorQuery\x12$\n\x06vector\x18\x01 \x01(\x0b\x32\x14.vectorsearch.Vector\x12\r\n\x05top_k\x18\x02 \x01(\x05\"/\n\x0cSearchResult\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\";\n\x0cVectorResult\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.vectorsearch.SearchResult\"!\n\x0eInsertResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xe4\x01\n\rVectorService\x12\x46\n\x0bLoadVectors\x12\x19.vectorsearch.VectorBatch\x1a\x1a.vectorsearch.LoadResponse\"\x00\x12G\n\x0cSearchVector\x12\x19.vectorsearch.VectorQuery\x1a\x1a.vectorsearch.VectorResult\"\x00\x12\x42\n\x0cInsertVector\x12\x14.vectorsearch.Vector\x1a\x1c.vectorsearch.InsertResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.vector_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VECTOR']._serialized_start=47
  _globals['_VECTOR']._serialized_end=71
  _globals['_VECTORBATCH']._serialized_start=73
  _globals['_VECTORBATCH']._serialized_end=125
  _globals['_LOADRESPONSE']._serialized_start=127
  _globals['_LOADRESPONSE']._serialized_end=158
  _globals['_VECTORQUERY']._serialized_start=160
  _globals['_VECTORQUERY']._serialized_end=226
  _globals['_SEARCHRESULT']._serialized_start=228
  _globals['_SEARCHRESULT']._serialized_end=275
  _globals['_VECTORRESULT']._serialized_start=277
  _globals['_VECTORRESULT']._serialized_end=336
  _globals['_INSERTRESPONSE']._serialized_start=338
  _globals['_INSERTRESPONSE']._serialized_end=371
  _globals['_VECTORSERVICE']._serialized_start=374
  _globals['_VECTORSERVICE']._serialized_end=602
# @@protoc_insertion_point(module_scope)
