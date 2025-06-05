import streamlit as st
from .utils import st_code_block, make_tabs

def database_segment():
    st.header("🗄 Database", help="The gigantic storage drawer that holds many collections of your data together.")
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:
        
        st_code_block("create-database", "create or replace an existing database",
        """
        CREATE [ OR REPLACE ] [ TRANSIENT ] DATABASE [ IF NOT EXISTS ] <database_name>
            [ CLONE <source_db> 
                [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> } ) ] ]
            [ COMMENT = '<string_literal>' ]

        """
        )

    with alter_tab:
        
        
        st_code_block("alter-database", "rename a database",
        """
        ALTER DATABASE [ IF EXISTS ] <database_name> RENAME TO <new_db_name>
        """
        )

        st_code_block("alter-database", "swap two databases",
        """
        ALTER DATABASE [ IF EXISTS ] <database_name> SWAP WITH <target_db_name>
        """
        )

        st_code_block("alter-database", "set database properties",
        """
        ALTER DATABASE [ IF EXISTS ] <database_name> SET 
            [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
            [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
            [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
            [ COMMENT = '<string_literal>' ]
        """
        )

    with drop_tab:
        st_code_block("drop-database", "remove a database",
        """
        DROP DATABASE [ IF EXISTS ] <database_name> 
        """
        )

    with describe_tab:
        st_code_block("desc-database", "describe the database (e.g. show schemas)",
        """
        DESC DATABASE <database_name>
        """
        )

    with show_tab:
        st_code_block("show-databases", "show available databases",
        """
        SHOW DATABASES [ HISTORY ] [ LIKE '<pattern>' ]
        """
        )

    with tips_tab:
    
        st.markdown("""
        💡 **Tips**
        - Follow consistent and meaningful naming conventions for `DATABASE` objects.
        - When you create a new Snowflake database, it also generates two schemas: `PUBLIC` (the default schema) and `INFORMATION_SCHEMA` (containing views and table functions for querying metadata across objects).
        - Use a `TRANSIENT` `DATABASE` to isolate temporary data, and provide a dedicated space for intermediate results or temporary tables during specific analysis or transformation tasks.
        - Utilize zero-copy cloning using `CREATE DATABASE <name> CLONE <source_db>` for efficient, space-saving `DATABASE` copies.
        - Continuously analyze query and resource usage patterns to fine-tune `DATABASE` parameters for optimal performance and cost efficiency.
        """
        )
    


