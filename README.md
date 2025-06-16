# Final Project: Student Outcome Prediction and Analysis

## Business Understanding

Jaya Jaya Institute, an educational institution established in 2000, has a strong reputation for producing high-quality graduates. However, the institute faces a significant challenge with a considerable number of students who do not complete their education and drop out. This high dropout rate is a major concern that the institute aims to address proactively.

### Business Problem

The primary business problem is the high student dropout rate. The institute needs to develop a system to identify a student's likely academic outcome as early as possible. This early identification will allow the institute to provide targeted guidance to students at risk of dropping out, while also understanding the profile of those likely to graduate.

### Project Scope

The scope of this project is to assist Jaya Jaya Institute by:

1.  Analyzing a comprehensive student dataset to identify the key factors that correlate with student outcomes.
2.  Developing and comparing machine learning models, including **`RandomForestClassifier`** and **`XGBoostClassifier`**, for a multi-class classification task to predict if a student will `Dropout`, remain `Enrolled`, or `Graduate`.
3.  Creating an interactive dashboard for the institute to monitor key student performance indicators.
4.  Building a prototype of the machine learning system using the best-performing model.

### Preparation

**Data Source:**
The dataset used for this project is the "Predict students' dropout and academic success" dataset from the UCI Machine Learning Repository. The original three-class target variable (`Dropout`, `Enrolled`, `Graduate`) was used for model training and evaluation.

You can access the dataset via the following link **[here](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)**.

**Setup Environment:**
To set up the environment, ensure you have Python installed.

1. Clone this repository to your local machine. (Please replace the URL with your actual repository link).
```
git clone https://github.com/liswahyuni/StudentPerformace.git
```
2. Navigate to the cloned project directory:
```
cd your-repository-name
```
3. Open and run Anaconda Prompt from this directory.

Create a new Conda environment (e.g., student-project):
```
conda create --name student-project python=3.10
```
4. Activate the newly created environment:
```
conda activate student-project
```
5. Install all the required libraries from the requirements.txt file:
```
pip install -r requirements.txt
```
6. Open the notebook.ipynb file:
```
python notebook.ipynb
```
## Business Dashboard

An interactive business dashboard was created using Tableau to help the Jaya Jaya Institute management monitor student data effectively. The dashboard provides visualizations of the most critical factors influencing student outcomes. This tool enables the administration to quickly identify trends and patterns, facilitating data-driven strategic planning to improve student retention.

The dashboard can be accessed on Tableau Public via the following link:
**[Dashboard Student Performance](https://public.tableau.com/views/DashboardStudentPerformance/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

## Running the Machine Learning System

A prototype of the machine learning system has been deployed as a Streamlit application. After evaluating multiple algorithms for the multi-class problem, the final system utilizes a trained model to provide real-time predictions. An administrator can input a student's information, and the system will output a prediction of the student's likely academic status: **Dropout, Enrolled, or Graduate**.

The prototype is publicly hosted and can be accessed via the following link:
**[https://studentperformance-liswahyuni.streamlit.app/](https://studentperformance-liswahyuni.streamlit.app/)** 

To run the prototype locally, execute the following command in your terminal:

```bash
streamlit run app.py
```

## Conclusion

This project successfully developed and evaluated the best robust machine learning model (**XGBoost**) for predicting student outcomes across three classes. The final model demonstrates strong performance, achieving an overall **weighted avg F1-score of training set approximately 86%** and **weighted avg F1-score of testing set approximately 75%**.

The dashboard reveals a critical situation at Jaya Jaya Institute, with a dropout rate of 32.12%, meaning nearly one-third of all students fail to complete their studies. While the student body is predominantly female (64.83%) and attends during the daytime (89.08%), these factors do not appear to be the primary drivers of the issue.

The most telling insight comes from the socio-economic breakdown of students who drop out. The treemap indicates a significant concentration of dropouts among students whose mothers are in unskilled occupations and have lower levels of formal education. This suggests that students from less privileged socio-economic backgrounds are disproportionately at risk of dropping out.

The resulting models and dashboard provide Jaya Jaya Institute with powerful tools to transition from a reactive to a proactive approach in managing student pathways.

### Recommended Action Items

Based on the project findings, here are several actionable recommendations for Jaya Jaya Institute:

1.  **Develop Targeted Financial Aid and Support Programs:**
    * **Action:** Proactively identify and reach out to students whose family backgrounds (as indicated by parental occupation and education) align with the high-risk profiles shown in the treemap.
    * **Reasoning:** These students are the most vulnerable. Offering them targeted scholarships, flexible tuition payment plans, or part-time work opportunities can alleviate the financial pressure that is likely a major contributor to their decision to drop out.

2.  **Establish a Mentorship Program:**
    * **Action:** Create a mentorship program pairing first-generation students or those from at-risk backgrounds with successful senior students, alumni, or faculty members who have similar backgrounds.
    * **Reasoning:** Beyond financial aid, these students may lack the social and academic support systems that are crucial for navigating higher education. A mentor can provide guidance, encouragement, and a valuable network.

3.  **Integrate Early Academic Intervention:**
    * **Action:** While not explicitly shown in this dashboard view, the next step is to cross-reference this socio-economic data with first-semester academic performance (like grades and approved credits). Students who fit the at-risk demographic *and* show early signs of academic struggle should be the top priority for intervention.
    * **Reasoning:** Combining socio-economic risk factors with academic performance data will create a highly accurate early warning system, allowing the institute to intervene with academic counseling and support before it's too late.