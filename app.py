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

# Custom CSS for modern styling, cards, and clean typography
st.markdown("""
<style>
    .reportview-container { background: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .lecture-card { background-color: #ffffff; padding: 25px; border-radius: 12px; border-left: 5px solid #1E3A8A; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .quiz-card { background-color: #F8FAFC; padding: 25px; border-radius: 12px; border: 1px solid #E2E8F0; margin-top: 20px; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h2 { color: #2563EB; }
    h3 { color: #0F172A; }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. Gamification State Engine
# ----------------------------------------------------
# List of modules in precise chronological syllabus order
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
    st.session_state.unlocked_idx = 0  # Starts at 0 (Welcome)
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}

# ----------------------------------------------------
# 3. Sidebar Navigation Control
# ----------------------------------------------------
st.sidebar.title("🌍 AOS102 Study Hub")
st.sidebar.markdown("### **Spring 2026 Final Review**")
st.sidebar.caption("Instructor: Prof. J. David Neelin")

# Master Admin Bypass for grading/testing purposes
god_mode = st.sidebar.toggle("🔓 Unlock All Chapters (Admin Mode)", value=False)

# Render navigation radio options with lock/unlock icons
display_modules = []
for i, mod in enumerate(MODULES):
    if god_mode or i <= st.session_state.unlocked_idx:
        display_modules.append(f"🟢 {mod}")
    else:
        display_modules.append(f"🔒 {mod}")

selected_display = st.sidebar.radio("Go to Module:", display_modules)
current_idx = display_modules.index(selected_display)

# Progress Bar
progress_percent = int((st.session_state.unlocked_idx / (len(MODULES)-1)) * 100)
st.sidebar.markdown("### **Your Course Progress**")
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
            <h3>📋 Course Administration & Safety Guardrails</h3>
            <p>Welcome to the custom learning environment built around Neelin's <i>Climate Change and Climate Modeling</i> textbook. Use this app to master the core quantitative principles of the physical climate system.</p>
            <ul>
                <li><b>TAs:</b> Zhiyuan (Jacob) Chen & Anqi Song</li>
                <li><b>Cheat Sheet Requirement:</b> Hard copies only! <b>At least 10% of each page MUST be in your own handwriting</b>, or you will face academic integrity penalties.</li>
                <li><b>Best-of Grading Engine:</b> Your course weight scales automatically! If you had a rough day on the midterm, your final weight automatically escalates to 45% while decreasing the midterm weight to 20% to optimize your final mark.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.info("💡 **Ready to begin?** Pass the quick diagnostic sanity check below to unlock Chapter 1!")
    
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Gatekeeper Check: Exam Rules</h3>', unsafe_allow_html=True)
    q1 = st.radio("Can you use a tablet or phone to view your cheat sheets during the final exam?", ["Yes, as long as it's in airplane mode.", "No, electronics are completely prohibited. Hard copy only."])
    
    if st.button("Submit Answers & Verify"):
        if q1 == "No, electronics are completely prohibited. Hard copy only.":
            st.success("🎯 Correct! Chapter 1 has been unlocked in the sidebar.")
            if st.session_state.unlocked_idx == 0:
                st.session_state.unlocked_idx = 1
                st.balloons()
        else:
            st.error("❌ Incorrect. Remember, no electronic devices of any kind are permitted.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 1: CHAPTER 1 ---
elif current_idx == 1:
    st.title("📊 Chapter 1: Overview of Climate Variability & Science")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Weather, Climate, and Anomalies</h3>
            <p><b>Weather</b> represents the instantaneous state of the atmosphere (e.g., standard chaotic hourly fluctuations), whereas <b>Climate</b> is defined by the statistical properties (averages, variances, probabilities) over a prolonged averaging window—typically 30 years.</p>
            <p>An <b>anomaly</b> is defined mathematically as the departure from the long-term climatology:</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.latex(r"X_{\text{anomaly}} = X_{\text{observed}} - \overline{X}_{\text{climatology}}")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h4>Anthropogenic Driving Forces vs. Natural Modes</h4>
            <ul>
                <li><b>Natural Internal Variability:</b> Phenomenon driven by inherent fluid dynamics and coupled system delays, primarily exemplified by the <b>El Niño Southern Oscillation (ENSO)</b> on interannual scales, and paleoclimate shifts over thousands of years.</li>
                <li><b>Anthropogenic Forcing:</b> Sustained linear modifications to the planetary energy balance via industrial emissions of trace greenhouse gases ($CO_2$, $CH_4$, nitrous oxides), shifting baseline state distributions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 1 Validation Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("If a severe winter storm causes record low temperatures on May 1st, 2026, this event is fundamentally classified as a change in:", ["Global Anthropogenic Climate Change", "Anomalous Short-term Weather Variability"])
    
    if st.button("Submit Module 1 Quiz"):
        if q == "Anomalous Short-term Weather Variability":
            st.success("🎯 Mastered! Chapter 2 is now unlocked.")
            if st.session_state.unlocked_idx == 1:
                st.session_state.unlocked_idx = 2
                st.balloons()
        else:
            st.error("❌ Think about the time scale! A single storm is a weather event, not a shifting 30-year climatological baseline.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 2: CHAPTER 2 ---
elif current_idx == 2:
    st.title("☀️ Chapter 2: Basics of Global Climate")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: System Interconnectivity & Geochemical Cycles</h3>
            <p>The global climate structure comprises six dynamic elements: the <b>Atmosphere</b>, the <b>Ocean</b>, the <b>Land Surface</b>, the <b>Cryosphere</b> (sea ice, ice shelves, snow layers), the <b>Biosphere</b>, and the deep <b>Lithosphere</b>.</p>
            <h3>🔄 The Global Carbon Budget Hierarchy</h3>
            <p>Understanding where carbon resides dictates how rapidly human emissions alter planetary systems:</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Metric Representation for Carbon Pools
    c1, c2, c3 = st.columns(3)
    c1.metric("Deep Ocean Reservoir", "~85% of Active Carbon", "Dominant Sink")
    c2.metric("Land Surface / Soils", "Significant Buffer", "Medium Dynamics")
    c3.metric("Atmospheric Reservoir", "~1.3% of Active Carbon", "Highly Vulnerable")
    
    st.markdown(
        """
        <div class="lecture-card">
            <p>Because the atmospheric storage pool is relatively small, human industrial output can quickly perturb its baseline concentration. 
            This sets up a <b>planetary energy imbalance</b> where incoming shortwave solar radiation ($S_0$) is uncompensated by outgoing longwave thermal emissions.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 2 Validation Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("Why does the addition of carbon dioxide cause such a rapid impact on atmospheric composition compared to the global system?", ["The atmospheric reservoir is small (~1.3%), making its relative sensitivity to perturbations extraordinarily high.", "The deep ocean completely isolates carbon and refuses to exchange it with other reservoirs."])
    
    if st.button("Submit Module 2 Quiz"):
        if q == "The atmospheric reservoir is small (~1.3%), making its relative sensitivity to perturbations extraordinarily high.":
            st.success("🎯 Correct! Chapter 3 is now unlocked.")
            if st.session_state.unlocked_idx == 2:
                st.session_state.unlocked_idx = 3
                st.balloons()
        else:
            st.error("❌ Incorrect. Review the small fractional share of atmospheric carbon storage!")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 3: CHAPTER 3 ---
elif current_idx == 3:
    st.title("🌀 Chapter 3: Physical Processes in the Climate System")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Dynamic Balances and Fluid Dynamics</h3>
            <p>Climate engines run entirely on fundamental conservation laws. Atmospheric and oceanic fluid circulation profiles are dictated by Newton's Second Law applied to continuous media:</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.latex(r"\mathbf{a} = \frac{\sum \mathbf{F}}{m}")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h4>The Primary Forces Driving Climate Motion:</h4>
            <ul>
                <li><b>Pressure Gradient Force (PGF):</b> Direct mechanical thrust moving air and fluid particles away from localized high pressure toward low pressure cells.</li>
                <li><b>Coriolis Force:</b> An apparent acceleration induced by the Earth's planetary rotation framework. It acts perpendicular to the velocity vector, deflecting moving parcels rightward in the Northern Hemisphere.</li>
                <li><b>Friction/Drag:</b> Turbulent dissipation occurring predominantly within the planetary boundary layers.</li>
            </ul>
            <h4>⚖️ Geostrophic Balance</h4>
            <p>Away from equatorial zones and boundary layer friction surfaces, a precise diagnostic equilibrium emerges where the <b>PGF balances the Coriolis Force</b> perfectly:</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.latex(r"f \cdot v = \frac{1}{\rho}\frac{\partial p}{\partial x}")
    st.markdown("This balance causes winds to blow **parallel to isobars** (lines of constant pressure) rather than directly crossing them from high to low pressure.")
    
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 3 Validation Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("Geostrophic balance describes an idealized physical state resulting from the equilibrium between which two forces?", ["Gravity and Surface Turbulent Friction", "Pressure Gradient Force and Coriolis Force"])
    
    if st.button("Submit Module 3 Quiz"):
        if q == "Pressure Gradient Force and Coriolis Force":
            st.success("🎯 Excellent physical intuition! Chapter 4 is now open.")
            if st.session_state.unlocked_idx == 3:
                st.session_state.unlocked_idx = 4
                st.balloons()
        else:
            st.error("❌ Retray! Look closely at the geostrophic balance equation terms.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 4: CHAPTER 4 ---
elif current_idx == 4:
    st.title("🌊 Chapter 4: El Niño and Year-to-Year Climate Prediction")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Ocean-Atmosphere Feedbacks and Probability Shifts</h3>
            <p>The <b>El Niño Southern Oscillation (ENSO)</b> represents the preeminent example of coupled macro-scale interannual natural variability. During its classical mature warm configuration, standard eastern Pacific upwelling pathways stall, and high sea surface temperature (SST) anomalies expand eastward.</p>
            <h4>🎰 The Concept of a Climatological Probability Shift</h4>
            <p>A common misconception is that El Niño acts as a deterministic switch for regional weather patterns. In reality, it acts to <i>bias the statistics</i> of the system. Chaotic internal atmospheric weather means that every individual El Niño winter has unique weather events, but the overall probability curve shifts significantly towards wetter conditions in regions like Southern California.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 4 Validation Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("If an intense El Niño phase materializes, does it absolutely guarantee a catastrophic flooding winter in California?", ["Yes, it completely dictates daily weather occurrences on a deterministic level.", "No, it shifts the probability distribution, making an unusually wet winter highly probable but not mathematically certain due to chaotic weather noise."])
    
    if st.button("Submit Module 4 Quiz"):
        if q == "No, it shifts the probability distribution, making an unusually wet winter highly probable but not mathematically certain due to chaotic weather noise.":
            st.success("🎯 Correct! Heading to Chapter 6 next (per Prof. Neelin's specific syllabus roadmap order).")
            if st.session_state.unlocked_idx == 4:
                st.session_state.unlocked_idx = 5
                st.balloons()
        else:
            st.error("❌ Think about the distinction between weather noise and climate probabilities!")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 5: CHAPTER 6 ---
elif current_idx == 5:
    st.title("☁️ Chapter 6: The Greenhouse Effect and Climate Feedbacks")
    st.caption("⚠️ Chronological Syllabus Track: Covered prior to Chapter 5 to establish radiative fundamentals.")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Radiative Forcing Profiles and Cloud Feedbacks</h3>
            <p><b>Radiative Forcing</b> is defined as the net thermal energy imbalance engineered at the top boundary of the troposphere due to greenhouse gas perturbations. Outgoing longwave radiation is effectively trapped by trace gas absorption lines, reducing structural planetary heat escape.</p>
            <h3>⛅ The Complex Mechanics of Cloud Feedbacks</h3>
            <p>Clouds exert a dual control on the planetary radiation budget, depending entirely on altitude and optical depth:</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("🟥 **High-Level Clouds (Cirrus)**")
        st.markdown(
            "Optically thin to incoming shortwave solar rays, but highly effective at absorbing upward-directed terrestrial longwave infrared radiation. Because they are high and cold, they radiate very little energy back out to space, yielding a net **warming tendency**."
        )
    with col2:
        st.info("🟦 **Low-Level Clouds (Marine Stratus)**")
        st.markdown(
            "Optically thick with highly reflective albedo profiles. They reflect incoming solar rays back to space, and because they are low and warm, they emit infrared radiation efficiently. This yields a dominant net **cooling tendency**."
        )
        
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 6 Validation Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("An expansion of high-altitude thin cirrus clouds would initiate what net radiative feedback pattern?", ["A cooling trend due to the reflection of incoming solar radiation.", "A warming trend because they trap outgoing terrestrial longwave infrared radiation while remaining transparent to solar rays."])
    
    if st.button("Submit Module 6 Quiz"):
        if q == "A warming trend because they trap outgoing terrestrial longwave infrared radiation while remaining transparent to solar rays.":
            st.success("🎯 Spot on! Let's explore the structural grids of Chapter 5.")
            if st.session_state.unlocked_idx == 5:
                st.session_state.unlocked_idx = 6
                st.balloons()
        else:
            st.error("❌ Double-check cloud height dynamics! High clouds trap infrared effectively.")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 6: CHAPTER 5 ---
elif current_idx == 6:
    st.title("💻 Chapter 5: Constructing a Climate Model")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: General Circulation Model (GCM) Discretization</h3>
            <p>To evaluate continuous partial differential equations numerically, General Circulation Models discretize the planet into distinct 3D <b>grid cells</b>. Each individual block represents a single, uniform value for variables like temperature ($T$), moisture ($q$), and wind velocity vectors ($u, v, w$).</p>
            <h3>🧮 Exponential Cost Scaling Laws</h3>
            <p>When increasing a model's grid resolution, the computational demands scale non-linearly due to stability conditions (such as the Courant-Friedrichs-Lewy criterion). If you cut the horizontal grid spatial resolution in half, you must also halve the integration time-step ($ \Delta t $) to prevent computational instability.</p>
            <p><b>The Scaling Penalty:</b> Doubling spatial accuracy means:</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.latex(r"\text{Cost Factor} = 2_x \times 2_y \times 2_z \times 2_t = 2^4 = 16")
    st.markdown("A seemingly simple twofold enhancement in grid spacing escalates processing overhead **by a factor of 16**.")
    
    # Quiz Block
    st.markdown('<div class="quiz-card"><h3>🧠 Chapter 5 Validation Quiz</h3>', unsafe_allow_html=True)
    q = st.radio("If an atmospheric researcher upgrades a GCM grid mesh resolution by a factor of 3 along all dimensions (including the required adjustment to time-steps), how much greater will the computational workload be?", ["It will increase by a factor of 9.", "It will increase by a factor of 81 (3 to the power of 4).", "It will scale linearly by a factor of 3."])
    
    if st.button("Submit Module 5 Quiz"):
        if q == "It will increase by a factor of 81 (3 to the power of 4).":
            st.success("🎯 Mathematical genius! You've unlocked the final module.")
            if st.session_state.unlocked_idx == 6:
                st.session_state.unlocked_idx = 7
                st.balloons()
        else:
            st.error("❌ Remember the 4D scaling principle: $3 \times 3 \times 3 \times 3 = 3^4$. Try again!")
    st.markdown('</div>', unsafe_allow_html=True)


# --- MODULE 7: CHAPTER 7 ---
elif current_idx == 7:
    st.title("🔥 Chapter 7: Climate Model Scenarios and Extremes")
    
    st.markdown(
        """
        <div class="lecture-card">
            <h3>📖 Deep-Dive: Time-Dependent Scenarios and Statistical Shifts</h3>
            <p>Projections use standardized emission trajectories (such as SSP or RCP paths) to evaluate how the earth system reacts under different forcing conditions. These model simulations reveal uneven warming patterns across the globe, with the most severe changes occurring over polar regions due to ice-albedo feedbacks, particularly during the late summer and early autumn windows.</p>
            <h3>📈 Statistical Distribution of Weather Extremes</h3>
            <p>A modest modification in the mean value of a climate distribution induces an asymmetric, non-linear explosion in the occurrence frequency of extreme anomalies. This dynamic is illustrated using the interactive simulator below.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Interactive distribution simulator
    st.subheader("🛠️ Distribution Shift Simulator")
    shift = st.slider("Simulate Global Mean Warming Trend (Δ°C):", 0.0, 4.0, 1.5, 0.1)
    
    x = np.linspace(-6, 10, 1000)
    y_base = stats.norm.pdf(x, 0, 1.5)
    y_shifted = stats.norm.pdf(x, shift, 1.5)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y_base, label="Historical Baseline Climate", color="#1E3A8A", linewidth=2)
    ax.plot(x, y_shifted, label=f"Warmed Future State (+{shift}°C)", color="#EF4444", linewidth=2)
    
    # Establish a theoretical severe threshold line
    threshold = 2.5
    ax.axvline(x=threshold, color='#0F172A', linestyle='--', alpha=0.7, label="Severe Heatwave Cutoff")
    ax.fill_between(x, y_shifted, 0, where=(x > threshold), color='#EF4444', alpha=0.25)
    
    ax.set_ylabel("Probability Density")
    ax.set_xlabel("Temperature Deviation From Baseline")
    ax.set_title("How Shifting Mean Climates Create Disproportionate Extreme Anomalies")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.15)
    st.pyplot(fig)
    
    st.caption("📝 Notice that the area under the red curve past the dashed threshold increases dramatically with even a modest shift in the mean. This is why heatwaves and heavy precipitation events become far more frequent under global warming.")

    # Final Exam Review Quiz
    st.markdown('<div class="quiz-card"><h3>🎓 Final Review Master Challenge</h3>', unsafe_allow_html=True)
    q = st.radio("When the mean of a temperature distribution moves rightward while holding variance constant, what happens to the frequency of extreme heat events?", ["The probability of extreme events scales linearly with the mean shift.", "The probability of extreme events increases non-linearly, disproportionately expanding the area past the historical threshold."])
    
    if st.button("Submit Final Master Review Quiz"):
        if q == "The probability of extreme events increases non-linearly, disproportionately expanding the area past the historical threshold.":
            st.success("🎉 Comprehensive Course Mastery Achieved! You are officially prepared for the AOS102 Final Exam!")
            st.snow()
        else:
            st.error("❌ Take another look at the shaded region under the curve in the simulator. It expands far more quickly than the mean shift itself.")
    st.markdown('</div>', unsafe_allow_html=True)
