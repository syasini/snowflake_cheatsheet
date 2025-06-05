import streamlit as st
from .utils import st_code_block, make_tabs

def stream_segment():
    st.header("🌊 Stream", help="The thing that keeps track of changes in your data.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:
        
        st_code_block("create-stream", "create or replace an existing stream on a table",
        """
        CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS] <stream_name>
            ON TABLE <table_name>
            [ APPEND_ONLY = TRUE | FALSE ]
            [ SHOW_INITIAL_ROWS = TRUE | FALSE ]
            [ COMMENT = '<string_literal>' ]
        """
        )

        st_code_block("create-stream", "create or replace an existing stream on a directory table",
        """
        CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS] <stream_name>
            ON STAGE <stage_name>
            [ COMMENT = '<string_literal>' ]
        """
        )

        st_code_block("create-stream", "create or replace an existing stream on a view",
        """
        CREATE [ OR REPLACE ] STREAM [IF NOT EXISTS] <stream_name>
            ON VIEW <view_name>
            [ APPEND_ONLY = TRUE | FALSE ]
            [ SHOW_INITIAL_ROWS = TRUE | FALSE ]
            [ COMMENT = '<string_literal>' ]
        """
        )

    with alter_tab:
        
        
        st_code_block("alter-stream", "modify the comment on the stream",
        """
        ALTER STREAM [ IF EXISTS ] <stream_name> SET COMMENT = '<string_literal>'
        """
        )


    with drop_tab:
        st_code_block("drop-stream", "remove an existing stream",
        """
        DROP STREAM [ IF EXISTS ] <stream_name>
        """
        )


    with describe_tab:
        st_code_block("desc-stream", "describe the columns in the stream",
        """
        DESC STREAM <stream_name> 
        """
        )

    with show_tab:
        st_code_block("show-streams", "show available streams",
        """
        SHOW STREAMS [ LIKE '<pattern>' ]
                     [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
                     [ STARTS WITH '<name_string>' ]
                     [ LIMIT <rows> [ FROM '<name_string>' ] ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Use `APPEND_ONLY=TRUE` to track row inserts only, improving query performance over standard `STREAM`s and ideal for extract, load, transform (ELT), and similar scenarios dependent on row inserts.
        - Query the `STREAM` object to see additional metadata columns (`METADATA$ACTION`, `METADATA$ISUPDATE`, `METADATA$ROW_ID`) for tracking changes and actions.
        - `STREAM`s have no fail-safe period or Time Travel retention. Metadata cannot be recovered if a `STREAM` is dropped.
        - For geospatial data, create `APPEND_ONLY` `STREAM`s as standard `STREAM`s cannot retrieve such data.
        """)
        

