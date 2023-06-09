import os
import sys
import pandas as pd
from dataclasses import dataclass

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from source.exception import CustomException
from source.logger import logging

from source.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','trained_model.pkl')

class ModelTrainer:
    def __init__(self):
        self.trained_model_config = ModelTrainerConfig()

    def initiate_model_Trainer(self,train_):
