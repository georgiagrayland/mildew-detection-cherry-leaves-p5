import streamlit as st


def page_project_summary_body():
    """
    Function displays project summary as text on dedicated page 
    """

    st.title("Project Summary")

    st.header("Context ")
    st.info(
        f"Cherry leaves are a plant product used throughout the world. "
        f"They can be consumed directly, but more importantly are a vital "
        f"ingredient in many products consumed today. "
        f"They can be found in products ranging from teas, herbal remedies "
        f"and supplements. They have great health benefits, "
        f"as they are high in antioxidants, reduce sugar levels, and are "
        f"effective painkillers. Countries and regions rely on the import "
        f"and export of this plant, therefore their healthy growth "
        f"is of utmost importance to the farmers and enterprises who grow "
        f"and use them.\n\nHowever, as cherry leaves are a biological product, "
        f"they are susceptible to natural and fungal infection, "
        f"and Powdery Mildew is a widespread example of this. "
        f"This fungal infection has the capability to hinder farmers from "
        f"growing sufficient crop for sale and export, "
        f"and thus it cannot be utiised by companies using it as an ingredient "
        f"or product.\n\n"
        f"Powdery Mildew is a disease that affects a range of plants worldwide."
        f" Powdery Mildew diseases on plants are caused "
        f"by different species of ascomycete fungi. Infected plants can display"
        f" powdery white areas and spots on their leaves and stems. "
        f"Lower leaves are mostly affected, however mildew can also appear on "
        f"any part of a plant above-ground. Mildew can spread the length "
        f"of a plant, as large numbers of spores form.\n\n"
        f"Hence the importance of this project is to detect the disease, in "
        f"order to prevent spreading within a plantation. "
        f"Powdery Mildew casues great harm in a greenhouse setting, and the "
        f"disease can significantly decrease crop yields. "
        f"It does not need a vector to spread, so early detection is highly "
        f"important, to protect as many plants as possible from disease.\n\n"
        f"**Source:** "
        f"[Powdery Mildew Diease](https://en.wikipedia.org/wiki/Powdery_mildew)"
    )

    st.header("Problem Statement")
    st.warning(
        f"* Farmy & Foods are facing a challenge where their cherry "
        f"plantations have been presenting powdery mildew. \n"
        f"* The cherry crop is one of their finest products in the portfolio "
        f"and the company is concerned about supplying the market with a "
        f"product of compromised quality. \n"
        f"The current process is manual verification of powdery mildew "
        f"presence, which takes an employee around 30 minutes per tree. \n"
        f"* The company has thousands of trrees located in muliple national "
        f"farms. Thus the manual process is **not scalable** due to time spent."
        f"\n* The company therefore wants to implement an ML system to save "
        f"time and labour, which instantly detects powdery mildew in "
        f"leaves from images. "
    )

    st.header("Business Requirements")
    st.subheader("This project has 2 business requirements:")
    if st.checkbox("Business Requirement 1:"):
        st.write(
            f"**The study includes an analysis on:**\n"
            f"- Average images and variability images for healthy or powdery "
            f"mildew.\n"
            f"- Differences between average healthy and average powdery mildew "
            f"cherry leaves.\n"
            f"- An image montage displayed for each class. "
        )

    if st.checkbox("Business Requirement 2:"):
        st.write(
            f"- Deliver an ML system that is capable of predicting whether a "
            f"given cherry leaf is healthy or infected with powdery mildew.\n"
        )

    if st.button("Project Dataset Here"):
        st.success(
            f"The dataset is from "
            f"[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves):\n\n"
            f"* The available dataset contains 2104 healthy leaves and 2104 "
            f"infected leaves. "
        )

    st.write(
        f"For more information, please "
        f"[view the project README file](https://github.com/georgiagrayland/mildew-detection-cherry-leaves-p5/blob/main/README.md)"
    )
