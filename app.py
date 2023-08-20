import streamlit as st
from app_pages.multipage import MultiPage

# Load page scrits from app_pages
from app_pages.page_project_summary import page_project_summary_body

app = MultiPage(app_name = "Cherry Leaves Mildew Detector")

# App pages added individually to create dashboard
app.add_page("Project Summary", page_project_summary_body)

app.run()