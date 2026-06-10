import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set up the page configuration
st.set_page_config(page_title="AOS102 Final Review Dashboard", layout="wide")

# Sidebar for Navigation
st.sidebar.title("AOS102 Study Modules")
module = st.sidebar.radio(
    "Select a Topic to Review:",
    (
        "Home / Exam Rules",
        "1. Probability & El Niño",
        "2. Constructing a Climate Model",
        "3. Radiative Forcing & Feedbacks",
        "4. Scenarios & Emissions",
        "5. Spatial Patterns & Extremes",
        "6. Sea Level Rise & Mitigation"
    )
)

if module == "Home / Exam Rules":
    st.title("AOS102: Climate Change & Climate Modeling")
    st.subheader("Post-midterm-ish Review Dashboard")
    st.markdown("Welcome to your study dashboard! This covers concepts heavily weighted towards the second half of the class[cite: 644].")
    
    st.info("📸 **Photo Recommendation**: Add the title slide image (Page 1) here to make the dashboard look like your lecture deck.")

    st.warning("""
    **🚨 Final Exam Rules Reminder:**
    * **Aids permitted:** Two 8.5"x11" sheets of paper, double-sided (4 pages total)[cite: 647].
    * Must have your name on each side and be handed in with the exam[cite: 647].
    * Notes can include figures and clips, but must be organized individually[cite: 648].
    * **At least 10% of each page MUST be in your handwriting**[cite: 649].
    * Hard copy only (no electronics!)[cite: 650].
    """)

elif module == "1. Probability & El Niño":
    st.title("Probability Distributions & Precipitation")
    
    st.markdown("""
    ### El Niño's Effect on Precipitation (e.g., California)
    Climate models run multiple times with different initial conditions show that different weather and storms happen each year, even during the exact same El Niño event[cite: 671, 673].
    
    * **The Shift:** The probability of a rainy winter is enhanced during El Niño, but it is far from certain[cite: 655].
    * **Example (Figure 4.22):** You might find a precipitation value that only **33%** (1/3) of all normal winters exceed. During El Niño winters, **50%** of winters might exceed that exact same value[cite: 660, 661, 662].
    * Stronger El Niños enhance the probability of a rainier-than-average winter substantially more[cite: 676].
    """)
    
    st.info("📸 **Photo Recommendation**: Insert the Northern/Southern California precipitation probability distribution graphs (Slides 3-4) showing the La Niña/Neutral/El Niño curves.")

