# Text Embedding Visualization Tool

## Overview

This repository demonstrates the application of text embeddings, Uniform Manifold Approximation and Projection (UMAP), and visualization tools such as Plotly Dash to gain insights into a dataset of research paper abstracts and associated metadata. 

![Text Embedding Dashboard Demo](data\text-embedding-demo.gif)

## Installation

### Google Colab

To run the demo on Google Colab, follow these steps:

1. Copy the URL of the `abstract_summary.ipynb` notebook: [Notebook URL](https://github.com/NoviaIntSysGroup/text-embedding-demo/blob/main/notebooks/abstract_summary.ipynb)
2. Navigate to [Google Colab](https://colab.research.google.com/).
3. Click on `File` > `Open notebook`.
4. Switch to the `GitHub` tab, paste the copied URL into the search bar, and press Enter.
5. Open the notebook from the search results.

### Local Installation

To install and run the demo locally, follow the steps below in the terminal:

```bash
$ conda create -n text-embedding-demo python=3.11
$ conda activate text-embedding-demo
$ pip install torch # Use the exact installation command from https://pytorch.org/
$ git clone https://github.com/NoviaIntSysGroup/text-embedding-demo.git
$ cd text-embedding-demo
$ pip install -e .
```
NOTE: One needs to have conda, python and git installed.

## Components

### 1. 2D UMAP Scatter Plot
- **Description**: Utilizes UMAP for visualizing data similarity in a 2D scatter plot, where each point corresponds to an individual research paper.  
- **Interactive Features**:
  - **Hover**: Displays summary/abstract and metadata on hover.
  - **Selection**: Enables selection of multiple points for comparative analysis.

### 2. Keyword Bar Graph
- **Description**: A horizontal bar graph representing the similarity of keywords in the dataset, offering insights into dominant themes.

### 3. Detailed Data View
- **Description**: Provides detailed information about a highlighted or selected data entry from the scatter plot.

### 4. Spider (Radar) Chart
- **Description**: Visualizes metrics related to the dataset using a radar chart.
- **Features**:
  - **Mean Line**: Depicts the average value for each metric across the dataset.
  - **Hover Line**: Updates to show the metric values of a data point highlighted in the UMAP plot.

## Usage

- **Explore Clusters**: Begin with the 2D UMAP scatter plot to explore data clusters and patterns.
- **Inspect Details**: Hover over points to view abstracts, metadata, and an updated Spider Chart.
- **Group Analysis**: Select multiple points for comparative analysis.
- **Identify Themes**: Abstracts can be color-coded based on their similarity to a specific input query by user or a selected topic sentence. Analyze the Keyword Bar Graph for prevalent themes and leverage the UMAP-generated scatter plot for thematic categorization of abstracts.
- **Deep Dive**: Use the Detailed Data View and Spider Chart for deeper insights, comparing individual metrics against the dataset mean.

## Contributors:

- [Johan Westö](mailto:johan.westo@novia.fi)
- [Mikael Manngård](mailto:mikael.manngard@novia.fi)
- [Ashish Dahal](https://www.linkedin.com/in/adahal/)
