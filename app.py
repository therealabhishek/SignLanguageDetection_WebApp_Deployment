from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys
from signLanguage.pipeline.training_pipeline import Trainpipeline


if __name__ == '__main__':
    obj = Trainpipeline()
    obj.run_pipeline()