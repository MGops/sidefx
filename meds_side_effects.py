from collections import Counter

# Define the dictionary with medications and their side effects
medications = {
    'A': [1, 2, 3],
    'B': [1, 2, 4, 5],
    'C': [1, 4, 5],
    'D': [1, 5]
}

# Function to get the hierarchical list of side effects based on the medications a patient is taking
def get_side_effects(patient_medications, med_dict):
    side_effects_counter = Counter()
    
    # Count the frequency of each side effect across the selected medications
    for med in patient_medications:
        if med in med_dict:
            side_effects_counter.update(med_dict[med])
    
    # Sort side effects by frequency in descending order
    sorted_side_effects = sorted(side_effects_counter.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_side_effects

# Function to input medications
def input_medications():
    # Input: Medications the patient is taking
    patient_medications = input("Enter the medications the patient is taking (separated by commas, e.g., A,B,D): ").split(',')
    # Strip any extra whitespace from each medication
    patient_medications = [med.strip() for med in patient_medications]
    return patient_medications

# Get user input for the medications by creating a variable that turns it into a list
patient_medications = input_medications()

# Get the hierarchical list of side effects
side_effects_hierarchy = get_side_effects(patient_medications, medications)

# Print the side effects sorted by their frequency
print("Hierarchical list of side effects based on frequency:")
#for key, value in 
for side_effect, frequency in side_effects_hierarchy:
    print(f"Side effect {side_effect}: {frequency} occurrence(s)")
