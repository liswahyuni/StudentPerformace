import streamlit as st
import prediction
import pandas as pd

st.set_page_config(page_title="Student Status Prediction", layout="centered")
st.title("Student Status Prediction")

# Define input fields for all features
# You should adjust these fields to match your actual features and their types

student_input = {}
student_input['Marital_status'] = st.number_input('Marital_status', min_value=0, max_value=10, value=1)
student_input['Application_mode'] = st.number_input('Application_mode', min_value=0, max_value=10000, value=1)
student_input['Application_order'] = st.number_input('Application_order', min_value=0, max_value=100, value=1)
student_input['Course'] = st.number_input('Course', min_value=0, max_value=10000, value=1)
student_input['Daytime_evening_attendance'] = st.number_input('Daytime_evening_attendance', min_value=0, max_value=10000, value=1)
student_input['Previous_qualification'] = st.number_input('Previous_qualification', min_value=0, max_value=100, value=1)
student_input['Previous_qualification_grade'] = st.number_input('Previous_qualification_grade', min_value=0.0, max_value=200.0, value=122.0)
student_input['Nacionality'] = st.number_input('Nacionality', min_value=0, max_value=200, value=1)
student_input['Mothers_qualification'] = st.number_input('Mothers_qualification', min_value=0, max_value=100, value=1)
student_input['Fathers_qualification'] = st.number_input('Fathers_qualification', min_value=0, max_value=100, value=19)
student_input['Mothers_occupation'] = st.number_input('Mothers_occupation', min_value=0, max_value=100, value=12)
student_input['Fathers_occupation'] = st.number_input('Fathers_occupation', min_value=0, max_value=100, value=5)
student_input['Admission_grade'] = st.number_input('Admission_grade', min_value=0.0, max_value=200.0, value=127.3)
student_input['Displaced'] = st.number_input('Displaced', min_value=0, max_value=1, value=1)
student_input['Educational_special_needs'] = st.number_input('Educational_special_needs', min_value=0, max_value=1, value=0)
student_input['Debtor'] = st.number_input('Debtor', min_value=0, max_value=1, value=0)
student_input['Tuition_fees_up_to_date'] = st.number_input('Tuition_fees_up_to_date', min_value=0, max_value=1, value=0)
student_input['Gender'] = st.number_input('Gender', min_value=0, max_value=1, value=1)
student_input['Scholarship_holder'] = st.number_input('Scholarship_holder', min_value=0, max_value=1, value=1)
student_input['Age_at_enrollment'] = st.number_input('Age_at_enrollment', min_value=0, max_value=100, value=20)
student_input['International'] = st.number_input('International', min_value=0, max_value=1, value=0)
student_input['Curricular_units_1st_sem_credited'] = st.number_input('Curricular_units_1st_sem_credited', min_value=0, max_value=50, value=0)
student_input['Curricular_units_1st_sem_enrolled'] = st.number_input('Curricular_units_1st_sem_enrolled', min_value=0, max_value=50, value=0)
student_input['Curricular_units_1st_sem_evaluations'] = st.number_input('Curricular_units_1st_sem_evaluations', min_value=0, max_value=50, value=0)
student_input['Curricular_units_1st_sem_approved'] = st.number_input('Curricular_units_1st_sem_approved', min_value=0, max_value=50, value=0)
student_input['Curricular_units_1st_sem_grade'] = st.number_input('Curricular_units_1st_sem_grade', min_value=0.0, max_value=20.0, value=0.0)
student_input['Curricular_units_1st_sem_without_evaluations'] = st.number_input('Curricular_units_1st_sem_without_evaluations', min_value=0, max_value=50, value=0)
student_input['Curricular_units_2nd_sem_credited'] = st.number_input('Curricular_units_2nd_sem_credited', min_value=0, max_value=50, value=0)
student_input['Curricular_units_2nd_sem_enrolled'] = st.number_input('Curricular_units_2nd_sem_enrolled', min_value=0, max_value=50, value=0)
student_input['Curricular_units_2nd_sem_evaluations'] = st.number_input('Curricular_units_2nd_sem_evaluations', min_value=0, max_value=50, value=0)
student_input['Curricular_units_2nd_sem_approved'] = st.number_input('Curricular_units_2nd_sem_approved', min_value=0, max_value=50, value=0)
student_input['Curricular_units_2nd_sem_grade'] = st.number_input('Curricular_units_2nd_sem_grade', min_value=0.0, max_value=20.0, value=0.0)
student_input['Curricular_units_2nd_sem_without_evaluations'] = st.number_input('Curricular_units_2nd_sem_without_evaluations', min_value=0, max_value=50, value=0)
student_input['Unemployment_rate'] = st.number_input('Unemployment_rate', min_value=0.0, max_value=100.0, value=10.8)
student_input['Inflation_rate'] = st.number_input('Inflation_rate', min_value=-10.0, max_value=10.0, value=1.4)
student_input['GDP'] = st.number_input('GDP', min_value=-10.0, max_value=100.0, value=1.74)

if st.button('Predict'):
    pred = prediction.predict(student_input)
    st.success(f"Predicted Status: {pred}")