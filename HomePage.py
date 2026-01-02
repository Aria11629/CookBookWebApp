import streamlit as st
from PIL import Image

imglogo = Image.open("logo.png")
imgbanner = Image.open("logobanner.png")

st.set_page_config(
    page_title="CookBook",
    page_icon=imglogo,
    layout="wide",
    initial_sidebar_state="collapsed"  
)

st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    .block-container {
        padding-top: 6rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    


    </style>
    """, unsafe_allow_html=True)

st.image(imgbanner, use_container_width=True)

with st.sidebar:
    st.page_link("HomePage.py", label = "Home", icon="🏠")
    st.page_link("pages/AddRecipe.py", label = "Add Recipe", icon="➕")
    st.page_link("pages/ExploreRecipes.py", label = "Explore Recipes", icon="🔍")