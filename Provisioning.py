# provisioning.py
# Author: Arjun Bindhu Suresh
# Date: September 27, 2024
# Description: This script simulates a cloud resource provisioning system by checking if the requested CPU cores and memory can be allocated based on available resources.

# Define two Constants
The_total_number_of_CPU_cores_available = 16  # Total CPU cores available
The_total_amount_of_memory_available_in_gigabytes_GB = 64.0  # Total memory available in GB

# Ask the user to input two values, stored in variables
required_CPU = int(input("Enter the number of required CPU cores: "))
required_memory = float(input("Enter the amount of required memory (in GB): "))

# Variables to keep track of remaining resources
remaining_CPU = The_total_number_of_CPU_cores_available
remaining_memory = The_total_amount_of_memory_available_in_gigabytes_GB

# check whether the required values entered by the user are available based on the limits defined as constants
if required_CPU <= remaining_CPU and required_memory <= remaining_memory:
    print("Resources provisioned successfully.")
    # Update remaining resources after provisioning
    remaining_CPU -= required_CPU
    remaining_memory -= required_memory
else:
    print("Resource request exceeds capacity level. Provisioning failed.")

# Display the total remaining CPU cores and memory available resources
print(f"Remaining CPU cores: {remaining_CPU}")
print(f"Remaining memory (GB): {remaining_memory}")





    






