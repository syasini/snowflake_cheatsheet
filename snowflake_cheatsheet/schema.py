import streamlit as st
from .utils import st_code_block, make_tabs

def schema_segment():
    st.header("🗃 Schema", help="The individual drawers in your storage unit that help you organize your data.")
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    
    with create_tab:
        st_code_block("create-schema", "create or replace an existing schema",
        """
        CREATE [ OR REPLACE ] [ TRANSIENT ] SCHEMA [ IF NOT EXISTS ] <schema_name>
            [ CLONE <source_schema>
                    [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> } ) ] ]
            [ COMMENT = '<string_literal>' ]
        """
        )

    with alter_tab:
        
        
        st_code_block("alter-schema", "rename a schema",
        """
        ALTER SCHEMA [ IF EXISTS ] <schema_name> RENAME TO <new_schema_name>
        """
        )

        st_code_block("alter-schema", "swap two schemas",
        """
        ALTER SCHEMA [ IF EXISTS ] <schema_name> SWAP WITH <target_schema_name>
        """
        )

        st_code_block("alter-schema", "set schema properties",
        """
        ALTER SCHEMA [ IF EXISTS ] <schema_name> SET 
            [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
            [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
            [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
            [ COMMENT = '<string_literal>' ]
        """
        )

    with drop_tab:
        st_code_block("drop-schema", "remove a schema",
        """
        DROP SCHEMA [ IF EXISTS ] <schema_name> 
        """
        )

    with describe_tab:
        st_code_block("desc-schema", "describe the schema (e.g. show tables)",
        """
        DESC SCHEMA <schema_name>
        """
        )

    with show_tab:
        st_code_block("show-schemas","show available schemas",
        """
        SHOW SCHEMAS [ HISTORY ] [ LIKE '<pattern>' ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips** 
        - Set a default `SCHEMA` to simplify querying and avoid mentioning the `SCHEMA` name in every query.
        - Utilize `SCHEMA`-level access controls to provide granular security and control over who can access and modify objects within a `SCHEMA`.
        - Improve data management by organizing your data with multiple `SCHEMA`s, allowing for better organization and separation of different types of data or workloads.
        """)



