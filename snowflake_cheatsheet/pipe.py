import streamlit as st
from .utils import st_code_block, make_tabs

def pipe_segment():
    st.header("🚰 Pipe", help="The magic portal that helps move data into Snowflake tables.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, status_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "PIPE_STATUS", "❄️"])
    with create_tab:

        s3_tab, azure_tab, gcp_tab = make_tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("create-pipe", "create or replace a pipe from Amazon S3",
            """
            CREATE [ OR REPLACE ] PIPE [ IF NOT EXISTS ] <pipe_name>
                [ AUTO_INGEST = [ TRUE | FALSE ] ]
                [ ERROR_INTEGRATION = <integration_name> ]
                [ AWS_SNS_TOPIC = '<string>' ]
                [ COMMENT = '<string_literal>' ]
                AS <copy_statement>
            """
            )

        with azure_tab:
            st_code_block("create-pipe", "create or replace a pipe from Microsoft Azure",
            """
            CREATE [ OR REPLACE ] PIPE [ IF NOT EXISTS ] <pipe_name>
                [ AUTO_INGEST = [ TRUE | FALSE ] ]
                [ ERROR_INTEGRATION = <integration_name> ]
                [ INTEGRATION = '<string>' ]
                [ COMMENT = '<string_literal>' ]
                AS <copy_statement>
            """
            )

        with gcp_tab:
            st_code_block("create-pipe", "create or replace a pipe from Google Cloud Storage",
            """
            CREATE [ OR REPLACE ] PIPE [ IF NOT EXISTS ] <pipe_name>
                [ AUTO_INGEST = [ TRUE | FALSE ] ]
                [ ERROR_INTEGRATION = <integration_name> ]
                [ INTEGRATION = '<string>' ]
                [ COMMENT = '<string_literal>' ]
                AS <copy_statement>
            """
            )

    with alter_tab:
        
        
        st_code_block("alter-pipe", "change the properties of an existing pipe",
        """
        ALTER PIPE [ IF EXISTS ] <pipe_name> SET { PIPE_EXECUTION_PAUSED = { TRUE | FALSE }
            [ COMMENT = '<string_literal>' ] }
        """
        )

        st_code_block("alter-pipe", "refresh the pipe to copy staged files that were not loaded",
        """
        ALTER PIPE [ IF EXISTS ] <pipe_name> REFRESH { [ PREFIX = '<path>' ] [ MODIFIED_AFTER = <start_time> ] }
        """
        )


    with drop_tab:
        st_code_block("drop-pipe", "remove an existing pipe",
        """
        DROP PIPE [ IF EXISTS ] <pipe_name>
        """
        )


    with describe_tab:
        st_code_block("desc-pipe", "describe the properties of the pipe (e.g. create date, definition, pattern)",
        """
        DESC PIPE <pipe_name> 
        """
        )

    with show_tab:
        st_code_block("show-pipes", "show available pipes",
        """
        SHOW PIPES [ LIKE '<pattern>' ]
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

    with status_tab:
        st_code_block("https://docs.snowflake.com/en/sql-reference/functions/system_pipe_status", "return the current status of the pipe",
        """
        SELECT SYSTEM$PIPE_STATUS( '<pipe_name>' )
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Use `PIPE`s to efficiently stream and ingest data in real-time from external sources into Snowflake, providing a continuous flow of data updates without the need for manual data loading.
        - Use `PIPE`s for real-time data ingestion from streaming sources, `COPY INTO` for batch loading data from files in cloud storage, and `EXTERNAL TABLE`s for querying data residing in external cloud storage without copying it into Snowflake.
        - Enable `AUTO_INGEST` to automatically detect and load new data files into Snowflake through Snowpipe, ensuring continuous data ingestion from external sources.
        - Use the `ALTER PIPE <name> REFRESH` command to manually trigger loading of staged data files into the Snowpipe ingest queue for a specific pipe. It helps resolve data loading issues and allows you to load specific subsets of data when needed.
        - Remember that `REFRESH` can only load data files staged within the last 7 days and checks load history for both the pipe and target table, queueing files not previously loaded by the same pipe or `COPY INTO <table>` statement. Use it for short-term issue resolution, not for regular use.
        """)


