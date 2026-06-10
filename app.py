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
        "Ch 5: Climate Models",
        "Ch 6: The Greenhouse Effect",
        "Ch 7: Scenarios & Extremes"
    )
)

if module == "Exam Rules & Intro":
    st.title("AOS102: Climate Change & Climate Modeling")
    st.subheader("Ultimate Final Review Dashboard")
    st.markdown("Welcome to your study dashboard! This app covers key, high-level final exam concepts.")
    
    st.warning("""
    **🚨 Final Exam Rules Reminder:**
    * **Aids permitted:** Two 8.5"x11" sheets of paper, double-sided (4 pages total).
    * Must have your name on each side and be handed in with the exam.
    * Notes can include figures and clips, but must be organized individually.
    * **At least 10% of each page MUST be in your handwriting**.
    * Hard copy only (no electronics!).
    """)

elif module == "Ch 5: Climate Models":
    st.title("Chapter 5: Constructing a Climate Model")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### GCM Grid and Time Steps
        * **Grid Cells:** For each grid cell, there is a single value for variables like temperature and velocity. 
        * The vertical coordinate follows the topography of the earth.
        * **Fluxes:** Transports of mass, energy, and moisture are calculated into and out of each grid cell.
        * **Time Steps:** Budgets calculate changes for the next time step, such as every 15 minutes.
        """)
        st.info("📸 **Photo Recommendation**: Insert Figure 5.1 (3D typical atmospheric GCM grid).")
        
    with col2:
        st.markdown("""
        ### Computational Cost & Resolution
        * If you halve the horizontal grid size, you also have to halve the time step. Why? The time step must be small enough so that wind/waves don't cross more than one grid box per step, or the model becomes unstable.
        * **The Math:** Doubling resolution in x, y, and z means $2 \\times 2 \\times 2 \\times$ (number of grid cells). Because you also must double the time steps, **the cost increases by a factor of $2^4 = 16$**.
        * It can cost the same computationally to run a low-resolution model for 40 years as it does to run a high-resolution model for 1 week.
        """)

elif module == "Ch 6: The Greenhouse Effect":
    st.title("Chapter 6: Forcing & Feedbacks")
    
    st.markdown("""
    ### Radiative Forcing
    Radiative forcing is the energy imbalance at the top of the atmosphere due to anthropogenic and other changes.
    * Outgoing longwave radiation is trapped by greenhouse gases, resulting in an imbalance where less energy escapes than arrives.
    
    ### Cloud Feedbacks
    Clouds play a complex dual role in the earth's energy budget:
    * **High Clouds (Cirrus):** Cause a net **warming tendency**. They let solar radiation through but absorb outgoing infrared (IR) radiation, emitting it from a higher, colder level.
    * **Low Clouds (Marine Stratus):** Cause a net **cooling tendency**. They create increased reflection of incoming solar radiation, and their IR emission is similar to the surface since they are warm at low levels.
    """)
    st.info("📸 **Photo Recommendation**: Insert the cloud feedback visual from Ch 6 showing the arrows for High Cloud vs Low Cloud.")

elif module == "Ch 7: Scenarios & Extremes":
    st.title("Chapter 7: Scenarios & Extremes")
    
    st.markdown("""
    ### Sea Ice Projections
    * Model simulations (like those from CMIP5) project distinct decreases in Northern Hemisphere sea ice extent based on different forcing scenarios (e.g., RCP2.6, RCP4.5, RCP6.0, RCP8.5). 
    * The most severe ice loss anomalies occur in late summer/early fall (September-November timeframe).
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
    
    st.caption("As the distribution slides right, the area under the curve past the old threshold grows drastically. This mathematical concept applies to heatwaves and extreme precipitation events.")
