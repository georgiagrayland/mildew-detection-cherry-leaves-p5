import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate import load_test_evaluation


def page_ml_performance_body():
    """
    Function displays performance of the ML Model 
    """
    st.header("ML Performance Metrics")
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    labels_pie = plt.imread(f"outputs/{version}/labels_pie.png")
    st.image(labels_pie,
             caption='Overall Dataset Split')
    st.write("---")

    st.header("Model Training History")
    st.info(
        f"The graphs visually represent the learning process and cycle of "
        f"the ML model used in this project."
        f"The two graphs show accuracy and loss plots as a result of the "
        f"training process of the model. \n\n"
        f"The graphs show that the model is neither overfitting or "
        f"underfitting, showing a normal learing curve of an ML pipeline."
    )
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.success(
        f"This table numerically represents the graphs above.\n"
        f"This provides explanation and evidence that the model that is "
        f"**99% accurate**"
    )

    load_test_evaluation(version)
