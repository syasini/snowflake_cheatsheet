import streamlit as st
from .utils import st_code_block, make_tabs

def table_segment():
    st.header("📊 Table", help="The big spreadsheet that holds all your data and organizes it in rows and columns.")
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, truncate_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "TRUNCATE", "❄️"])
    with create_tab:
        
        st_code_block("create-table", "create or replace an existing table",
        """
        CREATE [ OR REPLACE ]
            [ { TEMPORARY | TRANSIENT } ] TABLE [ IF NOT EXISTS ] <table_name>
            ( <col_name> <col_type> )
            [ CLUSTER BY ( <expr> [ , <expr> , ... ] ) ]
        """
        )

    with alter_tab:
        
        
        st_code_block("alter-table", "rename a table",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> RENAME TO <new_table_name>
        """
        )

        st_code_block("alter-table", "swap two tables",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> SWAP WITH <target_table_name>
        """
        )

        st_code_block("alter-table", "set table properties",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> SET 
            [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
            [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
            [ ENABLE_SCHEMA_EVOLUTION = { TRUE | FALSE } ]
            [ COMMENT = '<string_literal>' ]
        """
        )

        st_code_block("alter-table", "cluster columns of an existing table",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> CLUSTER BY ( <expr> [ , <expr> , ... ] )
        """
        )

        st_code_block("alter-table", "add column to an existing table",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> ADD [ COLUMN ] <col_name> <col_type>
        """
        )

        st_code_block("alter-table", "drop column of an existing table",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> DROP [ COLUMN ] <col1_name> [, <col2_name> ... ]
        """
        )

        st_code_block("alter-table", "rename column of an existing table",
        """
        ALTER TABLE [ IF EXISTS ] <table_name> RENAME COLUMN <col_name> TO <new_col_name>
        """
        )

        

    with drop_tab:
        st_code_block("drop-table", "remove an existing table",
        """
        DROP TABLE [ IF EXISTS ] <table_name> 
        """
        )

        st_code_block("drop-table", "restore the most recent dropped table",
        """
        UNDROP TABLE <table_name> 
        """
        )

    with describe_tab:
        st_code_block("desc-table", "describe the table (e.g. show columns or values)",
        """
        DESC TABLE <table_name> 
        """
        )

    with show_tab:
        st_code_block("show-tables", "show available tables",
        """
        SHOW TABLES [ HISTORY ] [ LIKE '<pattern>' ]
                                [ IN { ACCOUNT | DATABASE [ <database_name> ] | SCHEMA [ <schema_name> ] } ]
        """
        )
        
        st_code_block("show-tables", "show available columns in tables or views",
        """
        SHOW COLUMNS [ LIKE '<pattern>' ]
                     [ IN { ACCOUNT | DATABASE [ <database_name> ] | SCHEMA [ <schema_name> ] | TABLE | [ TABLE ] <table_name> | VIEW | [ VIEW ] <view_name> } ]
        """
        )

    with truncate_tab:
        st_code_block("truncate-table", "remove all the rows from the table, but leave it intact",
        """
        TRUNCATE [ TABLE ] [ IF EXISTS ] <name>
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Use normal `TABLE`s to store persistent data for long-term use. Use `TEMPORARY` `TABLE`s for session-specific data to automatically delet it at the end of the session. Use `TRANSIENT` `TABLE`s to hold temporary or intermediate data which do not need a Fail-safe period (typically used for short-term processing or query optimization).
        - Use `CLUSTER BY` in `TABLE` creation to improve query performance by physically organizing data based on specified clustering keys. Arrange the clustering columns in order of increasing cardinality for better results. Exercise caution when clustering large tables, as it can lead to significant costs.
        - Use `CREATE TABLE <table_name> LIKE <source_table>` to create a new `TABLE` with the same structure as an existing `TABLE`, saving time and effort.
        - Use `CREATE TABLE <table_name> CLONE <source_table>` to create an exact copy of an existing `TABLE`, including data and associated objects, for testing, development, or isolating workloads without duplicating data.
        """)


