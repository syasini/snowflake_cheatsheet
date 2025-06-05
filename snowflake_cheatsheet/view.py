import streamlit as st
from .utils import st_code_block, make_tabs

def view_segment():
    st.header("🔎 View", help="The thing that let's you see the whole or a segment of your data in a special way.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:
        
        st_code_block("create-view", "create or replace an existing view",
        """
        CREATE [ OR REPLACE ] [ TEMPORARY ] VIEW [ IF NOT EXISTS ] <view_name>
            [ ( <column_list> ) ]
            AS <select_statement>
        """
        )

    with alter_tab:
        
        
        st_code_block("alter-view", "rename a view",
        """
        ALTER VIEW [ IF EXISTS ] <old_view_name> RENAME TO <new_view_name>
        """
        )

        st_code_block("alter-view", "add comment to view",
        """
        ALTER VIEW [ IF EXISTS ] <view_name> SET COMMENT = '<string_literal>'
        """
        )

        st_code_block("alter-view", "remove comment from view",
        """
        ALTER VIEW [ IF EXISTS ] <view_name> UNSET COMMENT
        """
        )

        st_code_block("alter-view", "set table properties",
        """
        ALTER TABLE [ IF EXISTS ] <view_name> SET 
            [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
            [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
            [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
            [ COMMENT = '<string_literal>' ]
        """
        )

        st_code_block("alter-view", "add masking policy to columns of the view",
        """
        ALTER VIEW <view_name> { ALTER | MODIFY } [ COLUMN ] <col_name> SET MASKING POLICY <policy_name> [ USING ( <col_name> , cond_col_1 , ... ) ]
        """
        )

    with drop_tab:
        st_code_block("drop-view", "remove an existing view",
        """
        DROP VIEW [ IF EXISTS ] <view_name> 
        """
        )


    with describe_tab:
        st_code_block("desc-view", "describe the columns in view",
        """
        DESC VIEW <view_name> 
        """
        )

    with show_tab:
        st_code_block("show-views", "show available views",
        """
        SHOW VIEWS [ LIKE '<pattern>' ]
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
        - Use `TEMPORARY` `VIEW`s when you need a `VIEW` that exists only for the duration of a session, providing a temporary and disposable data transformation or filtering mechanism during an analysis or query execution.
        - Use `MATRIALIZED` `VIEW`s when the underlying table or the subset of rows used in the view *don't change frequently*, the view results are *frequently used*, and the *query consumes significant resources*, such as processing time, credits, or storage space for intermediate results.
        - Keep in mind that `MATERIALIZED` `VIEW`s cannot directly use `JOIN`s, including self-`JOIN`s, so consider using alternatives like `DYNAMIC TABLE`s or subqueries within `VIEW`s to achieve the desired functionality.
        - Optimize `VIEW`s by carefully designing underlying queries, minimizing unnecessary complexity, and avoiding redundant calculations.
        - Apply access control in `VIEW`s to enforce data security and privacy. Utilize Snowflake's robust access control mechanisms to grant appropriate privileges to users or roles, limiting data visibility based on business requirements and user roles.
        """)


