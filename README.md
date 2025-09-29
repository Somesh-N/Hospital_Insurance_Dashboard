# Hospital & Insurance Performance Insights — Power BI Dashboard

## Project Overview

This project presents a detailed Power BI dashboard analyzing hospital and insurance performance metrics .
As a final-year engineering student Intereted in data Engineering , I developed this project to demonstrate my ability to Handle raw data with SQL & Transform into actionable insights using Power BI Without Using Any Of The Pre-Defined Templates or Themes.


## Objectives

- Visualize key performance indicators for hospitals and insurance providers
- Analyze treatment cost variations by age, gender, region, and insurance type
- Track patient admission trends and average Bill trends over the years 
- Compare claim ratios across major insurance providers
- Apply advanced Power BI techniques for layout, filtering, and interactivity

---

## Dataset Summary
Dataet url :[https://1drv.ms/x/c/d72b75e7ea0e398d/EUCDSQ8yTiZOpX59mOEJuA4B9ChZfxQu16smeHDW7QGFYA?e=scX3Xb]

It is a large dataset of 55,000 Entries  That  includes anonymized records under Fields:
- Patient ID  
- Hospital Type  
- Insurance Provider  
- Gender  
- Age  
- Region  
- Treatment Cost  
- Medication Type
- Type of Admission
- name
-age
-name
-age
-gender
--bloodtype
--medical_condition
-admission_date
-doctor
-hospital_name
-insurance_provider
-billing
-room_number
-medication
-test_result



---

## Dashboard Features

### Insurance Provider Analysis
- Claim ratio comparison across six major providers
- Gender distribution segmented by provider
- Time-series trends of admissions

### Hospital Performance Metrics
- Total hospital count and type-wise breakdown
- Average patient age and length of stay by provider
- Billing Trends over Time
- Gender Distributions across Genders

### Treatment Breakdown
-Admission Trends & Test Result
- Cost trends by age group and gender
- Regional and insurance-based cost variations
- Successful Medication based on Admission Type

---
### Real-World Applications from Dashboard Patterns
- Helps patients identify insurance providers with high claim failure rates before choosing coverage.
- Enables insurers to monitor gender-wise disease distribution and launch targeted wellness campaigns.
- Tracks billing trends over time to support hospital revenue forecasting and budget planning.
- Analyzes average treatment and result times to improve diagnostic turnaround and service quality.
- Reveals age-wise claim rejection patterns across providers to guide smarter insurance decisions for customers.


---
## Technical Implementation

- Tool: Power BI Desktop  
- File Format: `.pbix`  
- Techniques Used:
  -imported Dataset & converted intoo CSV file.
  - Used Pandas & Matplotlib Libraries for Handling Data & Initial Visualization
  - MySQL Workbench 8.0 CE To Normalise & Cleaning The Data
  - mysql-connector-python TO connect Python & SQL 
  - DAX for calculated columns and measures
  - Used visualisation and Data Fields  For The optimization
  -  Handled Cross-filtering and drill-through functions
  - GitHub Desktop & GitBash For The Repo
  
---

## How to Run

1. Clone or download this repository  
2. Open `Healthcare_Insights.pbix` in Power BI Desktop  
3. Explore the interactive dashboard.  
4.  Interact with filters and visuals to explore insights 

---

## Author

N Somesh  
Final Year Engineering Student Interested in Data Engineering & Roles 

Email: someshnalluri78@gmail.com  
LinkedIn:www.linkedin.com/in/someshn

---

## Notes

This dashboard is intended for academic and portfolio purposes. All data used is either simulated or anonymized. Feedback and suggestions for improvement are welcome.

