
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


# ============================================================
# 1. MODEL TRAINER CONFIGURATION
# ============================================================

@dataclass
class ModelTrainerConfig:

    trained_model_file_path: str = os.path.join(
        "artifacts",
        "model.pkl"
    )


# ============================================================
# 2. MODEL TRAINER CLASS
# ============================================================

class ModelTrainer:

    def __init__(self):

        self.model_trainer_config = ModelTrainerConfig()


    # ========================================================
    # 3. MODEL TRAINING METHOD
    # ========================================================

    def initiate_model_trainer(self, train_array, test_array):

        try:

            logging.info("Started model training")


            # =================================================
            # STEP 1: SPLIT TRAINING AND TESTING DATA
            # =================================================

            logging.info("Splitting training and testing data")

            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]

            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]


            # =================================================
            # STEP 2: DEFINE MODELS
            # =================================================

            models = {

                "Random Forest":
                    RandomForestRegressor(),

                "Decision Tree":
                    DecisionTreeRegressor(),

                "Gradient Boosting":
                    GradientBoostingRegressor(),

                "Linear Regression":
                    LinearRegression(),

                "XGBRegressor":
                    XGBRegressor(),

                "CatBoosting Regressor":
                    CatBoostRegressor(verbose=False),

                "AdaBoost Regressor":
                    AdaBoostRegressor()
            }


            # =================================================
            # STEP 3: DEFINE HYPERPARAMETERS
            # =================================================

            params = {

                "Decision Tree": {

                    "criterion": [
                        "squared_error",
                        "friedman_mse",
                        "absolute_error",
                        "poisson"
                    ]
                },


                "Random Forest": {

                    "n_estimators": [
                        8,
                        16,
                        32,
                        64
                    ]
                },


                "Gradient Boosting": {

                    "learning_rate": [
                        0.1,
                        0.01,
                        0.05
                    ],

                    "subsample": [
                        0.6,
                        0.8,
                        0.9
                    ],

                    "n_estimators": [
                        8,
                        16,
                        32,
                        64
                    ]
                },


                "Linear Regression": {},


                "XGBRegressor": {

                    "learning_rate": [
                        0.1,
                        0.01,
                        0.05
                    ],

                    "n_estimators": [
                        8,
                        16,
                        32,
                        64
                    ]
                },


                "CatBoosting Regressor": {

                    "depth": [
                        6,
                        8
                    ],

                    "learning_rate": [
                        0.01,
                        0.05,
                        0.1
                    ],

                    "iterations": [
                        30,
                        50,
                        100
                    ]
                },


                "AdaBoost Regressor": {

                    "learning_rate": [
                        0.1,
                        0.01,
                        0.5
                    ],

                    "n_estimators": [
                        8,
                        16,
                        32,
                        64
                    ]
                }
            }


            # =================================================
            # STEP 4: EVALUATE ALL MODELS
            # =================================================

            logging.info("Evaluating different models")

            model_report = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params
            )


            logging.info(f"Model report: {model_report}")

            print("\nMODEL REPORT")
            print("--------------------------------")

            for model_name, score in model_report.items():

                print(
                    f"{model_name}: {score:.4f}"
                )


            # =================================================
            # STEP 5: FIND BEST MODEL SCORE
            # =================================================

            best_model_score = max(
                model_report.values()
            )

            print("\nBEST MODEL SCORE:", best_model_score)


            # =================================================
            # STEP 6: FIND BEST MODEL NAME
            # =================================================

            best_model_name = list(
                model_report.keys()
            )[
                list(model_report.values()).index(
                    best_model_score
                )
            ]

            print(
                "BEST MODEL:",
                best_model_name
            )


            # =================================================
            # STEP 7: GET BEST MODEL
            # =================================================

            best_model = models[
                best_model_name
            ]


            # =================================================
            # STEP 8: TRAIN BEST MODEL
            # =================================================

            logging.info(
                f"Training best model: {best_model_name}"
            )

            best_model.fit(
                X_train,
                y_train
            )


            # =================================================
            # STEP 9: SAVE BEST MODEL
            # =================================================

            logging.info(
                "Saving trained model"
            )

            save_object(
                file_path=
                self.model_trainer_config.trained_model_file_path,

                obj=best_model
            )


            print(
                "\nModel saved successfully!"
            )

            print(
                "Location:",
                self.model_trainer_config.trained_model_file_path
            )


            # =================================================
            # STEP 10: PREDICTION
            # =================================================

            predicted = best_model.predict(
                X_test
            )


            # =================================================
            # STEP 11: CALCULATE R2 SCORE
            # =================================================

            r2_square = r2_score(
                y_test,
                predicted
            )


            print(
                "Final R2 Score:",
                r2_square
            )


            logging.info(
                f"Final R2 score: {r2_square}"
            )


            return r2_square


        except Exception as e:

            logging.error(
                "Error occurred during model training"
            )

            raise CustomException(
                e,
                sys
            )

### What this code does

# Your complete pipeline is now:

# ```text
# stud.csv
#    ↓
# Data Ingestion
#    ↓
# train.csv + test.csv
#    ↓
# Data Transformation
#    ↓
# train_arr + test_arr
#    ↓
# Model Trainer
#    ↓
# Try multiple ML models
#    ↓
# Compare R² scores
#    ↓
# Choose best model
#    ↓
# FIT best model
#    ↓
# save_object()
#    ↓
# artifacts/model.pkl
# ```

# The key new part is:

# ```python
# best_model.fit(X_train, y_train)
# ```

# Then:

# ```python
# save_object(
#     file_path=self.model_trainer_config.trained_model_file_path,
#     obj=best_model
# )
# ```

# So after successful execution you should have:

# ```text
# mlproject48/
# │
# ├── artifacts/
# │   ├── data.csv
# │   ├── train.csv
# │   ├── test.csv
# │   ├── proprocessor.pkl
# │   └── model.pkl          ← THIS
# │
# ├── notebook/
# ├── src/
# │   ├── components/
# │   │   ├── data_ingestion.py
# │   │   ├── data_transformation.py
# │   │   └── model_trainer.py
# │   ├── exception.py
# │   ├── logger.py
# │   └── utils.py
# │
# └── ...
# ```

# # ### One important thing

# # Your `model_trainer.py` depends on **`evaluate_models()` and `save_object()` inside `src/utils.py`**.

# # So if you run this and `model.pkl` **still doesn't appear**, don't change this file again. Send me your **complete `src/utils.py`**.

# # I'll check those two functions because that's the next likely place where the problem is.
