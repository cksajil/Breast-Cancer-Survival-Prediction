# Breast-Cancer-Survival-Prediction
Breast Cancer Survival Prediction with Clinical and Gene Expression Data

### Overview

Cancer is a disease in which cells in the human body grow uncontrollably. This phenomenon often spreads to other parts of the body. Human bodies contain
trillions of cells. Human growth starts with a one-celled zygote. Both sperm and egg from parents meet and form the zygote. The process of cell division is essential to human life to form various tissues and organs as the body needs them. The cells also have a life cycle. As they grow older or are damaged, the cells die and are replaced with new ones. This natural process sometimes breaks and abnormal or damaged cells keep multiplying. These unwanted cells may form tumors. Such a situation is known as cancer.

Breast cancer is the second most common cancer after skin cancer in women. It affects nearly 2.1 million women every year globally. Genetic information is the software that runs behind every biological organism. Modern genetic measurement technologies such as Next Generation Sequencing and Microarray
show light on active and inactive genes responsible for certain biological functions. Comparing these gene expression changes for healthy and cancerous
cells sheds light on the causal factors associated with cancer growth. This gives better insights into cancer prognosis and treatment plans such as therapy. Machine learning helps us to learn complex patterns from intricate data that are difficult for human beings to recognize manually. One such use case is estimating the survival time and hence preventing unnecessary surgical treatments. Here in this project, the survival status is predicted using gene expression data and clinical data using classical machine learning algorithms.

### Dataset
The dataset going to be used in the case study is published in Nature Communications (Pereira et al., 2016), also available in Kaggle named as
Molecular Taxonomy of Breast Cancer International Consortium (METABRIC) database. This is part of a Canada-UK Project which contains targeted
sequencing data of 1,980 primary breast cancer samples. The associated clinical and genomic data was downloaded from cBioPortal. The dataset was originally
collected by Professor Carlos Caldas from Cambridge Research Institute and Professor Sam Aparicio from the British Columbia Cancer Center in Canada.

### Jupyter Notebooks
The project is carried out in the following jupyter notebooks:
  1. EDA_Modeling.ipynb: contains the exploratory data analysis and visualization of the data
  2. Case_Study_I_Final.ipynb: conatins functions that predicts on new data using saved models

The deployment.zip file contains python code corresponding to a deployed version of the project as flask based webapp.
