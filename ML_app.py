import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier

#loading up the Classification model we created

model = DecisionTreeClassifier(criterion='entropy', max_depth=10, min_samples_leaf=5,
                       random_state=0)
model = joblib.load('finalized_model.joblib')
#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(Buying, Maint, Doors, Persons, Lug_boot, Safety):
    if  Safety == 'med':
        Safety = 1
    elif Safety == 'high':
        Safety = 2
    elif Safety == 'low':
        Safety = 3
    df = pd.DataFrame([Buying, Maint, Doors, Persons, Lug_boot, Safety]),
    columns=(['buying','maint','doors','persons','lug_boot','safety'])
    prediction =model.predict([[Buying, Maint, Doors, Persons, Lug_boot, Safety]])
    return prediction

st.title('Car Evalution Classification')
st.image("""https://duckduckgo.com/?t=h_&q=lamborghini&iax=images&ia=images&iai=https%3A%2F%2Fcar-images.bauersecure.com%2Fpagefiles%2F68553%2Fzlambo-003.jpg""")
st.header('enter the information of the car:')
st.text("vhigh = 1 high = 2 med = 3 low = 4")

Buying = st.number_input('buying:', min_value=1, max_value=4, value=1)
st.text("vhigh = 1 high = 2 med 3 low = 4")

Maint = st.number_input('maint:', min_value=1, max_value=4, value=1)

st.text("2-Doors = 1 3-Doors 2 4-Doors = 3 5more = 4")

Doors = st.number_input('doors:', min_value=1, max_value=4, value=1)

st.text("2-persons = 1 4-persons = 2 more = 3 ")

Persons = st.number_input('persons:', min_value=1, max_value=3, value=1)

st.text("small 1 med 2 big = 3")

Lug_boot = st.number_input('lug_boot:', min_value=1, max_value=3, value=1)

Safety = st.radio('safety:', ('med', 'high', 'low'))
if st.button('submit_car_Infos'):
  cal_eval = predict(Buying, Maint, Doors, Persons, Lug_boot, Safety)
  st.success(f'The Evalution of car : {cal_eval[0]}')
