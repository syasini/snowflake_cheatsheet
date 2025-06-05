import streamlit as st


def code_block(url, caption=None, code=None):
    """Display SQL code snippet with documentation link."""
    if not url.startswith("https"):
        url = f"https://docs.snowflake.com/en/sql-reference/sql/{url}"
    st.caption(f"[☁️]({url}) {caption}")
    st.code(code, language="sql")


def make_tabs(*names):
    """Wrapper around st.tabs returning the created tab objects."""
    if len(names) == 1 and isinstance(names[0], (list, tuple)):
        names = names[0]
    return st.tabs(list(names))


# Backward compatibility
st_code_block = code_block
