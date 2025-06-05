import streamlit as st
from .utils import st_code_block, make_tabs

def alert_segment():
    st.header("🚨 Alert", help="The thing that let's you know that your data has met a certain criteria.")
    
    create_tab, alter_tab, drop_tab, describe_tab, show_tab, history_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "DROP", "DESCRIBE", "SHOW", "HISTORY", "❄️"])
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



