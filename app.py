import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set up the page configuration
st.set_page_config(page_title="AOS102 Ultimate Final Review", layout="wide")

# Sidebar for Navigation
st.sidebar.title("AOS102 Study Modules")
module = st.sidebar.radio(
    "Select a Chapter to Review:",
    (
        "Exam Rules & Intro",
        "Ch 1: Climate vs. Weather",
        "Ch 2: The Climate System",
        "Ch 3: Physical Processes",
        "Ch 4: El Niño & Variability",
        "Ch 5: Climate Models",
        "Ch 6: Forcing & Feedbacks",
        "Ch 7: Scenarios & Extremes"
    )
)

if module == "Exam Rules & Intro":
    st.title("AOS102: Climate Change & Climate Modeling")
    st.subheader("Ultimate Final Review Dashboard")
    st.markdown("Welcome to your study dashboard! This covers concepts heavily weighted towards the second half of the class, while integrating foundational concepts from Chapters 1-4.")
    
    st.warning("""
    **🚨 Midterm / Final Exam Rules Reminder:**
    * **Aids permitted:** Two 8.5"x11" sheets of paper, double-sided (4 pages total)[cite: 4585].
    * Must have your name on each side and be handed in with the exam.
    * Notes can include figures and clips, but must be organized individually[cite: 4455].
    * **At least 10% of each page MUST be in your handwriting**[cite: 4456].
    * Hard copy only (no electronics!).
    """)

elif module == "Ch 1: Climate vs. Weather":
    st.title("Chapter 1: Climate vs. Weather")
    
    st.markdown("""
    ### Definitions
    * **Climate vs. Weather:** Climate quantities are defined by averages or other statistics over the weather for a sufficiently long interval[cite: 4457]. 
    * We look at anomalies (departures from the long-term climatology) to understand variations.
    * **Example:** Creating a histogram of November-April precipitation over many years to obtain climatological probabilities[cite: 4458].
    
    ### Natural vs. Anthropogenic
    * **Natural Variability:** El Niño is a leading example of natural climate variation on interannual timescales[cite: 3].
    * **Anthropogenic:** Trace gases and human emissions (specifically $CO_2$) drive the rapid warming observed since the industrial revolution[cite: 4].
    """)
    st.info("📸 **Photo Recommendation**: Insert the Chapter 1 Title Slide or a precipitation histogram here to visualize climatological averages.")

elif module == "Ch 2: The Climate System":
    st.title("Chapter 2: Basics of Global Climate")
    
    st.markdown("""
    ### Components of the Climate System
    To model climate, we must consider the interacting components:
    * **Atmosphere**
    * **Ocean**
    * **Land Surface**
    * **Cryosphere:** Land ice (ice shelves, glaciers), snow, and sea ice[cite: 451].
    * **Biosphere**
    * **Lithosphere:** Solid earth[cite: 451].
    * **Biogeochemistry:** The chemical composition and biological chemistry of the climate system[cite: 451].
    
    ### Carbon Reservoirs
    * The **deep ocean** holds the vast majority of carbon (~85%).
    * Fossil fuel reserves and land hold significant amounts.
    * The **atmosphere** is a comparatively small carbon reservoir (~1.3%), meaning that human emissions create a massive impact on atmospheric concentrations relatively quickly.
    """)

