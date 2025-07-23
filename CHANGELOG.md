# 🧠 Resonant Fields Simulation – CHANGELOG.md

A chronological record of updates and enhancements made to the Resonant Fields Simulation models and system.

---

## 📦 Model V2 – Interactive Visualization & Animation
**Date:** 2025-07-23  
**Status:** Released

### ✨ Added
- Integrated `plotly.graph_objects` for 3D visualizations.
- New method: `visualize_step_interactive(step_index)`  
  → Displays a single simulation step as an interactive 3D scatter plot.
- New method: `animate_resonance_evolution()`  
  → Animates resonance dynamics over time in 3D with:
    - Play/Pause controls
    - Scrubbing slider for step navigation
    - State-based coloring and phase tooltip
- HTML export (`resonance_animation.html`) for offline interactive use.

### 🔁 Changed
- `run_simulation_3d()` now automatically calls the 3D animation after simulation ends.

---

## 🧱 Model V1 – Initial Implementation
**Date:** 2025-07-22 
**Status:** Baseline

### ✅ Implemented
- Core simulation logic:
    - `Chronon` as binary information carrier
    - `ResonanceNode` with state, phase, and information
    - `Hyperstructure3D` lattice with neighbor-based update rules
- Data logging of node state across timesteps.
- CSV export of full simulation history.

---