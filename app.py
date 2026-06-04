import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Settings (Dark Theme and Wide Layout)
st.set_page_config(page_title="Vibrant Premium Dashboard", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for Premium UI
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .main-title { 
        font-size: 42px; 
        font-weight: 800; 
        background: linear-gradient(45deg, #FF416C, #FF4B2B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; 
        margin-bottom: 5px; 
    }
    .subtitle { 
        font-size: 16px; 
        color: #a3a8b4; 
        text-align: center; 
        margin-bottom: 35px; 
    }
    .metric-box {
        background-color: #1f2430;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FF4B2B;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# Titles
st.markdown('<div class="main-title">🚀 Colabs Project: Premium Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Developed by <b>Eshaal Atif</b> | Data Analytics Web App</div>', unsafe_allow_html=True)

# 2. Data Loading
@st.cache_data
def load_data():
    bookings_data = {
        'BookingID': ['B101', 'B102', 'B103', 'B104'],
        'MemberID': ['M001', 'M002', 'M001', 'M003'],
        'AmountPaid': [5000, 3500, 4500, 6000]
    }
    members_data = {
        'MemberID': ['M001', 'M002', 'M003'],
        'FullName': ['Bilal Siddiqui', 'Amna Imam', 'Zainab Khan'],
        'MembershipType': ['Premium', 'Basic', 'Premium']
    }
    return pd.DataFrame(bookings_data), pd.DataFrame(members_data)

df, df1 = load_data()
master_df = pd.merge(df, df1, on='MemberID', how='inner')

# 3. Sidebar Configuration
st.sidebar.markdown("## ⚙️ Interface Settings")
vibrant_theme = st.sidebar.selectbox("Color Palette", ["Neon Punch", "Electric Cyber", "Sunset Glow"])
show_tables = st.sidebar.checkbox("👀 Inspect Raw Data", value=False)

# Color Scheme Mapping
color_maps = {
    "Neon Punch": ['#FF1493', '#00FFFF'],
    "Electric Cyber": ['#7B2CBF', '#3C096C'],
    "Sunset Glow": ['#FF8C00', '#FF007F']
}
selected_colors = color_maps[vibrant_theme]

# 4. KPI Summary Cards
total_rev = master_df['AmountPaid'].sum()
total_bookings = master_df['BookingID'].count()

col_m1, col_m2 = st.columns(2)
with col_m1:
    st.markdown(f"""
    <div class="metric-box">
        <span style="color:#a3a8b4; font-size:14px;">TOTAL REVENUE GENERATED</span><br>
        <span style="color:#ffffff; font-size:28px; font-weight:bold;">PKR {total_rev:,}</span>
    </div>
    """, unsafe_allow_html=True)
with col_m2:
    st.markdown(f"""
    <div class="metric-box" style="border-left-color: #00FFFF;">
        <span style="color:#a3a8b4; font-size:14px;">TOTAL BOOKINGS CONFIRMED</span><br>
        <span style="color:#ffffff; font-size:28px; font-weight:bold;">{total_bookings} Bookings</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

# 5. Raw Data Section
if show_tables:
    st.subheader("📋 Backend Dataframes")
    t1, t2 = st.columns(2)
    with t1: st.dataframe(df, use_container_width=True)
    with t2: st.dataframe(df1, use_container_width=True)

# 6. Vibrant Plotly Chart
st.subheader("📊 Dynamic Revenue Distribution")
revenue_by_membership = master_df.groupby('MembershipType')['AmountPaid'].sum().reset_index()

left_col, right_col = st.columns([2, 3])

with left_col:
    st.write("This interactive interface updates instantly based on your backend logic. Hover over the chart to see magic!")
    st.dataframe(revenue_by_membership, use_container_width=True)

with right_col:
    # Creating a modern vibrant Donut Chart using Plotly
    fig = px.pie(
        revenue_by_membership, 
        values='AmountPaid', 
        names='MembershipType', 
        hole=0.4,
        color_discrete_sequence=selected_colors
    )
    
    fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#0e1117', width=3)))
    fig.update_layout(
        margin=dict(t=20, b=20, l=20, r=20),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff')
    )
    st.plotly_chart(fig, use_container_width=True)