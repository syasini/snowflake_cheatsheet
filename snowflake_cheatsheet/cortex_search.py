import streamlit as st
from .utils import st_code_block, make_tabs


def cortex_search_segment():
    st.header(
        "🧠 Cortex Search",
        help="Service for fast semantic search across your data using vector indexes.",
    )

    create_tab, alter_tab, show_tab, describe_tab, drop_tab, tips_tab = \
        make_tabs(["CREATE", "ALTER", "SHOW", "DESCRIBE", "DROP", "❄️"])

    with create_tab:
        st_code_block(
            "create-cortex-search",
            "create or replace a cortex search service",
            """
            CREATE [ OR REPLACE ] CORTEX SEARCH SERVICE [ IF NOT EXISTS ] <name>
              ON <search_column>
              ATTRIBUTES <col_name> [ , ... ]
              WAREHOUSE = <warehouse_name>
              TARGET_LAG = '<num> { seconds | minutes | hours | days }'
              AS <query>;
            """,
        )

    with alter_tab:
        st_code_block(
            "alter-cortex-search",
            "suspend or resume indexing or serving",
            """
            ALTER CORTEX SEARCH SERVICE [ IF EXISTS ] <name>
              { SUSPEND | RESUME } [ { INDEXING | SERVING } ]
            """,
        )

        st_code_block(
            "alter-cortex-search",
            "refresh the service",
            """
            ALTER CORTEX SEARCH SERVICE [ IF EXISTS ] <name> REFRESH
            """,
        )

        st_code_block(
            "alter-cortex-search",
            "update target lag or warehouse",
            """
            ALTER CORTEX SEARCH SERVICE [ IF EXISTS ] <name> SET
              [ TARGET_LAG = '<num> { seconds | minutes | hours | days }' ]
              [ WAREHOUSE = <warehouse_name> ]
            """,
        )

    with show_tab:
        st_code_block(
            "show-cortex-search",
            "show available cortex search services",
            """
            SHOW SEARCH SERVICES [ LIKE '<pattern>' ]
                                [ IN { ACCOUNT | DATABASE [ <db_name> ] | [ SCHEMA ] [ <schema_name> ] } ]
                                [ STARTS WITH '<name_string>' ]
                                [ LIMIT <rows> [ FROM '<name_string>' ] ]
            """,
        )

    with describe_tab:
        st_code_block(
            "describe-cortex-search",
            "describe a cortex search service",
            """
            DESCRIBE CORTEX SEARCH SERVICE <name>
            """,
        )

    with drop_tab:
        st_code_block(
            "drop-cortex-search",
            "remove a cortex search service",
            """
            DROP CORTEX SEARCH SERVICE [ IF EXISTS ] <name>
            """,
        )

    with tips_tab:
        st.markdown(
            """
            💡 **Tips**
            - Use the SEARCH_PREVIEW SQL function only for quick testing and validation—it’s slower and has a strict 300 KB response limit.
            - Choose your query method based on the use case: use the Python API for pipelines, REST API for external apps, and SQL for simple previews.
            - Improve search result ranking by applying `numeric_boosts` (with columns and weights) and `time_decays` (for recency signals) during queries.
            - To reduce embedding costs, avoid frequent row updates, as any change—even outside the search column—triggers re-embedding.
            - Set the `TARGET_LAG` parameter based on your business needs to avoid unnecessary refreshes and compute costs.
            - Disable reranking during queries to reduce latency by 100–300ms if precise result quality is not essential.
            - Suspend the service when it's not actively serving queries to avoid ongoing serving compute charges.
            - Keep the source query simple and avoid joins or complex transformations to reduce indexing time and cost.
            - Monitor compute and serving costs using the `CORTEX_SEARCH_DAILY_USAGE_HISTORY` and `CORTEX_SEARCH_SERVING_USAGE_HISTORY` views.
            """
        )
