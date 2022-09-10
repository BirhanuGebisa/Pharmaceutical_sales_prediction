from pprint import pprint
import dvc.api

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_squared_error, r2_score

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
import os, sys

import io 

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
sys.path.insert(0, path_parent+'/src')


path="data/train_store.csv"
repo="/"
version="vts1"

data_url = dvc.api.read(
    path=path,
    repo=repo,
    rev=version,
)

mlflow.set_experiment('random_forest')

def main():
    # prepare example dataset
    data = pd.read_csv(io.StringIO(data_url), sep=",")
    print(data.columns)
    
    #log data params
    # mlflow.log_param('data_url', data_url)
    mlflow.log_param('data_version', version)
    mlflow.log_param('input_rows', data.shape[0])
    mlflow.log_param('input_colums', data.shape[1])
    
  
    
    data.set_index('Year', inplace=True)

    data.drop(['StateHoliday'], axis=1, inplace=True)

    data = data[data['Open'] == 1]
    data = data[data['Sales'] > 0.0]

    X = data.drop('Sales', axis=1)
    y = data['Sales']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123)


    lr = RandomForestRegressor()
    
    lr.fit(x_train, y_train)
    
    score = lr.score(X_test, y_test)
    
    print("Score: %s" % score)
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(lr, "model")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)


if __name__ == "__main__":
    main()