#!/usr/bin/env python3
import sys
import pandas as pd
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_fastq(input_file):
    data = []
    # FASTQ dosyasını oku
    for record in SeqIO.parse(input_file, "fastq"):
        seq = str(record.seq)
        length = len(seq)
        # GC İçeriği hesapla
        gc_content = (seq.count('G') + seq.count('C')) / length * 100
        # Ortalama Kalite Skoru (Phred Quality)
        mean_qual = sum(record.letter_annotations["phred_quality"]) / length
        
        data.append([record.id, length, gc_content, mean_qual])

    df = pd.DataFrame(data, columns=['Read_ID', 'Length', 'GC_Content', 'Mean_Quality'])
    
    # 1. Veriyi CSV olarak kaydet
    df.to_csv("read_stats.csv", index=False)
    
    # 2. İstatistiksel özet metni oluştur
    with open("summary.txt", "w") as f:
        f.write("--- KEY STATISTICS ---\n")
        f.write(df[['Length', 'GC_Content', 'Mean_Quality']].mean().to_string())
    
    # 3. Görselleştirme (Grafikler)
    plt.figure(figsize=(15, 5))
    
    # GC Content Dağılımı
    plt.subplot(1, 3, 1)
    sns.histplot(df['GC_Content'], color='green', kde=True)
    plt.title('GC Content Distribution')

    # Read Length Dağılımı
    plt.subplot(1, 3, 2)
    sns.histplot(df['Length'], color='blue', kde=True)
    plt.title('Read Length Distribution')

    # Quality Score Dağılımı
    plt.subplot(1, 3, 3)
    sns.violinplot(y=df['Mean_Quality'], color='red')
    plt.title('Mean Quality Scores')

    plt.tight_layout()
    plt.savefig("qc_plots.png")

if __name__ == "__main__":
    analyze_fastq(sys.argv[1])