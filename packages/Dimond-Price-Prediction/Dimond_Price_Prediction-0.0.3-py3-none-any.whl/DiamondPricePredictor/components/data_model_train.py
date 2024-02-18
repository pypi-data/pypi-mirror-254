import os
import sys
import json
import urllib.request as request
import zipfile
from pathlib import Path
from DiamondPricePredictor.logger import logging
from DiamondPricePredictor.utils.MLUtils import PrepareData,SplitDataSet,evaluate_model,DataTransformation,best_score
from DiamondPricePredictor.exception import CustomException
from DiamondPricePredictor.entity.config_entity import PrepareBaseModelConfig
from DiamondPricePredictor.constants import *
from DiamondPricePredictor.utils.common import read_yaml, create_directories,load_json,save_loaded_json,save_json,save_obj,get_size






class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    
    def initiate_model_trainer(self):
        try:            
            path_of_files=self.config.data_dir
            Target_Column=self.config.target_column
            Drop_Columns=self.config.drop_column
            split_ratio=self.config.test_train_split
            random_state=self.config.random_state
            model_param_file=self.config.model_param_file
            base_model_path=self.config.base_model_path
            root_dir=self.config.root_dir


            feature_data,Target_data=PrepareData(Path(path_of_files),Target_Column,Drop_Columns)
            
            
            x_train,y_train,x_test,y_test=SplitDataSet(feature_data,Target_data,split_ratio,random_state)
            
    
            
            x_train_t,y_train_t,x_test_t,y_test_t=DataTransformation(x_train,y_train,x_test,y_test)

            model_and_parameters=load_json(model_param_file)
            
            json_string = json.dumps(model_and_parameters)
            data_dict = json.loads(json_string)
            params = data_dict.get("params", {})
            models=data_dict.get("models", {})



            
            model_report:dict=evaluate_model(x_train=x_train_t,y_train=y_train_t,x_test=x_test_t,y_test=y_test_t,models=models,param=params)

            
            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException('no best model found')
            

            best_model_dict={'best_model':best_model}

            save_json(base_model_path,best_model_dict)

            
            #save_obj(
            #    file_path=base_model_path,
            #    obj=best_model
            #)
            
            r2_score_best_model=best_score(root_dir,best_model,x_train_t,y_train_t)

            

            return r2_score_best_model
        except Exception as e:
           raise CustomException(e,sys)
    
