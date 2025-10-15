import pandas as pd
from src import CustomException, logging

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            df = pd.read_csv(self.config.data_dir).drop(columns="customerID", errors="ignore")
            schema = self.config.all_schemas  # dict from YAML

            # --- 1. Validate column names ---
            dataset_cols = set(df.columns)
            schema_cols = set(schema.keys())

            missing_cols = schema_cols - dataset_cols
            extra_cols = dataset_cols - schema_cols

            if missing_cols:
                logging.error(f"Missing columns in data: {missing_cols}")
            if extra_cols:
                logging.warning(f"Extra columns not in schema: {extra_cols}")

            # --- 2. Validate data types ---
            dtype_mismatch = {}
            for col, expected_dtype in schema.items():
                if col in df.columns:
                    actual_dtype = str(df[col].dtype)
                    if actual_dtype != expected_dtype:
                        dtype_mismatch[col] = {'expected': expected_dtype, 'found': actual_dtype}

            validation_status = not (missing_cols or extra_cols or dtype_mismatch)

            # --- 3. Write status file ---
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}\n")
                if missing_cols:
                    f.write(f"Missing columns: {missing_cols}\n")
                if extra_cols:
                    f.write(f"Extra columns: {extra_cols}")    
                
                if dtype_mismatch:
                    f.write(f"Dtype mismatches: {dtype_mismatch}\n")

            logging.info(f"Validation complete. Status: {validation_status}")
            return validation_status

        except Exception as e:
            raise CustomException(e)
