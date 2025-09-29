# simple_python_plot.py

import matplotlib.pyplot as plt

# Sample data
diseases = ['Diabetes', 'Hypertension', 'Asthma']
patient_count = [10, 15, 5]

# Create bar chart
plt.bar(diseases, patient_count, color='skyblue')
plt.xlabel('Disease')
plt.ylabel('Number of Patients')
plt.title('Number of Patients per Disease')

# Optional: show values on top of bars
for i, count in enumerate(patient_count):
    plt.text(i, count + 0.5, str(count), ha='center')

# Display the chart
plt.show()
