# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vector_tile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vector_tile.proto',
  package='vector_tile',
  serialized_pb=_b('\n\x11vector_tile.proto\x12\x0bvector_tile\"\xa4\x05\n\x04Tile\x12\'\n\x06layers\x18\x03 \x03(\x0b\x32\x17.vector_tile.Tile.Layer\x1a\xd1\x01\n\x05Value\x12\x14\n\x0cstring_value\x18\x01 \x01(\t\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x02\x12\x14\n\x0c\x64ouble_value\x18\x03 \x01(\x01\x12\x11\n\tint_value\x18\x04 \x01(\x03\x12\x12\n\nuint_value\x18\x05 \x01(\x04\x12\x12\n\nsint_value\x18\x06 \x01(\x12\x12\x12\n\nbool_value\x18\x07 \x01(\x08\x12\x16\n\nhash_value\x18\x08 \x03(\rB\x02\x10\x01\x12\x16\n\nlist_value\x18\t \x03(\rB\x02\x10\x01*\x08\x08\n\x10\x80\x80\x80\x80\x02\x1a\x86\x01\n\x07\x46\x65\x61ture\x12\r\n\x02id\x18\x01 \x01(\x04:\x01\x30\x12\x10\n\x04tags\x18\x02 \x03(\rB\x02\x10\x01\x12\x31\n\x04type\x18\x03 \x01(\x0e\x32\x1a.vector_tile.Tile.GeomType:\x07UNKNOWN\x12\x14\n\x08geometry\x18\x04 \x03(\rB\x02\x10\x01\x12\x11\n\x05knots\x18\x05 \x03(\x01\x42\x02\x10\x01\x1a\xc1\x01\n\x05Layer\x12\x12\n\x07version\x18\x0f \x02(\r:\x01\x31\x12\x0c\n\x04name\x18\x01 \x02(\t\x12+\n\x08\x66\x65\x61tures\x18\x02 \x03(\x0b\x32\x19.vector_tile.Tile.Feature\x12\x0c\n\x04keys\x18\x03 \x03(\t\x12\'\n\x06values\x18\x04 \x03(\x0b\x32\x17.vector_tile.Tile.Value\x12\x14\n\x06\x65xtent\x18\x05 \x01(\r:\x04\x34\x30\x39\x36\x12\x12\n\ndimensions\x18\x06 \x01(\r*\x08\x08\x10\x10\x80\x80\x80\x80\x02\"K\n\x08GeomType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05POINT\x10\x01\x12\x0e\n\nLINESTRING\x10\x02\x12\x0b\n\x07POLYGON\x10\x03\x12\n\n\x06SPLINE\x10\x04*\x05\x08\x10\x10\x80@B\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TILE_GEOMTYPE = _descriptor.EnumDescriptor(
  name='GeomType',
  full_name='vector_tile.Tile.GeomType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POINT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINESTRING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLYGON', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLINE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=629,
  serialized_end=704,
)
_sym_db.RegisterEnumDescriptor(_TILE_GEOMTYPE)


_TILE_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='vector_tile.Tile.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_value', full_name='vector_tile.Tile.Value.string_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='vector_tile.Tile.Value.float_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='vector_tile.Tile.Value.double_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='vector_tile.Tile.Value.int_value', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint_value', full_name='vector_tile.Tile.Value.uint_value', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sint_value', full_name='vector_tile.Tile.Value.sint_value', index=5,
      number=6, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='vector_tile.Tile.Value.bool_value', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash_value', full_name='vector_tile.Tile.Value.hash_value', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='list_value', full_name='vector_tile.Tile.Value.list_value', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10, 536870912), ],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=294,
)

_TILE_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='vector_tile.Tile.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='vector_tile.Tile.Feature.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='vector_tile.Tile.Feature.tags', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='type', full_name='vector_tile.Tile.Feature.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='vector_tile.Tile.Feature.geometry', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='knots', full_name='vector_tile.Tile.Feature.knots', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=431,
)

_TILE_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='vector_tile.Tile.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='vector_tile.Tile.Layer.version', index=0,
      number=15, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='vector_tile.Tile.Layer.name', index=1,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='features', full_name='vector_tile.Tile.Layer.features', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='vector_tile.Tile.Layer.keys', index=3,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='vector_tile.Tile.Layer.values', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extent', full_name='vector_tile.Tile.Layer.extent', index=5,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4096,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='vector_tile.Tile.Layer.dimensions', index=6,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(16, 536870912), ],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=627,
)

_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='vector_tile.Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layers', full_name='vector_tile.Tile.layers', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TILE_VALUE, _TILE_FEATURE, _TILE_LAYER, ],
  enum_types=[
    _TILE_GEOMTYPE,
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(16, 8192), ],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=711,
)

_TILE_VALUE.containing_type = _TILE
_TILE_FEATURE.fields_by_name['type'].enum_type = _TILE_GEOMTYPE
_TILE_FEATURE.containing_type = _TILE
_TILE_LAYER.fields_by_name['features'].message_type = _TILE_FEATURE
_TILE_LAYER.fields_by_name['values'].message_type = _TILE_VALUE
_TILE_LAYER.containing_type = _TILE
_TILE.fields_by_name['layers'].message_type = _TILE_LAYER
_TILE_GEOMTYPE.containing_type = _TILE
DESCRIPTOR.message_types_by_name['Tile'] = _TILE

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), dict(

  Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
    DESCRIPTOR = _TILE_VALUE,
    __module__ = 'vector_tile_pb2'
    # @@protoc_insertion_point(class_scope:vector_tile.Tile.Value)
    ))
  ,

  Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
    DESCRIPTOR = _TILE_FEATURE,
    __module__ = 'vector_tile_pb2'
    # @@protoc_insertion_point(class_scope:vector_tile.Tile.Feature)
    ))
  ,

  Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), dict(
    DESCRIPTOR = _TILE_LAYER,
    __module__ = 'vector_tile_pb2'
    # @@protoc_insertion_point(class_scope:vector_tile.Tile.Layer)
    ))
  ,
  DESCRIPTOR = _TILE,
  __module__ = 'vector_tile_pb2'
  # @@protoc_insertion_point(class_scope:vector_tile.Tile)
  ))
_sym_db.RegisterMessage(Tile)
_sym_db.RegisterMessage(Tile.Value)
_sym_db.RegisterMessage(Tile.Feature)
_sym_db.RegisterMessage(Tile.Layer)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_TILE_VALUE.fields_by_name['hash_value'].has_options = True
_TILE_VALUE.fields_by_name['hash_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_TILE_VALUE.fields_by_name['list_value'].has_options = True
_TILE_VALUE.fields_by_name['list_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_TILE_FEATURE.fields_by_name['tags'].has_options = True
_TILE_FEATURE.fields_by_name['tags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_TILE_FEATURE.fields_by_name['geometry'].has_options = True
_TILE_FEATURE.fields_by_name['geometry']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_TILE_FEATURE.fields_by_name['knots'].has_options = True
_TILE_FEATURE.fields_by_name['knots']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
