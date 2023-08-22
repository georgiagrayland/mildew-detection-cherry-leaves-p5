import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    st.dataframe(pd.DataFrame(
        load_pkl_file(
            f'outputs/{version}/evaluation.pkl'), index=['Loss', 'Accuracy']))

