

/*
WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

This file was generated from AddThreeInts_.idl using "rtiddsgen".
The rtiddsgen tool is part of the RTI Connext distribution.
For more information, type 'rtiddsgen -help' at a command shell
or consult the RTI Connext manual.
*/

#ifndef AddThreeInts__330796887_h
#define AddThreeInts__330796887_h

#ifndef NDDS_STANDALONE_TYPE
#ifndef ndds_cpp_h
#include "ndds/ndds_cpp.h"
#endif
#else
#include "ndds_standalone_type.h"
#endif

namespace tutorial_interfaces {
    namespace srv {
        namespace dds_ {

            extern const char *AddThreeInts_Request_TYPENAME;

            struct AddThreeInts_Request_Seq;
            #ifndef NDDS_STANDALONE_TYPE
            class AddThreeInts_Request_TypeSupport;
            class AddThreeInts_Request_DataWriter;
            class AddThreeInts_Request_DataReader;
            #endif

            class AddThreeInts_Request_ 
            {
              public:
                typedef struct AddThreeInts_Request_Seq Seq;
                #ifndef NDDS_STANDALONE_TYPE
                typedef AddThreeInts_Request_TypeSupport TypeSupport;
                typedef AddThreeInts_Request_DataWriter DataWriter;
                typedef AddThreeInts_Request_DataReader DataReader;
                #endif

                DDS_LongLong   a_ ;
                DDS_LongLong   b_ ;
                DDS_LongLong   c_ ;

            };
            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT)
            /* If the code is building on Windows, start exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport __declspec(dllexport)
            #endif

            NDDSUSERDllExport DDS_TypeCode* AddThreeInts_Request__get_typecode(void); /* Type code */

            DDS_SEQUENCE(AddThreeInts_Request_Seq, AddThreeInts_Request_);

            NDDSUSERDllExport
            RTIBool AddThreeInts_Request__initialize(
                AddThreeInts_Request_* self);

            NDDSUSERDllExport
            RTIBool AddThreeInts_Request__initialize_ex(
                AddThreeInts_Request_* self,RTIBool allocatePointers,RTIBool allocateMemory);

            NDDSUSERDllExport
            RTIBool AddThreeInts_Request__initialize_w_params(
                AddThreeInts_Request_* self,
                const struct DDS_TypeAllocationParams_t * allocParams);  

            NDDSUSERDllExport
            void AddThreeInts_Request__finalize(
                AddThreeInts_Request_* self);

            NDDSUSERDllExport
            void AddThreeInts_Request__finalize_ex(
                AddThreeInts_Request_* self,RTIBool deletePointers);

            NDDSUSERDllExport
            void AddThreeInts_Request__finalize_w_params(
                AddThreeInts_Request_* self,
                const struct DDS_TypeDeallocationParams_t * deallocParams);

            NDDSUSERDllExport
            void AddThreeInts_Request__finalize_optional_members(
                AddThreeInts_Request_* self, RTIBool deletePointers);  

            NDDSUSERDllExport
            RTIBool AddThreeInts_Request__copy(
                AddThreeInts_Request_* dst,
                const AddThreeInts_Request_* src);

            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT)
            /* If the code is building on Windows, stop exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport
            #endif
        } /* namespace dds_  */
    } /* namespace srv  */
} /* namespace tutorial_interfaces  */
namespace tutorial_interfaces {
    namespace srv {
        namespace dds_ {

            extern const char *AddThreeInts_Response_TYPENAME;

            struct AddThreeInts_Response_Seq;
            #ifndef NDDS_STANDALONE_TYPE
            class AddThreeInts_Response_TypeSupport;
            class AddThreeInts_Response_DataWriter;
            class AddThreeInts_Response_DataReader;
            #endif

            class AddThreeInts_Response_ 
            {
              public:
                typedef struct AddThreeInts_Response_Seq Seq;
                #ifndef NDDS_STANDALONE_TYPE
                typedef AddThreeInts_Response_TypeSupport TypeSupport;
                typedef AddThreeInts_Response_DataWriter DataWriter;
                typedef AddThreeInts_Response_DataReader DataReader;
                #endif

                DDS_LongLong   sum_ ;

            };
            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT)
            /* If the code is building on Windows, start exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport __declspec(dllexport)
            #endif

            NDDSUSERDllExport DDS_TypeCode* AddThreeInts_Response__get_typecode(void); /* Type code */

            DDS_SEQUENCE(AddThreeInts_Response_Seq, AddThreeInts_Response_);

            NDDSUSERDllExport
            RTIBool AddThreeInts_Response__initialize(
                AddThreeInts_Response_* self);

            NDDSUSERDllExport
            RTIBool AddThreeInts_Response__initialize_ex(
                AddThreeInts_Response_* self,RTIBool allocatePointers,RTIBool allocateMemory);

            NDDSUSERDllExport
            RTIBool AddThreeInts_Response__initialize_w_params(
                AddThreeInts_Response_* self,
                const struct DDS_TypeAllocationParams_t * allocParams);  

            NDDSUSERDllExport
            void AddThreeInts_Response__finalize(
                AddThreeInts_Response_* self);

            NDDSUSERDllExport
            void AddThreeInts_Response__finalize_ex(
                AddThreeInts_Response_* self,RTIBool deletePointers);

            NDDSUSERDllExport
            void AddThreeInts_Response__finalize_w_params(
                AddThreeInts_Response_* self,
                const struct DDS_TypeDeallocationParams_t * deallocParams);

            NDDSUSERDllExport
            void AddThreeInts_Response__finalize_optional_members(
                AddThreeInts_Response_* self, RTIBool deletePointers);  

            NDDSUSERDllExport
            RTIBool AddThreeInts_Response__copy(
                AddThreeInts_Response_* dst,
                const AddThreeInts_Response_* src);

            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT)
            /* If the code is building on Windows, stop exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport
            #endif
        } /* namespace dds_  */
    } /* namespace srv  */
} /* namespace tutorial_interfaces  */

#endif /* AddThreeInts_ */

