import streamlit as st
import json
from datetime import datetime

def main():
    st.set_page_config(
        page_title="EventIQ - Consulting Career Assistant", 
        page_icon="🎯",
        layout="wide"
    )
    
    st.title("🎯 EventIQ - Management Consulting Career Assistant")
    st.subheader("AI-powered event selection for consulting interview success")
    
    # Quick profile setup
    with st.expander("⚡ Quick Setup (30 seconds)", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            mba_year = st.selectbox("MBA Year", ["1st Year", "2nd Year"])
            case_exp = st.selectbox("Case Experience", ["Beginner", "Some Practice", "Advanced"])
        
        with col2:
            target_firms = st.multiselect("Target Firms", 
                ["McKinsey", "BCG", "Bain", "Deloitte", "PwC", "EY", "Boutique"],
                default=["McKinsey", "BCG", "Bain"])
            timeline = st.selectbox("Recruiting Phase", 
                ["Pre-Prep", "Active Recruiting", "Interview Season"])
        
        with col3:
            industries = st.multiselect("Target Industries",
                ["Healthcare", "Technology", "Financial Services", "Consumer Products", "Energy"],
                default=["Healthcare", "Technology"])
            budget = st.selectbox("Event Budget", ["$0", "$0-500", "$500-2000", "No Limit"])
        
        with col4:
            priorities = st.multiselect("Focus Areas",
                ["Case Skills", "Industry Knowledge", "Networking", "Presentation Skills"],
                default=["Case Skills", "Networking"])
            time_available = st.slider("Hours/week for events", 2, 20, 8)
    
    # Main interface
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.header("📅 Event Analysis")
        
    
