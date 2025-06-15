import streamlit as st
import pandas as pd
import prediction 

# --- Page Configuration ---
st.set_page_config(
    page_title="Student Success Predictor",
    page_icon="🎓",
    layout="wide"
)

# --- CSS Custom (Dark-Mode Friendly) ---
st.markdown("""
<style>
    /* ------------------- */
    /* --- LIGHT THEME --- */
    /* ------------------- */

    /* Latar Belakang Aplikasi Utama (Biru Sangat Terang) */
    .stApp {
        background-color: #f0f5ff;
    }

    /* Judul Utama (Biru Sangat Gelap) */
    h1 {
        color: #002147;
        text-align: center;
        font-weight: bold;
    }

    /* Label untuk semua widget (Biru Gelap) */
    .st-emotion-cache-q8sbsg {
        color: #002147;
        font-weight: 550;
    }
    
    /* Sub-judul di dalam Expander */
    .st-emotion-cache-12w0qpk h2 {
       color: #002147;
       font-size: 1.25rem;
    }

    /* Box Expander (Latar Belakang Biru Muda dengan Border Biru Sedang) */
    .st-emotion-cache-12w0qpk {
        background-color: #d9e6f6; 
        border-radius: 10px;
        border: 1px solid #a7c7e7;
    }
    
    /* Judul Expander (Biru Gelap) */
    .st-emotion-cache-lrlib, .st-emotion-cache-1629p8f {
        font-weight: bold;
        color: #002147;
    }
    
    /* Tombol */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        border: 2px solid #002147;
        background-color: #1c4e80;
        color: #ffffff; /* Teks putih di tombol agar kontras */
        font-size: 20px;
        font-weight: bold;
        padding: 10px 0;
    }
    .stButton>button:hover {
        background-color: #002147; 
        border-color: #002147;
    }

    /* Kotak Hasil Prediksi (Sukses) */
    .st-emotion-cache-1pxazr7 {
        border-radius: 10px;
        text-align: center;
        padding: 20px;
        font-size: 24px;
        font-weight: bold;
        background-color: #e6f7ff; 
        color: #002147;
        border: 1px solid #1c4e80;
    }

    /* ------------------ */
    /* --- DARK THEME --- */
    /* ------------------ */

    /* Override warna untuk Dark Mode */
    body.theme-dark .stApp {
        background-color: #0b1a30; /* Latar Belakang Biru Navy Gelap */
    }

    body.theme-dark h1,
    body.theme-dark .st-emotion-cache-q8sbsg, /* Label Widget */
    body.theme-dark .st-emotion-cache-12w0qpk h2 { /* Sub-judul */
        color: #cddcfa; /* Warna Font Biru Terang untuk Kontras */
    }

    body.theme-dark .st-emotion-cache-12w0qpk {
        background-color: #1c2b4a; /* Latar Box Biru Gelap */
        border: 1px solid #3c5a8a;
    }

    body.theme-dark .st-emotion-cache-lrlib,
    body.theme-dark .st-emotion-cache-1629p8f {
        color: #cddcfa; /* Judul Expander Biru Terang */
    }

    body.theme-dark .st-emotion-cache-1pxazr7 {
        background-color: #1c3a4a;
        color: #e6f7ff;
        border: 1px solid #3c5a8a;
    }

</style>
""", unsafe_allow_html=True)


