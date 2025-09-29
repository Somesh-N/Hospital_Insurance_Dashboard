CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    bloodtype VARCHAR(5),
    medical_condition VARCHAR(255),
    admission_date DATE,
    doctor VARCHAR(100),
    hospital_name VARCHAR(100),
    insurance_provider VARCHAR(100),
    billing DECIMAL(10,2),
    room_number VARCHAR(10),
    medication VARCHAR(255),
    test_result VARCHAR(255)
);
