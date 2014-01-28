/* Generated by the protocol buffer compiler.  DO NOT EDIT! */

/* Do not generate deprecated warnings for self */
#ifndef PROTOBUF_C_NO_DEPRECATED
#define PROTOBUF_C_NO_DEPRECATED
#endif

#include "rdb.pb-c.h"
void   reading__init
                     (Reading         *message)
{
  static Reading init_value = READING__INIT;
  *message = init_value;
}
size_t reading__get_packed_size
                     (const Reading *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t reading__pack
                     (const Reading *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t reading__pack_to_buffer
                     (const Reading *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
Reading *
       reading__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (Reading *)
     protobuf_c_message_unpack (&reading__descriptor,
                                allocator, len, data);
}
void   reading__free_unpacked
                     (Reading *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   reading_set__init
                     (ReadingSet         *message)
{
  static ReadingSet init_value = READING_SET__INIT;
  *message = init_value;
}
size_t reading_set__get_packed_size
                     (const ReadingSet *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading_set__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t reading_set__pack
                     (const ReadingSet *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading_set__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t reading_set__pack_to_buffer
                     (const ReadingSet *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading_set__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
ReadingSet *
       reading_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (ReadingSet *)
     protobuf_c_message_unpack (&reading_set__descriptor,
                                allocator, len, data);
}
void   reading_set__free_unpacked
                     (ReadingSet *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &reading_set__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   database_delta__init
                     (DatabaseDelta         *message)
{
  static DatabaseDelta init_value = DATABASE_DELTA__INIT;
  *message = init_value;
}
size_t database_delta__get_packed_size
                     (const DatabaseDelta *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_delta__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t database_delta__pack
                     (const DatabaseDelta *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_delta__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t database_delta__pack_to_buffer
                     (const DatabaseDelta *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_delta__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
DatabaseDelta *
       database_delta__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (DatabaseDelta *)
     protobuf_c_message_unpack (&database_delta__descriptor,
                                allocator, len, data);
}
void   database_delta__free_unpacked
                     (DatabaseDelta *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_delta__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   database_record__init
                     (DatabaseRecord         *message)
{
  static DatabaseRecord init_value = DATABASE_RECORD__INIT;
  *message = init_value;
}
size_t database_record__get_packed_size
                     (const DatabaseRecord *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_record__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t database_record__pack
                     (const DatabaseRecord *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_record__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t database_record__pack_to_buffer
                     (const DatabaseRecord *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_record__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
DatabaseRecord *
       database_record__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (DatabaseRecord *)
     protobuf_c_message_unpack (&database_record__descriptor,
                                allocator, len, data);
}
void   database_record__free_unpacked
                     (DatabaseRecord *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &database_record__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   query__init
                     (Query         *message)
{
  static Query init_value = QUERY__INIT;
  *message = init_value;
}
size_t query__get_packed_size
                     (const Query *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &query__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t query__pack
                     (const Query *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &query__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t query__pack_to_buffer
                     (const Query *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &query__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
Query *
       query__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (Query *)
     protobuf_c_message_unpack (&query__descriptor,
                                allocator, len, data);
}
void   query__free_unpacked
                     (Query *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &query__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   nearest__init
                     (Nearest         *message)
{
  static Nearest init_value = NEAREST__INIT;
  *message = init_value;
}
size_t nearest__get_packed_size
                     (const Nearest *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &nearest__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t nearest__pack
                     (const Nearest *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &nearest__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t nearest__pack_to_buffer
                     (const Nearest *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &nearest__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
Nearest *
       nearest__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (Nearest *)
     protobuf_c_message_unpack (&nearest__descriptor,
                                allocator, len, data);
}
void   nearest__free_unpacked
                     (Nearest *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &nearest__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   delete__init
                     (Delete         *message)
{
  static Delete init_value = DELETE__INIT;
  *message = init_value;
}
size_t delete__get_packed_size
                     (const Delete *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &delete__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t delete__pack
                     (const Delete *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &delete__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t delete__pack_to_buffer
                     (const Delete *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &delete__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
Delete *
       delete__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (Delete *)
     protobuf_c_message_unpack (&delete__descriptor,
                                allocator, len, data);
}
void   delete__free_unpacked
                     (Delete *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &delete__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
void   response__init
                     (Response         *message)
{
  static Response init_value = RESPONSE__INIT;
  *message = init_value;
}
size_t response__get_packed_size
                     (const Response *message)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &response__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t response__pack
                     (const Response *message,
                      uint8_t       *out)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &response__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t response__pack_to_buffer
                     (const Response *message,
                      ProtobufCBuffer *buffer)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &response__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
Response *
       response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (Response *)
     protobuf_c_message_unpack (&response__descriptor,
                                allocator, len, data);
}
void   response__free_unpacked
                     (Response *message,
                      ProtobufCAllocator *allocator)
{
  PROTOBUF_C_ASSERT (message->base.descriptor == &response__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
static const ProtobufCFieldDescriptor reading__field_descriptors[5] =
{
  {
    "timestamp",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Reading, timestamp),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "value",
    2,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Reading, value),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "seqno",
    3,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_UINT32,
    PROTOBUF_C_OFFSETOF(Reading, has_seqno),
    PROTOBUF_C_OFFSETOF(Reading, seqno),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "min",
    4,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_DOUBLE,
    PROTOBUF_C_OFFSETOF(Reading, has_min),
    PROTOBUF_C_OFFSETOF(Reading, min),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "max",
    5,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_DOUBLE,
    PROTOBUF_C_OFFSETOF(Reading, has_max),
    PROTOBUF_C_OFFSETOF(Reading, max),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned reading__field_indices_by_name[] = {
  4,   /* field[4] = max */
  3,   /* field[3] = min */
  2,   /* field[2] = seqno */
  0,   /* field[0] = timestamp */
  1,   /* field[1] = value */
};
static const ProtobufCIntRange reading__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 5 }
};
const ProtobufCMessageDescriptor reading__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "Reading",
  "Reading",
  "Reading",
  "",
  sizeof(Reading),
  5,
  reading__field_descriptors,
  reading__field_indices_by_name,
  1,  reading__number_ranges,
  (ProtobufCMessageInit) reading__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor reading_set__field_descriptors[3] =
{
  {
    "streamid",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(ReadingSet, streamid),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "substream",
    2,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(ReadingSet, substream),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "data",
    3,
    PROTOBUF_C_LABEL_REPEATED,
    PROTOBUF_C_TYPE_MESSAGE,
    PROTOBUF_C_OFFSETOF(ReadingSet, n_data),
    PROTOBUF_C_OFFSETOF(ReadingSet, data),
    &reading__descriptor,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned reading_set__field_indices_by_name[] = {
  2,   /* field[2] = data */
  0,   /* field[0] = streamid */
  1,   /* field[1] = substream */
};
static const ProtobufCIntRange reading_set__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 3 }
};
const ProtobufCMessageDescriptor reading_set__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "ReadingSet",
  "ReadingSet",
  "ReadingSet",
  "",
  sizeof(ReadingSet),
  3,
  reading_set__field_descriptors,
  reading_set__field_indices_by_name,
  1,  reading_set__number_ranges,
  (ProtobufCMessageInit) reading_set__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor database_delta__field_descriptors[7] =
{
  {
    "timestamp",
    1,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_INT32,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_timestamp),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, timestamp),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "value",
    2,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_INT64,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_value),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, value),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "seqno",
    3,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_INT32,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_seqno),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, seqno),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "min_delta",
    4,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_INT64,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_min_delta),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, min_delta),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "max_delta",
    5,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_INT64,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_max_delta),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, max_delta),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "min",
    6,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_DOUBLE,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_min),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, min),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "max",
    7,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_DOUBLE,
    PROTOBUF_C_OFFSETOF(DatabaseDelta, has_max),
    PROTOBUF_C_OFFSETOF(DatabaseDelta, max),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned database_delta__field_indices_by_name[] = {
  6,   /* field[6] = max */
  4,   /* field[4] = max_delta */
  5,   /* field[5] = min */
  3,   /* field[3] = min_delta */
  2,   /* field[2] = seqno */
  0,   /* field[0] = timestamp */
  1,   /* field[1] = value */
};
static const ProtobufCIntRange database_delta__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 7 }
};
const ProtobufCMessageDescriptor database_delta__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "DatabaseDelta",
  "DatabaseDelta",
  "DatabaseDelta",
  "",
  sizeof(DatabaseDelta),
  7,
  database_delta__field_descriptors,
  database_delta__field_indices_by_name,
  1,  database_delta__number_ranges,
  (ProtobufCMessageInit) database_delta__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor database_record__field_descriptors[3] =
{
  {
    "period_length",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(DatabaseRecord, period_length),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "first",
    2,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(DatabaseRecord, first),
    &reading__descriptor,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "deltas",
    3,
    PROTOBUF_C_LABEL_REPEATED,
    PROTOBUF_C_TYPE_MESSAGE,
    PROTOBUF_C_OFFSETOF(DatabaseRecord, n_deltas),
    PROTOBUF_C_OFFSETOF(DatabaseRecord, deltas),
    &database_delta__descriptor,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned database_record__field_indices_by_name[] = {
  2,   /* field[2] = deltas */
  1,   /* field[1] = first */
  0,   /* field[0] = period_length */
};
static const ProtobufCIntRange database_record__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 3 }
};
const ProtobufCMessageDescriptor database_record__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "DatabaseRecord",
  "DatabaseRecord",
  "DatabaseRecord",
  "",
  sizeof(DatabaseRecord),
  3,
  database_record__field_descriptors,
  database_record__field_indices_by_name,
  1,  database_record__number_ranges,
  (ProtobufCMessageInit) database_record__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor query__field_descriptors[5] =
{
  {
    "streamid",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Query, streamid),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "substream",
    2,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Query, substream),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "starttime",
    3,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Query, starttime),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "endtime",
    4,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Query, endtime),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "action",
    5,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_UINT32,
    PROTOBUF_C_OFFSETOF(Query, has_action),
    PROTOBUF_C_OFFSETOF(Query, action),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned query__field_indices_by_name[] = {
  4,   /* field[4] = action */
  3,   /* field[3] = endtime */
  2,   /* field[2] = starttime */
  0,   /* field[0] = streamid */
  1,   /* field[1] = substream */
};
static const ProtobufCIntRange query__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 5 }
};
const ProtobufCMessageDescriptor query__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "Query",
  "Query",
  "Query",
  "",
  sizeof(Query),
  5,
  query__field_descriptors,
  query__field_indices_by_name,
  1,  query__number_ranges,
  (ProtobufCMessageInit) query__init,
  NULL,NULL,NULL    /* reserved[123] */
};
const ProtobufCEnumValue nearest__direction__enum_values_by_number[2] =
{
  { "NEXT", "NEAREST__DIRECTION__NEXT", 1 },
  { "PREV", "NEAREST__DIRECTION__PREV", 2 },
};
static const ProtobufCIntRange nearest__direction__value_ranges[] = {
{1, 0},{0, 2}
};
const ProtobufCEnumValueIndex nearest__direction__enum_values_by_name[2] =
{
  { "NEXT", 0 },
  { "PREV", 1 },
};
const ProtobufCEnumDescriptor nearest__direction__descriptor =
{
  PROTOBUF_C_ENUM_DESCRIPTOR_MAGIC,
  "Nearest.Direction",
  "Direction",
  "Nearest__Direction",
  "",
  2,
  nearest__direction__enum_values_by_number,
  2,
  nearest__direction__enum_values_by_name,
  1,
  nearest__direction__value_ranges,
  NULL,NULL,NULL,NULL   /* reserved[1234] */
};
static const ProtobufCFieldDescriptor nearest__field_descriptors[5] =
{
  {
    "streamid",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Nearest, streamid),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "substream",
    2,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Nearest, substream),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "reference",
    3,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Nearest, reference),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "direction",
    4,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_ENUM,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Nearest, direction),
    &nearest__direction__descriptor,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "n",
    5,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_UINT32,
    PROTOBUF_C_OFFSETOF(Nearest, has_n),
    PROTOBUF_C_OFFSETOF(Nearest, n),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned nearest__field_indices_by_name[] = {
  3,   /* field[3] = direction */
  4,   /* field[4] = n */
  2,   /* field[2] = reference */
  0,   /* field[0] = streamid */
  1,   /* field[1] = substream */
};
static const ProtobufCIntRange nearest__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 5 }
};
const ProtobufCMessageDescriptor nearest__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "Nearest",
  "Nearest",
  "Nearest",
  "",
  sizeof(Nearest),
  5,
  nearest__field_descriptors,
  nearest__field_indices_by_name,
  1,  nearest__number_ranges,
  (ProtobufCMessageInit) nearest__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor delete__field_descriptors[4] =
{
  {
    "streamid",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Delete, streamid),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "substream",
    2,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Delete, substream),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "starttime",
    3,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT64,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Delete, starttime),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "endtime",
    4,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_UINT64,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Delete, endtime),
    NULL,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned delete__field_indices_by_name[] = {
  3,   /* field[3] = endtime */
  2,   /* field[2] = starttime */
  0,   /* field[0] = streamid */
  1,   /* field[1] = substream */
};
static const ProtobufCIntRange delete__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 4 }
};
const ProtobufCMessageDescriptor delete__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "Delete",
  "Delete",
  "Delete",
  "",
  sizeof(Delete),
  4,
  delete__field_descriptors,
  delete__field_indices_by_name,
  1,  delete__number_ranges,
  (ProtobufCMessageInit) delete__init,
  NULL,NULL,NULL    /* reserved[123] */
};
const ProtobufCEnumValue response__error_code__enum_values_by_number[4] =
{
  { "OK", "RESPONSE__ERROR_CODE__OK", 1 },
  { "FAIL", "RESPONSE__ERROR_CODE__FAIL", 2 },
  { "FAIL_PARAM", "RESPONSE__ERROR_CODE__FAIL_PARAM", 3 },
  { "FAIL_MEM", "RESPONSE__ERROR_CODE__FAIL_MEM", 4 },
};
static const ProtobufCIntRange response__error_code__value_ranges[] = {
{1, 0},{0, 4}
};
const ProtobufCEnumValueIndex response__error_code__enum_values_by_name[4] =
{
  { "FAIL", 1 },
  { "FAIL_MEM", 3 },
  { "FAIL_PARAM", 2 },
  { "OK", 0 },
};
const ProtobufCEnumDescriptor response__error_code__descriptor =
{
  PROTOBUF_C_ENUM_DESCRIPTOR_MAGIC,
  "Response.ErrorCode",
  "ErrorCode",
  "Response__ErrorCode",
  "",
  4,
  response__error_code__enum_values_by_number,
  4,
  response__error_code__enum_values_by_name,
  1,
  response__error_code__value_ranges,
  NULL,NULL,NULL,NULL   /* reserved[1234] */
};
static const ProtobufCFieldDescriptor response__field_descriptors[2] =
{
  {
    "error",
    1,
    PROTOBUF_C_LABEL_REQUIRED,
    PROTOBUF_C_TYPE_ENUM,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Response, error),
    &response__error_code__descriptor,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "data",
    2,
    PROTOBUF_C_LABEL_OPTIONAL,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    PROTOBUF_C_OFFSETOF(Response, data),
    &reading_set__descriptor,
    NULL,
    0,            /* packed */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned response__field_indices_by_name[] = {
  1,   /* field[1] = data */
  0,   /* field[0] = error */
};
static const ProtobufCIntRange response__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 2 }
};
const ProtobufCMessageDescriptor response__descriptor =
{
  PROTOBUF_C_MESSAGE_DESCRIPTOR_MAGIC,
  "Response",
  "Response",
  "Response",
  "",
  sizeof(Response),
  2,
  response__field_descriptors,
  response__field_indices_by_name,
  1,  response__number_ranges,
  (ProtobufCMessageInit) response__init,
  NULL,NULL,NULL    /* reserved[123] */
};
const ProtobufCEnumValue message_type__enum_values_by_number[5] =
{
  { "QUERY", "MESSAGE_TYPE__QUERY", 1 },
  { "READINGSET", "MESSAGE_TYPE__READINGSET", 2 },
  { "RESPONSE", "MESSAGE_TYPE__RESPONSE", 3 },
  { "NEAREST", "MESSAGE_TYPE__NEAREST", 4 },
  { "DELETE", "MESSAGE_TYPE__DELETE", 5 },
};
static const ProtobufCIntRange message_type__value_ranges[] = {
{1, 0},{0, 5}
};
const ProtobufCEnumValueIndex message_type__enum_values_by_name[5] =
{
  { "DELETE", 4 },
  { "NEAREST", 3 },
  { "QUERY", 0 },
  { "READINGSET", 1 },
  { "RESPONSE", 2 },
};
const ProtobufCEnumDescriptor message_type__descriptor =
{
  PROTOBUF_C_ENUM_DESCRIPTOR_MAGIC,
  "MessageType",
  "MessageType",
  "MessageType",
  "",
  5,
  message_type__enum_values_by_number,
  5,
  message_type__enum_values_by_name,
  1,
  message_type__value_ranges,
  NULL,NULL,NULL,NULL   /* reserved[1234] */
};
static const ProtobufCMethodDescriptor reading_db__method_descriptors[3] =
{
  { "Ask", &query__descriptor, &response__descriptor },
  { "Tell", &reading_set__descriptor, &response__descriptor },
  { "Iter", &nearest__descriptor, &response__descriptor },
};
const unsigned reading_db__method_indices_by_name[] = {
  0,        /* Ask */
  2,        /* Iter */
  1         /* Tell */
};
const ProtobufCServiceDescriptor reading_db__descriptor =
{
  PROTOBUF_C_SERVICE_DESCRIPTOR_MAGIC,
  "ReadingDB",
  "Tell",
  "ReadingDB",
  "",
  3,
  reading_db__method_descriptors,
  reading_db__method_indices_by_name
};
void reading_db__ask(ProtobufCService *service,
                     const Query *input,
                     Response_Closure closure,
                     void *closure_data)
{
  PROTOBUF_C_ASSERT (service->descriptor == &reading_db__descriptor);
  service->invoke(service, 0, (const ProtobufCMessage *) input, (ProtobufCClosure) closure, closure_data);
}
void reading_db__tell(ProtobufCService *service,
                      const ReadingSet *input,
                      Response_Closure closure,
                      void *closure_data)
{
  PROTOBUF_C_ASSERT (service->descriptor == &reading_db__descriptor);
  service->invoke(service, 1, (const ProtobufCMessage *) input, (ProtobufCClosure) closure, closure_data);
}
void reading_db__iter(ProtobufCService *service,
                      const Nearest *input,
                      Response_Closure closure,
                      void *closure_data)
{
  PROTOBUF_C_ASSERT (service->descriptor == &reading_db__descriptor);
  service->invoke(service, 2, (const ProtobufCMessage *) input, (ProtobufCClosure) closure, closure_data);
}
void reading_db__init (ReadingDB_Service *service,
                       ReadingDB_ServiceDestroy destroy)
{
  protobuf_c_service_generated_init (&service->base,
                                     &reading_db__descriptor,
                                     (ProtobufCServiceDestroy) destroy);
}
