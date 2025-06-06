import streamlit as st
from .utils import st_code_block, make_tabs

def data_manipulation_segment():
    st.header("🌀 Data Manipulation", help="The things you do to add or change data in the tables.")
    
    insert_tab, update_tab, merge_tab, delete_tab, tips_tab = \
        make_tabs(["INSERT", "UPDATE", "MERGE", "DELETE", "❄️"])
    
    with insert_tab:
        st_code_block("insert", "insert or replace data into a table from explicit values ",
        """
        INSERT [ OVERWRITE ] INTO <target_table> [ ( <target_col_name> [ , ... ] ) ]
            VALUES ( { <value> | DEFAULT | NULL } [ , ... ] ) [ , ( ... ) ]

        """
        )

        st_code_block("insert", "insert or replace data into a table from a select query ",
        """
        INSERT [ OVERWRITE ] INTO <target_table> [ ( <target_col_name> [ , ... ] ) ]
            < query > 
        """
        )

    with update_tab:
        st_code_block("update", "update specific rows and columns in an existing table",
        """
        UPDATE <target_table>
            SET <col_name> = <value> [ , <col_name> = <value> , ... ]
                [ FROM <additional_tables> ]
                [ WHERE <condition> ]
        
        """
        )

        st_code_block("update", "prevent non-deterministic updates on multi-joined rows",
        """
        ALTER SESSION SET ERROR_ON_NONDETERMINISTIC_UPDATE=TRUE
        """
        )


    with merge_tab:
        
        st_code_block("merge", "insert, update, and delete values in a table based on the given conditions",
        """
        MERGE INTO <target_table> 
            USING <source> ON <join_expr> { 
                WHEN MATCHED [ AND <case_predicate> ] THEN { UPDATE SET <col_name> = <expr> [ , <col_name2> = <expr2> ... ] | DELETE } [ ... ] |
                WHEN NOT MATCHED [ AND <case_predicate> ] THEN INSERT [ ( <col_name> [ , ... ] ) ] VALUES ( <expr> [ , ... ] )
            }
        """
        )

        st_code_block("https://docs.snowflake.com/en/sql-reference/parameters#label-error-on-nondeterministic-merge", "prevent non-deterministic merge on multi-joined rows",
        """
        ALTER SESSION SET ERROR_ON_NONDETERMINISTIC_MERGE=TRUE
        """
        )



    with delete_tab:
        st_code_block("delete", "remove rows from a table based on the given condtions", 
        """
        DELETE FROM <table_name>
            [ USING <additional_table_or_query> [, <additional_table_or_query> ] ]
            [ WHERE <condition> ]
        """
        )



    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Ensure that the data types of the values you're inserting in multi-row `INSERT`s are consistent across the rows, as the data type of the first row is used as a guide.
        - When `INSERT`ing `JSON` data into a `VARIANT` column, you can use the `PARSE_JSON` function to convert `JSON` strings into `VARIANT` data for insertion.
        - When using a `FROM` clause to `JOIN` multiple tables, be aware of the possibility of multi-joined rows. These occur when a target row matches more than one row in the joined table. The `ERROR_ON_NONDETERMINISTIC_UPDATE` session parameter controls how updates are handled in such cases.
        - When `ERROR_ON_NONDETERMINISTIC_UPDATE` is `FALSE`, updates proceed without errors but may be nondeterministic. When set to `TRUE`, errors signal nondeterministic updates, which can be addressed by using 1-to-1 joins to ensure specific row updates.
        - When the `MERGE` statement joins a target row to multiple source rows, it can result in nondeterministic behavior for `UPDATE` and `DELETE` operations, unless you use `ERROR_ON_NONDETERMINISTIC_MERGE` or ensure deterministic conditions.
        - To avoid nondeterministic behavior in `MERGE`s, apply `GROUP BY` in the source clause to guarantee that each target row joins against only one source row.
        """)


left_column_defaults = [
    "🗄 database", 
    "🗃 schema",
    "📊 table", 
    "👁️ view",
    "📸 materialized view",
    "🔄 dynamic table", 
    "📋 task",
    "🌊 stream",
    "🚨 alert",
    ]

right_column_defaults = [
    "🚉 stage",
    "🚚 data loading",
    "🌀 data manipulation",
    "🪄 function", 
    "🪜 procedure",
    "🚰 pipe",
    ]

all_segments = left_column_defaults + right_column_defaults

