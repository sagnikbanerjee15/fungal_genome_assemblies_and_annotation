###################################################################################################################################################################################################
# fungal_genome_assemblies_and_annotation
###################################################################################################################################################################################################

FROM ubuntu
LABEL maintainer="sagnikbanerjee15@gmail.com" 
LABEL org.opencontainers.image.source https://github.com/sagnikbanerjee15/dockerized_tools_and_pipelines

ENV TZ=America/New_York
ENV DEBIAN_FRONTEND=noninteractive

###################################################################################################################################################################################################
# Update base image and install software
###################################################################################################################################################################################################

RUN apt-get -y update
RUN apt-get -y install git python3 wget

###################################################################################################################################################################################################
# fungal_genome_assemblies_and_annotation 0.0.1
###################################################################################################################################################################################################

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN mkdir -p /softwares && \
	cd /softwares && \
	git clone https://github.com/sagnikbanerjee15/fungal_genome_assemblies_and_annotation.git && \
	cd fungal_genome_assemblies_and_annotation/src && \
	git clone https://github.com/sagnikbanerjee15/Finder.git && \
	cp Finder/scripts/annotate_gtf_with_CDS . && \
	rm -rf Finder

RUN wget https://ftp.ncbi.nlm.nih.gov/blast/db/swissprot.tar.gz && \
	tar -xvzf swissprot.tar.gz

ENV PATH $PATH:/softwares/fungal_genome_assemblies_and_annotation/src
