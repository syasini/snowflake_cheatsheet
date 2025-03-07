## IMPORTANT CALL OUT 
## ==================
## As you may have noticed, this script can use a lot of refactoring 
## and should be broken down into multiple modules for better readability 
## and easier maintanance. If you are interested in helping out,
## please open an issue/PR and contribute to the project. 
## The community will greatly appreciate your help and contribution! 

import streamlit as st

st.set_page_config(page_title='Snowflake', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)

st.image("./logo/ungifted_amateur_v5.png", use_container_width=True )

st.snow()

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    with st.expander("**📖 How to Use This Cheat Sheet**"):
        st.markdown("""
                    However you like! 🤷🏻

                    But here's my recommendation:

                    In a typical Snowflake work session, you might find yourself juggling various commands such as 
                    cloning a database and schema, creating new tables or views, rummaging through files on a stage, keeping tabs on Snowpipe, wrangling data through manual copying, insertion, or updating, etc, etc ... the list is long!

                    Now, keeping the precise syntax of all these commands at your fingertips, especially for the less-frequently-used ones, can be quite a challenge. 
                    I recommend keeping this cheat sheet open in a tab while you work. This way, you can swiftly refer to the provided code snippets and easily adapt them to your specific tasks. 
                    To keep things streamlit 🎈... sorry, I mean streamlined, I have removed options and arguments that are not frequently used in each command. 
                    However, keep in mind that I have cherry-picked the options based on my personal workflow experience which may not necessarily align with yours.     

                    Within each segment, there's a special treat ❄️: a bonus section with top tips to elevate your Snowflake skills.  
                    I suggest that whenever you are using a command for the first time, spend a few minutes reading the tips and hopefully pick up something new.
                    """)
        
        st.info("""
                This guide is not intended to be a replacement for the official [Snowflake documentation](https://docs.snowflake.com/) (which is fantastic by the way!). 
                    For a comprehensive reference of objects and methods, make sure to explore the official documentation.
                """)
        
        st.markdown("""
                    If you happen to spot any errors or have suggestions for improving the descriptions or tips, please don't hesitate to reach out to me directly [here](https://www.linkedin.com/in/siavash-yasini/), or open an [issue](https://github.com/syasini/snowflake_cheatsheet/issues/new) on the GitHub page. Your feedback is invaluable—and relied upon—in keeping this guide accurate and useful.

                    👈 Don't forget to check the sidebar for additional info and layout options!

                    Now, go build something awesome on Snowflake! 🚀

                    """)

st.sidebar.title("❄️ Snowflake Cheatsheet 📄")
st.sidebar.caption("Made by an [Ungifted Amateur](https://www.linkedin.com/in/siavash-yasini/)")

st.sidebar.caption("Check out the accompanying Snowflake tutorial [here](https://medium.com/snowflake/the-ungifted-amateurs-guide-to-snowflake-449284e4bd72).")

with st.sidebar.expander("See My Other Streamlit Apps"):
    st.caption("streamliTissues: [App](https://tissues.streamlit.app/) 🎈")
    st.caption("Sophisticated Palette: [App](https://sophisticated-palette.streamlit.app/) 🎈,  [Blog Post](https://blog.streamlit.io/create-a-color-palette-from-any-image/) 📝")
    st.caption("Wordler: [App](https://wordler.streamlit.app/) 🎈,  [Blog Post](https://blog.streamlit.io/the-ultimate-wordle-cheat-sheet/) 📝")
    st.caption("Koffee of the World: [App](https://koffee.streamlit.app/) 🎈")
   
with st.sidebar.expander("ℹ️ **Latest Snowflake Release Notes**"):
    st.markdown("""Stay frosty and keep up with the coolest updates on the Snowflake website [here](https://docs.snowflake.com/en/release-notes/new-features).""")
cols = st.columns(2)

def st_code_block(url, caption=None, code=None):
    # prefill the http address for the sql-reference url
    if not url.startswith("https"):
        url = f"https://docs.snowflake.com/en/sql-reference/sql/{url}"
    st.caption(f"[☁️]({url}) {caption}")
    st.code(code, language="sql")

def database_segment():
    st.header("🗄 Database", help="The gigantic storage drawer that holds many collections of your data together.")
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
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
    


def schema_segment():
    st.header("🗃 Schema", help="The individual drawers in your storage unit that help you organize your data.")
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    
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



