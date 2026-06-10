import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# ----------------------------------------------------
# 1. Page Configuration & Aesthetic Theme
# ----------------------------------------------------
st.set_page_config(
    page_title="AOS102 Ultimate App", 
    page_icon="🌍", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for legibility fix and Cute Climate Theme
st.markdown("""
<style>
    /* Force a light background to prevent dark-mode text invisibility */
    .stApp { background-color: #FAFAFA; } 
    
    /* Explicitly Fix the Sidebar Legibility */
    [data-testid="stSidebar"] {
        background-color: #F8FAFC !important; /* Soft, light slate background */
    }
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label {
        color: #0F172A !important; /* Explicitly dark text for all sidebar elements */
    }
    
    /* Cute Earthy Green Lecture Cards */
    .lecture-card { 
        background-color: #F0FDF4; /* Soft mint/earth green */
        color: #064E3B !important; /* Explicitly dark forest green text */
        padding: 25px; 
        border-radius: 12px; 
        border-left: 6px solid #10B981; /* Bright emerald border */
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
        margin-bottom: 20px; 
    }
    .lecture-card p, .lecture-card ul, .lecture-card li { 
        color: #064E3B !important; 
        font-size: 1.05rem;
    }
    .lecture-card h3, .lecture-card h4 {
        color: #047857 !important;
    }

    /* Cute Ocean Blue Quiz Cards */
    .quiz-card { 
        background-color: #EFF6FF; /* Soft ocean blue */
        color: #1E3A8A !important; /* Explicitly dark navy blue text */
        padding: 25px; 
        border-radius: 12px; 
        border: 2px solid #BFDBFE; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-top: 20px; 
    }
    .quiz-card h3 {
        color: #1D4ED8 !important;
    }
    
    /* Headers & Text Fixes */
    h1 { color: #047857 !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h2 { color: #0284C7 !important; }
    
    /* Force Streamlit UI elements (like radio buttons) to be legible */
    .stRadio > label { font-weight: bold; color: #0F172A !important; }
    div[role="radiogroup"] label { color: #0F172A !important; }
    div[data-testid="stMarkdownContainer"] p { color: #1F2937; } /* Default text color */
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. Gamification State Engine
# ----------------------------------------------------
MODULES = [
    "🏠 Welcome & Logistics",
    "📊 Ch 1: Overview & Variability",
    "☀️ Ch 2: Basics of Global Climate",
    "🌀 Ch 3: Physical Processes",
    "🌊 Ch 4: El Niño Prediction",
    "☁️ Ch 6: Greenhouse Effect & Feedbacks",
    "💻 Ch 5: Climate Models",
    "🔥 Ch 7: Scenarios & Extremes"
]

if "unlocked_idx" not in st.session_state:
    st.session_state.unlocked_idx = 0 

# ----------------------------------------------------
# 3. Sidebar Navigation Control
# ----------------------------------------------------
st.sidebar.title("🌍 AOS102 Study Hub")
st.sidebar.markdown("### **Spring 2026 Final Review**")

god_mode = st.sidebar.toggle("🔓 Unlock All Chapters (Admin Mode)", value=False)

display_modules = []
for i, mod in enumerate(MODULES):
    if god_mode or i <= st.session_state.unlocked_idx:
        display_modules.append(f"🟢 {mod}")
    else:
        display_modules.append(f"🔒 {mod}")

selected_display = st.sidebar.radio("Go to Module:", display_modules)
current_idx = display_modules.index(selected_display)

progress_percent = int((st.session_state.unlocked_idx / (len(MODULES)-1)) * 100)
st.sidebar.progress(min(progress_percent, 100))
st.sidebar.metric(label="Modules Unlocked", value=f"{st.session_state.unlocked_idx + 1} / {len(MODULES)}")

# ----------------------------------------------------
# 4. Core App Routing Engine
# ----------------------------------------------------

# --- MODULE 0: LOGISTICS ---
if current_idx == 0:
    st.title("🌍 AOS102: Climate Change & Climate Modeling")
    st.subheader("Interactive Final Exam Study Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Final Exam Date", value="June 10, 2026", delta="3:00 PM - 6:00 PM")
    with col2:
        st.metric(label="Weighting", value="35% - 45%", delta="Best-of Scheme Active")
    with col3:
        st.metric(label="Allowed Sheets", value="2 Cheat Sheets", delta="4 Pages Total")
        
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📋 Course Administration</h3>
            <p>Welcome to the custom learning environment. The final exam integrates concepts from chapters 1-4, but is heavily weighted toward chapters 5-7. The quizzes in this dashboard are modeled directly off your problem sets (e.g., CMIP6 mapping, Energy Balance Equations, and Latent Heat of Fusion mechanics).</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 Gatekeeper Check: Exam Rules</h3>', unsafe_allow_html=True)
    q1 = st.radio("Can you use an iPad to view your cheat sheets during the final exam?", [
        "Yes, as long as the WiFi is turned off.", 
        "No, electronics are completely prohibited. Hard copy only, with at least 10% in my own handwriting."
    ])
    
    if st.button("Submit Answers & Verify"):
        if q1.startswith("No"):
            st.success("🎯 Correct! Chapter 1 has been unlocked.")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 1)
        else:
            st.error("❌ Incorrect. No electronics permitted.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 1: CHAPTER 1 ---
elif current_idx == 1:
    st.title("📊 Chapter 1: Overview of Climate Variability")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Weather, Climate, and Anomalies</h3>
            <p>As seen in <b>Problem Set 1A</b>, we often analyze correlation maps between time series (like an ENSO index) and global precipitation. Because weather is inherently noisy, it is entirely possible to generate maps from completely random data that show correlation coefficients exceeding ± 0.3 by pure chance.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 Problem Set 1A Style Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("Based on your analysis of correlation maps, why must climate scientists rely on physically-based climate models rather than just finding high correlation coefficients in short observational time series?", [
        "A) Because observational time series are completely fabricated and cannot be trusted for historical analysis.",
        "B) Because random, chaotic noise in the climate system can easily produce regions of high mathematical correlation purely by chance, creating false 'teleconnections' without statistical significance.",
        "C) Because the Earth's climate does not exhibit natural internal variability, making correlation maps useless."
    ])
    
    if st.button("Submit Module 1 Quiz"):
        if q.startswith("B"):
            st.success("🎯 Mastered! As the HW noted, random noise can easily fool you if you don't know the time series is random.")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 2)
        else:
            st.error("❌ Incorrect. Review Problem Set 1A regarding random time series mapping.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 2: CHAPTER 2 ---
elif current_idx == 2:
    st.title("☀️ Chapter 2: Basics of Global Climate")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Albedo and Energy Balance</h3>
            <p>From <b>Problem Set 1B</b>: If we try to change the temperature of the Earth by artificially paving an area the size of California with a highly reflective substance (albedo = 0.9), it alters the Earth's weighted average albedo. This directly changes the absorbed solar radiation (S₀ (1 - α_new)).</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 Problem Set 1B Style Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("If you calculate a new, slightly higher global weighted albedo (e.g., from 0.30 to 0.3005) due to massive geoengineering, and plug it into the basic no-atmosphere energy balance equation, what is the direct mathematical result?", [
        "A) The outgoing longwave radiation will immediately increase to compensate for the reflection.",
        "B) The calculated global average surface emission temperature will slightly decrease, because the system is absorbing less incoming shortwave radiation.",
        "C) The temperature will increase because the albedo traps infrared radiation."
    ])
    
    if st.button("Submit Module 2 Quiz"):
        if q.startswith("B"):
            st.success("🎯 Correct! Absorbing less solar energy means a cooler emission temperature. Chapter 3 unlocked.")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 3)
        else:
            st.error("❌ Incorrect. Albedo reflects shortwave solar radiation away from the Earth.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 3: CHAPTER 3 ---
elif current_idx == 3:
    st.title("🌀 Chapter 3: Physical Processes in the Climate System")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Geostrophic Balance</h3>
            <p>Fluid dynamics in the atmosphere rely on an approximate balance between the Coriolis force and the pressure gradient force (PGF).</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 3 Dynamics Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("Away from surface friction and the equator, geostrophic balance dictates that wind flows:", [
        "A) Directly across isobars from high pressure to low pressure.",
        "B) Vertically upwards to balance the force of gravity.",
        "C) Parallel to the isobars, as the Coriolis force perfectly balances the Pressure Gradient Force."
    ])
    
    if st.button("Submit Module 3 Quiz"):
        if q.startswith("C"):
            st.success("🎯 Excellent physical intuition! Chapter 4 is now open.")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 4)
        else:
            st.error("❌ Incorrect. Geostrophic balance causes flow along the lines of constant pressure.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 4: CHAPTER 4 ---
elif current_idx == 4:
    st.title("🌊 Chapter 4: El Niño and Prediction")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: ENSO Probability Shifts</h3>
            <p>During the mature warm phase of El Niño, atmospheric conditions shift dramatically. However, the internal chaotic variability of the atmosphere means that we can only speak in probabilities, not guarantees.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 ENSO Probability Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("When analyzing ensemble model runs of precipitation during strong El Niño years, why don't all the simulations produce the exact same rainfall totals for California?", [
        "A) Because climate models do not conserve momentum or energy properly.",
        "B) Because slightly different initial atmospheric conditions lead to chaotic, divergent weather storm tracks within the season, even with the exact same El Niño SST forcing.",
        "C) Because the El Niño sea surface temperatures fluctuate wildly on a day-to-day basis during the winter."
    ])
    
    if st.button("Submit Module 4 Quiz"):
        if q.startswith("B"):
            st.success("🎯 Correct! Heading to Chapter 6 (following the syllabus roadmap).")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 5)
        else:
            st.error("❌ Review the concept of 'weather noise' and shifting probability distributions.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 5: CHAPTER 6 ---
elif current_idx == 5:
    st.title("☁️ Chapter 6: Greenhouse Effect & Feedbacks")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Simple Climate Models & Heat Storage</h3>
            <p>From <b>Problem Set 3A</b>: The global average climate model taking into account ocean heat capacity is written as:</p>
            <p style="text-align:center;"><b>C (∂ΔT_s / ∂t) + αΔT_s = G + N</b></p>
            <p>Where C is the heat capacity of the upper ocean, α is the climate feedback parameter, and G is the radiative forcing from greenhouse gases.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 Problem Set 3A Style Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("In the equation above, what physical phenomenon explains why the surface temperature (ΔT_s) continues to rise slowly for decades even if the greenhouse gas forcing (G) is suddenly held perfectly constant?", [
        "A) The heat capacity of the ocean (C) absorbs the initial energy imbalance, causing a massive thermal lag between the forcing applied and the eventual equilibrium temperature.",
        "B) The climate feedback parameter (α) continuously increases over time, generating its own energy.",
        "C) The weather noise (N) dominates the equation on decadal timescales."
    ])
    
    if st.button("Submit Module 6 Quiz"):
        if q.startswith("A"):
            st.success("🎯 Spot on! The immense thermal inertia of the ocean creates 'committed warming'.")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 6)
        else:
            st.error("❌ Incorrect. The ocean's heat capacity (C) dictates the transient response lag.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 6: CHAPTER 5 ---
elif current_idx == 6:
    st.title("💻 Chapter 5: Climate Models & Ensembles")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: CMIP Projections & Uncertainty</h3>
            <p>From <b>Problem Set 3B</b>: When projecting future states (like 2080-2100 precipitation), CMIP6 models generate maps where certain regions are 'hatched'. This hatching indicates areas where the projected change is less than 1 standard deviation across the model ensemble from simulations of the baseline climatology.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown('<div class="quiz-card"><h3>🧠 Problem Set 3B Style Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("When analyzing a CMIP6 precipitation map under the SSP1-2.6 scenario, you notice a region is highly hatched. What does this statistically imply about the models' prediction for that specific region?", [
        "A) It implies absolute certainty; all models agree the precipitation will increase dramatically.",
        "B) It implies that the climate signal (the forced change) is smaller than the combination of natural variability and model disagreement, meaning we have low confidence in the predicted change.",
        "C) It implies that the grid resolution of the models was too small to render that geographical location."
    ])
    
    if st.button("Submit Module 5 Quiz"):
        if q.startswith("B"):
            st.success("🎯 Beautiful statistical analysis! You've unlocked the final module.")
            st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, 7)
        else:
            st.error("❌ Incorrect. Hatching indicates that the noise/uncertainty is masking the climate signal.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 7: CHAPTER 7 ---
elif current_idx == 7:
    st.title("🔥 Chapter 7: Scenarios, Extremes & Soil Moisture")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Evapotranspiration & Cryosphere Melt</h3>
            <p>From <b>Problem Set 3B</b> and <b>Problem Set 2</b>:</p>
            <ul>
                <li><b>Soil Moisture (PET):</b> Even if regional precipitation remains flat, soil moisture can drastically decline because higher temperatures drive massive increases in Potential Evapotranspiration (PET).</li>
                <li><b>Ice Melt & Sea Level:</b> Melting an ice sheet requires overcoming the Latent Heat of Fusion (L_f = 3.3 × 10⁵ J/kg). The surface energy imbalance dictates the exact rate of m/yr at which this ice mass converts to sea-level rise.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Interactive distribution simulator
    st.subheader("🛠️ Extreme Evapotranspiration / Temperature Simulator")
    shift = st.slider("Simulate Global Mean Warming Trend (Δ°C):", 0.0, 4.0, 1.5, 0.1)
    
    x = np.linspace(-6, 10, 1000)
    y_base = stats.norm.pdf(x, 0, 1.5)
    y_shifted = stats.norm.pdf(x, shift, 1.5)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y_base, label="Historical Baseline Climate", color="#1E3A8A", linewidth=2)
    ax.plot(x, y_shifted, label=f"Warmed Future State (+{shift}°C)", color="#EF4444", linewidth=2)
    
    threshold = 2.5
    ax.axvline(x=threshold, color='#0F172A', linestyle='--', alpha=0.7, label="Severe Heat/Drought Cutoff")
    ax.fill_between(x, y_shifted, 0, where=(x > threshold), color='#EF4444', alpha=0.25)
    ax.legend(loc="upper left")
    
    # Make Matplotlib transparent so it fits the new theme well
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    st.pyplot(fig)

    st.markdown('<div class="quiz-card"><h3>🎓 Final HW Master Challenge</h3>', unsafe_allow_html=True)
    q = st.radio("Based on your CMIP6 mapping from Problem Set 3B, why are researchers deeply concerned about severe summer soil moisture depletion in the Northern Hemisphere even in regions where precipitation does not significantly decrease?", [
        "A) Because the latent heat of fusion extracts moisture directly from the soil into the atmosphere.",
        "B) Because the underlying warming trend drastically increases the Potential Evapotranspiration (PET) rate, causing the atmosphere to evaporate water out of the soil faster than the stable precipitation can replace it.",
        "C) Because increased atmospheric CO2 physically seals the pores of the soil, preventing rain from entering."
    ])
    
    if st.button("Submit Final Master Review Quiz"):
        if q.startswith("B"):
            st.success("🎉 Comprehensive Course Mastery Achieved! You understand the PET dynamic perfectly. You are officially prepared for the AOS102 Final Exam!")
            st.balloons()
        else:
            st.error("❌ Take another look at the definition of Potential Evapotranspiration (PET).")
    st.markdown('</div>', unsafe_allow_html=True)
