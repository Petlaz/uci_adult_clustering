# UCI Adult Census Income Clustering

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" alt="Cookiecutter Data Science"/>
</a>
<img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
<img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">

This project explores unsupervised machine learning techniques on the UCI Adult Census Income dataset, aiming to discover hidden demographic and economic clusters within the U.S. adult population. The dataset contains mixed categorical and numerical features with missing values and outliers, making it a realistic challenge for data preprocessing and modeling.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         uci_adult_clustering and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── uci_adult_clustering   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes uci_adult_clustering a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

**Key Techniques Applied:**
- Advanced clustering (HDBSCAN on raw + latent features)
- Dimensionality reduction (UMAP, PCA)
- Autoencoder-based representation learning
- Interactive visualization

Installation

**Prerequisites**
- Python 3.9+
- pip package manager

**Setup**
```bash
# Clone repository
git clone https://github.com/yourusername/uci-adult-unsupervised.git
cd uci-adult-unsupervised

* Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

* Install dependencies
pip install -r requirements.txt

Dataset
The UCI Adult Census Income dataset contains 1994 U.S. Census data with:
Key Features:
* Demographic: age, education, marital status, race, sex
* Economic: occupation, work class, capital gains/losses
* Target: income bracket (≤50K vs >50K)
Source:UCI Machine Learning Repository

Usage
Run the main notebook for complete analysis:
bash

jupyter notebook uci_adult_unsupervised.ipynb
Workflow Stages:
1. Data Preprocessing
    * Handle missing values & outliers
    * Feature encoding & scaling
2. Exploratory Analysis
    * Feature distributions
    * Correlation heatmaps
3. Dimensionality Reduction
    * UMAP/PCA visualizations
4. Clustering
    * HDBSCAN on raw features
    * Autoencoder latent space clustering
5. Evaluation
    * Silhouette scores
    * Cluster profiling

Results & Insights
Key Findings:
* Raw feature clustering achieved strong separation (Silhouette Score ~0.915)
* Identified 5 distinct socio-economic clusters
* Latent-space clustering revealed finer subgroups
Cluster Characteristics:
1. High-Income Professionals
    * High education + managerial occupations
2. Working Class
    * Moderate education + blue-collar jobs
3. Young Part-Time Workers
    * Low hours/week + some college
4. Retirees
    * Older age + fixed income
5. Outliers
    * Extreme capital gains/losses

Deployment
Interactive Dashboard:https://img.shields.io/badge/Heroku-Deployed-blueviolet
Deployment Steps:
1. Set up Heroku CLI
2. Create new app
3. Push via Git:
bash

git push heroku main

Contributions
Contributions welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Submit a pull request

License
MIT License - See LICENSE for details
