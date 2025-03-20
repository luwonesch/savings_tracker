import streamlit as st

# Function to calculate missed savings
def calculate_missed_savings(data_lake_size_pb):
    PUBLIC_LIST_PRICE_PER_TB = 30  # Example public list price for cloud storage per TB per month in USD
    DISCOUNT = 0.20  # 20% discount applied to public list pricing
    COMPUTE_MULTIPLIER = 4  # Compute is 4x storage cost
    STORAGE_WASTE_PERCENTAGE = 0.50  # 50% of storage costs are wasted
    COMPUTE_WASTE_PERCENTAGE = 0.10  # 10% of compute costs are wasted

    data_lake_size_tb = data_lake_size_pb * 1000
    storage_cost_per_tb = PUBLIC_LIST_PRICE_PER_TB * (1 - DISCOUNT)
    total_storage_cost = storage_cost_per_tb * data_lake_size_tb
    total_compute_cost = total_storage_cost * COMPUTE_MULTIPLIER
    
    missed_storage_savings = total_storage_cost * STORAGE_WASTE_PERCENTAGE
    missed_compute_savings = total_compute_cost * COMPUTE_WASTE_PERCENTAGE
    total_missed_savings = missed_storage_savings + missed_compute_savings

    return {
        "Total Missed Savings": total_missed_savings,
        "Missed Storage Savings": missed_storage_savings,
        "Missed Compute Savings": missed_compute_savings,
        "Missed Savings Per Day": round(total_missed_savings / 30),
        "Missed Savings Per Week": round(total_missed_savings / 4),
        "Missed Savings Per Month": round(total_missed_savings),
    }

# UI Configuration
st.set_page_config(page_title="Cloud Data Lake Waste Calculator", layout="centered")
st.markdown(
    """
    <style>
        body, .stApp { background-color: #FFFFFF; color: #000000; }
        .big-font { font-size: 50px; font-weight: bold; color: #FFD700; text-align: center; }
        .metric-font { font-size: 30px; font-weight: bold; text-align: center; color: #000000; }
        .info-icon { font-size: 16px; color: #555555; }
        .small-input input { width: 80px !important; text-align: center !important; font-size: 20px !important; background-color: #F0F0F0; color: #000000; border: 1px solid #BBBBBB; }
        .logo { display: flex; justify-content: center; }
        .button { display: flex; justify-content: center; margin-top: 20px; }
        .stButton>button { background-color: #D3D3D3; color: #000000; font-weight: bold; border-radius: 5px; padding: 10px; }
        .stButton>button:hover { background-color: #A9A9A9; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Granica.ai logo
st.markdown("<div class='logo'><img src='https://www.granica.ai/logo.png' width='200'></div>", unsafe_allow_html=True)

st.markdown("<div class='big-font'>Cloud Data Lake Overspending</div>", unsafe_allow_html=True)

# Centered Small Input Field
data_lake_size_pb = st.number_input(
    "Enter your Data Lake Size (PB)", min_value=1, max_value=1000, value=10, step=1,
    key="data_input", format="%d",
    help="Enter the size of your data lake in petabytes (PB)."
)

# Calculate button centered
st.markdown("<div class='button'>", unsafe_allow_html=True)
if st.button("💡 See My Wasted Spend"):
    st.markdown("</div>", unsafe_allow_html=True)
    data = calculate_missed_savings(data_lake_size_pb)
    
    # Display Missed Savings with Hover Breakdown
    st.markdown(f"<div class='big-font' title='Storage: ${data['Missed Storage Savings']:,.0f}\nCompute: ${data['Missed Compute Savings']:,.0f}'>Estimated Overspending:</div>", unsafe_allow_html=True)

    st.markdown("---")
    
    # Show breakdown
    st.markdown(f"<div class='metric-font'>⏳ Per Day: ${data['Missed Savings Per Day']:,.0f}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-font'>📅 Per Week: ${data['Missed Savings Per Week']:,.0f}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-font'>📆 Per Month: ${data['Missed Savings Per Month']:,.0f}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### **Savings powered by Granica.ai**", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
