
/*
WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

This file was generated from AddThreeInts_.idl using "rtiddsgen".
The rtiddsgen tool is part of the RTI Connext distribution.
For more information, type 'rtiddsgen -help' at a command shell
or consult the RTI Connext manual.
*/

#include "AddThreeInts_Support.h"
#include "AddThreeInts_Plugin.h"

#ifndef dds_c_log_impl_h              
#include "dds_c/dds_c_log_impl.h"                                
#endif        

namespace tutorial_interfaces {
    namespace srv {
        namespace dds_ {

            /* ========================================================================= */
            /**
            <<IMPLEMENTATION>>

            Defines:   TData,
            TDataWriter,
            TDataReader,
            TTypeSupport

            Configure and implement 'AddThreeInts_Request_' support classes.

            Note: Only the #defined classes get defined
            */

            /* ----------------------------------------------------------------- */
            /* DDSDataWriter
            */

            /**
            <<IMPLEMENTATION >>

            Defines:   TDataWriter, TData
            */

            /* Requires */
            #define TTYPENAME   AddThreeInts_Request_TYPENAME

            /* Defines */
            #define TDataWriter AddThreeInts_Request_DataWriter
            #define TData       tutorial_interfaces::srv::dds_::AddThreeInts_Request_

            #include "dds_cpp/generic/dds_cpp_data_TDataWriter.gen"

            #undef TDataWriter
            #undef TData

            #undef TTYPENAME

            /* ----------------------------------------------------------------- */
            /* DDSDataReader
            */

            /**
            <<IMPLEMENTATION >>

            Defines:   TDataReader, TDataSeq, TData
            */

            /* Requires */
            #define TTYPENAME   AddThreeInts_Request_TYPENAME

            /* Defines */
            #define TDataReader AddThreeInts_Request_DataReader
            #define TDataSeq    AddThreeInts_Request_Seq
            #define TData       tutorial_interfaces::srv::dds_::AddThreeInts_Request_

            #include "dds_cpp/generic/dds_cpp_data_TDataReader.gen"

            #undef TDataReader
            #undef TDataSeq
            #undef TData

            #undef TTYPENAME

            /* ----------------------------------------------------------------- */
            /* TypeSupport

            <<IMPLEMENTATION >>

            Requires:  TTYPENAME,
            TPlugin_new
            TPlugin_delete
            Defines:   TTypeSupport, TData, TDataReader, TDataWriter
            */

            /* Requires */
            #define TTYPENAME    AddThreeInts_Request_TYPENAME
            #define TPlugin_new  tutorial_interfaces::srv::dds_::AddThreeInts_Request_Plugin_new
            #define TPlugin_delete  tutorial_interfaces::srv::dds_::AddThreeInts_Request_Plugin_delete

            /* Defines */
            #define TTypeSupport AddThreeInts_Request_TypeSupport
            #define TData        tutorial_interfaces::srv::dds_::AddThreeInts_Request_
            #define TDataReader  AddThreeInts_Request_DataReader
            #define TDataWriter  AddThreeInts_Request_DataWriter
            #define TGENERATE_SER_CODE
            #define TGENERATE_TYPECODE

            #include "dds_cpp/generic/dds_cpp_data_TTypeSupport.gen"

            #undef TTypeSupport
            #undef TData
            #undef TDataReader
            #undef TDataWriter
            #undef TGENERATE_TYPECODE
            #undef TGENERATE_SER_CODE
            #undef TTYPENAME
            #undef TPlugin_new
            #undef TPlugin_delete

        } /* namespace dds_  */
    } /* namespace srv  */
} /* namespace tutorial_interfaces  */
namespace tutorial_interfaces {
    namespace srv {
        namespace dds_ {

            /* ========================================================================= */
            /**
            <<IMPLEMENTATION>>

            Defines:   TData,
            TDataWriter,
            TDataReader,
            TTypeSupport

            Configure and implement 'AddThreeInts_Response_' support classes.

            Note: Only the #defined classes get defined
            */

            /* ----------------------------------------------------------------- */
            /* DDSDataWriter
            */

            /**
            <<IMPLEMENTATION >>

            Defines:   TDataWriter, TData
            */

            /* Requires */
            #define TTYPENAME   AddThreeInts_Response_TYPENAME

            /* Defines */
            #define TDataWriter AddThreeInts_Response_DataWriter
            #define TData       tutorial_interfaces::srv::dds_::AddThreeInts_Response_

            #include "dds_cpp/generic/dds_cpp_data_TDataWriter.gen"

            #undef TDataWriter
            #undef TData

            #undef TTYPENAME

            /* ----------------------------------------------------------------- */
            /* DDSDataReader
            */

            /**
            <<IMPLEMENTATION >>

            Defines:   TDataReader, TDataSeq, TData
            */

            /* Requires */
            #define TTYPENAME   AddThreeInts_Response_TYPENAME

            /* Defines */
            #define TDataReader AddThreeInts_Response_DataReader
            #define TDataSeq    AddThreeInts_Response_Seq
            #define TData       tutorial_interfaces::srv::dds_::AddThreeInts_Response_

            #include "dds_cpp/generic/dds_cpp_data_TDataReader.gen"

            #undef TDataReader
            #undef TDataSeq
            #undef TData

            #undef TTYPENAME

            /* ----------------------------------------------------------------- */
            /* TypeSupport

            <<IMPLEMENTATION >>

            Requires:  TTYPENAME,
            TPlugin_new
            TPlugin_delete
            Defines:   TTypeSupport, TData, TDataReader, TDataWriter
            */

            /* Requires */
            #define TTYPENAME    AddThreeInts_Response_TYPENAME
            #define TPlugin_new  tutorial_interfaces::srv::dds_::AddThreeInts_Response_Plugin_new
            #define TPlugin_delete  tutorial_interfaces::srv::dds_::AddThreeInts_Response_Plugin_delete

            /* Defines */
            #define TTypeSupport AddThreeInts_Response_TypeSupport
            #define TData        tutorial_interfaces::srv::dds_::AddThreeInts_Response_
            #define TDataReader  AddThreeInts_Response_DataReader
            #define TDataWriter  AddThreeInts_Response_DataWriter
            #define TGENERATE_SER_CODE
            #define TGENERATE_TYPECODE

            #include "dds_cpp/generic/dds_cpp_data_TTypeSupport.gen"

            #undef TTypeSupport
            #undef TData
            #undef TDataReader
            #undef TDataWriter
            #undef TGENERATE_TYPECODE
            #undef TGENERATE_SER_CODE
            #undef TTYPENAME
            #undef TPlugin_new
            #undef TPlugin_delete

        } /* namespace dds_  */
    } /* namespace srv  */
} /* namespace tutorial_interfaces  */

