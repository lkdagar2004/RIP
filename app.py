import streamlit as st
import random
import time  # 1. Import the time module

st.set_page_config(page_title="Valentine's Request", page_icon="💘", layout="wide")

# --- STATE INITIALIZATION ---
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = 0 
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False


# --- MAIN LAYOUT ---
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Will you be my valentine.? 🥺</h1>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

if st.session_state.yes_clicked:
    st.success("Yay! ✨💖 Best Valentine's Day ever! 💖✨")
    
    # 2. Trigger multiple waves of balloons!
    for _ in range(3):
        st.balloons()
        time.sleep(1.5)  # Pauses for 1.5 seconds before launching the next wave
        
else:
    # --- BUTTON LAYOUT ---
    col1, col_yes, col_no_start, col4, col5 = st.columns(5)
    
    with col_yes:
        if st.button("YES", type="primary", use_container_width=True):
            st.session_state.yes_clicked = True
            st.rerun()

    slots = []
    slots.append(col_no_start) 
    
    # --- CREATE THE ESCAPE GRID ---
    for _ in range(5):
        st.markdown("<br><br>", unsafe_allow_html=True) 
        cols = st.columns(5)
        slots.extend(cols)
        
    # --- RENDER THE NO BUTTON ---
    with slots[st.session_state.no_pos]:
        if st.button("NO", use_container_width=True):
            available_slots = [i for i in range(1, len(slots)) if i != st.session_state.no_pos]
            st.session_state.no_pos = random.choice(available_slots)
            st.rerun()
