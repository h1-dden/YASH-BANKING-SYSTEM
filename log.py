import logging

logging.basicConfig(
    filename='banking_system.log',  # Log file name
    level=logging.DEBUG,              # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)