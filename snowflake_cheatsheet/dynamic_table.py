import streamlit as st
from .utils import st_code_block, make_tabs

def dynamic_table_segment():
    st.header("🔄 Dynamic Table", help="A special kind of table that can change its contents automatically when the data it's based on changes.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:
        
        st_code_block("create-dynamic-table", "create or replace an existing dynamic table",
        """
        CREATE [ OR REPLACE ] DYNAMIC TABLE <dyn_table_name>
            TARGET_LAG = { '<num> { seconds | minutes | hours | days }' | DOWNSTREAM }
            WAREHOUSE = <warehouse_name>
            AS <query>
            [ COMMENT = '<string_literal>' ]
        """
        )

        
    with alter_tab:
        
        st_code_block("alter-dynamic-table", "resume or suspend the dynamic table",
        """
        ALTER DYNAMIC TABLE [ IF EXISTS ] <dyn_table_name>  { SUSPEND | RESUME }
        """
        )

        st_code_block("alter-dynamic-table", "manually refresh the dynamic table",
        """
        ALTER DYNAMIC TABLE [ IF EXISTS ] <dyn_table_name> REFRESH
        """
        )

        st_code_block("alter-dynamic-table", "update the target lag or warehouse for the dynamic table",
        """
        ALTER DYNAMIC TABLE [ IF EXISTS ] <dyn_table_name> SET
            [ TARGET_LAG = { '<num> { seconds | minutes | hours | days }'  | DOWNSTREAM } ]
            [ WAREHOUSE = <warehouse_name> ]
        """
        )


    with drop_tab:
        st_code_block("drop-dynamic-table", "remove an existing dynamic table",
        """
        DROP DYNAMIC TABLE [IF EXISTS] <dyn_table_name>
        """
        )


    with describe_tab:
        st_code_block("desc-dynamic-table", "describe the columns in the dynamic table",
        """
        DESC DYNAMIC TABLE <dyn_table_name>
        """
        )

    with show_tab:
        st_code_block("show-dynamic-table", "show available dynamic tables",
        """
        SHOW DYNAMIC TABLES [ LIKE '<pattern>' ]
                            [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
                            [ STARTS WITH '<name_string>' ]
                            [ LIMIT <rows> [ FROM '<name_string>' ] ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Establish `DYNAMIC TABLE`s to create chains of data dependencies, similar to creating a directed acyclic graph (DAG) of tasks. `DYNAMIC TABLE`s are automatically updated, or "refreshed," when the underlying data changes. 
        - Avoid `INSERT`, `UPDATE`, or `DELETE` operations on `DYNAMIC TABLE`s, as changes are automated during refresh processes.
        - When your transformation relies on a *single base table*, `MATERIALIZED VIEW`s may be a better choice, as they are designed to enhance query performance transparently.
        - If your data transformation requires non-declarative, imperative code with calls to stored `PROCEDURE`s, `UDF`s, or external `FUNCTION`s, `TASK`s and `STREAM`s may be a better choice than `DYNAMIC TABLE`s.
        - Ensure your `TARGET_LAG` setting aligns with your data freshness requirements, but avoid overly frequent refreshes that may lead to unnecessary compute costs. use `DOWNSTREAM` to refresh on-demand when other dependent `DYNAMIC TABLE`s need to refresh, ensuring data consistency.
        """)
        #- Utilize dynamic tables to simplify data transformation and avoid complex pipeline management, making them ideal for materializing query results from multiple base tables in ETL processes.


