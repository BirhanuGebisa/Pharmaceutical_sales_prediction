
import io
import sys

import dvc.api as dvc
sys.path.append('../')
import pandas as pd
#from src.rotating_logs import get_rotating_log


#logger = get_rotating_log(filename='data_loader.log', logger_name='DataLoaderLogger')

class File_handler:
    """This class is a wrapper for getting DVC versioned datasets and normal csvs from file"""
   # def dvc_get_data(path: str, version: str, repo: str = '../') -> pd.DataFrame:
    """Fetch DVC versioned files. You need to know the path to the file, starting from the root of the repo.
        """
    #read file csv
    def read_file(self, path, low_memory=True):
            #csv file
        try:
            df = pd.read_csv(path)
            #logger.info(f"Pandas: CSV read from: {path}")
            return df
        except FileNotFoundError:
                print(("File error"))
             #logger.exception(f"Pandas failed to read the csv at: {path}")
    #read data dvc
    def read_dvc(self, path, repo, rev, low_memory=True):
        try:
            file =dvc.read(path, repo=repo, rev=rev)
            #logger.info(f"Pandas: CSV read from: {path}")
            df=pd.read_csv(io.String(file), low_memory=low_memory)
            return df
        except Exception as e:
            print("Error occur", e)
            #logger.exception(f"Pandas failed to read the csv at: {path}")
              