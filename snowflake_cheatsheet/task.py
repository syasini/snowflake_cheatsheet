import streamlit as st
from .utils import st_code_block, make_tabs

def task_segment():
    st.header("📋 Task", help="The todo list that tells Snowflake what to do with the data and when to do them.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "❄️"])
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


