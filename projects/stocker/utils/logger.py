import logging
import os

def setup_logger(name):
    """Sets up a logger with console and file output."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # File handler
    if not os.path.exists('logs'):
        os.makedirs('logs')
    fh = logging.FileHandler(f'logs/{name}.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    return logger
