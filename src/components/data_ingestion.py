#Read the data from a specific source , either from mongodb or cloud 

import os 
import sys 
#sys.path.append("./src")
#from . import main
from src_.exception import CustomException
from src_.logge import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#decorator i can directyl define class variable withour init 
@dataclass
#where do u want to save ur output fiile . input giving to ur ingestion component so it will know where to save ur file 
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact','train.csv')
    test_data_path: str = os.path.join('artifact','test.csv')
    raw_data_path: str = os.path.join('artifact','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info('enterred the data ingestion method or component')
        try:
            df = pd.read_csv('fl\src\Ticket.csv',encoding ='utf-8')
            logging.info('read the dataset as dataframe using pandas')
            #create directory recursively , as we know the train,test ,raw path , create a folder artifact
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #if folderr is already there just add in that no need to delete and create it 
            df.to_csv(self.ingestion_config.raw_data_path,header=True,index =False)

            logging.info('train test split initated')
            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,header=True,index =False)
            test_set.to_csv(self.ingestion_config.test_data_path,header=True,index =False)
            logging.info('data ingestion is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)

           
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()







