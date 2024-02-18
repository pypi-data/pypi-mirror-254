# ./my_hello_world_lib/module_2.py
from src.z_test_poetry.module_1 import add1 
import logging

logger = logging.getLogger(__name__)

def say_hello():
    logger.info('hello world!')

add1(2, 2)