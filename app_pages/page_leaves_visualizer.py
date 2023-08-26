import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_leaves_visualizer_body():
    """
    Function to display leaves visualiser page 
    """
    st.title("Visualisation of Cherry Leaves")

    st.info(
        f"This page provides a visual representation of the two different "
        f"leaf types in this study: **healthy** and "
        f"**powdery mildew infected**"
    )

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_infected = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")

        st.image(avg_healthy, caption='Healty leaves - Average and Variability')
        st.image(avg_infected,
                 caption=
                'Powdery Mildew infected leaves - Average and Variability')

    st.warning(
        f"* A fairly significant visual difference can be observed between "
        f"healthy and infected leaves. \n"
        f"* It can be noted that average images of powdery mildew infected "
        f"leaves have detectable white patches and spots on their surface. \n"
        f"* Average images of healthy leaves have a more uniform green "
        f"colour, with no detectable white areas on the leaves.")
    st.write("---")

    if st.checkbox("Image Sizes on Train Set - Scatter Plot and Averages"):
        avg_img_size_train = plt.imread(f"outputs/{version}/image_shapes.png")
        st.image(avg_img_size_train, caption="Image Sizes in Train set - Width Average=256, Height Average=256")
    st.write("---")

    if st.checkbox(
            "Differences between Average Healthy and Average Infected Leaf"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.image(diff_between_avgs, caption="Difference Between Average Images")

        st.success(
            f"* There is a similar pattern to the above. \n"
            f"* **Healthy**  leaves have a more uniform, clear green appearance,"
            f" whereas the **infected leaves** have varying white pathches"
            f"  on their surface. \n"
            f"* However, visually it is diffcult to compare the two kinds of "
            f"leaves and detect quickly and easily whether they are healthy or"
            f" infected. "
        )
    st.write("---")
    if st.checkbox("Image Montage"):
        st.write(
            f"- To create and refresh the image montage, please click on "
            f"'Create Montage' button. This can be done repeatedly.\n"
        )
        my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir+ '/validation')
        label_to_display = st.selectbox(
            label="Select label:", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """Function to create and display image montage on dashbaord"""
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subsets the class you are interested to display
    if label_to_display in labels:

        # Checks if your montage space is greater than subset size
        images_list = os.listdir(dir_path+'/'+ label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return
    
        # Creates list of axes indices based on nrows and ncols
        list_rows = range(0,nrows)
        list_cols = range(0,ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

    # Creates a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0,nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
