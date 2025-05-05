import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("5G Network Simulation GUI")

# Canvas for visualizing network
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Draw nodes
nodes = {
    "gNodeB1": canvas.create_oval(250, 150, 300, 200, fill="skyblue", outline="black"),
    "UE1": canvas.create_oval(100, 100, 150, 150, fill="lightgreen", outline="black"),
    "UE2": canvas.create_oval(100, 250, 150, 300, fill="lightgreen", outline="black"),
    "5G Core": canvas.create_oval(400, 150, 450, 200, fill="pink", outline="black")
}

# Add labels for nodes
canvas.create_text(275, 135, text="gNodeB1", font=("Arial", 10, "bold"), fill="blue")
canvas.create_text(125, 85, text="UE1", font=("Arial", 10, "bold"), fill="green")
canvas.create_text(125, 235, text="UE2", font=("Arial", 10, "bold"), fill="green")
canvas.create_text(425, 135, text="5G Core", font=("Arial", 10, "bold"), fill="red")

# Draw connections
canvas.create_line(275, 175, 125, 125, fill="black", width=2)
canvas.create_line(275, 175, 125, 275, fill="black", width=2)
canvas.create_line(275, 175, 425, 175, fill="black", width=2)

# Function for simulating data transmission
def simulate_transmission():
    latencies = []
    for _ in range(5):
        latency = random.uniform(1, 3)
        latencies.append(latency)
        messagebox.showinfo("Transmission Result", f"Latency: {latency:.2f} seconds")
    print("Latencies:", latencies)

# Add a button to start simulation
start_button = tk.Button(root, text="Start Simulation", command=simulate_transmission)
start_button.pack()

# Run the main GUI loop
root.mainloop()
