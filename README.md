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