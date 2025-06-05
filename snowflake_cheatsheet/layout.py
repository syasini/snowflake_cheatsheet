import streamlit as st
from .utils import st_code_block, make_tabs


def default_layout(left_defaults, right_defaults):
    """Reset layout column selections to defaults."""
    st.session_state["layout_left_column"] = left_defaults
    st.session_state["layout_right_column"] = right_defaults
