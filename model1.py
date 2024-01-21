import pickle
import streamlit as st

model="model.sav"
model1=pickle.load(open(model,'rb'))

st.title("Predict your Credit Score")

col1, col2, col3, col4, col5, col6=st.columns(6)
with col1:
    ID=st.text_input("Enter your user_ID ")

with col2:
    Annual_Income=st.text_input("Enter your Annual income")

with col3:
    N_Bank_acc=st.text_input("Enter number of Bank account ")

with col4:
    N_credit_card=st.text_input("Enter Number of credit card")

with col5:
    Interest=st.text_input("Enter your interest Rate ")

with col6:
    num_loan=st.text_input("Enter your number of loan")

with col1:
    type_loan=st.text_input("Number of loan \n you have")

with col2:
    Num_of_Delayed_Payment=st.text_input("Enter your No of Delayed Payment")

with col3:
    Changed_Credit_Limit=st.text_input("Enter Changed Credit Limit")

with col4:
    Num_Credit_Inquiries=st.text_input("Enter your No Credit Inquiries")

with col5:
    credit_mix=st.text_input("Enter your Credit mix")

with col6:
    Outstanding_Debt=st.text_input("Enter your Outstanding Debt")

with col1:
    Credit_Utilization_Ratio=st.text_input("Enter your Credit Utilization Ratio")

with col2:
    Payment_of_Min_Amount=st.text_input("Enter your Payment Min Amount")

with col3:
    Total_EMI_per_month=st.text_input("Enter your Total EMI per month")

with col4:
    Amount_invested_monthly=st.text_input("Enter your Amount invested monthly")

with col5:
    Payment_Behaviour=st.text_input("Enter your Payment Behaviour")

with col6:
    Monthly_Balance=st.text_input("Enter your Monthly Balance")

credit_score=""
if st.button("Result"):
    pred=model1.predict(
        [[ID,Annual_Income,N_Bank_acc,N_credit_card,Interest,num_loan,type_loan,Num_of_Delayed_Payment,Changed_Credit_Limit,Num_Credit_Inquiries,credit_mix,Outstanding_Debt,Credit_Utilization_Ratio,Payment_of_Min_Amount,Total_EMI_per_month,Amount_invested_monthly,Payment_Behaviour,Monthly_Balance]])
    
    if pred[0]==0:
        credit_score="your credit score is good"
    elif pred[1]==1:
        credit_score="your credit score is standard"
    else:
        credit_score="your credit score is low"
st.success(credit_score)
