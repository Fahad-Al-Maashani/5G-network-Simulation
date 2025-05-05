import tkinter as tk
import random
import threading

# Create the main window
root = tk.Tk()
root.title("5G Network Simulation with Repeated Flows")

# Canvas for visualizing network
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Draw nodes
nodes = {
    "gNodeB1": canvas.create_oval(250, 150, 300, 200, fill="skyblue", outline="black"),
    "UE1": canvas.create_oval(100, 100, 150, 150, fill="lightgreen", outline="black"),
    "UE2": canvas.create_oval(100, 250, 150, 300, fill="lightgreen", outline="black")
}

# Add labels for nodes
canvas.create_text(275, 135, text="gNodeB1", font=("Arial", 10, "bold"), fill="blue")
canvas.create_text(125, 85, text="UE1", font=("Arial", 10, "bold"), fill="green")
canvas.create_text(125, 235, text="UE2", font=("Arial", 10, "bold"), fill="green")

# Draw connections
connections = [
    canvas.create_line(275, 175, 125, 125, fill="black", width=2),  # UE1 ↔ gNodeB1
    canvas.create_line(275, 175, 125, 275, fill="black", width=2)   # UE2 ↔ gNodeB1
]

def animate_signal(start_x, start_y, end_x, end_y, duration):
    """Animate the signal (circle) moving between two points."""
    steps = 100  # Number of steps in the animation
    delay = int(duration * 1000 / steps)  # Delay per step in milliseconds
    delta_x = (end_x - start_x) / steps
    delta_y = (end_y - start_y) / steps

    # Create a new signal for each animation
    signal = canvas.create_oval(0, 0, 0, 0, fill=random.choice(["red", "blue", "green", "orange"]), outline="")

    def step_signal(step):
        if step <= steps:
            canvas.move(signal, delta_x, delta_y)
            root.after(delay, step_signal, step + 1)
        else:
            canvas.delete(signal)  # Remove signal after animation completes

    canvas.coords(signal, start_x - 5, start_y - 5, start_x + 5, start_y + 5)
    step_signal(0)

def start_flow_from_ue1():
    """Start data flow from UE1 to gNodeB1."""
    start_x, start_y = 125, 125  # UE1 position
    end_x, end_y = 275, 175  # gNodeB1 position
    latency = random.uniform(1, 3)  # Simulate latency
    threading.Thread(target=animate_signal, args=(start_x, start_y, end_x, end_y, latency)).start()

def start_flow_from_ue2():
    """Start data flow from UE2 to gNodeB1."""
    start_x, start_y = 125, 275  # UE2 position
    end_x, end_y = 275, 175  # gNodeB1 position
    latency = random.uniform(1, 3)  # Simulate latency
    threading.Thread(target=animate_signal, args=(start_x, start_y, end_x, end_y, latency)).start()

# Add buttons for controlling data flow
button_frame = tk.Frame(root)
button_frame.pack()

ue1_button = tk.Button(button_frame, text="Start Flow from UE1", command=start_flow_from_ue1)
ue1_button.grid(row=0, column=0, padx=10, pady=5)

ue2_button = tk.Button(button_frame, text="Start Flow from UE2", command=start_flow_from_ue2)
ue2_button.grid(row=0, column=1, padx=10, pady=5)

# Run the main GUI loop
root.mainloop()