# Data Mapping
marital_status_map = {1: 'Single', 2: 'Married', 3: 'Widower', 4: 'Divorced', 5: 'Facto Union', 6: 'Legally Separated'}
application_mode_map = {1: '1st phase - general contingent', 2: 'Ordinance No. 612/93', 5: '1st phase - special contingent (Azores Island)', 7: 'Holders of other higher courses', 10: 'Ordinance No. 854-B/99', 15: 'International student (bachelor)', 16: '1st phase - special contingent (Madeira Island)', 17: '2nd phase - general contingent', 18: '3rd phase - general contingent', 26: 'Ordinance No. 533-A/99, item b2)', 27: 'Ordinance No. 533-A/99, item b3', 39: 'Over 23 years old', 42: 'Transfer', 43: 'Change of course', 44: 'Technological specialization diploma holders', 51: 'Change of institution/course', 53: 'Short cycle diploma holders', 57: 'Change of institution/course (International)'}
course_map = {33: 'Biofuel Production Technologies', 171: 'Animation and Multimedia Design', 8014: 'Social Service (evening attendance)', 9003: 'Agronomy', 9070: 'Communication Design', 9085: 'Veterinary Nursing', 9119: 'Informatics Engineering', 9130: 'Equinculture', 9147: 'Management', 9238: 'Social Service', 9254: 'Tourism', 9500: 'Nursing', 9556: 'Oral Hygiene', 9670: 'Advertising and Marketing Management', 9773: 'Journalism and Communication', 9853: 'Basic Education', 9991: 'Management (evening attendance)'}
prev_qual_map = {1: "Secondary education", 2: "Higher education - bachelor's degree", 3: "Higher education - degree", 4: "Higher education - master's", 5: "Higher education - doctorate", 6: "Frequency of higher education", 9: "12th year of schooling - not completed", 10: "11th year of schooling - not completed", 12: "Other - 11th year of schooling", 14: "10th year of schooling", 15: "10th year of schooling - not completed", 19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.", 38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.", 39: "Technological specialization course", 40: "Higher education - degree (1st cycle)", 42: "Professional higher technical course", 43: "Higher education - master (2nd cycle)"}
nationality_map = {1: 'Portuguese', 2: 'German', 6: 'Spanish', 11: 'Italian', 13: 'Dutch', 14: 'English', 17: 'Lithuanian', 21: 'Angolan', 22: 'Cape Verdean', 24: 'Guinean', 25: 'Mozambican', 26: 'Santomean', 32: 'Turkish', 41: 'Brazilian', 62: 'Romanian', 100: 'Moldova (Republic of)', 101: 'Mexican', 103: 'Ukrainian', 105: 'Russian', 108: 'Cuban', 109: 'Colombian'}
parent_qual_map = {1: "Secondary Education - 12th Year of Schooling or Eq.", 2: "Higher Education - Bachelor's Degree", 3: "Higher Education - Degree", 4: "Higher Education - Master's", 5: "Higher Education - Doctorate", 6: "Frequency of Higher Education", 9: "12th Year of Schooling - Not Completed", 10: "11th Year of Schooling - Not Completed", 11: "7th Year (Old)", 12: "Other - 11th Year of Schooling", 13: "2nd year complementary high school course", 14: "10th Year of Schooling", 18: "General commerce course", 19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.", 20: "Complementary High School Course", 22: "Technical-professional course", 25: "Complementary High School Course - not concluded", 26: "7th year of schooling", 27: "2nd cycle of the general high school course", 29: "9th Year of Schooling - Not Completed", 30: "8th year of schooling", 31: "General Course of Administration and Commerce", 33: "Supplementary Accounting and Administration", 34: "Unknown", 35: "Can't read or write", 36: "Can read without having a 4th year of schooling", 37: "Basic education 1st cycle (4th/5th year) or equiv.", 38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.", 39: "Technological specialization course", 40: "Higher education - degree (1st cycle)", 41: "Specialized higher studies course", 42: "Professional higher technical course", 43: "Higher Education - Master (2nd cycle)", 44: "Higher Education - Doctorate (3rd cycle)"}
occupation_map = {0: "Student", 1: "Directors & Executive Managers", 2: "Specialists in Intellectual and Scientific Activities", 3: "Intermediate Level Technicians and Professions", 4: "Administrative staff", 5: "Personal Services, Security and Sellers", 6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", 7: "Skilled Workers in Industry, Construction and Craftsmen", 8: "Installation and Machine Operators and Assembly Workers", 9: "Unskilled Workers", 10: "Armed Forces Professions", 90: "Other Situation", 99: "(blank)", 101: "Armed Forces Officers", 102: "Armed Forces Sergeants", 103: "Other Armed Forces personnel", 112: "Directors of administrative and commercial services", 114: "Hotel, catering, trade and other services directors", 121: "Specialists in the physical sciences, mathematics, engineering", 122: "Health professionals", 123: "Teachers", 124: "Specialists in finance, accounting, etc.", 125: "Specialists in ICT", 131: "Intermediate level science and engineering technicians", 132: "Intermediate level health technicians", 134: "Intermediate level technicians (legal, social, sports, etc.)", 135: "Information and communication technology technicians", 141: "Office workers, secretaries, data processing operators", 143: "Data, accounting, statistical, financial services operators", 144: "Other administrative support staff", 151: "Personal service workers", 152: "Sellers", 153: "Personal care workers", 154: "Protection and security services personnel", 161: "Market-oriented farmers and skilled agricultural workers", 163: "Subsistence farmers, fishermen, hunters", 171: "Skilled construction workers", 172: "Skilled workers in metallurgy, metalworking", 174: "Skilled workers in electricity and electronics", 175: "Workers in food processing, woodworking, clothing, etc.", 181: "Fixed plant and machine operators", 182: "Assembly workers", 183: "Vehicle drivers and mobile equipment operators", 191: "Cleaning workers", 192: "Unskilled workers in agriculture", 193: "Unskilled workers in industry, construction", 194: "Meal preparation assistants", 195: "Street vendors and street service providers"}
binary_map_yes_no = {1: 'Yes', 0: 'No'}
binary_map_gender = {1: 'Male', 0: 'Female'}
binary_map_attendance = {1: 'Daytime', 0: 'Evening'}

# Application Title
st.title("🎓 Student Success Predictor")
st.markdown("<h3 style='text-align: center; color: #333;'>Enter the student's details below to predict their academic outcome.</h3>", unsafe_allow_html=True)
st.markdown("---")

# This will be used to store the user's input.
student_input = {}

# --- Input Fields ---

with st.expander("👤 Personal & Demographic Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        student_input['Marital_status'] = st.selectbox('Marital Status', options=list(marital_status_map.keys()), format_func=lambda x: marital_status_map[x])
        student_input['Gender'] = st.selectbox('Gender', options=list(binary_map_gender.keys()), format_func=lambda x: binary_map_gender[x])
    with col2:
        student_input['Nacionality'] = st.selectbox('Nationality', options=list(nationality_map.keys()), format_func=lambda x: nationality_map[x], index=list(nationality_map.keys()).index(1)) # Default to Portuguese
        student_input['International'] = st.selectbox('Is the student international?', options=list(binary_map_yes_no.keys()), format_func=lambda x: binary_map_yes_no[x])
    with col3:
        student_input['Age_at_enrollment'] = st.number_input('Age at Enrollment', min_value=17, max_value=70, value=20)
        student_input['Displaced'] = st.selectbox('Is the student displaced?', options=list(binary_map_yes_no.keys()), format_func=lambda x: binary_map_yes_no[x])

with st.expander("📚 Academic & Application Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        student_input['Course'] = st.selectbox('Chosen Course', options=list(course_map.keys()), format_func=lambda x: course_map[x])
        student_input['Previous_qualification'] = st.selectbox('Previous Qualification', options=list(prev_qual_map.keys()), format_func=lambda x: prev_qual_map[x])
    with col2:
        student_input['Application_mode'] = st.selectbox('Application Mode', options=list(application_mode_map.keys()), format_func=lambda x: application_mode_map[x])
        student_input['Previous_qualification_grade'] = st.number_input('Previous Qualification Grade', min_value=0.0, max_value=200.0, value=122.0)
    with col3:
        student_input['Application_order'] = st.number_input('Application Order (0=first choice)', min_value=0, max_value=10, value=1)
        student_input['Admission_grade'] = st.number_input('Admission Grade', min_value=0.0, max_value=200.0, value=127.3)

with st.expander("🏡 Socio-economic & Family Background"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Mother's Information")
        student_input['Mothers_qualification'] = st.selectbox("Mother's Qualification", options=list(parent_qual_map.keys()), format_func=lambda x: parent_qual_map[x], index=list(parent_qual_map.keys()).index(1))
        student_input['Mothers_occupation'] = st.selectbox("Mother's Occupation", options=list(occupation_map.keys()), format_func=lambda x: occupation_map[x], index=list(occupation_map.keys()).index(5))
    with col2:
        st.subheader("Father's Information")
        student_input['Fathers_qualification'] = st.selectbox("Father's Qualification", options=list(parent_qual_map.keys()), format_func=lambda x: parent_qual_map[x], index=list(parent_qual_map.keys()).index(1))
        student_input['Fathers_occupation'] = st.selectbox("Father's Occupation", options=list(occupation_map.keys()), format_func=lambda x: occupation_map[x], index=list(occupation_map.keys()).index(7))

with st.expander("💰 Status & Fees"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        student_input['Debtor'] = st.selectbox('Is the student a debtor?', options=list(binary_map_yes_no.keys()), format_func=lambda x: binary_map_yes_no[x])
    with col2:
        student_input['Tuition_fees_up_to_date'] = st.selectbox('Tuition fees up to date?', options=list(binary_map_yes_no.keys()), format_func=lambda x: binary_map_yes_no[x], index=1)
    with col3:
        student_input['Scholarship_holder'] = st.selectbox('Is the student a scholarship holder?', options=list(binary_map_yes_no.keys()), format_func=lambda x: binary_map_yes_no[x])
    with col4:
        student_input['Educational_special_needs'] = st.selectbox('Has special educational needs?', options=list(binary_map_yes_no.keys()), format_func=lambda x: binary_map_yes_no[x])

with st.expander("📈 Curricular Performance & Macroeconomic Factors"):
    st.subheader("Semester 1 Performance")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        student_input['Curricular_units_1st_sem_credited'] = st.number_input('1st Sem Units (Credited)', min_value=0, max_value=50, value=0)
    with col2:
        student_input['Curricular_units_1st_sem_enrolled'] = st.number_input('1st Sem Units (Enrolled)', min_value=0, max_value=50, value=6)
    with col3:
        student_input['Curricular_units_1st_sem_approved'] = st.number_input('1st Sem Units (Approved)', min_value=0, max_value=50, value=6)
    with col4:
        student_input['Curricular_units_1st_sem_grade'] = st.number_input('1st Sem Grade', min_value=0.0, max_value=20.0, value=13.5)

    st.subheader("Semester 2 Performance")
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        student_input['Curricular_units_2nd_sem_credited'] = st.number_input('2nd Sem Units (Credited)', min_value=0, max_value=50, value=0)
    with col6:
        student_input['Curricular_units_2nd_sem_enrolled'] = st.number_input('2nd Sem Units (Enrolled)', min_value=0, max_value=50, value=6)
    with col7:
        student_input['Curricular_units_2nd_sem_approved'] = st.number_input('2nd Sem Units (Approved)', min_value=0, max_value=50, value=6)
    with col8:
        student_input['Curricular_units_2nd_sem_grade'] = st.number_input('2nd Sem Grade', min_value=0.0, max_value=20.0, value=13.2)
    
    st.subheader("Additional Information")
    col9, col10, col11 = st.columns(3)
    with col9:
        student_input['Daytime_evening_attendance'] = st.selectbox('Attendance', options=list(binary_map_attendance.keys()), format_func=lambda x: binary_map_attendance[x])
    with col10:
        student_input['Curricular_units_1st_sem_evaluations'] = st.number_input('1st Sem Evaluations', min_value=0, max_value=50, value=8)
        student_input['Curricular_units_2nd_sem_evaluations'] = st.number_input('2nd Sem Evaluations', min_value=0, max_value=50, value=7)
    with col11:
        student_input['Curricular_units_1st_sem_without_evaluations'] = st.number_input('1st Sem w/o Evaluations', min_value=0, max_value=50, value=0)
        student_input['Curricular_units_2nd_sem_without_evaluations'] = st.number_input('2nd Sem w/o Evaluations', min_value=0, max_value=50, value=0)

    st.subheader("Macroeconomic Factors")
    col12, col13, col14 = st.columns(3)
    with col12:
        student_input['Unemployment_rate'] = st.number_input('Unemployment Rate (%)', min_value=0.0, max_value=20.0, value=10.8)
    with col13:
        student_input['Inflation_rate'] = st.number_input('Inflation Rate (%)', min_value=-5.0, max_value=5.0, value=1.4)
    with col14:
        student_input['GDP'] = st.number_input('GDP Growth Rate (%)', min_value=-5.0, max_value=5.0, value=1.74)
        

st.markdown("---")

# --- Tombol Prediksi dan Output ---
if st.button('Predict Student Outcome'):
    try:
        pred = prediction.predict(student_input)

        st.success(f"Predicted Outcome: {pred}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")