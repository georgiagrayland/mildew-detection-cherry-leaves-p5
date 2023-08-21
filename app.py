import streamlit as st
from app_pages.multipage import MultiPage

# Load page scrits from app_pages
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_ml_performance import page_ml_performance_body

app = MultiPage(app_name="Mildew Detector Leaves Project")

# App pages added individually to create dashboard
app.add_page("Project Summary", page_project_summary_body)
app.add_page("Project Hypotheses and Validation", page_project_hypothesis_body)
app.add_page("Cherry Leaf Visualiser", page_leaves_visualizer_body)
app.add_page("ML Performance Metrics", page_ml_performance_body)

# Runs the app
app.run()
