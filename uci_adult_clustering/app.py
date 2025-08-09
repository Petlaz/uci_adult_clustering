import gradio as gr
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load CSV directly from Google Drive
CSV_URL = "https://drive.google.com/uc?export=download&id=1JgrEn4PlLUNpPL5x_fksO_zTiHvTKf16"
df_processed = pd.read_csv(CSV_URL)
numeric_cols = df_processed.select_dtypes(include=["number"]).columns.tolist()

def run_clustering(selected_features, n_clusters):
    if not selected_features:
        return "Please select at least one feature."
    X = df_processed[selected_features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    
    counts = pd.Series(labels).value_counts().sort_index().to_dict()
    result_str = "\n".join([f"Cluster {k}: {v} points" for k, v in counts.items()])
    return result_str

with gr.Blocks() as demo:
    gr.Markdown("# UCI Adult Clustering Dashboard")
    gr.Markdown("Interactive visualization & cluster exploration")

    features_input = gr.CheckboxGroup(
        choices=numeric_cols, label="Select features", value=numeric_cols
    )
    clusters_input = gr.Slider(
        minimum=1, maximum=10, step=1, value=3, label="Number of Clusters"
    )
    run_button = gr.Button("Run Clustering")

    output_text = gr.Textbox(label="Cluster Counts", interactive=False)
    
    run_button.click(
        fn=run_clustering,
        inputs=[features_input, clusters_input],
        outputs=output_text,
    )

if __name__ == "__main__":
    demo.launch()
