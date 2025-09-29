import mysql.connector
import matplotlib.pyplot as plt

# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # replace with your MySQL username
    password="MYsql#517561",  # replace with your MySQL password
    database="healthcare_project"
)

cursor = conn.cursor()

# 2️⃣ Query disease counts from patients table
cursor.execute("SELECT disease, COUNT(*) FROM patients GROUP BY disease")
data = cursor.fetchall()

# Close connection
cursor.close()
conn.close()

# 3️⃣ Prepare data for plotting
diseases = [row[0] for row in data]
counts = [row[1] for row in data]

# 4️⃣ Plot bar chart
plt.figure(figsize=(6,4))
plt.bar(diseases, counts, color='skyblue')
plt.title('Number of Patients per Disease')
plt.xlabel('Disease')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.show(block=True)
