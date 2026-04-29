import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. Page Configuration & Aesthetics
# ==========================================
st.set_page_config(
    page_title="PrimeMart Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for KPI cards
st.markdown("""
    <style>
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. Data Ingestion & Preprocessing
# ==========================================
@st.cache_data
def load_data():
    df = pd.read_csv("PrimeMartNig.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset 'PrimeMartNig.csv' not found.")
    st.stop()

# ==========================================
# 3. Sidebar: Strategic Filters
# ==========================================
st.sidebar.title("Data Filters")
available_years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect("Select Year(s):", available_years, default=available_years)

available_regions = sorted(df['Region'].unique())
selected_regions = st.sidebar.multiselect("Select Region(s):", available_regions, default=available_regions)

filtered_df = df[(df['Year'].isin(selected_years)) & (df['Region'].isin(selected_regions))]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# ==========================================
# 4. Header & Top-Tier KPIs
# ==========================================
st.title("PrimeMart Nigeria Ltd. - Executive Summary")
st.markdown("*Strategic performance diagnostic and cross-sectional analysis by Elijah & Faruk.*")

col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
col_kpi1.metric("Total Revenue (NGN)", f"₦{filtered_df['Sales_NGN'].sum():,.0f}")
col_kpi2.metric("Total Units Sold", f"{filtered_df['Units_Sold'].sum():,.0f}")
col_kpi3.metric("Avg. Order Value", f"₦{filtered_df['Sales_NGN'].mean():,.2f}")
col_kpi4.metric("Total Transactions", f"{filtered_df['Transaction_ID'].nunique():,.0f}")

st.markdown("---")

# ==========================================
# 5. NEW ROW 1: Deep Dive (Product Leadership & Heatmap)
# ==========================================
st.subheader("I. Performance Hotspots & Product Drivers")
col_r1_1, col_r1_2 = st.columns(2)

with col_r1_1:
    top_products_df = filtered_df.groupby('Product')['Sales_NGN'].sum().nlargest(10).reset_index().sort_values('Sales_NGN', ascending=True)
    fig_top_products = px.bar(
        top_products_df, x='Sales_NGN', y='Product', orientation='h',
        title="Top 10 Products by Total Revenue",
        color='Sales_NGN', color_continuous_scale="Blues"
    )
    fig_top_products.update_layout(showlegend=False, xaxis_title="Revenue (₦)", yaxis_title="", height=450)
    st.plotly_chart(fig_top_products, use_container_width=True)

with col_r1_2:
    heatmap_df = filtered_df.pivot_table(index='Region', columns='Category', values='Sales_NGN', aggfunc='sum').fillna(0)
    fig_heatmap = px.imshow(
        heatmap_df,
        labels=dict(x="Category", y="Region", color="Revenue (NGN)"),
        x=heatmap_df.columns, y=heatmap_df.index,
        text_auto='.2s', aspect="auto",
        title="Revenue Matrix: Region vs. Category",
        color_continuous_scale="RdYlGn" 
    )
    fig_heatmap.update_layout(height=450)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# ==========================================
# 6. NEW ROW 2: Market Segmentation (Balanced Region & Pie)
# ==========================================
st.subheader("II. Regional and Categorical Market Share")
col_r2_1, col_r2_2 = st.columns(2) # Balanced columns (1:1 ratio)

with col_r2_1:
    region_df = filtered_df.groupby('Region')['Sales_NGN'].sum().reset_index().sort_values(by='Sales_NGN', ascending=False)
    fig_region = px.bar(
        region_df, x='Sales_NGN', y='Region', orientation='h',
        title="Regional Revenue Contribution", color='Sales_NGN', color_continuous_scale="Viridis"
    )
    fig_region.update_layout(showlegend=False, xaxis_title="Revenue (₦)", yaxis_title="", height=450)
    st.plotly_chart(fig_region, use_container_width=True)

with col_r2_2:
    category_df = filtered_df.groupby('Category')['Sales_NGN'].sum().reset_index()
    fig_pie = px.pie(
        category_df, values='Sales_NGN', names='Category', 
        title="Category Market Share",
        hole=0 
    )
    # Removing legend and centering labels for a cleaner look
    fig_pie.update_layout(showlegend=True, height=550)
    fig_pie.update_traces(textinfo='label+percent', textfont_size=15)
    st.plotly_chart(fig_pie, use_container_width=True)

# ==========================================
# 7. NEW ROW 3: Revenue Trajectory (Quarterly Benchmarks)
# ==========================================
st.subheader("III. Temporal Trajectory: Quarterly Bookend Analysis")
trend_df = filtered_df.groupby(pd.Grouper(key='Date', freq='M'))['Sales_NGN'].sum().reset_index()

# Filter for the first and last months of each quarter (1, 3, 4, 6, 7, 9, 10, 12)
quarterly_months = [1, 3, 4, 6, 7, 9, 10, 12]
tick_data = trend_df[trend_df['Date'].dt.month.isin(quarterly_months)]

fig_trend = px.line(
    trend_df, x='Date', y='Sales_NGN', 
    title="Monthly Aggregated Sales with Quarterly Markers",
    labels={'Sales_NGN': 'Revenue (NGN)', 'Date': 'Timeline'},
    markers=True
)

# Detail management: Show only specific months on X-axis to avoid clutter
fig_trend.update_xaxes(
    tickmode='array',
    tickvals=tick_data['Date'],
    ticktext=tick_data['Date'].dt.strftime('%b %Y'),
    tickangle=-45,
    showgrid=True, gridwidth=1, gridcolor='rgba(211, 211, 211, 0.5)'
)
fig_trend.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(211, 211, 211, 0.5)')
fig_trend.update_layout(xaxis_title="", yaxis_title="Revenue (₦)", height=450)
st.plotly_chart(fig_trend, use_container_width=True)

# ==========================================
# 8. Raw Data Access
# ==========================================
with st.expander("🔍 Audit Trail: Raw Transactional Data"):
    st.dataframe(filtered_df.head(100), use_container_width=True)