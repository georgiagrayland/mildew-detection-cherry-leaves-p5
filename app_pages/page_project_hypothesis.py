import streamlit as st


def page_project_hypothesis_body():

    st.header("Mildew Detection in Cherry Leaves Hypotheses and Validation")

    st.subheader(
        f"There are 4 main hypotheses for this project:")
    st.info(
        f"1) Cherry leaves that are infected with powdery mildew have white "
        f"spots or areas on the leaf surface, or plant stems.\n\n"
        f"2) The infection of powdery mildew would gradually spread, "
        f"to eventually cover the plant to have a white powdery/fuzzy "
        f"appearance all over. \n\n"
        f"3) This appearance of an infected plant should be a sufficient "
        f"difference from a healthy leaf, to be able to trian an ML model "
        f"to detect and predict the presence of powdery mildew"
        f" on new leaf image data. This can help the client decrease "
        f"time and labour costs associated with manual detection. \n\n"
        f"4) The ML model will be able to distinush between a healthy cherry "
        f"leaf, and one which has been infected with powdery mildew, "
        f"with an **accuracy of at least 97%**.\n\n"
    )

    st.success(
        f"**Project Hypotheses Validation**\n\n"

        f"- It can be seen that Cherry Leaves that are infected with powdery "
        f"mildew have a lighter colouring/white patchy appearance, "
        f"as well as more deformed edges compared with "
        f"healthy leaves. \n\n"

        f"- An image montage clearly displays the visual difference between "
        f"the two types of leaves in this project. \n\n"

        f"- The ML app differentiates between a healthy cherry "
        f"leaf and one that is infected with powdery mildew.\n\n"
        f"- The Mildew Detector predicts on new data with at least a 97% "
        f"level of accuracy. This has been confirmed in the training and "
        f"validation steps of the model training process. \n\n"
        f"- The detailed ML pipline performance evaluation can be viewed on "
        f"the 'ML Performance Metrics' page.\n\n"
        f"- Please navigate to the 'Cherry Leaf Visualiser' page in the menu "
        f"sidebar to view image montages for healthy and infected leaves. "
    )
