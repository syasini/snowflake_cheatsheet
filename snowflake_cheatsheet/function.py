import streamlit as st
from .utils import st_code_block, make_tabs

def function_segment():
    st.header("🪄 Function (UDF)", help="The thing that let's you do a special trick on your data.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:

        python_tab, sql_tab, java_tab, scala_tab = make_tabs(["Python", "SQL", "JavaScript", "Scala"])
        
        with python_tab:
            st_code_block("create-function", "create or replace an existing Python UDF (user-defined function)",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] FUNCTION [ IF NOT EXISTS ] <func_name> ( [ <arg_name> <arg_data_type> ] [ , ... ] )
                RETURNS { <result_data_type> | TABLE ( <col_name> <col_data_type> [ , ... ] ) }
                [ [ NOT ] NULL ]
                LANGUAGE PYTHON
                [ { CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT } ]
                RUNTIME_VERSION = <python_version>
                [ COMMENT = '<string_literal>' ]
                [ IMPORTS = ( '<stage_path_and_file_name_to_read>' [ , ... ] ) ]
                [ PACKAGES = ( '<package_name>[==<version>]' [ , ... ] ) ]
                HANDLER = '<function_name>'
                AS '<function_definition>'
            """
            )

        with sql_tab:
            st_code_block("create-function", "create or replace an existing SQL UDF (user-defined function)",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] FUNCTION <func_name> ( [ <arg_name> <arg_data_type> ] [ , ... ] )
                RETURNS { <result_data_type> | TABLE ( <col_name> <col_data_type> [ , ... ] ) }
                [ [ NOT ] NULL ]
                [ MEMOIZABLE ]
                [ COMMENT = '<string_literal>' ]
                AS '<function_definition>'
            """
            )

        with java_tab:
            st_code_block("create-function", "create or replace an existing JavaScript UDF (user-defined function)",
            """
            🤔 Have you heard of Python?
            """
            )

        with scala_tab:
            st_code_block("create-function", "create or replace an existing Scala UDF (user-defined function)",
            """
            😐 C'mon, use Python already...
            """
            )

    with alter_tab:
        
        st_code_block("alter-function", "rename the UDF (user-defined function)",
        """
        ALTER FUNCTION [ IF EXISTS ] <func_name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>
        """
        )

        st_code_block("alter-function", "modify the comment on the UDF (user-defined function)",
        """
        ALTER FUNCTION [ IF EXISTS ] <func_name> ( [ <arg_data_type> , ... ] ) SET COMMENT = '<string_literal>'
        """
        )


    with drop_tab:
        st_code_block("drop-function", "remove an existing UDF (user-defined function)",
        """
        DROP FUNCTION [ IF EXISTS ] <func_name> ( [ <arg_data_type> , ... ] )
        """
        )


    with describe_tab:
        st_code_block("desc-function", "describe the parameters of the UDF (user-defined function)",
        """
        DESC FUNCTION <func_name> ( [ <arg_data_type> ] [ , ... ] )
        """
        )

    with show_tab:
        st_code_block("show-functions", "show available UDFs (user-defined functions)",
        """
        SHOW USER FUNCTIONS [ LIKE '<pattern>' ]
                            [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Create `TEMPORARY` `FUNCTION`s to automatically drop them at the end of the session.
        - List required packages as dependencies with `package_name==version_number` (e.g. `numpy==1.25`). Omitting `version_number` uses the latest package available.
        - Use dollar signs `$$` around the `<function_definition>` for easier single quote handling within `FUNCTION`s.
        - For `UDF`s storing code in a file in a stage, the `DROP FUNCTION` command won't remove the file, so ensure the file is not removed while any other `UDF` refers to it.
        """)


