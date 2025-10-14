import sys
import logging
import os
from pathlib import Path
from datetime import datetime

# -----------------------------
# Logging Setup
# -----------------------------
base_log_folder = Path(os.path.join(os.getcwd()), "logs")
today_folder = datetime.now().strftime("%Y_%m_%d")
log_folder = os.path.join(base_log_folder, today_folder)
os.makedirs(log_folder, exist_ok=True)

log_file_name = f"{datetime.now().strftime('%I_%M%p')}.log"
log_file_path = os.path.join(log_folder, log_file_name)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s:%(funcName)s:%(lineno)d] - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

# -----------------------------
# Custom Exception
# -----------------------------
def error_message_details(error, error_details: sys):
    _, _, tb = error_details.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name:[{file_name}] "
        f"line number:[{tb.tb_lineno}] "
        f"Error Message:[{str(error)}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_details: sys = sys):
        super().__init__(error)
        self.error_message = error_message_details(error, error_details)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    print(log_file_path)