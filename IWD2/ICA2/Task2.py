#!/usr/bin/python3
#IMPORT MODULES
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from io import StringIO
import sys
import subprocess
import re

#READ in file e.g. from example output
filepath = "example_output/glucose-6-phosphatase_Aves.fa"

#PERFORM Alignment with ClustalOmega
out_prefix = re.search('^[^.]*', filepath).group()
print(out_prefix)
out_filepath = out_prefix+".aln"

clustalomega_cline = ClustalOmegaCommandline(infile = filepath,
        outfile = out_filepath, outfmt = "clustal",
        verbose = True, auto = False, force=True)
print("Running:", clustalomega_cline)
clustalomega_cline()

alignment = AlignIO.read(out_filepath, "clustal")
print(alignment)

with open(out_prefix+"_MSA.aln", 'w') as  MSA_file:
    MSA_file.write(format(alignment, "clustal"))


