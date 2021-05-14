import subprocess
import pandas as pd
import os

def performOPERA_LG(assembler,k):
    contig_file=""
    if assembler=="Spades":
        contig_file="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/spades_assembly/K"+str(k)+"/final_contigs.fasta "
    elif assembler=="Soapdenovo":
        contig_file="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/soapdenovo_assembly/k"+str(k)+"/soapdenovo_Sample_2.scafSeq "
    elif assembler=="Abyss":
        contig_file="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/abyss_assembly/k"+str(k)+"/Sample_2-scaffolds.fa "
    elif assembler=="Masurca":
        contig_file="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/masurca_assembly/SOAP_assembly/asm2.scafSeq2 "
    for opera_k in range(25,150,10):
        os.system("mkdir -p "+"/".join(contig_file.split("/")[:-1])+"/OPERA_scaffold_"+str(opera_k))
        cmd="/work/LAS/rpwise-lab/sagnik/softwares/OPERA-LG/bin/OPERA-long-read.pl "
        cmd+=" --contig-file "
        cmd+=contig_file
        cmd+=" --long-read-file "
        cmd+=contig_file
        cmd+=" --output-prefix "+"/".join(contig_file.split("/")[:-1])+"/OPERA_scaffold_"+str(opera_k)+"_mapping"
        cmd+=" --output-directory "+"/".join(contig_file.split("/")[:-1])+"/OPERA_scaffold_"+str(opera_k)
        cmd+=" --num-of-processors 30 "
        cmd+=" --opera /work/LAS/rpwise-lab/sagnik/softwares/OPERA-LG/bin/ "
        cmd+=" --illumina-read1 "+" <(cat /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/65_S65_paired_trim_R1.fastq /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/68_S68_paired_trim_R1.fastq /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/2_S2_L001_cov_paired_trim_R1_001.fastq /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/2_S2_L001_enz_paired_trim_R1_001.fastq)"
        cmd+=" --illumina-read2 "+" <(cat /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/65_S65_paired_trim_R2.fastq /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/68_S68_paired_trim_R2.fastq /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/2_S2_L001_cov_paired_trim_R2_001.fastq  /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/2_S2_L001_enz_paired_trim_R2_001.fastq)"
        #print(cmd)
        """print("/".join(contig_file.split("/")[:-1])+"/OPERA_scaffold_"+str(opera_k)+"/results/scaffoldSeq.fasta")
        continue"""
        if os.path.exists("/".join(contig_file.split("/")[:-1])+"/OPERA_scaffold_"+str(opera_k)+"/results/scaffoldSeq.fasta")==False:
            subprocess.check_call(['bash', '-c', cmd])
        else:
            print("Scaffold generation is over for "+assembler+" "+k+" OPERA "+str(opera_k))
        #break
    
def main():
    filename="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/FGMP_results_post_assembly.csv"
    data = pd.read_csv(filename)
    """print(data.head())
    print(data.columns)"""
    data=data.sort_values(by=['NUM OF FGMP COMPLETENESS MARKERS'], ascending=False)
    #print(data.head())
    for index,row in enumerate(data.values.tolist()):
        if index==10:break
        #print(row)
        assembler,k=row[0],row[1]
        # Generate scaffolds
        performOPERA_LG(assembler,k)
        #break

if __name__ == "__main__":
    main()