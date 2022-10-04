import pandas as pd
import numpy as np
import altair as alt
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import itertools
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import shap
import pickle
import streamlit as st 
st.write("Hello App!")