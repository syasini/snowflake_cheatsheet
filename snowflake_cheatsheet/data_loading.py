import streamlit as st
from .utils import st_code_block, make_tabs

def data_loading_segment():
    st.header("🚚 Loading Data", help="The thing you do to dump data into Snowflake Tables.")
    
    standard_tab, transform_tab, tips_tab = \
        make_tabs(["COPY INTO (standard)", "COPY INTO (with transformation)", "❄️"])
    with standard_tab:

        st_code_block("copy-into-table", "copy data from internal or external stage",
        """
        COPY INTO [<namespace>.]<table_name>
            FROM {@[<namespace>.]<stage_name>[/<path>]
                | @[<namespace>.]%<table_name>[/<path>]
                | @~[/<path>]
            }
            [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
            [ PATTERN = '<regex_pattern>' ]
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
            [ FORCE = { TRUE | FALSE } ]
            [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
        """
        )

        s3_tab, azure_tab, gcp_tab = make_tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("copy-into-table", "copy data from Amazon S3 directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM 's3://<bucket>[/<path>]'
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( {  { AWS_KEY_ID = '<string>' AWS_SECRET_KEY = '<string>' [ AWS_TOKEN = '<string>' ] } } ) } ]
                [ ENCRYPTION = ( [ TYPE = 'AWS_CSE' ] [ MASTER_KEY = '<string>' ] |
                                 [ TYPE = 'AWS_SSE_S3' ] |
                                 [ TYPE = 'AWS_SSE_KMS' [ KMS_KEY_ID = '<string>' ] ] |
                                 [ TYPE = 'NONE' ] ) ]
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
                [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
            """
            )

        with azure_tab:
            st_code_block("copy-into-table", "copy data from Azure directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM 'azure://<account>.blob.core.windows.net/<container>[/<path>]'
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( [ AZURE_SAS_TOKEN = '<string>' ] ) } ]
                [ ENCRYPTION = ( [ TYPE = { 'AZURE_CSE' | 'NONE' } ] [ MASTER_KEY = '<string>' ] ) ]
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
                [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
            """
            )

        with gcp_tab:
            st_code_block("copy-into-table", "copy data from Google Cloud Storage directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM 'gcs://<bucket>[/<path>]'
                [ STORAGE_INTEGRATION = <integration_name> ]
                [ ENCRYPTION = ( [ TYPE = 'GCS_SSE_KMS' ] [ KMS_KEY_ID = '<string>' ] | [ TYPE = 'NONE' ] ) ]
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
                [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
            """
            )
    
    with transform_tab:

        st_code_block("copy-into-table", "copy data from internal or external stage",
        """
        COPY INTO [<namespace>.]<table_name>
            FROM ( 
                SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                FROM {@[<namespace>.]<stage_name>[/<path>]
                    | @[<namespace>.]%<table_name>[/<path>]
                    | @~[/<path>]
                }
            )
            [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
            [ PATTERN = '<regex_pattern>' ]
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
            [ FORCE = { TRUE | FALSE } ]
            
        """
        )

        s3_tab, azure_tab, gcp_tab = make_tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("copy-into-table", "copy data from Amazon S3 directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM ( 
                    SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                    FROM 's3://<bucket>[/<path>]'
                    [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( {  { AWS_KEY_ID = '<string>' AWS_SECRET_KEY = '<string>' [ AWS_TOKEN = '<string>' ] } } ) } ]
                    [ ENCRYPTION = ( [ TYPE = 'AWS_CSE' ] [ MASTER_KEY = '<string>' ] |
                                    [ TYPE = 'AWS_SSE_S3' ] |
                                    [ TYPE = 'AWS_SSE_KMS' [ KMS_KEY_ID = '<string>' ] ] |
                                    [ TYPE = 'NONE' ] ) ]
                )
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
            """
            )

        with azure_tab:
            st_code_block("copy-into-table", "copy data from Azure directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM (
                    SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                    FROM 'azure://<account>.blob.core.windows.net/<container>[/<path>]'
                    [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( [ AZURE_SAS_TOKEN = '<string>' ] ) } ]
                    [ ENCRYPTION = ( [ TYPE = { 'AZURE_CSE' | 'NONE' } ] [ MASTER_KEY = '<string>' ] ) ]
                )
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
            """
            )

        with gcp_tab:
            st_code_block("copy-into-table", "copy data from Google Cloud Storage directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM ( 
                    SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                    FROM 'gcs://<bucket>[/<path>]'
                    [ STORAGE_INTEGRATION = <integration_name> ]
                    [ ENCRYPTION = ( [ TYPE = 'GCS_SSE_KMS' ] [ KMS_KEY_ID = '<string>' ] | [ TYPE = 'NONE' ] ) ]
                )
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
            """
            )

    with tips_tab:
        st.markdown("💡 **Tips**")
    
        st.markdown("- Use `COPY INTO` when you have static files or batch data that needs to be loaded into Snowflake. `COPY INTO` provides more control and flexibility over the loading process compared to pipes.")
        st.markdown("- Use `PIPE`s when you need to ingest real-time or near real-time streaming data into Snowflake (see the 🚰 **Pipe**s segment).")
        st.markdown("- Distribute your data across multiple files or use file compression to take advantage of parallel loading and improve loading speed.")
        st.markdown("- By default `COPY_INTO` will not load files that have already been transfered within *the past 64 days*. Use `FORCE = TRUE` to enforce loading all files regardless of loading history. Note the this will potentially duplicate data in the target table.")
    

