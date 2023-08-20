import streamlit as st


def page_project_summary_body():
    """
    Function displays project summary as text on dedicated page 
    """

    st.title("Project Summary")

    st.header("Context ")
    st.info(
        f"Cherry leaves are a plant product used throughout the world. "
        f"They can be consumed directly, but more importantly are a vital ingredient in many products consumed today. "
        f"They can be found in products ranging from teas, herbal remedies and supplements. "
        f"They have great health benefits, as they are high in antioxidants, reduce sugar levels, and are effective painkillers. "
        f"Countries and regions rely on the import and export of this plant, therefore their healthy growth "
        f"is of utmost importance to the farmers and enterprises who grow and use them.\n\n"
        f"However, as cherry leaves are a biological product, they are susceptible to natural and fungal infection, "
        f"and Powdery Mildew is a widespread example of this. "
        f"This fungal infection has the capability to hinder farmers from growing sufficient crop for sale and export, "
        f"and thus it cannot be utiised by companies using it as an ingredient or product.\n\n"
        f"Powdery Mildew is a disease that affects a range of plants worldwide. Powdery Mildew diseases on plants are caused "
        f"by different species of ascomycete fungi. Infected plants can display powdery white areas and spots on their leaves and stems. "
        f"Lower leaves are mostly affected, however mildew can also appear on any part of a plant above-ground. Mildew can spread the length "
        f"of a plant, as large numbers of spores form.\n\n"
        f"Hence the importance of this project is to detect the disease, in order to prevent spreading within a plantation. "
        f"Powdery Mildew casues great harm in a greenhouse setting, and the disease can significantly decrease crop yields. "
        f"It does not need a vector to spread, so early detection is highly important, to protect as many plants as possible from disease.\n\n"
        f"**Source:** [Powdery Mildew Diease](https://en.wikipedia.org/wiki/Powdery_mildew)"
    )

    st.write(
        f"For more information, please view the project README:"
        f"[View file here](insert readme link)"
    )
