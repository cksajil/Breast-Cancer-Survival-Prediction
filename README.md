# Breast-Cancer-Survival-Prediction (work in progress)
Breast Cancer Survival Prediction with Clinical and Gene Expression Data

### Overview

Breast cancer is the second most common cancer after skin cancer in women. It affects nearly 2.1 million women every year globally. Modern genetic measurement technologies such as Next Generation Sequencing and Microarray show light on active and inactive genes responsible for certain biological functions. Comparing these gene expression changes for healthy and cancerous cells sheds light on the causal factors associated with cancer growth. This gives better insights into cancer prognosis and treatment plans such as therapy. 

Machine learning helps us to learn complex patterns from intricate data that are difficult for human beings to recognize manually. One such use case is estimating the survival time and hence preventing unnecessary surgical treatments. Here in this project, the survival status is predicted using gene expression data and clinical data using classical machine learning algorithms.

### Dataset
The dataset going to be used in the case study is published in Nature Communications ([Pereira et al., 2016](https://www.nature.com/articles/ncomms11479)), also available in Kaggle named as Molecular Taxonomy of Breast Cancer International Consortium (METABRIC) database. This is part of a Canada-UK Project which contains targeted sequencing data of 1,980 primary breast cancer samples. The associated clinical and genomic data was downloaded from [cBioPortal](https://www.cbioportal.org/). The dataset was originally collected by Professor Carlos Caldas from Cambridge Research Institute and Professor Sam Aparicio from the British Columbia Cancer Center in Canada.

### Jupyter Notebooks
The analysis is available in the following jupyter notebooks:
  1. EDA_Modeling.ipynb: contains the exploratory data analysis and visualization of the data
  2. Case_Study_I_Final.ipynb: conatins functions that predicts on new data using saved models

### Flask Deployment
The deployment.zip file contains python code corresponding to a deployed version of the project as flask based webapp.

**Python Version**
```
Python 3.9.12
```

### Setting up virtual environment

*Installing Virtual Environment*
```console
python -m pip install --user virtualenv
```
*Creating New Virtual Environment*
```console
python -m venv envname
```
*Activating Virtual Environment*
```console
source envname/bin/activate
```
*Upgrade PIP*
```console
python -m pip install --upgrade pip
```
*Installing Packages*
```console
python -m pip install -r requirements.txt
```

### How to run

```console
#Download Dataset
python run.py -s d

#Model Training
python run.py -s m

#Predict on Test Data
python run.py -s t
```

### Testing
```console
python -m pytest --verbose
```

### Results

| Model | Accuracy (5-fold CV)  | AUC          | Sensitivity  | Specificity  | FPR          |
|-------|-----------------------|--------------|--------------|--------------|--------------|
| LR    | 0.7601 +/- 0.0267     | 0.769232     | 0.755396     | 0.783069     | 0.216931     |
| DT    | 0.7447 +/- 0.0288     | 0.733470     | 0.705036     | 0.761905     | 0.238095     |
| SVM   | 0.7434 +/- 0.0289     | **0.774105** | 0.712230     | 0.835979     | 0.164021     |
| RF    | 0.6454 +/- 0.0378     | 0.665772     | 0.453237     | **0.878307** | **0.121693** |
| XGB   | **0.8128 +/- 0.0212** | 0.767957     | **0.805755** | 0.730159     | 0.269841     |
