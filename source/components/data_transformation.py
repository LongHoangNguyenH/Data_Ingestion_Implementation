import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from source.exception import CustomException
from source.logger import logging
import os
import numpy as np
from source.utils import save_object
#Fill missing value
#Scale data
#encode data
@dataclass
class Data_transformation_Config:
    preprocessor_file_path = os.path.join('artifacts','processor.pkl')

class Data_transformation:
    def __init__(self):
        self.data_transformation_config = Data_transformation_Config()
    
    def get_transformation_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            cate_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False)),
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cate_pipeline,categorical_columns)

                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        #read file
        #take input_train, output_train, input_test, output_test
        # fit train_Data
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            
            target_column = 'math_score'
            numerical_columns = ['writing_score','reading_score']

            input_data_train = train_df.drop(columns= [target_column],axis=1)
            output_data_train = train_df[target_column]

            input_data_test = test_df.drop(columns= [target_column],axis=1)
            output_data_test = test_df[target_column]

            logging.info(f'Applying preprocessing object on training dataframe and testing dataframe')

            preprocessing_obj = self.get_transformation_object()
            input_feature_train_arr = preprocessing_obj.fit_transform(input_data_train)
            input_feature_test_arr = preprocessing_obj.transform(input_data_test)

            train_arr = np.c_[input_feature_train_arr, np.array(output_data_train)]
            test_arr = np.c_[input_feature_test_arr,np.array(output_data_test)]

            logging.info(f'Saved processing object.')
            
            save_object(
                file_path = self.data_transformation_config.preprocessor_file_path,
                object = preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
