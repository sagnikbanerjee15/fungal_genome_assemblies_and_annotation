import os

def readInfoFromFGMPSummaryFile(filename):
    fhr=open(filename,"r")
    for line in fhr:
        if "NUM OF UCEs found:" in line:
            UCEs=line.strip().split("NUM OF UCEs found:")[-1].strip().split()[0]
        elif "NUM OF MARKERS COMPLETE:" in line:
            num_of_complete_markers=line.strip().split()[-1]
        elif "NUM OF MARKERS PARTIAL" in line:
            num_of_partial_markers=line.strip().split()[-1]
        elif "NUM OF ABBERANT PROTEINS" in line:
            num_of_abberant_markers=line.strip().split()[-1]
        elif "NUM OF FGMP COMPLETENESS MARKERS" in line:
            num_of_fgmp_completeness_markers=line.strip().split()[-1]
    fhr.close()
    return UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers

def collectInfoForAbyssAssemblies():
    abyss_assembly_info=[]
    for k in range(50,101,10):
        filename="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/abyss_assembly/k"+str(k)+"/Sample_2-scaffolds.fa.unfiltered.renamed.hmmsearch.summary_report"
        if os.path.exists(filename):
            UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers=readInfoFromFGMPSummaryFile(filename)
        else:
            UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers="NA","NA","NA","NA","NA"
        abyss_assembly_info.append(["Abyss",str(k),UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers])
    return abyss_assembly_info

def collectInfoSoapDenovo2Assemblies():
    soap_devono_assembly_info=[]
    for k in range(15,127,10):
        filename="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/soapdenovo_assembly/k"+str(k)+"/soapdenovo_Sample_2.scafSeq.unfiltered.renamed.hmmsearch.summary_report"
        if os.path.exists(filename):
            UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers=readInfoFromFGMPSummaryFile(filename)
        else:
            UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers="NA","NA","NA","NA","NA"
        soap_devono_assembly_info.append(["Soapdenovo",str(k),UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers])
    return soap_devono_assembly_info

def collectInfoSpadesAssemblies():
    spades_devono_assembly_info=[]
    for k in range(15,127,10):
        filename="/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/spades_assembly/K"+str(k)+"/final_contigs.fasta.unfiltered.renamed.hmmsearch.summary_report"
        if os.path.exists(filename):
            UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers=readInfoFromFGMPSummaryFile(filename)
        else:
            UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers="NA","NA","NA","NA","NA"
        spades_devono_assembly_info.append(["Spades",str(k),UCEs,num_of_complete_markers,num_of_partial_markers,num_of_abberant_markers,num_of_fgmp_completeness_markers])
    return spades_devono_assembly_info

def main():
    abyss_assembly_info=collectInfoForAbyssAssemblies()
    masurca_assembly_info=[["Masurca","auto"]]
    masurca_assembly_info[0].extend(readInfoFromFGMPSummaryFile("/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/masurca_assembly/SOAP_assembly/asm2.scafSeq2.unfiltered.renamed.hmmsearch.summary_report"))
    print(masurca_assembly_info)
    soap_denovo_assembly_info=collectInfoSoapDenovo2Assemblies()
    spades_denovo_assembly_info=collectInfoSpadesAssemblies()
    fhw=open("/work/LAS/rpwise-lab/sagnik/3FG/data/Sample_2/FGMP_results_post_assembly.csv","w")
    fhw.write(",".join(["Assembler","K","NUM OF UCEs found","NUM OF MARKERS COMPLETE","NUM OF MARKERS PARTIAL","NUM OF ABBERANT PROTEINS","NUM OF FGMP COMPLETENESS MARKERS"])+"\n")
    for assembly in [abyss_assembly_info,masurca_assembly_info,soap_denovo_assembly_info,spades_denovo_assembly_info]:
        for row in assembly:
            fhw.write(",".join(row)+"\n")
    fhw.close()

if __name__ == "__main__":
    main()