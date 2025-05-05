import random
import time
import simpy
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name, node_type):
        self.name = name
        self.node_type = node_type
        self.connections = []

    def add_connection(self, other_node):
        self.connections.append(other_node)

    def send_data(self, data, destination):
        if destination in self.connections:
            print(f"{self.name} ({self.node_type}) is sending data to {destination.name} ({destination.node_type})")
            # Simulate transmission time
            transmission_time = random.uniform(1, 3)
            time.sleep(transmission_time)
            print(f"Data delivered to {destination.name} in {transmission_time:.2f} seconds")
            return transmission_time
        else:
            print(f"{destination.name} is not directly connected to {self.name}")
            return None

# Example of a simple 5G network topology
gNodeB1 = Node("gNodeB1", "gNodeB")
ue1 = Node("UE1", "User Equipment")
ue2 = Node("UE2", "User Equipment")
core_network = Node("5GC", "5G Core")

# Establish connections
gNodeB1.add_connection(ue1)
ue1.add_connection(gNodeB1)
gNodeB1.add_connection(ue2)
ue2.add_connection(gNodeB1)
gNodeB1.add_connection(core_network)
core_network.add_connection(gNodeB1)

# Debugging: Print connections to verify
print("Connections for gNodeB1:", [node.name for node in gNodeB1.connections])

# Measure performance metrics
latencies = []
for _ in range(5):  # Simulate multiple transmissions
    latency = ue1.send_data("Hello", gNodeB1)
    if latency:
        latencies.append(latency)

# Visualize performance metrics
plt.plot(latencies, marker='o')
plt.title("Data Transmission Latency")
plt.xlabel("Transmission Attempt")
plt.ylabel("Latency (seconds)")
plt.grid()
plt.show()
