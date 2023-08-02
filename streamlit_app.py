import streamlit as st

class StreamlitApp:
    def __init__(self, port="", config="", page_title="Car Sales Prediction", page_icon=":car:", subheader="Car Sales Prediction"):
        
        self.port = port
        self.config = config
        self.page_title = page_title
        self.page_icon = page_icon
        self.subheader = subheader

        self.create_main_pg()

    def create_main_pg(self):
        # Create page
        st.set_page_config(page_title=self.page_title, page_icon=self.page_icon, layout = 'wide')
        
        with open('./page_content/welcome.txt') as file:
            page_content = file.read()

        st.markdown(page_content, unsafe_allow_html=True)

if __name__ == "__main__":
    st_app = StreamlitApp()
