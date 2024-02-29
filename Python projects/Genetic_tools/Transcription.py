# Demonstrates functionality of DNA toolkit functions 

import random 

from Genetic_components import * 
from Utilities import colored 
from DNA_toolkit import *

# Generate random DNA string 
DNAsequence = randDNAstr(Nucleotides, 30)
validateSeq(DNAsequence)

# Invalidseq = "AAGGHH"
# print(validateSeq(Invalidseq))




print(f"\nSequence: {DNAsequence}\n")
print(f"[1] Sequence length: {len(DNAsequence)} base pairs")
print(f"[2] Nucleotide frequency: {countNucFrequency(DNAsequence)}")
print(f"[3] RNA transcript: {transcription(DNAsequence)}\n")
print("[4] DNA strand + Complement")
print(f"5' {DNAsequence} 3'")
print(f"   {''.join(['|' for c in range(len(DNAsequence))])}")
print(f"3' {reverse_complement(DNAsequence)} 5'\n")

print(colored(DNAsequence))