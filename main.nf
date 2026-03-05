nextflow.enable.dsl=2

params.input = "data/*.fastq" // Girdi dosya yolu
params.outdir = "results"     // Çıktı klasörü

process RUN_QC_ANALYSIS {
    publishDir params.outdir, mode: 'copy'

    input:
    path fastq_file

    output:
    path "read_stats.csv"
    path "qc_plots.png"
    path "summary.txt"

    script:
    """
    python3 ${baseDir}/bin/qc_script.py ${fastq_file}
    """
}

workflow {
    input_ch = Channel.fromPath(params.input)
    RUN_QC_ANALYSIS(input_ch)
}