# Wine Quality Prediction — End-to-End MLOps Pipeline

An end-to-end Machine Learning system designed to predict wine quality using modular design patterns, automated data pipelines, MLflow experiment tracking hosted on DagsHub, and an interactive Flask web interface.

---

## Key Features

- **Modular Architecture:** Clear separation of concerns into Config, Entities, Components, and Pipelines.
- **Automated Validation:** Schema and datatype verification prior to model processing.
- **Experiment Tracking:** Real-time logging of parameters, metrics (RMSE, MAE, R²), and model artifacts via MLflow & DagsHub.
- **Web Application:** Lightweight Flask UI allowing single-sample predictions and batch evaluations.
- **Containerization:** Pre-configured `Dockerfile` for seamless deployment.

---

## Project Structure

```text
├── .github/workflows/      # CI/CD deployment pipelines
├── config/                 # Pipeline configuration files
│   └── config.yaml
├── research/               # Jupyter notebook experiments & trials
├── src/DSPROJECT/
│   ├── components/         # Ingestion, validation, transformation, training, evaluation
│   ├── config/             # Configuration managers
│   ├── constants/          # Static paths and project constants
│   ├── entity/             # Data classes and configuration types
│   ├── pipeline/           # Training and prediction stages
│   └── utils/              # Helper utilities (YAML readers, directory managers)
├── templates/              # Flask HTML templates
├── app.py                  # Web application entry point
├── main.py                 # Pipeline execution entry point
├── params.yaml             # Model hyperparameters
├── schema.yaml             # Dataset column definitions and data types
├── Dockerfile              # Container configuration
└── requirements.txt        # Project dependencies
