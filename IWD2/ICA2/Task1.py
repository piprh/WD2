#!/usr/bin/python3
#IMPORT modules
from Bio import Entrez, SeqIO
import os, sys, subprocess


### NCBI DATABASE SEARCH ###
#Various personal info for NCBI API
#email to prevent NCBI throttling - user could input their own or have option to go without
Entrez.email = "pippi.r.hill@gmail.com"
#NCBI API token - user should input their own if htey have one
NCBI_token = "beb3d549cbfdc17be696fdec0d4f3d92b909"

#Search optional parameters, default is G6P, Aves - user to input
protein = "glucose-6-phosphatase" 
taxa = "Aves"
#Concatenate search terms to make esearch easier to read
search_term = protein + "[PROT]" + " AND " + taxa + "[ORGN]"
retmax = 10 ##User input?
#Run search
Entrez.api_key = NCBI_token
search = Entrez.esearch(db="protein", retmax=retmax, term = search_term, 
        sleep_between_tries = 30)
#Save protein IDs obtained in search
ID_list = Entrez.read(search)['IdList']
print("Found %s accession numbers for %s %s: " % (len(ID_list), protein, taxa))
search.close()
#Break here if user not happy with number of accessions?

#FETCH
print("Fetching sequences")
fetch = Entrez.efetch(db='protein', id=ID_list, rettype="fasta")


#PARSE
seq_dict = SeqIO.to_dict(SeqIO.parse(fetch, "fasta"))
fetch.close()
print("Found %s sequences" % len(seq_dict.values()))

#WRITE SEQUENCES TO .FA FILE
print(os.getcwd())
if not os.path.exists('./example_output'):
   os.makedirs('./example_output')

fasta_filename = "./example_output/"+protein+"_"+taxa+".fa"
with open(fasta_filename, "w") as seq_file:
    SeqIO.write(seq_dict.values(), seq_file, "fasta")
#Check output file
print("Saved output as: " + fasta_filename)
linecount = int(subprocess.check_output(["grep", "-c", ">", fasta_filename]).split()[0])
print("\t\t with %s sequences" % linecount)



