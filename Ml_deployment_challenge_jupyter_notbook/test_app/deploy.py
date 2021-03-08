import streamlit as st
from pickle import load

classifier=load(open('pickle/svm_rbf.pkl','rb'))

st.markdown("<h1 style='text-align: center; color: black;'>Deployment Challenge</h1>", unsafe_allow_html=True)

def main():

    col1=st.number_input('Enter a number1')
    col2=st.number_input('Enter a number2')
    prediction=classifier.predict([[col1,col2]])
    if st.button('Predict'):
        if(prediction==1):
            st.info('Yes :sunglasses:')
        elif(prediction==0):
            st.sucess('No :sad:')
        else:
            st.info(None)

if(__name__=='__main__'):

    main()
