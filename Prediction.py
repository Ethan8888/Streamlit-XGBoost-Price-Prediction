import numpy as np 
import pandas as pd 
import pickle 
import streamlit as st
import time

st.set_page_config(
   page_title=" Prediction",
   page_icon="🦈",
   layout="wide",
   initial_sidebar_state="expanded",
)


# THE MAIN STARTS FROM HERE ...........

# Reading the Pickle file

# Load the trained machine learning model
with open('prediction.pkl', 'rb') as f:
    reg = pickle.load(f)

def predict(Open,Close,High,Low):
    input_data = np.array([[Open,Close,High,Low]])
    return reg.predict(input_data)[0]


def main():

    # Tab Title and Icon
    #code snippet for the sidebar
    code_snippet = """
        R-squared (R2): 
        """
    st.sidebar.code(code_snippet, language='python')

    # Title of The WebPage
    st.title('Machine Learning Prediction🧊')
    st.warning("🧊")

    #Taking Inputs From The User....
    sub = box.form_submit_button('Predict')
    Open = box.number_input("Enter:",max_value=30.6, min_value=4.2, step=2.0)
    Close = box.number_input('Enter:',max_value=20.6, min_value=4.0, step=2.0)
    High = box.number_input('Enter:',max_value=26.1, min_value=4.1, step=2.0)
    Low = box.number_input('Enter:',max_value=69, min_value=11, step=5)
    result = predict(Open,Close,High,Low)
    sub = box.form_submit_button('Predict')

    if sub:
        with st.spinner(f'Processing Wait a sec...{name} 🧊'):
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

        Value -->  {result} 🧊"""
        
        st.code(code_snippet, language='python')


        


    footer()
if __name__ == '__main__':
    main()
