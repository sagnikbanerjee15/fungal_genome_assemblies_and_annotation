1. Install conda from https://www.anaconda.com/distribution/
2. You will need two different environments - one called masurca which will have everything you need to do the assembling and scaffolding, the other is called FGMP for running FGMP. Two environments yml files are included in this folder one for masurca and the other for FGMP
3. Download from github git clone https://github.com/stajichlab/FGMP.git
4. Install both the environments
	- conda env create -f environment_FGMP.yml
	- conda env create -f environment_masurca.yml
5. Request an interactive node. Then issue the command `conda activate masurca`. You need to be in conda environment even if you run a pbs script.
6. Check the pbs_scripts folder. There are pbs scripts for each of the assemblers. Change the Sample_2 and also the names of the read files.
7. Change to the FGMP environment. `conda activate FGMP`
8. To run FGMP you will need to copy each contig/scaffold fasta file to the location where you downloaded FGMP and then run FGMP.
9. Please use the pbs script named assembly_fgmp.pbs to run FGMP

## BRAKER commands

nohup braker.pl --genome=/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/soapdenovo_assembly/k115/soapdenovo_Sample_2.scafSeq --prot_seq=/work/LAS/rpwise-lab/sagnik/3FG/data/uniprot.fasta --ALIGNMENT_TOOL_PATH=/work/LAS/rpwise-lab/sagnik/softwares/anaconda3/envs/BRAKER2/bin -prg=gth --trainFromGth --species=Cercospora_sojina --softmasking --gff3 --cores 30 --fungus --overwrite --workingdir=/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/soapdenovo_assembly/k115/braker2 > /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/soapdenovo_assembly/k115/braker2.output 2> /work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/soapdenovo_assembly/k115/braker2.error &

## Assembling the genome

1)  Masurca (http://www.genome.umd.edu/masurca.html)

2)  SWAP-Assembler2 (https://ieeexplore.ieee.org/abstract/document/7573818)

3)  SOAPdenovo

4)  ALLPATHS-LG [Needs jumping reads]

5)  ABySS 2.0 (https://genome.cshlp.org/content/27/5/768)

6)  SPAdes

7)  PASHA (Last Update on 2013) (http://pasha.sourceforge.net/homepage.htm#latest)

## Scaffolders

1)  OPERA-LG (https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0951-y)

2)  InGAP (https://academic.oup.com/nar/article/45/6/e43/2638393)

3)  iLSLS (https://ieeexplore.ieee.org/abstract/document/8416733)

4)  AGOUTI (https://academic.oup.com/gigascience/article/5/1/s13742-016-0136-3/2558793) [Uses RNA-Seq reads]

5)  Rascaf ([file:///Users/gsfuerst/Downloads/tpg-9-3-plantgenome2016.03.0027.pdf](file:///Users/gsfuerst/Downloads/tpg-9-3-plantgenome2016.03.0027.pdf)) [Uses RNA-Seq reads]

6)  P_RNA_scaffolder (https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-4567-3?optIn=false)

7) SSPACE Scaffolding pre-assembled contigs using SSPACE. Boetzer M, Henkel CV, Jansen HJ, Butler D, Pirovano W Bioinformatics. 2011 Feb 15; 27(4):578-9.

8) GapFiller: a de novo assembly approach to fill the gap within paired reads. Nadalin F, Vezzi F, Policriti A BMC Bioinformatics. 2012; 13 Suppl 14():S8.



## Assessing genome quality

Perform `FGMP` comparison - script already written up

## Characterizing the genome

1. Find tandem repeats and TEs using repeatmasker, repeatmodeller and LTR FINDER (Xu, Z., and H. Wang, 2007 LTR_FINDER: an efficient tool for the prediction of full-length LTR retrotransposons. Nucleic Acids Res. 35 (Web Server issue): W265–268.)
2. Estimate genome size (Estimation of genomic characteristics by analyzing *k-*mer frequency in *de novo* genome projects. *eprint arXiv*, 13082012 (2013).) See k-mer analysis of https://www.nature.com/articles/s41598-019-42231-9

GC Content

N50

Total Length

Total Number of contigs

Table 1 of https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5374754/

## Genome annotation

1. BRAKER using RNA-Seq data and verified proteins obtained from Uniprot
2. rRNA - RNAmmer ( RNAmmer: consistent and rapid annotation of ribosomal RNA genes. )
3. tRNA - RFAM (Rfam: annotating non-coding RNAs in complete genomes)
4. ncRNA genes - TRNASCAN-SE (tRNAscan-SE: a program for improved detection of transfer RNA genes in genomic sequence.)
5. Verification with BUSCO

## Functional annotation

1. CSEP discovery (Effectorp, Localizer and Apoplastp)
2. Blast2GO (High-throughput functional annotation and data mining with the Blast2GO suite)
3. MFannot https://megasun.bch.umontreal.ca/cgi-bin/mfannot/mfannotInterface.pl
4. hmmsearch https://www.sciencedirect.com/science/article/pii/S2352340919310480#bib17) against PFAM database (v32.0) (e-value cut off ≤ 10e-5) 
5. BLASTP https://www.sciencedirect.com/science/article/pii/S2352340919310480#bib18) (e-value cut off ≤ 10e-10) against the NCBI nr database
6. CSEP discovery (Effectorp, Localizer, Apoplastp)
7. Run phylostratr on the proteins to determine clades
8. Orthologous genes analysis using OrthoMCL (OrthoMCL: Identification of ortholog groups for eukaryotic genomes. Gen Res. 2003;13(9):2178–89.)

https://mbio.asm.org/content/10/5/e01692-19 --> nice discussion of several biologically intersting features about the genome



# TO DO

1. Rewrite scripts to make the job plug and play - simpler to run
2. Download experimentally verified proteins from Uniprot (Type in database:(type:ensemblfungi) AND reviewed:yes in the search box) September 2020. Total of 28270 sequences were obtained.
3. Set up one single conda environment for doing all analysis
4. 

