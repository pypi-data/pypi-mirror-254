import os
from pathlib import Path
from DiamondPricePredictor.exception import CustomException
from DiamondPricePredictor.constants import *
from DiamondPricePredictor.utils.common import read_yaml, create_directories,save_loaded_json,load_json
from DiamondPricePredictor.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig



    
class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        model_params_filepath = MODEL_PARAM_FILE_PATH,
        ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.model_param=load_json(model_params_filepath)
        

        
        create_directories([self.config.artifacts_root,self.config.artifacts_root+'/prepare_base_model'])

        path=self.config.artifacts_root+'/prepare_base_model'+'/model_params.json'
    
        save_loaded_json(path,self.model_param)


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file_train=config.local_data_file_train,
            local_data_file_test=config.local_data_file_test,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            data_dir=Path(config.data_dir),
            model_param_file=Path(config.model_param_file),
            target_column=self.params.TARGET_COLUMN,
            drop_column=self.params.DROP_COLUMN,
            test_train_split=self.params.TEST_TRAIN_SPLIT,
            random_state=self.params.RANDOM_STATE,
        )

        return prepare_base_model_config
