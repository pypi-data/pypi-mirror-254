import os
import sys
from dataclasses import dataclass
from pathlib import Path
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
# Modelling
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
#import warnings
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from DiamondPricePredictor.logger import logging
from DiamondPricePredictor.exception import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any,List
import base64
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


@ensure_annotations
def PrepareData(path_of_files: Path,Target_Column:str,Drop_Columns:List):
    try:
        print(path_of_files)
        df=pd.read_csv(path_of_files)
        X = df.drop(columns=[Target_Column],axis=1)
       
        X.drop(columns=Drop_Columns,inplace=True)
        
        y=df[[Target_Column]]
        num_features = X.select_dtypes(exclude="object").columns
        cat_features = X.select_dtypes(include="object").columns
        return X,y
    except BoxValueError:
        raise ValueError("file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def SplitDataSet(feature_data:pd.DataFrame,Target_data:pd.DataFrame,split_ratio:float,random_state:int):
    
    
    try:
        split_ratio=float(split_ratio)
        x_train,x_test,y_train,y_test = train_test_split(feature_data,Target_data,test_size=split_ratio,random_state=random_state)
        logging.info(f"The shape of X_train {x_train.shape}")
        logging.info(f"The head of X_test {x_train.head}")
        logging.info(f"The shape of X_test {x_test.shape}")
        logging.info(f"The head of X_train {x_test.head}")
        logging.info(f"The shape of y_train {y_train.shape}")
        logging.info(f"The head of y_train {y_train.head}")
        logging.info(f"The shape of y_train {y_test.shape}")
        logging.info(f"The head of y_test {y_test.head}")
        return x_train,y_train,x_test,y_test
    except BoxValueError:
        raise ValueError("file is empty")
    except Exception as e:
        raise e
    

def evaluate_model(x_train,y_train,x_test,y_test,models,param):
    try:
        report={}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param_grid=param[list(models.keys())[i]]
            print(model)
            print(param_grid)
            model_name=model
            logging.info(f"the Current model select {param_grid} for the model {model}")
            model = eval(model)
            gs=GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
            
            gs.fit(x_train,y_train)
            
            model.set_params(**gs.best_params_)
            logging.info(f"The Best Working Model {model}")
            model.fit(x_train,y_train)
            joblib.dump(model, 'artifacts/prepare_base_model/'+model_name[:-2]+'.joblib')
            y_train_pred=model.predict(x_train)
            y_test_pred=model.predict(x_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

        
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e:
        raise e

@ensure_annotations   
def DataTransformation(x_train:pd.DataFrame,y_train:pd.DataFrame,x_test:pd.DataFrame,y_test:pd.DataFrame):
    
    
    try:
        num_features = x_train.select_dtypes(exclude="object").columns
        cat_features = x_train.select_dtypes(include="object").columns
    
        #Imputer=SimpleImputer(strategy="median")

        def transform_data_train(data, num_features, cat_features):
            # Check for null values in input data
            if data.isnull().any().any():
                raise ValueError("Input data contains null values. Please handle null values before transformation.")

            # Print statistics of input data before transformations
           

            # Create transformers
            numeric_transformer = StandardScaler()
            label_encoding = LabelEncoder()

            # Apply transformations to numerical features
            num_transformed = numeric_transformer.fit_transform(data[num_features].astype('float'))
           
            # Apply transformations to categorical features
            cat_transformed = pd.DataFrame()
            for col in cat_features:
                cat_transformed[col] = label_encoding.fit_transform(data[col].astype('str'))
         

            # Concatenate the transformed numerical and categorical features
            transformed_data = pd.concat([pd.DataFrame(num_transformed, columns=num_features), cat_transformed], axis=1)

            return transformed_data
        
        def transform_data_test(data, num_features, cat_features):
            # Create transformers
            numeric_transformer_test = StandardScaler()
            label_encoding_test = LabelEncoder()

            # Apply transformations to numerical features
            num_transformed = numeric_transformer_test.fit_transform(data[num_features].astype('float'))

            # Apply transformations to categorical features column by column
            cat_transformed = pd.DataFrame()
            for col in cat_features:
                cat_transformed[col] = label_encoding_test.fit_transform(data[col].astype('str'))
         
            # Concatenate the transformed numerical and categorical features
            transformed_data_test = pd.concat([pd.DataFrame(num_transformed, columns=num_features), cat_transformed], axis=1)

            return transformed_data_test
        
        x_train_t=transform_data_train(x_train,num_features,cat_features)
       
        x_test_t=transform_data_test(x_test,num_features,cat_features)
    

        
       
        def transform_lebal_data(data):
            log_price_data = np.log1p(data)
            normalized_log_price_data = (log_price_data - log_price_data.min()) / (log_price_data.max() - log_price_data.min())
            return normalized_log_price_data
        

        y_train_t = transform_lebal_data(y_train)
        y_test_t = transform_lebal_data(y_test)
        

        logging.info(f"The shape of Transformed X_train {x_train_t.shape}")
        logging.info(f"The head of Transformed X_test {x_train_t.head}")
        logging.info(f"The shape of Transformed  Transformed X_test {x_test_t.shape}")
        logging.info(f"The head of Transformed X_train {x_test_t.head}")
        logging.info(f"The shape of Transformed y_train {y_train_t.shape}")
        logging.info(f"The head of Transformed  y_train {y_train_t.head}")
        logging.info(f"The shape of Transformed y_train {y_test_t.shape}")
        logging.info(f"The head of Transformed y_test {y_test_t.head}")

        return  x_train_t,y_train_t,x_test_t,y_test_t
    except BoxValueError:
        raise ValueError("file is empty")
    except Exception as e:
        raise CustomException(e,sys)
    



def best_score(path_of_files,best_model,x_test_t,y_test_t):
    try:

        path_of_model = os.path.join(path_of_files, best_model[:-2] + '.joblib')
        model = joblib.load(path_of_model)

   
        predictions = model.predict(x_test_t)
        r2_score_best_model=r2_score(y_test_t,predictions)
        return r2_score_best_model 
    

    except BoxValueError:
        raise ValueError("file is empty")
    except Exception as e:
        raise e
    

    