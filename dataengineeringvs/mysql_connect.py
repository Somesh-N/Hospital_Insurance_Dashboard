import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    password="MYsql#517561",  # your MySQL password
    database="healthcare_project"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    disease VARCHAR(100),
    admission_date DATE
)
""")

# Insert sample data
cursor.execute("""
INSERT INTO patients (name, age, disease, admission_date)
VALUES 
('John Doe', 45, 'Diabetes', '2025-09-20'),
('Jane Smith', 30, 'Hypertension', '2025-09-21')
""")

conn.commit()

# Query table
cursor.execute("SELECT * FROM patients")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
