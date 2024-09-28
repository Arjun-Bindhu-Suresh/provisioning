# provisioning_loops.py
# Author: Arjun Bindhu Suresh
# Date: September 27, 2024
# Description: This program manages multiple resource allocation requests and checks if the requested CPU cores and memory are available.

# Define two Constants
Total_CPU_cores = 16  # Total CPU cores available
Total_CPU_memory = 64.0  # Total memory available in GB

# Creating two empty lists
allocated_resources = []
pending_requests = []

# Variables to track remaining resources
remaining_cpu = Total_CPU_cores
remaining_memory = Total_CPU_memory

# Main program loop
while True:
    # Get user inputs
    username = input("Enter username: ")
    required_cpu = int(input("Enter the number of required CPU cores: "))
    required_memory = float(input("Enter the amount of required memory (in GB): "))

    # Check if resources are available
    if required_cpu <= remaining_cpu and required_memory <= remaining_memory:
        # Add to allocated resources
        allocated_resources.append((username, required_cpu, required_memory))
        remaining_cpu -= required_cpu
        remaining_memory -= required_memory
        print(f"Resources allocated for {username}.")
    else:
        # Add to pending requests
        pending_requests.append((username, required_cpu, required_memory))
        print(f"Not enough resources for {username}. Added to pending requests.")

    # Ask if the user wants to make another request
    while True:
        another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
        if another_request == "yes":
            break  
        elif another_request == "no":
            print("Exiting the program...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if another_request == "no":
        break  

# Display allocated resources
print("\nAllocated Resources:")
for resource in allocated_resources:
    print(f"User: {resource[0]}, CPU Cores: {resource[1]}, Memory: {resource[2]} GB")

# Display pending requests
print("\nPending Requests:")
for request in pending_requests:
    print(f"User: {request[0]}, CPU Cores: {request[1]}, Memory: {request[2]} GB")

