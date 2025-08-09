---
title: UCI Adult Census Income Clustering Dashboard
emoji: 🌖
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 5.42.0
app_file: app.py
pinned: false
license: mit
short_description: This Space implements an interactive clustering dashboard.
---

# UCI Adult Census Income Clustering Dashboard

This Space implements an interactive clustering dashboard for the UCI Adult Census Income dataset using Gradio. Explore demographic and economic clusters interactively by selecting numeric features and cluster counts.

## Usage

- Select features and number of clusters on the sidebar  
- Click **Run Clustering** to view cluster counts  

## Data Source

Dataset is loaded dynamically from a public Google Drive CSV link.

## Tech Stack

- Python  
- Pandas  
- Scikit-learn (KMeans, StandardScaler)  
- Gradio (for UI)

## Author

Peter Obi

---

## Deployment

This app is deployed on Hugging Face Spaces with Gradio. You can view and interact with the live demo here:  
[https://huggingface.co/spaces/Peterobi/uci_adult_clustering](https://huggingface.co/spaces/Peterobi/uci_adult_clustering)
