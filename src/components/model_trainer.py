import pandas as pd
import os
from src import logging, CustomException
from xgboost import XGBClassifier
import joblib
import time
from scipy import sparse
from sklearn.metrics import recall_score
import optuna
import yaml
from dataclasses import replace
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config 
        
        
    def get_best_params(self, n_trials=30):
        """Optuna hyperparameter tuning"""
        logging.info("Find best params")
        params_config = self.config.all_params
        
        # load data 
        X_train_arr = sparse.load_npz(self.config.X_train_path)
        X_test_arr = sparse.load_npz(self.config.X_test_path)
        y_train = pd.read_csv(self.config.y_train_path)
        y_test = pd.read_csv(self.config.y_test_path)
        
        def objective(trial):
            params = {} 
            for key, cfg in params_config.items():
                if isinstance(cfg, (int, float, str, bool)):
                    params[key] = cfg 
                    continue
                
                p_type = cfg.get("type")
                low = cfg.get("low")
                high = cfg.get("high")
                
                if p_type == "int":
                    params[key] = trial.suggest_int(key,low,high)
                    
                elif p_type == "float":
                    if cfg.get("log", False):
                        params[key] = trial.suggest_float(key, low, high, log=True)
                    else:
                        params[key] = trial.suggest_float(key, low, high)
                
            # handle dynamic scale_pos_weight 
            if params.get("scale_pos_weight") == "auto":
                scale = (y_train.value_counts().iloc[0]).sum() / (y_train.value_counts().iloc[1]).sum()
                params["scale_pos_weight"] = float(scale)
                
            # Fixed values 
            params["random_state"] = 42 
            params["n_jobs"] = -1 
            params["eval_metric"] = "logloss"
            
            
            # Evaluate model 
            model = XGBClassifier(**params)       
            model.fit(X_train_arr, y_train)
            proba = model.predict_proba(X_test_arr)[:,1]
            y_pred = (proba >= self.config.THRESHOLD).astype(int)
            return recall_score(y_test ,y_pred, pos_label=1)
        
        
        # run optuna 
        study = optuna.create_study(direction="maximize")
        study.optimize(objective, n_trials=n_trials)     
        
        
        best_params = study.best_params 
        logging.info(f"✅ Best parameters found: {best_params}")
        
        # save best params 
        with open(self.config.best_params_path, "w") as f:
            yaml.dump(best_params, f)
        
        # update config to use best params for training
        self.config= replace(self.config, all_params=best_params)
        
        return best_params
            
    
    
    def train(self):
        """Train final model using best params"""
        #Initiate Model 
        model = XGBClassifier(**self.config.all_params)
        logging.info(f"🚀 Initializing model: {model.__class__.__name__} with parameters: {model.get_params()}")
        
        # load data 
        X_train_arr = sparse.load_npz(self.config.X_train_path)
        y_train = pd.read_csv(self.config.y_train_path)
        
        # Training timer
        start_train = time.time()
        model.fit(X_train_arr, y_train)
        train_time = time.time() - start_train
        print(f"⏱ Training time: {train_time:.2f} seconds")
        
        # save model 
        model_save_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model, model_save_path)
        logging.info(f"Model {model.__class__.__name__} saved at {model_save_path}")
        
        return model
        
        