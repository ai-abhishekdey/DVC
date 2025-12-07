## ML Pipeline with DVC and MLflow

**Author: Abhishek Dey**

## About:

This project demonstrates a reproducible end-to-end Machine Learning pipeline using DVC and MLFlow. 

## Problem Statement:

To classify Iris flower species using the [Iris dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv)

## Pipeline Stages:

| Stage                   | Script                      | Purpose                                      |
| ----------------------- | ----------------------------| ---------------------------------------------|
| 1. Data Ingestion       | `src/data_ingestion.py`     | Download dataset from URL                    |
| 2. Data Preprocessing   | `src/data_preprocessing.py` | Clean raw dataset                            |
| 3. Feature Engineering  | `src/feature_engineering.py`| Generate features dataset for training       |
| 4. Model Training       | `src/train.py`              | Train & save model file                      |
| 5. Evaluation           | `src/eval.py`               | Compute accuracy and log evaluation metrics  |         |

## Setup virtual environment and install packages

```
python3 -m venv myenv

source  myenv/bin/activate

pip3 install -r requirements.txt

```

## Run Pipeline

```
dvc repro

```