elif module == "Ch 3: Physical Processes":
    st.title("Chapter 3: Physical Processes")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Conservation of Momentum
        Climate models rely on fundamental physics, notably Newton's Second Law ($F = ma$ or $a = F/m$) applied to fluids[cite: 937]. 
        * Acceleration ($a$) is the rate of change of velocity.
        * **Forces in the Atmosphere/Ocean:** The forces driving this include the Coriolis force, Pressure Gradient Force (PGF), gravity, and friction/drag[cite: 938].
        """)
        
    with col2:
        st.markdown("""
        ### Geostrophic Balance
        * Wind doesn't blow directly from high to low pressure. 
        * **Geostrophic Balance** is an approximate balance between the **Coriolis force** and the **pressure gradient force** (PGF)[cite: 932]. 
        * This balance dictates wind and current motions in many applications, keeping winds blowing *along* isobars rather than across them.
        """)
        
    st.info("📸 **Photo Recommendation**: Insert Figure 3.4 showing Geostrophic Balance (arrows balancing PGF and Coriolis).")

elif module == "Ch 4: El Niño & Variability":
    st.title("Chapter 4: El Niño & Year-to-Year Prediction")
    
    st.markdown("""
    ### El Niño Southern Oscillation (ENSO)
    ENSO is the primary driver of natural interannual climate variability.
    * During the fully developed warm phase (like December 1997), massive anomalies in Sea Surface Temperatures (SST) alter global weather[cite: 1442].
    
    ### The Shift in Precipitation Probabilities
    Climate models run multiple times with different initial conditions show that different storms happen each year, even during the exact same El Niño event.
    * **The Shift:** The probability of a rainy winter is enhanced during El Niño, but it is far from certain.
    * Stronger El Niños enhance the probability of a rainier-than-average winter substantially more.
    """)
    
    st.info("📸 **Photo Recommendation**: Insert the California precipitation probability distribution graphs from the slides showing the La Niña/Neutral/El Niño shifted curves.")

elif module == "Ch 5: Climate Models":
    st.title("Chapter 5: Constructing a Climate Model")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### GCM Grid and Resolution
        * **Grid Cells:** For each grid cell, there is a single value for variables like temperature, velocity, etc.[cite: 2105]. 
        * The vertical coordinate follows the topography of the earth[cite: 2105].
        * **Fluxes:** Transports of mass, energy, and moisture are calculated into and out of each grid cell[cite: 2105].
        * **Time Steps:** Budgets calculate changes for the next time step (e.g., every 15 minutes)[cite: 2105].
        """)
        st.info("📸 **Photo Recommendation**: Insert Figure 5.1 (3D typical atmospheric GCM grid).")
        
    with col2:
        st.markdown("""
        ### Computational Cost of High Resolution
        * If you halve the horizontal grid size, you also have to halve the time step.
        * **The Math:** Doubling resolution in x, y, and z means $2 \\times 2 \\times 2 \\times$ (number of grid cells), plus $2 \\times$ the time steps. **The cost increases by a factor of $2^4 = 16$**.
        """)

elif module == "Ch 6: Forcing & Feedbacks":
    st.title("Chapter 6: Forcing & Feedbacks")
    
    st.markdown("""
    ### Cloud Feedbacks
    Clouds play a complex dual role in the earth's energy budget:
    * **High Clouds (Cirrus):** Cause a net **warming tendency**. They let solar radiation through but absorb outgoing infrared (IR) radiation from the earth[cite: 2379].
    * **Low Clouds (Marine Stratus):** Cause a net **cooling tendency**. They act as a thick shield, creating increased reflection of incoming solar radiation[cite: 2379].
    
    ### The Water Vapor Feedback
    * Increased water vapor is critical for precipitation changes.
    * For typical lower troposphere temperatures, water vapor increases about 7% per °K (if Relative Humidity remains constant).
    """)
    st.info("📸 **Photo Recommendation**: Insert the cloud feedback visual showing the arrows for High Cloud (warming) vs Low Cloud (cooling).")

elif module == "Ch 7: Scenarios & Extremes":
    st.title("Chapter 7: Scenarios & Extremes")
    
    st.markdown("""
    ### Time-Dependent Warming Scenarios
    Climate model predictions respond to forcings (like GHGs) continuously applied according to specific emissions pathways[cite: 2911]. 
    * These responses map out drastically different spatial patterns depending on if we hit peak forcing soon or continue unabated[cite: 2911].
    * Changes represent significant spatial impacts on sea ice fraction, leading to drastic melt projections (e.g., in the September-November timeframe over the Arctic)[cite: 3932].
    """)
    
    st.divider()
    
    st.markdown("### How a Shift in Mean Temperature Affects Extremes")
    st.markdown("If the standard deviation remains similar but the mean temperature rises, events considered 'extreme' heat waves today will occur much more frequently.")
    
    # Interactive visual for extreme events shifting
    st.subheader("Interactive: Shift the Mean Temperature")
    shift = st.slider("Increase Mean Temperature", 0.0, 4.0, 0.0, 0.5)
    
    x = np.linspace(-5, 10, 1000)
    y_base = stats.norm.pdf(x, 0, 1.5)
    y_shifted = stats.norm.pdf(x, shift, 1.5)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y_base, label="Historical Climate", color="blue")
    ax.plot(x, y_shifted, label=f"Warmed Climate (+{shift}°)", color="red")
    ax.axvline(x=2.5, color='black', linestyle='--', label="Historical 'Extreme' Threshold")
    ax.fill_between(x, y_shifted, 0, where=(x > 2.5), color='red', alpha=0.3)
    ax.set_title("Shift in Probability Distribution")
    ax.legend()
    st.pyplot(fig)
    
    st.caption("As the distribution slides right, the area under the curve past the old threshold grows drastically. This concept applies to heatwaves and extreme precipitation events!")
