## IMPORTANT CALL OUT 
## ==================
## As you may have noticed, this script can use a lot of refactoring 
## and should be broken down into multiple modules for better readability 
## and easier maintanance. If you are interested in helping out,
## please open an issue/PR and contribute to the project. 
## The community will greatly appreciate your help and contribution! 

import streamlit as st
from snowflake_cheatsheet.database import database_segment
from snowflake_cheatsheet.schema import schema_segment
from snowflake_cheatsheet.table import table_segment
from snowflake_cheatsheet.view import view_segment
from snowflake_cheatsheet.materialized_view import materialized_view_segment
from snowflake_cheatsheet.stage import stage_segment
from snowflake_cheatsheet.pipe import pipe_segment
from snowflake_cheatsheet.data_loading import data_loading_segment
from snowflake_cheatsheet.task import task_segment
from snowflake_cheatsheet.stream import stream_segment
from snowflake_cheatsheet.function import function_segment
from snowflake_cheatsheet.procedure import procedure_segment
from snowflake_cheatsheet.dynamic_table import dynamic_table_segment
from snowflake_cheatsheet.alert import alert_segment
from snowflake_cheatsheet.data_manipulation import data_manipulation_segment
from snowflake_cheatsheet.layout import default_layout

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

custom_layout = st.sidebar.expander("🧑‍🎨 Customize Layout")
with custom_layout:
    st.button(
        "Default Layout",
        on_click=lambda: default_layout(left_column_defaults, right_column_defaults),
    )
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
