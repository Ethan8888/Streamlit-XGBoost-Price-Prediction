import numpy as np 
import pandas as pd 
import pickle 
import streamlit as st
import time
from PIL import Image
import streamlit as st
import numpy as np 
import pandas as pd 
import time
import plotly.express as px 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import shap
import xgboost
from xgboost import XGBRegressor
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.set_page_config(
   page_title=" Prediction",
   page_icon="🦈",
   layout="wide",
   initial_sidebar_state="expanded",
)


# THE MAIN STARTS FROM HERE ...........

# Reading the Pickle file

# Load the trained machine learning model
with open('Prediction.pkl', 'rb') as f:
    XGBRegressor = pickle.load(f)

def predict(Open,Close,High,Low):
    input_data = np.array([[Open,Close,High,Low]])
    return reg.predict(input_data)[0]


def main():

    # Tab Title and Icon
    #code snippet for the sidebar
    code_snippet = """
        R-squared (R2): 0.78
        """
    st.sidebar.code(code_snippet, language='python')

    # Title of The WebPage
    st.title('Machine Learning Prediction🧊')
    st.warning("🧊")

    #Taking Inputs From The User....
    sub = box.form_submit_button('Predict')
    Open = box.number_input("Enter:",max_value=4201.4, min_value=2211.8, step=1.0)
    Close = box.number_input('Enter:',max_value=4212.9, min_value=2212.7, step=1.0)
    High = box.number_input('Enter:',max_value=4244.7, min_value=2223.2, step=1.0)
    Low = box.number_input('Enter:',max_value=4173.0, min_value=2203.4, step=1.0)
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
