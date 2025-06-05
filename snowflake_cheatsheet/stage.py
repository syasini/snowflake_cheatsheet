import streamlit as st
from .utils import st_code_block, make_tabs

def stage_segment():
    st.header("🚉 Stage", help="The platform where the data sits before moving in and out of Snowflake.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, list_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "LIST", "❄️"])
    
    with create_tab:
        
        st_code_block("create-stage", "create or replace an internal stage",
        """
        CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <internal_stage_name>
            [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                  [ REFRESH_ON_CREATE =  { TRUE | FALSE } ] ) ]
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT }) ]
        """
        )

        s3_tab, azure_tab, gcp_tab = make_tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("create-stage", "create or replace an external stage for Amazon S3",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <external_stage_name>
                [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                    [ REFRESH_ON_CREATE =  { TRUE | FALSE } ]
                    [ AUTO_REFRESH = { TRUE | FALSE } ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT })  ]
            """
            )

        with azure_tab:
            st_code_block("create-stage", "create or replace an external stage for Microsoft Azure",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <external_stage_name>
                [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                    [ REFRESH_ON_CREATE =  { TRUE | FALSE } ]
                    [ AUTO_REFRESH = { TRUE | FALSE } ] ) ]
                    [ NOTIFICATION_INTEGRATION = '<notification_integration_name>' ] 
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT })  ]
            """
            )

        with gcp_tab:
            st_code_block("create-stage", "create or replace an external stage for Google Cloud Storage",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <external_stage_name>
                [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                    [ REFRESH_ON_CREATE =  { TRUE | FALSE } ]
                    [ AUTO_REFRESH = { TRUE | FALSE } ] ) ]
                    [ NOTIFICATION_INTEGRATION = '<notification_integration_name>' ] 
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT })  ]
            """
            )

    with alter_tab:
        
        
        st_code_block("alter-stage", "rename a stage",
        """
        ALTER STAGE [ IF EXISTS ] <name> RENAME TO <new_stage_name>
        """
        )

        st_code_block("alter-stage", "change directory settings for the stage",
        """
        ALTER STAGE [ IF EXISTS ] <name> SET DIRECTORY = ( { ENABLE = TRUE | FALSE } )

        ALTER STAGE [ IF EXISTS ] <name> REFRESH [ SUBPATH = '<relative-path>' ]
        """
        )

        st_code_block("alter-stage", "change internal stage parameters",
        """
        ALTER STAGE [ IF EXISTS ] <name> SET {
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
            [ COMMENT = '<string_literal>' ] 
        }
        """
        )


        s3_tab, azure_tab, gcp_tab = make_tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("alter-stage", "change external stage parameters for Amazon S3",
            """
            ALTER STAGE [ IF EXISTS ] <name> SET {
                [ URL = 's3://<bucket>[/<path>/]' ]
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( {  { AWS_KEY_ID = '<string>' AWS_SECRET_KEY = '<string>' [ AWS_TOKEN = '<string>' ] } | AWS_ROLE = '<string>'  } ) } ]
                [ ENCRYPTION = ( [ TYPE = 'AWS_CSE' ] [ MASTER_KEY = '<string>' ] |
                                 [ TYPE = 'AWS_SSE_S3' ] |
                                 [ TYPE = 'AWS_SSE_KMS' [ KMS_KEY_ID = '<string>' ] |
                                 [ TYPE = 'NONE' ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
                [ COMMENT = '<string_literal>' ] }
            }
            """
            )

        with azure_tab:
            st_code_block("alter-stage", "change external stage parameters for Microsoft Azure",
            """
            ALTER STAGE [ IF EXISTS ] <name> SET {
                [ URL = 'azure://<account>.blob.core.windows.net/<container>[/<path>/]' ]
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( [ AZURE_SAS_TOKEN = '<string>' ] ) } ]
                [ ENCRYPTION = ( [ TYPE = { 'AZURE_CSE' | 'NONE' } ] [ MASTER_KEY = '<string>' ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
                [ COMMENT = '<string_literal>' ] }
            }
            """
            )

        with gcp_tab:
            st_code_block("alter-stage", "change external stage parameters for Google Cloud Storage",
            """
            ALTER STAGE [ IF EXISTS ] <name> SET {
                [ URL = 'gcs://<bucket>[/<path>/]' ]
                [ STORAGE_INTEGRATION = <integration_name> } ]
                [ ENCRYPTION = ( [ TYPE = 'GCS_SSE_KMS' ] [ KMS_KEY_ID = '<string>' ] | [ TYPE = 'NONE' ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
                [ COMMENT = '<string_literal>' ] }
            }
            """
            )


    with drop_tab:
        st_code_block("drop-stage", "remove an existing stage",
        """
        DROP STAGE [ IF EXISTS ] <name> 
        """
        )


    with describe_tab:
        st_code_block("desc-stage", "describe the properties of the stage (e.g. file format, copy, location)",
        """
        DESC STAGE <name> 
        """
        )

    with show_tab:
        st_code_block("show-stages", "show available stages",
        """
        SHOW STAGES [ LIKE '<pattern>' ]
            [ IN
                 {
                   ACCOUNT                  |
                   DATABASE                 |
                   DATABASE <database_name> |
                   SCHEMA                   |
                   SCHEMA <schema_name>     |
                   <schema_name>
                 }
            ]
        """
        )

    with list_tab:
        st_code_block("list", "return a list of files that have been staged",
        """
        LIST { 
                @[<namespace>.]<int_stage_name>[/<path>]
                | @[<namespace>.]%<table_name>[/<path>]
                | @~[/<path>]
             } 
             [ PATTERN = '<regex_pattern>' ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - See [this guide](https://docs.snowflake.com/en/user-guide/data-load-s3-config) for various options to configure secure access to a private Amazon S3 bucket. 
        - Use `DIRECTORY` tables to efficiently store and catalog staged files, allowing seamless querying to retrieve URLs for the staged files, along with other essential metadata.
        - Use `EXTERNAL` tables when you want to access and query data that resides in external cloud storage (e.g. AWS S3) without copying or moving the data into Snowflake.
        """)

