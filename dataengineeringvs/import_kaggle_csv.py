import pandas as pd
import mysql.connector

# 1️⃣ Read CSV
df = pd.read_csv(r"C:\Users\SOMESH.N\OneDrive\Desktop\Data Engineeringproject\dataengineeringvs\patients_kaggle.csv")

# 2️⃣ Convert 'Date of Admission' to YYYY-MM-DD format
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], dayfirst=True, errors='coerce')

# 3️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",               # replace with your MySQL username
    password="MYsql#517561",  # replace with your MySQL password
    database="healthcare_project"
)
cursor = conn.cursor()

# 4️⃣ Insert data into patients table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO patients (name, age, gender, bloodtype, medical_condition, admission_date,
                              doctor, hospital_name, insurance_provider, billing, room_number,
                              admission_type, medication, test_result)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        str(row['Name']),
        int(row['Age']),
        str(row['Gender']),
        str(row['Blood Type']),
        str(row['Medical Condition']),
        row['Date of Admission'].strftime('%Y-%m-%d') if not pd.isna(row['Date of Admission']) else None,
        str(row['Doctor']),
        str(row['Hospital']),
        str(row['Insurance Provider']),
        float(row['Billing Amount']),
        str(row['Room Number']),
        str(row['Admission Type']),
        str(row['Medication']),
        str(row['Test Results'])
    ))

# 5️⃣ Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Kaggle healthcare data imported successfully!")
