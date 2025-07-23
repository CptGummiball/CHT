
# 🌀 Chrono-Resonant Hyperstructure Simulation

This repository provides a Python-based simulation of a speculative physical model called the **Chrono-Resonant Hyperstructure Theory (CHT)**. The theory treats the universe as an informational, resonating field where time, space, energy, and consciousness emerge from discrete temporal units (*Chronons*) interacting via resonant hyperstructures.

## 📚 Theory Summary

In contrast to traditional physics models:

- **Time** is quantized into indivisible units called **Chronons**.
- **Space** is an emergent interference pattern from Chronon interactions.
- **Energy** is modeled as informational wavefronts.
- **Gravity** arises from distortions in a higher-dimensional **Hyperstructure Field**.
- **Consciousness** is a locally stabilized resonance.

This simulation treats the universe as a 3D toroidal grid of resonating nodes ("Resonanzknoten"), each driven by discrete time packets and updated via neighbor-based interactions modulated by global *meta-time drift*.

## 🚀 Features
- 🔁 **3D Simulation** of a resonant field lattice over time (V1/V2)
- ⏱️ Configurable simulation duration and grid size (V1/V2)
- 📊 **Logging and CSV export** of all node states at each timestep (V1/V2)
- 🌐 Toroidal topology (wrap-around edges in all 3 dimensions) (V1/V2)
- 🧠 Encoded Chronon-based information dynamics (V1/V2)
- **interactive 3D visualization of resonant fields** (V2 only)

## ✅ Difference between V1 and V2
| Feature                            | Model V1 | Model V2 |
| ---------------------------------- | -------- | -------- |
| Static CSV export                  | ✅        | ✅        |
| Interactive 3D visualization       | ❌        | ✅        |
| Animated time evolution            | ❌        | ✅        |
| HTML export of visualization       | ❌        | ✅        |
| Slider to scrub steps in animation | ❌        | ✅        |
| Plotly integration                 | ❌        | ✅        |


## 🧪 Example Output
Exported `.csv` structure:
```csv
time_step,x,y,z,state,phase,information,meta_zeit
0,0,0,0,-0.29995,5.3166,-1,0.05
0,0,0,1,0.37543,4.4522,-1,0.05
...
````
## 🛠️ Requirements

- Python 3.8+
- numpy
- pandas
- plotly (for V2)

Install dependencies:

V1/V2:
```bash
pip install numpy pandas
````
V2:
```bash
pip install plotly
````
## ▶️ Usage
Run the simulation via terminal:
```bash
python chrono_hyperstructure.py
````

You will be prompted to input:

- Simulation duration (in seconds)
- Grid size (e.g. 20 for a 20x20x20 lattice)

After execution, a hyperstruktur_log.csv file will be generated in the working directory.

## 📁 Output
- `hyperstruktur_log.csv`: Contains the full time-series log of the system's state across all nodes and timesteps.

## 🧠 Future Ideas
- Fourier and entropy analysis of emergent patterns
- Cognitive input modulation experiments
- GPU-accelerated large-lattice simulation

## 🙋 About
This project is a speculative, metaphysical exploration of physics and complexity theory. It is not intended to replace existing models but to creatively inspire new ways of thinking about the structure of the universe.

## License

[MIT](LICENSE)
