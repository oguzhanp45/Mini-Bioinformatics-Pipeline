# Long-Read Sequencing Quality Control Pipeline

An automated, fully reproducible bioinformatics workflow designed to perform primary Quality Control (QC) on raw long-read sequencing data (e.g., Oxford Nanopore, PacBio). 

## 🚀 Pipeline Architecture
This workflow is built using **Nextflow** for process management and utilizes **Conda** for strict environment and dependency isolation. Upon receiving a `.fastq` input, the pipeline executes two parallel processes:
1. **Standardized QC (`NanoPlot`):** Integrates the industry-standard long-read analysis tool to generate comprehensive HTML reports and statistics.
2. **Custom QC Analysis (`Python`):** A custom script utilizing `BioPython` and `Pandas` to calculate per-read GC content, Read Lengths, and Mean Phred Quality Scores, outputting structured CSV data and distribution plots (`Seaborn`/`Matplotlib`).

## 📁 Repository Structure
```text
.
├── bin/
│   └── qc_script.py      # Custom Python script for metric extraction & plotting
├── data/
│   └── test_reads.fastq  # Dummy sequencing data for immediate testing
├── environment.yml       # Conda dependencies (Python, NanoPlot, BioPython, Pandas, etc.)
├── main.nf               # Nextflow workflow definition
└── README.md
🛠️ Prerequisites
To run this pipeline, ensure you have the following installed on your system:

Nextflow

Miniconda or Anaconda

🏃‍♂️ Quick Start (How to Run)
1.Clone the repository:

Bash

git clone [https://github.com/oguzhanp45/Mini-Bioinformatics-Pipeline.git](https://github.com/oguzhanp45/Mini-Bioinformatics-Pipeline.git)
cd Mini-Bioinformatics-Pipeline
2.Run the automated pipeline:
The pipeline is pre-configured to process the dummy data provided in the data/ directory. Conda will automatically build the required environment upon the first run.

Bash

nextflow run main.nf -with-conda environment.yml
3.Review the Results:
Once execution is complete, a results/ directory will be generated containing:

custom_qc/: Contains read_stats.csv, a statistical summary.txt, and visual distribution plots (qc_plots.png).

nanoplot_report/: Contains the comprehensive NanoPlot QC outputs.

📧 Communication: Lab Report
To: Professor Kılıç
Subject: Initial QC Report & Metrics for Recent Long-Read Sequencing Data

Dear Professor Kılıç,

I have successfully established the automated Quality Control (QC) pipeline and completed the initial analysis of the raw long-read sequencing data you provided. The workflow concurrently utilized both specialized long-read tools (NanoPlot) and our custom analytical scripts to assess the structural integrity of the sample.

Key Analytical Findings:

Read Length Distribution: The fragment lengths exhibit a distribution characteristic of successful long-read libraries. The N50 values and length averages indicate we have sufficiently long reads to resolve complex structural variations.

GC Content: The GC distribution plot demonstrates a standard normal curve. This aligns with the expected genomic profile and suggests there is no significant contamination bias in the sample.

Mean Quality Scores (Q-Scores): The base-calling confidence falls within the expected Phred score thresholds for this specific sequencing platform. The data is highly robust.

Recommendation:
Based on the generated QC metrics and visualizations, the structural integrity and quality of the raw reads are excellent. I highly recommend that we proceed directly to the downstream full alignment phase against the reference genome.

The detailed CSV statistics, distribution graphs, and the complete NanoPlot report are available in the pipeline's output directory for your further review.

Best regards,

Oğuzhan Püsküllü

