import streamlit as st


def page_project_summary_body():
    """
    Function displays project summary as text on dedicated page 
    """

    st.title("Project Summary")

    st.header("Overview ")
    st.info(
        f"Cherries, and their leaves, are a plant product used throughout the world."
        f"They are consumed directly, and perhaps more importantly, a vital ingredient in many foods today"
        f"Countries and regions rely on the import and export of this plant, therefore their healthy growth"
        f"is of utmost importance to the farmers and enterprises who grow and use them."
    )

    st.write(
        f"For more information, please view the project README:"
        f"[View file here](insert readme link)"
    )