def table_segment():
    st.header("📊 Table", help="The big spreadsheet that holds all your data and organizes it in rows and columns.")
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, truncate_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "TRUNCATE", "❄️"])
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


def view_segment():
    st.header("🔎 View", help="The thing that let's you see the whole or a segment of your data in a special way.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
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


def materialized_view_segment():
    st.header("📸 Materialized View", help="The thing that takes a snapshot of your data and stores it, kinda like a view, but more permanent.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
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


def stage_segment():
    st.header("🚉 Stage", help="The platform where the data sits before moving in and out of Snowflake.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, list_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "LIST", "❄️"])
    
    with create_tab:
        
        st_code_block("create-stage", "create or replace an internal stage",
        """
        CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <internal_stage_name>
            [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                  [ REFRESH_ON_CREATE =  { TRUE | FALSE } ] ) ]
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT }) ]
        """
        )

        s3_tab, azure_tab, gcp_tab = st.tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("create-stage", "create or replace an external stage for Amazon S3",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <external_stage_name>
                [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                    [ REFRESH_ON_CREATE =  { TRUE | FALSE } ]
                    [ AUTO_REFRESH = { TRUE | FALSE } ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT })  ]
            """
            )

        with azure_tab:
            st_code_block("create-stage", "create or replace an external stage for Microsoft Azure",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <external_stage_name>
                [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                    [ REFRESH_ON_CREATE =  { TRUE | FALSE } ]
                    [ AUTO_REFRESH = { TRUE | FALSE } ] ) ]
                    [ NOTIFICATION_INTEGRATION = '<notification_integration_name>' ] 
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT })  ]
            """
            )

        with gcp_tab:
            st_code_block("create-stage", "create or replace an external stage for Google Cloud Storage",
            """
            CREATE [ OR REPLACE ] [ TEMPORARY ] STAGE [ IF NOT EXISTS ] <external_stage_name>
                [ DIRECTORY = ( ENABLE = { TRUE | FALSE }
                    [ REFRESH_ON_CREATE =  { TRUE | FALSE } ]
                    [ AUTO_REFRESH = { TRUE | FALSE } ] ) ]
                    [ NOTIFICATION_INTEGRATION = '<notification_integration_name>' ] 
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT })  ]
            """
            )

    with alter_tab:
        
        
        st_code_block("alter-stage", "rename a stage",
        """
        ALTER STAGE [ IF EXISTS ] <name> RENAME TO <new_stage_name>
        """
        )

        st_code_block("alter-stage", "change directory settings for the stage",
        """
        ALTER STAGE [ IF EXISTS ] <name> SET DIRECTORY = ( { ENABLE = TRUE | FALSE } )

        ALTER STAGE [ IF EXISTS ] <name> REFRESH [ SUBPATH = '<relative-path>' ]
        """
        )

        st_code_block("alter-stage", "change internal stage parameters",
        """
        ALTER STAGE [ IF EXISTS ] <name> SET {
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
            [ COMMENT = '<string_literal>' ] 
        }
        """
        )


        s3_tab, azure_tab, gcp_tab = st.tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("alter-stage", "change external stage parameters for Amazon S3",
            """
            ALTER STAGE [ IF EXISTS ] <name> SET {
                [ URL = 's3://<bucket>[/<path>/]' ]
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( {  { AWS_KEY_ID = '<string>' AWS_SECRET_KEY = '<string>' [ AWS_TOKEN = '<string>' ] } | AWS_ROLE = '<string>'  } ) } ]
                [ ENCRYPTION = ( [ TYPE = 'AWS_CSE' ] [ MASTER_KEY = '<string>' ] |
                                 [ TYPE = 'AWS_SSE_S3' ] |
                                 [ TYPE = 'AWS_SSE_KMS' [ KMS_KEY_ID = '<string>' ] |
                                 [ TYPE = 'NONE' ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
                [ COMMENT = '<string_literal>' ] }
            }
            """
            )

        with azure_tab:
            st_code_block("alter-stage", "change external stage parameters for Microsoft Azure",
            """
            ALTER STAGE [ IF EXISTS ] <name> SET {
                [ URL = 'azure://<account>.blob.core.windows.net/<container>[/<path>/]' ]
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( [ AZURE_SAS_TOKEN = '<string>' ] ) } ]
                [ ENCRYPTION = ( [ TYPE = { 'AZURE_CSE' | 'NONE' } ] [ MASTER_KEY = '<string>' ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
                [ COMMENT = '<string_literal>' ] }
            }
            """
            )

        with gcp_tab:
            st_code_block("alter-stage", "change external stage parameters for Google Cloud Storage",
            """
            ALTER STAGE [ IF EXISTS ] <name> SET {
                [ URL = 'gcs://<bucket>[/<path>/]' ]
                [ STORAGE_INTEGRATION = <integration_name> } ]
                [ ENCRYPTION = ( [ TYPE = 'GCS_SSE_KMS' ] [ KMS_KEY_ID = '<string>' ] | [ TYPE = 'NONE' ] ) ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ COPY_OPTIONS = ( ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } )  ]
                [ COMMENT = '<string_literal>' ] }
            }
            """
            )


    with drop_tab:
        st_code_block("drop-stage", "remove an existing stage",
        """
        DROP STAGE [ IF EXISTS ] <name> 
        """
        )


    with describe_tab:
        st_code_block("desc-stage", "describe the properties of the stage (e.g. file format, copy, location)",
        """
        DESC STAGE <name> 
        """
        )

    with show_tab:
        st_code_block("show-stages", "show available stages",
        """
        SHOW STAGES [ LIKE '<pattern>' ]
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

    with list_tab:
        st_code_block("list", "return a list of files that have been staged",
        """
        LIST { 
                @[<namespace>.]<int_stage_name>[/<path>]
                | @[<namespace>.]%<table_name>[/<path>]
                | @~[/<path>]
             } 
             [ PATTERN = '<regex_pattern>' ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - See [this guide](https://docs.snowflake.com/en/user-guide/data-load-s3-config) for various options to configure secure access to a private Amazon S3 bucket. 
        - Use `DIRECTORY` tables to efficiently store and catalog staged files, allowing seamless querying to retrieve URLs for the staged files, along with other essential metadata.
        - Use `EXTERNAL` tables when you want to access and query data that resides in external cloud storage (e.g. AWS S3) without copying or moving the data into Snowflake.
        """)

def pipe_segment():
    st.header("🚰 Pipe", help="The magic portal that helps move data into Snowflake tables.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, status_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "PIPE_STATUS", "❄️"])
    with create_tab:

        s3_tab, azure_tab, gcp_tab = st.tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("create-pipe", "create or replace a pipe from Amazon S3",
            """
            CREATE [ OR REPLACE ] PIPE [ IF NOT EXISTS ] <pipe_name>
                [ AUTO_INGEST = [ TRUE | FALSE ] ]
                [ ERROR_INTEGRATION = <integration_name> ]
                [ AWS_SNS_TOPIC = '<string>' ]
                [ COMMENT = '<string_literal>' ]
                AS <copy_statement>
            """
            )

        with azure_tab:
            st_code_block("create-pipe", "create or replace a pipe from Microsoft Azure",
            """
            CREATE [ OR REPLACE ] PIPE [ IF NOT EXISTS ] <pipe_name>
                [ AUTO_INGEST = [ TRUE | FALSE ] ]
                [ ERROR_INTEGRATION = <integration_name> ]
                [ INTEGRATION = '<string>' ]
                [ COMMENT = '<string_literal>' ]
                AS <copy_statement>
            """
            )

        with gcp_tab:
            st_code_block("create-pipe", "create or replace a pipe from Google Cloud Storage",
            """
            CREATE [ OR REPLACE ] PIPE [ IF NOT EXISTS ] <pipe_name>
                [ AUTO_INGEST = [ TRUE | FALSE ] ]
                [ ERROR_INTEGRATION = <integration_name> ]
                [ INTEGRATION = '<string>' ]
                [ COMMENT = '<string_literal>' ]
                AS <copy_statement>
            """
            )

    with alter_tab:
        
        
        st_code_block("alter-pipe", "change the properties of an existing pipe",
        """
        ALTER PIPE [ IF EXISTS ] <pipe_name> SET { PIPE_EXECUTION_PAUSED = { TRUE | FALSE }
            [ COMMENT = '<string_literal>' ] }
        """
        )

        st_code_block("alter-pipe", "refresh the pipe to copy staged files that were not loaded",
        """
        ALTER PIPE [ IF EXISTS ] <pipe_name> REFRESH { [ PREFIX = '<path>' ] [ MODIFIED_AFTER = <start_time> ] }
        """
        )


    with drop_tab:
        st_code_block("drop-pipe", "remove an existing pipe",
        """
        DROP PIPE [ IF EXISTS ] <pipe_name>
        """
        )


    with describe_tab:
        st_code_block("desc-pipe", "describe the properties of the pipe (e.g. create date, definition, pattern)",
        """
        DESC PIPE <pipe_name> 
        """
        )

    with show_tab:
        st_code_block("show-pipes", "show available pipes",
        """
        SHOW PIPES [ LIKE '<pattern>' ]
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

    with status_tab:
        st_code_block("https://docs.snowflake.com/en/sql-reference/functions/system_pipe_status", "return the current status of the pipe",
        """
        SELECT SYSTEM$PIPE_STATUS( '<pipe_name>' )
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Use `PIPE`s to efficiently stream and ingest data in real-time from external sources into Snowflake, providing a continuous flow of data updates without the need for manual data loading.
        - Use `PIPE`s for real-time data ingestion from streaming sources, `COPY INTO` for batch loading data from files in cloud storage, and `EXTERNAL TABLE`s for querying data residing in external cloud storage without copying it into Snowflake.
        - Enable `AUTO_INGEST` to automatically detect and load new data files into Snowflake through Snowpipe, ensuring continuous data ingestion from external sources.
        - Use the `ALTER PIPE <name> REFRESH` command to manually trigger loading of staged data files into the Snowpipe ingest queue for a specific pipe. It helps resolve data loading issues and allows you to load specific subsets of data when needed.
        - Remember that `REFRESH` can only load data files staged within the last 7 days and checks load history for both the pipe and target table, queueing files not previously loaded by the same pipe or `COPY INTO <table>` statement. Use it for short-term issue resolution, not for regular use.
        """)


def data_loading_segment():
    st.header("🚚 Loading Data", help="The thing you do to dump data into Snowflake Tables.")
    
    standard_tab, transform_tab, tips_tab = \
        st.tabs(["COPY INTO (standard)", "COPY INTO (with transformation)", "❄️"])
    with standard_tab:

        st_code_block("copy-into-table", "copy data from internal or external stage",
        """
        COPY INTO [<namespace>.]<table_name>
            FROM {@[<namespace>.]<stage_name>[/<path>]
                | @[<namespace>.]%<table_name>[/<path>]
                | @~[/<path>]
            }
            [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
            [ PATTERN = '<regex_pattern>' ]
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
            [ FORCE = { TRUE | FALSE } ]
            [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
        """
        )

        s3_tab, azure_tab, gcp_tab = st.tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("copy-into-table", "copy data from Amazon S3 directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM 's3://<bucket>[/<path>]'
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( {  { AWS_KEY_ID = '<string>' AWS_SECRET_KEY = '<string>' [ AWS_TOKEN = '<string>' ] } } ) } ]
                [ ENCRYPTION = ( [ TYPE = 'AWS_CSE' ] [ MASTER_KEY = '<string>' ] |
                                 [ TYPE = 'AWS_SSE_S3' ] |
                                 [ TYPE = 'AWS_SSE_KMS' [ KMS_KEY_ID = '<string>' ] ] |
                                 [ TYPE = 'NONE' ] ) ]
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
                [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
            """
            )

        with azure_tab:
            st_code_block("copy-into-table", "copy data from Azure directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM 'azure://<account>.blob.core.windows.net/<container>[/<path>]'
                [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( [ AZURE_SAS_TOKEN = '<string>' ] ) } ]
                [ ENCRYPTION = ( [ TYPE = { 'AZURE_CSE' | 'NONE' } ] [ MASTER_KEY = '<string>' ] ) ]
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
                [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
            """
            )

        with gcp_tab:
            st_code_block("copy-into-table", "copy data from Google Cloud Storage directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM 'gcs://<bucket>[/<path>]'
                [ STORAGE_INTEGRATION = <integration_name> ]
                [ ENCRYPTION = ( [ TYPE = 'GCS_SSE_KMS' ] [ KMS_KEY_ID = '<string>' ] | [ TYPE = 'NONE' ] ) ]
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
                [ VALIDATION_MODE = RETURN_<n>_ROWS | RETURN_ERRORS | RETURN_ALL_ERRORS ]
            """
            )
    
    with transform_tab:

        st_code_block("copy-into-table", "copy data from internal or external stage",
        """
        COPY INTO [<namespace>.]<table_name>
            FROM ( 
                SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                FROM {@[<namespace>.]<stage_name>[/<path>]
                    | @[<namespace>.]%<table_name>[/<path>]
                    | @~[/<path>]
                }
            )
            [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
            [ PATTERN = '<regex_pattern>' ]
            [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
            [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
            [ FORCE = { TRUE | FALSE } ]
            
        """
        )

        s3_tab, azure_tab, gcp_tab = st.tabs(["Amazon S3", "Microsoft Azure", "Google Cloud Storage"])
        with s3_tab:
            st_code_block("copy-into-table", "copy data from Amazon S3 directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM ( 
                    SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                    FROM 's3://<bucket>[/<path>]'
                    [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( {  { AWS_KEY_ID = '<string>' AWS_SECRET_KEY = '<string>' [ AWS_TOKEN = '<string>' ] } } ) } ]
                    [ ENCRYPTION = ( [ TYPE = 'AWS_CSE' ] [ MASTER_KEY = '<string>' ] |
                                    [ TYPE = 'AWS_SSE_S3' ] |
                                    [ TYPE = 'AWS_SSE_KMS' [ KMS_KEY_ID = '<string>' ] ] |
                                    [ TYPE = 'NONE' ] ) ]
                )
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
            """
            )

        with azure_tab:
            st_code_block("copy-into-table", "copy data from Azure directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM (
                    SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                    FROM 'azure://<account>.blob.core.windows.net/<container>[/<path>]'
                    [ { STORAGE_INTEGRATION = <integration_name> } | { CREDENTIALS = ( [ AZURE_SAS_TOKEN = '<string>' ] ) } ]
                    [ ENCRYPTION = ( [ TYPE = { 'AZURE_CSE' | 'NONE' } ] [ MASTER_KEY = '<string>' ] ) ]
                )
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
            """
            )

        with gcp_tab:
            st_code_block("copy-into-table", "copy data from Google Cloud Storage directly",
            """
            COPY INTO [<namespace>.]<table_name>
                FROM ( 
                    SELECT [<alias>.]$<file_col_num>[.<element>] [ , [<alias>.]$<file_col_num>[.<element>] ... ]
                    FROM 'gcs://<bucket>[/<path>]'
                    [ STORAGE_INTEGRATION = <integration_name> ]
                    [ ENCRYPTION = ( [ TYPE = 'GCS_SSE_KMS' ] [ KMS_KEY_ID = '<string>' ] | [ TYPE = 'NONE' ] ) ]
                )
                [ FILES = ( '<file_name>' [ , '<file_name>' ] [ , ... ] ) ]
                [ PATTERN = '<regex_pattern>' ]
                [ FILE_FORMAT = ( TYPE = { CSV | JSON | AVRO | ORC | PARQUET | XML } ) ]
                [ ON_ERROR = { CONTINUE | SKIP_FILE | ABORT_STATEMENT } ]
                [ FORCE = { TRUE | FALSE } ]
            """
            )

    with tips_tab:
        st.markdown("💡 **Tips**")
    
        st.markdown("- Use `COPY INTO` when you have static files or batch data that needs to be loaded into Snowflake. `COPY INTO` provides more control and flexibility over the loading process compared to pipes.")
        st.markdown("- Use `PIPE`s when you need to ingest real-time or near real-time streaming data into Snowflake (see the 🚰 **Pipe**s segment).")
        st.markdown("- Distribute your data across multiple files or use file compression to take advantage of parallel loading and improve loading speed.")
        st.markdown("- By default `COPY_INTO` will not load files that have already been transfered within *the past 64 days*. Use `FORCE = TRUE` to enforce loading all files regardless of loading history. Note the this will potentially duplicate data in the target table.")
    

def task_segment():
    st.header("📋 Task", help="The todo list that tells Snowflake what to do with the data and when to do them.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:
        
        st_code_block("create-task",  "create or replace an existing task",
        """
        CREATE [ OR REPLACE ] TASK [ IF NOT EXISTS ] <task_name>
            [ WAREHOUSE = <string> ]
            [ SCHEDULE = '{ <num> MINUTE | USING CRON <expr> <time_zone> }' ]
            [ ALLOW_OVERLAPPING_EXECUTION = TRUE | FALSE ]
            [ <session_parameter> = <value> [ , <session_parameter> = <value> ... ] ]
            [ USER_TASK_TIMEOUT_MS = <num> ]
            [ SUSPEND_TASK_AFTER_NUM_FAILURES = <num> ]
            [ COMMENT = '<string_literal>' ]
            [ AFTER <string> [ , <string> , ... ] ]
            [ WHEN <boolean_expr> ]
        AS
            { <sql> | <stored_procedure> }
        """
        )

        with st.expander("CRON Expressions"):
            st.code("""
                # __________ minute (0-59)
                # | ________ hour (0-23)
                # | | ______ day of month (1-31, or L)
                # | | | ____ month (1-12, JAN-DEC)
                # | | | | _ day of week (0-6, SUN-SAT, or L)
                # | | | | |
                # | | | | |
                * * * * *        
            """)

    with alter_tab:
        
        
        st_code_block("alter-task", "resume or suspend a task",
        """
        ALTER TASK [ IF EXISTS ] <task_name> { RESUME | SUSPEND }
        """
        )

        st_code_block("alter-task", "change the location in the [DAG of tasks](https://docs.snowflake.com/en/user-guide/tasks-intro#label-task-dag)",
        """
        ALTER TASK [ IF EXISTS ] <task_name> REMOVE AFTER <string> [ , <string> , ... ] | ADD AFTER <string> [ , <string> , ... ]
        """
        )

        st_code_block("alter-task", "change the task parameters",
        """
        ALTER TASK [ IF EXISTS ] <task_name> SET
            [ WAREHOUSE = <string> ]
            [ SCHEDULE = '{ <number> MINUTE | USING CRON <expr> <time_zone> }' ]
            [ ALLOW_OVERLAPPING_EXECUTION = TRUE | FALSE ]
            [ <session_parameter> = <value> [ , <session_parameter> = <value> ... ] ]
            [ USER_TASK_TIMEOUT_MS = <num> ]
            [ SUSPEND_TASK_AFTER_NUM_FAILURES = <num> ]
            [ COMMENT = <string> ]
        """
        )

        st_code_block("alter-task", "modify the task definition",
        """
        ALTER TASK [ IF EXISTS ] <task_name> MODIFY AS <sql>
        """
        )


    with drop_tab:
        st_code_block("drop-task", "remove an existing task",
        """
        DROP TASK [ IF EXISTS ] <task_name>
        """
        )


    with describe_tab:
        st_code_block("desc-task", "describe the columns in the task",
        """
        DESC TASK <task_name> 
        """
        )

    with show_tab:
        st_code_block("show-tasks", "show available tasks",
        """
        SHOW TASKS  [ LIKE '<pattern>' ]
                    [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
                    [ STARTS WITH '<name_string>' ]
                    [ ROOT ONLY ]
                    [ LIMIT <rows> [ FROM '<name_string>' ] ]
        """
        )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Thoroughly test SQL statements and stored procedures before creating a `TASK` for automation.
        - Serverless `TASK`s cannot use `UDF`s with Java or Python code or call Scala (using Snowpark) stored `PROCEDURE`s. Omit the `WAREHOUSE` parameter to create serverless `TASK`s that use Snowflake-managed resources.
        - Schedule is required for standalone or root `TASK`s in a DAG; child `TASK`s in a DAG cannot have specified schedules.
        - After creating a `TASK`, use `ALTER TASK <name> RESUME` for execution based on defined parameters. Accounts have a limit of 10,000 resumed `TASK`s.
        - Query `TASK` usage history with `TASK_HISTORY()` table function for the entire account or specific `TASK`s within a specified date range.
        """)
        st.code("""
        SELECT * 
        FROM TABLE(information_schema.TASK_HISTORY())
        ORDER BY scheduled_time;
        """,
        language = "sql")


def stream_segment():
    st.header("🌊 Stream", help="The thing that keeps track of changes in your data.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
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
        

def function_segment():
    st.header("🪄 Function (UDF)", help="The thing that let's you do a special trick on your data.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:

        python_tab, sql_tab, java_tab, scala_tab = st.tabs(["Python", "SQL", "JavaScript", "Scala"])
        
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


def procedure_segment():
    st.header("🪜 Procedure", help="The thing that follows a set of steps to transform your data.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
    with create_tab:

        python_tab, sql_tab, java_tab, scala_tab = st.tabs(["Python", "SQL", "JavaScript", "Scala"])
        
        with python_tab:

            in_line_tab, on_stage_tab = st.tabs(["in-line", "on stage"])
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


def dynamic_table_segment():
    st.header("🔄 Dynamic Table", help="A special kind of table that can change its contents automatically when the data it's based on changes.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
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


def alert_segment():
    st.header("🚨 Alert", help="The thing that let's you know that your data has met a certain criteria.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, history_tab, tips_tab = \
        st.tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "HISTORY", "❄️"])
    with create_tab:
        
        st_code_block("create-alert", "create or replace an existing alert",
        """
        CREATE [ OR REPLACE ] ALERT [ IF NOT EXISTS ] <alert_name>
            WAREHOUSE = <warehouse_name>
            SCHEDULE = '{ <num> MINUTE | USING CRON <expr> <time_zone> }'
            COMMENT = '<string_literal>'
            IF( EXISTS(
                <condition>
            ))
            THEN
                <action>
        """
        )

        with st.expander("CRON Expressions"):
            st.code("""
                # __________ minute (0-59)
                # | ________ hour (0-23)
                # | | ______ day of month (1-31, or L)
                # | | | ____ month (1-12, JAN-DEC)
                # | | | | _ day of week (0-6, SUN-SAT, or L)
                # | | | | |
                # | | | | |
                * * * * *        
            """)

        
    with alter_tab:
        
        st_code_block("alter-alert", "resume or suspend the alert",
        """
        ALTER ALERT [ IF EXISTS ] <alert_name> { RESUME | SUSPEND }
        """
        )

        st_code_block("alter-alert", "alter the alert properties",
        """
        ALTER ALERT [ IF EXISTS ] <alert_name> SET
            [ WAREHOUSE = <string> ]
            [ SCHEDULE = '{ <number> MINUTE | USING CRON <expr> <time_zone> }' ]
            [ COMMENT = '<string_literal>' ]
        """
        )

        st_code_block("alter-alert", "modify the alert condition",
        """
        ALTER ALERT [ IF EXISTS ] <alert_name> MODIFY CONDITION EXISTS (<condition>)
        """
        )

        st_code_block("alter-alert", "modify the alert action",
        """
        ALTER ALERT [ IF EXISTS ] <alert_name> MODIFY ACTION <action>
        """
        )

    with drop_tab:
        st_code_block("drop-alert", "remove an existing alert",
        """
        DROP ALERT <alert_name>
        """
        )


    with describe_tab:
        st_code_block("desc-alert", "describe the propoerties of the alert",
        """
        DESCRIBE ALERT <alert_name>
        """
        )

    with show_tab:
        st_code_block("show-alert", "show available alerts",
        """
        SHOW ALERTS [ LIKE '<pattern>' ]
                    [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
                    [ STARTS WITH '<name_string>' ]
                    [ LIMIT <rows> [ FROM '<name_string>' ] ]
        """
        )

    with history_tab:
            st_code_block("https://docs.snowflake.com/en/sql-reference/functions/alert_history", "show alert history",
            """
            ALERT_HISTORY(
                [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
                [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
                [, RESULT_LIMIT => <integer> ]
                [, ALERT_NAME => '<string>' ] )
            """   
            )

    with tips_tab:
        st.markdown("""
        💡 **Tips**
        - Set up `ALERT`s to be notified or take actions when specific conditions in your data are met (e.g. warehouse credit usage surpassing a threshold, or data sanity checks failing).
        - Newly created or cloned `ALERT`s are suspended upon creation. Remember to resume the alert for it to execute using `ALTER ALERT <alert_name> RESUME`.
        - Monitor `ALERT` execution by checking the results of the specified actions or by viewing the history of alert executions. You can use the `ALERT_HISTORY` table function or the `ALERT_HISTORY` view in the `ACCOUNT_USAGE` schema for this purpose.
        """)



def data_manipulation_segment():
    st.header("🌀 Data Manipulation", help="The things you do to add or change data in the tables.")
    
    insert_tab, update_tab, merge_tab, delete_tab, tips_tab = \
        st.tabs(["INSERT", "UPDATE", "MERGE", "DELETE", "❄️"])
    
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
    "🔎 view",
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

def default_layout():
    st.session_state["layout_left_column"] = left_column_defaults
    st.session_state["layout_right_column"] = right_column_defaults

custom_layout = st.sidebar.expander("🧑‍🎨 Customize Layout")
with custom_layout:
    st.button("Default Layout", on_click=default_layout)
    side_left_col, side_right_col = st.columns(2)
    left_col_segments = side_left_col.multiselect("Left Column", 
                          options=all_segments, 
                          default=left_column_defaults,
                          key="layout_left_column")
                          
    right_col_segments = side_right_col.multiselect("Right Column", 
                          options=all_segments, 
                          default=right_column_defaults,
                          key="layout_right_column")

segment_dict = {
    "🗄 database": database_segment,
    "📊 table": table_segment,
    "🗃 schema": schema_segment,
    "🔎 view": view_segment,
    "📸 materialized view": materialized_view_segment,
    "🚉 stage": stage_segment,
    "🚰 pipe": pipe_segment,
    "🚚 data loading": data_loading_segment,
    "📋 task": task_segment,
    "🌊 stream": stream_segment,
    "🪄 function": function_segment,
    "🪜 procedure": procedure_segment,
    "🔄 dynamic table": dynamic_table_segment,
    "🚨 alert": alert_segment,
    "🌀 data manipulation": data_manipulation_segment,

}
with cols[0]:
    for seg in left_col_segments:
        segment_dict[seg]()
    

with cols[1]:
    for seg in right_col_segments:
        segment_dict[seg]()


    # st.header("Clustering")
    # st.header("Data Sampling")
    # st.header("Time Travel")
    # st.header("External Table")

with st.sidebar.expander("🗺 Legend", expanded=True):
    st.markdown("""
    - Text inside `[ BRACKETS ]` indicates *optional parameters* that can be omitted. Drop carefully!
    - Text inside `{ CURLY | BRACKETS }` indicates *available options* for the command. Choose wisely!   
    - Text inside `< angle.brackets >` indicates *entity names* (e.g. table, schema, etc.). Pick responsibly!
    - The [☁️](https://docs.snowflake.com/) icon in each section will snow-flake you to the relevant section on the documentation website.  
    """)

st.sidebar.info("""
Note: This online cheatsheet for Snowflake is based on materials from the [Snowflake documentation website](https://docs.snowflake.com/). 
    The content and logo of Snowflake used in this application are the intellectual property of Snowflake Inc. and are used here with proper attribution. 
    This cheatsheet is not affiliated with or endorsed by Snowflake Inc. Please refer to the official Snowflake documentation for detailed information and updates.
"""
)


st.sidebar.success("""
This guide is limited in scope and offers just a glimpse into the expansive array of Snowflake's *cool* features—pun intended. 
The reason for this is threefold:  
1. Time is finite, as suggested by modern physics. 
2. Snowflake is breaking the laws of physics by adding features faster than the speed of light, making it impossible for any mortal to catch up.
3. I am a mortal.

But here's where you come in, my knowledgeable friend. You likely have insights, cool features, or corrections that could benefit the entire Snowflake community. 
As an open-source project, I warmly (or should I say coolly? 🤔) welcome and eagerly look forward to your invaluable contribution. 
Don't hesitate to jump to the GitHub repository to open an issue or start a pull request (PR) to suggest additions or modifications to the content. 
Your expertise can help us keep this guide up-to-date and comprehensive.
"""
)

with st.sidebar.expander("Acknowledgments"):
    st.markdown("""
    I am incredibly grateful to my amazing Snowflake mentor, [Sang Hai](https://www.linkedin.com/in/sangvhai/), who is always sharing his extensive knowledge about the exciting and innovative features of Snowflake and guiding me in implementing them in my work. 
    I would also like to express my heartfelt appreciation to [Kathryn Reck Harris](https://www.linkedin.com/in/kathrynreck/) and [Varun Chavakula](https://www.linkedin.com/in/varunchavakula/), my awesome Snowflake buddies, who always share the exhilarating ride of exploring Snowflake and provide invaluable insights and support.

    Lastly, a special thanks to [**Jessica Smith**](https://www.linkedin.com/in/jessica-s-095a861b3/), a true champion of the Streamlit platform, for always encouraging me to create fun things in Streamlit and for her continuous support within the vibrant Streamlit community.
    """)
