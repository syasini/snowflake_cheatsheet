import streamlit as st
from .utils import st_code_block, make_tabs

def procedure_segment():
    st.header("🪜 Procedure", help="The thing that follows a set of steps to transform your data.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:

        python_tab, sql_tab, java_tab, scala_tab = make_tabs(["Python", "SQL", "JavaScript", "Scala"])
        
        with python_tab:

            in_line_tab, on_stage_tab = make_tabs(["in-line", "on stage"])
            with in_line_tab:
                st_code_block("create-procedure", "create or replace an existing in-line Python stored procedure",
                """
                CREATE [ OR REPLACE ] PROCEDURE <procedure_name> ( [ <arg_name> <arg_data_type> ] [ , ... ] )
                    RETURNS { <result_data_type> [ [ NOT ] NULL ] | TABLE ( [ <col_name> <col_data_type> [ , ... ] ] ) }
                    LANGUAGE PYTHON
                    RUNTIME_VERSION = '<python_version>'
                    PACKAGES = ( 'snowflake-snowpark-python[==<version>]'[, '<package_name>[==<version>]' ... ])
                    [ IMPORTS = ( '<stage_path_and_file_name_to_read>' [, '<stage_path_and_file_name_to_read>' ...] ) ]
                    HANDLER = '<function_name>'
                    [ COMMENT = '<string_literal>' ]
                    AS '<procedure_definition>'
                """
                )

            with on_stage_tab:
                st_code_block("create-procedure", "create or replace an existing Python stored procedure on stage",
                """
                CREATE [ OR REPLACE ] PROCEDURE <procedure_name> ( [ <arg_name> <arg_data_type> ] [ , ... ] )
                    RETURNS { <result_data_type> [ [ NOT ] NULL ] | TABLE ( [ <col_name> <col_data_type> [ , ... ] ] ) }
                    LANGUAGE PYTHON
                    RUNTIME_VERSION = '<python_version>'
                    PACKAGES = ( 'snowflake-snowpark-python[==<version>]'[, '<package_name>[==<version>]' ... ])
                    [ IMPORTS = ( '<stage_path_and_file_name_to_read>' [, '<stage_path_and_file_name_to_read>' ...] ) ]
                    HANDLER = '<module_file_name>.<function_name>'
                    [ COMMENT = '<string_literal>' ]
                """
                )

        with sql_tab:
            st_code_block("create-procedure", "create or replace an existing SQL procedure",
            """
            CREATE [ OR REPLACE ] PROCEDURE <procedure_name> ( [ <arg_name> <arg_data_type> ] [ , ... ] )
                RETURNS { <result_data_type> | TABLE ( [ <col_name> <col_data_type> [ , ... ] ] ) }
                [ NOT NULL ]
                LANGUAGE SQL
                [ COMMENT = '<string_literal>' ]
                [ EXECUTE AS { CALLER | OWNER } ]
                AS $$
                BEGIN
                <procedure_definition>;
                END
                $$
            """
            )

        with java_tab:
            st_code_block("create-procedure", "create or replace an existing JavaScript procedure",
            """
            🤔 Have you heard of Python?
            """
            )

        with scala_tab:
            st_code_block("create-procedure", "create or replace an existing Scala procedure",
            """
            😐 C'mon, use Python already...
            """
            )

    with alter_tab:
        
        st_code_block("alter-procedure", "rename the procedure",
        """
        ALTER PROCEDURE [ IF EXISTS ] <procedure_name> ( [ <arg_data_type> , ... ] ) RENAME TO <new_name>
        """
        )

        st_code_block("alter-procedure", "modify the comment on the procedure",
        """
        ALTER FUNCTION [ IF EXISTS ] <procedure_name> ( [ <arg_data_type> , ... ] ) SET COMMENT = '<string_literal>'
        """
        )

        st_code_block("alter-procedure", "modify the executer privilege of the procedure",
        """
        ALTER FUNCTION [ IF EXISTS ] <procedure_name> ( [ <arg_data_type> , ... ] ) EXECUTE AS { CALLER | OWNER }
        """
        )


    with drop_tab:
        st_code_block("drop-procedure", "remove an existing procedure",
        """
        DROP PROCEDURE [ IF EXISTS ] <procedure_name> ( [ <arg_data_type> , ... ] )
        """
        )


    with describe_tab:
        st_code_block("desc-procedure", "describe the parameters of the procedure",
        """
        DESC PROCEDURE <procedure_name> ( [ <arg_data_type> ] [ , ... ] )
        """
        )

    with show_tab:
        st_code_block("show-procedures", "show available procedures",
        """
        SHOW PROCEDURE [ LIKE '<pattern>' ]
                       [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Create anonymous `PROCEDURE`s using `WITH <name> AS PROCEDURE CALL <name>` instead of stored `PROCEDURE`s. This allows you to create and call `PROCEDURE`s without requiring `CREATE PROCEDURE` schema privileges.
        - When creating `PROCEDURE`s in SnowSQL or the Classic Console, remember to use string literal delimiters (`'` or `$$`) around the `PROCEDURE` definition. This ensures that the `PROCEDURE` is correctly parsed and executed.
        - Take advantage of overloading to create `PROCEDURE`s with the same name but different parameter counts or data types. This provides flexibility and allows you to use the same `PROCEDURE` name for different functionalities.
        - Keep in mind that stored `PROCEDURE`s are not atomic. If one statement within a `PROCEDURE` fails, other statements in the same `PROCEDURE` won't necessarily be rolled back automatically. Consider transaction management for more precise control over the `PROCEDURE`'s behavior.
        - Choose the appropriate `EXECUTE AS` option when creating `PROCEDURE`s to define the execution privileges. Use `EXECUTE AS CALLER` for `PROCEDURE`s executing with the caller's rights or `EXECUTE AS OWNER` for `PROCEDURE`s executing with the owner's rights. By default, `PROCEDURE`s run as owner's rights.
        - Consider using a naming convention for stored `PROCEDURE`s to distinguish between caller's rights and owner's rights `PROCEDURE`s in organizations with a mix of both.
        """)


