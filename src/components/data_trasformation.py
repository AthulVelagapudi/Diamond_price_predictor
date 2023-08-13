import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')

            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z', 'price']
            categorical_cols = ['cut', 'color', 'clarity']

            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D','E','F','G','H','I','J']
            clarity_categories = ['I1', 'SI2', 'SI1','VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            
            logging.info('Data transformation Initiated')
            num_pipeline = Pipeline(steps = [
                ('imputer',SimpleImputer(strategy='median')),
                ('scalar', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                    steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                    ('scalar', StandardScaler())
                ]
            )

            preprocessing = ColumnTransformer([
                    ('num_pipeline', num_pipeline, numerical_cols),
                    ('cat_pipeline', cat_pipeline, categorical_cols)
                ]
            )
            logging.info('Preprocessing completed')
            return preprocessing
        
        except Exception as e:
            logging.info('Error in Data Transformation')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            pass
        except Exception as e:
            logging.info("Exception occured in initiate_data_transformation")
            raise CustomException(e,sys)
        
