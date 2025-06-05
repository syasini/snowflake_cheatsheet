import streamlit as st
from .utils import st_code_block, make_tabs

def materialized_view_segment():
    st.header("📸 Materialized View", help="The thing that takes a snapshot of your data and stores it, kinda like a view, but more permanent.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:
        
        st_code_block("create-materialized-view", "create or replace an existing materialized view",
        """
        CREATE [ OR REPLACE ] [ TEMPORARY ] MATERIALIZED VIEW [ IF NOT EXISTS ] <mat_view_name>
            [ ( <column_list> ) ]
            [ CLUSTER BY ( <expr1> [, <expr2> ... ] ) ]
            AS <select_statement>
        """
        )

    with alter_tab:
        
        
        st_code_block("alter-materialized-view", "rename a materialized view",
        """
        ALTER MATERIALIZED VIEW [ IF EXISTS ] <old_mat_view_name> RENAME TO <new_mat_view_name>
        """
        )

        st_code_block("alter-materialized-view", "suspend or resume the materialized view",
        """
        ALTER MATERIALIZED VIEW <mat_view_name>  { SUSPEND | RESUME }
        """
        )

        st_code_block("alter-materialized-view", "add clustering to the materialized view",
        """
        ALTER MATERIALIZED VIEW <mat_view_name>  CLUSTER BY ( <expr1> [, <expr2> ... ] )
        """
        )
        
        st_code_block("alter-materialized-view", "drop, suspend, or resume clustering on the materialized view",
        """
        ALTER MATERIALIZED VIEW <mat_view_name>  { DROP CLUSTERING KEY | SUSPEND RECLUSTER | RESUME RECLUSTER }
        """
        )

        st_code_block("alter-materialized-view", "add comment to materialized view",
        """
        ALTER MATERIALIZED VIEW [ IF EXISTS ] <mat_view_name> SET COMMENT = '<string_literal>'
        """
        )

        st_code_block("alter-materialized-view", "remove comment from materialized view",
        """
        ALTER MATERIALIZED VIEW [ IF EXISTS ] <mat_view_name> UNSET COMMENT
        """
        )


        

    with drop_tab:
        st_code_block("drop-materialized-view", "remove an existing materialized view",
        """
        DROP MATERIALIZED VIEW [ IF EXISTS ] <mat_view_name> 
        """
        )


    with describe_tab:
        st_code_block("desc-materialized-view", "describe the columns in materialized view",
        """
        DESC MATERIALIZED VIEW <mat_view_name> 
        """
        )

    with show_tab:
        st_code_block("show-materialized-views", "show available materialized views",
        """
        SHOW MATERIALIZED VIEWS [ LIKE '<pattern>' ]
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

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - `MATERIALIZED VIEW`s are beneficial when the query results are relatively small compared to the base table, contain data requiring extensive processing, or involve external tables with slower performance.
        - Choose to create a `MATERIALIZED VIEW` when *query results are stable*, *used frequently*, and *resource-intensive*, or when saving processing time, and storage costs matter.
        - Opt for a regular `VIEW` when query results change often, aren't frequently used, or the query is not resource-intensive, and it's not costly to re-run.
        - Creating a `MATERIALIZED VIEW` incurs costs, and the decision to use them should be evaluated against the potential performance gains.
        - `MATERIALIZED VIEW`s are limited to querying a single table and cannot support `JOIN`s, including self-`JOIN`s. They are also unable to query `MATERIALIZED VIEW`s, regular `VIEW`s, or user-defined `FUNCTION`s (`UDF`). See the full list of limitations [here](https://docs.snowflake.com/en/user-guide/views-materialized).
        """)


