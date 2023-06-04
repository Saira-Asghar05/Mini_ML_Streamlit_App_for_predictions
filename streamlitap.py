
import streamlit as st
import joblib
#Create a web form for user input
st.sidebar.header('Enter Diamond Characteristics')
carat = st.sidebar.slider('Carat', 0.2, 5.0, 1.0, 0.1)
cut = st.sidebar.selectbox('Cut', ['0', '1', '2', '3', '4'])
color = st.sidebar.selectbox ('Color', ['0', '1', '2', '3', '4','5', '6'])
clarity = st.sidebar.selectbox('Clarity', ['0', '1', '2', '4', '5', '6', '7'])
#load the model
model = joblib.load("model.pkl")
#Make a prediction based on user input
prediction = model.predict([[carat, cut, color, clarity]])
#Display the prediction to the user
st.write('')
st.write('')
st.subheader('Predicted Diamond Price')
st.write(f'${prediction [0]:,.2f}')
#import streamlit as st
#st.write("Hello")