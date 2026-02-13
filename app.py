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

# 2. Custom CSS for the "World's Best UI"
# We inject this to change fonts, colors, and button shapes.
st.markdown("""
<style>
    /* Import a cute cursive font */
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    /* The Main Background - A soft romantic gradient */
    .stApp {
        background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
    }

    /* The Title Styling */
    h1 {
        font-family: 'Pacifico', cursive;
        color: #d63384;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 0px;
    }

    /* Subtitle/Text Styling */
    p {
        font-family: 'Poppins', sans-serif;
        color: #5a5a5a;
        font-size: 1.2rem;
    }

    /* Button Styling - Making them look like candy */
    .stButton>button {
        border-radius: 50px;
        border: none;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
    }

    /* Hover effects */
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    }

</style>
""", unsafe_allow_html=True)

# 3. Session State Management
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = 0  # Start at position 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False

# 4. The Logic
if st.session_state.yes_clicked:
    # --- SUCCESS SCREEN ---
    
    # Center the celebration
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1>YAY! I Knew You Would Say Yes! ❤️</h1>", unsafe_allow_html=True)
        # A cute celebrating bear GIF
        st.image("https://media.tenor.com/gUiu1zyxfzYAAAAi/bear-kiss-bear-kisses.gif", use_container_width=True)
        
    # The 5-Second Balloon Party
    # We use a loop to keep the party going!
    for _ in range(4): # 4 loops * 1.5s delay = ~6 seconds of joy
        st.balloons()
        time.sleep(1.5)
        
else:
    # --- QUESTION SCREEN ---
    
    # 1. The Cute Header Image (A shy bear)
    col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
    with col_img2:
        st.image("https://media.tenor.com/nEf-Y6u7zQAAAAAi/bear-cute.gif", use_container_width=True)
    
    # 2. The Question
    st.markdown("<h1>Will you be my Valentine? 🥺</h1>", unsafe_allow_html=True)
    st.write("") # Spacer

    # 3. The Interactive Buttons
    # We create a Grid of 25 slots (5x5) to let the NO button jump far away.
    # Slot 2 (Top row, middle) is reserved for the YES button.
    
    # Create the grid slots
    slots = []
    
    # Row 1
    r1_col1, r1_col2, r1_col3, r1_col4, r1_col5 = st.columns(5)
    slots.extend([r1_col1, r1_col2, r1_col3, r1_col4, r1_col5])
    
    # Rows 2-5 (The "Escape Zone")
    for _ in range(4):
        st.markdown("<br>", unsafe_allow_html=True) # Add vertical distance
        cols = st.columns(5)
        slots.extend(cols)

    # --- PLACING THE BUTTONS ---
    
    # Always place YES in the nice center spot (Index 2 of our list)
    with slots[2]:
        if st.button("YES! 💖", type="primary", use_container_width=True):
            st.session_state.yes_clicked = True
            st.rerun()

    # Place NO in the random spot determined by session_state
    # If the random spot happens to be 2 (where YES is), we move it to 3.
    pos = st.session_state.no_pos
    if pos == 2: 
        pos = 3
        
    with slots[pos]:
        # We give the NO button a unique key so Streamlit knows it's moving
        if st.button("No 😢", key=f"no_btn_{pos}", use_container_width=True):
            # Generate a new random position (0 to 24)
            new_pos = random.randint(0, 24)
            # Ensure it doesn't land on the YES button (index 2)
            while new_pos == 2:
                new_pos = random.randint(0, 24)
            
            st.session_state.no_pos = new_pos
            st.rerun()
