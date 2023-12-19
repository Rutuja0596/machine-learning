import pickle
import streamlit as st
from streamlit_option_menu import option_menu

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("C:/Users/Rutuja/Desktop/Mult_Disease_Predict/reports-b55ce-firebase-adminsdk-befwj-ebfd0922f9.json")  #service account key
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Rutuja/Desktop/Mult_Disease_Predict/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/Rutuja/Desktop/Mult_Disease_Predict/heart_model.sav','rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],
                icons = ['box','heart'],menu_icon="cast",
                default_index=1)

    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')

    name = st.text_input("Enter Name")
    options = ["Male", "Female", "Others"]
    gender = st.radio("Gender", options)
    age = st.number_input("Enter Age", min_value=0)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure mmHg')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    
    with col2:
        Insulin = st.text_input('Insulin')
    
    with col3:
        BMI = st.text_input('BMI')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Enter Age')
        
    
    # code for Prediction
    diab_diagnos = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnos = 'Diabetes tests positive'
        else:
          diab_diagnos = 'Non Diabetic'
    
   
    st.success(diab_diagnos)
doc_ref = db.collection("patients").add({"name": name,"gender":gender,"age": age,"results":diab_diagnos})
    
    

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        gender = st.number_input('gender')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnos = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, gender, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnos = 'The person is having heart disease'
        else:
          heart_diagnos = 'The person does not have any heart disease'

        st.success(heart_diagnos)
    doc_ref = db.collection("heart").add({"name": name,"gender":gender,"age": age,"results":heart_diagnos})

#text = ''':pill: :syringe:'''
    
st.markdown("""<style>
 [data-testid=stSidebar] {
        background-color: #00FF80;
    }
}
</style>""",unsafe_allow_html=True)


