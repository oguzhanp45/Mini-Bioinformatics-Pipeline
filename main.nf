nextflow.enable.dsl=2

params.input = "data/*.fastq" // Girdi dosya yolu
params.outdir = "results"     // Çıktı klasörü

//Hazır endüstri standardı araç (NanoPlot)
process RUN_NANOPLOT {
    publishDir "${params.outdir}/nanoplot_report", mode: 'copy'

    input:
    path fastq_file

    output:
    path "*"

    script:
    """
    NanoPlot --fastq ${fastq_file} -o .
    """
}

//Özel metrik hesaplama ve grafik aracı
process RUN_QC_ANALYSIS {
    publishDir "${params.outdir}/custom_qc", mode: 'copy'

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
    
    // Veriyi her iki işleme de paralel olarak gönderiyoruz
    RUN_NANOPLOT(input_ch)
    RUN_QC_ANALYSIS(input_ch)
}
