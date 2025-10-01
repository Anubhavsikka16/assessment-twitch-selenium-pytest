import logging
import time
import os

class Logger:

    def __init__(self, logger, file_level=logging.INFO, console_level=logging.INFO):
        
        #Deleting old logs files
        logs_dir = "logs"
        os.makedirs(logs_dir, exist_ok=True)
        for log_file in os.listdir(logs_dir):
            log_path = os.path.join(logs_dir, log_file)
        try:
            if os.path.isfile(log_path):
                os.remove(log_path)
        except Exception as e:
            print(f"❌ Could not delete: {e}")
        #Setting up new log file    
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(file_level)
        fmt=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        current_time=time.strftime("%Y-%m-%d %H:%M:%S")
        self.LogFileName='/Users/anubhavsikka/Documents/Assessment-twitch-selenium-framework/assessment-twitch-selenium-pytest/logs/log'+ current_time +'.log'
        sh=logging.FileHandler(self.LogFileName)
        sh.setLevel(file_level)
        sh.setFormatter(fmt)
        self.logger.addHandler(sh)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(fmt)
        self.logger.addHandler(console_handler)