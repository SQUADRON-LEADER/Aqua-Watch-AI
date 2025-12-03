# Import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="AquaWatch AI",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2e86ab;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .info-box {
        background-color: #000000;
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid #29b6f6;
        margin: 1rem 0;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Load the model and structure
@st.cache_resource
def load_model():
    """Load the trained pollution prediction model and its features"""
    try:
        model = joblib.load("pollution_model.pkl")
        model_cols = joblib.load("model_columns.pkl")
        st.success("✅ Trained model loaded successfully!")
        return model, model_cols
    except FileNotFoundError:
        st.error("❌ Model files not found! Please ensure 'pollution_model.pkl' and 'model_columns.pkl' are in the current directory.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

# Initialize the trained model
model, model_cols = load_model()

# Display model info
def display_model_info():
    """Display information about the trained model"""
    st.sidebar.markdown("### 🤖 Model Information")
    st.sidebar.info(f"""
    **Trained Model Features:**
    - Model Type: {type(model).__name__}
    - Features: {len(model_cols)} input features
    - Predictions: 6 pollutant parameters
    - TDS: Calculated from model outputs
    """)

display_model_info()

# Load the original dataset for reference
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("PB_All_2000_2021.csv", sep=";")
        df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
        df['year'] = df['date'].dt.year
        return df
    except FileNotFoundError:
        st.warning("Dataset file not found. Some features may be limited.")
        return None

# Create station mapping with states and cities
@st.cache_data
def get_station_mapping():
    """Create a mapping of station IDs to states and cities"""
    station_mapping = {
        # Maharashtra - Mumbai & Pune
        1: {"state": "Maharashtra", "city": "Mumbai", "location": "Powai Lake"},
        2: {"state": "Maharashtra", "city": "Mumbai", "location": "Mithi River"},
        3: {"state": "Maharashtra", "city": "Mumbai", "location": "Mahim Creek"},
        4: {"state": "Maharashtra", "city": "Mumbai", "location": "Thane Creek"},
        5: {"state": "Maharashtra", "city": "Pune", "location": "Mutha River"},
        6: {"state": "Maharashtra", "city": "Pune", "location": "Mula River"},
        7: {"state": "Maharashtra", "city": "Nagpur", "location": "Nag River"},
        8: {"state": "Maharashtra", "city": "Nashik", "location": "Godavari River"},
        
        # Tamil Nadu - Chennai & other cities
        9: {"state": "Tamil Nadu", "city": "Chennai", "location": "Cooum River"},
        10: {"state": "Tamil Nadu", "city": "Chennai", "location": "Adyar River"},
        11: {"state": "Tamil Nadu", "city": "Chennai", "location": "Buckingham Canal"},
        12: {"state": "Tamil Nadu", "city": "Chennai", "location": "Kosasthalaiyar River"},
        13: {"state": "Tamil Nadu", "city": "Coimbatore", "location": "Noyyal River"},
        14: {"state": "Tamil Nadu", "city": "Madurai", "location": "Vaigai River"},
        15: {"state": "Tamil Nadu", "city": "Tiruchirappalli", "location": "Kaveri River"},
        16: {"state": "Tamil Nadu", "city": "Salem", "location": "Thirumanimutharu River"},
        
        # Karnataka - Bangalore & other cities
        17: {"state": "Karnataka", "city": "Bangalore", "location": "Vrishabhavathi River"},
        18: {"state": "Karnataka", "city": "Bangalore", "location": "Hebbal Lake"},
        19: {"state": "Karnataka", "city": "Bangalore", "location": "Bellandur Lake"},
        20: {"state": "Karnataka", "city": "Mysore", "location": "Kaveri River"},
        21: {"state": "Karnataka", "city": "Hubli", "location": "Dharwad River"},
        22: {"state": "Karnataka", "city": "Mangalore", "location": "Netravati River"},
        
        # Delhi NCR
        23: {"state": "Delhi", "city": "New Delhi", "location": "Yamuna River"},
        24: {"state": "Delhi", "city": "Delhi", "location": "Najafgarh Drain"},
        25: {"state": "Delhi", "city": "Delhi", "location": "Hindon River"},
        26: {"state": "Haryana", "city": "Gurgaon", "location": "Najafgarh Drain"},
        27: {"state": "Haryana", "city": "Faridabad", "location": "Yamuna River"},
        28: {"state": "Uttar Pradesh", "city": "Noida", "location": "Hindon River"},
        29: {"state": "Uttar Pradesh", "city": "Ghaziabad", "location": "Hindon River"},
        
        # Andhra Pradesh & Telangana
        30: {"state": "Telangana", "city": "Hyderabad", "location": "Hussain Sagar Lake"},
        31: {"state": "Telangana", "city": "Hyderabad", "location": "Musi River"},
        32: {"state": "Andhra Pradesh", "city": "Visakhapatnam", "location": "Gosthani River"},
        33: {"state": "Andhra Pradesh", "city": "Vijayawada", "location": "Krishna River"},
        34: {"state": "Andhra Pradesh", "city": "Tirupati", "location": "Swarnamukhi River"},
        
        # Gujarat
        35: {"state": "Gujarat", "city": "Ahmedabad", "location": "Sabarmati River"},
        36: {"state": "Gujarat", "city": "Surat", "location": "Tapi River"},
        37: {"state": "Gujarat", "city": "Vadodara", "location": "Vishwamitri River"},
        38: {"state": "Gujarat", "city": "Rajkot", "location": "Aji River"},
        
        # West Bengal
        39: {"state": "West Bengal", "city": "Kolkata", "location": "Hooghly River"},
        40: {"state": "West Bengal", "city": "Kolkata", "location": "Salt Lake"},
        41: {"state": "West Bengal", "city": "Durgapur", "location": "Damodar River"},
        42: {"state": "West Bengal", "city": "Siliguri", "location": "Mahananda River"},
        
        # Kerala
        43: {"state": "Kerala", "city": "Kochi", "location": "Periyar River"},
        44: {"state": "Kerala", "city": "Trivandrum", "location": "Karamana River"},
        45: {"state": "Kerala", "city": "Kozhikode", "location": "Kallai River"},
        46: {"state": "Kerala", "city": "Thrissur", "location": "Bharathapuzha River"},
        
        # Rajasthan
        47: {"state": "Rajasthan", "city": "Jaipur", "location": "Mansagar Lake"},
        48: {"state": "Rajasthan", "city": "Udaipur", "location": "Lake Pichola"},
        49: {"state": "Rajasthan", "city": "Jodhpur", "location": "Kaylana Lake"},
        50: {"state": "Rajasthan", "city": "Kota", "location": "Chambal River"},
        
        # Punjab
        51: {"state": "Punjab", "city": "Ludhiana", "location": "Sutlej River"},
        52: {"state": "Punjab", "city": "Amritsar", "location": "Beas River"},
        53: {"state": "Punjab", "city": "Jalandhar", "location": "Sutlej River"},
        54: {"state": "Punjab", "city": "Patiala", "location": "Ghaggar River"},
        
        # Uttar Pradesh
        55: {"state": "Uttar Pradesh", "city": "Lucknow", "location": "Gomti River"},
        56: {"state": "Uttar Pradesh", "city": "Kanpur", "location": "Ganga River"},
        57: {"state": "Uttar Pradesh", "city": "Agra", "location": "Yamuna River"},
        58: {"state": "Uttar Pradesh", "city": "Varanasi", "location": "Ganga River"},
        59: {"state": "Uttar Pradesh", "city": "Meerut", "location": "Ganga Canal"},
        60: {"state": "Uttar Pradesh", "city": "Allahabad", "location": "Sangam Point"},
        
        # Madhya Pradesh
        61: {"state": "Madhya Pradesh", "city": "Bhopal", "location": "Upper Lake"},
        62: {"state": "Madhya Pradesh", "city": "Indore", "location": "Khan River"},
        63: {"state": "Madhya Pradesh", "city": "Jabalpur", "location": "Narmada River"},
        64: {"state": "Madhya Pradesh", "city": "Gwalior", "location": "Chambal River"},
        
        # Bihar & Jharkhand
        65: {"state": "Bihar", "city": "Patna", "location": "Ganga River"},
        66: {"state": "Bihar", "city": "Gaya", "location": "Falgu River"},
        67: {"state": "Jharkhand", "city": "Ranchi", "location": "Subarnarekha River"},
        68: {"state": "Jharkhand", "city": "Jamshedpur", "location": "Subarnarekha River"},
        
        # Odisha
        69: {"state": "Odisha", "city": "Bhubaneswar", "location": "Kuakhai River"},
        70: {"state": "Odisha", "city": "Cuttack", "location": "Mahanadi River"},
        
        # Assam & Northeast
        71: {"state": "Assam", "city": "Guwahati", "location": "Brahmaputra River"},
        72: {"state": "Assam", "city": "Dibrugarh", "location": "Brahmaputra River"},
        
        # Himachal Pradesh & Uttarakhand
        73: {"state": "Himachal Pradesh", "city": "Shimla", "location": "Sutlej River"},
        74: {"state": "Himachal Pradesh", "city": "Manali", "location": "Beas River"},
        75: {"state": "Himachal Pradesh", "city": "Dharamshala", "location": "Banganga River"},
        76: {"state": "Uttarakhand", "city": "Dehradun", "location": "Rispana River"},
        77: {"state": "Uttarakhand", "city": "Haridwar", "location": "Ganga River"},
        78: {"state": "Uttarakhand", "city": "Rishikesh", "location": "Ganga River"},
        79: {"state": "Uttarakhand", "city": "Nainital", "location": "Naini Lake"},
        
        # Jammu & Kashmir
        80: {"state": "Jammu & Kashmir", "city": "Srinagar", "location": "Dal Lake"},
        81: {"state": "Jammu & Kashmir", "city": "Srinagar", "location": "Jhelum River"},
        82: {"state": "Jammu & Kashmir", "city": "Jammu", "location": "Tawi River"},
        83: {"state": "Jammu & Kashmir", "city": "Leh", "location": "Indus River"},
        
        # Chhattisgarh
        84: {"state": "Chhattisgarh", "city": "Raipur", "location": "Mahanadi River"},
        85: {"state": "Chhattisgarh", "city": "Bilaspur", "location": "Arpa River"},
        86: {"state": "Chhattisgarh", "city": "Durg", "location": "Shivnath River"},
        
        # Goa
        87: {"state": "Goa", "city": "Panaji", "location": "Mandovi River"},
        88: {"state": "Goa", "city": "Margao", "location": "Sal River"},
        89: {"state": "Goa", "city": "Vasco da Gama", "location": "Zuari River"},
        
        # Tripura & Northeast States
        90: {"state": "Tripura", "city": "Agartala", "location": "Haora River"},
        91: {"state": "Manipur", "city": "Imphal", "location": "Imphal River"},
        92: {"state": "Meghalaya", "city": "Shillong", "location": "Umiam Lake"},
        93: {"state": "Mizoram", "city": "Aizawl", "location": "Tlawng River"},
        94: {"state": "Nagaland", "city": "Kohima", "location": "Doyang River"},
        95: {"state": "Arunachal Pradesh", "city": "Itanagar", "location": "Pare River"},
        96: {"state": "Sikkim", "city": "Gangtok", "location": "Teesta River"},
        
        # Additional Maharashtra stations
        97: {"state": "Maharashtra", "city": "Aurangabad", "location": "Kham River"},
        98: {"state": "Maharashtra", "city": "Solapur", "location": "Sina River"},
        99: {"state": "Maharashtra", "city": "Kolhapur", "location": "Panchganga River"},
        100: {"state": "Maharashtra", "city": "Sangli", "location": "Krishna River"},
        
        # Additional Tamil Nadu stations
        101: {"state": "Tamil Nadu", "city": "Vellore", "location": "Palar River"},
        102: {"state": "Tamil Nadu", "city": "Tirunelveli", "location": "Thamirabarani River"},
        103: {"state": "Tamil Nadu", "city": "Erode", "location": "Kaveri River"},
        104: {"state": "Tamil Nadu", "city": "Thanjavur", "location": "Kaveri River"},
        105: {"state": "Tamil Nadu", "city": "Kanchipuram", "location": "Vegavathi River"},
        
        # Additional Karnataka stations
        106: {"state": "Karnataka", "city": "Belgaum", "location": "Ghataprabha River"},
        107: {"state": "Karnataka", "city": "Gulbarga", "location": "Bhima River"},
        108: {"state": "Karnataka", "city": "Davangere", "location": "Tungabhadra River"},
        109: {"state": "Karnataka", "city": "Shimoga", "location": "Tunga River"},
        110: {"state": "Karnataka", "city": "Hassan", "location": "Hemavati River"},
        
        # Additional Andhra Pradesh stations
        111: {"state": "Andhra Pradesh", "city": "Guntur", "location": "Krishna River"},
        112: {"state": "Andhra Pradesh", "city": "Nellore", "location": "Pennar River"},
        113: {"state": "Andhra Pradesh", "city": "Kakinada", "location": "Godavari River"},
        114: {"state": "Andhra Pradesh", "city": "Anantapur", "location": "Pennar River"},
        115: {"state": "Andhra Pradesh", "city": "Kurnool", "location": "Tungabhadra River"},
        
        # Additional Gujarat stations
        116: {"state": "Gujarat", "city": "Gandhinagar", "location": "Sabarmati River"},
        117: {"state": "Gujarat", "city": "Bhavnagar", "location": "Gaurishankar Lake"},
        118: {"state": "Gujarat", "city": "Jamnagar", "location": "Lakhota Lake"},
        119: {"state": "Gujarat", "city": "Junagadh", "location": "Kalwa River"},
        120: {"state": "Gujarat", "city": "Anand", "location": "Watrak River"},
        
        # Additional West Bengal stations
        121: {"state": "West Bengal", "city": "Howrah", "location": "Hooghly River"},
        122: {"state": "West Bengal", "city": "Malda", "location": "Mahananda River"},
        123: {"state": "West Bengal", "city": "Asansol", "location": "Damodar River"},
        124: {"state": "West Bengal", "city": "Darjeeling", "location": "Teesta River"},
        
        # Additional Kerala stations
        125: {"state": "Kerala", "city": "Kannur", "location": "Valapattanam River"},
        126: {"state": "Kerala", "city": "Kollam", "location": "Ashtamudi Lake"},
        127: {"state": "Kerala", "city": "Palakkad", "location": "Bharathapuzha River"},
        128: {"state": "Kerala", "city": "Alappuzha", "location": "Vembanad Lake"},
        
        # Additional Rajasthan stations
        129: {"state": "Rajasthan", "city": "Bikaner", "location": "Gajner Lake"},
        130: {"state": "Rajasthan", "city": "Ajmer", "location": "Ana Sagar Lake"},
        131: {"state": "Rajasthan", "city": "Alwar", "location": "Siliserh Lake"},
        132: {"state": "Rajasthan", "city": "Bharatpur", "location": "Ajan Bund"},
        
        # Additional Punjab & Haryana stations
        133: {"state": "Punjab", "city": "Bathinda", "location": "Ghaggar River"},
        134: {"state": "Punjab", "city": "Mohali", "location": "Ghaggar River"},
        135: {"state": "Haryana", "city": "Panipat", "location": "Yamuna River"},
        136: {"state": "Haryana", "city": "Karnal", "location": "Yamuna River"},
        137: {"state": "Haryana", "city": "Hisar", "location": "Ghaggar River"},
        138: {"state": "Haryana", "city": "Rohtak", "location": "Drainage Canal"},
        
        # Additional UP stations
        139: {"state": "Uttar Pradesh", "city": "Bareilly", "location": "Ramganga River"},
        140: {"state": "Uttar Pradesh", "city": "Moradabad", "location": "Ramganga River"},
        141: {"state": "Uttar Pradesh", "city": "Saharanpur", "location": "Yamuna River"},
        142: {"state": "Uttar Pradesh", "city": "Gorakhpur", "location": "Rapti River"},
        143: {"state": "Uttar Pradesh", "city": "Mathura", "location": "Yamuna River"},
        144: {"state": "Uttar Pradesh", "city": "Firozabad", "location": "Yamuna River"},
        145: {"state": "Uttar Pradesh", "city": "Aligarh", "location": "Kali River"},
        
        # Additional MP stations
        146: {"state": "Madhya Pradesh", "city": "Ujjain", "location": "Shipra River"},
        147: {"state": "Madhya Pradesh", "city": "Sagar", "location": "Bina River"},
        148: {"state": "Madhya Pradesh", "city": "Rewa", "location": "Tons River"},
        149: {"state": "Madhya Pradesh", "city": "Satna", "location": "Tons River"},
        150: {"state": "Madhya Pradesh", "city": "Dewas", "location": "Kshipra River"}
    }
    return station_mapping

df = load_data()
station_mapping = get_station_mapping()

# Main title
st.markdown('<h1 class="main-header">💧 Water Quality Prediction System</h1>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["🔮 Prediction", "📊 Data Analysis", "ℹ️ About"])

if page == "🔮 Prediction":
    st.markdown('<h2 class="sub-header">🔮 Pollutant Level Prediction</h2>', unsafe_allow_html=True)
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ⚙️ Location & Time Parameters")
        
        # State selection
        available_states = sorted(list(set([info["state"] for info in station_mapping.values()])))
        selected_state = st.selectbox(
            "️ Select State", 
            options=["All States"] + available_states,
            help="Choose a state to filter cities and monitoring stations"
        )
        
        # City selection based on state
        if selected_state == "All States":
            available_cities = sorted(list(set([info["city"] for info in station_mapping.values()])))
            selected_city = st.selectbox(
                "🏙️ Select City", 
                options=["All Cities"] + available_cities,
                help="Choose a city to view water quality data"
            )
        else:
            state_cities = [info["city"] for info in station_mapping.values() if info["state"] == selected_state]
            available_cities = sorted(list(set(state_cities)))
            selected_city = st.selectbox(
                "🏙️ Select City", 
                options=["All Cities"] + available_cities,
                help="Choose a city to view water quality data"
            )
        
        # Station selection based on city
        if selected_city == "All Cities":
            if selected_state == "All States":
                available_stations = sorted(list(station_mapping.keys()))
            else:
                available_stations = [sid for sid, info in station_mapping.items() if info["state"] == selected_state]
        else:
            available_stations = [sid for sid, info in station_mapping.items() if info["city"] == selected_city]
        
        # Create station options with location details
        station_options = []
        for sid in available_stations:
            info = station_mapping[sid]
            station_options.append(f"Station {sid} - {info['location']}")
        
        selected_station_display = st.selectbox(
            "🏭 Select Monitoring Station", 
            options=station_options,
            help="Choose from available water quality monitoring stations"
        )
        
        # Extract station ID from selection
        station_id = int(selected_station_display.split(" ")[1])
        
        year_input = st.number_input(
            "📅 Select Year", 
            min_value=2000, 
            max_value=2030, 
            value=2022,
            help="Enter the year for prediction (2000-2030)"
        )
        
        # Display selected location info
        selected_info = station_mapping[station_id]
        st.info(f"📍 **Selected Location:**\n\n"
                f"**State:** {selected_info['state']}\n\n"
                f"**City:** {selected_info['city']}\n\n"
                f"**Monitoring Point:** {selected_info['location']}")
    
    with col2:
        st.markdown("### 🧪 Water Quality Parameters")
        st.markdown("""
        <div class="info-box">
        <strong style="color: #ffffff; font-size: 1.1em;">Parameters measured & calculated:</strong><br><br>
        • <strong style="color: #29b6f6;">O2</strong>: <span style="color: #ffffff;">Dissolved Oxygen (mg/L) - Essential for aquatic life</span><br>
        • <strong style="color: #29b6f6;">NO3</strong>: <span style="color: #ffffff;">Nitrate (mg/L) - Agricultural runoff indicator</span><br>
        • <strong style="color: #29b6f6;">NO2</strong>: <span style="color: #ffffff;">Nitrite (mg/L) - Industrial pollution marker</span><br>
        • <strong style="color: #29b6f6;">SO4</strong>: <span style="color: #ffffff;">Sulfate (mg/L) - Natural minerals & acid rain</span><br>
        • <strong style="color: #29b6f6;">PO4</strong>: <span style="color: #ffffff;">Phosphate (mg/L) - Detergents & fertilizers</span><br>
        • <strong style="color: #29b6f6;">CL</strong>: <span style="color: #ffffff;">Chloride (mg/L) - Salinity & taste indicator</span><br>
        • <strong style="color: #ff6b6b;">TDS</strong>: <span style="color: #ffffff;">Total Dissolved Solids (mg/L) - Overall mineralization</span><br><br>
        <strong style="color: #4ecdc4;">🚰 Includes comprehensive drinkability assessment based on WHO/BIS standards</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Prediction button
    if st.button('🔍 Predict Water Quality Using Trained Model', type="primary", use_container_width=True):
        if not station_id:
            st.warning('⚠️ Please enter a valid station ID')
        else:
            with st.spinner('🧠 Running your trained model prediction...'):
                # Prepare the input for your trained model
                input_df = pd.DataFrame({'year': [year_input], 'id': [str(station_id)]})
                input_encoded = pd.get_dummies(input_df, columns=['id'])

                # Align with trained model columns
                for col in model_cols:
                    if col not in input_encoded.columns:
                        input_encoded[col] = 0
                input_encoded = input_encoded[model_cols]

                # Make prediction using YOUR trained model
                predicted_pollutants = model.predict(input_encoded)[0]
                pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
                pollutant_units = ['mg/L', 'mg/L', 'mg/L', 'mg/L', 'mg/L', 'mg/L']

                # Calculate TDS (Total Dissolved Solids) from trained model predictions
                # TDS calculation based on major ions from your model's output
                tds_value = predicted_pollutants[1] + predicted_pollutants[3] + predicted_pollutants[5]  # NO3 + SO4 + CL
                tds_value += 50  # Add base minerals typically present in water

            st.success('✅ Prediction completed using your trained model!')
            
            st.markdown(f'<h3 class="sub-header">📊 AI Model Predictions for {station_mapping[station_id]["city"]}, {station_mapping[station_id]["state"]} ({year_input})</h3>', unsafe_allow_html=True)
            
            # Location details with model info
            location_info = station_mapping[station_id]
            st.markdown(f"""
            **📍 Location Details:**
            - **State:** {location_info['state']}
            - **City:** {location_info['city']}
            - **Monitoring Point:** {location_info['location']}
            - **Station ID:** {station_id}
            
            **🤖 Model Information:**
            - **Prediction Source:** Your Trained ML Model
            - **Model Type:** {type(model).__name__}
            - **Training Data:** Historical water quality dataset
            - **TDS Calculation:** Derived from model predictions (NO3 + SO4 + CL + minerals)
            """)
            
            # Display metrics in columns
            col1, col2, col3, col4 = st.columns(4)
            
            # Display pollutant metrics
            cols = [col1, col2, col3, col1, col2, col3]  # Repeat columns for 6 pollutants
            for i, (pollutant, value, unit) in enumerate(zip(pollutants, predicted_pollutants, pollutant_units)):
                with cols[i]:
                    st.metric(
                        label=f"{pollutant}",
                        value=f"{value:.2f} {unit}",
                        help=f"Predicted {pollutant} concentration"
                    )
            
            # Display TDS in the 4th column
            with col4:
                st.metric(
                    label="TDS",
                    value=f"{tds_value:.0f} mg/L",
                    help="Total Dissolved Solids (calculated from major ions)"
                )
            
            # Create visualization with TDS
            extended_pollutants = pollutants + ['TDS']
            extended_values = list(predicted_pollutants) + [tds_value]
            
            fig = go.Figure(data=[
                go.Bar(
                    x=extended_pollutants,
                    y=extended_values,
                    marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#17becf'],
                    text=[f'{val:.2f}' for val in extended_values],
                    textposition='auto',
                )
            ])
            
            fig.update_layout(
                title=f"AI Model Predictions with TDS Analysis - {location_info['city']}, {location_info['state']} ({year_input})",
                xaxis_title="Water Quality Parameters",
                yaxis_title="Concentration (mg/L)",
                template="plotly_white",
                height=500,
                annotations=[
                    dict(
                        text="Predictions from your trained ML model",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.5, y=1.1, xanchor='center', yanchor='bottom',
                        font=dict(size=12, color="grey")
                    )
                ]
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Comprehensive Water Quality Assessment with Drinkability (using trained model predictions)
            st.markdown("### 🎯 AI-Powered Water Quality Assessment & Drinkability Analysis")
            st.info("📊 **Analysis based on your trained machine learning model predictions**")
            
            # Initialize assessment variables
            quality_score = 0
            max_score = 7  # Total parameters to check
            assessments = []
            drinkability_issues = []
            
            # WHO/BIS Standards for drinking water
            standards = {
                'O2': {'min': 4.0, 'ideal_min': 6.0, 'name': 'Dissolved Oxygen'},
                'NO3': {'max': 45.0, 'name': 'Nitrate'},
                'NO2': {'max': 3.0, 'name': 'Nitrite'}, 
                'SO4': {'max': 200.0, 'name': 'Sulfate'},
                'PO4': {'max': 0.1, 'name': 'Phosphate'},
                'CL': {'max': 250.0, 'name': 'Chloride'},
                'TDS': {'max': 500.0, 'acceptable_max': 1000.0, 'name': 'Total Dissolved Solids'}
            }
            
            # Check each parameter against standards
            # Dissolved Oxygen (higher is better)
            o2_level = predicted_pollutants[0]
            if o2_level >= standards['O2']['ideal_min']:
                quality_score += 1
                assessments.append("✅ Excellent oxygen levels - supports aquatic life")
            elif o2_level >= standards['O2']['min']:
                quality_score += 0.5
                assessments.append("🟡 Adequate oxygen levels")
            else:
                assessments.append("❌ Low oxygen levels - poor water quality")
                drinkability_issues.append("Insufficient dissolved oxygen")
            
            # Nitrate
            no3_level = predicted_pollutants[1]
            if no3_level <= standards['NO3']['max']:
                quality_score += 1
                assessments.append("✅ Safe nitrate levels")
            else:
                assessments.append("❌ High nitrate levels - health risk")
                drinkability_issues.append("Nitrate exceeds safe limits")
            
            # Nitrite  
            no2_level = predicted_pollutants[2]
            if no2_level <= standards['NO2']['max']:
                quality_score += 1
                assessments.append("✅ Safe nitrite levels")
            else:
                assessments.append("❌ High nitrite levels - health risk")
                drinkability_issues.append("Nitrite exceeds safe limits")
            
            # Sulfate
            so4_level = predicted_pollutants[3]
            if so4_level <= standards['SO4']['max']:
                quality_score += 1
                assessments.append("✅ Acceptable sulfate levels")
            else:
                assessments.append("❌ High sulfate levels - may cause digestive issues")
                drinkability_issues.append("Sulfate exceeds recommended limits")
            
            # Phosphate
            po4_level = predicted_pollutants[4]
            if po4_level <= standards['PO4']['max']:
                quality_score += 1
                assessments.append("✅ Low phosphate levels")
            else:
                assessments.append("⚠️ Elevated phosphate levels - may indicate pollution")
                drinkability_issues.append("Phosphate levels elevated")
            
            # Chloride
            cl_level = predicted_pollutants[5]
            if cl_level <= standards['CL']['max']:
                quality_score += 1
                assessments.append("✅ Acceptable chloride levels")
            else:
                assessments.append("❌ High chloride levels - taste and corrosion issues")
                drinkability_issues.append("Chloride exceeds taste threshold")
            
            # TDS Assessment
            if tds_value <= standards['TDS']['max']:
                quality_score += 1
                assessments.append("✅ Excellent TDS levels - ideal for drinking")
            elif tds_value <= standards['TDS']['acceptable_max']:
                quality_score += 0.5
                assessments.append("🟡 Acceptable TDS levels - drinkable but not ideal")
            else:
                assessments.append("❌ High TDS levels - poor taste, may require treatment")
                drinkability_issues.append("TDS exceeds acceptable limits")
            
            # Display detailed assessment
            col_assess1, col_assess2 = st.columns(2)
            
            with col_assess1:
                st.markdown("#### 📋 Parameter Assessment")
                for assessment in assessments:
                    st.write(assessment)
            
            with col_assess2:
                # Overall quality score
                quality_percentage = (quality_score / max_score) * 100
                
                st.markdown("#### 🏆 Overall Quality Score")
                st.progress(quality_percentage / 100)
                st.write(f"**Score: {quality_score:.1f}/{max_score} ({quality_percentage:.1f}%)**")
                
                # Drinkability verdict
                st.markdown("#### 💧 **DRINKABILITY ASSESSMENT**")
                
                if len(drinkability_issues) == 0 and quality_percentage >= 85:
                    st.success("🟢 **SAFE TO DRINK** - Water meets drinking standards")
                    st.write("✅ This water is suitable for human consumption")
                elif len(drinkability_issues) <= 2 and quality_percentage >= 60:
                    st.warning("🟡 **CONDITIONAL DRINKING** - Minor treatment recommended")
                    st.write("⚠️ Water is generally safe but may benefit from filtration")
                    if drinkability_issues:
                        st.write("**Issues to address:**")
                        for issue in drinkability_issues:
                            st.write(f"• {issue}")
                else:
                    st.error("🔴 **NOT SAFE TO DRINK** - Treatment required")
                    st.write("❌ This water requires treatment before consumption")
                    if drinkability_issues:
                        st.write("**Critical issues:**")
                        for issue in drinkability_issues:
                            st.write(f"• {issue}")
                
                # TDS specific guidance
                st.markdown("#### 🧪 TDS Classification")
                if tds_value < 150:
                    st.info(f"TDS: {tds_value:.0f} mg/L - Low mineralization")
                elif tds_value < 300:
                    st.success(f"TDS: {tds_value:.0f} mg/L - Optimal for drinking")
                elif tds_value < 500:
                    st.warning(f"TDS: {tds_value:.0f} mg/L - Acceptable")
                elif tds_value < 1000:
                    st.warning(f"TDS: {tds_value:.0f} mg/L - Poor taste")
                else:
                    st.error(f"TDS: {tds_value:.0f} mg/L - Unacceptable for drinking")

elif page == "📊 Data Analysis":
    st.markdown('<h2 class="sub-header">📊 Historical Data Analysis</h2>', unsafe_allow_html=True)
    
    if df is not None:
        # AAdd station mapping to dataframe
        df_enhanced = df.copy()
        df_enhanced['state'] = df_enhanced['id'].map(lambda x: station_mapping[x]['state'])
        df_enhanced['city'] = df_enhanced['id'].map(lambda x: station_mapping[x]['city'])
        df_enhanced['location'] = df_enhanced['id'].map(lambda x: station_mapping[x]['location'])
        
        # ataset overview
        st.markdown("### Dataset Overview")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Records", len(df_enhanced))
        with col2:
            st.metric("States Covered", df_enhanced['state'].nunique())
        with col3:
            st.metric("Cities Monitored", df_enhanced['city'].nunique())
        with col4:
            st.metric("Years Covered", f"{df_enhanced['year'].min()}-{df_enhanced['year'].max()}")
        
        # Analysis type selection
        analysis_type = st.selectbox(
            "📈 Select Analysis Type",
            ["State-wise Comparison", "City-wise Comparison", "Pollutant Trends", "Station Comparison"]
        )
        
        if analysis_type == "State-wise Comparison":
            st.markdown("### 🗺️ State-wise Water Quality Comparison")
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
            selected_pollutant = st.selectbox("Select pollutant to analyze", pollutants)
            
            # Calculate state-wise averages
            state_data = df_enhanced.groupby('state')[selected_pollutant].mean().reset_index()
            state_data = state_data.sort_values(selected_pollutant, ascending=False)
            
            fig = px.bar(
                state_data, 
                x='state', 
                y=selected_pollutant,
                title=f'Average {selected_pollutant} Levels by State',
                labels={'state': 'State', selected_pollutant: f'{selected_pollutant} (mg/L)'},
                color=selected_pollutant,
                color_continuous_scale='blues'
            )
            fig.update_layout(template="plotly_white", height=500)
            fig.update_xaxes(tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
            
            # State ranking
            st.markdown("#### 🏆 State Rankings")
            for i, row in state_data.iterrows():
                rank = i + 1
                st.write(f"{rank}. **{row['state']}**: {row[selected_pollutant]:.2f} mg/L")
        
        elif analysis_type == "City-wise Comparison":
            st.markdown("### 🏙️ City-wise Water Quality Comparison")
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
            
            selected_pollutant = st.selectbox("Select pollutant to analyze", pollutants)
            
            # State filter for cities
            selected_state_filter = st.selectbox(
                "Filter by State (optional)",
                ["All States"] + sorted(df_enhanced['state'].unique())
            )
            
            if selected_state_filter != "All States":
                filtered_df = df_enhanced[df_enhanced['state'] == selected_state_filter]
            else:
                filtered_df = df_enhanced
            
            # Calculate city-wise averages
            city_data = filtered_df.groupby(['city', 'state'])[selected_pollutant].mean().reset_index()
            city_data = city_data.sort_values(selected_pollutant, ascending=False)
            
            fig = px.bar(
                city_data, 
                x='city', 
                y=selected_pollutant,
                color='state',
                title=f'Average {selected_pollutant} Levels by City',
                labels={'city': 'City', selected_pollutant: f'{selected_pollutant} (mg/L)'}
            )
            fig.update_layout(template="plotly_white", height=500)
            fig.update_xaxes(tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
        
        elif analysis_type == "Pollutant Trends":
            st.markdown("### 📈 Pollutant Trends Over Time")
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
            
            selected_pollutant = st.selectbox("Select pollutant to analyze", pollutants)
            
            # Geographic filter
            geo_filter = st.selectbox(
                "Geographic Filter",
                ["All Locations", "By State", "By City"]
            )
            
            if geo_filter == "By State":
                selected_states = st.multiselect(
                    "Select states", 
                    sorted(df_enhanced['state'].unique()),
                    default=[]
                )
                if selected_states:
                    plot_df = df_enhanced[df_enhanced['state'].isin(selected_states)]
                else:
                    plot_df = df_enhanced
            elif geo_filter == "By City":
                selected_cities = st.multiselect(
                    "Select cities", 
                    sorted(df_enhanced['city'].unique()),
                    default=[]
                )
                if selected_cities:
                    plot_df = df_enhanced[df_enhanced['city'].isin(selected_cities)]
                else:
                    plot_df = df_enhanced
            else:
                plot_df = df_enhanced
            
            # Group by year and calculate mean
            yearly_data = plot_df.groupby('year')[selected_pollutant].mean().reset_index()
            
            fig = px.line(
                yearly_data, 
                x='year', 
                y=selected_pollutant,
                title=f'{selected_pollutant} Trends Over Time',
                labels={'year': 'Year', selected_pollutant: f'{selected_pollutant} (mg/L)'}
            )
            
            fig.update_layout(template="plotly_white", height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        elif analysis_type == "Station Comparison":
            st.markdown("### 🏭 Station Comparison")
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
            station_comparison = df_enhanced.groupby(['id', 'state', 'city', 'location'])[pollutants].mean().reset_index()
            
            selected_pollutant = st.selectbox("Select pollutant for comparison", pollutants)
            
            fig = px.scatter(
                station_comparison,
                x='id',
                y=selected_pollutant,
                color='state',
                size=selected_pollutant,
                hover_data=['city', 'location'],
                title=f'Station-wise Average {selected_pollutant} by Station',
                labels={'id': 'Station ID', selected_pollutant: f'{selected_pollutant} (mg/L)'}
            )
            
            fig.update_layout(template="plotly_white", height=500)
            st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.error("Unable to load historical data for analysis.")

elif page == "ℹ️ About":
    st.markdown('<h2 class="sub-header">ℹ️ About This Application</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Purpose
    This Water Quality Prediction System uses machine learning to predict pollutant levels in water based on historical monitoring data from various stations.
    
    ### 🔬 Machine Learning Model
    - **Algorithm**: Random Forest Regressor with Multi-Output capability
    - **Features**: Station ID and Year
    - **Targets**: 6 different pollutant concentrations (O2, NO3, NO2, SO4, PO4, CL)
    - **Training Data**: Historical water quality measurements from 2000-2021
    
    ### 📊 Data Sources
    The model is trained on water quality monitoring data containing:
    - **22 monitoring stations**
    - **6 key pollutants**
    - **20+ years of historical data**
    
    ### 🚀 Features
    - **Real-time Predictions**: Get instant pollutant level predictions
    - **Interactive Visualizations**: Charts and graphs for better understanding
    - **Historical Analysis**: Explore trends and patterns in the data
    - **Quality Assessment**: Basic water quality evaluation
    
    ### 🛠️ Technology Stack
    - **Frontend**: Streamlit
    - **Machine Learning**: Scikit-learn
    - **Data Processing**: Pandas, NumPy
    - **Visualizations**: Plotly
    
    ### 📝 Usage Instructions
    1. Navigate to the **Prediction** page
    2. Select a year and station ID
    3. Click **Predict Water Quality**
    4. View results and quality assessment
    5. Explore historical trends in the **Data Analysis** page
    
    ### ⚠️ Disclaimer
    This tool is for educational and research purposes. For actual water quality monitoring and decision-making, please consult with environmental professionals and use certified testing methods.
    """)