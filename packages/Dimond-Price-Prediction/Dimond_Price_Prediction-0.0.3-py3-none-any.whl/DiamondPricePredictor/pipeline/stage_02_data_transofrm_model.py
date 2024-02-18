from DiamondPricePredictor.config.configuration import ConfigurationManager
from DiamondPricePredictor.components.data_model_train import PrepareBaseModel
from DiamondPricePredictor.logger import logging


STAGE_NAME = "Data Transformation and model stage"

class ModelCreationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.initiate_model_trainer()




if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelCreationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e