import numpy as np 
import pandas as pd 
import pickle 
import streamlit as st

st.set_page_config(
   page_title=" Prediction",
   layout="wide",
   initial_sidebar_state="expanded")


# THE MAIN STARTS FROM HERE ...........

# Reading the Pickle file

# Load the trained machine learning model
with open('Prediction.pkl', 'rb') as f:
    xgb = pickle.load

def predict(Open,Close,High,Low):
    input_data = np.array([[Open,Close,High,Low]])
    return xgb.predict(input_data)[0]


def main():

    # Tab Title and Icon
    #code snippet for the sidebar
    code_snippet = """
        R-squared (R2): 0.78
        """
    st.sidebar.code(code_snippet, language='python')

    # Title of The WebPage
    st.title('Machine Learning Prediction')
    st.warning("warning")

    #Taking Inputs From The User....
    car = st.form('my_car') 
    sub = car.form_submit_button('Predict')
    Open = car.number_input("Enter:",max_value=4201.4, min_value=2211.8, step=1.0)
    Close = car.number_input('Enter:',max_value=4212.9, min_value=2212.7, step=1.0)
    High = car.number_input('Enter:',max_value=4244.7, min_value=2223.2, step=1.0)
    Low = car.number_input('Enter:',max_value=4173.0, min_value=2203.4, step=1.0)
    result = predict(Open,Close,High,Low)
    sub = car.form_submit_button('Predict')

    if sub:
        with st.spinner(f'Processing Wait a sec...{name} '):
            time.sleep(10)


        st.divider()
        
        #st.error(f'Good to See You {name}')
        
        st.subheader("Prediction Report")
        
        code_snippet = f"""
        Good To See You {name}
        Open:   {Open}
        Close :   {Close}
        High:   {High}
        Low:   {Low}
        
        Result: 

        Value -->  {result} """
        
        st.code(code_snippet, language='python')


        


    footer()
if __name__ == '__main__':
    main()
