import os
import sys
import pandas as pd
from source.exception import CustomException
from source.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from source.components.data_transformation import Data_transformation, Data_transformation_Config
from source.components.data_model_trainer import ModelTrainerConfig, ModelTrainer
#Define dataIngestion config
@dataclass
class DataIngestion_Config:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')
# Define Data ingestion
    # Generate config
    # read data 
    # make new direction to train_data_path
    # write to csv
    # Train_test_split
    # return
class DataIngestion:
    def __init__(self):
        self.DataIngestion_Config = DataIngestion_Config()

    def Ingest(self):
        try:
            df = pd.read_csv('Notebook\data\stud.csv')

            logging.info('Read Data completed')
            os.makedirs(os.path.dirname(self.DataIngestion_Config.train_data_path),exist_ok=True)
            df.to_csv(self.DataIngestion_Config.raw_data_path,index=False,header=True)

            logging.info('Train_test_split generated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.DataIngestion_Config.train_data_path,index=False,header=True)
            test_set.to_csv(self.DataIngestion_Config.test_data_path,index=False,header=True)

            logging.info('Ingestion completed')
            return(
                self.DataIngestion_Config.train_data_path,
                self.DataIngestion_Config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
if __name__=='__main__':
    ingest = DataIngestion()
    train_data,test_data = ingest.Ingest()

    data_transform=Data_transformation()
    train_arr,test_arr,_ = data_transform.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    model_trainer.Initiate_ModelTrainer(train_arr,test_arr)