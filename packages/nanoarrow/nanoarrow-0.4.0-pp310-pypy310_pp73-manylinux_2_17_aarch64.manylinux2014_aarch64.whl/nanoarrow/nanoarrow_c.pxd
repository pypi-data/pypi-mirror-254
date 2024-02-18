
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# cython: language_level = 3

from libc.stdint cimport int8_t, uint8_t, int16_t, uint16_t
from libc.stdint cimport int32_t, uint32_t, int64_t, uint64_t

cdef extern from "nanoarrow.h" nogil:

    ctypedef int ArrowErrorCode
    cdef int NANOARROW_OK
    cdef int NANOARROW_MAX_FIXED_BUFFERS
    cdef int ARROW_FLAG_DICTIONARY_ORDERED
    cdef int ARROW_FLAG_NULLABLE
    cdef int ARROW_FLAG_MAP_KEYS_SORTED

    struct ArrowSchema:
        const char* format
        const char* name
        const char* metadata
        int64_t flags
        int64_t n_children
        ArrowSchema** children
        ArrowSchema* dictionary
        void (*release)(ArrowSchema*)
        void* private_data

    struct ArrowArray:
        int64_t length
        int64_t null_count
        int64_t offset
        int64_t n_buffers
        int64_t n_children
        const void** buffers
        ArrowArray** children
        ArrowArray* dictionary
        void (*release)(ArrowArray*)
        void* private_data

    struct ArrowArrayStream:
        int (*get_schema)(ArrowArrayStream*, ArrowSchema* out)
        int (*get_next)(ArrowArrayStream*, ArrowArray* out)
        const char* (*get_last_error)(ArrowArrayStream*)
        void (*release)(ArrowArrayStream*)
        void* private_data

    struct ArrowError:
        char message[1024]

    enum ArrowType:
        NANOARROW_TYPE_UNINITIALIZED = 0
        NANOARROW_TYPE_NA = 1
        NANOARROW_TYPE_BOOL
        NANOARROW_TYPE_UINT8
        NANOARROW_TYPE_INT8
        NANOARROW_TYPE_UINT16
        NANOARROW_TYPE_INT16
        NANOARROW_TYPE_UINT32
        NANOARROW_TYPE_INT32
        NANOARROW_TYPE_UINT64
        NANOARROW_TYPE_INT64
        NANOARROW_TYPE_HALF_FLOAT
        NANOARROW_TYPE_FLOAT
        NANOARROW_TYPE_DOUBLE
        NANOARROW_TYPE_STRING
        NANOARROW_TYPE_BINARY
        NANOARROW_TYPE_FIXED_SIZE_BINARY
        NANOARROW_TYPE_DATE32
        NANOARROW_TYPE_DATE64
        NANOARROW_TYPE_TIMESTAMP
        NANOARROW_TYPE_TIME32
        NANOARROW_TYPE_TIME64
        NANOARROW_TYPE_INTERVAL_MONTHS
        NANOARROW_TYPE_INTERVAL_DAY_TIME
        NANOARROW_TYPE_DECIMAL128
        NANOARROW_TYPE_DECIMAL256
        NANOARROW_TYPE_LIST
        NANOARROW_TYPE_STRUCT
        NANOARROW_TYPE_SPARSE_UNION
        NANOARROW_TYPE_DENSE_UNION
        NANOARROW_TYPE_DICTIONARY
        NANOARROW_TYPE_MAP
        NANOARROW_TYPE_EXTENSION
        NANOARROW_TYPE_FIXED_SIZE_LIST
        NANOARROW_TYPE_DURATION
        NANOARROW_TYPE_LARGE_STRING
        NANOARROW_TYPE_LARGE_BINARY
        NANOARROW_TYPE_LARGE_LIST
        NANOARROW_TYPE_INTERVAL_MONTH_DAY_NANO

    enum ArrowTimeUnit:
        NANOARROW_TIME_UNIT_SECOND = 0
        NANOARROW_TIME_UNIT_MILLI = 1
        NANOARROW_TIME_UNIT_MICRO = 2
        NANOARROW_TIME_UNIT_NANO = 3

    enum ArrowValidationLevel:
        NANOARROW_VALIDATION_LEVEL_NONE = 0
        NANOARROW_VALIDATION_LEVEL_MINIMAL = 1
        NANOARROW_VALIDATION_LEVEL_DEFAULT = 2
        NANOARROW_VALIDATION_LEVEL_FULL = 3

    enum ArrowBufferType:
        NANOARROW_BUFFER_TYPE_NONE
        NANOARROW_BUFFER_TYPE_VALIDITY
        NANOARROW_BUFFER_TYPE_TYPE_ID
        NANOARROW_BUFFER_TYPE_UNION_OFFSET
        NANOARROW_BUFFER_TYPE_DATA_OFFSET
        NANOARROW_BUFFER_TYPE_DATA

    struct ArrowStringView:
        const char* data
        int64_t size_bytes

    union ArrowBufferViewData:
        const void* data
        const int8_t* as_int8
        const uint8_t* as_uint8
        const int16_t* as_int16
        const uint16_t* as_uint16
        const int32_t* as_int32
        const uint32_t* as_uint32
        const int64_t* as_int64
        const uint64_t* as_uint64
        const double* as_double
        const float* as_float
        const char* as_char

    struct ArrowBufferView:
        ArrowBufferViewData data
        int64_t size_bytes

    struct ArrowBufferAllocator:
        uint8_t* (*reallocate)(ArrowBufferAllocator* allocator, uint8_t* ptr,
                         int64_t old_size, int64_t new_size)
        void (*free)(ArrowBufferAllocator* allocator, uint8_t* ptr, int64_t size)
        void* private_data

    struct ArrowBuffer:
        uint8_t* data
        int64_t size_bytes
        int64_t capacity_bytes
        ArrowBufferAllocator allocator

    struct ArrowBitmap:
        ArrowBuffer buffer
        int64_t size_bits

    struct ArrowLayout:
        ArrowBufferType buffer_type[3]
        ArrowType buffer_data_type[3]
        int64_t element_size_bits[3]
        int64_t child_size_elements

    struct ArrowArrayView:
        const ArrowArray* array
        int64_t offset
        int64_t length
        int64_t null_count
        ArrowType storage_type
        ArrowLayout layout
        ArrowBufferView buffer_views[3]
        int64_t n_children
        ArrowArrayView** children
        ArrowArrayView* dictionary
        int8_t* union_type_id_map

    struct ArrowArrayPrivateData:
        ArrowBitmap bitmap
        ArrowBuffer buffers[3 - 1]
        const void* buffer_data[3]
        ArrowType storage_type
        ArrowLayout layout
        int8_t union_type_id_is_child_index

    struct ArrowInterval:
        ArrowType type
        int32_t months
        int32_t days
        int32_t ms
        int64_t ns

    struct ArrowDecimal:
        uint64_t words[4]
        int32_t precision
        int32_t scale
        int n_words
        int high_word_index
        int low_word_index

    struct ArrowMetadataReader:
        const char* metadata
        int64_t offset
        int32_t remaining_keys

    struct ArrowSchemaView:
        const ArrowSchema* schema
        ArrowType type
        ArrowType storage_type
        ArrowLayout layout
        ArrowStringView extension_name
        ArrowStringView extension_metadata
        int32_t fixed_size
        int32_t decimal_bitwidth
        int32_t decimal_precision
        int32_t decimal_scale
        ArrowTimeUnit time_unit
        const char* timezone
        const char* union_type_ids

    const char* ArrowTypeString(ArrowType type)
    const char* ArrowTimeUnitString(ArrowTimeUnit time_unit)
    void* ArrowMalloc(int64_t size)
    void* ArrowRealloc(void* ptr, int64_t size)
    void ArrowFree(void* ptr)
    void ArrowSchemaMove(ArrowSchema* src, ArrowSchema* dst)
    void ArrowSchemaRelease(ArrowSchema* schema)
    void ArrowArrayMove(ArrowArray* src, ArrowArray* dst)
    void ArrowArrayRelease(ArrowArray* array)
    void ArrowArrayStreamMove(ArrowArrayStream* src, ArrowArrayStream* dst)
    ArrowErrorCode ArrowArrayStreamGetSchema(ArrowArrayStream* array_stream, ArrowSchema* out, ArrowError* error)
    ArrowErrorCode ArrowArrayStreamGetNext(ArrowArrayStream* array_stream, ArrowArray* out, ArrowError* error)
    const char* ArrowArrayStreamGetLastError(ArrowArrayStream* array_stream)
    void ArrowArrayStreamRelease(ArrowArrayStream* array_stream)
    const char* ArrowNanoarrowVersion()
    int ArrowNanoarrowVersionInt()
    void ArrowLayoutInit(ArrowLayout* layout, ArrowType storage_type)
    ArrowErrorCode ArrowDecimalSetDigits(ArrowDecimal* decimal, ArrowStringView value)
    ArrowErrorCode ArrowDecimalAppendDigitsToBuffer(const ArrowDecimal* decimal, ArrowBuffer* buffer)
    void ArrowSchemaInit(ArrowSchema* schema)
    ArrowErrorCode ArrowSchemaInitFromType(ArrowSchema* schema, ArrowType type)
    int64_t ArrowSchemaToString(const ArrowSchema* schema, char* out, int64_t n, char recursive)
    ArrowErrorCode ArrowSchemaSetType(ArrowSchema* schema, ArrowType type)
    ArrowErrorCode ArrowSchemaSetTypeStruct(ArrowSchema* schema, int64_t n_children)
    ArrowErrorCode ArrowSchemaSetTypeFixedSize(ArrowSchema* schema, ArrowType type, int32_t fixed_size)
    ArrowErrorCode ArrowSchemaSetTypeDecimal(ArrowSchema* schema, ArrowType type, int32_t decimal_precision, int32_t decimal_scale)
    ArrowErrorCode ArrowSchemaSetTypeDateTime(ArrowSchema* schema, ArrowType type, ArrowTimeUnit time_unit, const char* timezone)
    ArrowErrorCode ArrowSchemaSetTypeUnion(ArrowSchema* schema, ArrowType type, int64_t n_children)
    ArrowErrorCode ArrowSchemaDeepCopy(const ArrowSchema* schema, ArrowSchema* schema_out)
    ArrowErrorCode ArrowSchemaSetFormat(ArrowSchema* schema, const char* format)
    ArrowErrorCode ArrowSchemaSetName(ArrowSchema* schema, const char* name)
    ArrowErrorCode ArrowSchemaSetMetadata(ArrowSchema* schema, const char* metadata)
    ArrowErrorCode ArrowSchemaAllocateChildren(ArrowSchema* schema, int64_t n_children)
    ArrowErrorCode ArrowSchemaAllocateDictionary(ArrowSchema* schema)
    ArrowErrorCode ArrowMetadataReaderInit(ArrowMetadataReader* reader, const char* metadata)
    ArrowErrorCode ArrowMetadataReaderRead(ArrowMetadataReader* reader, ArrowStringView* key_out, ArrowStringView* value_out)
    int64_t ArrowMetadataSizeOf(const char* metadata)
    char ArrowMetadataHasKey(const char* metadata, ArrowStringView key)
    ArrowErrorCode ArrowMetadataGetValue(const char* metadata, ArrowStringView key, ArrowStringView* value_out)
    ArrowErrorCode ArrowMetadataBuilderInit(ArrowBuffer* buffer, const char* metadata)
    ArrowErrorCode ArrowMetadataBuilderAppend(ArrowBuffer* buffer, ArrowStringView key, ArrowStringView value)
    ArrowErrorCode ArrowMetadataBuilderSet(ArrowBuffer* buffer, ArrowStringView key, ArrowStringView value)
    ArrowErrorCode ArrowMetadataBuilderRemove(ArrowBuffer* buffer, ArrowStringView key)
    ArrowErrorCode ArrowSchemaViewInit(ArrowSchemaView* schema_view, const ArrowSchema* schema, ArrowError* error)
    void ArrowBufferInit(ArrowBuffer* buffer)
    ArrowErrorCode ArrowBufferSetAllocator(ArrowBuffer* buffer, ArrowBufferAllocator allocator)
    void ArrowBufferReset(ArrowBuffer* buffer)
    void ArrowBufferMove(ArrowBuffer* src, ArrowBuffer* dst)
    ArrowErrorCode ArrowBufferResize(ArrowBuffer* buffer, int64_t new_capacity_bytes, char shrink_to_fit)
    ArrowErrorCode ArrowBufferReserve(ArrowBuffer* buffer, int64_t additional_size_bytes)
    void ArrowBufferAppendUnsafe(ArrowBuffer* buffer, const void* data, int64_t size_bytes)
    ArrowErrorCode ArrowBufferAppend(ArrowBuffer* buffer, const void* data, int64_t size_bytes)
    ArrowErrorCode ArrowBufferAppendFill(ArrowBuffer* buffer, uint8_t value, int64_t size_bytes)
    ArrowErrorCode ArrowBufferAppendDouble(ArrowBuffer* buffer, double value)
    ArrowErrorCode ArrowBufferAppendFloat(ArrowBuffer* buffer, float value)
    ArrowErrorCode ArrowBufferAppendStringView(ArrowBuffer* buffer, ArrowStringView value)
    ArrowErrorCode ArrowBufferAppendBufferView(ArrowBuffer* buffer, ArrowBufferView value)
    int8_t ArrowBitGet(const uint8_t* bits, int64_t i)
    void ArrowBitSet(uint8_t* bits, int64_t i)
    void ArrowBitClear(uint8_t* bits, int64_t i)
    void ArrowBitSetTo(uint8_t* bits, int64_t i, uint8_t value)
    void ArrowBitsSetTo(uint8_t* bits, int64_t start_offset, int64_t length, uint8_t bits_are_set)
    int64_t ArrowBitCountSet(const uint8_t* bits, int64_t i_from, int64_t i_to)
    void ArrowBitmapInit(ArrowBitmap* bitmap)
    void ArrowBitmapMove(ArrowBitmap* src, ArrowBitmap* dst)
    ArrowErrorCode ArrowBitmapReserve(ArrowBitmap* bitmap, int64_t additional_size_bits)
    ArrowErrorCode ArrowBitmapResize(ArrowBitmap* bitmap, int64_t new_capacity_bits, char shrink_to_fit)
    ArrowErrorCode ArrowBitmapAppend(ArrowBitmap* bitmap, uint8_t bits_are_set, int64_t length)
    void ArrowBitmapAppendUnsafe(ArrowBitmap* bitmap, uint8_t bits_are_set, int64_t length)
    void ArrowBitmapReset(ArrowBitmap* bitmap)
    ArrowErrorCode ArrowArrayInitFromType(ArrowArray* array, ArrowType storage_type)
    ArrowErrorCode ArrowArrayInitFromSchema(ArrowArray* array, const ArrowSchema* schema, ArrowError* error)
    ArrowErrorCode ArrowArrayInitFromArrayView(ArrowArray* array, const ArrowArrayView* array_view, ArrowError* error)
    ArrowErrorCode ArrowArrayAllocateChildren(ArrowArray* array, int64_t n_children)
    ArrowErrorCode ArrowArrayAllocateDictionary(ArrowArray* array)
    void ArrowArraySetValidityBitmap(ArrowArray* array, ArrowBitmap* bitmap)
    ArrowErrorCode ArrowArraySetBuffer(ArrowArray* array, int64_t i, ArrowBuffer* buffer)
    ArrowErrorCode ArrowArrayStartAppending(ArrowArray* array)
    ArrowErrorCode ArrowArrayReserve(ArrowArray* array, int64_t additional_size_elements)
    ArrowErrorCode ArrowArrayAppendNull(ArrowArray* array, int64_t n)
    ArrowErrorCode ArrowArrayAppendEmpty(ArrowArray* array, int64_t n)
    ArrowErrorCode ArrowArrayAppendInt(ArrowArray* array, int64_t value)
    ArrowErrorCode ArrowArrayAppendUInt(ArrowArray* array, uint64_t value)
    ArrowErrorCode ArrowArrayAppendDouble(ArrowArray* array, double value)
    ArrowErrorCode ArrowArrayAppendBytes(ArrowArray* array, ArrowBufferView value)
    ArrowErrorCode ArrowArrayAppendString(ArrowArray* array, ArrowStringView value)
    ArrowErrorCode ArrowArrayAppendInterval(ArrowArray* array, const ArrowInterval* value)
    ArrowErrorCode ArrowArrayAppendDecimal(ArrowArray* array, const ArrowDecimal* value)
    ArrowErrorCode ArrowArrayFinishElement(ArrowArray* array)
    ArrowErrorCode ArrowArrayFinishUnionElement(ArrowArray* array, int8_t type_id)
    ArrowErrorCode ArrowArrayShrinkToFit(ArrowArray* array)
    ArrowErrorCode ArrowArrayFinishBuildingDefault(ArrowArray* array, ArrowError* error)
    ArrowErrorCode ArrowArrayFinishBuilding(ArrowArray* array, ArrowValidationLevel validation_level, ArrowError* error)
    void ArrowArrayViewInitFromType(ArrowArrayView* array_view, ArrowType storage_type)
    void ArrowArrayViewMove(ArrowArrayView* src, ArrowArrayView* dst)
    ArrowErrorCode ArrowArrayViewInitFromSchema(ArrowArrayView* array_view, const ArrowSchema* schema, ArrowError* error)
    ArrowErrorCode ArrowArrayViewAllocateChildren(ArrowArrayView* array_view, int64_t n_children)
    ArrowErrorCode ArrowArrayViewAllocateDictionary(ArrowArrayView* array_view)
    void ArrowArrayViewSetLength(ArrowArrayView* array_view, int64_t length)
    ArrowErrorCode ArrowArrayViewSetArray(ArrowArrayView* array_view, const ArrowArray* array, ArrowError* error)
    ArrowErrorCode ArrowArrayViewSetArrayMinimal(ArrowArrayView* array_view, const ArrowArray* array, ArrowError* error)
    ArrowErrorCode ArrowArrayViewValidate(ArrowArrayView* array_view, ArrowValidationLevel validation_level, ArrowError* error)
    void ArrowArrayViewReset(ArrowArrayView* array_view)
    int8_t ArrowArrayViewIsNull(const ArrowArrayView* array_view, int64_t i)
    int8_t ArrowArrayViewUnionTypeId(const ArrowArrayView* array_view, int64_t i)
    int8_t ArrowArrayViewUnionChildIndex(const ArrowArrayView* array_view, int64_t i)
    int64_t ArrowArrayViewUnionChildOffset(const ArrowArrayView* array_view, int64_t i)
    int64_t ArrowArrayViewGetIntUnsafe(const ArrowArrayView* array_view, int64_t i)
    uint64_t ArrowArrayViewGetUIntUnsafe(const ArrowArrayView* array_view, int64_t i)
    double ArrowArrayViewGetDoubleUnsafe(const ArrowArrayView* array_view, int64_t i)
    void ArrowArrayViewGetDecimalUnsafe(const ArrowArrayView* array_view, int64_t i, ArrowDecimal* out)
    ArrowErrorCode ArrowBasicArrayStreamInit(ArrowArrayStream* array_stream, ArrowSchema* schema, int64_t n_arrays)
    void ArrowBasicArrayStreamSetArray(ArrowArrayStream* array_stream, int64_t i, ArrowArray* array)
    ArrowErrorCode ArrowBasicArrayStreamValidate(const ArrowArrayStream* array_stream, ArrowError* error)
