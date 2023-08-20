import streamlit as st


def page_project_summary_body():
    """
    Function displays project summary as text on dedicated page 
    """

    st.title("Project Summary")

    st.header("Overview ")
    st.info(
        f"Cherry leaves are a plant product used throughout the world. "
        f"They can be consumed directly, but more importantly are a vital ingredient in many products consumed today. "
        f"They can be found in products ranging from teas, herbal remedies and supplements. "
        f"They have great health benefits, as they are high in antioxidants, reduce sugar levels, and are effective painkillers. "
        f"Countries and regions rely on the import and export of this plant, therefore their healthy growth "
        f"is of utmost importance to the farmers and enterprises who grow and use them."
    )

    st.write(
        f"For more information, please view the project README:"
        f"[View file here](insert readme link)"
    )