elif module == "2. Constructing a Climate Model":
    st.title("Constructing a Climate Model")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### GCM Grid and Resolution
        * **Grid Cells:** For each grid cell, there is a single value for variables like temperature, velocity, etc.[cite: 712]. The vertical coordinate follows the topography[cite: 712].
        * **Time Steps:** Budgets calculate changes for the next time step (e.g., 15 minutes)[cite: 715].
        """)
        st.info("📸 **Photo Recommendation**: Insert Figure 5.1 (3D typical atmospheric GCM grid).")
        
    with col2:
        st.markdown("""
        ### Computational Cost of High Resolution
        * If you halve the horizontal grid size, you also have to halve the time step[cite: 733].
        * **The Math:** Doubling resolution in x, y, and z means $2 \\times 2 \\times 2 \\times$ (number of grid cells), plus $2 \\times$ the time steps. **The cost increases by a factor of $2^4 = 16$**[cite: 734, 735].
        * Running a low-resolution model for 40 years can cost the same computationally as running a high-resolution model for 1 week[cite: 740, 741].
        """)

elif module == "3. Radiative Forcing & Feedbacks":
    st.title("Radiative Forcing & The Water Vapor Feedback")
    
    st.markdown("""
    ### Radiative Forcing Imbalance
    Radiative forcing is the top-of-atmosphere initial imbalance in the energy budget[cite: 449].
    * **Aerosols:** Anthropogenic aerosols reflect sunlight[cite: 450].
    * **Greenhouse Gases (GHG):** GHGs trap infrared (IR) radiation[cite: 450]. 
    * **Equilibrium:** To reach equilibrium with higher GHGs, the temperature increases until the top of the atmosphere IR again balances net solar radiation. Ocean heat capacity slows this process down[cite: 450, 451].
    
    ### The Water Vapor Feedback
    * Increased water vapor is critical for precipitation changes[cite: 453, 463].
    * For typical lower troposphere temperatures, **water vapor increases about 7% per °K** (if Relative Humidity remains constant)[cite: 454, 464].
    """)

elif module == "4. Scenarios & Emissions":
    st.title("Emissions Scenarios (RCPs)")
    
    st.markdown("Representative Concentration Pathways (RCPs) are named based on their radiative forcing in the year 2100[cite: 470, 478].")
    
    st.table({
        "Scenario": ["RCP 8.5", "RCP 6.0", "RCP 4.5", "RCP 3-PD (2.6)"],
        "Radiative Forcing (2100)": ["8.5 W/m²", "6.0 W/m²", "4.5 W/m²", "Peak of 3.0 W/m² then declines"],
        "CO2 eq (ppm)": ["1370 ppm", "850 ppm", "650 ppm", "Peaks at 490 ppm then declines"],
        "Notes": ["Highest emissions [cite: 470, 478]", "Stabilizes after 2100 [cite: 471, 479]", "Stabilizes after 2100 [cite: 472, 480]", "Requires net negative emissions [cite: 481]"]
    })
    
    st.markdown("""
    **Transient vs. Equilibrium:**
    Even if greenhouse gas emissions are suddenly stopped at a specific time, the temperature was less than equilibrium due to lag, so it **continues to rise for several decades**[cite: 464].
    """)

elif module == "5. Spatial Patterns & Extremes":
    st.title("Spatial Patterns of Warming & Extreme Events")
    
    st.markdown("""
    ### Key Spatial Patterns
    * **Poleward Amplification:** A robust feature where the poles warm faster, influenced by the snow/ice feedback and lapse rate differences[cite: 499, 500, 515, 516].
    * **Continents vs. Oceans:** Continents generally warm before the oceans[cite: 503, 519].
    * **Precipitation:** Global average precipitation increases (~1.5-3% per °C). High latitudes and tropical areas get more rain, but subtropical dry areas decrease[cite: 524, 525]. This is the **"Rich-Get-Richer"** effect: more moisture leads to increased transport to current convergence regions[cite: 484].
    """)
    
    st.divider()
    
    st.markdown("### How a Shift in Mean Temperature Affects Extremes [cite: 540]")
    st.markdown("If the standard deviation remains similar but the mean temperature rises, events considered 'extreme' heat waves today will occur much more frequently[cite: 540].")
    
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
    
    st.caption("As the distribution slides right, the area under the curve past the old threshold grows drastically[cite: 540, 542].")

elif module == "6. Sea Level Rise & Mitigation":
    st.title("Sea Level Rise & Mitigation")
    
    st.markdown("""
    ### Sea Level Rise Sources
    * **Thermosteric (Thermal Expansion):** Ocean heat storage slows down surface warming but expands the water, raising sea levels (~0.8 mm/yr above 700m depth)[cite: 586, 596, 600].
    * **Land Ice Melt:** Major loss mechanism from energy balance changes (~1-2 mm/yr)[cite: 585, 601].
    * **Ongoing Rise:** Sea level rise continues even after CO2 concentrations are brought to a constant level due to the deep ocean's immense thermal inertia[cite: 601, 613].
    """)
    st.info("📸 **Photo Recommendation**: Insert the Global Mean Sea Level (GMSL) vs SSP Scenarios line chart here.")

    st.markdown("""
    ### Mitigation and Emissions
    * **Constant emissions** yields an ongoing increase in concentration[cite: 616, 631]. 
    * To stabilize CO2, emissions must be brought down dramatically[cite: 616]. 
    * If emissions drop too slowly, we overshoot stabilization targets, which means **negative emissions** (actively removing CO2) will be required[cite: 617].
    * **California Example:** Meeting the 80% reduction by 2050 requires 3 major energy system transformations (efficiency, decarbonized electricity, electrification of direct fuel uses)[cite: 632].
    """)
