import streamlit as st
from pickle import load

st.markdown('<style>body{background-color: #ccffe5;}</style>',unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>Churn prediction Application</h1>", unsafe_allow_html=True)



def load_sidebar():
    st.sidebar.subheader("Churn prediction")
    st.sidebar.success("Customer churn, also known as customer attrition, occurs when customers stop doing business with a company.The companies are interested in identifying segments of these customers because the price for acquiring a new customer is usually higher than retaining the old one.")
    st.sidebar.warning("Made with :heart: :sunglasses:")

classifier = load(open('pickle/logistc5_model.pkl', 'rb'))

@st.cache()
def prediction(Dependents,OnlineBackup,TechSupport,StreamingTV,StreamingMovies,InternetService_Fiber_optic,InternetService_No,Contract_One_year,Contract_Two_year,PaymentMethod_Electronic_check):
    if Dependents=='Yes':
        Dependents = 1
    else:
        Dependents = 0
    if OnlineBackup=='Yes':
        OnlineBackup=1
    else:
        OnlineBackup=0
    if TechSupport=='Yes':
        TechSupport=1
    else:
        TechSupport=0
    if StreamingTV=='Yes':
        StreamingTV=1
    else:
        StreamingTV=0
    if StreamingMovies=='Yes':
        StreamingMovies=1
    else:
        StreamingMovies=0
    if InternetService_Fiber_optic=='Yes':
        InternetService_Fiber_optic=1.0
    else:
        InternetService_Fiber_optic=0.0
    if InternetService_No=='Yes':
        InternetService_No=1.0
    else:
        InternetService_No=0.0
    if Contract_One_year=='Yes':
        Contract_One_year=1.0
    else:
        Contract_One_year=0.0
    if Contract_Two_year=='Yes':
        Contract_Two_year=1.0
    else:
        Contract_Two_year=0.0
    if PaymentMethod_Electronic_check=='Yes':
        PaymentMethod_Electronic_check=1.0
    else:
        PaymentMethod_Electronic_check=0.0
    prediction=classifier.predict([[Dependents,OnlineBackup,TechSupport,StreamingTV,StreamingMovies,InternetService_Fiber_optic,InternetService_No,Contract_One_year,Contract_Two_year,PaymentMethod_Electronic_check]])
    if prediction==0:
        pred='No Churn'
    elif prediction==1:
        pred='Churn Yes'
    else:
        pred=None
    return pred

def main():

    load_sidebar()



    Dependents=st.selectbox('Dependents',('Yes','No'))
    OnlineBackup=st.selectbox('OnlineBackup',('Yes','No'))
    TechSupport=st.selectbox('TechSupport',('Yes','No'))
    StreamingTV=st.selectbox('StreamingTV',('Yes','No'))
    StreamingMovies=st.selectbox('StreamingMovies',('Yes','No'))
    InternetService_Fiber_optic=st.selectbox('InternetService_Fiber_optic',('Yes','No'))
    InternetService_No=st.selectbox('InternetService_No',('Yes','No'))
    Contract_One_year=st.selectbox('Contract_One_year',('Yes','No'))
    Contract_Two_year=st.selectbox('Contract_Two_year',('Yes','No'))
    PaymentMethod_Electronic_check=st.selectbox('PaymentMethod_Electronic_check',('Yes','No'))
    if st.button('predict'):
        churn_predict=prediction(Dependents,OnlineBackup,TechSupport,StreamingTV,StreamingMovies,InternetService_Fiber_optic,InternetService_No,Contract_One_year,Contract_Two_year,PaymentMethod_Electronic_check)
        st.info(churn_predict)

if __name__=='__main__':
    main()
