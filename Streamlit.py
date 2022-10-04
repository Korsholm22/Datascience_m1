import pandas as pd
import pickle 
from xgboost import XGBRegressor 
from sklearn.preprocessing import StandardScaler
import shap 

import numpy as np
import itertools 
import streamlit as st 

st.title("Hello")
st.write("Hello App!")

tabs1, tabs2 = (["Tab1, tab2"])

with tabs1:
    st.header("Hello")

with tabs2:
    st.header("Hello2")
