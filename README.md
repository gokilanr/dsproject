# End to End Data Science Project
Goal: Build an ML pipeline for Wine Quality prediction with structured modules, tracking experiments with MLflow on DagsHub, and display results on a Flask web interface.

Dataset: winequality.csv (red/white wine dataset)

Modules/Components:

1.Entity (entity) – Defines configuration and data classes:
DataIngestionConfig
DataTransformationConfig
ModelTrainerConfig
ModelEvaluationConfig

2.Configuration (config) – Reads YAML files and provides config objects for each stage:
ConfigurationManager loads config.yaml and params.yaml

3.Constants (constants) – Paths, file names, column names, etc.

4.Utils (utils) – Helper functions:

read_yaml, save_json, create_directories, etc.

5.Data Ingestion (data_ingestion):

Load raw data (winequality.csv)

Split into train/test

Save to artifact/raw and artifact/processed

6.Data Transformation (data_transformation):

Clean data, handle missing values

Feature engineering (scaling, encoding, etc.)

Output: transformed train/test datasets

7. Data Validation (data_validation):

Schema validation (check required columns, dtypes)

Value range checks

Output: validation report

8. Model Training (model_trainer):

Train ML model (ElasticNet / RandomForest, etc.)

Save model to artifact/models/model.pkl

Log parameters to MLflow

9. Model Evaluation (model_evaluation):

Load trained model

Predict on test set

Compute metrics (RMSE, MAE, R2)

Save metrics locally

Log metrics & model to MLflow/DagsHub

10. Flask App (app.py):

Simple HTML interface to:

Upload a CSV or input wine features

Display predictions

Display evaluation metrics from MLflow
not deployed in any cloud.

11. MLflow/DagsHub:

Configure mlflow.set_tracking_uri("https://dagshub.com/<username>/<repo>.mlflow")
### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py