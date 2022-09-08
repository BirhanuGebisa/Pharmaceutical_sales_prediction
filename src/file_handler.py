import json
import mlflow
import pickle
from fileinput import filename
import io
import dvc.api
import pandas as pd
from get_log import get_logger
from time import gmtime, strftime

logger = get_logger("FileHandler")

#filehandler class
class FileHandler():

  def __init__(self):
    pass

  #dvc Fetch DVC versioned files from the root of the repo.
  @staticmethod
  def dvc_get_data(path: str, version: str, repo: str = '../'):
    try:
        content = dvc.api.read(path=path,
                                    repo=repo,
                                    rev=version)
        df = pd.read_csv(io.StringIO(content), sep=",")
        logger.info(f"DVC: CSV file read with path: {path} | version: {version} | from: {repo}")
        return df
    except:
        logger.exception("DVC data getter raised an exception")
  #save the csv file with index
  def save_csv(self, df, csv_path, index=False):
    try:
      df.to_csv(csv_path, index=index)
      logger.info("The Dataset file saved as csv")

    except Exception:
      logger.exception("The file is not saved: ERROR")
  #read csv file 
  def read_csv(self, csv_path):
    try:
      df = pd.read_csv(csv_path)
      my_logger.debug("Read the Dataset as csv")
      return df
    except FileNotFoundError:
      my_logger.exception("The Dataset file is not found")
  #save the model
  def save_model(self, model, model_name):
    try:
      file_name = model_name+"_model "+ strftime("%Y-%m-%d %H-%M-%S", gmtime())
      with open(f'../models/{file_name}.pkl', 'wb') as my_model:
        pickle.dump(model, my_model) 

      mlflow.log_artifact(f"../models/{file_name}.pkl")
      my_logger.info("Model is successfully saved !")

    except Exception:
      my_logger.exception("process of saving model failed")

    
                