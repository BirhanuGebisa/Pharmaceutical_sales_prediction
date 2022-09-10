import sys
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import testing
import numpy as np
import pandas as pd
import streamlit as st
sys.path.append('../src')
import warnings
warnings.filterwarnings('ignore')
from visualize_data import visualize
def compare_test_train(train_data, test_data, feature, title):
    fig, ax = plt.subplots(1, 2, sharex=True, figsize=(12, 4))
    ax[0].set_title("Train " + title)
    sns.countplot(x=feature, data=train_data, ax=ax[0])
    ax[1].set_title("Test " + title)
    sns.countplot(x=feature, data=test_data, ax=ax[1])
    fig.subplots_adjust(wspace=0.3)

def trainingDataLoad():
    df = pd.read_csv("../data/train_store.csv")
    return df


def testingDataLoad():
    df = pd.read_csv("../data/test_store.csv")
    return df


def transform_date(df):
     
    df['Month'] = pd.DatetimeIndex(df['Date']).month 
    return df


def app():

    promo = ["Not participating", "Participating"]
    train_data = trainingDataLoad()
    test_data = testingDataLoad()

    st.title('Pharmaceutical Sales Prediction Across Multiple Stores')
    
    st.header('Table Description')
    st.markdown(
    '''
       The Pharmaceutical Supplemental Information About the Stores
    ''')
    df = transform_date(train_data.copy())
    #sns.histplot(data = df, x ="Month", y = "Sales",
    #           hue = 'Promo',
    #          sharex=False)