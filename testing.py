from src.logger import get_logger 
from src.custom_exception import CustomException
import sys 

logger = get_logger(__name__)

def divide_no(a,b):
    try:
        result = a/b
        logger.info('divide 2 nos.')
        return result 
    except Exception as e:
        logger.error("Error Occured")
        raise CustomException("Custom Error zeros",sys)
    
if __name__ == "__main__":
    try:
        logger.info("Starting ")
        divide_no(10,0)

    except CustomException as ce:
        logger.error(str(ce))