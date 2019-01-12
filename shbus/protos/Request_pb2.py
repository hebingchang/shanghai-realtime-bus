# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Request.proto',
  package='protoc.Request',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rRequest.proto\x12\x0eprotoc.Request\x1a\x19google/protobuf/any.proto\".\n\x07Request\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"K\n\x08Sequence\x12\x11\n\tdirection\x18\x03 \x01(\x08\x12\x0c\n\x04info\x18\x01 \x01(\x08\x12\x0c\n\x04line\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x04 \x01(\rb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='protoc.Request.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='protoc.Request.Request.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=106,
)


_SEQUENCE = _descriptor.Descriptor(
  name='Sequence',
  full_name='protoc.Request.Sequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direction', full_name='protoc.Request.Sequence.direction', index=0,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='protoc.Request.Sequence.info', index=1,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='protoc.Request.Sequence.line', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='protoc.Request.Sequence.sequence', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=183,
)

_REQUEST.fields_by_name['items'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Sequence'] = _SEQUENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Request_pb2'
  # @@protoc_insertion_point(class_scope:protoc.Request.Request)
  ))
_sym_db.RegisterMessage(Request)

Sequence = _reflection.GeneratedProtocolMessageType('Sequence', (_message.Message,), dict(
  DESCRIPTOR = _SEQUENCE,
  __module__ = 'Request_pb2'
  # @@protoc_insertion_point(class_scope:protoc.Request.Sequence)
  ))
_sym_db.RegisterMessage(Sequence)


# @@protoc_insertion_point(module_scope)
