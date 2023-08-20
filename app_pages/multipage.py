import streamlit as st

# class generates multiple streamlit pages
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️")

    def add_page(self, title, func) -> None:
        """Function adds page titles"""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Functions adds title names to sidebar menu
        """
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
