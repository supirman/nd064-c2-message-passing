# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location_ingest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='location_ingest.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15location_ingest.proto\"f\n\x15LocationIngestMessage\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x15\n\rcreation_time\x18\x04 \x01(\t2J\n\x0eLocationIngest\x12\x38\n\x06\x43reate\x12\x16.LocationIngestMessage\x1a\x16.LocationIngestMessageb\x06proto3'
)




_LOCATIONINGESTMESSAGE = _descriptor.Descriptor(
  name='LocationIngestMessage',
  full_name='LocationIngestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='LocationIngestMessage.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='LocationIngestMessage.longitude', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='LocationIngestMessage.latitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='LocationIngestMessage.creation_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=25,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['LocationIngestMessage'] = _LOCATIONINGESTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationIngestMessage = _reflection.GeneratedProtocolMessageType('LocationIngestMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONINGESTMESSAGE,
  '__module__' : 'location_ingest_pb2'
  # @@protoc_insertion_point(class_scope:LocationIngestMessage)
  })
_sym_db.RegisterMessage(LocationIngestMessage)



_LOCATIONINGEST = _descriptor.ServiceDescriptor(
  name='LocationIngest',
  full_name='LocationIngest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=129,
  serialized_end=203,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='LocationIngest.Create',
    index=0,
    containing_service=None,
    input_type=_LOCATIONINGESTMESSAGE,
    output_type=_LOCATIONINGESTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONINGEST)

DESCRIPTOR.services_by_name['LocationIngest'] = _LOCATIONINGEST

# @@protoc_insertion_point(module_scope)
