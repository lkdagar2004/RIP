import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Be My Valentine?",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for a Single-Page Fit
st.markdown("""
<style>
    /* Remove Streamlit's default top padding to pull everything up */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }

    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    /* The Main Background */
    .stApp {
        background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
        overflow: hidden; /* Helps prevent accidental scrollbars */
    }

    /* The Title Styling - Slightly smaller to fit on one page */
    h1 {
        font-family: 'Pacifico', cursive;
        color: #d63384;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        font-size: 3rem !important; 
        text-align: center;
        margin-top: 0px;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }

    /* Button Styling */
    .stButton>button {
        border-radius: 50px;
        border: none;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# 3. Session State Management
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = 0  
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False

# 4. The Logic
if st.session_state.yes_clicked:
    # --- SUCCESS SCREEN ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1>YAY! I Knew You Would Say Yes! ❤️</h1>", unsafe_allow_html=True)
        st.image("https://media.tenor.com/gUiu1zyxfzYAAAAi/bear-kiss-bear-kisses.gif", use_container_width=True)
        
    for _ in range(4): 
        st.balloons()
        time.sleep(1.5)
        
else:
    # --- QUESTION SCREEN ---
    
    # 1. The Cute Header Image (Made narrower to save vertical space)
    col_img1, col_img2, col_img3 = st.columns([2, 1, 2])
    with col_img2:
        st.image("https://media.tenor.com/nEf-Y6u7zQAAAAAi/bear-cute.gif", use_container_width=True)
    
    # 2. The Question
    st.markdown("<h1>Will you be my Valentine? 🥺</h1>", unsafe_allow_html=True)
    st.write("") # Just one small spacer

    # 3. The Escape Grid (Now 3 rows of 5 columns = 15 slots)
    slots = []
    for _ in range(3):
        cols = st.columns(5)
        slots.extend(cols)

    # --- PLACING THE BUTTONS ---
    
    # Place YES in the top-middle (Index 2)
    with slots[2]:
        if st.button("YES! 💖", type="primary", use_container_width=True):
            st.session_state.yes_clicked = True
            st.rerun()

    # Place NO button
    pos = st.session_state.no_pos
    if pos == 2: 
        pos = 3
        
    with slots[pos]:
        if st.button("No 😢", key=f"no_btn_{pos}", use_container_width=True):
            # Generate a new random position (0 to 14 for our 15 slots)
            new_pos = random.randint(0, 14)
            while new_pos == 2: # Keep it away from the YES button
                new_pos = random.randint(0, 14)
            
            st.session_state.no_pos = new_pos
            st.rerun()
