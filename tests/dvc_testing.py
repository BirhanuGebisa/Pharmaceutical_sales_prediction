from tkinter.filedialog import test
import unittest
import mlflow
import pandas as pd
import logging, os, sys
sys.path.append('../')
import warnings
warnings.filterwarnings('ignore')
from src.file_handler import FileHandler
File_handler=FileHandler()

logging.basicConfig(filename="logs/log_file.log", filemode='a',
                    encoding='utf-8', level=logging.DEBUG)
#train
data_path = 'data/train.csv'
version = 'v3'
repo = '../'

store_df = File_handler.dvc_get_data(data_path, version, repo)

# test
data_path = 'data/test.csv'
version = 'v5'

train_df = File_handler.dvc_get_data(data_path, version, repo)

# store
data_path = 'data/store.csv'
version = 'vs'

test_df = File_handler.dvc_get_data(data_path, version, repo)

class TestGetInformations(unittest.TestCase):
    def test_load_store(self):
       self.assertIsInstance(store_df,pd.DataFrame)
       
    def test_load_train(self):
       self.assertIsInstance(train_df,pd.DataFrame)
       
    def test_load_test(self):
       self.assertIsInstance(test_df,pd.DataFrame)
        
        
if __name__ == "__main__":
    unittest.main()