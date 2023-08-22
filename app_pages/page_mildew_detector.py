import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
    )


def page_mildew_detector_body():
    """
    Function displays page with the live mildew detector
    """
    st.header("Mildew Detector")
    st.info(
        f"The client is interested in predicting whehter a cherry leaf "
        f"is infected with podery mildew or not. "
    )
    st.write('---')
    
    st.write(
        f"Upload images for a prediction, and click on the **Make Prediction** "
        f"button to view the result.\n"
        f"Images can be downloaded from "
        f"[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )
    images_buffer = st.file_uploader(' ', accept_multiple_files=True)
    predict_button = st.button("Make Prediction")

    if predict_button:
        make_live_predict(images_buffer)

def make_live_predict(images_buffer):
    """
    Function uploads images, makes the live prediction from the ML model
    """

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x "
                f"{img_array.shape[0]}px height"
            )

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append(
                {"Name": image.name, 'Result': pred_class}, ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)