import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.model_selection import train_test_split
import joblib
from src import logging
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def get_data_transformer_object(self, df):
        logging.info("Getting data transformer object dynamically")

        # --- Step 1: Ensure TotalCharges is numeric ---
        if 'TotalCharges' in df.columns:
            df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

        # --- Step 2: Identify columns ---
        numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        object_cols = df.select_dtypes(include=['object']).columns.tolist()

        # --- Step 3: Classify categorical columns ---
        binary_cols = [col for col in object_cols if df[col].nunique() == 2]
        multi_category_cols = [col for col in object_cols if df[col].nunique() > 2]

        logging.info(f"Numerical cols: {numerical_cols}")
        logging.info(f"Binary cols: {binary_cols}")
        logging.info(f"Multi-category cols: {multi_category_cols}")

        # --- Step 4: Build transformers ---
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        binary_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OrdinalEncoder())
        ])

        multi_cat_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ])

        # --- Step 5: Combine everything ---
        preprocessor = ColumnTransformer(transformers=[
            ('num', numeric_transformer, numerical_cols),
            ('bin', binary_transformer, binary_cols),
            ('multi', multi_cat_transformer, multi_category_cols)
        ])

        return preprocessor
    
    def initiate_data_transformer(self):
        logging.info("Initiating data transformer")

        df = pd.read_csv(self.config.data_path)
        target_name = str(self.config.target_name)

        X = df.drop(columns=target_name)
        y = df[target_name]

        preprocessing_obj = self.get_data_transformer_object(X)

        # --- Split data ---
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # --- Encode target variable ---
        y_train = y_train.map({'Yes': 1, 'No': 0}).fillna(0).astype(int)
        y_test = y_test.map({'Yes': 1, 'No': 0}).fillna(0).astype(int)

        logging.info(f"\nX_train: {X_train.shape}\nX_test: {X_test.shape}\ny_train: {y_train.shape}\ny_test: {y_test.shape}")

        # --- Apply preprocessing ---
        logging.info("Applying preprocessing on training and testing data")
        X_train_arr = preprocessing_obj.fit_transform(X_train)
        X_test_arr = preprocessing_obj.transform(X_test)

        # --- Save preprocessing object ---
        with open(self.config.transformer_path, "wb") as f:
            joblib.dump(preprocessing_obj, f)

        # --- Optionally save splits ---
        X_train.to_csv(self.config.X_train_path, index=False)
        X_test.to_csv(self.config.X_test_path, index=False)
        y_train.to_csv(self.config.y_train_path, index=False)
        y_test.to_csv(self.config.y_test_path, index=False)

        return preprocessing_obj, X_train_arr, X_test_arr, y_train, y_test
