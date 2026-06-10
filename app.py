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

st.markdown("""
<style>
    .stApp { background-color: #FAFAFA; } 
    [data-testid="stSidebar"] { background-color: #F8FAFC !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {
        color: #0F172A !important; 
    }
    .lecture-card { 
        background-color: #F0FDF4; color: #064E3B !important; padding: 25px; 
        border-radius: 12px; border-left: 6px solid #10B981; box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
        margin-bottom: 20px; 
    }
    .lecture-card p, .lecture-card ul, .lecture-card li { color: #064E3B !important; font-size: 1.05rem; }
    .lecture-card h3, .lecture-card h4 { color: #047857 !important; }
    .quiz-card { 
        background-color: #EFF6FF; color: #1E3A8A !important; padding: 25px; 
        border-radius: 12px; border: 2px solid #BFDBFE; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-top: 20px; 
    }
    .quiz-card h3 { color: #1D4ED8 !important; }
    h1 { color: #047857 !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h2 { color: #0284C7 !important; }
    .stRadio > label { font-weight: bold; color: #0F172A !important; }
    div[role="radiogroup"] label { color: #0F172A !important; }
    div[data-testid="stMarkdownContainer"] p { color: #1F2937; } 
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
st.sidebar.metric(label="Course Progress", value=f"{st.session_state.unlocked_idx + 1} / {len(MODULES)} Unlocked")

# Helper function for 5-question quizzes
def render_quiz(questions, module_idx):
    st.markdown('<div class="quiz-card"><h3>🧠 Gatekeeper Quiz: Pass to Unlock Next Chapter</h3>', unsafe_allow_html=True)
    with st.form(key=f"quiz_form_{module_idx}"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            ans = st.radio("Select an answer:", q['options'], key=f"q_{module_idx}_{i}", label_visibility="collapsed")
            user_answers.append(ans)
            st.write("---")
        
        submitted = st.form_submit_button("Submit 5 Answers")
        if submitted:
            score = sum([1 for i, ans in enumerate(user_answers) if ans == questions[i]['correct']])
            if score == 5:
                st.success("🎯 Perfect Score (5/5)! You have unlocked the next module.")
                st.session_state.unlocked_idx = max(st.session_state.unlocked_idx, module_idx + 1)
                st.balloons()
            else:
                st.error(f"❌ You scored {score}/5. Review the notes and try again to unlock the next section!")
    st.markdown('</div>', unsafe_allow_html=True)

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
            <p>Welcome to the ultimate learning environment. The final exam integrates concepts from chapters 1-4, but is heavily weighted toward chapters 5-7. Pass the 5-question quizzes at the end of every chapter to prove your knowledge and unlock the next module.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "How many double-sided notes pages are allowed for the final?", "options": ["1 page", "2 pages (4 sides)", "Open book"], "correct": "2 pages (4 sides)"},
        {"question": "What percentage of each notes page MUST be in your own handwriting?", "options": ["0%", "10%", "50%"], "correct": "10%"},
        {"question": "Are electronic devices permitted to view your notes?", "options": ["Yes, if on airplane mode.", "No, strictly hard copy only."], "correct": "No, strictly hard copy only."},
        {"question": "Which of the following describes the grading scheme?", "options": ["Strictly 35% Final", "Best-of scheme automatically scales between 35% and 45% based on midterm performance"], "correct": "Best-of scheme automatically scales between 35% and 45% based on midterm performance"},
        {"question": "What subject line format should you use when emailing Prof. Neelin or the TAs?", "options": ["AOS 102", "AOS102", "Climate Class"], "correct": "AOS102"}
    ]
    render_quiz(q_data, 0)


# --- MODULE 1: CHAPTER 1 ---
elif current_idx == 1:
    st.title("📊 Chapter 1: Overview of Climate Variability")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Weather vs. Climate & Teleconnections</h3>
            <ul>
                <li><b>Weather vs. Climate:</b> Weather is an initial value problem—chaotic and highly sensitive to starting conditions. Climate is a boundary value problem based on statistics (averages over 30 years).</li>
                <li><b>Anomalies:</b> Calculated as the observed state minus the climatological baseline ($X_{anomaly} = X_{obs} - \overline{X}$).</li>
                <li><b>Anthropogenic vs. Natural:</b> Anthropogenic global warming is driven primarily by $CO_2$. Natural variability on interannual scales is dominated by ENSO (El Niño).</li>
                <li><b>Correlation Maps (PbSet 1A):</b> When mapping time series to precipitation, weather noise can randomly generate high correlation coefficients ($\pm0.3$). Without a physical climate model to verify mechanics, you could falsely identify 'teleconnections' out of pure statistical noise!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "How is a climate 'anomaly' defined mathematically?", "options": ["Observed value divided by average value", "Observed value minus the long-term climatological average", "The standard deviation of the weather"], "correct": "Observed value minus the long-term climatological average"},
        {"question": "According to PbSet 1A, what danger exists when calculating correlation maps on short observational time series?", "options": ["The math equations break down.", "Chaotic weather noise can create patches of high correlation (>0.3) completely by chance.", "Satellites cannot accurately read sea surface temperatures."], "correct": "Chaotic weather noise can create patches of high correlation (>0.3) completely by chance."},
        {"question": "El Niño is considered an example of:", "options": ["Anthropogenic climate change", "Natural internal climate variability", "Milankovitch orbital forcing"], "correct": "Natural internal climate variability"},
        {"question": "Which greenhouse gas is the primary driver of anthropogenic warming since the industrial revolution?", "options": ["Water Vapor", "Carbon Dioxide (CO2)", "Ozone"], "correct": "Carbon Dioxide (CO2)"},
        {"question": "Why can climate models predict 50 years into the future when weather forecasts fail after 2 weeks?", "options": ["Because climate models use quantum computing.", "Because weather models predict the exact chaotic state, whereas climate models predict the statistical boundary values resulting from energy balances.", "Because weather forecasts are intentionally downgraded."], "correct": "Because weather models predict the exact chaotic state, whereas climate models predict the statistical boundary values resulting from energy balances."}
    ]
    render_quiz(q_data, 1)


# --- MODULE 2: CHAPTER 2 ---
elif current_idx == 2:
    st.title("☀️ Chapter 2: Basics of Global Climate")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Carbon Reservoirs & Albedo Math</h3>
            <ul>
                <li><b>Carbon Pools:</b> Deep Ocean (85%), Fossil Fuels (8.9%), Land (5.1%), Atmosphere (~1.3%). Because the atmosphere holds so little active carbon, human fossil fuel emissions rapidly double its concentration, destabilizing the system.</li>
                <li><b>Albedo Calculation (PbSet 1B):</b> The global energy balance is $S_0 (1 - \\alpha) = \sigma T_e^4$.</li>
                <li>If we geoengineer the planet by paving California with highly reflective material ($\\alpha = 0.9$), we raise the global weighted average albedo.</li>
                <li><b>Result:</b> The Earth reflects more shortwave radiation back to space, absorbing less energy, resulting in a slightly lower calculated emission temperature ($T_e$).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "Why do anthropogenic carbon emissions drastically impact the atmosphere but not immediately alter the deep ocean's composition?", "options": ["The atmosphere contains only ~1.3% of active carbon, making its baseline highly sensitive to small numerical additions.", "The deep ocean refuses to absorb carbon dioxide."], "correct": "The atmosphere contains only ~1.3% of active carbon, making its baseline highly sensitive to small numerical additions."},
        {"question": "If you recalculate the global energy balance using a slightly higher global albedo (from PbSet 1B geoengineering), what happens?", "options": ["The calculated emission temperature decreases because the Earth absorbs less solar radiation.", "The emission temperature increases because albedo traps heat.", "Outgoing longwave radiation increases."], "correct": "The calculated emission temperature decreases because the Earth absorbs less solar radiation."},
        {"question": "Which of the following is NOT a primary component of the modeled physical climate system?", "options": ["Cryosphere", "Atmosphere", "The Solar Core", "Biosphere"], "correct": "The Solar Core"},
        {"question": "What is the primary driver of the deep ocean (thermohaline) circulation?", "options": ["Moon's gravitational pull", "Water density differences (temperature and salinity) and wind", "Geothermal vents"], "correct": "Water density differences (temperature and salinity) and wind"},
        {"question": "Which reservoir holds the vast majority (~85%) of active carbon in the climate system?", "options": ["The Atmosphere", "The Deep Ocean", "Land Surface / Soils"], "correct": "The Deep Ocean"}
    ]
    render_quiz(q_data, 2)


# --- MODULE 3: CHAPTER 3 ---
elif current_idx == 3:
    st.title("🌀 Chapter 3: Physical Processes")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Fluid Dynamics & Balances</h3>
            <ul>
                <li><b>Conservation Laws:</b> Climate models rely on the Conservation of Momentum (Newton's 2nd Law, $a = F/m$), Mass, Energy, and Moisture.</li>
                <li><b>Geostrophic Balance:</b> Away from the equator and surface friction, wind is controlled by an equilibrium between the <b>Pressure Gradient Force (PGF)</b> and the <b>Coriolis Force</b>.</li>
                <li>Because these forces pull in opposite directions, the resulting wind blows <b>parallel to isobars</b> (lines of constant pressure).</li>
                <li><b>Rossby Waves:</b> Planetary-scale waves that create complex flow patterns, enabling localized tropical heating (like El Niño) to cause long-distance teleconnections globally.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "Geostrophic balance describes an equilibrium between which two forces?", "options": ["Gravity and Friction", "Pressure Gradient Force and Coriolis Force", "Centrifugal Force and Albedo"], "correct": "Pressure Gradient Force and Coriolis Force"},
        {"question": "Because of Geostrophic Balance, how does wind flow in the upper atmosphere?", "options": ["Directly from High to Low pressure", "Parallel to the isobars", "Vertically upwards"], "correct": "Parallel to the isobars"},
        {"question": "What physical process allows a localized warming anomaly in the tropical Pacific to alter the storm tracks over North America?", "options": ["Rossby wave propagation", "Ocean thermohaline circulation", "Direct latent heat transfer"], "correct": "Rossby wave propagation"},
        {"question": "How does surface friction alter the geostrophic balance in the boundary layer?", "options": ["It increases wind speed", "It breaks the balance, causing wind to spiral slightly across isobars toward low pressure", "It completely cancels out the Coriolis force"], "correct": "It breaks the balance, causing wind to spiral slightly across isobars toward low pressure"},
        {"question": "Which foundational physics principle is the basis for the atmospheric conservation of momentum equations?", "options": ["Newton's Second Law (F=ma)", "The Ideal Gas Law", "Stefan-Boltzmann Law"], "correct": "Newton's Second Law (F=ma)"}
    ]
    render_quiz(q_data, 3)


# --- MODULE 4: CHAPTER 4 ---
elif current_idx == 4:
    st.title("🌊 Chapter 4: El Niño Prediction")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: ENSO & Probability Shifts</h3>
            <ul>
                <li><b>ENSO Mechanism:</b> Under normal conditions, trade winds pile warm water in the West Pacific. During El Niño, trade winds weaken, allowing the warm water pool to slosh eastward, flattening the thermocline and shutting down South American upwelling.</li>
                <li><b>Probability Shifts:</b> El Niño does not strictly <i>guarantee</i> rain in California. Chaos in the atmosphere (Initial Conditions) means every winter storm track is unique. </li>
                <li>Instead, El Niño shifts the <i>climatological probability distribution</i> to the right, making a wet winter far more likely, but not mathematically certain.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "During the mature warm phase of El Niño, what happens to the Pacific trade winds?", "options": ["They strengthen massively", "They weaken significantly, allowing warm water to shift eastward", "They blow continuously from South to North"], "correct": "They weaken significantly, allowing warm water to shift eastward"},
        {"question": "Why don't all ensemble climate model runs for the 1997 El Niño produce the exact same rainfall amounts for California?", "options": ["Because models don't conserve momentum.", "Because slightly different initial conditions lead to chaotic, divergent daily weather tracks, adding 'weather noise'.", "Because the ocean temperature changes daily."], "correct": "Because slightly different initial conditions lead to chaotic, divergent daily weather tracks, adding 'weather noise'."},
        {"question": "If an intense El Niño occurs, does it absolutely guarantee a catastrophic flooding winter in California?", "options": ["Yes, it completely dictates weather.", "No, it just shifts the probability distribution to make it more likely, but weather noise still exists."], "correct": "No, it just shifts the probability distribution to make it more likely, but weather noise still exists."},
        {"question": "What happens to the oceanic thermocline in the Eastern Pacific during El Niño?", "options": ["It deepens/flattens out, stopping cold water upwelling", "It rises to the surface, freezing the water", "It becomes highly saline"], "correct": "It deepens/flattens out, stopping cold water upwelling"},
        {"question": "What is the opposite, cold phase of ENSO called?", "options": ["The Annular Mode", "La Niña", "The Pacific Decadal Oscillation"], "correct": "La Niña"}
    ]
    render_quiz(q_data, 4)


# --- MODULE 5: CHAPTER 6 ---
elif current_idx == 5:
    st.title("☁️ Chapter 6: Greenhouse Effect & Feedbacks")
    st.caption("*(Covered prior to Ch. 5 based on Syllabus routing)*")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Radiative Forcing & Committed Warming</h3>
            <ul>
                <li><b>Radiative Forcing:</b> Energy imbalance at the top of the atmosphere. GHGs trap outgoing longwave infrared (IR) radiation.</li>
                <li><b>Energy Balance Model (PbSet 3A):</b> $C \\frac{\\partial \\Delta T_s}{\\partial t} + \\alpha \\Delta T_s = G + N$</li>
                <li><b>Thermal Lag:</b> Even if we freeze GHG concentrations today ($G$ is constant), $T_s$ continues to rise for decades because the massive heat capacity of the ocean ($C$) takes a long time to absorb the imbalance.</li>
                <li><b>Cloud Feedbacks:</b> 
                    <br>🔴 <i>High Clouds (Cirrus):</i> Transparent to solar, traps IR -> Net Warming.
                    <br>🔵 <i>Low Clouds (Stratus):</i> Highly reflective to solar, emits IR easily -> Net Cooling.
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "In the simple model equation, what physical variable explains why the Earth continues to warm for decades even after GHG emissions are frozen?", "options": ["The climate feedback parameter (alpha)", "The massive heat capacity of the upper and deep ocean (C)", "Weather noise (N)"], "correct": "The massive heat capacity of the upper and deep ocean (C)"},
        {"question": "What net radiative feedback is caused by an expansion of HIGH, thin cirrus clouds?", "options": ["A warming tendency (they let solar in but trap outgoing IR)", "A cooling tendency (they reflect solar radiation)"], "correct": "A warming tendency (they let solar in but trap outgoing IR)"},
        {"question": "What net radiative feedback is caused by LOW marine stratus clouds?", "options": ["Warming tendency", "Cooling tendency (they reflect incoming solar radiation and emit IR efficiently due to warm temperatures)"], "correct": "Cooling tendency (they reflect incoming solar radiation and emit IR efficiently due to warm temperatures)"},
        {"question": "Which of the following is a classic POSITIVE climate feedback loop?", "options": ["The water vapor feedback (warmer air holds more water vapor, which is a GHG)", "The lapse rate feedback in the tropics", "The low cloud feedback"], "correct": "The water vapor feedback (warmer air holds more water vapor, which is a GHG)"},
        {"question": "How does the ice-albedo feedback act as an amplifier?", "options": ["Warming melts ice, decreasing albedo, causing the earth to absorb more sunlight, leading to more warming.", "Warming creates more ice, increasing albedo, cooling the earth."], "correct": "Warming melts ice, decreasing albedo, causing the earth to absorb more sunlight, leading to more warming."}
    ]
    render_quiz(q_data, 5)


# --- MODULE 6: CHAPTER 5 ---
elif current_idx == 6:
    st.title("💻 Chapter 5: Climate Models")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: GCMs & Grid Computations</h3>
            <ul>
                <li><b>General Circulation Models (GCMs):</b> Divide the earth into 3D grid cells. Calculations occur at time steps (e.g., 15 mins).</li>
                <li><b>Computational Cost Math:</b> If you double the horizontal and vertical resolution ($2_x \\times 2_y \\times 2_z = 8$), you must also halve the integration time-step ($2_t$) to prevent computational instability. <b>$2^4 = 16$ times more expensive!</b></li>
                <li><b>Parameterization:</b> We cannot grid individual clouds. We use empirical approximations (parameterizations) to estimate sub-grid scale processes.</li>
                <li><b>CMIP Hatching (PbSet 3B):</b> When looking at ensemble model projections, a 'hatched' region means the projected climate change signal is smaller than 1 standard deviation of model noise/variability. It implies <i>low confidence</i> in the localized projection.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    q_data = [
        {"question": "If a modeling center doubles the resolution of their GCM in all 3 spatial dimensions, how much does the computational cost increase?", "options": ["By a factor of 8", "By a factor of 16 (because the time step must also be halved)", "By a factor of 2"], "correct": "By a factor of 16 (because the time step must also be halved)"},
        {"question": "Because individual cumulus clouds are smaller than a GCM grid box, how do models simulate their effects?", "options": ["They ignore them completely.", "They use parameterization (empirical approximations based on the grid box's average temperature/moisture).", "They run a separate quantum model."], "correct": "They use parameterization (empirical approximations based on the grid box's average temperature/moisture)."},
        {"question": "When analyzing a CMIP6 precipitation projection map, what does a 'hatched' region indicate?", "options": ["Absolute certainty of the outcome.", "The forced climate signal is smaller than the model spread/natural variability (low confidence).", "The models crashed in that region."], "correct": "The forced climate signal is smaller than the model spread/natural variability (low confidence)."},
        {"question": "What is 'climate drift' or 'spin-up' in a GCM?", "options": ["The time required for the model's oceans and atmosphere to reach a dynamically consistent equilibrium before the actual experiment begins.", "When the model physically drifts off the server."], "correct": "The time required for the model's oceans and atmosphere to reach a dynamically consistent equilibrium before the actual experiment begins."},
        {"question": "What does a single grid box in a GCM represent?", "options": ["A single, uniform averaged value for variables like temperature and wind velocity across that specific volume of space.", "Millions of individual data points for every tree and building inside it."], "correct": "A single, uniform averaged value for variables like temperature and wind velocity across that specific volume of space."}
    ]
    render_quiz(q_data, 6)


# --- MODULE 7: CHAPTER 7 ---
elif current_idx == 7:
    st.title("🔥 Chapter 7: Scenarios & Extremes")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Evapotranspiration, Ice Melt Math & Extremes</h3>
            <ul>
                <li><b>Extremes:</b> A modest shift in the mean temperature drastically increases the area under the tail of the bell curve. Heatwaves become exponentially more frequent.</li>
                <li><b>Soil Moisture (PET):</b> Even if summer precipitation remains normal, models project severe Northern Hemisphere soil moisture droughts. Why? Warming increases <b>Potential Evapotranspiration (PET)</b>, allowing the atmosphere to suck moisture out of the ground faster than rain replaces it.</li>
                <li><b>Ice Melt (PbSet 2 Calculation):</b> Melting ice into sea level rise uses the Latent Heat of Fusion ($L_f = 3.3 \\times 10^5$ J/kg). Energy absorbed by the ice goes entirely into phase-changing the mass, not raising its temperature.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Visual Interactive 
    st.subheader("🛠️ Shift in Extremes Simulator")
    shift = st.slider("Simulate Global Mean Warming Trend (Δ°C):", 0.0, 4.0, 1.5, 0.1)
    x = np.linspace(-6, 10, 1000)
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(x, stats.norm.pdf(x, 0, 1.5), label="Historical Baseline", color="#1E3A8A", linewidth=2)
    ax.plot(x, stats.norm.pdf(x, shift, 1.5), label=f"Warmed State (+{shift}°C)", color="#EF4444", linewidth=2)
    ax.axvline(x=2.5, color='#0F172A', linestyle='--', label="Severe Heatwave Cutoff")
    ax.fill_between(x, stats.norm.pdf(x, shift, 1.5), 0, where=(x > 2.5), color='#EF4444', alpha=0.3)
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    ax.legend(loc="upper left")
    st.pyplot(fig)

    q_data = [
        {"question": "Look at the simulator above. When the mean temperature distribution shifts to the right, what happens to the frequency of extreme heat events?", "options": ["It increases linearly.", "It increases disproportionately (non-linearly) because the area under the far tail of the curve expands massively.", "It remains exactly the same."], "correct": "It increases disproportionately (non-linearly) because the area under the far tail of the curve expands massively."},
        {"question": "According to CMIP projections, why will many regions suffer severe soil moisture depletion even if rainfall amounts do not decrease?", "options": ["Warming dramatically increases Potential Evapotranspiration (PET), causing the atmosphere to dry out the soil.", "The soil physically absorbs less water when hot."], "correct": "Warming dramatically increases Potential Evapotranspiration (PET), causing the atmosphere to dry out the soil."},
        {"question": "When calculating the rate of ice sheet melt to determine sea level rise (PbSet 2), what crucial thermodynamic constant is required?", "options": ["Latent Heat of Vaporization", "Latent Heat of Fusion (3.3 x 10^5 J/kg)", "The Ideal Gas Constant"], "correct": "Latent Heat of Fusion (3.3 x 10^5 J/kg)"},
        {"question": "What are 'negative emissions'?", "options": ["Emissions from electric vehicles.", "Actively removing CO2 from the atmosphere and storing it long-term (e.g., Direct Air Capture, restoring ecosystems).", "Lowering the speed limit."], "correct": "Actively removing CO2 from the atmosphere and storing it long-term (e.g., Direct Air Capture, restoring ecosystems)."},
        {"question": "Why does the Arctic warm significantly faster than the equator (Poleward Amplification)?", "options": ["Because the ice-albedo feedback accelerates localized warming as reflective ice turns into dark, heat-absorbing ocean water.", "Because the equator is cooling down."], "correct": "Because the ice-albedo feedback accelerates localized warming as reflective ice turns into dark, heat-absorbing ocean water."}
    ]
    render_quiz(q_data, 7)
