# Student Performance Analyser

An end-to-end machine learning project that predicts a student's academic performance (math score) from demographic and academic factors. It covers the full lifecycle: data ingestion, transformation, model training, evaluation, a Flask web app for predictions, and deployment on AWS with CI/CD.

## Overview

Student performance depends on many factors, such as parental education, lunch type, test preparation, and scores in other subjects. This project uses those factors to train regression models and serves the best one through a web interface. A user enters a student's details and gets a predicted score.

## Features

- Modular ML pipeline with separate ingestion, transformation, and training components
- Exploratory data analysis and model experiments in Jupyter notebooks
- Preprocessing with imputation, scaling, and one-hot encoding
- Training and comparison of several regression models, including CatBoost
- Hyperparameter tuning, with the best model selected by R² score
- Saved model and preprocessor in the `artifacts/` folder
- Flask web app with a form for live predictions
- Custom logging and exception handling
- Deployment on AWS Elastic Beanstalk with a CI/CD pipeline

## Tech Stack

| Area | Tools |
|------|-------|
| Language | Python 3.x |
| Data and ML | Pandas, NumPy, Scikit-learn, CatBoost, XGBoost |
| Visualisation | Matplotlib, Seaborn |
| Web framework | Flask |
| Cloud and DevOps | AWS Elastic Beanstalk, AWS CodePipeline, Git and GitHub |

## Project Structure

```
Student_performance_analyser/
├── .ebextensions/        # AWS Elastic Beanstalk configuration
├── .vscode/              # Editor settings
├── artifacts/            # Saved data splits, model, and preprocessor
├── catboost_info/        # CatBoost training logs
├── notebook/             # EDA and model training notebooks
├── src/                  # Source code
│   ├── components/       # Data ingestion, transformation, model trainer
│   ├── pipeline/         # Training and prediction pipelines
│   ├── logger.py         # Logging setup
│   ├── exception.py      # Custom exception handling
│   └── utils.py          # Helper functions
├── templates/            # HTML templates for the Flask app
├── app.py                # Flask app (local run)
├── application.py        # Entry point for AWS Elastic Beanstalk
├── requirements.txt      # Dependencies
├── setup.py              # Package setup
└── README.md
```

## Dataset

The dataset contains student records with these features:

- **gender**
- **race/ethnicity**
- **parental level of education**
- **lunch** (standard or free/reduced)
- **test preparation course** (completed or none)
- **reading score**
- **writing score**

**Target:** math score

## Installation

```bash
# Clone the repository
git clone https://github.com/Harsh270511/Student_performance_analyser.git
cd Student_performance_analyser

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Train the model

```bash
python src/components/data_ingestion.py
```

This runs ingestion, transformation, and training, then saves the model and preprocessor to `artifacts/`.

### Run the web app

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser, fill in the student details, and click predict.

## Model Workflow

1. **Data ingestion:** load the dataset and split it into train and test sets
2. **Data transformation:** handle missing values, encode categorical features, scale numerical features
3. **Model training:** train multiple regressors and tune hyperparameters
4. **Evaluation:** compare models using R² score and pick the best one
5. **Prediction:** the saved model is loaded by the Flask app to serve predictions

## Deployment

The app is deployed on **AWS Elastic Beanstalk**. `.ebextensions` holds the environment configuration, and `application.py` is the entry point Elastic Beanstalk uses. A CI/CD pipeline (GitHub → AWS CodePipeline → Elastic Beanstalk) redeploys the app automatically on every push to `main`.

## Results

| Model | R² Score |
|-------|----------|
| Linear Regression | _add value_ |
| Random Forest | _add value_ |
| CatBoost | _add value_ |
| **Best model** | _add value_ |

## Future Improvements

- Add more features and a larger dataset
- Containerise the app with Docker
- Add model monitoring and automated retraining
- Add unit tests and GitHub Actions workflows
- Improve the UI with charts and result explanations

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, and open a pull request.

## License

Add a license (for example MIT) and link it here.

## Author

**Harsh** – [GitHub](https://github.com/Harsh270511)
