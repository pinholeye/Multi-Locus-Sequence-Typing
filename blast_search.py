#Imports
from subprocess import Popen, PIPE

def BLAST_search(genome):

#Calling method:
#BLAST_search("genomes/*.fna")
    
    blast_results = [
        "blastn", 
        "-query", "input/alleles_query.fna", 
        "-subject",  genome, 
        "-task", 'blastn', 
        "-outfmt", "6 qseqid qlen qstart qend evalue sseq",
        "-out", "output/genome.tsv"
    ]
    
    pipe = Popen(blast_results, stdout=PIPE, stderr=PIPE)
    
    stdout, stderr = pipe.communicate()
    
    return stdout.decode()