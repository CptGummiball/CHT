import numpy as np
import pandas as pd
import plotly.graph_objects as go
import os


# === Chronon: Carrier of an elementary information unit ===
class Chronon:
    def __init__(self):
        self.information = np.random.choice([-1, 1])  # binary


# === Resonance node: lattice point in the hyperstructure ===
class ResonanceNode:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.state = np.random.uniform(-1.0, 1.0)
        self.information = Chronon().information
        self.phase = np.random.uniform(0, 2 * np.pi)

    def update(self, neighbors, meta_time):
        avg_neighbor = np.mean([n.state for n in neighbors])
        resonance_drift = np.sin(self.phase + meta_time)
        info_modulation = self.information * 0.1
        self.state += 0.05 * (avg_neighbor - self.state) + info_modulation + 0.02 * resonance_drift
        self.phase += 0.1 * meta_time
        self.state = np.clip(self.state, -1.5, 1.5)


# === Hyperstructure: the 3D resonance lattice ===
class Hyperstructure3D:
    def __init__(self, size):
        self.size = size
        self.grid = [[[ResonanceNode(x, y, z) for z in range(size)] for y in range(size)] for x in range(size)]
        self.meta_time = 0
        self.history = []

    def get_neighbors(self, x, y, z):
        offsets = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
        neighbors = []
        for dx, dy, dz in offsets:
            nx = (x + dx) % self.size
            ny = (y + dy) % self.size
            nz = (z + dz) % self.size
            neighbors.append(self.grid[nx][ny][nz])
        return neighbors

    def step(self):
        self.meta_time += 0.05
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    neighbors = self.get_neighbors(x, y, z)
                    self.grid[x][y][z].update(neighbors, self.meta_time)
        self.log_state()

    def visualize_step_interactive(self, step_index=-1):
        if step_index >= len(self.history):
            print(f"Invalid step index: {step_index}")
            return

        df = pd.DataFrame(self.history[step_index])
        fig = go.Figure(data=go.Scatter3d(
            x=df['x'], y=df['y'], z=df['z'],
            mode='markers',
            marker=dict(
                size=3,
                color=df['state'],  # Use resonance state for coloring
                colorscale='Viridis',
                colorbar=dict(title="State"),
                opacity=0.8
            ),
            text=[f"Phase: {p:.2f}<br>Info: {i}" for p, i in zip(df['phase'], df['information'])]
        ))

        fig.update_layout(
            title=f"Resonant Field Visualization (Step {step_index})",
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z'
            ),
            margin=dict(l=0, r=0, b=0, t=30)
        )
        fig.show()

    def animate_resonance_evolution(self):
        if not self.history:
            print("No history available for animation.")
            return

        frames = []
        for t, step in enumerate(self.history):
            df = pd.DataFrame(step)
            frame = go.Frame(
                data=[go.Scatter3d(
                    x=df['x'], y=df['y'], z=df['z'],
                    mode='markers',
                    marker=dict(
                        size=3,
                        color=df['state'],
                        colorscale='Viridis',
                        opacity=0.8,
                        colorbar=dict(title="State")
                    ),
                    text=[f"Phase: {p:.2f}<br>Info: {i}" for p, i in zip(df['phase'], df['information'])]
                )],
                name=str(t)
            )
            frames.append(frame)

        # Initial frame
        initial_df = pd.DataFrame(self.history[0])
        fig = go.Figure(
            data=[go.Scatter3d(
                x=initial_df['x'], y=initial_df['y'], z=initial_df['z'],
                mode='markers',
                marker=dict(
                    size=3,
                    color=initial_df['state'],
                    colorscale='Viridis',
                    opacity=0.8
                ),
                text=[f"Phase: {p:.2f}<br>Info: {i}" for p, i in zip(initial_df['phase'], initial_df['information'])]
            )],
            layout=go.Layout(
                title="Animated Resonant Field Evolution",
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[
                        dict(label="Play", method="animate", args=[None]),
                        dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}])
                    ]
                )],
                sliders=[{
                    "steps": [
                        {
                            "args": [[str(k)], {"frame": {"duration": 0, "redraw": True},
                                                "mode": "immediate"}],
                            "label": str(k),
                            "method": "animate"
                        } for k in range(len(self.history))
                    ],
                    "transition": {"duration": 0},
                    "x": 0, "y": -0.1,
                    "currentvalue": {"prefix": "Step: "}
                }],
                scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                margin=dict(l=0, r=0, b=0, t=30)
            ),
            frames=frames
        )
        fig.show()
        fig.write_html("resonance_animation.html")

    def log_state(self):
        step_data = []
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    k = self.grid[x][y][z]
                    step_data.append({
                        'x': x, 'y': y, 'z': z,
                        'state': k.state,
                        'phase': k.phase,
                        'information': k.information,
                        'meta_zeit': self.meta_time
                    })
        self.history.append(step_data)

    def export_csv(self, filename="hyperstructure_log.csv"):
        all_steps = [pd.DataFrame(step) for step in self.history]
        df = pd.concat(all_steps, keys=range(len(all_steps)), names=["time_step"])
        df.reset_index().to_csv(filename, index=False)
        return filename


# === Main function to execute ===
def run_simulation_3d(runtime_seconds=10, field_sizes=20):
    steps = int(runtime_seconds * 10)
    hyperfield = Hyperstructure3D(size=field_sizes)

    for _ in range(steps):
        hyperfield.step()

    filename = "hyperstructure_log.csv"
    path = os.path.join(os.getcwd(), filename)
    hyperfield.export_csv(filename=path)

    print(f"Simulation completed. Data saved at: {path}")

    # Show interactive 3D animation
    hyperfield.animate_resonance_evolution()


# === Execution ===
if __name__ == "__main__":
    try:
        runtime = float(input("Enter the desired runtime in seconds: "))
        field_size = int(input("Enter the desired field size (e.g. 20): "))
        run_simulation_3d(runtime_seconds=runtime, field_sizes=field_size)
    except Exception as e:
        print("Incorrect entry:", e)