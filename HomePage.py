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
    
    .stApp{
        background-color: #fce8ec;
    }
    .block-container {
        padding-top: 6rem;
        padding-left: 6rem;
        padding-right: 6rem;
    }
    
      .stButton>button {
        background-color: #FFD4E0;
        color: white;
    }
    
        .stButton>button:hover {
        background-color: #FF9DB8;
        color: white;
    }
    
    .feature-card {
        background: #FFD4E0;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #FF9DB8;
        margin: 1rem 0;
    }
    
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.page_link("HomePage.py", label = "Home", icon="🏠")
    st.page_link("pages/AddRecipe.py", label = "Add Recipe", icon="➕")
    st.page_link("pages/ExploreRecipes.py", label = "Explore Recipes", icon="🔍")
    

nav_col1, nav_col2, nav_col3 = st.columns([6, 1, 1])
with nav_col2:
    if st.button("Login", use_container_width=True):
        pass  # Login functionality will go here
with nav_col3:
    if st.button("Sign Up", use_container_width=True):
        pass  # Sign up functionality will go here
    
st.image(imgbanner, use_container_width=True)

st.markdown("<h2 style='text-align: center;'>Welcome to Your Culinary Journey</h2>", unsafe_allow_html=True)
st.markdown("""
            <p style ='text-align: center;'>
            CookBook is your intelligent cooking companion that helps you organize, discover,
            and master your favorite recipes. Save your cherished family recipes, explore new 
            culinary adventures, and get personalized AI suggestions based on your taste preferences.
            </p>
            """, unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([2, 1, 2])
with col_center:
    if st.button("Learn More", use_container_width=True):
        pass
    
st.markdown("---")
st.markdown("## ✨ Key Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.markdown("""
        <div class="feature-card">
            <h3>📚 Organize Your Recipes</h3>
            <p>Save and categorize all your favorite recipes in one place. Add custom tags, 
            notes, and ratings to keep everything organized.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-card">
            <h3>🛒 Smart Ingredient Tracking</h3>
            <p>Keep track of ingredients across all your recipes. Generate shopping lists 
            automatically and never forget what you need.</p>
        </div>
    """, unsafe_allow_html=True)

with feature_col2:
    st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI-Powered Suggestions</h3>
            <p>Get personalized recipe recommendations based on your saved recipes, 
            preferences, and cooking history.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-card">
            <h3>🏷️ Flexible Tagging System</h3>
            <p>Create custom tags for dietary preferences, meal types, cuisines, and more. 
            Find exactly what you're looking for in seconds.</p>
        </div>
    """, unsafe_allow_html=True)
    
st.markdown("---")
st.markdown("## How It Works")

step_col1, step_col2, step_col3 = st.columns(3)

with step_col1:
    st.markdown("### 1️⃣ Sign Up")
    st.write("Create your free account in seconds")

with step_col2:
    st.markdown("### 2️⃣ Add Recipes")
    st.write("Save your favorite recipes with ingredients and tags")

with step_col3:
    st.markdown("### 3️⃣ Get Suggestions")
    st.write("Let AI discover new recipes you'll love")