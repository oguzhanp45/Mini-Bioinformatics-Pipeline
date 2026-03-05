# Long-Read Sequencing Quality Control Pipeline

This repository contains an automated, reproducible bioinformatics pipeline for Quality Control (QC) of long-read sequencing data (e.g., Oxford Nanopore, PacBio). It is built using **Nextflow** and uses **Conda** for dependency management.

## 🚀 Features
* **Automated Processing:** Reads raw `.fastq` files and extracts key metrics.
* **Metric Calculation:** Calculates Read Length, GC Content, and Mean Phred Quality Scores per read.
* **Visualization:** Automatically generates distribution plots (Histograms and Violin plots).
* **Reproducibility:** Fully containerized environment via Conda.

## 🛠️ Prerequisites
* [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html)
* [Conda](https://docs.conda.io/en/latest/miniconda.html)

## 🏃‍♂️ How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/oguzhanp45/Mini-Bioinformatics-Pipeline.git](https://github.com/oguzhanp45/Mini-Bioinformatics-Pipeline.git)
   cd Mini-Bioinformatics-Pipeline
